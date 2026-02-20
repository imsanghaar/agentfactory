### Core Concept
Velero delivers Kubernetes-aware backups and restores, capturing cluster resources and persistent volumes with policies aligned to RPO/RTO.

### Key Mental Models
- **K8s-native**: Back up both objects and volumes; restores must match namespaces and storage classes.
- **Schedules + retention**: Automate recurring backups with labeled retention policies.
- **Isolation**: Store backups in separate buckets/credentials for resilience.

### Critical Patterns
- Install Velero with proper cloud plugin/credentials; configure backup storage location.
- Create schedules for critical namespaces; include/exclude resources intentionally.
- Test restores into non-prod namespaces/clusters; verify PV data and app health.
- Secure credentials and encrypt backups; set TTLs for cleanup.

### Common Mistakes
- Backing up only manifests without PV snapshots (or vice versa).
- Restoring into mismatched storage classes or missing CRDs, causing failures.
- Not testing restores or leaving Velero credentials overly privileged.

### Connections
- **Builds on**: Backup fundamentals.
- **Leads to**: Chaos engineering and DR scenarios that validate restore plans.
