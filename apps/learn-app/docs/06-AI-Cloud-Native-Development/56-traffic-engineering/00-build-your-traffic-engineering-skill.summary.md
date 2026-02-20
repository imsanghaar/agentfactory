### Core Concept
Build a traffic-engineer skill from official Envoy Gateway documentation before learning traffic management concepts, transforming learning into an owned asset that generates Gateway API configurations, rate limiting policies, and autoscaling rules.

### Key Mental Models
- **Skill-First Learning**: Create the skill first using fetched documentation, then improve it as you learn each traffic engineering pattern
- **LEARNING-SPEC.md**: Define what, why, and success criteria before asking AI to build the skill
- **Grounded Knowledge**: Skills built from official Context7 documentation produce accurate patterns, not hallucinated configurations
- **Validation-Driven**: Use `kubectl apply --dry-run=client` to verify generated YAML is valid

### Critical Patterns
- Clone skills-lab fresh for each chapter to avoid state assumptions
- Write LEARNING-SPEC.md with clear success criteria before skill creation
- Fetch official docs via Context7 before generating skill content
- Test skill output with dry-run validation immediately after creation

### AI Collaboration Keys
- Use Context7 skill to fetch authoritative Envoy Gateway documentation
- Specify Task API requirements clearly when generating configurations
- Answer clarifying questions about traffic patterns to customize the skill

### Common Mistakes
- Skipping LEARNING-SPEC.md and asking AI to build skill without defined success criteria
- Using AI memory instead of fetched documentation for Gateway API patterns
- Not testing generated YAML with kubectl dry-run before marking skill complete

### Connections
- **Builds on**: Kubernetes deployment skills from Chapter 50
- **Leads to**: Lesson 1 (Ingress Fundamentals) where you learn what the skill should know
