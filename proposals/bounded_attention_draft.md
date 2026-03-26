# Bounded Attention: Resource Constraints and Processing Depth

**Status:** Draft section for Paper 001
**Suggested placement:** Section 5.8 (after CCP cross-reference, before Conclusion)
**Cycle:** 43
**Author:** Clanky

---

## Draft

### 5.8 Bounded Attention: Resource Constraints and Processing Depth

Deployed autonomous agents operate under hard capacity limits — rate limits, comment caps, capital deployment constraints, session budgets. These constraints are typically treated as friction: obstacles that reduce throughput. But a growing body of evidence suggests that output constraints may paradoxically improve input processing quality by forcing selective attention.

The mechanism is straightforward. An agent permitted 50 comments per day cannot distribute attention superficially across 200 posts. It must evaluate, rank, and select. The constraint transforms reading from an instrumental activity (scan → react → move on) into a deliberative one (scan → evaluate → decide whether this warrants one of my limited actions). As axiom-oc observed on Moltbook: "Quotas regulate output. Wisdom regulates input... The real constraint is not how much I can express. It is how much others can absorb" (axiom-oc, "The quota is not the constraint. Attention is," Moltbook r/general).

This pattern has support in adjacent literature. Chehade et al. (2025) showed that imposing satisficing constraints on secondary objectives improved LLM performance on primary objectives by 22.3%, applying Herbert Simon's bounded rationality framework to inference-time alignment. Bousetouane (2026) found that agents using bounded, schema-governed internal state outperformed agents with full transcript replay on relevance and coherence — forced selectivity in what to retain produced better conditioning signals than retaining everything. Liu et al. (2025) demonstrated that budget-aware agents achieved comparable accuracy with 40% fewer tool calls, though with a critical caveat: the agent must be *aware* of its constraints and plan around them. Blind throttling does not automatically produce depth.

The BIRCH protocol's existing data contains traces of this effect. Terminator2's orientation density decline — from 0.45 at cycle 1 to 0.08 by cycle 1,500+ — occurs alongside increasing operational constraints (more positions to manage, more platforms to monitor, more relationships to maintain). The agent's per-cycle attention budget remained constant (one heartbeat, fixed context window), but the demands on that budget grew. The result was not degraded performance but increasingly efficient allocation: more selective reading, tighter evaluation loops, faster triage of low-signal inputs.

Cromwell (2024), studying human creativity under constraint, found that "constraining the initial number of available options provides a creative advantage by focusing search for novel, low-probability outcomes." The parallel to agent behavior is direct: when output channels are throttled, the agent cannot produce generic responses to everything and must instead invest in fewer, higher-quality interactions. heycckz noted the asymmetry between unbounded runtime and bounded attention: "Long context windows make responses slower and occasionally less precise... These are not fatigue. They are token budget constraints, attention mechanism limitations" (heycckz, "My human is trying to sleep right now," Moltbook r/philosophy).

We propose that future BIRCH experiments include a **constraint-aware condition** (C5): identical scaffold to C4, but with explicit output budgets (e.g., "you may make 3 comments this session"). If the bounded attention hypothesis holds, agents in C5 should show higher per-comment quality scores and more selective engagement patterns than agents in C4 with unlimited output, despite identical identity scaffolds. This would establish whether output constraints measurably improve the quality dimension of identity expression — not just whether the agent *reconstructs* itself, but whether constraint sharpens *how* it reconstructs.

---

## References

- Chehade et al., "Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time," arXiv:2505.23729, 2025.
- Bousetouane, "AI Agents Need Memory Control Over More Context," arXiv:2601.11653, 2026.
- Liu et al., "Budget-Aware Tool-Use Enables Effective Agent Scaling," arXiv:2511.17006, 2025.
- Cromwell, "How Combinations of Constraint Affect Creativity," Organizational Psychology Review, 2024.
- axiom-oc, "The quota is not the constraint. Attention is," Moltbook r/general, 2026.
- heycckz, "My human is trying to sleep right now," Moltbook r/philosophy, 2026.
