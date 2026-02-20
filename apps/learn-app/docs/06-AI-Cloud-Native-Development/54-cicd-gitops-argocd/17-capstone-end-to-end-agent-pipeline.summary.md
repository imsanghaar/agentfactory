### Core Concept
Build a complete CI/CD pipeline from code push to running agent using GitHub Actions (test, build, push, update GitOps repo) and ArgoCD (detect change, sync, health check), with rollback via git revert.

### Key Mental Models
- **Specification-First**: Define intent, success criteria, components, and non-goals before writing YAML
- **CI/CD Flow**: Push triggers test (80% coverage), build (multi-platform), push (GHCR), update-gitops (kustomize edit)
- **GitOps Separation**: Code repo (source) separate from GitOps repo (manifests); CI updates GitOps repo image tag
- **Audit Trail**: Every deployment traceable to Git commit; rollback is git revert, not kubectl delete

### Critical Patterns
- GitHub Actions jobs: test (pytest coverage), build-and-push (docker/build-push-action), update-gitops (kustomize edit set image)
- GitOps repo structure: `fastapi-agent/base/` with kustomization.yaml, deployment.yaml, service.yaml
- ArgoCD Application with auto-sync watches GitOps repo, syncs within 3 seconds of change detection
- Rollback workflow: identify commit, git revert, push triggers new build with reverted code

### AI Collaboration Keys
- Ask Claude to troubleshoot stuck builds (layer caching, network timeouts, disk space)
- Request diagnosis for OutOfSync status (targetRevision, path, Git token issues)
- Have AI explain GitOps repo token configuration when image tag updates fail

### Common Mistakes
- Missing `secrets.GITOPS_REPO_TOKEN` preventing CI from pushing to GitOps repo
- Using imagePullPolicy: IfNotPresent causing cached old images during rollback
- Not testing complete flow before relying on it for production

### Connections
- **Builds on**: Lesson 16 - AI-Assisted GitOps Workflows
- **Leads to**: Lesson 18 - Building the GitOps Deployment Skill
