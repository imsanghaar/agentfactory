### Core Concept
Grafana transforms Prometheus metrics into actionable dashboards with panels for the 4 golden signals, variables for multi-service filtering, and JSON models that enable version control and deployment as code via ConfigMaps.

### Key Mental Models
- **Dashboard JSON Model**: Dashboards are JSON documents with settings, variables, rows, and panels; export to Git for version control
- **Panel Types**: Time series for trends over time, Gauge for current status with thresholds, Table for multi-metric comparisons
- **Variables**: Query-based dropdowns (namespace, service) that filter all panels; enable one dashboard for multiple services
- **Thresholds**: Green/yellow/red based on SLOs (e.g., green &lt; 500ms, yellow 500-800ms, red > 800ms)

### Critical Patterns
- 4 golden signals panels: P95 latency (time series), traffic (time series), error rate (gauge), saturation (gauge)
- Variable query: `label_values(kube_namespace_labels, namespace)` populates namespace dropdown
- Use variables in PromQL: `{namespace="$namespace", service="$service"}`
- Deploy dashboards as ConfigMaps with `grafana_dashboard: "1"` label for auto-import

### AI Collaboration Keys
- Ask Claude to generate per-endpoint latency breakdown using `by (endpoint)` grouping
- Request Table panel configuration for real-time endpoint status leaderboard
- Have AI recommend dashboard architecture for 5-10 services (overview vs detail hierarchy)

### Common Mistakes
- Hardcoding namespace/service in queries instead of using variables (not reusable)
- Missing unit configuration on panels (confusing whether value is seconds or milliseconds)
- Not setting thresholds based on SLOs (green/yellow/red become meaningless)

### Connections
- **Builds on**: Lesson 2 - Metrics with Prometheus
- **Leads to**: Lesson 4 - Distributed Tracing with OpenTelemetry and Jaeger
