### Core Concept
Good memory systems are selective: they prioritize what matters, compress what is old, and delete what should not exist. Relevance scoring, consolidation, and GDPR-compliant forgetting are essential for production memory systems.

### Key Mental Models
- Relevance scoring combines semantic similarity, recency decay, and access frequency with domain-specific weights
- Consolidation is lossy compression: detailed memories become summaries over time while preserving patterns
- Active forgetting is a capability, not a failure; some information must be deleted, not just deprioritized
- Contradictions are not always errors; sometimes they represent legitimate evolution of preferences over time

### Critical Patterns
- Relevance formula: `score = w1*semantic + w2*recency + w3*frequency` with weights tuned per agent type
- Time-based consolidation: daily -> weekly -> monthly -> yearly summaries with triggered thresholds
- GDPR Article 17 compliance: complete user deletion upon request with audit logging
- Contradiction resolution strategies: timestamp-based (newer wins), explicit update (user confirms), version history

### AI Collaboration Keys
- Use AI to design relevance scoring weights for specific domains (customer support vs research agent)
- Have AI design consolidation strategies that identify what information is preserved vs lost
- Practice contradiction handling scenarios with temporal evolution of preferences

### Common Mistakes
- Storing everything without prioritization, leading to retrieval noise and storage costs
- Consolidating too aggressively and losing important details
- Ignoring privacy requirements until after deployment rather than designing for compliance

### Connections
- **Builds on**: Lesson 2 - Memory Architecture Patterns (understanding what each type stores)
- **Leads to**: Lesson 4 - Memory Retrieval Strategies (getting the right memories back)
