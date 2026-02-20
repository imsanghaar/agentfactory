### Core Concept
Values override precedence hierarchy (values.yaml &lt; -f file &lt; --set) enables multi-environment deployments from a single chart, while schema validation prevents invalid configurations before rendering.

### Key Mental Models
- **Precedence Hierarchy**: Later sources override earlier ones; --set has highest priority, values.yaml has lowest
- **Minimal Overrides**: Environment files should only override what differs from defaults, not repeat everything
- **Concept-Based Organization**: Nest values by what they configure (agent.*, database.*) not where they're used (deployment.*, service.*)
- **Schema as Guard**: values.schema.json catches typos and invalid values before they become broken manifests

### Critical Patterns
- Three-tier environments: values.yaml (dev defaults), values-staging.yaml, values-prod.yaml
- --set for emergency/testing: `--set image.tag=v1.0.1`
- --set-string for numeric strings: `--set-string apiKey=12345`
- Schema validation with required fields, types, enums, and ranges

### AI Collaboration Keys
- Ask AI to generate environment-specific values that only override what differs
- Request schema.json for critical fields with enum validation
- Have AI explain values precedence for specific deployment scenarios

### Common Mistakes
- Putting secrets in values files (use Kubernetes Secrets or --set from vault)
- Repeating all defaults in environment files (creates maintenance burden)
- Using --set for permanent config (not version-controlled, lost on next deploy)

### Connections
- **Builds on**: Lesson 3 (Named Templates and Helpers) - accessing values in templates
- **Leads to**: Lesson 5 (Chart Dependencies) for composing infrastructure charts
