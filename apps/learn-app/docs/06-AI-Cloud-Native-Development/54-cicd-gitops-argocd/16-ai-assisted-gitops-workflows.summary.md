### Core Concept
AI generates GitOps manifests quickly but requires human evaluation and iterative refinement because AI lacks visibility into actual cluster topology, registry credentials, environment constraints, and organizational naming conventions.

### Key Mental Models
- **AI Generation Strengths**: Boilerplate ApplicationSets, multi-environment templates, manifest composition, pattern suggestions
- **AI Visibility Gaps**: Actual cluster names/URLs, registry credentials, environment-specific constraints, security policies
- **Iterative Refinement**: Initial generation, constraint sharing, manifest revision, validation testing
- **7-Point Checklist**: Cluster references, registry credentials, namespace alignment, resource limits, sync strategies, health checks, variable substitution

### Critical Patterns
- Provide AI with actual cluster server URLs, registry URIs, and pull secret names
- Share environment-specific constraints: auto-sync for dev, manual for prod
- Validate with `argocd app create --dry-run` and `argocd app diff` before applying
- Test with one cluster before scaling to multi-cluster ApplicationSets

### AI Collaboration Keys
- Ask Claude to generate initial ApplicationSet, then refine with your cluster topology
- Request explanations of tradeoffs between different templating approaches (Helm values vs Kustomize patches)
- Have AI identify assumptions in generated manifests that need environment validation

### Common Mistakes
- Accepting AI-generated manifests without checking cluster-specific values
- Not providing registry credentials and pull secret names to AI
- Skipping dry-run validation before production deployment

### Connections
- **Builds on**: Lesson 15 - Multi-Cluster Deployments
- **Leads to**: Lesson 17 - Capstone: End-to-End Agent Pipeline
