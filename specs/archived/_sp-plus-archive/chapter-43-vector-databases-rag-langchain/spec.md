# Chapter 43: Vector Databases & RAG with LangChain

## Overview

This chapter teaches students how to build production-grade Retrieval-Augmented Generation (RAG) systems using LangChain for orchestration and Qdrant as the vector database. Students extend their Task API from Chapter 40 with semantic search capabilities, learning 8 RAG architecture patterns from simple to agentic.

**Part**: 6 (AI Native Software Development)
**Position in Part 6**: Data Layer chapter - adds knowledge retrieval to agent services
**Target Proficiency**: B1 (Intermediate)

## Prerequisites

- **Chapter 40**: FastAPI for Agents (Task API foundation)
- **Chapters 34-36**: Agent SDK chapters (agents know how to call tools)
- **Docker**: For running Qdrant locally

## Learning Outcomes

By the end of this chapter, students will be able to:

1. Explain why agents need external knowledge (parametric vs non-parametric memory)
2. Describe how vector embeddings represent semantic meaning
3. Use LangChain for document loading, text splitting, and embedding
4. Set up and interact with Qdrant vector store through LangChain
5. Build retrieval chains and QA chains for semantic search
6. Integrate RAG with the Task API for semantic task search
7. Evaluate RAG quality using LangSmith and RAGAS metrics
8. Design RAG systems using appropriate architecture patterns (Simple, HyDE, CRAG, etc.)

---

## Lesson Structure (L00-L08)

### L00: Build Your RAG Skill (MANDATORY FIRST)
**Duration**: 20 minutes | **Layer**: L1 (Manual Foundation) | **Proficiency**: B1

Students create their `rag-deployment` skill before learning RAG concepts:
1. Clone skills-lab fresh
2. Use /fetching-library-docs to get LangChain RAG docs
3. Create skill with /skill-creator
4. Test that skill responds to RAG-related prompts

**Student skill name**: `rag-deployment`

---

### L01: Why Agents Need External Knowledge
**Duration**: 25 minutes | **Layer**: L1 (Conceptual) | **Proficiency**: A2

**Concepts**:
- Parametric memory (training data) vs non-parametric memory (retrieval)
- Knowledge cutoff problem: LLMs don't know recent information
- Hallucination risk when LLMs make up facts
- RAG as the solution: ground responses in retrieved documents

**Running Example Hook**:
"Your Task API has hundreds of tasks. A user asks: 'Show me tasks related to Docker deployment.' Currently you can only filter by exact fields like status or priority. RAG lets you find semantically similar tasks."

**No code in this lesson** - pure conceptual foundation.

---

### L02: Vector Embeddings Mental Model
**Duration**: 30 minutes | **Layer**: L1 (Conceptual) | **Proficiency**: A2

**Concepts**:
- Embeddings as numerical representations of meaning
- Semantic similarity: similar meanings = close vectors
- Embedding models: text-embedding-3-small (1536 dimensions)
- Cosine similarity for comparing vectors

**Visual**: Show 2D projection of embedding space with similar concepts clustered

**Try With AI**: Generate embeddings for sample sentences and compare similarity scores

---

### L03: LangChain Document Processing
**Duration**: 40 minutes | **Layer**: L2 (AI Collaboration) | **Proficiency**: B1

**Concepts**:
- Document loaders: WebBaseLoader, PyPDFLoader, TextLoader
- Text splitters: RecursiveCharacterTextSplitter
- Chunking parameters: chunk_size, chunk_overlap, separators
- Metadata preservation through splitting

**Code Pattern**:
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True,
)
splits = text_splitter.split_documents(docs)
```

**Try With AI**: Load and split a markdown file, experiment with chunk sizes

---

### L04: Qdrant Vector Store with LangChain
**Duration**: 45 minutes | **Layer**: L2 (AI Collaboration) | **Proficiency**: B1

**Concepts**:
- Running Qdrant with Docker: `docker run -p 6333:6333 qdrant/qdrant`
- QdrantVectorStore initialization patterns (in-memory, Docker, cloud)
- Adding documents with embeddings
- Similarity search and retrieval modes (dense, sparse, hybrid)

**Code Pattern**:
```python
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

vector_store = QdrantVectorStore.from_documents(
    splits,
    OpenAIEmbeddings(model="text-embedding-3-small"),
    url="http://localhost:6333",
    collection_name="task_docs",
)
```

**Try With AI**: Set up Qdrant, index sample documents, run similarity searches

---

### L05: Building Retrieval Chains
**Duration**: 45 minutes | **Layer**: L2 (AI Collaboration) | **Proficiency**: B1

**Concepts**:
- Retriever pattern: vector_store.as_retriever()
- Simple QA chain: retriever → prompt → LLM
- Chain composition with LCEL (LangChain Expression Language)
- Formatting retrieved documents for context

**Code Pattern**:
```python
retriever = vector_store.as_retriever(search_kwargs={"k": 4})

chain = (
    {"context": retriever | format_docs, "question": lambda x: x}
    | prompt
    | llm
)
response = chain.invoke("How do I create a task?")
```

**Try With AI**: Build a QA chain over your indexed documents

---

### L06: RAG for Task API
**Duration**: 50 minutes | **Layer**: L3 (Skill Integration) | **Proficiency**: B1

**Integration with Chapter 40**: Add semantic search endpoint to Task API

**Concepts**:
- Indexing task descriptions for semantic search
- Adding `/tasks/search/semantic` endpoint
- Combining structured filters with vector similarity
- Returning ranked results with relevance scores

**Code Pattern**:
```python
@router.post("/tasks/search/semantic")
async def semantic_search(query: str, k: int = 5):
    results = vector_store.similarity_search_with_score(query, k=k)
    return [
        {"task_id": doc.metadata["task_id"], "relevance": score}
        for doc, score in results
    ]
```

**Try With AI**: Extend your Task API with semantic search

---

### L07: Evaluating RAG Quality
**Duration**: 45 minutes | **Layer**: L2 (AI Collaboration) | **Proficiency**: B1

**Concepts**:
- Four evaluation dimensions: Correctness, Relevance, Groundedness, Retrieval Quality
- LLM-as-Judge pattern for evaluation
- LangSmith for tracing and visualization
- RAGAS metrics: faithfulness, answer_relevancy, context_precision, context_recall

**Code Pattern**:
```python
from ragas.metrics import faithfulness, answer_relevancy
from ragas import evaluate

results = evaluate(dataset, metrics=[faithfulness, answer_relevancy])
```

**Try With AI**: Create an evaluation dataset and run metrics

---

### L08: RAG Architecture Patterns (Capstone)
**Duration**: 60 minutes | **Layer**: L4 (Orchestration) | **Proficiency**: B1

**Eight RAG Patterns**:
1. **Simple RAG** - Basic retrieval → generate
2. **Simple RAG with Memory** - Conversation context
3. **Branched RAG** - Route to specialized retrievers
4. **HyDE** - Generate hypothetical answer first
5. **Adaptive RAG** - Adjust strategy by query complexity
6. **Corrective RAG (CRAG)** - Grade documents, fallback to web
7. **Self-RAG** - Self-assess and re-retrieve
8. **Agentic RAG** - Multi-tool agent orchestration

**Capstone Project**: Implement at least two RAG patterns for the Task API:
1. Simple RAG (baseline)
2. One advanced pattern (student choice: HyDE, CRAG, or Agentic)

---

## Technology Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Orchestration | LangChain | Handles chunking, embedding, retrieval, chains |
| Vector DB | Qdrant | Open source, Docker-friendly, excellent LangChain support |
| Embeddings | OpenAI text-embedding-3-small | Production quality, 1536 dimensions |
| Evaluation | LangSmith + RAGAS | Industry standard for RAG evaluation |

**Dependencies**:
```
langchain>=0.3.0
langchain-qdrant>=0.2.0
langchain-openai>=0.2.0
langchain-text-splitters>=0.3.0
qdrant-client>=1.12.0
ragas>=0.2.0
```

---

## Scope Boundaries

### In Scope (Chapter 43)
- What is RAG and why agents need it
- Vector embeddings conceptual model
- LangChain document loaders and text splitters
- Qdrant vector store with LangChain integration
- Retrieval chains and QA chains
- Semantic search over Task API data
- RAG evaluation basics (LangSmith, RAGAS)
- 8 RAG architecture patterns (overview + 2 implementations)

### Out of Scope (Not in Chapter 43)
- Building vector DB from scratch (use LangChain abstraction)
- Fine-tuning embedding models (advanced topic)
- Multi-modal RAG (text only in this chapter)
- Production scaling and sharding (covered in Part 7)
- Graph RAG (future chapter topic)
- Agentic RAG with LangGraph full implementation (covered conceptually only)

---

## Running Example Integration

**Task API Extension**: Students extend their Task API from Chapter 40 with:
1. Task description indexing (L04)
2. Semantic search endpoint (L06)
3. RAG-powered task recommendations (L08)

This maintains narrative continuity from Part 6's API chapters while demonstrating RAG's practical value.

---

## Skill-First Pattern

Every lesson ends with a "Reflect on Your Skill" section:

```markdown
---

## Reflect on Your Skill

You built a `rag-deployment` skill in Lesson 0. Test and improve it.

### Test Your Skill
[Prompt to test skill with current lesson's concepts]

### Identify Gaps
[Questions about what might be missing]

### Improve Your Skill
[Prompt to update skill if gaps found]
```

---

## Layer Progression

| Lesson | Layer | Description |
|--------|-------|-------------|
| L00 | L1 | Build skill manually from docs |
| L01 | L1 | Conceptual: why RAG |
| L02 | L1 | Conceptual: embeddings |
| L03 | L2 | AI collaboration: document processing |
| L04 | L2 | AI collaboration: Qdrant setup |
| L05 | L2 | AI collaboration: retrieval chains |
| L06 | L3 | Skill integration: Task API extension |
| L07 | L2 | AI collaboration: evaluation |
| L08 | L4 | Orchestration: architecture patterns |

---

## Images/Videos Available

None specified. Diagrams should be created for:
- L02: Embedding space visualization (2D projection)
- L05: Retrieval chain flow diagram
- L08: RAG architecture comparison table

---

## Quality Requirements

1. **Full YAML frontmatter** with skills, learning_objectives, cognitive_load, differentiation
2. **Compelling narrative opening** connecting to Task API and agent needs
3. **Evidence blocks** for all code examples (show output)
4. **Three "Try With AI" prompts** per lesson with learning explanations
5. **"Reflect on Your Skill"** section at end of L01-L08
6. **Safety notes** for API key handling

---

## Created By

Spec generated using /sp.chapter workflow.
Expertise skill: `.claude/skills/building-rag-systems/SKILL.md`
