### Core Concept
Production containers require three pillars: environment variable configuration (flexibility), health checks (observability for orchestrators), and non-root users (security through privilege limitation).

### Key Mental Models
- **ENV vs ARG**: ENV persists at runtime (configuration), ARG exists only during build (versioning)
- **Health Check Contract**: HEALTHCHECK tells orchestrators how to verify container health before routing traffic
- **Principle of Least Privilege**: Non-root users limit damage if container is compromised
- **Defense in Depth**: Multiple security layers (non-root + no secrets + health checks) compound protection

### Critical Patterns
- Set defaults with ENV, override at runtime with `-e`: `ENV LOG_LEVEL=INFO`
- Create non-root user: `RUN adduser -D -u 1000 appuser` then `USER appuser`
- Use `--chown` when copying files: `COPY --chown=appuser:appuser main.py .`
- Add HEALTHCHECK: `HEALTHCHECK --interval=30s CMD wget --spider http://localhost:8000/health || exit 1`
- Verify health with `docker inspect --format='{{.State.Health.Status}}' <container>`

### AI Collaboration Keys
- Review Dockerfiles for security gaps (root user, missing health checks, hardcoded config)
- Design health check strategy based on service dependencies
- Apply hardening patterns systematically with explanatory comments

### Common Mistakes
- Putting USER before COPY (can't copy files without ownership)
- Adding HEALTHCHECK without implementing /health endpoint
- Using wrong port in HEALTHCHECK (internal port, not host mapping)
- Putting secrets in ENV instructions (visible in image history)

### Connections
- **Builds on**: Lesson 5 (multi-stage optimization) adding security and observability
- **Leads to**: Lesson 7 (Docker Image Builder Skill) to encode patterns as reusable intelligence
