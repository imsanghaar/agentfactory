### Core Concept
Start Chapter 60 by creating a cloud-deployment skill that captures patterns for provisioning clusters, networking, secrets, and app rollout—built from official docs and refined through the chapter.

### Key Mental Models
- **Skill-first**: Build the asset before deeper lessons; iterate with each deployment task.
- **Spec-driven**: Define cluster, network, DNS, and secret requirements up front.
- **Provider-agnostic**: Encode reusable patterns that adapt across clouds.

### Critical Patterns
- Use `/skill-creator` with fetched provider/Kubernetes docs to build the deployment skill.
- Include provisioning, load balancer/DNS, secret management, and app rollout templates.
- Set success criteria in LEARNING-SPEC and validate generated manifests/commands.

### Common Mistakes
- Building from memory instead of docs, leading to broken IaC patterns.
- Ignoring DNS/secrets/ingress in the skill scope, forcing ad hoc fixes later.
- Treating the initial skill as final rather than improving after each lesson.

### Connections
- **Builds on**: Earlier skill-first chapters and Kubernetes/Docker foundations.
- **Leads to**: Practical cloud setup and deployment steps in the remaining lessons.
