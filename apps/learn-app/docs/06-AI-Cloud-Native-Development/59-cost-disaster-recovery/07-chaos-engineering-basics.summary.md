### Core Concept
Chaos engineering tests resilience by safely injecting failure to validate that systems meet reliability targets and recover within SLO/RTO bounds.

### Key Mental Models
- **Hypothesis-driven**: Define expected behavior before running experiments.
- **Blast radius control**: Start small, observe, then expand.
- **Steady state**: Measure normal metrics to detect meaningful deviations.

### Critical Patterns
- Run controlled experiments (pod kill, network latency, node loss) with safeguards and rollbacks.
- Monitor SLOs/error budgets during tests; halt if breach risk is high.
- Document findings and fix gaps (readiness probes, retries, failover) before rerunning.

### Common Mistakes
- Testing without hypotheses or success criteria, yielding noise.
- Too-large blast radius causing real incidents.
- Ignoring monitoring/alerts during experiments, missing regressions.

### Connections
- **Builds on**: Backups/DR readiness and observability.
- **Leads to**: Data sovereignty/compliance considerations and capstone resilience validation.
