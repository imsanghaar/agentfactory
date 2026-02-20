### Core Concept
Start Chapter 50 by building a `kubernetes-deployment` skill from official docs so you can deploy and scale containers while refining the skill through later lessons.

### Key Mental Models
- **Skill-first**: Create the skill before deep learning; improve it as you progress.
- **Doc-grounded**: Use Context7 to pull Kubernetes documentation, not memory.
- **Deployment focus**: The skill targets real deployments from “hello world” to production.

### Critical Patterns
- Clone/open the skills lab, then prompt `/skill-creator` to build the Kubernetes skill using fetched docs.
- Capture templates and references for resources, scaling, health checks, and limits in the skill.
- Keep the skill in `.claude/skills/kubernetes-deployment/` for iterative refinement during the chapter.

### Common Mistakes
- Building from assumptions instead of official docs, leading to bad manifests.
- Skipping clarifying questions, so the skill misses requirements (limits, health checks, scaling).
- Treating the initial skill as final instead of refining it per lesson.

### Connections
- **Builds on**: Skill-first pattern from earlier chapters.
- **Leads to**: Kubernetes architecture and resource lessons that harden this skill.
