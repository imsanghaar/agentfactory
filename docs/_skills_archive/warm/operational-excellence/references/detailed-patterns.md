# Operational Excellence Detailed Patterns

## VPA Deep Dive

### Architecture Components

**Recommender**: Analyzes metrics from Metrics Server, generates target/lower/upper bound recommendations. Runs in kube-system namespace.

**Updater**: Compares pod configs with recommendations, evicts pods when difference exceeds threshold. Respects PodDisruptionBudgets.

**Admission Controller**: Mutating webhook that injects recommendations into new pods before scheduling.

### Installation via Helm

```bash
# Recommended: stevehipwell chart
helm repo add stevehipwell https://stevehipwell.github.io/helm-charts/
helm install vpa stevehipwell/vertical-pod-autoscaler --version 1.10.1
```

### Complete VPA CRD

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: example-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-deployment
  updatePolicy:
    updateMode: "Recreate"  # Off|Initial|Recreate|InPlaceOrRecreate
    maxUnavailable: 1
    minReplicas: 2
  resourcePolicy:
    containerPolicies:
    - containerName: "app"
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2000m
        memory: 2Gi
      controlledResources: [cpu, memory]
      controlledValues: RequestsAndLimits
    - containerName: "sidecar"
      controlledResources: []  # Don't scale sidecar
```

### VPA + HPA Safe Patterns

**Pattern A**: Different metrics
- HPA: `http_requests_per_second` (custom metric)
- VPA: CPU/memory (Off mode for recommendations)

**Pattern B**: VPA Off + HPA active
- VPA generates recommendations for manual review
- HPA handles all automatic scaling

---

## OpenCost Deep Dive

### Cost Calculation

```
Workload Cost = max(resource_request, actual_usage) × hourly_rate
Idle Cost = Provisioned resources - Allocated resources
```

### API Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/allocation` | Kubernetes workload costs |
| `/assets` | Infrastructure asset costs |
| `/cloudCost` | Cloud provider billing data |
| `/customCost/total` | External costs (plugins) |

### Common Queries

```bash
# Last 7 days by namespace
curl -G http://opencost:9003/allocation \
  -d window=7d \
  -d aggregate=namespace

# Cost by team label
curl -G http://opencost:9003/allocation \
  -d window=7d \
  -d aggregate=label:team

# With idle cost distribution
curl -G http://opencost:9003/allocation \
  -d window=7d \
  -d shareIdle=true \
  -d idleByNode=true
```

### FinOps Tagging Strategy

Required labels:
- `team`: Team ownership
- `environment`: dev|staging|production
- `app`: Application name
- `cost-center`: Budget owner

---

## Velero Deep Dive

### Backup Storage Locations

```yaml
apiVersion: velero.io/v1
kind: BackupStorageLocation
metadata:
  name: default
  namespace: velero
spec:
  provider: aws
  objectStorage:
    bucket: velero-backups
  config:
    region: us-east-1
```

### MinIO for Local Development

```yaml
spec:
  provider: aws
  objectStorage:
    bucket: velero-backups
  config:
    s3Url: http://minio:9000
    insecureSkipTLSVerify: "true"
```

### Backup Hooks (Pre/Post)

```yaml
hooks:
  resources:
    - name: mysql-backup
      includedNamespaces: [production]
      pre:
        - exec:
            container: mysql
            command: ["/bin/sh", "-c", "mysql -e 'FLUSH TABLES WITH READ LOCK'"]
            onError: Fail
            timeout: 30s
      post:
        - exec:
            container: mysql
            command: ["/bin/sh", "-c", "mysql -e 'UNLOCK TABLES'"]
            onError: Continue
            timeout: 30s
```

### RTO/RPO Trade-offs

| Strategy | RTO | RPO | Cost |
|----------|-----|-----|------|
| Daily backups | 2-4h | 24h | Low |
| Hourly backups | 1-2h | 1h | Medium |
| 15-min backups | 30min | 15min | High |
| CSI snapshots | 15-30min | Per snapshot | Medium |

---

## Chaos Mesh Deep Dive

### Experiment Types

**PodChaos Actions**:
- `pod-kill`: Terminate pod
- `pod-failure`: Inject failure via pause image
- `container-kill`: Kill specific container

**NetworkChaos Actions**:
- `delay`: Add latency
- `loss`: Drop packets
- `duplication`: Duplicate packets
- `partition`: Network partition
- `corruption`: Corrupt packets

### Workflow Orchestration

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: chaos-workflow
spec:
  entry: serial-node
  templates:
    - name: serial-node
      templateType: Serial
      children:
        - network-delay
        - pod-kill
    - name: network-delay
      templateType: NetworkChaos
      networkChaos:
        action: delay
        delay:
          latency: "100ms"
    - name: pod-kill
      templateType: PodChaos
      podChaos:
        action: pod-kill
```

### Safety Configuration

Enable namespace filtering:
```bash
helm install chaos-mesh chaos-mesh/chaos-mesh \
  --set controllerManager.enableFilterNamespace=true
```

Annotate allowed namespaces:
```bash
kubectl annotate ns staging chaos-mesh.org/inject=enabled
```

---

## Sources

- [VPA Official](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)
- [OpenCost Docs](https://opencost.io/docs/)
- [Velero Docs](https://velero.io/docs/)
- [Chaos Mesh Docs](https://chaos-mesh.org/docs/)
- [FinOps Foundation](https://www.finops.org/)
