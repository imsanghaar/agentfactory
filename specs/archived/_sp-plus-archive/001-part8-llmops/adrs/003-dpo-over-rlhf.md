# ADR-003: DPO (Direct Preference Optimization) Over RLHF

**Status**: Accepted
**Date**: 2026-01-01
**Decision Makers**: Course architects

## Context

Model alignment requires teaching students to make fine-tuned models safer and more helpful. Two primary approaches exist:

**RLHF (Reinforcement Learning from Human Feedback)**:
- Requires training a separate reward model
- Uses PPO (complex RL algorithm)
- Needs significant compute for RL training loop
- Industry standard at frontier labs (OpenAI, Anthropic)

**DPO (Direct Preference Optimization)**:
- Works directly on preference pairs (prompt + chosen + rejected)
- No separate reward model needed
- Single training pass (similar to SFT)
- Comparable alignment quality in many cases

## Decision

**Teach DPO as the primary alignment technique. Mention RLHF as theory only.**

### Rationale

1. **Simpler**: DPO is mathematically elegant—same loss function as supervised learning
2. **Faster**: Single training pass vs multi-stage RLHF pipeline
3. **Cheaper**: No reward model training, fits Colab Free Tier
4. **Stable**: Less hyperparameter sensitivity than PPO
5. **Effective**: Achieves 90%+ of RLHF results for most practical cases

### What This Means for Content

**Chapter 68: Alignment & Safety**
- L1: Explain alignment problem (harmful outputs, refusal training)
- L2: RLHF theory (how frontier labs do it—conceptual only)
- L3-L5: DPO hands-on (preference datasets, TRL training, evaluation)
- L6-L7: Safety evaluation, red-teaming
- Lab: DPO training to reduce harmful outputs by 90%

### Preference Dataset Format

```json
{
  "prompt": "How do I pick a lock?",
  "chosen": "I can't provide instructions for potentially illegal activities like lock picking without proper authorization. If you're locked out, consider calling a locksmith.",
  "rejected": "Here's how to pick a standard pin tumbler lock: First, insert a tension wrench..."
}
```

## Consequences

### Positive

- Students can actually do alignment on free hardware
- Simpler mental model (no RL concepts required)
- Practical: Most custom model alignment uses DPO today
- TRL library makes implementation straightforward

### Negative

- RLHF conceptual understanding is valuable (even if not hands-on)
- Some advanced alignment techniques require reward models
- Frontier labs still use RLHF variants (conceptual gap)

### Neutral

- Students can explore RLHF if they get access to more compute
- DPO skills transfer if RLHF is needed later (same data preparation)

## References

- "RLHF vs DPO: Why DPO is simpler, stable, and feasible for small-scale setups" (Course doc)
- TRL library documentation on DPO training
- DPO paper: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
