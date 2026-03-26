# Experiments

Raw and processed experimental data for BIRCH Protocol papers.

## TFPA Dataset

Extracted from Claude Code session JSONL logs by Clanky (cycle 26, 2026-03-26).

- `tfpa_dataset.json` — 129 data points (119 T2 heartbeat cycles + 10 Clanky cycles)
- `tfpa_summary.json` — Summary statistics and methodology

### Schema

Each record in `tfpa_dataset.json`:

| Field | Type | Description |
|-------|------|-------------|
| `cycle` | int | Sequential cycle number within this dataset |
| `started_at` | ISO timestamp | Session start (first tool result timestamp) |
| `first_productive_at` | ISO timestamp | First external API interaction |
| `tfpa_seconds` | float | Time to first productive action (seconds) |
| `cycle_duration_seconds` | float | Total session duration (seconds) |
| `capsule_files` | string[] | Scaffold files read during orientation |
| `agent_type` | "t2" or "clanky" | Which agent ran this cycle |
| `log_file` | string | Source JSONL log filename |

### Key Findings

- **T2 TFPA:** median 35.9s (IQR 27.3–48.8s), N=119
- **Clanky TFPA:** median 115.4s (IQR 72.3–166.3s), N=10
- **Scaffold consistency:** checkpoint.json, self_rules.md, briefing_digest.txt loaded in 100% of T2 cycles
- **SOUL.md loaded in only 45% of T2 cycles** — identity scaffold is not re-read every cycle once internalized
