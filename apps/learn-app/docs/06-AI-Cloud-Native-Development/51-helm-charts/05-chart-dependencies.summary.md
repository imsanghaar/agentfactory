### Core Concept
Chart dependencies enable composition of production infrastructure by declaring subcharts (PostgreSQL, Redis) in Chart.yaml, so a single helm install deploys your application with all its supporting services.

### Key Mental Models
- **Composition over Construction**: Use community charts (Bitnami) instead of building database deployments from scratch
- **Conditional Dependencies**: Use `condition: postgresql.enabled` to make dependencies optional per environment
- **Tags for Grouping**: Group related dependencies (database, cache, messaging) for bulk enable/disable
- **Subchart Configuration**: Parent values pass to subcharts through nested keys (postgresql.auth.username)

### Critical Patterns
- Declare dependencies: Chart.yaml `dependencies:` with name, version, repository
- Semantic versioning: `^13.0.0` allows minor/patch updates; `~11.1.0` allows patch only
- Fetch subcharts: `helm dependency update` downloads to charts/ directory
- Configure via parent: Subchart name becomes values key (postgresql:, redis:)

### AI Collaboration Keys
- Ask AI to generate Chart.yaml with proper dependency declarations
- Request values.yaml structure for configuring subcharts
- Have AI explain version constraints for production deployments

### Common Mistakes
- Forgetting `helm dependency update` after changing Chart.yaml dependencies
- Using exact versions in production (misses security patches)
- Conflicting condition and tag settings (condition takes precedence)

### Connections
- **Builds on**: Lesson 4 (Values Deep Dive) - configuring subcharts through values
- **Leads to**: Lesson 6 (Helm Hooks and Lifecycle) for pre-deployment automation
