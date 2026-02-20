### Core Concept
The security checklist is a practical verification list to ensure every required control from Chapter 58 is implemented and validated.

### Key Mental Models
- **Check + evidence**: Each item needs confirmation (command/output or manifest) not just a tick.
- **Layered coverage**: Items span RBAC, networking, PSS, secrets, supply chain, Dapr security, and compliance.

### Critical Patterns
- Confirm dedicated ServiceAccounts, Roles/Bindings, default-deny NetworkPolicies, PSS labels, secret sourcing, and image scanning/signing.
- Verify Dapr mTLS/component scopes and restricted ingress/egress.
- Record audit/logging enabled and compliance mapping completed.

### Common Mistakes
- Checking boxes without proof or leaving TODOs.
- Missing one layer (e.g., open egress or unscoped components) that weakens the whole stack.
- Using mutable tags (`latest`) or default service accounts despite checklist items.

### Connections
- **Builds on**: Chapter 58 lessons.
- **Leads to**: Capstone deployment and ongoing security reviews in later chapters.
