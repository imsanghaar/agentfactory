### Core Concept
Resilience patterns operate at multiple layers: retries with exponential backoff recover from transient failures, timeouts prevent resource exhaustion, PodDisruptionBudgets guarantee availability during maintenance, and graceful shutdown completes in-flight requests.

### Key Mental Models
- **Retry Selectivity**: Retry 502/503/504 (transient); never retry 400/401/404 (permanent failures)
- **Exponential Backoff**: Delays increase (100ms, 200ms, 400ms) to avoid overwhelming recovering services
- **PDB Voluntary Protection**: Protects against node drains and upgrades; cannot protect against node crashes
- **Graceful Shutdown Race**: preStop sleep (10s) allows endpoints propagation before SIGTERM processing

### Critical Patterns
- Set per-retry timeout shorter than request timeout (5s retry in 30s request)
- Configure PDB with minAvailable: 2 for 3-replica deployments
- Use `terminationGracePeriodSeconds` = preStop sleep + max request duration + buffer
- Enable outlier detection to auto-exclude pods returning consecutive errors

### AI Collaboration Keys
- Generate BackendTrafficPolicy with retry policy and exponential backoff
- Configure PodDisruptionBudget matching deployment availability requirements
- Design graceful shutdown with preStop hook and appropriate grace period

### Common Mistakes
- Using liveness probe for dependency health (causes restart loops when database is down)
- Missing preStop hook causing dropped requests during deployments
- PDB with minAvailable equal to replicas (blocks all maintenance)

### Connections
- **Builds on**: Lesson 9 (Autoscaling) for capacity management
- **Leads to**: Lesson 11 (Envoy AI Gateway) for LLM-specific traffic patterns
