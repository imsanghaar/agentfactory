### Core Concept
ArgoCD continuously monitors resource health across five states (Healthy, Progressing, Degraded, Unknown, Missing), aggregates to application-level status, and can send notifications via Slack or webhooks when sync or health events occur.

### Key Mental Models
- **Health Aggregation**: Application health equals worst health of all contained resources; one Degraded pod makes entire Application Degraded
- **Built-in Health Checks**: ArgoCD understands standard resources (Deployment checks ready replicas, Job checks completion, PVC checks binding)
- **Custom Lua Health Checks**: For CRDs/operators, define Lua scripts in argocd-cm ConfigMap that return `hs.status` and `hs.message`
- **Notification Triggers**: Events like on-sync-succeeded, on-sync-failed, on-health-degraded fire notifications via configured services

### Critical Patterns
- Custom health check format: `resource.customizations.health.{GROUP}_{KIND}` in argocd-cm ConfigMap
- Configure notification services in argocd-notifications-cm with service.slack and template definitions
- Subscribe Applications to triggers via labels: `notifications.argoproj.io/subscribe.on-sync-failed.slack: channel-name`
- Use webhook notifications for custom integrations (PagerDuty, incident management systems)

### AI Collaboration Keys
- Ask Claude to write Lua health check for a CRD based on status.phase or conditions
- Request argocd-notifications-cm ConfigMap with Slack triggers for deployment events
- Have AI diagnose why Application shows Degraded and suggest troubleshooting steps

### Common Mistakes
- Forgetting to install argocd-notifications controller separately from ArgoCD
- Not adding notification subscription labels to Application metadata
- Writing Lua health checks that don't return the required hs object structure

### Connections
- **Builds on**: Lesson 11 - ArgoCD Projects and RBAC
- **Leads to**: Lesson 13 - Progressive Delivery Overview
