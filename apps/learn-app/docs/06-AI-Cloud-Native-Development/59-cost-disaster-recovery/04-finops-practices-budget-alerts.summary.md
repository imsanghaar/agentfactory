### Core Concept
FinOps practices operationalize cost control through budgets, alerts, and accountability loops across engineering and finance.

### Key Mental Models
- **Inform → Optimize → Operate**: Visibility, action, governance as a cycle.
- **Ownership**: Teams own their spend and respond to budget signals.
- **Preemptive alerts**: Catch drift early with thresholds and anomaly detection.

### Critical Patterns
- Set budgets per team/product; configure alerts (Prometheus/OpenCost) on burn rates and anomalies.
- Review spend regularly with actionable reports; tie runbooks to alerts.
- Include cost checks in delivery pipelines (e.g., flag expensive changes).

### Common Mistakes
- Alerts without owners/runbooks, leading to noise.
- Budgets set without alignment to business goals or unit economics.
- Only reacting post-bill instead of monitoring daily/weekly trends.

### Connections
- **Builds on**: OpenCost visibility and labeling.
- **Leads to**: Backup/DR planning with cost-awareness and chaos testing tradeoffs.
