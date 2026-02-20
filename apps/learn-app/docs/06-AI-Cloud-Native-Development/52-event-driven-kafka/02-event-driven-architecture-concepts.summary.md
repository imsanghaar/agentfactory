### Core Concept
Event-driven architecture relies on the fundamental distinction between events (immutable past-tense facts) and commands (imperative requests), with eventual consistency as an acceptable trade-off for most business scenarios.

### Key Mental Models
- Events vs Commands: Past-tense naming (`TaskCreated`) vs imperative (`CreateTask`); facts vs requests
- Eventual Consistency: Changes propagate through events with acceptable delay; humans already accept delays (direct deposits, stock settlements)
- Event Sourcing: Store events as source of truth, rebuild state by replaying
- CQRS: Separate read and write models for independent optimization

### Critical Patterns
- Event naming convention: `OrderCreated`, `PaymentProcessed` (past tense, immutable facts)
- Command naming: `CreateOrder`, `ProcessPayment` (imperative, can fail)
- Eventual consistency acceptable when correct eventual state matters more than instant consistency
- Strong consistency required for limited inventory, real-time trading, reservations

### AI Collaboration Keys
- Classify scenarios as events or commands with proper naming conventions
- Evaluate consistency requirements for ticket booking, checkout flows
- Design event schemas balancing consumer needs without coupling

### Common Mistakes
- Events that are really commands ("Please process this order" as event)
- Synchronous semantics over events (blocking until event processed)
- Event schema coupled to consumer needs rather than producer's domain
- Using events for request-response queries

### Connections
- **Builds on**: Lesson 1 - Coupling problems and event-driven alternative
- **Leads to**: Lesson 3 - Kafka Mental Model
