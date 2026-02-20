### Core Concept
Compose MCP-wrapping and script-execution skills into orchestrated workflows. Define step sequence, data contracts between steps, error recovery per step, and convergence criteria. Workflows are DAGs with state management.

### Key Mental Models
- **Skill composition**: Output from Step N = Input to Step N+1; workflow validates compatibility
- **Data contracts**: Output format contract (Skill A defines) + Input format contract (Skill B expects) + Validation layer
- **Recovery hierarchy**: Recoverable? → Retry with backoff → Fallback strategy → Escalate
- **Convergence = terminal state**: Success (all steps complete) OR Failure (max retries/unrecoverable)

### Critical Patterns
- Workflow spec: Intent, Steps (name/input/output/success/failures), Data contracts, State management, Convergence criteria
- Error recovery table: Step | Failure | Detection | Recovery | Fallback | Max Attempts
- Retry with backoff: [1, 2, 4] seconds between attempts; exponential to avoid overwhelming services
- Graceful degradation: Continue with empty/cached data when step fails but workflow can proceed

### AI Collaboration Keys
- Test all paths: happy, degradation, recovery, escalation
- State must persist across steps for resume capability
- Iteration limits prevent infinite loops—define per step and globally

### Common Mistakes
- No data contract validation (silent failures when formats mismatch)
- Missing fallback strategies (single failure kills entire workflow)
- No convergence criteria (workflow never terminates)

### Connections
- **Builds on**: Build Script-Execution Skill (Lesson 6)
- **Leads to**: Capstone: Shippable Agent Skill (Lesson 8)
