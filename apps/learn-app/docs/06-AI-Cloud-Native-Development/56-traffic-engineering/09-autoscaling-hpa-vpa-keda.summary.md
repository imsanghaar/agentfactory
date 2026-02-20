### Core Concept
Autoscaling matches capacity to demand through HPA (replica count based on CPU/memory), VPA (pod resource sizing), and KEDA (event-driven scaling with scale-to-zero), eliminating waste during quiet periods and failures during traffic spikes.

### Key Mental Models
- **HPA vs VPA vs KEDA**: HPA adds replicas, VPA resizes pods, KEDA scales on any metric including to zero
- **ScaledObject as HPA Factory**: KEDA creates and manages HPAs automatically based on custom triggers
- **Scale-to-Zero Economics**: Zero pods when idle eliminates cost; first request triggers cold start
- **Trigger Diversity**: KEDA supports Prometheus metrics, Kafka lag, cron schedules, and 50+ scalers

### Critical Patterns
- Install metrics-server before using HPA (required for CPU/memory metrics)
- Use KEDA for event-driven workloads like Kafka consumers scaling on lag
- Set `minReplicaCount: 1` for latency-sensitive services to avoid cold starts
- Configure `cooldownPeriod` to prevent scaling flapping (300s typical for scale-down)

### AI Collaboration Keys
- Generate HPA with behavior section for aggressive scale-up and gradual scale-down
- Configure KEDA ScaledObject with Prometheus trigger and appropriate threshold
- Design scale-to-zero configuration with cold start mitigation

### Common Mistakes
- Using HPA without metrics-server (shows `<unknown>` targets)
- Using VPA with HPA on same resource (both try to control CPU/memory)
- Aggressive cooldownPeriod causing scaling oscillation

### Connections
- **Builds on**: Lesson 8 (Traffic Splitting) for deployment strategies
- **Leads to**: Lesson 10 (Resilience Patterns) for production reliability
