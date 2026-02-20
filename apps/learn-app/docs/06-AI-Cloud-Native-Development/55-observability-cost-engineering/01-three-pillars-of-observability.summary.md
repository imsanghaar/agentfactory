### Core Concept
Observability rests on three complementary pillars: metrics (aggregated numerical data for system-wide trends), traces (request flow across services for debugging specific requests), and logs (event-level detail for understanding exactly what happened and why).

### Key Mental Models
- **Metrics (Prometheus)**: Highly compressed, fast to query, good for dashboards and alerts; answers "how much" and "how often"
- **Traces (Jaeger/OpenTelemetry)**: Follows individual requests through services showing timing per span; answers "where" and "how long"
- **Logs (Loki)**: Timestamped text records with rich context; answers "what" and "why"
- **4 Golden Signals**: Latency (how long), Traffic (how much demand), Errors (failure rate), Saturation (resource utilization)

### Critical Patterns
- Debugging workflow: Start with metrics (triage), drill into traces (locate), read logs (diagnose)
- P50/P95/P99 latency percentiles for understanding typical vs worst-case user experience
- Error rate = 5xx responses / total requests as percentage
- Saturation as leading indicator: CPU/memory utilization predicts failures before they occur

### AI Collaboration Keys
- Ask Claude to design observability strategy for your specific AI agent architecture
- Request walkthrough of 4 golden signals debugging for performance issues
- Have AI identify which pillar and signal to start with for different production scenarios

### Common Mistakes
- Using only one pillar instead of combining all three for complete visibility
- Skipping metrics triage and jumping straight to logs (inefficient)
- Not tracking saturation as leading indicator of future failures

### Connections
- **Builds on**: Lesson 0 - Build Your Observability Skill
- **Leads to**: Lesson 2 - Metrics with Prometheus
