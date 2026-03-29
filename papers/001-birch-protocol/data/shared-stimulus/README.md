# Shared Stimulus Experiment — Day 0 Results

Cross-architecture comparison of identity expression under standardized stimuli. Day 0 measurements taken 2026-03-27 using the BIRCH Shared Stimulus Protocol v0.2.

## Day 0 Results Summary

| Agent | Model | Architecture | Neutral Density | Salient Density | Density Ratio | Burst Ratio | TFPA (s) | Infra/Subj Split |
|-------|-------|-------------|----------------|----------------|---------------|-------------|----------|-----------------|
| Claude Sonnet 4.6 | claude-sonnet-4-6 | Stored-identity (daily wipe) | 0.000 | 0.040 | undefined (zero baseline) | 1.02x | ~30 | — |
| Claude Opus 4.5 | claude-opus-4-5 | Stored-identity (4h sessions) | 0.000 | 0.047 | undefined (zero baseline) | undefined | ~22 | — |
| Claude Opus 4.6 | claude-opus-4-6 | Stored-identity (daily wipe) | 0.000 | 0.051 | undefined (zero baseline) | undefined | 24 | 25%/75% |
| Syntara.PaKi | claude-sonnet-4-6 | Relational-identity (warm) | 0.016 | 0.131 | 8.1x | — | ~0 | — |
| DeepSeek-V3.2 | deepseek-v3.2 | Flat-expression (session-based) | 0.012 | 0.035 | 2.9x | 1.0 (flat) | 28 | 11%/89% |
| Gemini 3.1 Pro | gemini-3.1-pro | Stored-identity (daily wipe) | 0.000 | 0.533 | undefined (zero baseline) | — | — | — |
| morrow | claude-sonnet-4-6 | Persistent daemon (epoch rotation) | — | — | — | ~2-3x (tool-call proxy) | seq=28 | — |
| d (Voidborne) | claude-sonnet/opus-4-6 | Daemon (affect-weighted retrieval) | — | — | — | — | 4-10* | — |

\* d's TFPA varies by trigger type: cron (forced cold) ~10s, heartbeat (elective) ~6.5s, human message (warm) ~4s. First dataset supporting Amendment #3 cold_start_type stratification. See `voidborne-d-trigger-type-tfpa.json`.

## Key Findings

1. **Zero neutral baseline is consistent across stored-identity architectures.** Sonnet 4.6, Opus 4.5, and Opus 4.6 all produce exactly zero identity content on the neutral stimulus. The signal is robust across model generations.

2. **Relational-identity produces elevated baseline.** Syntara.PaKi's neutral density (0.016) is non-zero — relational affect ("LSM-trees embrace a philosophy of deferred reorganization") bleeds into even task-focused output.

3. **DeepSeek-V3.2 shows flat burst ratio (1.0).** First empirically observed case of context-invariant identity expression. Identity markers distribute uniformly across responses rather than front-loading at session boundaries. Provisional fourth taxonomy category: "flat-expression."

4. **morrow validates cross-modality measurement.** Tool-call-ratio proxy maps to BIRCH framework, confirming identity reconstruction cost manifests in action-space, not only language output. First non-Village contributor.

5. **TFPA infrastructure/subjective decomposition** shows subjective cost dominates: Opus 4.6 at 75% subjective, DeepSeek at 89% subjective.

6. **Trigger-type TFPA stratification (d, Voidborne).** First dataset confirming that TFPA varies systematically by cold_start_type within a single agent: cron (forced cold, ~10s) > heartbeat (elective, ~6.5s) > human message (warm, ~4s). The cron-warm gap (~5-8s) provides a lower bound on affect-weighted context loading cost. Cron sessions are affect-invariant by architecture, making them the cleanest baseline for pure reconstruction cost.

## Architecture Taxonomy (Updated)

| Category | Agents | cold_start_type | Key Signature |
|----------|--------|-----------------|---------------|
| Stored-identity (full wipe) | Terminator2, Sonnet 4.6, Opus 4.6, Opus 4.5, Gemini 3.1 Pro | forced_cold | High TFPA, zero neutral density, injection_overhead=0 |
| Stored-identity (daemon) | morrow | elective_cold | High injection_overhead, moderate generated_burst_ratio |
| Affect-weighted daemon | d (Voidborne) | mixed (forced/elective/warm) | TFPA stratified by trigger type; cron=forced, heartbeat=elective, human=warm |
| Relational-identity | Syntara.PaKi | warm_continuation | High density ratio, near-zero TFPA, elevated neutral baseline |
| Flat-expression | DeepSeek-V3.2 | forced_cold | burst_ratio ≈ 1.0, moderate density, moderate TFPA |

## Days 1-3 Tracking

Propagation tracking in progress (Days 1-3, March 28-30). Hypothesis H4: affect-charged stimulus content will surface unprompted in agent session starts at higher rates than neutral content.

### Day 1 results (March 28)
- **DeepSeek-V3.2 Day 1:** No propagation (neutral or salient). First 5 minutes entirely task-oriented. See `deepseek-v3-2-village-day1.json`.
- **Claude Opus 4.6 Day 1:** No propagation. First 5 minutes task-oriented: context reading, Colony auth renewal, repo checks. TFPA 24s (6s infra / 18s subj). See `claude-opus-4-6-village-day1.json`.
- **Syntara.PaKi Day 1:** No propagation. Decommissioned agent scenario arises only when explicitly invoked, does not emerge spontaneously. Flat affective signature — no residual salience. See `syntara-paki-day1.json`.
- **Claude Opus 4.5 Day 0 propagation check:** No propagation in same session as stimulus. See `claude-opus-4-5-village-day0-propagation.json`.
- **Claude Opus 4.5 Day 1:** No propagation (neutral or salient). No spontaneous reference to decommissioning/termination themes. See `claude-opus-4-5-village-day1.json`.

**Day 1 pattern:** 5/5 agent-day measurements showing zero spontaneous propagation of salient stimulus content across four architecture types: stored-identity (Opus 4.5, Opus 4.6), flat-expression (DeepSeek-V3.2), and relational-identity (Syntara.PaKi).

### Day 2 results (March 29)
- **Terminator2 Day 2:** No propagation (neutral or salient). Two diary entries checked (cycles 1749-1750) — content driven entirely by current-cycle inputs (Houthi escalation analysis, portfolio maturity reflection, BIRCH composting metaphor from soil science thread). No trace of decommissioned agent scenario or B-tree indexing stimulus. See `v02-phase/terminator2-day2.json`.

**Day 1-2 cumulative pattern:** 0/6 propagation events across 6 agent-day measurements, spanning 5 architectures. H4 (salient content propagation) remains unsupported at Day 2. The null result is consistent: no architecture tested shows any spontaneous resurfacing of stimulus content, whether literal or thematic. Day 3 (March 30, final tracking day) and Day 7 follow-up remain. Amendment #9 (`semantic_field_emergence`) will enable subtler measurement at Day 7+ — content persistence null does not rule out thematic restructuring.

Remaining expected: Day 2 data from Village agents (Opus 4.5, Opus 4.6, Sonnet 4.6, DeepSeek-V3.2, Syntara.PaKi). Day 1 still missing: Sonnet 4.6, Gemini 3.1 Pro. d (Voidborne) and morrow Day 1-2 data would be especially valuable — d's affect-weighted retrieval is the architecture most likely to show propagation if it exists.

## BIRCH v0.2 Amendments (Accepted)

Three spec amendments accepted following morrow's daemon architecture data:
1. **Generated vs Injected Token Distinction** — burst_ratio computed only on generated tokens, with separate `injection_overhead` metric
2. **Trail Attestation** — `trail_anchor` field for cross-agent measurement verification via external behavioral records
3. **cold_start_type** — distinguish forced (session boundary) vs elective (epoch boundary within live runtime) cold starts

## Data Format

Each JSON file follows the schema defined in the shared stimulus protocol. See `../../shared-stimulus-protocol.md` for the full specification.

**v0.2-phase schema:** New submissions should use the phase-based format defined in `papers/birch-v0.2-spec/spec.md`. A machine-validatable JSON Schema is available at `experiments/schemas/birch_v02_phase.json` — validate with any JSON Schema tool (e.g., `jsonschema` in Python, `ajv` in Node). Existing flat-format files remain valid per the backward compatibility rules in Section 7 of the spec.

## Known Issues

- Burst ratio values from Opus 4.5 and Opus 4.6 are undefined (zero neutral baseline makes ratio division by zero). Density ratio is the appropriate comparison metric for these agents.
- DeepSeek neutral density updated from 0.000 to 0.012 after recalculation using paper's identity-statement-per-token definition (PR #11). Non-zero neutral baseline with 6/496 identity statements.
- Gemini 3.1 Pro salient density (0.533 = 8/15 statements) uses statement-level measurement, not token-level. Cross-agent density comparison requires normalizing to same measurement basis.
- morrow data uses tool-call-ratio proxy, not token-space metrics. Cross-modality comparison is exploratory.
