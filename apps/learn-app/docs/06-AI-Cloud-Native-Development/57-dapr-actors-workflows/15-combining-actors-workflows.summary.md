### Core Concept
Actors manage per-entity state; workflows orchestrate cross-entity processes. Combining them lets you coordinate durable business flows while keeping entity logic isolated.

### Key Mental Models
- **Role separation**: Actors hold state and invariants; workflows sequence actions across actors/services.
- **Message boundaries**: Interact via actor proxies inside workflows; workflows should not mutate actor state directly.
- **Failure domains**: Actor failures are local; workflow failures span steps—compensation may involve multiple actors.

### Critical Patterns
- Invoke actors from workflows to read/update state; use activities to encapsulate actor calls if needed.
- Keep actor methods small and idempotent to tolerate retries from workflow orchestration.
- Use workflow compensation to reverse actor changes when later steps fail.
- Pass only necessary data between workflow and actors to reduce coupling.

### Common Mistakes
- Embedding orchestration logic inside actors, losing replay guarantees and increasing coupling.
- Making actor methods non-idempotent, causing inconsistent state on retries.
- Sharing actor state across identities instead of routing through proper ActorIds.

### Connections
- **Builds on**: Actor communication and workflow patterns.
- **Leads to**: Multi-app workflows and namespaced actors for larger systems.
