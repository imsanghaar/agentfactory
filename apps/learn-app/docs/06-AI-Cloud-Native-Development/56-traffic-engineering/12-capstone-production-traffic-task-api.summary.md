### Core Concept
Capstone integrates all traffic engineering patterns (Gateway, HTTPRoute, rate limiting, TLS, KEDA autoscaling) using specification-first development where success criteria (SC-001 through SC-007) define "production-ready" before generating any YAML.

### Key Mental Models
- **Specification-First**: Write traffic-spec.md with validation commands before generating configuration
- **Success Criteria Validation**: Each SC-XXX has a concrete bash command that must succeed
- **Phased Application Order**: Namespace -> TLS Secret -> Gateway -> HTTPRoute -> Policies -> ScaledObject
- **Skill Finalization**: Complete template library with decision tree for all traffic engineering scenarios

### Critical Patterns
- Write spec with business goals and measurable success criteria before implementation
- Apply Gateway before HTTPRoute (route depends on gateway existing)
- Use `kubectl wait --for=condition=Programmed` before applying dependent resources
- Validate with `kubectl apply --dry-run=client` before actual application

### AI Collaboration Keys
- Generate complete traffic stack from specification requirements
- Produce validation commands matching each success criterion
- Create reusable template library for future deployments

### Common Mistakes
- Applying HTTPRoute before Gateway is programmed (causes attachment failures)
- Missing TLS secret before Gateway with HTTPS listener
- Skipping dry-run validation before production apply

### Connections
- **Builds on**: Lessons 0-11 (all traffic engineering patterns)
- **Leads to**: Chapter 57 (Dapr Actors & Workflows) for distributed application patterns
