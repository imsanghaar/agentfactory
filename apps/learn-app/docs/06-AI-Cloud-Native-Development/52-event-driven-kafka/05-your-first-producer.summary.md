### Core Concept
Kafka producers use asynchronous production with delivery callbacks: `produce()` queues messages immediately, while `poll()` and `flush()` trigger callbacks that report delivery success or failure with partition and offset details.

### Key Mental Models
- Non-Blocking Produce: `produce()` returns immediately, message enters internal buffer
- Callback-Driven Confirmation: Delivery callbacks execute only when `poll()` or `flush()` is called
- Message Keys for Ordering: Same key always routes to same partition, ensuring event ordering
- Dual Verification: Callback confirms delivery; Kafka CLI verifies messages arrived

### Critical Patterns
- Producer config: `bootstrap.servers`, `client.id`, and `acks` settings
- Delivery callback: receives `err` (error or None) and `msg` (topic, partition, offset)
- `poll(0)` after produce: non-blocking callback processing
- `flush()` before exit: block until all messages delivered

### AI Collaboration Keys
- Debug silent producers (missing poll/flush calls)
- Design message key strategy balancing ordering guarantees vs parallelism
- Add robust error handling to delivery callbacks for production resilience

### Common Mistakes
- Forgetting `poll()` after `produce()` (callbacks never execute)
- Not calling `flush()` before program exit (messages may be lost)
- Producing without message keys (lose ordering guarantees)
- Missing delivery callback (blind to failures)

### Connections
- **Builds on**: Lesson 4 - Running Kafka cluster with Strimzi
- **Leads to**: Lesson 6 - Producer Reliability Deep Dive
