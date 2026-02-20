### Core Concept
Kafka consumers follow a poll-process-commit loop where the commit strategy determines message delivery guarantees: auto-commit risks message loss, while manual commit after processing provides at-least-once delivery with possible duplicates.

### Key Mental Models
- Poll Loop Pattern: Continuously call `poll()`, process messages, commit offsets
- Auto-Commit Risk: Offset committed before processing completes = message loss on crash
- Manual Commit Safety: Process first, commit after = at-least-once with possible duplicates
- Idempotent Processing: Design handlers to produce same result if message processed twice

### Critical Patterns
- Consumer config: `group.id`, `auto.offset.reset` (earliest/latest), `enable.auto.commit`
- Error handling: `_PARTITION_EOF` is informational (not error), continue polling
- Manual commit: `consumer.commit(message=msg)` after successful processing
- Graceful shutdown: Always call `consumer.close()` for fast rebalancing and offset commit

### AI Collaboration Keys
- Debug consumers losing messages (auto-commit with slow processing)
- Design idempotent processing to handle duplicate deliveries safely
- Choose commit strategy based on real-time dashboard vs audit log requirements

### Common Mistakes
- Auto-commit with slow processing (message loss on crash)
- Treating `_PARTITION_EOF` as error (it's just "caught up" signal)
- Committing before processing (message loss if processing fails)
- Forgetting `consumer.close()` (slow rebalancing, uncommitted offsets)

### Connections
- **Builds on**: Lesson 6 - Producer reliability and delivery callbacks
- **Leads to**: Lesson 8 - Consumer Groups and Rebalancing
