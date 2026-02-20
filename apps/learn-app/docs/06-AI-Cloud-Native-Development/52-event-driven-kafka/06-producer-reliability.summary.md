### Core Concept
Production-grade Kafka producers require proper acknowledgment levels (`acks=all` for durability), idempotent configuration to prevent duplicates during retries, and robust delivery failure handling with retry and dead-letter queue patterns.

### Key Mental Models
- Acks Spectrum: `acks=0` (fire and forget), `acks=1` (leader only), `acks=all` (all in-sync replicas)
- Idempotent Producer: Sequence numbers prevent duplicates during network retries
- Latency-Durability Trade-off: 5-20ms extra for `acks=all` vs `acks=1`
- Retriable vs Fatal Errors: Network issues retry automatically; authorization failures need intervention

### Critical Patterns
- `acks=all` + `enable.idempotence=True` for critical business events
- `max.in.flight.requests.per.connection &lt;= 5` required for idempotence
- `delivery.timeout.ms` controls total retry window
- Dead letter queue pattern for permanently failed messages

### AI Collaboration Keys
- Analyze use cases to determine appropriate acks level per event type
- Debug NOT_ENOUGH_REPLICAS errors (ISR below min.insync.replicas)
- Design error handling strategy with proper logging, DLQ, and metrics

### Common Mistakes
- Using `acks=0` or `acks=1` for critical business data
- Setting `max.in.flight > 5` which disables idempotence
- Not distinguishing retriable from fatal errors in callbacks
- Missing retry configuration (`retries`, `retry.backoff.ms`, `delivery.timeout.ms`)

### Connections
- **Builds on**: Lesson 5 - Basic producer with delivery callbacks
- **Leads to**: Lesson 7 - Your First Consumer
