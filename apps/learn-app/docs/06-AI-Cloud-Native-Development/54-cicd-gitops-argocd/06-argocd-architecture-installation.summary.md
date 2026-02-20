### Core Concept
ArgoCD is a declarative GitOps controller with five core components (API Server, Repo Server, Application Controller, Redis, Dex) that watches Git repositories and automatically reconciles Kubernetes cluster state to match declared manifests.

### Key Mental Models
- **API Server**: Exposes REST API for UI and CLI communication on port 8080
- **Repo Server**: Clones Git repos and renders manifests (helm template, kustomize build) in isolation for scalability
- **Application Controller**: The reconciliation loop that compares Git state with cluster state every 3 seconds and applies changes
- **Redis + Dex**: Redis caches Git/cluster state for performance; Dex provides OIDC authentication for multi-user access

### Critical Patterns
- Install ArgoCD with Helm: `helm install argocd argo/argo-cd --namespace argocd`
- Port-forward to access UI: `kubectl port-forward svc/argocd-server -n argocd 8080:443`
- Retrieve admin password: `kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`
- Authenticate CLI: `argocd login localhost:8080 --username admin --password <password> --insecure`

### AI Collaboration Keys
- Ask Claude to troubleshoot when argocd-repo-server crashes with OOMKilled on memory-constrained clusters
- Request resource limit adjustments for ArgoCD components in constrained environments
- Have AI explain which components to scale when managing many applications

### Common Mistakes
- Not waiting for health checks before testing (pods may report Running but not be ready)
- Using outdated Helm chart versions without checking for breaking changes
- Forgetting the --insecure flag for localhost CLI login (fails on self-signed certificate)

### Connections
- **Builds on**: Lesson 5 - GitOps Principles: Git as Truth
- **Leads to**: Lesson 7 - Your First ArgoCD Application
