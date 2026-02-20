### Core Concept
Dapr sidecars must be observable too—configure metrics, traces, and logs so you can see where latency or failures occur between application code, Dapr building blocks, and backend services.

### Key Mental Models
- **Sidecar visibility gap**: Without Dapr telemetry, half of each request path is invisible.
- **Configuration as the switch**: A Dapr Configuration CRD governs metrics/tracing for all sidecars that reference it.
- **Trace correlation**: Follow a request from app spans through Dapr spans to backend operations to pinpoint bottlenecks.

### Critical Patterns
- Create a Dapr `Configuration` enabling Prometheus metrics and OpenTelemetry tracing, and reference it via pod annotations.
- Add ServiceMonitor resources so Prometheus scrapes sidecar endpoints; forward traces to Jaeger/OTel collectors.
- Query actor/workflow-specific metrics to understand activations, invocations, and step durations.
- Use structured JSON logs from sidecars to align with existing Loki/LogQL practices.

### Common Mistakes
- Forgetting `dapr.io/config` annotations, leaving sidecars unobserved.
- Scraping the app but not the sidecar, producing misleading latency attributions.
- Sampling every request in production without considering cost/noise; tune rates after verification.

### Connections
- **Builds on**: Observability stack from earlier Chapter 55 lessons and Dapr fundamentals from Chapter 53.
- **Leads to**: Actor/workflow observability in Chapter 57 and the full-stack capstone in Lesson 10.
