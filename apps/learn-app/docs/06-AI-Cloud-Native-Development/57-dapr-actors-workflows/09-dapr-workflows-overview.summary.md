### Core Concept
Dapr Workflows provide durable, replayable orchestration for long-running, multi-step processes, complementing actors by handling deterministic control flow and retries.

### Key Mental Models
- **Deterministic orchestrator**: Workflow code must be replay-safe; non-determinism belongs in activities.
- **Activities vs workflows**: Workflows coordinate; activities do side effects and external I/O.
- **Stateful durability**: Workflow runtime persists progress, enabling retries and restarts without manual plumbing.

### Critical Patterns
- Define workflows with decorators and yield-based `call_activity` steps; register them with `WorkflowRuntime`.
- Keep workflow logic pure: use `ctx.current_utc_datetime`, avoid randomness/HTTP; push those to activities.
- Configure retry policies on activities and handle compensation logic for failures.
- Manage workflows with `DaprWorkflowClient` for scheduling, querying, raising events, and terminating.

### Common Mistakes
- Calling external services directly from workflows, breaking determinism.
- Forgetting to register workflows/activities with the runtime, causing invocation failures.
- Skipping retry/compensation strategy, leading to partial progress on failure.

### Connections
- **Builds on**: Actor fundamentals; contrasts actors (per-entity state) with workflows (process orchestration).
- **Leads to**: Workflow architecture, authoring, management, and patterns in following lessons.
