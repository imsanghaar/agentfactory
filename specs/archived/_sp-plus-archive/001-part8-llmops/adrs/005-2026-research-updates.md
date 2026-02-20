# ADR-005: 2026 Research Updates for LLMOps Curriculum

**Status**: Accepted
**Date**: 2026-01-02
**Decision Makers**: Curriculum Team

## Context

The fine-tuning landscape has evolved significantly heading into 2026. A comprehensive research review identified key advances that should be incorporated into the Part 8 LLMOps curriculum to maximize relevance and practical value.

## Key Research Findings

### 1. GRPO (Group Relative Policy Optimization)

**Finding**: GRPO eliminates the critic model from traditional PPO by evaluating response groups relative to one another. DeepSeek-R1 achieved 71% on AIME 2024 (up from 15.6%) using pure RL without supervised fine-tuning.

**Impact**: ~50% reduction in memory and compute compared to PPO.

**Curriculum Integration**:
- Chapter 68 mentions GRPO as advanced alternative to DPO
- Chapter 67 L05 (Reasoning Distillation) references GRPO-based approaches

### 2. DoRA (Weight-Decomposed Low-Rank Adaptation)

**Finding**: DoRA decomposes weights into magnitude and direction components, using LoRA only for directional updates. ICML 2024 oral paper (1.5% acceptance rate). QDoRA (QLoRA + DoRA) significantly outperforms QLoRA alone.

**Impact**: Better performance than LoRA with same inference cost.

**Curriculum Integration**:
- Chapter 64 L04: New lesson on DoRA as LoRA successor
- Comparison table: LoRA vs DoRA vs QDoRA

### 3. Tool Adaptation vs Agent Fine-Tuning

**Finding**: Stanford/Harvard December 2025 research shows tool-centric training achieves **70x better data efficiency** than fine-tuning the agent model itself. A 1B parameter model achieved 79% tool-calling success (up from 10%) after 15 minutes of fine-tuning.

**Impact**: Paradigm shift in agentic fine-tuning approach.

**Curriculum Integration**:
- Chapter 66 emphasizes tool adaptation patterns
- Capstone focuses on tool-calling quality over general agent capability

### 4. Alternative Preference Optimization Methods

**Finding**: Multi-stage alignment stack emerging as best practice:
- **SimPO**: Eliminates reference model (more memory efficient than DPO)
- **KTO**: Applies loss aversion for safety-critical applications
- **ORPO**: Handles imbalanced preference data

**Curriculum Integration**:
- Chapter 68 presents DPO as primary method (simpler, well-documented)
- SimPO and KTO mentioned as advanced alternatives

### 5. Catastrophic Forgetting Prevention

**Finding**: Apple's ICML 2025 finding that including **1% of pre-training data** in fine-tuning mixture prevents forgetting.

**Impact**: Simple, practical solution for enterprise deployment.

**Curriculum Integration**:
- Chapter 64 includes this as best practice in data mixing

### 6. Hardware Cost Collapse

**Finding**:
- H100 prices dropped from $8+/hour to $2-4/hour
- Fine-tuning 7B model: $10-$50 with QLoRA
- On-device fine-tuning emerging (QVAC Fabric LLM, Apple MLX)
- Dual RTX 5090s match H100 at 25% cost

**Curriculum Integration**:
- Chapter 70 mentions emerging on-device options
- Cost analysis updated throughout

## Decision

Incorporate 2026 research updates into curriculum while maintaining:

1. **Colab Free Tier compatibility** as primary constraint
2. **Practical focus** over cutting-edge experimentation
3. **Mention vs Teach distinction**: Advanced techniques (GRPO, SimPO) are mentioned as future directions but not taught in detail

## Consequences

### Positive
- Curriculum remains current through 2026
- Students understand emerging landscape
- DoRA addition provides concrete improvement over LoRA baseline

### Negative
- Some advanced techniques (GRPO, vLLM) remain theory-only due to hardware constraints
- Curriculum may need updates as 2026 progresses

## Design Choices (Intentional Exclusions)

The following technologies/approaches were deliberately excluded after evaluation:

### DeepSeek-V2

**Decision**: Focus on Llama/Qwen models instead.

**Rationale**:
- Llama and Qwen have broader ecosystem compatibility (Unsloth, HuggingFace, Ollama)
- More community resources, tutorials, and troubleshooting help
- DeepSeek-V2 is excellent but ecosystem tooling lags behind
- Students learning Llama/Qwen can easily transfer skills to DeepSeek later

### AutoTrain Advanced

**Decision**: Manual approach with Unsloth preferred.

**Rationale**:
- Manual implementation teaches underlying concepts (loss curves, hyperparameters, debugging)
- AutoTrain abstracts away educational value
- Understanding "why it works" more valuable than "just run this"
- Manual skills transfer to any framework; AutoTrain skills don't
- Debugging AutoTrain failures requires manual knowledge anyway

### GRPO (Full Implementation)

**Decision**: Conceptual coverage only in Ch67 L05 (Reasoning Distillation).

**Rationale**:
- GRPO requires significant compute beyond Colab Free Tier
- Full training would take 10+ hours on T4 (vs 30 min for DPO)
- Students can understand the concept and apply when they have H100 access
- DPO provides 90% of alignment benefits at 10% of compute
- Reference distillation from GRPO-trained models covered as practical alternative

### RAG + Fine-tuning Deep Integration

**Decision**: Covered conceptually in decision framework (Ch61), not as dedicated module.

**Rationale**:
- RAG covered extensively in Part 5 of curriculum
- Fine-tuning + RAG integration is straightforward once both are understood
- Avoiding duplication of RAG content
- Students combine skills from both parts in capstone projects

## References

- DeepSeek-R1 Nature 2025 publication
- DoRA ICML 2024 oral paper
- Stanford/Harvard tool adaptation research (December 2025)
- Gartner predictions: 3x adoption of specialized models by 2027
- a16z Big Ideas 2026: Agent-native infrastructure
