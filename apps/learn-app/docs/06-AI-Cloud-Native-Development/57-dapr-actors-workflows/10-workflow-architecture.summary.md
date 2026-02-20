### Core Concept
Workflow architecture separates orchestration from execution: a deterministic workflow runtime coordinates registered workflows and activities, backed by storage for durability and an API surface for control.

### Key Mental Models
- **Runtime components**: Workflow host, storage, activity workers, and client API form the system.
- **Boundary of determinism**: Orchestrator code must be replay-safe; activities own side effects.
- **Operational hooks**: Health, scaling, and persistence are part of the architecture, not afterthoughts.

### Critical Patterns
- Register workflows and activities with `WorkflowRuntime`, start/shutdown with app lifecycle hooks.
- Use workflow storage (e.g., state store) for progress checkpoints; ensure it’s resilient.
- Expose management endpoints via `DaprWorkflowClient` for start/query/terminate and event injection.
- Plan scaling: more activity workers for throughput; keep orchestrator light to avoid bottlenecks.

### Common Mistakes
- Mixing non-deterministic logic into workflows, forcing replay failures.
- Neglecting persistence configuration, leading to lost progress on restarts.
- Overloading orchestrator with heavy work instead of scaling activities.

### Connections
- **Builds on**: Workflow overview.
- **Leads to**: Authoring workflows, managing, and applying patterns (fan-out, saga, monitors).
