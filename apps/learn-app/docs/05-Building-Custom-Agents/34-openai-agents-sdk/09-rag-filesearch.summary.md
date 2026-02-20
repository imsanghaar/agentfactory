### Core Concept
Agentic RAG lets agents decide when to retrieve from knowledge bases rather than searching for every prompt. FileSearchTool connects to OpenAI vector stores, enabling grounded responses that cite specific documents.

### Key Mental Models
- **Agentic vs Traditional RAG**: Agent reasons about whether retrieval is needed—doesn't blindly search every time
- **Vector stores = Semantic search**: Find documents by meaning, not exact keyword matches
- **Grounding = Traceability**: Responses cite source documents, proving answers aren't hallucinated

### Critical Patterns
- Create vector store via OpenAI dashboard or API → Get `vs_xxx` ID
- Configure tool: `FileSearchTool(vector_store_ids=["vs_xxx"], max_num_results=5)`
- Add to agent: `Agent(tools=[file_search])`
- Upload files: `client.beta.vector_stores.files.upload(vector_store_id, file)`

### AI Collaboration Keys
- Instruct agents when to search: "YES for policy questions, NO for general knowledge"
- Always require citations: "Reference the source document in your response"

### Common Mistakes
- Retrieving for every prompt (wastes tokens and adds latency)
- Setting max_num_results too high (exceeds context limits)
- Not citing sources (loses the trust benefit of RAG)

### Connections
- **Builds on**: MCP integration (Lesson 8)
- **Leads to**: Capstone customer support system (Lesson 10)
