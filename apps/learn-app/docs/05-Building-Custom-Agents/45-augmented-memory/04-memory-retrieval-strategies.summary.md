### Core Concept
Storing memories is only half the problem; retrieval determines whether agents surface the right context. Four strategies (recency, relevance, entity, hybrid) address different query types, all constrained by token budgets.

### Key Mental Models
- Different strategies serve different needs: recency for continuity, relevance for specific questions, entity for focused topics
- Hybrid retrieval combines multiple strategies with weighted scoring to handle ambiguous queries
- Token budget is a hard constraint: you cannot inject more memories than the context window allows
- Query classification determines which strategy to use for optimal results

### Critical Patterns
- Recency-based: sort by `created_at` DESC, best for "what we just discussed" queries
- Relevance-based: vector similarity search, best for specific factual lookups
- Entity-based: extract entities from query, retrieve all memories mentioning those entities
- Hybrid retrieval: combine all three with `calculate_hybrid_score()` using weighted formula
- Token-aware selection: iterate through sorted memories, accumulating until budget exhausted

### AI Collaboration Keys
- Use AI to design query classifiers that determine strategy selection
- Have AI create token budget optimization algorithms balancing relevance vs diversity
- Practice entity extraction and relationship traversal for domain-specific agents (CRM, project management)

### Common Mistakes
- Using only semantic search, missing recent context that is highly relevant
- Ignoring token budgets and trying to inject too many memories
- Not deduplicating when combining multiple retrieval strategies

### Connections
- **Builds on**: Lesson 3 - What to Remember and Forget (relevance scoring concepts)
- **Leads to**: Lesson 5 - Context Window Management (managing what gets injected)
