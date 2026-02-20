# Chapter 43: Tasks

Generated from: `specs/chapter-43-vector-databases-rag-langchain/plan.md`

---

## Task Overview

| Task ID | Description | Output Path | Status |
|---------|-------------|-------------|--------|
| T43.README | Create chapter README | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/README.md` | [x] |
| T43.L00 | Create L00: Build Your RAG Skill | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/00-build-your-rag-skill.md` | [x] |
| T43.L01 | Create L01: Why Agents Need External Knowledge | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/01-why-agents-need-external-knowledge.md` | [x] |
| T43.L02 | Create L02: Vector Embeddings Mental Model | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/02-vector-embeddings-mental-model.md` | [x] |
| T43.L03 | Create L03: LangChain Document Processing | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/03-langchain-document-processing.md` | [x] |
| T43.L04 | Create L04: Qdrant Vector Store with LangChain | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/04-qdrant-vector-store-langchain.md` | [x] |
| T43.L05 | Create L05: Building Retrieval Chains | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/05-building-retrieval-chains.md` | [x] |
| T43.L06 | Create L06: RAG for Task API | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/06-rag-for-task-api.md` | [x] |
| T43.L07 | Create L07: Evaluating RAG Quality | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/07-evaluating-rag-quality.md` | [x] |
| T43.L08 | Create L08: RAG Architecture Patterns (Capstone) | `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/08-rag-architecture-patterns-capstone.md` | [x] |
| T43.VALIDATE | Run validators on all lessons | N/A | [x] |

---

## Task Details

### T43.README: Chapter README

**Description**: Create chapter README with overview, lesson list, and prerequisites

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/README.md`

**Dependencies**: None

**Acceptance Criteria**:
- [ ] Sidebar position configured
- [ ] Clear chapter overview
- [ ] Lesson list with durations
- [ ] Prerequisites listed (Ch40, Ch34-36)
- [ ] Learning outcomes summary

---

### T43.L00: Build Your RAG Skill

**Description**: Create Lesson 0 - Skill-First lesson where students create their rag-deployment skill

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/00-build-your-rag-skill.md`

**Dependencies**: None (first lesson)

**Acceptance Criteria**:
- [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- [ ] Step 1: Get the Skills Lab (clone instructions)
- [ ] Step 2: Create Your Skill (exact prompt to copy)
- [ ] Brief "Done" section explaining what comes next
- [ ] Duration: ~20 minutes
- [ ] Layer: L1 (Manual Foundation)

---

### T43.L01: Why Agents Need External Knowledge

**Description**: Create Lesson 1 - Conceptual foundation for RAG

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/01-why-agents-need-external-knowledge.md`

**Dependencies**: T43.L00

**Acceptance Criteria**:
- [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
- [ ] Compelling narrative opening connecting to Task API
- [ ] Parametric vs non-parametric memory explained
- [ ] Knowledge cutoff problem
- [ ] Hallucination risk
- [ ] RAG as solution
- [ ] 3 "Try With AI" prompts with learning explanations
- [ ] "Reflect on Your Skill" section at end
- [ ] Duration: ~25 minutes
- [ ] Layer: L1 (Conceptual)
- [ ] NO code in this lesson (pure conceptual)

---

### T43.L02: Vector Embeddings Mental Model

**Description**: Create Lesson 2 - Conceptual understanding of embeddings

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/02-vector-embeddings-mental-model.md`

**Dependencies**: T43.L01

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening
- [ ] Embeddings as numerical representations
- [ ] Semantic similarity explained
- [ ] Cosine similarity concept
- [ ] Embedding model options
- [ ] Visual: 2D embedding space diagram
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] Duration: ~30 minutes
- [ ] Layer: L1 (Conceptual with minimal code)

---

### T43.L03: LangChain Document Processing

**Description**: Create Lesson 3 - Document loaders and text splitters

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/03-langchain-document-processing.md`

**Dependencies**: T43.L02

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening
- [ ] Document loaders: WebBaseLoader, PyPDFLoader, TextLoader
- [ ] RecursiveCharacterTextSplitter with parameters
- [ ] Code examples with Output: blocks
- [ ] Metadata preservation
- [ ] Three Roles demonstration (AI as Teacher/Student/Co-Worker)
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] Duration: ~40 minutes
- [ ] Layer: L2 (AI Collaboration)

---

### T43.L04: Qdrant Vector Store with LangChain

**Description**: Create Lesson 4 - Qdrant setup and LangChain integration

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/04-qdrant-vector-store-langchain.md`

**Dependencies**: T43.L03

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening
- [ ] Docker setup: `docker run -p 6333:6333 qdrant/qdrant`
- [ ] QdrantVectorStore initialization patterns
- [ ] Adding documents with embeddings
- [ ] Similarity search examples
- [ ] Retrieval modes: dense, sparse, hybrid
- [ ] Code with Output: blocks
- [ ] Three Roles demonstration
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] Duration: ~45 minutes
- [ ] Layer: L2 (AI Collaboration)

---

### T43.L05: Building Retrieval Chains

**Description**: Create Lesson 5 - Retriever pattern and QA chains

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/05-building-retrieval-chains.md`

**Dependencies**: T43.L04

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening
- [ ] Retriever pattern: vector_store.as_retriever()
- [ ] Simple QA chain composition
- [ ] LCEL (LangChain Expression Language) basics
- [ ] Format documents for context
- [ ] Diagram: Retrieval chain flow
- [ ] Code with Output: blocks
- [ ] Three Roles demonstration
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] Duration: ~45 minutes
- [ ] Layer: L2 (AI Collaboration)

---

### T43.L06: RAG for Task API

**Description**: Create Lesson 6 - Integration with Task API from Chapter 40

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/06-rag-for-task-api.md`

**Dependencies**: T43.L05

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening connecting to Chapter 40
- [ ] Indexing task descriptions
- [ ] Adding `/tasks/search/semantic` endpoint
- [ ] Combining structured filters with vector similarity
- [ ] Returning ranked results with scores
- [ ] Code with Output: blocks
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] Duration: ~50 minutes
- [ ] Layer: L3 (Skill Integration)

---

### T43.L07: Evaluating RAG Quality

**Description**: Create Lesson 7 - Evaluation with LangSmith and RAGAS

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/07-evaluating-rag-quality.md`

**Dependencies**: T43.L06

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening
- [ ] Four evaluation dimensions
- [ ] LLM-as-Judge pattern
- [ ] LangSmith setup and tracing
- [ ] RAGAS metrics: faithfulness, answer_relevancy, context_precision, context_recall
- [ ] Creating evaluation datasets
- [ ] Code with Output: blocks
- [ ] Three Roles demonstration
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section
- [ ] Duration: ~45 minutes
- [ ] Layer: L2 (AI Collaboration)

---

### T43.L08: RAG Architecture Patterns (Capstone)

**Description**: Create Lesson 8 - 8 RAG patterns + capstone implementation

**Output Path**: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/08-rag-architecture-patterns-capstone.md`

**Dependencies**: T43.L07

**Acceptance Criteria**:
- [ ] Full YAML frontmatter
- [ ] Narrative opening
- [ ] 8 RAG patterns overview:
  - [ ] Simple RAG
  - [ ] Simple RAG with Memory
  - [ ] Branched RAG
  - [ ] HyDE
  - [ ] Adaptive RAG
  - [ ] Corrective RAG (CRAG)
  - [ ] Self-RAG
  - [ ] Agentic RAG
- [ ] Architecture comparison table
- [ ] When to use which pattern
- [ ] Capstone: Implement 2 patterns for Task API
- [ ] Code with Output: blocks for at least 2 patterns
- [ ] 3 "Try With AI" prompts
- [ ] "Reflect on Your Skill" section (final reflection)
- [ ] Duration: ~60 minutes
- [ ] Layer: L4 (Orchestration)

---

### T43.VALIDATE: Run Validators

**Description**: Run all validators on completed lessons

**Dependencies**: T43.L00 through T43.L08

**Acceptance Criteria**:
- [ ] educational-validator passes for all 9 lessons
- [ ] validation-auditor passes chapter-wide
- [ ] factual-verifier verifies all claims
- [ ] pedagogical-designer validates progression

---

## Progress Tracking

- Total tasks: 11
- Completed: 11
- In progress: 0
- Pending: 0

---

## Notes

- All lesson files go in: `apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/`
- Follow quality reference: `apps/learn-app/docs/06-AI-Native-Software-Development/40-fastapi-for-agents/`
- Use expertise skill: `.claude/skills/building-rag-systems/SKILL.md`
