### Core Concept
The Actor Model replaces shared-state concurrency with isolated actors that process messages one at a time, giving AI agents scalable, race-free state management via virtual actors that auto-activate, persist, and recover.

### Key Mental Models
- **Private state + mailbox**: Each actor owns state and a FIFO mailbox; no other actor can touch its data.
- **Turn-based concurrency**: One message at a time per actor eliminates locks and race conditions while thousands of actors run in parallel.
- **Virtual actors**: On-demand activation, automatic persistence, routing, and recovery mean you address actors by ID without lifecycle plumbing.
- **Fit for AI agents**: Per-user or per-task identity maps cleanly to actors, keeping conversation/task state isolated.

### Critical Patterns
- Use actors for entities with identity needing concurrent access, per-entity timers, and durable state (ChatActor, TaskActor).
- Let the framework handle activation/deactivation; address actors by ID rather than managing lifecycles.
- Think “across actors parallel, within actor sequential” when reasoning about throughput and correctness.

### Common Mistakes
- Trying to share state or locks between actors, which breaks the model’s guarantees.
- Choosing actors for stateless or batch workloads better served by standard services or workers.
- Forgetting determinism per actor: assume messages are processed sequentially, not concurrently.

### Connections
- **Builds on**: Dapr sidecar basics from Chapter 53.
- **Leads to**: Actor implementation, communication, timers, and reminders in later Chapter 57 lessons.
