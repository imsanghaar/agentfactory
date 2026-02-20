### Core Concept
Library charts (type: library) encode organizational standards as reusable templates that application charts consume as dependencies, ensuring consistent labels, probes, and security contexts across all deployments.

### Key Mental Models
- **Standards as Code**: Library charts encode organizational patterns (labels, security) that all applications inherit
- **Cannot Be Installed**: Library charts provide templates only; they cannot be deployed directly
- **Include Pattern**: Application charts use `include` to pull library templates with proper indentation
- **Override Hierarchy**: Applications customize library defaults through values.yaml under library chart name

### Critical Patterns
- Declare library: `type: library` in Chart.yaml
- Define templates: `{{- define "org-standards.labels" }}...{{- end }}`
- Consume as dependency: Add to application Chart.yaml dependencies
- Use templates: `{{ include "org-standards.labels" . | nindent 4 }}`

### AI Collaboration Keys
- Ask AI to identify patterns across multiple charts that should become library templates
- Request library chart structure for organizational standards
- Have AI show override patterns for application-specific customization

### Common Mistakes
- Trying to install library charts (Helm blocks this intentionally)
- Using library chart name instead of template name in include
- Hardcoding values in library templates instead of using values with defaults

### Connections
- **Builds on**: Lesson 8 (OCI Registries) - distribute library charts via registries
- **Leads to**: Lesson 10 (AI-Assisted Chart Development) for collaborative refinement
