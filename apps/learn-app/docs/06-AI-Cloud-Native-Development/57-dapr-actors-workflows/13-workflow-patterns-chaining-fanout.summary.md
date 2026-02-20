### Core Concept
Chaining and fan-out/fan-in patterns let workflows sequence dependent steps and run parallel tasks with structured aggregation and retries.

### Key Mental Models
- **Chaining**: Linear steps where each output feeds the next; failures short-circuit or trigger compensation.
- **Fan-out/fan-in**: Parallel activity calls collected via `when_all`/aggregation to improve throughput.
- **Deterministic coordination**: Orchestration logic remains pure while activities handle side effects.

### Critical Patterns
- Implement sequential chains with clear inputs/outputs and per-step retries/timeouts.
- Use `when_all` or equivalent to launch parallel activities and join results; handle partial failures.
- Limit fan-out concurrency and add backpressure to avoid overwhelming downstream systems.
- Record progress in workflow state to resume safely on replay.

### Common Mistakes
- Over-parallelizing without limits, causing thundering herds.
- Ignoring partial failures in fan-in, leading to inconsistent aggregate results.
- Doing aggregation with non-deterministic code (e.g., unordered dict iteration) and breaking replay.

### Connections
- **Builds on**: Workflow authoring/management.
- **Leads to**: Saga and monitor patterns, combining chains and parallelism with compensation.
