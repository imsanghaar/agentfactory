### Core Concept
The Saga pattern coordinates multi-service transactions through event choreography where each service reacts independently, with explicit compensation events that undo work when downstream steps fail.

### Key Mental Models
- **Saga vs distributed transaction**: Saga embraces eventual consistency with compensation; distributed transactions block resources and fail in microservices
- **Choreography vs orchestration**: Choreography has services react to events with no coordinator; orchestration has central coordinator directing each step
- **Compensation symmetry**: Every forward action must have corresponding compensation - not always exact reversal (can't unsend email, but can send correction)
- **Saga state tracking**: Track saga progress by consuming all saga-related events and updating state machine per saga_id

### Critical Patterns
- Forward events: `task.created` -> `user.assigned` -> `notification.sent`
- Failure triggers compensation chain: `notification.failed` -> `user.unassigned` -> `task.marked.failed`
- Each event carries `saga_id` linking all events in one saga instance
- Compensations must be idempotent - safe to execute multiple times if compensation itself fails
- Dead letter queue for compensations that fail after max retries - requires manual intervention

### AI Collaboration Keys
- Use AI to design compensation events for each saga step, distinguishing direct reversals from semantic corrections
- Ask AI to handle tricky scenarios where compensation is impossible (email already sent)
- Leverage AI to map saga pattern to your specific domain with appropriate forward and compensation events

### Common Mistakes
- Attempting distributed transactions (2PC) across services instead of accepting eventual consistency
- Forgetting to design compensation for each forward step before implementing
- Making compensations non-idempotent, causing issues when compensation is retried

### Connections
- **Builds on**: Lesson 16 (Agent Event Patterns - event schemas, correlation tracking)
- **Leads to**: Lesson 18 (Production Kafka with Strimzi - deploying reliable Kafka for saga coordination)
