### Core Concept
GitOps makes Git the single source of truth for infrastructure, using declarative YAML to define desired state while a controller (ArgoCD) continuously reconciles the cluster to match Git, enabling auditability, rollback via git revert, and automatic drift correction.

### Key Mental Models
- **Declarative vs Imperative**: Declarative describes desired end state ("3 replicas"); imperative describes steps to execute ("kubectl scale")
- **Reconciliation Loop**: Controller continuously observes Git, diffs against cluster, acts to correct mismatches (every 3 seconds)
- **Drift Detection**: When cluster state diverges from Git (manual kubectl changes), controller automatically corrects back to Git-declared state
- **Git as Source of Truth**: Every change is committed with author, timestamp, message; cluster is reproducible from Git at any point in history

### Critical Patterns
- Store all Kubernetes manifests in Git with version control and review process
- Use automated reconciliation to detect and correct drift without human intervention
- Rollback by running `git revert` instead of manual kubectl rollback commands
- Enable self-healing so manual cluster modifications are automatically reverted to Git state

### AI Collaboration Keys
- Ask Claude to explain what happens when someone manually scales a deployment in a GitOps environment
- Request comparison of audit trails between manual kubectl and GitOps deployments
- Have AI design a GitOps-based incident response workflow

### Common Mistakes
- Using kubectl apply as primary deployment method (loses audit trail and enables undocumented drift)
- Treating cluster as source of truth instead of Git (cluster becomes fragile and unreproducible)
- Not enabling selfHeal, allowing manual changes to persist until next intentional sync

### Connections
- **Builds on**: Lesson 4 - Testing and Quality Gates
- **Leads to**: Lesson 6 - ArgoCD Architecture & Installation
