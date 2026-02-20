# ADR-001: Platform-Agnostic Design for LLMOps Content

**Status**: Accepted
**Date**: 2026-01-01
**Decision Makers**: Course architects

## Context

The original Part 8 README referenced "Turing Platform" as the primary managed LLMOps workflow. However, the user explicitly requested platform-agnostic content that doesn't depend on a single platform.

Students need to understand LLMOps concepts that transfer across:
- Open-source tools (Unsloth, HuggingFace, Ollama)
- Managed platforms (AWS Bedrock, Azure AI Studio, Together AI)
- Enterprise solutions (Turing, custom infrastructure)

## Decision

**Teach concepts using open-source implementations, then show how managed platforms abstract this.**

### Implementation Approach

| Concept | Primary Tool (Open-Source) | Managed Alternative (Mentioned) |
|---------|---------------------------|--------------------------------|
| Fine-tuning | Unsloth + HuggingFace | AWS Bedrock, Azure AI Studio |
| Quantization | BitsAndBytes | Managed inference auto-handling |
| Model serving | Ollama, vLLM | Together AI, Fireworks, Modal |
| Evaluation | LLM-as-a-Judge + TRL | LangSmith, W&B |
| Alignment | TRL DPO | OpenAI fine-tuning, Anthropic CAI |

### Content Pattern

1. **Explain the concept** (what problem it solves)
2. **Show open-source implementation** (hands-on with Unsloth/Ollama)
3. **Mention managed alternatives** ("If you prefer managed, platforms like X handle this automatically")
4. **Highlight trade-offs** (control vs convenience, cost vs speed)

## Consequences

### Positive

- Students understand *what's happening* even when using managed tools
- Content remains relevant regardless of which platform students use
- No vendor lock-in or commercial dependencies
- Free-tier compatible (critical for accessibility)

### Negative

- More content to maintain (open-source APIs change faster)
- Can't show polished managed platform UIs
- Students may want guided managed workflow (deferred to supplementary content)

### Neutral

- Turing Platform can still be mentioned as one of many managed options
- README's "Turing Platform Mastery" section becomes "Managed Platform Patterns"

## Alternatives Considered

1. **Turing-first**: Rejected—creates vendor dependency, may not be accessible to all students
2. **Pure theory**: Rejected—students need hands-on practice, not just concepts
3. **Multiple platforms in parallel**: Rejected—too much content, fragments learning

## References

- User requirement: "Platform-agnostic (not dependent on single platform like Turing)"
- Constitution v7.0.0: Digital FTE production as outcome
- Part 8 README: LLMOps fundamentals applicable across platforms
