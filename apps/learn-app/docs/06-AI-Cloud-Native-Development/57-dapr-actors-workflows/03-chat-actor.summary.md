### Core Concept
Map each chat session to a Dapr actor that owns its conversation history, processes messages sequentially, and emits pub/sub events so stateful AI interactions stay isolated per user while other services react to updates.

### Key Mental Models
- **Per-user actor isolation**: ActorId gives each session its own state and mailbox; no cross-talk.
- **Interface-first contract**: Pydantic models and `@actormethod` names define the surface clients call.
- **Evented actors**: Actors can publish to pub/sub on state changes to fan out conversation updates.

### Critical Patterns
- Implement ChatActor with `_on_activate` initialization, bounded history, and validation via Pydantic.
- Use `ActorProxy.create("ChatAgent", ActorId, Interface)` in FastAPI endpoints for `ProcessMessage` and `GetConversationHistory`.
- Limit stored history (e.g., last 20 messages) and serialize safely before writing to the state store.
- Publish `ConversationUpdated` events from within actor methods using `DaprClient.publish_event`; subscribe via a Dapr Subscription routed to `/subscribe`.

### Common Mistakes
- Forgetting to validate input before persisting, risking bad history data.
- Allowing unbounded history growth, inflating state store size.
- Misaligned `@actormethod` names vs method calls, causing invocation errors.
- Publishing without handling JSON encoding or exceptions, hiding failures.

### Connections
- **Builds on**: Hello Actor patterns from Lesson 2.
- **Leads to**: Actor state management, timers/reminders, and observability in subsequent lessons.
