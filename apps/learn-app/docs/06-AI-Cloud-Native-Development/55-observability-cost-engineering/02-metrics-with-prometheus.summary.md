### Core Concept
Prometheus pulls metrics from /metrics endpoints at regular intervals, stores them in a time series database, and enables PromQL queries for the 4 golden signals; applications expose metrics using prometheus_client and Prometheus discovers them via ServiceMonitors.

### Key Mental Models
- **Pull Model**: Prometheus scrapes applications at /metrics; apps don't need to know where Prometheus lives
- **Time Series**: Metric samples with timestamps stored efficiently for time-range queries
- **ServiceMonitor**: Kubernetes CRD that tells Prometheus which Services to scrape (selector + endpoint + interval)
- **Recording Rules**: Pre-compute complex PromQL queries and store as new time series for dashboard efficiency

### Critical Patterns
- Install kube-prometheus-stack via Helm with `serviceMonitorSelectorNilUsesHelmValues=false`
- PromQL rate() for request rates: `sum(rate(http_requests_total[5m])) by (service)`
- histogram_quantile() for latency: `histogram_quantile(0.95, sum(rate(bucket[5m])) by (le))`
- Instrument FastAPI with Counter (requests_total) and Histogram (duration_seconds)

### AI Collaboration Keys
- Ask Claude to write PromQL queries for error budget burn rate calculation
- Request metric design review for cardinality issues (user_id labels are high cardinality)
- Have AI troubleshoot ServiceMonitor discovery issues (namespace selector, label matching)

### Common Mistakes
- Using high-cardinality labels like user_id (creates unbounded time series, exhausts memory)
- Forgetting `release: prometheus` label on ServiceMonitor (not discovered by Helm-installed Prometheus)
- Not setting `serviceMonitorSelectorNilUsesHelmValues=false` (ignores custom ServiceMonitors)

### Connections
- **Builds on**: Lesson 1 - Three Pillars of Observability
- **Leads to**: Lesson 3 - Visualization with Grafana
