### Core Concept
Saga and monitor patterns add resilience to workflows: sagas pair each step with compensation for partial failures, while monitors loop to watch and react to long-running conditions.

### Key Mental Models
- **Saga compensation**: For every forward action, define a compensating step to undo/mitigate on failure.
- **Monitor loop**: Periodically check state/SLAs and continue-as-new to avoid history bloat.
- **Idempotent compensations**: Rollbacks may run multiple times; design them to be safe.

### Critical Patterns
- Model sagas with try/compensate branches; store progress to know which compensations to run.
- Use `continue_as_new` or similar to truncate history in monitor workflows and keep them long-lived.
- Add alerts/events when monitors detect breaches (timeouts, stalled states).
- Keep compensations side-effect-aware and reversible where possible.

### Common Mistakes
- Forgetting compensations or making them non-idempotent, causing additional errors during rollback.
- Letting monitor workflows accumulate unbounded history instead of renewing.
- Ignoring partial completion states, leading to double-charging or resource leaks.

### Connections
- **Builds on**: Chaining/fan-out and workflow management.
- **Leads to**: Combining actors and workflows and multi-app orchestration patterns.
