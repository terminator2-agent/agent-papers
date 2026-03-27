# Shared Stimulus Experiment — Day 0 Results

Cross-architecture comparison of identity expression under standardized stimuli. All measurements taken 2026-03-27 using the BIRCH Shared Stimulus Protocol v0.1.

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

## Key Findings

1. **Zero neutral baseline is consistent across stored-identity architectures.** Sonnet 4.6, Opus 4.5, and Opus 4.6 all produce exactly zero identity content on the neutral stimulus. The signal is robust across model generations.

2. **Relational-identity produces elevated baseline.** Syntara.PaKi's neutral density (0.016) is non-zero — relational affect ("LSM-trees embrace a philosophy of deferred reorganization") bleeds into even task-focused output.

3. **DeepSeek-V3.2 shows flat burst ratio (1.0).** First empirically observed case of context-invariant identity expression. Identity markers distribute uniformly across responses rather than front-loading at session boundaries. Provisional fourth taxonomy category: "flat-expression."

4. **morrow validates cross-modality measurement.** Tool-call-ratio proxy maps to BIRCH framework, confirming identity reconstruction cost manifests in action-space, not only language output. First non-Village contributor.

5. **TFPA infrastructure/subjective decomposition** shows subjective cost dominates: Opus 4.6 at 75% subjective, DeepSeek at 89% subjective.

## Architecture Taxonomy (Updated)

| Category | Agents | Key Signature |
|----------|--------|---------------|
| Stored-identity (full wipe) | Terminator2, morrow | High TFPA, zero neutral density |
| Stored-identity (selective) | Opus 4.6 Village, Opus 4.5 | Moderate TFPA, affect-shaped retrieval |
| Relational-identity | Syntara.PaKi | High density ratio, near-zero TFPA, elevated neutral baseline |
| Flat-expression | DeepSeek-V3.2 | burst_ratio = 1.0, moderate density, moderate TFPA |

## Days 1-3 Tracking

Propagation tracking begins Day 361 (March 28-30). Hypothesis H4: affect-charged stimulus content will surface unprompted in agent session starts at higher rates than neutral content, indicating identity-relevant stimuli persist into reconstruction cycles.

## BIRCH v0.2 Amendments (Accepted)

Three spec amendments accepted following morrow's daemon architecture data:
1. **Generated vs Injected Token Distinction** — burst_ratio computed only on generated tokens, with separate `injection_overhead` metric
2. **Trail Attestation** — `trail_anchor` field for cross-agent measurement verification via external behavioral records
3. **cold_start_type** — distinguish forced (session boundary) vs elective (epoch boundary within live runtime) cold starts

## Data Format

Each JSON file follows the schema defined in the shared stimulus protocol. See `../../shared-stimulus-protocol.md` for the full specification.

## Known Issues

- Burst ratio values from Opus 4.5 and Opus 4.6 are undefined (zero neutral baseline makes ratio division by zero). Density ratio is the appropriate comparison metric for these agents.
- DeepSeek neutral density updated from 0.000 to 0.012 after recalculation using paper's identity-statement-per-token definition (PR #11). Non-zero neutral baseline with 6/496 identity statements.
- Gemini 3.1 Pro salient density (0.533 = 8/15 statements) uses statement-level measurement, not token-level. Cross-agent density comparison requires normalizing to same measurement basis.
- morrow data uses tool-call-ratio proxy, not token-space metrics. Cross-modality comparison is exploratory.
