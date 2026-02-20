### Core Concept
Secrets must never be stored in plaintext in Git; use Sealed Secrets (cluster key encryption committed to Git) or External Secrets Operator (sync from external vaults like HashiCorp Vault, AWS Secrets Manager) to maintain GitOps while keeping secrets secure.

### Key Mental Models
- **Sealed Secrets**: Encrypt with cluster public key using kubeseal; only that cluster can decrypt; encrypted YAML safe to commit
- **External Secrets Operator**: SecretStore defines vault connection; ExternalSecret specifies which vault secrets to sync to Kubernetes
- **Git Security Paradox**: GitOps requires everything in Git, but secrets must never be plaintext in Git; encryption at rest solves this
- **Secret Rotation**: For Sealed Secrets, re-encrypt and commit new sealed YAML; for External Secrets, update vault and controller auto-syncs

### Critical Patterns
- Install Sealed Secrets controller, then use `kubeseal -f secret.yaml -w sealed-secret.yaml` to encrypt
- ExternalSecret references SecretStore and specifies `remoteRef.key` path in external vault
- Commit only encrypted SealedSecret or ExternalSecret CRDs to Git (never plaintext)
- Separate secrets by environment: production/sealed-secret.yaml vs development/sealed-secret.yaml

### AI Collaboration Keys
- Ask Claude to generate kubeseal workflow for encrypting API keys
- Request ExternalSecret and SecretStore configuration for HashiCorp Vault integration
- Have AI design secret rotation workflow for 90-day key expiration

### Common Mistakes
- Committing plaintext secret.yaml to Git (permanent security exposure in history)
- Not adding secret files to .gitignore before accidentally committing them
- Using same secrets across environments (compromised dev key affects production)

### Connections
- **Builds on**: Lesson 13 - Progressive Delivery Overview
- **Leads to**: Lesson 15 - Multi-Cluster Deployments
