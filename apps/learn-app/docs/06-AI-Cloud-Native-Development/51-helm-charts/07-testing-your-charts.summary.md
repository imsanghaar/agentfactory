### Core Concept
Chart testing spans static validation (helm lint, helm template) to runtime verification (test pods, helm test), creating a safety net that catches errors before they reach production.

### Key Mental Models
- **Static vs Runtime**: lint/template catch syntax errors locally; test pods verify live connectivity
- **Exit Code Semantics**: Test pods signal success with exit 0, failure with non-zero; Helm reports results
- **Unit vs Integration**: Unit tests (helm-unittest) validate template logic; integration tests verify deployed behavior
- **Test Hook Annotation**: Pods with `helm.sh/hook: test` run only during `helm test`, not during install

### Critical Patterns
- Validation flow: helm lint -> helm template -> helm install -> helm test
- Test pod annotation: `helm.sh/hook: test` with `helm.sh/hook-delete-policy: hook-succeeded`
- Unit test structure: YAML files in tests/ with assertions on rendered output
- Debug rendering: `helm template --debug` shows line-by-line template evaluation

### AI Collaboration Keys
- Ask AI to create test pods that verify service connectivity
- Request helm-unittest patterns for template conditionals
- Have AI generate validation workflows with proper timeout handling

### Common Mistakes
- Running helm test before deployment (release must exist)
- Forgetting test hook annotation (pod runs during install instead of test phase)
- Assuming helm lint catches all errors (it validates structure, not Kubernetes semantics)

### Connections
- **Builds on**: Lesson 6 (Helm Hooks and Lifecycle) - test hooks are lifecycle hooks
- **Leads to**: Lesson 8 (OCI Registries and Distribution) for publishing validated charts
