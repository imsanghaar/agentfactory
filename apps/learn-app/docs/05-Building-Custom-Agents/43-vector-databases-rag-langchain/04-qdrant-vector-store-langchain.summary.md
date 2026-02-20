### Core Concept
Qdrant stores vectors and enables semantic search. Three initialization patterns: in-memory (testing), Docker (development), from_existing (production reconnect). Three retrieval modes: dense (semantic), sparse (keywords), hybrid (both). Metadata filtering combines vector similarity with structured constraints.

### Key Mental Models
- **Vector database purpose**: Store embeddings, search by similarity
- **Retrieval modes**: Dense = meaning, Sparse = keywords, Hybrid = both
- **Metadata filtering**: Vector similarity + structured constraints (status, priority)
- **Score interpretation**: Higher = more similar; threshold filters weak matches

### Critical Patterns
- Docker deploy: `docker run -p 6333:6333 -v $(pwd)/qdrant_data:/qdrant/storage qdrant/qdrant`
- In-memory init: `QdrantClient(":memory:")` for tests
- Add documents: `vector_store.add_documents(documents=docs, ids=uuids)`
- Similarity search: `vector_store.similarity_search_with_score(query, k=3)`
- Metadata filter: `filter=models.Filter(must=[models.FieldCondition(...)])`

### AI Collaboration Keys
- Debug vector size mismatch (1536 for text-embedding-3-small)
- Compare retrieval modes for specific query patterns
- Design hybrid search for production mixed-intent queries

### Common Mistakes
- Wrong vector size in collection config (mismatch with embedding model)
- Forgetting persistence volume (data lost on restart)
- Over-fetching (k=50 wastes tokens, confuses LLM)

### Connections
- **Builds on**: LangChain Document Processing (Lesson 3)
- **Leads to**: Building Retrieval Chains (Lesson 5)
