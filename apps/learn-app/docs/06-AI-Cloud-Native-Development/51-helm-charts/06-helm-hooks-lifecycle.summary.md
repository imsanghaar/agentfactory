### Core Concept
Helm hooks execute Kubernetes Jobs at specific lifecycle points (pre-install, pre-upgrade, post-delete) to automate tasks like database migrations, cache invalidation, and backup creation as part of the deployment workflow.

### Key Mental Models
- **Lifecycle Timing**: 9 hook types correspond to install/upgrade/delete/rollback phases; pre-hooks block if they fail
- **Hook Weights**: Lower weight = earlier execution; use negative weights for critical first steps (-10, -5, 0, 5, 10)
- **Delete Policies**: Control cleanup with hook-succeeded, hook-failed, before-hook-creation
- **Idempotency Required**: Hooks may run multiple times; use IF NOT EXISTS patterns for safe re-execution

### Critical Patterns
- Hook annotation: `helm.sh/hook: pre-upgrade`
- Weight ordering: `helm.sh/hook-weight: "-5"` runs before weight "0"
- Cleanup: `helm.sh/hook-delete-policy: hook-succeeded,before-hook-creation`
- Always use Jobs (not Pods) for durability and completion semantics

### AI Collaboration Keys
- Ask AI to create migration hooks with retry logic for database startup delays
- Request hook sequences for backup -> migrate -> validate patterns
- Have AI explain what happens when hooks fail at different phases

### Common Mistakes
- Non-idempotent migrations (ALTER TABLE without IF NOT EXISTS fails on retry)
- Missing delete-policy causes hook Jobs to accumulate in cluster
- Pre-hooks block deployment; post-hooks complete even if they fail

### Connections
- **Builds on**: Lesson 5 (Chart Dependencies) - hooks run against dependency services
- **Leads to**: Lesson 7 (Testing Your Charts) for validating hook behavior
