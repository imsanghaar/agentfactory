### Core Concept
Automate Docker image building in GitHub Actions using the docker/build-push-action, tagging images with commit SHAs for traceability and pushing to container registries (Docker Hub, GHCR, ECR) for deployment.

### Key Mental Models
- **Image Tagging Strategy**: Use commit SHA, branch name, and semantic version tags for traceability
- **Registry Authentication**: Configure credentials once in secrets, use docker/login-action
- **Layer Caching**: Speed up builds by caching Docker layers between workflow runs
- **Multi-Platform Builds**: Use buildx for ARM and AMD64 images from single workflow

### Critical Patterns
- Use `docker/login-action` to authenticate to container registry
- Use `docker/metadata-action` to generate tags from git context
- Use `docker/build-push-action` with cache-from and cache-to for speed
- Tag with `${{ github.sha }}` for exact commit traceability

### AI Collaboration Keys
- Ask Claude to generate optimized Dockerfile and build workflow for your stack
- Request cache configuration for fastest possible builds
- Have AI explain multi-stage Docker builds for smaller production images

### Common Mistakes
- Using `latest` tag alone without commit SHA (impossible to trace deployments)
- Not configuring build caching (slow builds on every commit)
- Exposing registry credentials in workflow logs

### Connections
- **Builds on**: Lesson 2 - GitHub Actions Fundamentals
- **Leads to**: Lesson 4 - Testing and Quality Gates
