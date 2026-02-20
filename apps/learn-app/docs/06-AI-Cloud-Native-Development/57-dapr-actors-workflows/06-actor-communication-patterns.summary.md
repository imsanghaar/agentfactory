### Core Concept
Actors collaborate by messaging each other through proxies, enabling composition without shared state while preserving turn-based concurrency per actor.

### Key Mental Models
- **Proxy-to-actor messaging**: Use `ActorProxy`/invocation APIs instead of direct state access.
- **Pipelines vs fan-out**: Chain calls for ordered workflows or parallelize across actors when state is independent.
- **Backpressure awareness**: Each actor processes sequentially; avoid unbounded caller fan-out that overloads a callee.

### Critical Patterns
- Invoke other actors with typed interfaces; pass minimal payloads and avoid leaking internal state structures.
- Use fire-and-forget patterns for notifications; await responses when state consistency is required.
- Aggregate results by coordinating actor collects (e.g., orchestrator actor fans out and gathers).
- Handle timeouts/retries explicitly to avoid caller blocking indefinitely.

### Common Mistakes
- Tight coupling through shared keys or bypassing proxies.
- Creating call cycles or unbounded recursion between actors.
- Overloading a single actor with too many concurrent requests without rate limits or queuing strategy.

### Connections
- **Builds on**: State, timers/reminders.
- **Leads to**: Event-driven actors and workflow orchestration patterns.
