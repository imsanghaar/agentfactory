### Core Concept
Multi-stage builds separate dependency installation (build stage with tools) from runtime (minimal stage), combined with UV package manager and Alpine base images to achieve 70-90% image size reduction.

### Key Mental Models
- **Build vs Runtime Separation**: Build stage has compilers and dev tools; runtime stage has only what's needed to run
- **COPY --from**: Transfer only necessary artifacts between stages; build stage is discarded
- **Base Image Tradeoffs**: Full (900MB) > slim (150MB) > alpine (50MB) with compatibility vs size tradeoff
- **Layer Analysis**: Use `docker history` to identify which layers contribute most to size

### Critical Patterns
- Use `FROM python:3.12-slim AS builder` then fresh `FROM python:3.12-alpine` for runtime
- Copy site-packages and bin from builder: `COPY --from=builder /usr/local/lib/python3.12/site-packages ...`
- Install UV for 10-100x faster package installation: `RUN pip install uv && uv pip install --system --no-cache`
- Combine RUN commands and clean caches in same layer
- Volume mount large files (>100MB) instead of embedding in image

### AI Collaboration Keys
- Analyze existing Dockerfiles for size optimization opportunities
- Generate multi-stage Dockerfiles with specific constraints
- Debug unexpected image sizes using `docker history` output

### Common Mistakes
- Embedding model files in image (use volume mounts instead)
- Using Alpine when packages need C compilation (fall back to slim)
- Leaving build tools and caches in runtime stage

### Connections
- **Builds on**: Lesson 4 (debugging) with size measurement and validation
- **Leads to**: Lesson 6 (Production Hardening) for security and observability
