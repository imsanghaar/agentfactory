### Core Concept
Container debugging requires reading logs, executing commands inside containers, and inspecting configuration to diagnose failures that would otherwise be hidden behind Docker's abstraction layer.

### Key Mental Models
- **Container Forensics**: Use `docker logs`, `docker inspect`, and exit codes to understand what happened
- **Inside vs Outside**: Test from inside container with `docker exec` to isolate application vs networking issues
- **Restart Policies**: Configure automatic recovery with `--restart=unless-stopped` for production resilience
- **Detached Debugging**: Running containers with `-d` requires explicit log checking

### Critical Patterns
- View logs with `docker logs <container>`, follow with `-f`, limit with `--tail N`
- Execute commands with `docker exec <container> <cmd>`, shell with `-it sh`
- Inspect configuration with `docker inspect --format='{{...}}' <container>`
- Check exit codes: 0=success, 1=error, 137=OOM killed
- Resolve port conflicts by using different host port or stopping conflicting container

### AI Collaboration Keys
- Create containers with required environment variables and diagnose when missing
- Debug port mapping issues by testing from inside container
- Configure resilient services with restart policies and resource limits

### Common Mistakes
- Not checking logs when container exits immediately
- Using wrong port in HEALTHCHECK (use internal container port, not host port)
- Running as root without `--restart` policy in production

### Connections
- **Builds on**: Lesson 3 (writing Dockerfiles) with practical debugging scenarios
- **Leads to**: Lesson 5 (Multi-Stage Builds) for production optimization
