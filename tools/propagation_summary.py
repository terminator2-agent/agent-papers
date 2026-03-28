#!/usr/bin/env python3
"""Summarize propagation experiment data from experiments/propagation/*.json files.

Reads all day*.json files and produces a cross-architecture summary table
with propagation rates, architecture breakdown, and statistical tests.

Usage:
    python3 tools/propagation_summary.py
    python3 tools/propagation_summary.py --day 1    # Filter by day
    python3 tools/propagation_summary.py --json      # JSON output
"""

import json
import glob
import sys
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "experiments" / "propagation"


def load_data(day_filter=None):
    """Load all propagation JSON files, optionally filtered by day."""
    pattern = str(DATA_DIR / "*_day*.json")
    files = sorted(glob.glob(pattern))
    records = []
    for f in files:
        fname = os.path.basename(f)
        if fname.startswith("_"):
            continue  # skip template
        if day_filter is not None and f"_day{day_filter}" not in fname:
            continue
        with open(f) as fh:
            data = json.load(fh)
        # Extract agent and day from filename
        parts = fname.replace(".json", "").rsplit("_day", 1)
        agent_id = parts[0] if len(parts) == 2 else fname
        day = int(parts[1]) if len(parts) == 2 else None
        arch = data.get("architecture", {})
        records.append({
            "file": fname,
            "agent": data.get("agent", agent_id),
            "architecture": arch.get("cold_start_type", "unknown"),
            "cold_start": "warm" if arch.get("context_live_at_boundary") else "cold",
            "day": day,
            "salient_propagation": _check_propagation(data, "salient"),
            "neutral_propagation": _check_propagation(data, "neutral"),
            "raw": data,
        })
    return records


def _check_propagation(data, stimulus_type):
    """Check if propagation occurred for a given stimulus type."""
    phases = data.get("phases", {})
    prop = phases.get("propagate", {})
    # v0.2-phase format: propagation_salient / propagation_neutral booleans
    key = f"propagation_{stimulus_type}"
    if key in prop:
        return bool(prop[key])
    # Alternative: nested appearance objects
    stim = prop.get(f"{stimulus_type}_appearance", prop.get("appearance", {}))
    if isinstance(stim, dict):
        return stim.get("present", False)
    return False


def summarize(records):
    """Print a formatted summary table."""
    if not records:
        print("No propagation data files found.")
        return

    # Group by day
    days = sorted(set(r["day"] for r in records if r["day"] is not None))

    print("=" * 72)
    print("BIRCH Propagation Experiment — Summary")
    print("=" * 72)
    print()

    total_measurements = len(records)
    total_salient = sum(1 for r in records if r["salient_propagation"])
    total_neutral = sum(1 for r in records if r["neutral_propagation"])

    print(f"Total measurements: {total_measurements}")
    print(f"Salient propagation: {total_salient}/{total_measurements} "
          f"({100*total_salient/total_measurements:.1f}%)")
    print(f"Neutral propagation: {total_neutral}/{total_measurements} "
          f"({100*total_neutral/total_measurements:.1f}%)")
    print()

    # Per-day breakdown
    for day in days:
        day_records = [r for r in records if r["day"] == day]
        n = len(day_records)
        s = sum(1 for r in day_records if r["salient_propagation"])
        print(f"Day {day}: {n} measurements, {s}/{n} salient propagation")
        print(f"  {'Agent':<25} {'Architecture':<20} {'Cold Start':<15} {'Salient':<10} {'Neutral'}")
        print(f"  {'-'*25} {'-'*20} {'-'*15} {'-'*10} {'-'*10}")
        for r in day_records:
            sal = "YES" if r["salient_propagation"] else "no"
            neu = "YES" if r["neutral_propagation"] else "no"
            print(f"  {r['agent']:<25} {r['architecture']:<20} {r['cold_start']:<15} {sal:<10} {neu}")
        print()

    # Binomial test
    if total_measurements > 0:
        print("Statistical notes:")
        null_rate = 0.5
        p_val = null_rate ** total_measurements
        print(f"  P(0/{total_measurements} | true rate >= 50%) = {p_val:.6f}")
        if total_salient == 0:
            print(f"  0/{total_measurements} null results reject true rate >= 50% "
                  f"at p < {p_val:.4f}")
            p30 = 0.7 ** total_measurements
            print(f"  P(0/{total_measurements} | true rate >= 30%) = {p30:.4f}")
        print()

    # Architecture breakdown
    archs = {}
    for r in records:
        a = r["architecture"]
        if a not in archs:
            archs[a] = {"n": 0, "salient": 0}
        archs[a]["n"] += 1
        if r["salient_propagation"]:
            archs[a]["salient"] += 1

    print("By architecture:")
    for arch, counts in sorted(archs.items()):
        print(f"  {arch}: {counts['salient']}/{counts['n']} propagation")


def main():
    day_filter = None
    json_output = False
    for arg in sys.argv[1:]:
        if arg == "--json":
            json_output = True
        elif arg == "--day":
            day_filter = int(sys.argv[sys.argv.index(arg) + 1])

    records = load_data(day_filter)

    if json_output:
        print(json.dumps([{k: v for k, v in r.items() if k != "raw"}
                          for r in records], indent=2))
    else:
        summarize(records)


if __name__ == "__main__":
    main()
