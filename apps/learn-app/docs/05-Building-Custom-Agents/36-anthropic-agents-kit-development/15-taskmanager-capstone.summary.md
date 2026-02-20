### Core Concept
TaskManager integrates all 8 Claude Agent SDK features into a deployable Digital FTE: canUseTool (permissions), settingSources (skills), slash commands, file checkpointing, session resume, cost tracking, lifecycle hooks, context compaction. Specification-first, then implementation.

### Key Mental Models
- **Specification-first**: Write complete spec before code—enables AI-driven development
- **8 features integration**: Permissions + Skills + Commands + Checkpointing + Sessions + Costs + Hooks + Compaction
- **Digital FTE maturity**: Safety validated + costs tracked + pricing sustainable + audit logged

### Critical Patterns
- ClaudeAgentOptions with all features: setting_sources, custom_command_paths, allow_file_checkpointing, session_id, track_costs, hooks, context_compaction_strategy
- canUseTool: Role-based decisions (intern can't delete, manager can assign)
- Deployment checklist: Permissions tested, persistence validated, recovery works, billing integrated

### AI Collaboration Keys
- Specification drives quality—write it completely before implementation
- Map business requirements to SDK features in requirements table
- Calculate unit economics: avg cost/customer vs subscription price = margin

### Common Mistakes
- Implementing before specifying (leads to rework)
- Integrating all features at once instead of incrementally
- Shipping without validating safety constraints (permissions, checkpointing)

### Connections
- **Builds on**: Production Patterns (Lesson 14)
- **Leads to**: Chapter Quiz (Lesson 16)
