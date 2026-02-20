### Core Concept
Kafka offers three delivery semantics (at-most-once, at-least-once, exactly-once) with at-least-once plus idempotent consumers being the recommended pattern for most use cases, providing reliability without the complexity and latency overhead of exactly-once transactions.

### Key Mental Models
- At-Most-Once: Commit before process; fast but messages can be lost
- At-Least-Once: Process before commit; safe but duplicates possible
- Exactly-Once: Transactional coordination; correct but complex and expensive
- Idempotent Consumer: Same message processed multiple times yields same result

### Critical Patterns
- Deduplication with idempotency key: Redis/cache to track processed event IDs
- Database upsert: `ON CONFLICT DO UPDATE` using natural key for CRUD operations
- Version/state check: `UPDATE WHERE status = 'pending'` for state transitions
- Decision framework: Can you lose? -> Can consumer be idempotent? -> Use at-least-once

### AI Collaboration Keys
- Analyze processing requirements to determine appropriate semantic per event type
- Design idempotency for external API calls that don't support idempotency keys
- Evaluate exactly-once vs idempotent consumer trade-offs for specific architecture

### Common Mistakes
- Using exactly-once when at-least-once with idempotent consumer suffices
- Forgetting that exactly-once only works within Kafka transactions
- Not testing idempotency under failure conditions (kill mid-processing)
- Auto-commit with slow processing (at-most-once when at-least-once intended)

### Connections
- **Builds on**: Lesson 10 - Schema-based serialization for reliable message contracts
- **Leads to**: Lesson 12 - Transactions and exactly-once implementation
