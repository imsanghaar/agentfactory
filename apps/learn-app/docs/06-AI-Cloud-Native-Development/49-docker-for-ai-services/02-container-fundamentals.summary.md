### Core Concept
Images are immutable templates (read-only blueprints) while containers are running instances with writable layers on top; this distinction enables reproducibility, security, and efficient resource sharing.

### Key Mental Models
- **Copy-on-Write**: Containers add a thin writable layer on top of immutable image layers; writes copy files to this layer
- **Layer Stacking**: Images are built from independent, reusable layers that can be shared across multiple images
- **Coffee Analogy**: Image is the recipe, container is the cup of coffee you make; multiple cups from same recipe
- **Immutability Guarantee**: Same image digest guarantees identical environment forever

### Critical Patterns
- Pull images with `docker pull python:3.12-slim` or `nginx:alpine`
- Run interactive containers with `-it` flag, detached with `-d` flag
- List running containers with `docker ps`, all containers with `docker ps -a`
- Execute commands inside containers with `docker exec <container> <command>`
- Access shell with `docker exec -it <container> sh`

### AI Collaboration Keys
- Ask AI to compare layer structures between different images
- Verify container independence by creating files in one container
- Investigate stopped containers to understand exit behavior

### Common Mistakes
- Storing important data in containers (use volumes for persistence)
- Trusting image tags for true immutability (use digests: `python@sha256:...`)
- Forgetting containers exist after stopping (`docker ps -a` shows them)

### Connections
- **Builds on**: Lesson 1 (installation and architecture understanding)
- **Leads to**: Lesson 3 (Writing Dockerfiles) to create your own images
