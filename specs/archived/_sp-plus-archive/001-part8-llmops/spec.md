# Feature Specification: Part 8 — LLMOps Proprietary Intelligence

**Feature Branch**: `001-part8-llmops`
**Created**: 2026-01-01
**Status**: Draft
**Proficiency Level**: B2-C1 (Intermediate to Advanced)
**Input**: User description: "Part 8: Turing LLMOps — Proprietary Intelligence (Chapters 61-72). Create specification for 12 chapters covering LLMOps fundamentals, data engineering, fine-tuning (SFT, PEFT, LoRA), persona/agentic tuning, alignment/safety (DPO), evaluation, deployment (Ollama/vLLM), and agent framework integration. Must be Colab Free Tier compatible (T4 GPU, 4-bit quantization). Platform-agnostic (not dependent on single platform like Turing - teach concepts that work with Unsloth, HuggingFace, or managed platforms). Running example: Task API from Chapter 40."

---

## Assumed Knowledge

**What students know BEFORE this part**:
- **Part 4 (SDD-RI)**: Specification-driven development, writing clear specs, acceptance criteria
- **Part 5 (Python)**: Async/await, type hints, Pydantic models, data processing with pandas
- **Part 6 (AI Native)**: Agent frameworks (OpenAI Agents SDK, Claude SDK, Google ADK), MCP servers, FastAPI for agents
- **Part 7 (Cloud Native)**: Docker containerization, Kubernetes deployment, Helm charts, observability
- **Running Example**: Task API from Chapter 40 (FastAPI + SQLModel + Neon)
- **Skill-First Pattern**: Creating skills from official documentation (L00 pattern from Parts 6-7)

**What this part must explain from scratch**:
- LLM architecture internals (transformers, attention, tokenization)
- Training taxonomy (pretraining vs SFT vs DPO vs agentic tuning)
- Compute reality (VRAM budgeting, quantization, free-tier constraints)
- PEFT techniques (LoRA, QLoRA, adapter theory)
- Dataset engineering (JSONL formats, synthetic data generation)
- Alignment techniques (DPO, preference datasets)
- Model export and serving (GGUF, Ollama, vLLM)

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Domain Expert Creates Custom Model (Priority: P1)

A domain expert (sales professional, legal expert, technical writer) wants to create a custom AI model specialized for their domain that can be monetized as a Digital FTE.

**Why this priority**: This is the core value proposition—transforming domain expertise into proprietary intelligence that generates recurring revenue. Aligns with the Agent Factory thesis.

**Independent Test**: Student can take a domain dataset, fine-tune a model on Colab Free Tier, and deploy it locally via Ollama—delivering working specialized model from start to finish.

**Acceptance Scenarios**:

1. **Given** a domain expert with 500+ instruction pairs for their field, **When** they complete Part 8, **Then** they have a fine-tuned model that responds accurately to domain-specific queries.
2. **Given** a student with only a T4 GPU (Colab Free Tier), **When** they follow the training workflow, **Then** the model trains successfully using 4-bit quantization without OOM errors.
3. **Given** a trained custom model, **When** deployed via Ollama, **Then** it can be queried locally and responds in the specialized domain voice.

---

### User Story 2 - Developer Replaces Expensive API Calls (Priority: P2)

A developer currently using GPT-4/Claude for specific tasks wants to fine-tune a smaller model to reduce costs while maintaining quality for narrowly-scoped tasks.

**Why this priority**: Cost optimization is a major business driver—custom models at $500-2000/mo vs $10K+/mo for API-heavy workflows.

**Independent Test**: Student can identify a specific task, fine-tune a 7B model for that task, and demonstrate comparable output quality at 90%+ lower inference cost.

**Acceptance Scenarios**:

1. **Given** a specific task (e.g., JSON tool-calling, code review, content rewriting), **When** fine-tuned model is deployed, **Then** it produces outputs within acceptable quality threshold.
2. **Given** a production workload, **When** using the fine-tuned model instead of foundation model API, **Then** cost per request decreases by 80%+.
3. **Given** an agentic workflow using OpenAI Agents SDK, **When** swapping in the custom model backend, **Then** tool-calling accuracy remains above 95%.

---

### User Story 3 - Student Builds Complete LLMOps Pipeline (Priority: P3)

A student completing Part 8 should own a reusable LLMOps skill and have built an end-to-end pipeline from data curation to production deployment.

**Why this priority**: Skill accumulation is core to Agent Factory paradigm—students graduate with sellable assets, not just knowledge.

**Independent Test**: Student has a `.claude/skills/llmops-fine-tuner/` skill that they created and refined through the chapter, plus a deployed model serving API requests.

**Acceptance Scenarios**:

1. **Given** completion of Part 8, **When** student examines their skills directory, **Then** they have a production-ready `llmops-fine-tuner` skill documented with official sources.
2. **Given** the capstone project, **When** end-to-end pipeline runs, **Then** it processes raw data → trains model → evaluates → exports → deploys in automated workflow.
3. **Given** the deployed model, **When** integrated with agent framework from Part 6, **Then** it serves as a custom agent backend accepting tool calls.

---

### Edge Cases

- What happens when training crashes due to OOM on T4? (4-bit quantization, gradient checkpointing, reduced batch size)
- How does system handle corrupted training data? (Data validation pipeline with schema checks)
- What if model produces harmful outputs after fine-tuning? (DPO alignment, safety evaluation, refusal training)
- What happens when MergeKit exceeds RAM? (Sharded loading, layer-by-layer merging)
- How to handle API rate limits during synthetic data generation? (Batching, caching, retry logic)

---

## Requirements *(mandatory)*

### Functional Requirements

#### Chapter Structure (12 Chapters: 61-72)

- **FR-001**: Part 8 MUST contain exactly 12 chapters numbered 61-72, following Part 7's ending at Chapter 60.
- **FR-002**: Chapters MUST follow the 4-stage structure from Part 8 README: Concepts/Setup → Data/Training → Evaluation/Quality → Deployment/Operations.
- **FR-003**: Each chapter MUST include L00 Skill-First lesson where applicable (building `llmops-*` skills from official docs).
- **FR-004**: All chapters MUST be compatible with Google Colab Free Tier (T4 GPU, 15GB VRAM, 12GB RAM).

#### Technical Constraints

- **FR-005**: Training workflows MUST use 4-bit quantization (BitsAndBytes/NF4) to fit models on T4 GPU.
- **FR-006**: Content MUST be platform-agnostic—teach concepts using Unsloth, HuggingFace, and show how managed platforms abstract these.
- **FR-007**: Model merging MUST use sharded loading techniques compatible with 12GB RAM constraint.
- **FR-008**: Axolotl MUST be covered as theory/YAML demonstration only (not hands-on due to install complexity).
- **FR-009**: Vision/multimodal fine-tuning MUST use Llama-3.2-11B-Vision quantized (only model that fits T4).

#### Pedagogical Requirements

- **FR-010**: Each chapter MUST follow Layer 1→4 progression (Manual Foundation → AI Collaboration → Intelligence Design → Spec-Driven Capstone).
- **FR-011**: Part 8 capstone MUST produce a Digital FTE outcome (deployable custom model with agent integration).
- **FR-012**: Running example MUST use Task API domain from Chapter 40 for continuity.
- **FR-013**: Every "Try With AI" section MUST follow the 5-part active collaboration template (no meta-commentary).
- **FR-014**: Lessons MUST end with "Try With AI" section only (no "What's Next", "Summary", or standalone "Safety Note" sections).

#### Content Accuracy

- **FR-015**: All code examples MUST have test execution logs demonstrating working code.
- **FR-016**: All API patterns MUST be verified against official documentation (Unsloth, HuggingFace, Ollama).
- **FR-017**: All factual claims (statistics, dates, model capabilities) MUST be WebSearch verified.
- **FR-018**: Dataset formats MUST match current industry standards (JSONL with instruction/input/output or conversations format).

#### Safety & Alignment

- **FR-019**: Alignment chapter MUST cover DPO (not RLHF—simpler, stable, free-tier feasible).
- **FR-020**: Red-teaming basics MUST be included (adversarial testing, jailbreak detection).
- **FR-021**: Safety guardrails MUST cover refusal training and toxicity filtering.

### Key Entities *(include if feature involves data)*

- **Training Dataset**: JSONL format with instruction pairs (Alpaca format) or conversation format (ShareGPT), includes quality metadata
- **Base Model**: Foundation model to fine-tune (Llama-3-8B, Mistral-7B, Qwen-7B), specified by HuggingFace model ID
- **Adapter**: LoRA/QLoRA weights that modify base model behavior, stored as safetensors files
- **Merged Model**: Adapter merged into base model weights, exportable to GGUF for local serving
- **Evaluation Dataset**: Held-out test set for measuring model quality, includes ground truth labels
- **Preference Dataset**: Prompt + chosen + rejected pairs for DPO alignment training

---

## Chapter Structure

### Stage 1: Concepts & Setup (Chapters 61-62)

| Ch  | Title                               | Lessons | Key Outcomes                                                                    |
| --- | ----------------------------------- | ------- | ------------------------------------------------------------------------------- |
| 61  | Introduction to LLMOps              | 6-7     | Understand when to fine-tune vs prompt, LLM lifecycle, proprietary intel ROI   |
| 62  | LLM Architecture & Compute Reality  | 7-8     | Transformer internals, quantization, VRAM budgeting, Lab: Inference on T4      |

### Stage 2: Data & Training (Chapters 63-67)

| Ch  | Title                                   | Lessons | Key Outcomes                                                          |
| --- | --------------------------------------- | ------- | --------------------------------------------------------------------- |
| 63  | Data Engineering for Training           | 7-8     | Dataset formats, quality pipelines, synthetic data, Lab: 500-row set  |
| 64  | Supervised Fine-Tuning (SFT)            | 8-9     | LoRA/QLoRA theory, Unsloth training, hyperparameters, Lab: Fine-tune  |
| 65  | Identity & Persona Tuning               | 6-7     | Style vs knowledge, persona datasets, Lab: Persona bot                |
| 66  | Agentic & Function-Calling Fine-Tuning  | 7-8     | Structured outputs, tool-calling datasets, Lab: JSON tool agent       |
| 67  | Model Merging & Optimization            | 6-7     | MergeKit techniques, reasoning distillation intro, Lab: Merge adapters|

### Stage 3: Evaluation & Quality (Chapters 68-69)

| Ch  | Title                      | Lessons | Key Outcomes                                                           |
| --- | -------------------------- | ------- | ---------------------------------------------------------------------- |
| 68  | Alignment & Safety         | 7-8     | DPO vs RLHF, preference datasets, red-teaming, Lab: Reduce harm 90%   |
| 69  | Evaluation & Quality Gates | 6-7     | LLM-as-a-Judge, task evaluations, regression testing, Lab: Eval pipe  |

### Stage 4: Deployment & Operations (Chapters 70-72)

| Ch  | Title                          | Lessons | Key Outcomes                                                          |
| --- | ------------------------------ | ------- | --------------------------------------------------------------------- |
| 70  | Deployment & Serving           | 7-8     | GGUF export, Ollama/vLLM, performance optimization, Lab: Local deploy|
| 71  | Agent Framework Integration    | 7-8     | Custom models as backends, MCP servers, FastAPI edges, Lab: SDK conn |
| 72  | Capstone: End-to-End LLMOps    | 8-10    | Complete pipeline (data→train→eval→deploy), Capstone: Domain FTE     |

---

## Non-Goals (What We're NOT Teaching)

- **Full pretraining from scratch**: Requires multi-GPU clusters, millions in compute—out of scope for practitioner-level content
- **RLHF with PPO**: Too complex, requires reward model training—DPO achieves alignment with simpler workflow
- **Multi-modal training (images) in depth**: Only brief coverage with Llama-3.2-Vision; full treatment deferred
- **Kubernetes-based training clusters**: Focus is on single-GPU practitioner workflow, not infrastructure engineering
- **Custom tokenizer training**: Use existing tokenizers; creating new ones is research-level work
- **Sparse Mixture-of-Experts (MoE)**: Mention as advanced path but don't teach—requires specialized infrastructure

---

## Assumptions

1. **Hardware**: Students have access to Google Colab Free Tier (T4 GPU, 15GB VRAM, 12GB RAM) or equivalent
2. **Cost Budget**: <$1 per student for synthetic data generation (GPT-4o-mini ~$0.10 for 500 rows)
3. **Prior Knowledge**: Students completed Parts 1-7 (especially Part 6 agents and Part 7 deployment)
4. **Base Models**: Llama-3-8B and Mistral-7B are primary models; Qwen-7B as alternative
5. **Running Example**: Task API domain provides sufficient complexity for domain-specific fine-tuning
6. **Local Serving**: Students can run Ollama locally on laptops with 8GB+ RAM (quantized models)
7. **Framework Stability**: Unsloth, TRL, and MergeKit APIs remain stable through content lifespan

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can complete full fine-tuning workflow (data prep → training → evaluation → deployment) in under 4 hours using Colab Free Tier
- **SC-002**: Training runs complete successfully on T4 GPU with <5% OOM failure rate using documented quantization settings
- **SC-003**: Fine-tuned models achieve 20%+ improvement on domain-specific benchmarks vs base model prompting
- **SC-004**: Deployed models respond to queries with <500ms latency on consumer hardware via Ollama
- **SC-005**: Tool-calling fine-tuned models achieve 95%+ JSON syntax accuracy on structured output tasks
- **SC-006**: DPO-aligned models reduce harmful output rate by 90%+ on red-team evaluation set
- **SC-007**: 80%+ of students complete Part 8 having created at least one deployable custom model
- **SC-008**: Students graduate with `llmops-fine-tuner` skill in their `.claude/skills/` directory

### Cost Targets

- **SC-009**: Total student cost for completing Part 8 < $1.00 (excluding optional cloud GPU rentals)
- **SC-010**: Synthetic data generation costs < $0.15 per student for typical 500-row dataset

---

## Dependencies

### Technical Dependencies

- **Google Colab**: T4 GPU access (free tier)
- **Unsloth**: Primary training framework (MIT licensed)
- **HuggingFace Transformers/TRL**: Model loading, DPO training
- **BitsAndBytes**: 4-bit quantization
- **MergeKit**: Adapter merging (MIT licensed)
- **Ollama**: Local model serving
- **vLLM**: Production serving (theory/demo only due to GPU requirements)

### Content Dependencies

- **Part 6 Chapters 40-41**: FastAPI and ChatKit patterns for agent integration
- **Part 7 Chapters 49-50**: Docker/Kubernetes for containerized model serving
- **Part 6 Chapters 34-36**: Agent SDKs for backend integration

---

## Risks & Mitigations

| Risk                               | Impact | Probability | Mitigation                                                       |
| ---------------------------------- | ------ | ----------- | ---------------------------------------------------------------- |
| Colab T4 availability changes      | High   | Low         | Document RunPod/Lambda Labs alternatives at $0.50-1/hr           |
| Unsloth API breaking changes       | Medium | Medium      | Pin specific versions in requirements, provide migration notes   |
| Model licensing restrictions       | Medium | Low         | Use permissively licensed models (Llama-3, Mistral Apache)       |
| Students lack local GPU            | Medium | Medium      | All training in Colab; Ollama works on CPU (slower but works)   |
| Synthetic data quality issues      | Medium | Medium      | Provide quality filtering scripts and validation checklists      |

---

## Platform-Agnostic Design

**Core Principle**: Teach concepts that transfer across platforms, not vendor lock-in.

| Concept          | Open-Source Tool       | Managed Platform Equivalent                            |
| ---------------- | ---------------------- | ------------------------------------------------------ |
| Fine-tuning      | Unsloth + HuggingFace  | Turing, AWS Bedrock, Azure AI Studio                   |
| Data preparation | Pandas + custom scripts| Scale AI, Labelbox, managed data pipelines             |
| Model serving    | Ollama, vLLM           | Together AI, Fireworks, Modal                          |
| Evaluation       | LLM-as-a-Judge + TRL   | LangSmith, Weights & Biases                            |
| Alignment        | TRL DPO                | Anthropic Constitutional AI, OpenAI fine-tuning        |

**Teaching approach**: Show open-source implementation, then explain how managed platforms abstract this.

---

## Validation Checklist

- [ ] All chapters compatible with T4 GPU (15GB VRAM)
- [ ] No single-platform dependencies (concepts transfer to any provider)
- [ ] Running example (Task API) provides coherent thread through chapters
- [ ] Skill-First pattern applied where applicable (L00 lessons)
- [ ] Layer 1-4 progression in each chapter
- [ ] Digital FTE outcome from capstone (deployable, monetizable)
- [ ] Cost under $1 per student verified
- [ ] All code examples tested and have execution logs
- [ ] No meta-commentary in student-facing content
- [ ] No forbidden sections at lesson ends
