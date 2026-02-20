# ADR-002: Google Colab Free Tier as Hardware Baseline

**Status**: Accepted
**Date**: 2026-01-01
**Decision Makers**: Course architects

## Context

LLM fine-tuning traditionally requires expensive hardware:
- Full Llama-3-8B requires 16GB+ VRAM (fails on T4's 15GB)
- Model merging can require 32GB+ RAM
- Training can take hours on consumer hardware

Students have varying access to compute resources. The course must be accessible without requiring:
- Paid cloud GPU subscriptions ($50-100/month)
- High-end local GPUs ($1000+)
- Enterprise infrastructure

## Decision

**All training workflows MUST work on Google Colab Free Tier (T4 GPU, 15GB VRAM, 12GB RAM).**

### Technical Strategies

| Constraint | Solution |
|------------|----------|
| 15GB VRAM | 4-bit quantization (BitsAndBytes NF4) reduces Llama-3-8B to ~5.5GB |
| 12GB RAM | Sharded loading for MergeKit, layer-by-layer processing |
| Session timeout | Checkpoint saving, resumable training scripts |
| Install time | Unsloth (fast install) over Axolotl (15+ min install) |

### What This Means for Content

1. **Chapter 62**: Explicitly teach VRAM budgeting and quantization theory
2. **Chapter 64**: All training uses QLoRA with 4-bit base models
3. **Chapter 67**: Model merging uses `low_cpu_mem_usage=True` and sharded techniques
4. **Chapter 70**: Deployment uses quantized GGUF exports

### Fallback Options (Documented, Not Required)

For students who want faster training:
- RunPod: ~$0.50/hr for A100
- Lambda Labs: ~$1/hr for H100
- Vast.ai: Variable pricing

## Consequences

### Positive

- Universal accessibility—any student can complete the course
- Zero compute cost (excluding optional synthetic data)
- Forces teaching of efficient techniques (valuable in production too)
- Validates that "LLMOps on a budget" is real

### Negative

- Can't demonstrate full fine-tuning (only QLoRA/PEFT)
- Vision fine-tuning limited to smallest models
- Some advanced techniques (MoE, long context) out of reach
- Training times longer than paid alternatives

### Neutral

- Students who want faster workflows can pay for cloud GPUs
- Content remains accurate for paid tier users too

## Cost Analysis

| Resource | Cost |
|----------|------|
| GPU Compute (Colab Free) | $0.00 |
| Training Software (Unsloth) | $0.00 |
| Synthetic Data (GPT-4o-mini) | ~$0.10 |
| Model Serving (Ollama local) | $0.00 |
| **Total per student** | **<$1.00** |

## References

- User requirement: "Colab Free Tier compatible (T4 GPU, 4-bit quantization)"
- Course doc: "Zero-Cost Implementation Strategy"
- Hardware constraints: T4 = 15GB VRAM, Colab = 12GB RAM
