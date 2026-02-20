### Core Concept
Kafka transactions wrap multiple writes across topics into atomic units, ensuring all-or-nothing semantics for stream processing with exactly-once delivery through transactional producers, consumer isolation, and zombie fencing.

### Key Mental Models
- **Transaction lifecycle**: `init_transactions()` -> `begin_transaction()` -> produce messages -> `commit_transaction()` or `abort_transaction()`
- **Zombie fencing**: Epoch-based mechanism where `transactional.id` ensures crashed producers cannot commit stale transactions
- **Read-process-write atomicity**: Entire consume-transform-produce cycle wrapped in single transaction prevents partial failures
- **ISR isolation**: Consumers with `isolation.level=read_committed` only see messages from committed transactions

### Critical Patterns
- Transactional producer requires unique, stable `transactional.id` per instance (include service name + partition)
- Call `init_transactions()` exactly once per producer lifecycle before any transactional operations
- Consumer `isolation.level=read_committed` prevents reading uncommitted or aborted messages
- Batch multiple operations in single transaction to reduce commit overhead (10-50ms per commit)
- Transaction timeout default is 60 seconds - keep transactions short or increase `transaction.timeout.ms`

### AI Collaboration Keys
- Use AI to evaluate which writes need atomicity versus simpler idempotent patterns
- Ask AI to analyze failure scenarios for your specific read-process-write workflows
- Leverage AI to design proper `transactional.id` naming schemes for horizontally-scaled processors

### Common Mistakes
- Using same `transactional.id` across multiple producer instances causes fencing conflicts
- Forgetting to abort transaction on errors leaves messages in uncommitted state blocking consumers
- Creating transaction per message instead of batching, causing excessive commit overhead

### Connections
- **Builds on**: Lesson 11 (Delivery Semantics - idempotent producers, at-least-once/at-most-once)
- **Leads to**: Lesson 13 (Reliability Configuration - ISR, min.insync.replicas)
