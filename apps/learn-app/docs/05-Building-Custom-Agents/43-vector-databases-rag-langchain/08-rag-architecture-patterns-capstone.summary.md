### Core Concept
Eight RAG architectures for different requirements: Simple, Memory, Branched, HyDE, Adaptive, CRAG, Self-RAG, Agentic. LangChain handles retrieval; OpenAI Agents SDK handles orchestration. Pattern selection depends on query complexity, accuracy requirements, and domain needs.

### Key Mental Models
- **Pattern spectrum**: Simple (fast) → Agentic (thorough, multi-step)
- **LangChain + Agents SDK split**: Retrieval vs orchestration responsibilities
- **Pattern composition**: Combine Memory + CRAG + Adaptive for production
- **Tradeoff analysis**: Latency vs accuracy vs complexity

### Critical Patterns
- Simple RAG: Agent + search_docs tool, single retrieval
- Memory RAG: SQLiteSession for multi-turn context
- HyDE: Generate hypothesis → search with hypothesis → refine answer
- CRAG: Grade docs → search_broader if low relevance → acknowledge uncertainty
- Agentic: Triage agent → specialist handoffs based on query type

### AI Collaboration Keys
- Select architecture based on domain requirements
- Combine patterns for production systems
- Add evaluation instrumentation to track performance

### Common Mistakes
- Using simple RAG for complex domains (insufficient accuracy)
- Over-engineering simple FAQ systems (unnecessary latency)
- Not handling uncertainty (CRAG pattern prevents confident wrong answers)

### Connections
- **Builds on**: Evaluating RAG Quality (Lesson 7) + all L01-L06 patterns
- **Leads to**: Chapter 44 (Relational Databases & SQLModel) / Production deployment
