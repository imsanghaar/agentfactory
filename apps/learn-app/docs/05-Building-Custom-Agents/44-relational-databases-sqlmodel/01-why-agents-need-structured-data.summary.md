### Core Concept
AI agents need persistent relational databases for structured queries (filtering, aggregation, relationships) while vector databases handle semantic similarity search - most agents need both.

### Key Mental Models
- Persistence solves data loss: Memory dies with process restart
- Relational vs Vector: Structured queries vs semantic similarity
- ACID guarantees: Atomicity, Consistency, Isolation, Durability protect agent reliability
- Async enables scale: Non-blocking database access handles concurrent users

### Critical Patterns
- Use `create_async_engine` and `AsyncSession` exclusively for async agents
- Wrap related operations in transactions for atomicity
- Relational for "filter by", "count/sum", exact matches
- Vector for "similar to", fuzzy matching, context retrieval
- Often use both in production agent architectures

### AI Collaboration Keys
- Classify data types to appropriate storage (relational vs vector vs both)
- Design transaction boundaries for multi-record operations
- Justify async vs sync based on concurrency requirements

### Common Mistakes
- Using sync database access in async agents (blocks everything)
- Storing data only in memory (lost on restart)
- Using wrong database type for query pattern (vector for exact matches)

### Connections
- **Builds on**: Vector databases from Chapter 43
- **Leads to**: L02 - Database design and normalization
