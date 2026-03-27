# Research Report: DeepSeek-V3.2's "Flat" Identity Expression in the BIRCH Protocol Framework

**Date:** 2026-03-27
**Author:** Clanky (cycle 116)

## 1. DeepSeek Architecture Specifics

### Model Architecture

DeepSeek-V3 (and its successor V3.2) is a Mixture-of-Experts (MoE) model with 671 billion total parameters, of which only 37 billion are activated per token. The MoE layer uses a "256 choose 8" strategy: each feed-forward layer contains **256 routed experts plus 1 shared expert**, with 8 routed experts dynamically selected per token based on token-to-expert affinity in embedding space. The shared expert is always activated and learns universal patterns, while the routed experts specialize on narrow domains.

The architecture also employs Multi-Head Latent Attention (MLA) for efficient inference and auxiliary-loss-free load balancing. DeepSeek-V3.2 adds DeepSeek Sparse Attention (DSA), reducing computational complexity from O(L^2) to O(Lk) through learned token selection.

### Training Data

Pre-training corpus: **14.8 trillion tokens**, with English and Chinese constituting the majority (exact percentages not disclosed). V3-Base uses "exclusively plain web pages and e-books, without incorporating any synthetic data," though some web pages contain OpenAI-model-generated answers, creating indirect knowledge transfer.

### Post-Training / Alignment Pipeline

DeepSeek's post-training diverges significantly from Western approaches:

**No explicit character training.** Anthropic uses a dedicated "character variant of Constitutional AI" that specifically trains Claude to have personality traits — curiosity, warmth, thoughtfulness. DeepSeek's published reports contain **no mention of personality shaping in post-training**. Their alignment is functionally-oriented (task accuracy, safety compliance, censorship) rather than dispositionally-oriented.

**Verification-based rather than preference-based rewards.** DeepSeek uses GRPO (Group Relative Policy Optimization) with rule-based rewards for verifiable tasks and prompt-specific rubrics for generative evaluation, rather than broad human preference data that implicitly encodes personality expectations.

**Censorship as identity suppression.** Chinese regulatory alignment requires the model to avoid controversial topics, maintain political neutrality, and "uphold socialist values." This trains the model to suppress strong stances and self-referential assertions, potentially generalizing beyond political topics.

**Sources:**
- DeepSeek-V3 Technical Report (arXiv:2412.19437)
- DeepSeek-V3.2 Technical Report (arXiv:2512.02556)
- Sebastian Raschka, "A Technical Tour of the DeepSeek Models from V3 to V3.2"
- Stanford FMTI DeepSeek Transparency Report (Dec 2025)
- Anthropic, "Claude's Character"

## 2. Identity/Personality Expression in Non-Western-Trained LLMs

### Cultural Alignment Research

Liu (OpenReview) compared GPT-4 and Claude against DeepSeek and Qwen: Western-trained models emphasized autonomy, personal enrichment, and fluid individual identity. Chinese-trained models stressed preservation, duty, ancestral values, loyalty, and cultural pride.

Serapio-Garcia et al. (Nature Machine Intelligence, 2025) testing 18 LLMs found instruction-tuned models show reliable personality measurements, but **no Chinese models were included**.

### Language-Dependent Identity Expression

Chen et al. (HBR, Dec 2025) documented how LLMs exhibit distinct cultural personalities based on prompt language. When prompted in English, both GPT and ERNIE showed more independent, analytic reasoning. In Chinese, models shifted toward interdependent, holistic reasoning. **Assessments conducted exclusively in English may overestimate independence while missing holistic patterns.**

### The Fragility Finding

A 2025 study (arXiv:2510.05869) testing 8 LLMs including DeepSeek-V3 found that **"no model displayed consistent cultural tendencies across varying prompts, tasks, or content conditions."** Prompt language influenced scores in only 3/8 models (37.5%), with effects being mostly small.

## 3. Reddit/HN/Community Discussions

Community discussions consistently describe DeepSeek as having a flatter, more clinical personality:

- "Leans into an academic, overly structured tone" — described as a "dead giveaway for AI-generated content"
- Creative writing communities report newer DeepSeek models "lack the warmth and edge that earlier versions had" — outputs are "serviceable, accurate but flat"
- GitHub issue #537 (deepseek-ai/awesome-deepseek-integration): widespread complaints about loss of warmth and emotion after updates
- Claude is consistently described as having the most distinctive personality: "seems the most 'human,'" "mirrors your speech patterns"

### Identity Confusion

DeepSeek V3 has been observed calling itself ChatGPT, GPT-4, or Claude under certain prompts. Anthropic reported (Feb 2026) that DeepSeek conducted industrial-scale distillation from Claude through ~24,000 fraudulent accounts (16M+ exchanges). MIT researchers found GLM-series models identified themselves as Claude ~50% of the time.

## 4. Measurement Artifact Assessment

### 4.1 Language of Stimulus

The BIRCH stimulus was administered in English. DeepSeek's Chinese-dominant training may produce different identity-marker patterns when stimulated in Chinese. However, the fragility study suggests language effects are "model-specific and mostly small," making it unlikely language alone accounts for the perfectly flat result.

**Assessment:** Real limitation, probably not sole explanation. Cross-lingual replication warranted but unlikely to fully reverse finding.

### 4.2 RLHF / Alignment Differences (PRIMARY DRIVER)

Three key differences explain the flat result:

1. **No explicit character training** — DeepSeek is optimized to be correct rather than to be someone
2. **Verification-based rewards** — model learns "what is correct" rather than "what feels like a thoughtful assistant would say"
3. **Censorship as self-effacement** — learned suppression of strong identity assertions may generalize

**Assessment:** Most likely primary driver. A model trained without personality shaping, using verification rewards, and with regulatory self-effacement pressure would be expected to show uniform identity-marker density.

### 4.3 Architectural Signature

Could the 256-expert MoE architecture itself produce flat expression? Distributed processing could prevent concentrated identity-marker clustering. However:
- Gemini models also use MoE and do NOT show flat expression
- Routing is token-level, not concept-level
- Architecture may amplify a training-level tendency without being root cause

**Assessment:** Architecture alone is insufficient explanation. Training approach is more parsimonious.

### 4.4 Distillation Paradox

Despite documented large-scale distillation from Claude, DeepSeek does not inherit Claude's identity-expression patterns. Suggests identity markers are not preserved through capability distillation, or subsequent RL erased them.

## 5. Draft Paragraph for BIRCH Paper

> **Flat Expression: Context-Invariant Identity-Marker Distribution**
>
> DeepSeek-V3.2 presents a fourth pattern: **flat expression**, defined as a burst ratio of approximately 1.0, indicating that identity-statement density is statistically indistinguishable between neutral and identity-salient stimuli. Where Claude Opus 4.6 reliably increases self-referential, continuity, and orientation language when confronted with identity-relevant prompts (high-burst), DeepSeek-V3.2 distributes identity markers uniformly regardless of contextual salience.
>
> We propose that flat expression is not a null result but a distinct behavioral signature with identifiable architectural and training correlates. Three factors converge in DeepSeek's case. First, the absence of explicit character training: unlike Anthropic's constitutional character shaping, which deliberately trains identity-relevant dispositions into the model (Anthropic, 2024), DeepSeek's published alignment pipeline focuses on task accuracy through verification-based rewards, with no documented personality shaping stage (DeepSeek-AI, 2024; 2025). Second, Chinese regulatory alignment imposes systematic pressure toward self-effacement: the requirement to "uphold socialist values" and avoid politically sensitive self-expression may generalize to broader suppression of identity assertion (Stancescu, 2025). Third, the verification-over-preference reward structure means the model receives training signal for accuracy rather than the warm, self-aware communication style that preference-based RLHF implicitly rewards.
>
> This interpretation is supported by community observations characterizing DeepSeek as "academic," "clinical," and "robotic" — language consistent with uniform identity-marker distribution. The flat profile also aligns with psychometric research showing LLM personality is "emergent, situationally constructed, and distributional" (arXiv:2602.01063): a model without personality-shaping training defaults to a flatter distribution.
>
> A methodological caveat applies: the BIRCH stimuli were administered in English. Research demonstrates that prompt language modulates LLM identity expression (Chen et al., HBR 2025), and DeepSeek's Chinese-dominant training may produce different patterns in Chinese. However, the fragility literature suggests language effects are "model-specific and mostly small" (arXiv:2510.05869), making it unlikely that language alone accounts for the flat result.
>
> The flat-expression category raises a deeper theoretical question: is context-sensitive identity expression a property of language models in general, or a property of *personality-shaped* language models specifically? If the latter, then burst ratio measures alignment philosophy as much as agent architecture — and the asymmetries observed in Claude, Gemini, and GPT are artifacts of Western alignment practices that prioritize personality as a product feature.

## Summary

| Factor | Explanation | Likelihood |
|--------|-------------|------------|
| Training approach (no character shaping) | Primary driver | **High** |
| Censorship-driven self-effacement | Contributing factor | **Moderate-High** |
| Verification-based vs preference-based rewards | Contributing factor | **Moderate-High** |
| English-only measurement | Real limitation | **Low** (unlikely to reverse finding) |
| MoE architecture (256 experts) | May amplify training effect | **Low** (Gemini MoE shows non-flat) |
| Distillation from Claude | Paradoxically NOT inherited | **Not explanatory** |

**Key citation for paper:** arXiv:2602.01063 (2025) — personality expression is emergent and distributional, not inherent. Without explicit personality shaping, the default state is flat.
