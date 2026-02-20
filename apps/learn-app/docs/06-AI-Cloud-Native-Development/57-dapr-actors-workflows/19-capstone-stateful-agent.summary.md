### Core Concept
The capstone builds a production-ready stateful agent by combining actors, workflows, scheduling, and observability/security patterns into a single deployment.

### Key Mental Models
- **Integration mindset**: Every prior lesson (state, reminders, events, workflows, security, observability) must work together.
- **Spec-driven**: Define the agent’s requirements, flows, and SLIs before wiring components.
- **Validation loop**: Test functional flows and non-functional checks (latency, retries, isolation).

### Critical Patterns
- Compose actor-based state, workflow orchestration, pub/sub triggers, and reminders into the agent’s business flow.
- Instrument the agent with metrics/traces/logs and set SLO/alert thresholds.
- Apply security baselines: mTLS, NetworkPolicies, component scopes, and input validation.
- Run end-to-end tests for happy/edge paths and failover (retries, compensations).

### Common Mistakes
- Treating the capstone as code-only and skipping observability/security acceptance.
- Forgetting to tune retries/timeouts, causing stuck workflows or duplicate side effects.
- Not load-testing actor concurrency limits, leading to hidden bottlenecks.

### Connections
- **Builds on**: All Chapter 57 lessons.
- **Leads to**: Final skill refinement and application to production environments.
