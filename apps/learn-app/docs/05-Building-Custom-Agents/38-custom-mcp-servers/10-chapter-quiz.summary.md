### Core Concept
20-question assessment covering all Chapter 38 topics: Context objects, sampling, notifications, roots, transport, scaling, error handling, and packaging. Tests both conceptual understanding and implementation knowledge. Passing: 15/20 (75%), Advanced: 18/20 (90%).

### Key Mental Models
- **Context injection**: Dependency injection enables automatic wiring without boilerplate
- **Sampling economics**: Client bears token cost; server stays provider-agnostic
- **Roots security**: Canonicalize paths, check against declared roots
- **Scaling tradeoffs**: Stateful = features; Stateless = horizontal scaling

### Critical Patterns
- Context: After `*` separator, per-request isolation
- Sampling: `context.session.create_message()` routes through client
- Progress: `report_progress(completed, total)` with completed = done count
- Roots: `is_path_allowed()` with abspath + realpath before comparison
- Packaging: `[project.scripts]` entry point in pyproject.toml

### AI Collaboration Keys
- Quiz identifies weak areas for targeted review
- "Try With AI" section for deep dives on challenging concepts
- Self-assessment: Can you explain sampling? Design roots? Choose transport?

### Common Mistakes
- Confusing stateless (horizontal scaling) with stateful (features)
- Not understanding cost shifting in sampling
- Missing path traversal prevention in roots

### Connections
- **Builds on**: Capstone: Production MCP Server (Lesson 9)
- **Leads to**: Chapter 39 (Agent Skills)
