### Core Concept
An ArgoCD Application CRD defines a GitOps contract specifying source (Git repo, path, revision), destination (cluster, namespace), and syncPolicy (automated prune/selfHeal), enabling three deployment methods: UI, CLI, and declarative YAML.

### Key Mental Models
- **Application CRD**: Kubernetes custom resource that tells ArgoCD what to sync (source), where to deploy (destination), and how to sync (syncPolicy)
- **Sync Status**: OutOfSync means Git differs from cluster; Syncing means reconciliation in progress; Synced means cluster matches Git
- **Health Status**: Healthy means resources are working; Progressing means pods starting; Degraded means resources deployed but failing
- **Automated Sync**: With prune=true and selfHeal=true, ArgoCD auto-deletes removed resources and fixes drift without manual intervention

### Critical Patterns
- Create Application via YAML: define `source.repoURL`, `source.path`, `destination.server`, `destination.namespace`, `syncPolicy.automated`
- Create via CLI: `argocd app create <name> --repo <url> --path <path> --dest-server <cluster> --auto-prune --self-heal`
- Sync manually: `argocd app sync <name>` or click Sync in UI
- Check status: `argocd app get <name>` shows sync status, health, and resource details

### AI Collaboration Keys
- Ask Claude to generate an Application manifest for a Helm chart with custom values
- Request diagnosis steps when Application shows Synced but Health is Degraded
- Have AI explain the difference between sync status and health status

### Common Mistakes
- Confusing Synced (Git matches cluster) with Healthy (resources actually working)
- Not enabling CreateNamespace=true, causing sync failure when namespace doesn't exist
- Setting targetRevision to a branch that doesn't exist, resulting in sync errors

### Connections
- **Builds on**: Lesson 6 - ArgoCD Architecture & Installation
- **Leads to**: Lesson 8 - Sync Strategies & Policies
