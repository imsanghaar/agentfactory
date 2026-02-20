### Core Concept
Actor state is owned per actor instance and persisted through Dapr’s state manager; use consistent keys, ETags, and transactional patterns to keep data durable and race-free.

### Key Mental Models
- **State per identity**: Each `ActorId` maps to its own keys; isolation is automatic.
- **Optimistic concurrency**: ETags prevent overwrites from stale reads.
- **Persistence lifecycle**: Activation loads state; reminders/timers and calls update and flush it.

### Critical Patterns
- Initialize defaults in `_on_activate`, then read/write via `_state_manager.get_state/set_state`.
- Use ETags or transactional `save_state` to avoid clobbering concurrent updates.
- Keep state small and serializable; apply retention/compaction to bound growth.
- Separate compute from storage: let the actor orchestrate, store data in the configured state store.

### Common Mistakes
- Reusing shared keys across actors, breaking isolation.
- Ignoring ETags and losing updates when multiple messages modify the same data.
- Storing non-serializable objects or unbounded history, causing errors and bloat.

### Connections
- **Builds on**: Hello Actor patterns.
- **Leads to**: Timers/reminders, communication, and observability that rely on correct state handling.
