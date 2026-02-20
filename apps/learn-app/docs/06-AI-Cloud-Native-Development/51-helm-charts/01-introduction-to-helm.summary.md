### Core Concept
Helm is the package manager for Kubernetes that solves the repetitive YAML problem by templating deployments with parameterized values, enabling consistent multi-environment deployments from a single chart.

### Key Mental Models
- **Chart as Package**: A Helm chart packages all Kubernetes manifests (Deployment, Service, ConfigMap) into a reusable directory structure
- **Values as Configuration**: values.yaml provides defaults; environment-specific files override only what differs
- **Release as Instance**: Each helm install creates a versioned release that can be upgraded, rolled back, or uninstalled
- **Template Substitution**: Go template syntax ({{ .Values.x }}) replaces hardcoded values with parameterized placeholders

### Critical Patterns
- Chart structure: Chart.yaml (metadata), values.yaml (defaults), templates/ (manifests)
- helm install creates release; helm upgrade updates; helm rollback reverts
- Use `-f values-prod.yaml` for environment-specific configuration
- helm template previews rendered manifests without deploying

### AI Collaboration Keys
- Ask AI to generate Chart.yaml and values.yaml for specific requirements
- Use AI to create environment-specific values files (dev/staging/prod)
- Refine by asking about secrets handling and hook patterns

### Common Mistakes
- Copying and modifying YAML files for each environment instead of using values overrides
- Forgetting to run helm repo update before installing public charts
- Hardcoding environment-specific values in templates instead of values.yaml

### Connections
- **Builds on**: Lesson 0 (Build Your Helm Skill) - test skill against basic chart creation
- **Leads to**: Lesson 2 (Advanced Go Templating) for dynamic manifest generation
