### Core Concept
The coordinator-dispatcher pattern separates user-facing communication from background work. Agent acknowledges request immediately, processes silently, saves results to persistent storage, and confirms completion—exactly two messages.

### Key Mental Models
- **Two-message architecture**: Acknowledgment → Silent processing → Completion
- **Silent processing phase**: All work invisible to user (search, enrich, format, save)
- **File persistence = artifact evidence**: Reports serve as audit trails and reusable outputs

### Critical Patterns
- File tool: `pathlib.Path.cwd() / filename` for cross-platform paths
- Return status dicts, not exceptions: `{"status": "success|error", "message": "..."}`
- Agent instructions explicitly state "Do NOT send intermediate messages"
- Markdown report templates remove format ambiguity

### AI Collaboration Keys
- Agent instructions must name the pattern ("two-message," "silent processing")
- Reference specific tools in order they should be used
- Include markdown template in instructions so agent follows format exactly

### Common Mistakes
- Streaming intermediate results (violates two-message pattern)
- Raising exceptions from file tools (agent should receive status dict)
- Using relative paths without pathlib (cross-platform issues)

### Connections
- **Builds on**: Session State & Memory (Lesson 3)
- **Leads to**: Callbacks & Guardrails (Lesson 5)
