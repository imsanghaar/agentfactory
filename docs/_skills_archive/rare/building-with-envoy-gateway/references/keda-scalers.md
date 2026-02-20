# KEDA Scaler Reference

## Core Concepts

KEDA extends Kubernetes HPA with event-driven scaling, including scale-to-zero capability.

### Architecture

```
Event Sources (Kafka, Prometheus, HTTP, etc.)
         │
         ▼
┌─────────────────┐
│  KEDA Operator  │ ◄── Watches ScaledObject/ScaledJob
└────────┬────────┘
         │ Creates/Manages
         ▼
┌─────────────────┐
│       HPA       │ ◄── Standard Kubernetes HPA
└────────┬────────┘
         │ Scales
         ▼
┌─────────────────┐
│   Deployment    │
└─────────────────┘
```

## ScaledObject Reference

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: app-scaler
  namespace: default
spec:
  # Target workload
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment        # or StatefulSet, Custom Resource
    name: my-deployment

  # Scaling bounds
  minReplicaCount: 0        # Scale to zero when idle
  maxReplicaCount: 100      # Upper limit
  idleReplicaCount: 0       # Replicas when triggers = 0

  # Polling and cooldown
  pollingInterval: 30       # Check triggers every N seconds
  cooldownPeriod: 300       # Wait before scaling down (seconds)

  # Fallback if scaler fails
  fallback:
    failureThreshold: 3
    replicas: 1

  # Advanced settings
  advanced:
    restoreToOriginalReplicaCount: true
    horizontalPodAutoscalerConfig:
      behavior:
        scaleDown:
          stabilizationWindowSeconds: 300
          policies:
          - type: Percent
            value: 10
            periodSeconds: 60

  # Event triggers
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus:9090
      query: sum(rate(http_requests_total[1m]))
      threshold: "100"
```

## Key Scalers for AI Agents

### Prometheus Scaler

Scale based on custom Prometheus metrics.

```yaml
triggers:
- type: prometheus
  metadata:
    serverAddress: http://prometheus.monitoring:9090
    metricName: custom_metric
    query: |
      sum(rate(http_requests_total{app="task-api"}[1m]))
    threshold: "100"
    activationThreshold: "0"  # Trigger activation

    # Authentication (optional)
    authModes: "bearer"
  authenticationRef:
    name: prometheus-auth
```

**Example Queries:**

```yaml
# Request rate per second
query: sum(rate(http_requests_total{app="task-api"}[1m]))

# Queue depth
query: sum(task_queue_depth{app="task-processor"})

# P95 latency (scale when slow)
query: histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Error rate percentage
query: sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# Active connections
query: sum(envoy_http_downstream_cx_active{app="task-api"})
```

### Kafka Scaler

Scale based on consumer lag (unprocessed messages).

```yaml
triggers:
- type: kafka
  metadata:
    bootstrapServers: kafka.default:9092
    consumerGroup: task-processors
    topic: task-events
    lagThreshold: "50"           # Scale up if lag > 50
    activationLagThreshold: "1"  # Activate from zero if lag > 1
    offsetResetPolicy: latest

    # Optional settings
    allowIdleConsumers: "false"
    excludePersistentLag: "false"
    limitToPartitionsWithLag: "false"
    partitionLimitation: "0,1,2"
    version: "1.0.0"

    # SASL authentication
    sasl: plaintext
    tls: enable
  authenticationRef:
    name: kafka-auth
```

**TriggerAuthentication for Kafka:**

```yaml
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: kafka-auth
spec:
  secretTargetRef:
  - parameter: sasl
    name: kafka-credentials
    key: sasl
  - parameter: username
    name: kafka-credentials
    key: username
  - parameter: password
    name: kafka-credentials
    key: password
  - parameter: tls
    name: kafka-credentials
    key: tls
  - parameter: ca
    name: kafka-credentials
    key: ca
```

### HTTP Scaler (HTTP Add-on)

Scale based on HTTP request volume.

```yaml
# First, install HTTP Add-on:
# helm install keda-http-addon kedacore/keda-add-ons-http -n keda

triggers:
- type: http
  metadata:
    scalingMetric: requestRate
    targetValue: "100"           # 100 requests per second per replica
    pathPrefixes: "/api"
    hosts: "api.example.com"

    # OR scale on concurrency
    scalingMetric: concurrency
    targetValue: "10"            # 10 concurrent requests per replica
```

**HTTPScaledObject (alternative):**

```yaml
apiVersion: http.keda.sh/v1alpha1
kind: HTTPScaledObject
metadata:
  name: http-app
spec:
  hosts:
  - api.example.com
  pathPrefixes:
  - /api
  scaleTargetRef:
    name: task-api
    kind: Deployment
  replicas:
    min: 1
    max: 50
  targetPendingRequests: 100
```

### Cron Scaler

Scale based on time schedules.

```yaml
triggers:
- type: cron
  metadata:
    timezone: America/New_York
    start: 0 8 * * *           # 8:00 AM
    end: 0 18 * * *            # 6:00 PM
    desiredReplicas: "10"

# Multiple schedules (business hours + off-hours)
- type: cron
  metadata:
    timezone: UTC
    start: 0 9 * * 1-5         # Weekdays 9 AM
    end: 0 17 * * 1-5          # Weekdays 5 PM
    desiredReplicas: "20"

- type: cron
  metadata:
    timezone: UTC
    start: 0 17 * * 1-5        # After hours
    end: 0 9 * * 1-5           # Before hours
    desiredReplicas: "2"
```

### PostgreSQL Scaler

Scale based on database query results.

```yaml
triggers:
- type: postgresql
  metadata:
    connectionFromEnv: POSTGRES_CONNECTION_STRING
    query: "SELECT COUNT(*) FROM tasks WHERE status = 'pending'"
    targetQueryValue: "10"      # 10 pending tasks per replica
    activationTargetQueryValue: "1"
```

### Redis Scaler

Scale based on Redis list/stream length.

```yaml
triggers:
- type: redis
  metadata:
    address: redis.default:6379
    listName: task-queue
    listLength: "50"            # Scale if queue > 50
    activationListLength: "1"   # Activate from zero if queue > 1

    # OR for Redis Streams
    stream: task-stream
    consumerGroup: processors
    pendingEntriesCount: "100"
```

### AWS SQS Scaler

Scale based on SQS queue depth.

```yaml
triggers:
- type: aws-sqs-queue
  metadata:
    queueURL: https://sqs.us-east-1.amazonaws.com/123456789/task-queue
    queueLength: "50"
    awsRegion: us-east-1
    activationQueueLength: "1"
  authenticationRef:
    name: aws-credentials
```

### RabbitMQ Scaler

Scale based on RabbitMQ queue.

```yaml
triggers:
- type: rabbitmq
  metadata:
    host: amqp://rabbitmq.default:5672
    queueName: task-queue
    mode: QueueLength           # or MessageRate
    value: "50"                 # 50 messages triggers scale
    activationValue: "1"
```

## Multi-Trigger Patterns

### Fan-In: Multiple Event Sources

```yaml
# Scale if ANY trigger exceeds threshold
triggers:
# CPU-based (resource)
- type: cpu
  metricType: Utilization
  metadata:
    value: "70"

# Queue-based (Kafka)
- type: kafka
  metadata:
    bootstrapServers: kafka:9092
    topic: events
    lagThreshold: "100"

# Request-based (Prometheus)
- type: prometheus
  metadata:
    query: sum(rate(http_requests_total[1m]))
    threshold: "200"
```

### Hybrid: Scheduled + Demand

```yaml
# Business hours: high capacity
- type: cron
  metadata:
    timezone: UTC
    start: 0 8 * * 1-5
    end: 0 18 * * 1-5
    desiredReplicas: "20"

# Demand-based overlay
- type: prometheus
  metadata:
    query: sum(task_queue_depth)
    threshold: "10"
```

### Cost-Optimized: Off-Peak Batch Processing

```yaml
# Scale up during cheap compute hours
- type: cron
  metadata:
    timezone: UTC
    start: 0 22 * * *          # 10 PM
    end: 0 6 * * *             # 6 AM
    desiredReplicas: "50"

# Process backlog during cheap hours
- type: kafka
  metadata:
    topic: batch-jobs
    lagThreshold: "10"
```

## ScaledJob for Batch Workloads

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledJob
metadata:
  name: batch-processor
spec:
  jobTargetRef:
    parallelism: 1
    completions: 1
    activeDeadlineSeconds: 600
    backoffLimit: 2
    template:
      spec:
        containers:
        - name: processor
          image: batch-processor:latest
        restartPolicy: Never

  pollingInterval: 30
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 3
  maxReplicaCount: 10

  triggers:
  - type: kafka
    metadata:
      bootstrapServers: kafka:9092
      topic: batch-tasks
      consumerGroup: batch-processors
      lagThreshold: "1"
```

## TriggerAuthentication

```yaml
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: secret-auth
spec:
  # From Kubernetes Secret
  secretTargetRef:
  - parameter: connection
    name: db-secret
    key: connection-string
  - parameter: password
    name: db-secret
    key: password

---
# Cluster-wide authentication
apiVersion: keda.sh/v1alpha1
kind: ClusterTriggerAuthentication
metadata:
  name: aws-auth
spec:
  podIdentity:
    provider: aws-eks
  # OR
  secretTargetRef:
  - parameter: awsAccessKeyID
    name: aws-creds
    key: access-key
  - parameter: awsSecretAccessKey
    name: aws-creds
    key: secret-key
```

## Integration with Envoy Gateway

### Scaling on Gateway Metrics

```yaml
# Envoy Gateway exposes metrics to Prometheus
triggers:
- type: prometheus
  metadata:
    serverAddress: http://prometheus:9090
    query: |
      sum(rate(envoy_http_downstream_rq_total{
        envoy_cluster_name=~".*task-api.*"
      }[1m]))
    threshold: "100"
```

### Scaling on Gateway Error Rate

```yaml
triggers:
- type: prometheus
  metadata:
    query: |
      sum(rate(envoy_http_downstream_rq_xx{
        envoy_cluster_name=~".*task-api.*",
        envoy_response_code_class="5"
      }[5m])) /
      sum(rate(envoy_http_downstream_rq_total{
        envoy_cluster_name=~".*task-api.*"
      }[5m])) * 100
    threshold: "5"  # Scale down if error rate > 5%
```

### Kedify (Gateway API Native HTTP Scaling)

```yaml
# Uses Envoy as the interceptor instead of HTTP Add-on
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: kedify-scaler
spec:
  scaleTargetRef:
    name: task-api
  triggers:
  - type: http
    metadata:
      scalingMetric: requestRate
      targetValue: "100"
      # Kedify auto-wires with HTTPRoute
```
