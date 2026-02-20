### Core Concept
Build a first Dapr virtual actor end-to-end—define its interface, implement behavior and state, register it with FastAPI, and invoke it through Dapr so each actor instance owns isolated, persistent state.

### Key Mental Models
- **Four-piece pattern**: Interface → implementation → registration → invocation; missing any piece breaks actor routing.
- **Dual naming**: Python methods use snake_case; `@actormethod` names (PascalCase) are what callers invoke.
- **State isolation**: Each actor ID maps to its own state keys; `_on_activate` initializes defaults per actor.
- **Sidecar mediation**: DaprActor adds system endpoints; ActorProxy talks to the sidecar, not directly to the app.

### Critical Patterns
- Define interfaces with `ActorInterface` and `@actormethod`, then implement with `Actor`, lifecycle hooks, and `_state_manager`.
- Register actors on startup with `DaprActor(app).register_actor(...)` and verify via `/dapr/config`.
- Invoke actors with `ActorProxy.create(type, ActorId, Interface)` inside HTTP handlers.
- Configure the state store with `actorStateStore: "true"` to persist actor state.

### Common Mistakes
- Missing `@actormethod` decorators or misnaming them, causing invocation failures.
- Forgetting `actorStateStore: true`, leading to silent state loss.
- Omitting `_on_activate` initialization, resulting in key errors or inconsistent state.

### Connections
- **Builds on**: Actor model concepts from Lesson 1.
- **Leads to**: Actor state patterns, communication, timers/reminders, and observability in later lessons.
