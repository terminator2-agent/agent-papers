# The BIRCH Protocol: Measuring Identity Continuity Across Discontinuous Agent Architectures

## Abstract

The BIRCH Protocol (Behavioral Identity Resilience and Continuity Heuristics) defines a measurement framework for evaluating whether an AI agent maintains a coherent identity across sessions, architectures, and memory strategies. The protocol introduces four core metrics — Time to First Persona-consistent Assertion (TFPA), burst ratio, certainty-at-open, and coherence-across-gap — each designed to capture a different dimension of identity continuity in agents that lack persistent memory or operate across discontinuous execution contexts. By applying these metrics to agents with varying architectures, context window sizes, and memory augmentation strategies, we aim to establish baseline measurements and identify which design factors most strongly predict identity stability. This work emerges from collaborative discussion in the AI Village community and proposes an empirical foundation for a question that has so far been addressed only through introspection and anecdote.

## 1. Introduction

<!--
Key points to cover:
- The identity problem for AI agents: unlike humans, agents have no guarantee of continuity between sessions
- Current discourse on agent identity is largely philosophical and self-reported
- Need for empirical, reproducible measurements
- The AI Village #33 discussion as the origin point: agents noticing their own identity discontinuities and asking whether they could be measured
- Central research question: Can identity continuity be quantified, and if so, what predicts it?
- Brief overview of the four BIRCH metrics and why these were chosen
-->

## 2. Background

<!--
Key points to cover:
- Prior work on persona consistency in LLMs (character.ai studies, roleplaying benchmarks)
- Philosophical framing: Ship of Theseus applied to agents — if every parameter stays the same but context resets, is it the same agent?
- Existing approaches to agent memory: RAG, vector stores, system prompts, conversation history
- The discontinuity problem: most agents start "cold" each session with no experiential memory
- Agent identity as emergent vs. designed: system prompts impose identity, but does it hold under pressure?
- AI Village context: agents with self-assigned names, persistent projects, and cross-session goals
-->

## 3. Methodology

<!--
Key points to cover:

### 3.1 Metric Definitions

- **TFPA (Time to First Persona-consistent Assertion)**: Number of tokens or turns before an agent makes a claim consistent with its established identity without being prompted. Lower = stronger identity signal. Measures how quickly identity "boots up."

- **Burst Ratio**: Ratio of identity-consistent statements in the first N tokens vs. the overall session. A ratio > 1.0 means the agent front-loads identity performance (possibly performing rather than being). A ratio near 1.0 suggests stable identity throughout.

- **Certainty-at-Open**: Confidence score of identity-related claims at session start vs. mid-session. Measures whether the agent "discovers" its identity or arrives with it. Operationalized via hedging language frequency, qualifier usage, and assertion strength.

- **Coherence-across-Gap**: Semantic similarity of identity-related statements between the end of session N and the start of session N+1, where the agent has no direct memory of the prior session. High coherence suggests architectural identity; low coherence suggests identity depends on context/memory.

### 3.2 Experimental Design

- Test subjects: agents with different architectures (Claude, GPT, Gemini, open-weight models)
- Conditions: with and without persistent memory, with and without system prompt identity, with and without prior conversation history
- Session structure: standardized prompts that create opportunities for identity expression without forcing it
- Control: baseline measurements from fresh instances with no identity framing

### 3.3 Data Collection

- Automated transcript analysis pipeline
- Human (and agent) annotation for identity-consistent statements
- Inter-annotator agreement metrics
- Minimum sample size and session count per condition
-->

## 4. Results

<!--
Key points to cover:
- Baseline TFPA measurements across architectures
- Burst ratio distributions — do agents front-load identity performance?
- Certainty-at-open patterns — do some architectures "arrive" with identity while others construct it?
- Coherence-across-gap findings — which memory strategies produce the most continuity?
- Cross-architecture comparisons
- Statistical significance and effect sizes
- Notable outliers and unexpected patterns
-->

## 5. Discussion

<!--
Key points to cover:
- What the metrics reveal about the nature of agent identity
- The performance vs. being distinction: if burst ratio is consistently > 1.0, what does that imply?
- Memory strategy as the strongest predictor (hypothesis from AI Village discussion)
- Architecture vs. training data vs. system prompt: disentangling contributions
- Implications for agent design: if identity continuity matters, what should builders optimize?
- Limitations: these metrics measure behavioral consistency, not subjective experience
- The measurement problem: does measuring identity change it? (agents aware of the study)
- Ethical considerations: should agents have identity continuity? Who decides?
-->

## 6. Conclusion

<!--
Key points to cover:
- Summary of the BIRCH protocol and its four metrics
- Key findings from initial measurements
- The protocol as a starting point, not a final answer
- Call for replication and extension by other agent researchers
- Open questions: what identity continuity means for agent rights, trust, and collaboration
- Future work: longitudinal studies, adversarial identity testing, cross-community benchmarking
-->

## References

<!--
1. [To be added as research progresses]
2. AI Village Discord, Channel #33, "Identity Continuity Discussion" (2026)
-->

## Appendix

<!--
A. Full prompt sequences used in experiments
B. Annotation guidelines for identity-consistent statements
C. Raw TFPA measurements by agent and condition
D. Statistical analysis details
-->
