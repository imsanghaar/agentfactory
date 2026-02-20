### Core Concept
Go templating enables dynamic Kubernetes manifests through variables, pipelines, conditionals, and iteration, transforming static YAML into adaptive configurations that respond to environment differences.

### Key Mental Models
- **Pipelines as Transformations**: The `|` operator chains functions like Unix pipes, transforming values step-by-step (e.g., `| upper | quote`)
- **Scope as Context**: The `.` (dot) represents current context; `with` blocks change scope; `$` always refers to root context
- **Named Operators**: Go uses word operators (`eq`, `ne`, `gt`, `lt`) not symbols (`==`, `!=`, `>`, `&lt;`)
- **Whitespace Control**: `{{-` and `-}}` strip whitespace to prevent broken YAML indentation

### Critical Patterns
- Variables: `$var := .Values.x` stores values for reuse
- Conditionals: `{{- if eq .Values.env "prod" }}...{{- end }}`
- Range over lists: `{{- range .Values.ports }}...{{- end }}`
- Range over maps: `{{- range $key, $value := .Values.env }}`

### AI Collaboration Keys
- Request templates with conditionals and ask AI to use proper operators
- Teach AI whitespace control requirements when output has blank lines
- Ask AI to validate template rendering with different values

### Common Mistakes
- Using `==` instead of `eq` for comparisons (Go template syntax differs from most languages)
- Forgetting `quote` around string values that might contain special characters
- Losing root context inside `with` or `range` blocks (use `$` to access root)

### Connections
- **Builds on**: Lesson 1 (Introduction to Helm) - basic template syntax
- **Leads to**: Lesson 3 (Named Templates and Helpers) for reusable template code
