### Core Concept
AppProjects define security boundaries restricting source repositories, destination namespaces, and resource types, while RBAC policies use p (permission) and g (group) syntax to control which users can perform which actions on which Applications.

### Key Mental Models
- **AppProject**: CRD that restricts sourceRepos (where to deploy from), destinations (where to deploy to), and resource types (what can be deployed)
- **RBAC p policy**: Permission rule format `p, role:name, resource, action, project/app, allow/deny`
- **RBAC g policy**: Group assignment format `g, user@email.com, role:name`
- **Least Privilege**: Start with `policy.default: deny` and explicitly allow only necessary actions

### Critical Patterns
- Restrict team to specific repos: `sourceRepos: ["https://github.com/myorg/team-repo"]`
- Block system namespaces with `deniedNamespaces: ["argocd", "kube-system"]`
- Block cluster-scoped resources: `clusterResourceBlacklist` for Namespace, ClusterRole, ClusterRoleBinding
- Scope permissions per project: `p, role:frontend-dev, applications, sync, frontend-team/*, allow`

### AI Collaboration Keys
- Ask Claude to design AppProject and RBAC for multi-team isolation (frontend vs backend teams)
- Request RBAC policy that allows sync but blocks delete for developer role
- Have AI explain wildcard patterns in RBAC policies (*/*, project/*, */app-name)

### Common Mistakes
- Using permissive default policy (`policy.default: allow`) instead of deny-by-default
- Granting `applications, *` when only sync/get needed (excessive permissions)
- Forgetting to deny access to other teams' namespaces in deniedNamespaces

### Connections
- **Builds on**: Lesson 10 - ApplicationSets: Scaling Deployments
- **Leads to**: Lesson 12 - Health Status and Notifications
