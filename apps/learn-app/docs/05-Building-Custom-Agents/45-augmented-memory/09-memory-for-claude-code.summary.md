### Core Concept
The claude-mem plugin gives Claude Code persistent memory across sessions, demonstrating memory from the user's perspective. It uses lifecycle hooks to capture and retrieve memories automatically while providing privacy controls.

### Key Mental Models
- Lifecycle hooks capture memory at key points: session start/end, prompt submit, tool use, stop
- `<private>` tags prevent storage of sensitive information wrapped within them
- Good memory feels like a colleague who knows your style; bad memory feels like surveillance
- Explicit project onboarding creates better memory than organic accumulation

### Critical Patterns
- Hook points: SessionStart (retrieve), UserPromptSubmit (capture intent), PostToolUse (observe), Stop (extract), SessionEnd (finalize)
- Privacy configuration: `excluded_patterns` (password, api_key, secret) and `excluded_paths` (**/.env*)
- Web UI features: timeline view, semantic search, category filters, memory management
- MCP tools: `search` (semantic), `timeline` (recent), `get_observations` (specific)
- Workflow patterns: project onboarding, decision documentation, error pattern capture, privacy-aware sharing

### AI Collaboration Keys
- Use AI to configure initial memory profile with preferences, project context, and privacy settings
- Have AI design monthly memory hygiene routines for cleanup and consolidation
- Create structured project onboarding templates for consistent, useful context

### Common Mistakes
- Not using `<private>` tags for sensitive information like API keys
- Allowing stale memories (outdated preferences, old projects) to persist without cleanup
- Over-remembering irrelevant details (e.g., personal preferences unrelated to coding)

### Connections
- **Builds on**: Lesson 8 - Building a Memory-Augmented Agent (complete implementation)
- **Leads to**: Chapter 46 - Agent Evaluation (testing whether agents actually work)
