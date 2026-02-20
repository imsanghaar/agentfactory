### Core Concept
Sync waves control deployment ordering with ascending wave numbers (-1, 0, 1, 2), while resource hooks (PreSync, PostSync, SyncFail) execute Jobs at critical sync lifecycle points for database migrations, notifications, and smoke tests.

### Key Mental Models
- **Sync Wave**: Annotation (`argocd.argoproj.io/sync-wave: "0"`) that groups resources by creation order; ArgoCD waits for each wave to stabilize before proceeding
- **PreSync Hook**: Job that runs before any resources sync; ideal for database migrations using `argocd.argoproj.io/hook: PreSync`
- **PostSync Hook**: Job that runs after sync completes successfully; used for Slack notifications, smoke tests, cache warming
- **Hook Deletion Policy**: Controls Job cleanup after execution (HookSucceeded, HookFailed, BeforeHookCreation)

### Critical Patterns
- Run database migrations in wave -1 with PreSync hook: `argocd.argoproj.io/sync-wave: "-1"` plus `argocd.argoproj.io/hook: PreSync`
- Deploy ConfigMaps/Secrets in wave 0, Deployments/Services in wave 1, verification in wave 2
- Use `HookSucceeded` deletion policy for one-time jobs like migrations
- Use `HookFailed` to keep failed jobs for debugging instead of auto-deleting

### AI Collaboration Keys
- Ask Claude to create PreSync hook for alembic database migrations with secret references
- Request PostSync hook that sends Slack notifications with deployed image tag
- Have AI explain hook ordering when combining waves and hook types

### Common Mistakes
- Setting PreSync hook in wave 1+ (runs after resources it should precede)
- Using HookSucceeded when debugging is needed (job deleted before logs accessible)
- Missing backoffLimit and restartPolicy on hook Jobs (infinite retries or restarts)

### Connections
- **Builds on**: Lesson 8 - Sync Strategies and Policies
- **Leads to**: Lesson 10 - ApplicationSets: Scaling Deployments
