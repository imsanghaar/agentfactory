### Core Concept
Sync policies control when and how ArgoCD deploys changes: manual sync requires explicit triggers, auto-sync deploys on Git changes, auto-prune deletes removed resources, self-heal reverts unauthorized cluster modifications, and sync windows restrict deployments to specific times.

### Key Mental Models
- **Auto-Sync**: ArgoCD polls Git every 3 seconds and automatically applies changes without manual intervention
- **Auto-Prune**: Delete resources from cluster when removed from Git; prevents orphaned resources but requires Git discipline
- **Self-Heal**: Automatically revert manual kubectl changes back to Git-declared state; enforces Git as single source of truth
- **Sync Windows**: Cron-based time restrictions using allow/deny windows to control when deployments can occur

### Critical Patterns
- Enable auto-sync with `syncPolicy.automated: {}` for true GitOps automation
- Use `prune: true` only after confirming all resources are in Git and reviewed before deletion
- Use `selfHeal: true` when team agrees Git is the only source of truth
- Configure sync windows with cron syntax: `schedule: "0 2 * * 0"` for Sunday 2 AM deployments

### AI Collaboration Keys
- Ask Claude about tradeoffs between auto-prune safety vs orphaned resource cleanup
- Request sync window configuration for maintenance-only deployments
- Have AI explain strategies for emergency changes when self-heal is enabled

### Common Mistakes
- Enabling prune before ensuring all resources are tracked in Git (accidental deletions)
- Using self-heal without team agreement (reverts emergency fixes)
- Forgetting Replace strategy for immutable field changes (selector modifications fail with Apply)

### Connections
- **Builds on**: Lesson 7 - Your First ArgoCD Application
- **Leads to**: Lesson 9 - Sync Waves and Resource Hooks
