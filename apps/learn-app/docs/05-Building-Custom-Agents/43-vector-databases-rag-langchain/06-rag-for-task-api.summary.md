### Core Concept
Integrate RAG into FastAPI: TaskVectorStore service handles indexing and search, `/tasks/search/semantic` endpoint exposes semantic search, auto-index on CRUD operations keeps vector store synchronized. Combine structured filters (status, priority) with semantic similarity.

### Key Mental Models
- **Service layer separation**: TaskVectorStore encapsulates Qdrant logic
- **Auto-indexing pattern**: Index on create, update on change, delete on remove
- **Combined filters**: Semantic similarity + metadata constraints (status=pending + "deployment")
- **Background indexing**: Use BackgroundTasks for non-blocking writes

### Critical Patterns
- Service init: `_ensure_collection()` creates if not exists
- Index task: `Document(page_content=..., metadata={task_id, title, status, priority})`
- Semantic endpoint: `POST /tasks/search/semantic?query=deployment&status=pending`
- Backfill: Migration script indexes existing database tasks

### AI Collaboration Keys
- Add hybrid search combining BM25 + dense vectors
- Implement re-ranking for better result ordering
- Handle task updates and deletes for consistency

### Common Mistakes
- Not indexing existing tasks (semantic search returns nothing)
- Missing metadata in documents (filters silently fail)
- Synchronous indexing blocking responses (use background tasks)

### Connections
- **Builds on**: Building Retrieval Chains (Lesson 5)
- **Leads to**: Evaluating RAG Quality (Lesson 7)
