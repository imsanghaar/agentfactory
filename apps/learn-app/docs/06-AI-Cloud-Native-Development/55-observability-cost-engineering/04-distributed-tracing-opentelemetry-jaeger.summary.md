### Core Concept
OpenTelemetry instruments applications to create traces (complete request journeys) composed of spans (timed operations), using context propagation to link spans across services, with Jaeger visualizing the waterfall to identify bottlenecks.

### Key Mental Models
- **Trace**: Complete journey of a single request through all services; unique trace_id links all operations
- **Span**: Single timed operation with name, duration, parent span ID, attributes, and status
- **Context Propagation**: W3C traceparent header passes trace_id and parent_span_id between services automatically
- **Sampling**: Reduce volume by tracing only a percentage; 1-10% in production, 100% in development

### Critical Patterns
- Auto-instrumentation: `opentelemetry-instrument uvicorn main:app` wraps FastAPI automatically
- Programmatic setup: TracerProvider with OTLPSpanExporter to Jaeger collector on port 4317
- Custom spans: `with tracer.start_as_current_span("operation") as span:` for business logic
- Kubernetes env vars: OTEL_SERVICE_NAME, OTEL_EXPORTER_OTLP_ENDPOINT, OTEL_TRACES_SAMPLER

### AI Collaboration Keys
- Ask Claude to design custom spans with appropriate attributes for payment processing
- Request troubleshooting checklist when traces don't appear in Jaeger
- Have AI calculate storage needs at different sampling rates and recommend strategy

### Common Mistakes
- Using auto-instrumentation with `uvicorn --reload` (doesn't work; use programmatic setup)
- Setting 100% sampling in production (storage costs explode at high traffic)
- Not adding span attributes that would help debugging (missing request context)

### Connections
- **Builds on**: Lesson 3 - Visualization with Grafana
- **Leads to**: Lesson 5 - Centralized Logging with Loki
