### Core Concept
Dapr provides unified APIs for secrets management and dynamic configuration, abstracting secret stores (Vault, AWS Secrets Manager) and config stores (Redis, etcd) from application code.

### Key Mental Models
- **Secrets API**: Retrieve secrets at runtime without embedding in code or environment
- **Configuration API**: Dynamic config that can change without redeployment
- **Secret Store Components**: Pluggable backends (local file, Kubernetes secrets, Vault)
- **Configuration Subscriptions**: Watch for config changes and react in real-time

### Critical Patterns
- Get secret: GET from `/v1.0/secrets/{store-name}/{secret-name}`
- Get config: GET from `/v1.0/configuration/{store-name}`
- Subscribe to config changes: GET with watch parameter
- Reference secrets in component YAML using secret references

### AI Collaboration Keys
- Ask Claude to design secret rotation strategies
- Request config subscription handlers for feature flags
- Have AI generate secret store component YAML for your provider

### Common Mistakes
- Storing secrets in environment variables instead of secret stores
- Not implementing config change handlers (missing dynamic updates)
- Forgetting scopes on secret stores (all apps can access all secrets by default)

### Connections
- **Builds on**: Lesson 7 - Jobs API for scheduled operations
- **Leads to**: Lesson 9 - Capstone Task API with Dapr
