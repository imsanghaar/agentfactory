### Core Concept
Context engineering is what separates a $50/month agent from a $5,000/month agent—not the model (everyone has access to frontier models), but the discipline of maintaining consistency, persistence, and domain expertise that accumulates rather than resets.

### Key Mental Models
- **Context Engineering Decision Tree**: Context > 70%? → Compaction. Multi-session? → Progress files. Workflow drifting? → Memory injection. Multiple agents? → Context isolation. The tree diagnoses specific problems and applies specific solutions.
- **Budget Allocation Awareness**: System prompt ~5-10%, CLAUDE.md ~5-10%, tool definitions ~10-15%, message history ~30-40%, tool outputs ~20-30%, reserve buffer ~10-15%. Message history grows to dominate—that's why conversations degrade.
- **Four Quality Criteria**: Consistency (same quality at turn 1 vs turn 50), Persistence (can resume after 24 hours), Scalability (handles 10+ step tasks without drift), Knowledge (applies domain expertise automatically).

### Critical Patterns
- The seven token budgeting strategies: summarize large text, chunk into vector DB, offload to external memory, use relevancy checks, structure prompts wisely, monitor real-time, use multi-round processing
- When-to-Use Framework: noisy context → signal audit; instructions ignored → position optimization; multi-day work → progress files; multi-agent conflicts → context isolation
- Quality gates: score 1-5 on each criterion, identify what affects each score, target improvements

### Common Mistakes
- Applying every technique instead of diagnosing the specific problem—the decision tree prevents this
- Ignoring the reserve buffer: running at 90% utilization means any file read pushes into degradation
- Not testing quality: build agents without measuring consistency, persistence, scalability, and knowledge application

### Connections
- **Builds on**: All previous lessons (Lessons 1-9) as synthesis capstone
- **Leads to**: Building production-quality specialized agents for real-world deployment
