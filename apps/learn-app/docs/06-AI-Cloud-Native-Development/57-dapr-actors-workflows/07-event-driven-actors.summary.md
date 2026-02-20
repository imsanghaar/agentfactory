### Core Concept
Actors can react to events by combining pub/sub with actor invocation, letting stateful entities consume streams without embedding broker logic in the actor.

### Key Mental Models
- **Inbox via pub/sub**: Subscriptions route topic messages to endpoints that dispatch into actors.
- **Decouple producers**: Events carry minimal data; actors enrich using their own state.
- **At-least-once handling**: Event delivery may repeat—idempotent actor methods are mandatory.

### Critical Patterns
- Create Dapr Subscriptions to map topics to HTTP handlers that invoke actor methods (via `ActorProxy`).
- Validate and sanitize event payloads before state mutation; persist checkpoints in actor state if needed.
- Use actor IDs derived from event attributes (e.g., user/task IDs) to route to the right instance.
- Publish events from actors for downstream services, keeping actor methods thin.

### Common Mistakes
- Putting broker client code inside actors instead of using Dapr pub/sub.
- Assuming exactly-once delivery and writing non-idempotent handlers.
- Overloading a single actor with unbounded event rates without backpressure or buffering.

### Connections
- **Builds on**: Actor communication patterns.
- **Leads to**: Actor observability and workflow/event orchestration patterns.
