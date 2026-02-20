### Core Concept
Author workflows with deterministic, yield-based orchestration that sequences activities, handles retries, and models long-running business processes safely.

### Key Mental Models
- **Workflow as state machine**: Each yield advances state; runtime persists progress.
- **Input/output contracts**: Strong typing for workflow inputs/outputs and activities reduces replay surprises.
- **Retry/timeout discipline**: Build resilience into each activity call.

### Critical Patterns
- Decorate workflows/activities, register them, and implement orchestration using `ctx.call_activity` and `ctx.current_utc_datetime`.
- Validate and serialize inputs/outputs; avoid non-deterministic calls inside workflows.
- Configure per-step retry policies and timeouts; branch on activity results for control flow.
- Use compensation or status markers to model failure paths.

### Common Mistakes
- Using `datetime.now()`/random/HTTP inside workflows instead of activities.
- Forgetting to register functions or mismatching names, causing runtime invocation errors.
- Ignoring error handling, leaving workflows stuck on transient failures.

### Connections
- **Builds on**: Workflow architecture and overview.
- **Leads to**: Managing workflows, fan-out patterns, saga/monitor workflows.
