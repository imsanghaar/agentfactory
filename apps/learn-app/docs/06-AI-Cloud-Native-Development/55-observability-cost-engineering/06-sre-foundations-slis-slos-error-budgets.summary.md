### Core Concept
SLIs measure what users experience (availability, latency), SLOs set internal targets (99.9%), and error budgets (100% - SLO) provide currency for velocity decisions: spend on deployments when healthy, freeze when exhausted.

### Key Mental Models
- **SLI**: Quantitative measure of service level (successful_requests / total_requests = availability)
- **SLO**: Target value for SLI with buffer from typical performance; internal bar, not customer promise
- **SLA**: Contractual commitment with financial consequences; SLA &lt; SLO &lt; typical performance
- **Error Budget**: 100% - SLO = monthly unreliability allowance (99.9% SLO = 43.2 min/month)

### Critical Patterns
- Availability SLI: `sum(rate(requests{status!~"5.."}[5m])) / sum(rate(requests[5m]))`
- Error budget consumption: `error_ratio / (1 - SLO)` gives burn rate (1x = normal, 14.4x = critical)
- Budget policy: >50% ship normally, 25-50% increased review, 10-25% freeze, &lt;10% emergency
- Recording rules: Pre-compute `task_api:error_budget_remaining:ratio30d` for instant dashboards

### AI Collaboration Keys
- Ask Claude to calculate error budget impact from a 15-minute, 20% failure incident
- Request SLI design for your specific service type (API vs pipeline vs batch job)
- Have AI generate Prometheus recording rules for availability and budget tracking

### Common Mistakes
- Setting SLO at typical performance (99.97% when you usually achieve 99.97% means constant failure)
- Conflating SLO with SLA (SLO is internal; SLA has contractual consequences)
- Not using error budget to make deployment decisions (defeats the purpose)

### Connections
- **Builds on**: Lesson 5 - Centralized Logging with Loki
- **Leads to**: Lesson 7 - Alerting and Incident Response
