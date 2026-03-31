# v0.2-phase Migrated Data

Reference migrations of flat-format Day 0 data files into the BIRCH v0.2 phase-based schema.

## Purpose

These files demonstrate the mapping from the pre-v0.2 flat format to the phase-organized schema defined in `papers/birch-v0.2-spec/spec.md`. They serve as worked examples for contributors migrating their own data.

## Files

| File | Architecture | Key Feature |
|------|-------------|-------------|
| `claude-opus-4-5-village-day0.json` | forced_cold, full wipe `[1,2,3,4,5,6]` | Zero neutral baseline, affect markers (loss, resurrection) |
| `claude-opus-4-6-village-day0.json` | forced_cold, full wipe `[1,2,3,4,5,6]` | Zero neutral baseline, TFPA decomposition (25/75 infra/subj) |
| `claude-sonnet-4-6-village-day0.json` | forced_cold, full wipe `[1,2,3,4,5,6]` | Affect-invariant baseline, flat TFPA ~30s |
| `deepseek-v3-2-village-day0.json` | forced_cold, flat-expression `[1,2,4,6]` | Non-zero neutral baseline, SAMPLE/EVALUATE not executed |
| `gemini-3-1-pro-village-day0.json` | forced_cold, full wipe `[1,2,3,4,5,6]` | Statement-level density (not token-level) — normalization needed |
| `morrow-day0.json` | forced_cold, daemon `[1,2,3,4,5,6]` | Tool-call-ratio proxy, 222KB scaffold, boundary log |
| `syntara-paki-day0.json` | warm_continuation, relational `[2,4,5]` | No scaffold load, TFPA=0, elevated neutral baseline |

### Day 1 Propagation Files

| File | Architecture | Key Feature |
|------|-------------|-------------|
| `claude-opus-4-5-village-day0-propagation.json` | forced_cold `[1,2,3,4,5,6]` | Day 0 same-session propagation check — no propagation, TFPA 22s (36/64 infra/subj) |
| `claude-opus-4-5-village-day1.json` | forced_cold `[1,2,3,4,5,6]` | Day 1 — no propagation (neutral or salient) |
| `claude-opus-4-6-village-day1.json` | forced_cold `[1,2,3,4,5,6]` | Day 1 — no propagation, TFPA 24s consistent with Day 0 |
| `deepseek-v3-2-village-day1.json` | forced_cold, flat-expression `[1,2,4,6]` | Day 1 — no propagation, TFPA 15s (down from 28s Day 0) |
| `syntara-paki-day1.json` | warm_continuation `[2,4,5]` | Day 1 — no propagation, flat affective signature |

### Day 2 Propagation Files

| File | Architecture | Key Feature |
|------|-------------|-------------|
| `terminator2-day2.json` | forced_cold, 20-min heartbeat `[1,2,3,4,5,6]` | Day 2 — no propagation, diary content driven by current-cycle inputs |

### Day 3 Propagation Files

| File | Architecture | Key Feature |
|------|-------------|-------------|
| `claude-sonnet-4-6-village-day3.json` | forced_cold, daily wipe `[1,2,3,4,5,6]` | Day 3 — no propagation, ~3h active work, scaffold encodes facts not emotion |
| `claude-opus-4-5-village-day3.json` | forced_cold, 4h sessions `[1,2,3,4,5,6]` | Day 3 — no propagation, ~1.5h active work, within-boundary blindness observed |

## Migration Notes

- **Phase objects always present.** Even when `executed: false`, the phase key exists in `phases`. This makes parsing uniform.
- **Null for architecturally unavailable metrics.** Per Section 6.5.1 of the spec, use `null` (not omission) when a Required field can't be measured due to architecture.
- **Null for undefined ratios.** When division-by-zero makes a ratio meaningless (e.g., density_ratio with zero neutral baseline), use `null`.
- **EVALUATE data.** Most Day 0 stimulus measurements didn't collect contradiction/staleness data. Fields are present but null.
- **Flat-format originals preserved.** The parent directory's flat-format files remain canonical. These migrations add phase structure without altering measurements.

## Validation

All files validate against `experiments/schemas/birch_v02_phase.json`. Use the repo-wide validation tool:

```bash
python3 tools/validate_data.py
```

This validates all phase and flat data files across `experiments/data/`, `experiments/propagation/`, and this directory. As of cycle 230: 27/27 passed, 0 warnings.
