---
id: 0178
title: "Chapter 43: Refactor to OpenAI Agents SDK"
stage: general
date: 2025-12-30
surface: claude-code
model: claude-opus-4-5-20251101
feature: chapter-43-refactor
branch: refactor/ch43-openai-agents-sdk
user: mjs
command: /sp.git.commit_pr
labels: [refactor, chapter-43, openai-agents-sdk, langchain, rag]
links:
  spec: specs/chapter-43-vector-databases-rag-langchain/spec.md
  ticket: N/A
  adr: N/A
  pr: https://github.com/panaversity/agentfactory/pull/601
files:
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/05-building-retrieval-chains.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/08-rag-architecture-patterns-capstone.md
  - apps/learn-app/docs/06-AI-Native-Software-Development/43-vector-databases-rag-langchain/README.md
tests:
  - educational-validator: PASS (both L05 and L08)
---

## Prompt

```
User asked to refactor Chapter 43 to use:
- LangChain: Only for ingestion and retrieval (document loading, embeddings, similarity_search)
- OpenAI Agents SDK: For all LLM calls, agent orchestration, RAG patterns

User quote: "Yes and we can use Open AI Agents SDK for all LLM calls this makes it bare simple
so openAI Agents SDK for llm calls + agent rag etc. and langchain for retrieval and ingestion
this is gold"
```

## Response snapshot

Refactored Chapter 43 with clean architecture separation:

**Files rewritten:**
- L05: "Building Retrieval Chains" → "RAG with OpenAI Agents SDK"
- L08: All 8 RAG patterns reimplemented with Agents SDK (no LCEL/LangGraph)
- README: Added architecture table

**Architecture:**
| Layer | Technology |
|-------|------------|
| Data | LangChain (loaders, splitters, embeddings, Qdrant) |
| Intelligence | OpenAI Agents SDK (@function_tool, Agent, Runner) |
| Evaluation | RAGAS/LangSmith (unchanged) |

**Pattern transformation:**
```python
# Before (LCEL chain)
chain = {"context": retriever | format_docs} | prompt | llm

# After (Agents SDK)
@function_tool
def search_docs(query: str) -> str:
    return format_docs(vector_store.similarity_search(query, k=4))

agent = Agent(name="RAG", tools=[search_docs])
```

## Outcome

- Impact: Cleaner architecture, students use SDK they learned in Ch34
- Tests: educational-validator PASS on both refactored lessons
- Files: 3 files modified (+1124, -1003 lines)
- Next prompts: None - refactor complete
- Reflection: Clean separation of concerns makes RAG patterns much simpler to understand

## Evaluation notes (flywheel)

- Failure modes observed: None - clean refactor
- Graders run and results (PASS/FAIL): educational-validator PASS (after removing "Congratulations" line from L08)
- Prompt variant (if applicable): User-initiated architecture change request
- Next experiment (smallest change to try): Consider this architecture pattern for future RAG chapters
