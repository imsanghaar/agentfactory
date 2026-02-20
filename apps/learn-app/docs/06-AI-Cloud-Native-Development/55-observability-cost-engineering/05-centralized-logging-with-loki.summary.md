### Core Concept
Grafana Loki aggregates logs from all containers with label-only indexing (not full-text), making it 10x cheaper than Elasticsearch while enabling fast queries when you narrow by namespace, app, and time window first.

### Key Mental Models
- **Label-Only Indexing**: Loki indexes metadata (namespace, app, pod) not content; content filters run on narrowed streams
- **Promtail DaemonSet**: Agent on each node tails /var/log/pods, adds Kubernetes labels, pushes to Loki
- **LogQL**: Query language with stream selectors ({app="task-api"}), line filters (|= "error"), and parsers (| json)
- **Trace Correlation**: Include trace_id in JSON logs to jump from Jaeger span to related log entries

### Critical Patterns
- Stream selector first: `{namespace="default", app="task-api"}` narrows before filtering
- Parse JSON logs: `{app="task-api"} | json | level="error"` extracts and filters by fields
- Trace correlation query: `{app="task-api"} |= "trace_id=\"abc123\""`
- Retention by environment: Dev 24-48h, Staging 7d, Prod 14-30d, Audit 90d+

### AI Collaboration Keys
- Ask Claude to build LogQL query for specific debugging scenario (endpoint errors with trace_id)
- Request structured logging schema with trace context injection for FastAPI
- Have AI analyze and optimize log volume with Promtail pipeline changes

### Common Mistakes
- Not narrowing with labels first (queries entire log history, slow and expensive)
- Using unstructured text logs (can't use | json parser for field extraction)
- Missing trace_id in logs (can't correlate with Jaeger traces)

### Connections
- **Builds on**: Lesson 4 - Distributed Tracing with OpenTelemetry and Jaeger
- **Leads to**: Lesson 6 - SRE Foundations: SLIs, SLOs, and Error Budgets
