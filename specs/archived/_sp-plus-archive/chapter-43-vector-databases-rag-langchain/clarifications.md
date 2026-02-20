# Chapter 43: Clarifications

## Review Date: 2025-12-30

## User-Provided Specifications (No Ambiguity)

The user provided detailed specifications that resolved all potential ambiguities:

### Technology Choices (CONFIRMED)
- **Orchestration**: LangChain (explicitly requested - "saves time on components")
- **Vector DB**: Qdrant (Docker-friendly, open source)
- **Embeddings**: OpenAI text-embedding-3-small
- **Evaluation**: LangSmith + RAGAS

### Scope Boundaries (CONFIRMED)
- **In scope**: 8 RAG architectures, LangChain patterns, evaluation basics
- **Out of scope**: Building vector DB from scratch, fine-tuning, multi-modal, production scaling

### Running Example (CONFIRMED)
- Task API from Chapter 40 extended with semantic search
- Student skill name: `rag-deployment`

### Lesson Structure (CONFIRMED)
- L00-L08 (9 lessons)
- L00: Build Your RAG Skill (MANDATORY FIRST)
- Skill-First pattern with "Reflect on Your Skill" at end of each lesson

## RAG Architectures to Cover (CONFIRMED)
User explicitly provided 8 patterns:
1. Simple RAG
2. Simple RAG with Memory
3. Branched RAG
4. HyDE (Hypothetical Document Embedding)
5. Adaptive RAG
6. Corrective RAG (CRAG)
7. Self-RAG
8. Agentic RAG

## Proficiency Level (CONFIRMED)
- Target: B1 (Intermediate)
- Prerequisites: Chapter 40 (FastAPI), Chapters 34-36 (Agent SDKs)

## No Clarifications Needed

Spec is complete and ready for planning phase.
