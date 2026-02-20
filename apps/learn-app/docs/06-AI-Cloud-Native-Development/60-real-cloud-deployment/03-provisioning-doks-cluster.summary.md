### Core Concept
Provision a DigitalOcean Kubernetes (DOKS) cluster with the right size, region, and networking to host the Task API reliably.

### Key Mental Models
- **Spec-driven provisioning**: Define region, node size/count, version, and networking before creating.
- **Security and access**: Control kubeconfig distribution and API access.
- **Cost/perf balance**: Choose node types and autoscaling aligned to workload needs.

### Critical Patterns
- Use `doctl`/console/TF to create the cluster; store kubeconfig securely.
- Configure node pools, autoscaling, and labels/taints for workloads.
- Verify cluster health and access; restrict API endpoints and rotate credentials.

### Common Mistakes
- Defaulting to small/unsupported node types or wrong regions.
- Distributing kubeconfig widely without rotation or RBAC.
- Skipping autoscaling and capacity planning, leading to outages or overspend.

### Connections
- **Builds on**: DO account setup.
- **Leads to**: Load balancer/DNS, secrets, and app deployment steps.
