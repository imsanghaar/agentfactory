### Core Concept
Hub-spoke architecture enables one ArgoCD instance to manage multiple Kubernetes clusters, using cluster registration with service accounts and ApplicationSets with cluster generators for per-cluster configurations and automated multi-region deployments.

### Key Mental Models
- **Hub-Spoke Topology**: Central ArgoCD hub manages multiple spoke clusters via registered credentials; single pane of glass for all deployments
- **Cluster Registration**: Create service account with cluster-admin on spoke, then `argocd cluster add <context> --name <name>` stores credentials as Secret
- **Cluster Generator**: ApplicationSet generator creates one Application per registered cluster using `{{name}}` and `{{server}}` template variables
- **Per-Cluster Values**: Use `valueFiles: [values.yaml, values-{{name}}.yaml]` to apply environment-specific Helm overrides

### Critical Patterns
- Register cluster: `kubectl create sa argocd-manager` + `argocd cluster add <context>`
- Label clusters for selection: `argocd cluster patch staging --labels 'env=staging,deploy=true'`
- Cluster generator selector: `clusters: { selector: { matchLabels: { deploy: "true" } } }`
- ArgoCD HA: `--set server.replicas=3 --set controller.replicas=3` for fault-tolerant hub

### AI Collaboration Keys
- Ask Claude to design ApplicationSet with cluster generator for prod/staging/DR
- Request per-cluster Helm values strategy with separate resource limits
- Have AI explain disaster recovery strategies for multi-cluster ArgoCD deployments

### Common Mistakes
- Not creating service account on spoke cluster before registration (connection fails)
- Using cluster-internal DNS across clusters (service.namespace.svc.cluster.local doesn't route)
- Single ArgoCD replica without HA (hub failure prevents all spoke deployments)

### Connections
- **Builds on**: Lesson 14 - Secrets Management for GitOps
- **Leads to**: Lesson 16 - AI-Assisted GitOps Workflows
