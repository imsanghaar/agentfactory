### Core Concept
Retrieval chains transform similarity search into intelligent answers. Flow: Query → Retriever → Format docs → Prompt → LLM → Answer. LCEL pipe syntax (`|`) chains components. Retriever wraps vector store with search configuration (k, search_type, mmr).

### Key Mental Models
- **Chain composition**: Components connect via `|` pipe operator
- **Retriever abstraction**: `vector_store.as_retriever()` wraps search for chain use
- **format_docs function**: Converts Document list to context string
- **Parallel branches**: `{context: ..., question: ...}` runs before prompt

### Critical Patterns
- Retriever: `vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 4})`
- Format: `"\n\n".join(doc.page_content for doc in docs)`
- Chain: `{"context": retriever | format_docs, "question": lambda x: x} | prompt | llm`
- Debug: Trace each component (retriever output, formatted context, filled prompt)

### AI Collaboration Keys
- Customize prompt templates for answer style
- Build conversational chains with memory
- Handle no-answer cases gracefully

### Common Mistakes
- Forgetting format_docs (passing Document list instead of string)
- Wrong k value (too few = missing info, too many = overwhelmed)
- Losing question in chain (lambda x: x passes it through)

### Connections
- **Builds on**: Qdrant Vector Store with LangChain (Lesson 4)
- **Leads to**: RAG for Task API (Lesson 6)
