### Core Concept
FinOps brings discipline to cloud spend: gain real-time visibility, allocate costs to owners, and right-size Kubernetes workloads so engineering speed aligns with budget accountability.

### Key Mental Models
- **FinOps lifecycle (Inform → Optimize → Operate)**: Visibility precedes efficiency; governance locks in savings.
- **Cost allocation as labeling**: Every dollar must trace to teams/products via namespace and pod labels.
- **Right-size from evidence**: VPA recommendations and usage metrics replace guesswork about requests/limits.

### Critical Patterns
- Deploy OpenCost alongside Prometheus to surface live spend data.
- Label namespaces and workloads (`team`, `product`, `cost-center`, `environment`) and query costs by owner.
- Detect waste with PromQL (idle capacity, over-provisioned requests) and act on right-sizing candidates.
- Use VPA in recommend mode to adjust requests, and schedule non-prod environments off-hours for savings.

### Common Mistakes
- Running cost tools without labels, leaving spend un-attributable.
- Acting on monthly bills instead of real-time metrics, so waste persists.
- Enabling VPA auto-updates or aggressive scheduling without guardrails, risking instability.

### Connections
- **Builds on**: Metrics stack from earlier lessons in Chapter 55.
- **Leads to**: Capstone stack (L10) that combines cost data with observability and Dapr integrations.
