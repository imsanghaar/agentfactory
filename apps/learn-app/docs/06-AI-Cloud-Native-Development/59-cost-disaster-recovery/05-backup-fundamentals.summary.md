### Core Concept
Backups protect data by capturing consistent copies with defined RPO/RTO targets and clear ownership for restore readiness.

### Key Mental Models
- **RPO/RTO**: Recovery point vs recovery time drive backup frequency and restore planning.
- **Consistency**: Quiesce or snapshot-aware backups to avoid corrupt data.
- **Tested restores**: Backups are useless without verified restore procedures.

### Critical Patterns
- Define RPO/RTO per workload; schedule backups accordingly.
- Use storage-native snapshots or backup tools that handle app consistency.
- Document and rehearse restore runbooks; validate integrity and access controls.
- Store backups in separate locations/accounts with encryption and retention policies.

### Common Mistakes
- Setting backups without testing restores.
- Ignoring application-level consistency (e.g., databases) leading to unusable snapshots.
- Keeping backups in the same fault domain or without encryption.

### Connections
- **Builds on**: Cost/FinOps (backups incur spend) and operational discipline.
- **Leads to**: Velero-based backups, DR, and chaos testing in later lessons.
