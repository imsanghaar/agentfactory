### Core Concept
Data sovereignty ensures data stays within required jurisdictions and complies with regional regulations, influencing where and how you store, process, and back up data.

### Key Mental Models
- **Location constraints**: Residency and locality requirements dictate storage/backup regions.
- **Access governance**: Who can access data across regions matters as much as storage location.
- **Compliance mapping**: Align storage, replication, and recovery with legal/contractual obligations.

### Critical Patterns
- Choose regions/buckets per compliance needs; prevent cross-region replication where disallowed.
- Encrypt data in transit/at rest; control cross-border access via IAM and network rules.
- Document data flows and DR plans that respect sovereignty; test restores in-region.

### Common Mistakes
- Replicating backups across prohibited regions or using global services without constraints.
- Granting broad access that bypasses residency intent.
- Lacking documentation/audits to prove data locality compliance.

### Connections
- **Builds on**: Backup/DR planning and compliance fundamentals.
- **Leads to**: Capstone resilient/cost-aware Task API that respects locality constraints.
