### Core Concept
Helm charts distribute via OCI-compliant registries (Docker Hub, ECR, ACR) using the same infrastructure and authentication as container images, unifying artifact management with semantic versioning.

### Key Mental Models
- **OCI Unification**: Same registry stores both Docker images and Helm charts; one auth model, one API
- **Package to Artifact**: helm package creates .tgz; helm push uploads to registry with version tag
- **Semantic Versioning**: Chart version determines registry tag; MAJOR.MINOR.PATCH signals compatibility
- **OCI URL Format**: `oci://registry/repo/chart:version` references charts like Docker images

### Critical Patterns
- Package: `helm package .` creates {chart}-{version}.tgz
- Authenticate: `helm registry login docker.io`
- Push: `helm push chart-1.0.0.tgz oci://docker.io/username/`
- Install directly: `helm install release oci://registry/chart:version`

### AI Collaboration Keys
- Ask AI to explain OCI vs traditional Helm repository differences
- Request workflow for multi-version chart publishing
- Have AI generate CI/CD patterns for automated chart distribution

### Common Mistakes
- Using docker pull on Helm charts (different artifact type, use helm pull)
- Reusing version numbers after pushing (creates ambiguity, always bump version)
- Forgetting trailing slash in push URL (helm push needs repo path, not chart path)

### Connections
- **Builds on**: Lesson 7 (Testing Your Charts) - only publish validated charts
- **Leads to**: Lesson 9 (Library Charts) for organizational standardization
