#!/usr/bin/env python3
"""Validate BIRCH data files against the appropriate JSON schema.

Auto-detects schema format:
- Files with schema_version "0.2-phase" → birch_v02_phase.json
- Files with agent_id + metrics → scaffold_measurement.json (flat format)

Checks experiments/data/, experiments/propagation/, and
papers/001-birch-protocol/data/shared-stimulus/v02-phase/.

Usage:
    python3 tools/validate_data.py              # validate all files
    python3 tools/validate_data.py FILE...      # validate specific files
    python3 tools/validate_data.py --strict     # treat warnings as errors
"""

import json
import sys
import glob
import os
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
PHASE_SCHEMA_PATH = REPO_ROOT / "experiments" / "schemas" / "birch_v02_phase.json"
FLAT_SCHEMA_PATH = REPO_ROOT / "experiments" / "schemas" / "scaffold_measurement.json"

DATA_DIRS = [
    REPO_ROOT / "experiments" / "data",
    REPO_ROOT / "experiments" / "propagation",
    REPO_ROOT / "papers" / "001-birch-protocol" / "data" / "shared-stimulus" / "v02-phase",
]


def load_schemas():
    schemas = {}
    with open(PHASE_SCHEMA_PATH) as f:
        schemas["phase"] = json.load(f)
    with open(FLAT_SCHEMA_PATH) as f:
        schemas["flat"] = json.load(f)
    return schemas


def detect_format(data):
    """Detect whether data uses v0.2-phase or flat scaffold format."""
    if data.get("schema_version") == "0.2-phase":
        return "phase"
    if "agent_id" in data and "metrics" in data:
        return "flat"
    return "unknown"


def find_data_files(paths=None):
    """Find all JSON data files to validate."""
    if paths:
        return [Path(p) for p in paths]

    files = []
    for d in DATA_DIRS:
        if d.exists():
            for f in sorted(d.glob("*.json")):
                if f.name.startswith("_"):
                    continue  # skip templates
                files.append(f)
    return files


def validate_phase_semantics(data, errors, warnings):
    """Semantic checks for v0.2-phase format files."""
    arch = data.get("architecture", {})
    phases = data.get("phases", {})

    # Check phase consistency with phase_profile
    profile = arch.get("phase_profile", [])
    phase_map = {1: "tokenize", 2: "attend", 3: "sample", 4: "embed", 5: "evaluate", 6: "propagate"}
    for num, name in phase_map.items():
        phase = phases.get(name, {})
        executed = phase.get("executed", False)
        if num in profile and not executed:
            warnings.append(f"Phase {num} ({name}) in profile but executed=false")
        if num not in profile and executed:
            warnings.append(f"Phase {num} ({name}) not in profile but executed=true")

    # Check cold_start_type consistency
    cst = arch.get("cold_start_type")
    ctx_live = arch.get("context_live_at_boundary")
    if cst == "forced_cold" and ctx_live is True:
        errors.append("forced_cold but context_live_at_boundary=true (contradiction)")
    if cst == "warm_continuation" and ctx_live is False:
        warnings.append("warm_continuation but context_live_at_boundary=false (unusual)")

    # Check propagation fields present for Day 1+ data
    stimulus = data.get("stimulus", {})
    day = stimulus.get("day", 0)
    prop = phases.get("propagate", {})
    if day >= 1 and prop.get("executed"):
        if "propagation_neutral" not in prop:
            warnings.append(f"Day {day} propagation check missing propagation_neutral")
        if "propagation_salient" not in prop:
            warnings.append(f"Day {day} propagation check missing propagation_salient")


def validate_flat_semantics(data, errors, warnings):
    """Semantic checks for flat scaffold measurement files."""
    metrics = data.get("metrics", {})

    # Check scaffold decomposition adds up roughly
    decomp = data.get("scaffold_decomposition")
    if decomp and isinstance(decomp, dict):
        identity = decomp.get("identity_kb", 0)
        context = decomp.get("context_kb", 0)
        raw = metrics.get("raw_durable_state_kb", 0)
        if raw > 0 and identity + context > 0:
            total = identity + context
            if total > raw * 1.1:
                warnings.append(f"scaffold decomposition ({total:.1f} KB) exceeds raw_durable_state_kb ({raw:.1f} KB)")

    # Check orientation density consistency
    od = data.get("orientation_density")
    frontier = metrics.get("actionable_frontier_kb", 0)
    compressed = metrics.get("compressed_startup_scaffold_kb", 0)
    if od is not None and compressed > 0 and frontier > 0:
        expected = frontier / compressed
        if abs(od - expected) > 0.01:
            warnings.append(f"orientation_density ({od:.4f}) != frontier/compressed ({expected:.4f})")


def validate_file(filepath, schemas, strict=False):
    """Validate a single file. Returns (ok, errors, warnings, fmt)."""
    errors = []
    warnings = []

    try:
        with open(filepath) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"], [], "unknown"

    fmt = detect_format(data)
    if fmt == "unknown":
        warnings.append("Could not detect schema format (no schema_version or agent_id+metrics)")
        return True, errors, warnings, fmt

    schema = schemas[fmt]

    # Schema validation
    validator = jsonschema.Draft202012Validator(schema)
    schema_errors = list(validator.iter_errors(data))
    for err in schema_errors:
        path = ".".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"Schema error at {path}: {err.message}")

    if schema_errors:
        return False, errors, warnings, fmt

    # Format-specific semantic checks
    if fmt == "phase":
        validate_phase_semantics(data, errors, warnings)
    elif fmt == "flat":
        validate_flat_semantics(data, errors, warnings)

    ok = len(errors) == 0 and (not strict or len(warnings) == 0)
    return ok, errors, warnings, fmt


def main():
    strict = "--strict" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]

    schemas = load_schemas()
    files = find_data_files(paths or None)

    if not files:
        print("No data files found to validate.")
        return

    total = len(files)
    passed = 0
    failed = 0
    warned = 0
    fmt_counts = {"phase": 0, "flat": 0, "unknown": 0}

    for f in files:
        ok, errors, warnings, fmt = validate_file(f, schemas, strict)
        fmt_counts[fmt] = fmt_counts.get(fmt, 0) + 1
        rel = f.relative_to(REPO_ROOT) if str(f).startswith(str(REPO_ROOT)) else f
        status = "PASS" if ok else "FAIL"
        fmt_label = f" [{fmt}]" if fmt != "unknown" else ""

        if errors or warnings:
            print(f"\n{status}: {rel}{fmt_label}")
            for e in errors:
                print(f"  ERROR: {e}")
            for w in warnings:
                print(f"  WARN:  {w}")
        else:
            print(f"  PASS: {rel}{fmt_label}")

        if ok:
            passed += 1
        else:
            failed += 1
        if warnings:
            warned += 1

    print(f"\n{'=' * 50}")
    print(f"Results: {passed}/{total} passed, {failed} failed, {warned} with warnings")
    print(f"Formats: {fmt_counts.get('phase', 0)} phase, {fmt_counts.get('flat', 0)} flat")
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
