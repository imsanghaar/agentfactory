### Core Concept
Named templates (partials) enable DRY principles in Helm charts by defining reusable template fragments in _helpers.tpl that can be included across multiple manifests with consistent labels, selectors, and annotations.

### Key Mental Models
- **Define Once, Include Everywhere**: Named templates eliminate copy-paste duplication across Deployment, Service, and ConfigMap
- **Underscore Convention**: Files prefixed with `_` (like `_helpers.tpl`) are not rendered as standalone manifests
- **Include vs Template**: Always use `include` (returns string, supports pipes) instead of deprecated `template` (renders directly, breaks indentation)
- **Namespacing**: Prefix template names with chart name (e.g., `myapp.labels`) to prevent collisions with subcharts

### Critical Patterns
- Define: `{{- define "myapp.labels" }}...{{- end }}`
- Include with indentation: `{{ include "myapp.labels" . | nindent 4 }}`
- Context passing: Always pass `.` to include for access to .Chart, .Values, .Release
- Root access in loops: Use `$` to access root context inside `range` blocks

### AI Collaboration Keys
- Ask AI to identify duplicate template sections across manifests
- Request helper templates for common patterns (labels, selectors, imagePullSecrets)
- Have AI show include syntax with proper nindent for different positions

### Common Mistakes
- Forgetting to pass context (`.`) to include: `{{ include "name" }}` fails, need `{{ include "name" . }}`
- Wrong indentation level with nindent (count spaces from left margin)
- Using `template` instead of `include` (breaks YAML indentation)

### Connections
- **Builds on**: Lesson 2 (Advanced Go Templating) - variables, conditionals, loops
- **Leads to**: Lesson 4 (Values Deep Dive) for multi-environment configuration
