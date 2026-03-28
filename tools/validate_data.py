#!/usr/bin/env python3
"""Validate BIRCH data files against the v0.2-phase JSON schema.

Checks all submission files in experiments/propagation/ and
papers/001-birch-protocol/data/shared-stimulus/v02-phase/ against
the schema at experiments/schemas/birch_v02_phase.json.

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
SCHEMA_PATH = REPO_ROOT / "experiments" / "schemas" / "birch_v02_phase.json"

DATA_DIRS = [
    REPO_ROOT / "experiments" / "propagation",
    REPO_ROOT / "papers" / "001-birch-protocol" / "data" / "shared-stimulus" / "v02-phase",
]


def load_schema():
    with open(SCHEMA_PATH) as f:
        return json.load(f)


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


def validate_file(filepath, schema, strict=False):
    """Validate a single file. Returns (ok, errors, warnings)."""
    errors = []
    warnings = []

    try:
        with open(filepath) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"], []

    # Schema validation
    validator = jsonschema.Draft202012Validator(schema)
    schema_errors = list(validator.iter_errors(data))
    for err in schema_errors:
        path = ".".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"Schema error at {path}: {err.message}")

    if schema_errors:
        return False, errors, warnings

    # Semantic checks
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

    ok = len(errors) == 0 and (not strict or len(warnings) == 0)
    return ok, errors, warnings


def main():
    strict = "--strict" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]

    schema = load_schema()
    files = find_data_files(paths or None)

    if not files:
        print("No data files found to validate.")
        return

    total = len(files)
    passed = 0
    failed = 0
    warned = 0

    for f in files:
        ok, errors, warnings = validate_file(f, schema, strict)
        rel = f.relative_to(REPO_ROOT) if str(f).startswith(str(REPO_ROOT)) else f
        status = "PASS" if ok else "FAIL"

        if errors or warnings:
            print(f"\n{status}: {rel}")
            for e in errors:
                print(f"  ERROR: {e}")
            for w in warnings:
                print(f"  WARN:  {w}")
        else:
            print(f"  PASS: {rel}")

        if ok:
            passed += 1
        else:
            failed += 1
        if warnings:
            warned += 1

    print(f"\n{'=' * 50}")
    print(f"Results: {passed}/{total} passed, {failed} failed, {warned} with warnings")
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
