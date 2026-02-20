### Core Concept
OpenCost provides real-time Kubernetes cost visibility, tying resource usage to dollars by namespace, team, or product.

### Key Mental Models
- **Allocation by label**: Meaningful labels (team/product/env) enable actionable reports.
- **Metrics to money**: CPU/memory usage + pricing → cost; validate data sources.
- **Continuous visibility**: Monitor trends daily, not just monthly bills.

### Critical Patterns
- Install OpenCost with Prometheus; ensure correct pricing inputs and scrape targets.
- Label namespaces/workloads for allocation and query costs by owner.
- Build dashboards/alerts for spend anomalies and top cost drivers.

### Common Mistakes
- Missing labels, yielding unallocated/unknown costs.
- Incorrect pricing config leading to misleading numbers.
- Treating OpenCost as one-time instead of continuous monitoring.

### Connections
- **Builds on**: Cost fundamentals and labeling discipline.
- **Leads to**: Budget alerts, backups, and DR cost considerations.
