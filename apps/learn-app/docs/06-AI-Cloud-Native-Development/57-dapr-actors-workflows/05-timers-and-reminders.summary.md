### Core Concept
Timers and reminders let actors schedule work; timers run while the actor is active, reminders persist across restarts and reactivations for durable scheduling.

### Key Mental Models
- **Timer vs reminder**: Timers are volatile and in-memory; reminders are persisted and survive crashes/idle GC.
- **Per-actor scheduling**: Each actor owns its timers/reminders tied to its identity and state.
- **Idempotent handlers**: Scheduled callbacks may replay; design to handle duplicates safely.

### Critical Patterns
- Register timers for short-lived, in-activation tasks; use reminders for durable deadlines and retries.
- Keep handlers quick and offload heavy work to other actors/services to avoid blocking turn-based processing.
- Store schedule metadata in actor state to coordinate or cancel reminders predictably.
- Use `receive_reminder` to update state and emit events when deadlines fire.

### Common Mistakes
- Using timers for critical jobs that must survive restarts.
- Performing long or blocking work in callbacks, delaying other messages.
- Failing to make reminder logic idempotent, causing double-processing on retries.

### Connections
- **Builds on**: Actor state management.
- **Leads to**: Communication and workflow coordination patterns using scheduled signals.
