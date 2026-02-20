### Core Concept
RBAC enforces least privilege in Kubernetes: bind a dedicated ServiceAccount to narrowly scoped Roles/ClusterRoles so pods can do only what they must—and nothing more.

### Key Mental Models
- **Four-piece model**: ServiceAccount (who) → Role/ClusterRole (what) → Binding (connect) → Scope (namespace vs cluster).
- **Least privilege**: Deny by default; never use wildcards; disable token automount unless needed.
- **Verification loop**: Use `kubectl auth can-i` to confirm allowed/denied actions before rollout.

### Critical Patterns
- Create per-app ServiceAccounts with `automountServiceAccountToken: false`; mount tokens explicitly when needed.
- Define Roles with specific resources/verbs; use ClusterRoles only when cross-namespace access is required.
- Bind SA to Role with RoleBinding (or ClusterRoleBinding for cluster scope).
- Test access via `kubectl auth can-i --as=system:serviceaccount:...` and enforce namespace scoping.

### Common Mistakes
- Using default service account or cluster-admin-level bindings for apps.
- Wildcarding resources/verbs or granting cluster-wide access unnecessarily.
- Skipping verification, leaving broken or overprivileged permissions in production.

### Connections
- **Builds on**: 4C security model.
- **Leads to**: NetworkPolicies, PSS, secrets management, and Dapr security controls in later lessons.
