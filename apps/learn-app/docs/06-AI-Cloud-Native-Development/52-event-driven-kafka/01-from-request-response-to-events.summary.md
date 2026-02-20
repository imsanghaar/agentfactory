### Core Concept
Direct API calls between services create tight coupling through temporal, availability, and behavioral dependencies that cascade failures and slow response times; asynchronous events solve these problems by treating messages as immutable facts.

### Key Mental Models
- Coupling as Architecture Debt: Coupling is baked into request-response, not a code quality issue
- Three Coupling Types: Temporal (both must be running), availability (chain availability multiplies), behavioral (caller knows callee's interface)
- Events as Facts: Past-tense immutable records vs imperative commands
- Fire and Forget: Producer announces facts without waiting for consumers

### Critical Patterns
- Cascading failure chain: one slow service blocks entire request path
- Availability math: 3 services at 99.9% = 99.7% combined (4x more downtime)
- Event-driven decoupling: Task API publishes event, consumers react independently
- Sync for queries, async for side effects

### AI Collaboration Keys
- Analyze your architecture for coupling types (temporal, availability, behavioral)
- Redesign synchronous calls as events while questioning if async is appropriate
- Calculate availability impact to build business cases for architectural change

### Common Mistakes
- Treating coupling as a code quality issue rather than architectural constraint
- Using events for operations that require immediate synchronous response
- Forgetting that event-driven adds eventual consistency complexity

### Connections
- **Builds on**: Lesson 0 - Kafka skill foundation
- **Leads to**: Lesson 2 - Event-Driven Architecture Concepts
