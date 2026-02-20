### Core Concept
Set up DigitalOcean accounts, credentials, and baseline security to provision and manage Kubernetes clusters safely.

### Key Mental Models
- **Account hygiene**: MFA, restricted API tokens, and least-privilege access.
- **Separation**: Isolate projects/environments to avoid cross-contamination.
- **Credential management**: Store tokens securely and inject via CI/secret managers.

### Critical Patterns
- Create DO projects per env; enable MFA and SSO where possible.
- Generate scoped API tokens; store in secret managers for tooling/CI.
- Prepare billing/quotas and regions aligned to deployment needs.

### Common Mistakes
- Using broad tokens or sharing accounts across teams/environments.
- Storing tokens in plaintext in repos or CI variables without protection.
- Ignoring quotas/limits until provisioning fails.

### Connections
- **Builds on**: Cloud readiness from prior lessons.
- **Leads to**: DOKS cluster provisioning and networking setup.
