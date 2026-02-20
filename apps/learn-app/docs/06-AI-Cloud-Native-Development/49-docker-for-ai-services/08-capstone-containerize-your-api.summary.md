### Core Concept
Apply specification-first containerization to the SQLModel + Neon Task API, writing constraints and success criteria BEFORE implementation to avoid Vibe Coding and ensure production readiness.

### Key Mental Models
- **Specification-First**: Write what you're building and success criteria before touching code
- **Constraint-Driven Design**: Image size, security, and configuration constraints shape Dockerfile decisions
- **Cross-Machine Validation**: True portability means anyone can `docker pull` and run your container
- **Registry as Distribution**: Push to Docker Hub or GHCR to share containers beyond your machine

### Critical Patterns
- Write containerization-spec.md with intent, constraints, success criteria, and non-goals
- Apply multi-stage build with UV, Alpine, non-root user, and HEALTHCHECK
- Pass DATABASE_URL at runtime with `-e` flag (never embed secrets)
- Tag images with version and push: `docker tag task-api:v1 username/task-api:v1`
- Validate each success criterion with specific commands and expected output

### AI Collaboration Keys
- Review specifications for gaps in security constraints or edge cases
- Optimize Dockerfiles for size, security, and rebuild speed
- Design tagging strategies with semantic versions and git hashes

### Common Mistakes
- Jumping to code without writing specification (Vibe Coding anti-pattern)
- Forgetting `?sslmode=require` for Neon PostgreSQL connections
- Not testing cross-machine pull and run (only validates local build)

### Connections
- **Builds on**: All chapter lessons (fundamentals, Dockerfiles, debugging, optimization, hardening, skill)
- **Leads to**: Chapter 50 (Kubernetes) for orchestrating multiple containers
