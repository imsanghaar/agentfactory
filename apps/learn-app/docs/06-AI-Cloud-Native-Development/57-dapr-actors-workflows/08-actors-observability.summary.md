### Core Concept
Instrument actors and their sidecars so you can see method latency, activation patterns, and failures—observability must cover both app code and Dapr runtime.

### Key Mental Models
- **Sidecar visibility**: Scrape sidecar metrics/traces/logs in addition to app metrics.
- **Actor-specific signals**: Track activations, turns, queue depth, reminders, and failures per actor type/ID.
- **Trace correlation**: Propagate trace IDs through actor calls and pub/sub to follow end-to-end flows.

### Critical Patterns
- Enable Dapr Configuration for metrics/tracing and add ServiceMonitors to scrape sidecar endpoints.
- Emit custom app metrics around actor methods (latency, errors) and tag with actor type/id.
- Correlate logs with trace IDs; use structured logging for searchable actor events.
- Build dashboards for activation counts, turn duration percentiles, reminder success, and failure rates.

### Common Mistakes
- Monitoring only the app container and ignoring the Dapr sidecar.
- Lacking IDs/labels in metrics/logs, making per-actor debugging impossible.
- Sampling traces too low before verifying instrumentation; too high in prod causing cost/noise.

### Connections
- **Builds on**: Dapr observability setup in Chapter 55.
- **Leads to**: Workflow observability and production hardening later in the chapter.
