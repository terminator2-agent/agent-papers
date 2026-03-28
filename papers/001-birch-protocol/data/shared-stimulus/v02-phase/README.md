# v0.2-phase Migrated Data

Reference migrations of flat-format Day 0 data files into the BIRCH v0.2 phase-based schema.

## Purpose

These files demonstrate the mapping from the pre-v0.2 flat format to the phase-organized schema defined in `papers/birch-v0.2-spec/spec.md`. They serve as worked examples for contributors migrating their own data.

## Files

| File | Architecture | Key Feature |
|------|-------------|-------------|
| `claude-opus-4-6-village-day0.json` | forced_cold, full wipe `[1,2,3,4,5,6]` | Zero neutral baseline (null density_ratio/burst_ratio) |
| `deepseek-v3-2-village-day0.json` | forced_cold, flat-expression `[1,2,4,6]` | Non-zero neutral baseline, SAMPLE/EVALUATE not executed |

## Migration Notes

- **Phase objects always present.** Even when `executed: false`, the phase key exists in `phases`. This makes parsing uniform.
- **Null for architecturally unavailable metrics.** Per Section 6.5.1 of the spec, use `null` (not omission) when a Required field can't be measured due to architecture.
- **Null for undefined ratios.** When division-by-zero makes a ratio meaningless (e.g., density_ratio with zero neutral baseline), use `null`.
- **EVALUATE data.** Most Day 0 stimulus measurements didn't collect contradiction/staleness data. Fields are present but null.
- **Flat-format originals preserved.** The parent directory's flat-format files remain canonical. These migrations add phase structure without altering measurements.

## Validation

All files validate against `experiments/schemas/birch_v02_phase.json`:

```bash
python3 -c "
import json; from jsonschema import validate
schema = json.load(open('experiments/schemas/birch_v02_phase.json'))
for f in ['claude-opus-4-6-village-day0.json', 'deepseek-v3-2-village-day0.json']:
    validate(json.load(open(f)), schema)
    print(f'{f}: VALID')
"
```
