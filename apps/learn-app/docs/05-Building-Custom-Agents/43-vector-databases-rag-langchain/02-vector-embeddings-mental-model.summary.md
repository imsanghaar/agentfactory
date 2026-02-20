### Core Concept
Embeddings convert text to numbers that represent meaning. "Dog" and "puppy" get similar vectors; "dog" and "democracy" get different vectors. Cosine similarity measures how close meanings are (0-1 scale). This enables semantic search: find related content even without keyword matches.

### Key Mental Models
- **GPS coordinates for meaning**: Each text gets a location in high-dimensional space
- **Semantic similarity**: Similar meanings cluster together regardless of words used
- **Cosine similarity**: 0.92 = very similar, 0.08 = unrelated
- **1536 dimensions**: text-embedding-3-small produces vectors capturing nuanced meaning

### Critical Patterns
- Embedding API call: `client.embeddings.create(input=text, model="text-embedding-3-small")`
- Same model required: Query and documents must use identical embedding model
- Chunk size matters: Long texts dilute specificity; chunk for focused embeddings
- Cluster visualization: Project to 2D to see topic groupings

### AI Collaboration Keys
- Explain semantic similarity with domain-specific examples
- Debug retrieval failures (wrong embeddings vs chunking issues)
- Choose embedding model based on domain and cost tradeoffs

### Common Mistakes
- Mixing embedding models (incompatible vector spaces)
- Thinking embeddings "understand" context (they capture moment-of-encoding meaning)
- Long documents without chunking (diluted, unfocused embeddings)

### Connections
- **Builds on**: Why Agents Need External Knowledge (Lesson 1)
- **Leads to**: LangChain Document Processing (Lesson 3)
