### Core Concept
Begin Chapter 58 by creating a reusable cloud-security skill up front—define a learning spec, fetch official Kubernetes security docs, and generate least-privilege patterns (RBAC, NetworkPolicy, PSS, secrets, scanning, Dapr security) so every later lesson refines a working asset.

### Key Mental Models
- **Skill-first learning**: Specify goals and success criteria (LEARNING-SPEC.md) before building, then iterate each lesson.
- **Defense in depth (4C)**: Cloud → Cluster → Container → Code; Kubernetes security spans RBAC, network isolation, pod security, and secrets.
- **Source-of-truth docs**: Ground patterns in official Kubernetes security guidance via Context7 to avoid hallucinated YAML.

### Critical Patterns
- Draft LEARNING-SPEC.md with scope (RBAC, NetworkPolicy, PSS, secrets, image scanning, Dapr mTLS/component scopes) and measurable checks.
- Use Context7 to fetch Kubernetes security docs, then drive `/skill-creator` to build the `cloud-security` skill with templates and references.
- Validate the skill by generating ServiceAccount/Role/RoleBinding YAML and applying `kubectl apply --dry-run=client`.

### Common Mistakes
- Building skills from memory instead of authoritative docs, leading to insecure or invalid manifests.
- Overprivileged RBAC (wildcards) or missing PSS/NetworkPolicy defaults that erode least privilege.
- Skipping success criteria, leaving no way to verify the skill’s output.

### Connections
- **Builds on**: Earlier skill-first practice (Ch.53/55) and Kubernetes basics from Chapters 49–51.
- **Leads to**: Applying and tightening security controls in subsequent Chapter 58 lessons.
