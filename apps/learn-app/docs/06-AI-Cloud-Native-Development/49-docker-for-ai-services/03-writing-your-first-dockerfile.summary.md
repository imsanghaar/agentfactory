### Core Concept
A Dockerfile is a recipe of instructions (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD) that Docker reads top-to-bottom to build an image, with each instruction creating a cacheable layer.

### Key Mental Models
- **Layer Caching**: Unchanged instructions reuse cached layers; place frequent changes at bottom for fast rebuilds
- **RUN vs CMD**: RUN executes during build (creates layer), CMD executes when container starts (no layer)
- **Build Context**: Docker sends your directory to the daemon; .dockerignore excludes unnecessary files
- **Instruction Order**: Dependencies first (rarely change) > application code last (frequently changes)

### Critical Patterns
- Start with `FROM python:3.12-slim` for minimal base
- Use `COPY --from=ghcr.io/astral-sh/uv:latest` for UV package manager
- Copy dependency files before code: `COPY pyproject.toml .` then `RUN uv sync`
- Use `--host 0.0.0.0` in CMD for container networking
- Build with `docker build -t name:tag .` and run with `-p host:container`

### AI Collaboration Keys
- Ask AI to diagnose slow build times (usually layer ordering)
- Troubleshoot native compilation failures (packages needing Rust/C)
- Design Dockerfiles for your specific API with proper comments

### Common Mistakes
- Wrong instruction order (copying all files before installing deps invalidates cache)
- Missing .dockerignore (sends .venv, .git, secrets to build context)
- Using localhost instead of 0.0.0.0 (container networking requires 0.0.0.0)

### Connections
- **Builds on**: Lesson 2 (understanding images and layers)
- **Leads to**: Lesson 4 (Container Lifecycle and Debugging)
