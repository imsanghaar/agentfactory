### Core Concept
Agent event patterns enable decoupled AI agent communication through consistent event schemas with correlation/causation tracking, notification fanout across multiple consumer groups, and immutable audit logging.

### Key Mental Models
- **domain.action naming**: Events use past tense (`task.created`, not `CreateTask`) - facts that happened, not requests
- **Correlation ID vs Causation ID**: Correlation traces single request across all services; causation links each event to what directly triggered it
- **Notification fanout**: Multiple services subscribe to same topic with different `group.id` - each receives every event independently
- **Immutable audit log**: Append-only consumer that logs ALL events with deduplication by event_id for compliance

### Critical Patterns
- Complete event schema: `event_id`, `event_type`, `occurred_at`, `data` (domain-specific), `metadata` (correlation_id, causation_id, source)
- Task API publishes event and returns immediately - notifications happen asynchronously via consumers
- Each service uses unique `group.id`: `notification-email`, `notification-slack`, `audit-log`
- Audit consumer uses `auto.offset.reset=earliest` to never miss events; filters duplicates before appending
- Single topic per domain (`task-events`) simpler than per-event-type topics; consumers filter by `event_type`

### AI Collaboration Keys
- Use AI to design complete event schemas with proper metadata for distributed tracing requirements
- Ask AI to troubleshoot fanout issues (often `auto.offset.reset=latest` causing missed events)
- Leverage AI to translate generic event patterns to your specific domain (healthcare, e-commerce, IoT)

### Common Mistakes
- Using `auto.offset.reset=latest` for audit consumers, missing events that occurred before consumer started
- Omitting correlation_id, making cross-service debugging nearly impossible
- Adding notification logic directly to Task API instead of decoupling through events

### Connections
- **Builds on**: Lesson 15 (CDC with Debezium - domain events from database changes)
- **Leads to**: Lesson 17 (Saga Pattern - multi-step workflows with compensation events)
