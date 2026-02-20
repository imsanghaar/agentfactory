### Core Concept
LLMs have training cutoffs and generic knowledge. Production agents need current, domain-specific information. RAG bridges this gap: retrieve relevant context at query time, then generate grounded answers. External knowledge transforms generic chatbots into specialized assistants.

### Key Mental Models
- **Knowledge cutoff problem**: LLMs don't know events after training (March 2023, Jan 2024)
- **Generic vs specialized**: Training data is broad; your domain needs specific details
- **Retrieval-Augmented Generation**: Retrieve first, then generate with context
- **Grounding prevents hallucination**: Answers cite sources, not imagination

### Critical Patterns
- RAG flow: Query → Retrieve documents → Format as context → Generate answer
- Context window as working memory: Retrieved docs fill prompt context
- Embedding similarity: Find semantically related content, not keyword matches
- Source attribution: Track where information came from

### AI Collaboration Keys
- Explain when RAG is needed vs when LLM knowledge suffices
- Design retrieval strategy based on query patterns
- Balance context size against token limits

### Common Mistakes
- Assuming LLM "knows" recent information (training cutoff)
- Not attributing sources (users can't verify answers)
- Stuffing too much context (overwhelms LLM, wastes tokens)

### Connections
- **Builds on**: Build Your RAG Skill (Lesson 0)
- **Leads to**: Vector Embeddings Mental Model (Lesson 2)
