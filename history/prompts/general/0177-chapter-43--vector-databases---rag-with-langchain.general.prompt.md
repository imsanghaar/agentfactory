---
id: 0177
title: "Chapter 43: Vector Databases & RAG with LangChain"
stage: general
date: 2025-12-30
surface: claude-code
model: claude-opus-4-5-20251101
feature: chapter-43
branch: main
user: mjs
command: /sp.chapter
labels: [chapter, rag, langchain, qdrant, vector-database, part-6]
links:
  spec: specs/chapter-43-vector-databases-rag-langchain/spec.md
  ticket: N/A
  adr: N/A
  pr: pending
files:
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/README.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/00-build-your-rag-skill.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/01-why-agents-need-external-knowledge.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/02-vector-embeddings-mental-model.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/03-langchain-document-processing.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/04-qdrant-vector-store-langchain.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/05-building-retrieval-chains.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/06-rag-for-task-api.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/07-evaluating-rag-quality.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/08-rag-architecture-patterns-capstone.md
  - specs/chapter-43-vector-databases-rag-langchain/spec.md
  - specs/chapter-43-vector-databases-rag-langchain/clarifications.md
  - specs/chapter-43-vector-databases-rag-langchain/plan.md
  - specs/chapter-43-vector-databases-rag-langchain/tasks.md
  - .claude/skills/building-rag-systems/SKILL.md
  - .claude/skills/building-rag-systems/references/langchain-patterns.md
  - .claude/skills/building-rag-systems/references/rag-architectures.md
  - .claude/skills/building-rag-systems/references/evaluation-patterns.md
tests:
  - educational-validator: PASS
  - factual-verifier: PASS (after RAGAS import fix)
---

## Prompt

```
/sp.chapter "Chapter 43: Vector Databases & RAG with LangChain"

Part 6: AI Native Software Development
Prerequisites: Ch40 (FastAPI for Agents), Ch34-36 (Agent SDKs), Docker
Running example: Task API extended with semantic search
Target proficiency: B1 (Intermediate)
Technology stack: LangChain + Qdrant + OpenAI text-embedding-3-small
Skill-First pattern with student skill name: rag-deployment
9 lessons (L00-L08) covering 8 RAG architecture patterns

Complete it autonomously from phase a to all parts of phase b no execution gates.
```

## Response snapshot

Created complete Chapter 43 with:
- Phase A: Extended building-rag-systems skill with LangChain patterns, 8 RAG architectures, and evaluation patterns
- Phase B: Full chapter implementation (10 files, ~180KB content)

Key deliverables:
1. 9 lessons (L00-L08) teaching RAG from conceptual foundations to advanced patterns
2. Skill-First approach with `rag-deployment` skill created in L00
3. Running example integrating with Task API from Chapter 40
4. 8 RAG architecture patterns: Simple, +Memory, Branched, HyDE, Adaptive, CRAG, Self-RAG, Agentic
5. Evaluation with LangSmith and RAGAS metrics

## Outcome

- Impact: Complete Part 6 chapter adding knowledge retrieval to agent services
- Tests: 2/2 validators passed (educational-validator, factual-verifier)
- Files: 18 files created/modified (10 lessons + 4 specs + 4 skill references)
- Next prompts: None - chapter complete
- Reflection: Parallel content-implementer agents reduced implementation time significantly

## Evaluation notes (flywheel)

- Failure modes observed: RAGAS imports used deprecated lowercase patterns (fixed in validation phase)
- Graders run and results (PASS/FAIL): educational-validator PASS, factual-verifier PASS (after fix)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Consider pre-validating volatile API imports before content generation
