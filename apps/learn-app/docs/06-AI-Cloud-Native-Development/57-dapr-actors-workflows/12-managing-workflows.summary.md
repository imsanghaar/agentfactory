### Core Concept
Managing workflows means controlling their lifecycle—start, query, raise events, suspend, and terminate—while monitoring health and progress for long-running operations.

### Key Mental Models
- **Lifecycle API**: Scheduling, querying state, event injection, and termination are first-class operations.
- **External signaling**: Events let outside systems influence in-flight workflows without breaking determinism.
- **Operational visibility**: Status, history, and failure reasons are part of management, not just code.

### Critical Patterns
- Use `DaprWorkflowClient` to start workflows, fetch state, raise events, and terminate when needed.
- Store correlation IDs and workflow instance IDs to connect requests with executions.
- Implement idempotent event handlers to handle duplicate signals.
- Expose health/status endpoints or dashboards showing runtime status and failures.

### Common Mistakes
- Losing track of instance IDs, making remediation impossible.
- Raising events with wrong names/payloads, causing silent failures.
- Terminating workflows without cleanup/compensation, leaving partial side effects.

### Connections
- **Builds on**: Workflow authoring.
- **Leads to**: Fan-out/fan-in, saga, monitor patterns where management actions are frequent.
