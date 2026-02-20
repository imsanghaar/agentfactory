---
title: "Training Taxonomy"
sidebar_position: 4
chapter: 61
lesson: 4
duration_minutes: 40

# HIDDEN SKILLS METADATA
skills:
  - name: "LLM Training Methods"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "AI and Machine Learning"
    measurable_at_this_level: "Student distinguishes between pretraining, SFT, and alignment methods"

  - name: "PEFT Methods"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "AI and Machine Learning"
    measurable_at_this_level: "Student explains how LoRA and QLoRA reduce training costs"

  - name: "Training Method Selection"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "AI and Machine Learning"
    measurable_at_this_level: "Student selects appropriate training method for given use case"

learning_objectives:
  - objective: "Distinguish between pretraining, supervised fine-tuning, and alignment methods"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student correctly categorizes training approaches in scenarios"

  - objective: "Explain how parameter-efficient methods (LoRA, QLoRA) enable fine-tuning on consumer hardware"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student explains adapter concept and VRAM savings"

  - objective: "Select the appropriate training method for a given use case"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Student justifies training method choice with trade-off analysis"

cognitive_load:
  new_concepts: 8
  assessment: "Pretraining, SFT, DPO, RLHF, LoRA, QLoRA, full fine-tuning, adapter - at B2 upper limit but scaffolded progressively"

differentiation:
  extension_for_advanced: "Compare RLHF and DPO mathematically; explore emerging alignment methods like ORPO"
  remedial_for_struggling: "Focus on pretraining vs SFT distinction before introducing alignment methods"

generated_by: "content-implementer"
created: "2026-01-01"
---

# Training Taxonomy

You've decided fine-tuning makes sense for your use case. Now comes a critical question: *what kind* of fine-tuning?

The term "fine-tuning" encompasses wildly different approaches. Some require $10 million in compute. Others run on a laptop. Some teach new knowledge. Others shape behavior without adding facts. Choosing the wrong method wastes resources or produces poor results.

This lesson maps the training landscape so you can navigate it with confidence.

## The Training Spectrum

Think of training language models like educating a person through different life stages:

**Pretraining** = Early childhood education. You're building foundational knowledge—language itself, facts about the world, reasoning patterns. This takes years (compute equivalent: months) and massive resources (thousands of GPUs).

**Supervised Fine-Tuning (SFT)** = Professional training. The foundation exists; now you're teaching specific skills. A medical school graduate becomes a surgeon. A general LLM becomes a task management expert.

**Alignment** = Behavioral coaching. The skills exist; now you're shaping *how* they're applied. Coaching a surgeon on bedside manner. Teaching a model to be helpful, harmless, and honest.

```
Pretraining    →    Fine-Tuning    →    Alignment
(Build brain)       (Add skills)        (Shape behavior)

Cost: $10M+         Cost: $10-$10K      Cost: $100-$1K
Time: Months        Time: Hours-Days    Time: Hours
Data: Trillions     Data: Thousands     Data: Hundreds
```

Most LLMOps work operates in the fine-tuning and alignment zones. You're not building brains—you're adding skills and shaping behavior.

## Pretraining: Building the Foundation

Pretraining creates a model from scratch. The model learns language structure, world knowledge, and reasoning patterns from massive text corpora.

### What Pretraining Teaches

| Capability | Example |
|------------|---------|
| Language structure | Grammar, syntax, word relationships |
| World knowledge | Paris is in France, water is H2O |
| Reasoning patterns | If A implies B and B implies C, then A implies C |
| Common sense | Objects fall down, people need food |
| Domain vocabulary | Medical terms, legal language, code syntax |

### The Resource Reality

**Compute**: GPT-4 reportedly required 25,000 A100 GPUs running for months. Llama 3 70B used 6,000 H100s for weeks.

**Data**: Trillions of tokens. Llama 3 trained on 15 trillion tokens—roughly 500 billion words.

**Cost**: Estimates range from $5 million (Llama 2 70B) to $100+ million (frontier models).

**Timeline**: 1-6 months of continuous training.

### When Would You Pretrain?

Almost never. Unless you're:
- A major AI lab building foundation models
- Training on a genuinely new domain with no existing models (rare)
- Building models for non-English languages underserved by current models

For 99.9% of LLMOps work, you start with a pretrained model and customize from there.

## Supervised Fine-Tuning (SFT): Adding Skills

SFT is the workhorse of practical LLMOps. You take a pretrained model and teach it specific skills through examples.

### How SFT Works

You provide input-output pairs:

```json
[
  {
    "input": "Create a high priority task: Review Q4 budget",
    "output": "{\"title\": \"Review Q4 budget\", \"priority\": \"high\", \"status\": \"pending\"}"
  },
  {
    "input": "What tasks are due this week?",
    "output": "Let me check your task list for this week. I found 3 tasks due: [lists tasks]"
  }
]
```

The model learns to produce outputs similar to your examples. After seeing hundreds or thousands of examples, it generalizes to new inputs.

### What SFT Can Achieve

| Capability | Example |
|------------|---------|
| Domain expertise | Task management, legal analysis, medical coding |
| Output format | Consistent JSON structure, specific template |
| Vocabulary | Your organization's terminology |
| Style | Concise responses, detailed explanations |
| Tool calling | When and how to invoke specific functions |

### SFT Resource Requirements

**Data**: 1,000-100,000 high-quality examples (depends on complexity)

**Compute**: Hours to days on single GPU (with PEFT methods)

**Cost**: $1-$100 with cloud providers; nearly free with local hardware

**Timeline**: Hours for small models, days for larger ones

### The SFT Trade-off

**Strength**: SFT directly teaches skills. Show the model what you want; it learns to do it.

**Weakness**: SFT can cause "catastrophic forgetting"—the model may lose general capabilities while gaining specific ones. A task management model might forget how to write poetry.

**Mitigation**: Use techniques like LoRA (coming up) that modify only a small portion of the model's weights.

## Alignment: Shaping Behavior

Alignment methods don't teach new skills—they shape *how* existing skills are applied. The model knows how to answer questions; alignment teaches it to answer helpfully and avoid harmful outputs.

### RLHF (Reinforcement Learning from Human Feedback)

The original alignment method, used to train ChatGPT and Claude.

**How it works**:
1. Train a reward model on human preferences (which response is better?)
2. Use reinforcement learning to optimize the LLM toward higher reward

**Strengths**: Powerful alignment, well-studied, proven at scale

**Weaknesses**:
- Requires training three models (LLM, reward model, reference model)
- Complex training loop
- Computationally expensive
- Prone to instability

### DPO (Direct Preference Optimization)

A simpler alternative to RLHF, gaining rapid adoption.

**How it works**:
1. Collect preference pairs (response A is better than response B)
2. Train directly on preferences—no separate reward model needed

**Strengths**:
- Simpler than RLHF (one training loop, not three)
- More stable training
- Lower compute requirements
- Easier to implement

**Weaknesses**:
- Less flexible than full RLHF
- May not capture subtle preferences as well

### Comparison: RLHF vs DPO

| Factor | RLHF | DPO |
|--------|------|-----|
| Complexity | High (3 models, RL loop) | Low (single training loop) |
| Stability | Can be unstable | Generally stable |
| Compute | High | Moderate |
| Data requirement | Preference pairs + more | Preference pairs |
| Adoption | Established (GPT, Claude) | Growing rapidly |

**Our recommendation**: For most LLMOps projects, start with DPO. It's simpler to implement and debug. Use RLHF only if DPO proves insufficient.

## Parameter-Efficient Fine-Tuning (PEFT)

Here's the revolution that makes LLMOps accessible: you don't need to train all model parameters.

### The Problem with Full Fine-Tuning

A 7 billion parameter model requires:
- 14 GB just to store the model weights (at fp16)
- 56+ GB to store optimizer states during training
- High-end GPUs with 80+ GB VRAM

Most practitioners don't have access to such hardware.

### The PEFT Solution

**Freeze the original weights. Train only small adapter layers.**

Instead of modifying 7 billion parameters, you train 20 million new parameters that sit alongside the original model. The result:
- Similar performance to full fine-tuning
- 10-100x less memory required
- Training on consumer hardware becomes possible

### LoRA (Low-Rank Adaptation)

The most popular PEFT method. LoRA injects trainable "adapter" matrices into specific layers.

**Core insight**: Weight changes during fine-tuning tend to be low-rank. Instead of updating a 4096x4096 weight matrix, LoRA trains two smaller matrices (4096x16 and 16x4096) whose product approximates the change.

```
Original weight matrix W: 4096 x 4096 = 16.7 million parameters
LoRA adapter (rank 16): (4096 x 16) + (16 x 4096) = 131,072 parameters

Reduction: 127x fewer trainable parameters
```

**Benefits**:
- Train on GPUs with 8-16 GB VRAM
- Multiple LoRA adapters for different tasks (swap them at runtime)
- Original model weights unchanged (no catastrophic forgetting)

### QLoRA (Quantized LoRA)

LoRA plus quantization. The base model is stored in 4-bit precision, further reducing memory.

**The magic**:
- 4-bit storage for the base model
- 16-bit computation when needed (dequantize on the fly)
- LoRA adapters trained in 16-bit precision

**Result**: Fine-tune a 7B model on a GPU with just 6 GB VRAM.

### PEFT Comparison

| Method | VRAM (7B model) | Training Speed | Quality |
|--------|-----------------|----------------|---------|
| Full Fine-Tuning | 60+ GB | Baseline | Best |
| LoRA (rank 16) | 16 GB | 2x faster | ~95% of full |
| QLoRA (rank 16) | 6 GB | 3x faster | ~93% of full |

The quality difference is often imperceptible in practice. Most LLMOps practitioners use QLoRA by default.

## Choosing Your Training Method

Now you can make informed decisions. Here's the decision tree:

```
Start: What do you need?
│
├── New capabilities the model lacks?
│   └── SFT with domain-specific examples
│
├── Better output quality on existing tasks?
│   └── SFT with high-quality examples
│
├── Different response style or persona?
│   └── SFT (for dramatic changes) or DPO (for refinement)
│
├── Safer or more aligned outputs?
│   └── DPO (simpler) or RLHF (more powerful)
│
└── Hardware constraints?
    ├── Consumer GPU (8-16 GB) → QLoRA
    ├── Professional GPU (24-48 GB) → LoRA or full fine-tuning
    └── Cloud or cluster → Any method viable
```

### The Task API Example

For our Task Management Assistant, the decision process:

**Goal**: Model should understand task management domain, produce consistent JSON, and interact naturally.

**Analysis**:
- Domain expertise needed → SFT with task examples
- Consistent output format → SFT with structured examples
- Persona/style shaping → Could use DPO after SFT
- Hardware: Consumer GPU → QLoRA

**Decision**: QLoRA-based SFT with 2,000-5,000 task management examples.

This gives us a domain-expert model that runs on accessible hardware. In Chapter 64, we'll implement exactly this.

## Method Selection Matrix

| Use Case | Primary Method | Secondary | Hardware |
|----------|---------------|-----------|----------|
| Domain expert | SFT | - | QLoRA on consumer GPU |
| JSON formatting | SFT | - | QLoRA on consumer GPU |
| Persona/style | SFT or DPO | - | QLoRA on consumer GPU |
| Safety alignment | DPO | RLHF | LoRA or full fine-tuning |
| Knowledge injection | SFT | - | Depends on scale |
| Behavior refinement | DPO | - | QLoRA on consumer GPU |

## Common Misconceptions

**"Fine-tuning teaches the model new facts"**

Partially true. SFT can encode domain knowledge, but models are better at learning *patterns* than *facts*. For specific factual recall, consider retrieval-augmented generation (RAG) instead of—or alongside—fine-tuning.

**"More parameters = better fine-tuning"**

Not necessarily. A well-tuned 7B model often outperforms a poorly-tuned 70B model on specific tasks. Match model size to your use case and data quality.

**"You need thousands of GPUs"**

Only for pretraining. Fine-tuning happens on single GPUs. QLoRA enables this on hardware you might already own.

**"RLHF is always better than DPO"**

For most use cases, DPO achieves comparable results with less complexity. RLHF's power matters at frontier scale; for practical LLMOps, DPO often suffices.

## Try With AI

Solidify your understanding by applying the training taxonomy to real scenarios.

**Prompt 1: Classify Training Approaches**

```text
I'm building a customer support chatbot that needs to:
1. Understand our product documentation
2. Follow our company's communication style guide
3. Avoid making promises about features we don't offer

For each requirement, which training method (pretraining, SFT, DPO, RLHF) is most appropriate? Explain your reasoning for each.
```

**What you're learning:** This exercise forces you to map business requirements to training methods. You'll recognize that different goals require different approaches—knowledge comes from SFT, safety constraints from alignment methods.

**Prompt 2: PEFT Trade-off Analysis**

```text
I have access to three hardware setups:
- Option A: Single RTX 4090 (24 GB VRAM)
- Option B: Cloud instance with A100 (80 GB VRAM)
- Option C: MacBook Pro M3 Max (64 GB unified memory)

For each option, what's the largest model I could fine-tune, and which PEFT method would you recommend? Consider both training time and final model quality.
```

**What you're learning:** This prompt develops your intuition for matching hardware to methods. You'll discover that consumer hardware is more capable than expected—and understand when cloud resources justify their cost.

**Prompt 3: Design Your Training Pipeline**

```text
I'm building a [your domain] assistant. The model needs to:
- [List 2-3 specific capabilities]

Design a training pipeline:
1. What pretrained base model would you start with?
2. Would you use SFT, DPO, or both? In what order?
3. What PEFT method fits my likely hardware constraints?
4. Roughly how much training data would I need for each stage?
```

**What you're learning:** This bridges taxonomy to practice. By designing for your actual domain, you internalize the full decision process—from base model selection through training method choice to resource planning.
