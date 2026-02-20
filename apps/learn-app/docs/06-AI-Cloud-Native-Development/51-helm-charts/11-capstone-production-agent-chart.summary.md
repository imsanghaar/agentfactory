### Core Concept
Specification-first development produces production-grade Helm charts by establishing clear success criteria and acceptance tests before implementation, then synthesizing all chapter concepts into a complete AI agent deployment with dependencies, hooks, and multi-environment support.

### Key Mental Models
- **Spec as Contract**: Written specification with acceptance criteria guides implementation and validation
- **Component Composition**: Single helm install deploys agent + PostgreSQL + Redis + migrations together
- **Environment Scaling**: Same chart deploys to dev (1 replica, 256Mi) through prod (3 replicas, 1Gi)
- **Validation-Driven**: Acceptance criteria (helm install works, helm test passes, multi-env works) prove completion

### Critical Patterns
- Specification structure: Intent, Success Criteria, Requirements, Constraints, Non-Goals
- Chart architecture: Deployment + Service + ConfigMap + Secret + hooks + tests + dependencies
- Pre-upgrade migration hook with weight -5 runs before deployment updates
- Checksum annotations trigger rollouts when config/secrets change

### AI Collaboration Keys
- Use AI to validate specification against production best practices
- Request edge case testing scenarios (network failures, migration failures)
- Have AI suggest production hardening (PDB, NetworkPolicies, HPA)

### Common Mistakes
- Starting implementation without clear specification
- Skipping acceptance criteria verification
- Hardcoding passwords instead of using Kubernetes Secrets

### Connections
- **Builds on**: All lessons (templating, dependencies, hooks, testing, distribution)
- **Leads to**: Lesson 12 (Building Helm Chart Skill) for encoding expertise as reusable skill
