### Core Concept

Tasks are filesystem-backed persistent state—your plan lives on disk in `~/.claude/tasks/`, not in context. This decouples your roadmap from your conversation, letting you `/clear` aggressively without losing the project plan.

### Key Mental Models

- **Plan-on-Disk = Context Freedom**: Old Todos lived in chat and vanished with `/clear`. Tasks persist on filesystem, so clearing context no longer means losing your roadmap.
- **Dependency DAGs**: Tasks can block other tasks via `blockedBy` relationships. When Task 1 completes, Task 2 automatically becomes available. Complex projects form directed acyclic graphs of dependencies.
- **Tasks vs Progress Files**: Tasks track WHAT needs to be done (action items). Progress files track WHAT you've learned (decisions, discoveries). Use both together.

### Critical Patterns

- Phase 1 Plan: Create tasks at session start when context is fresh with proper `blockedBy` dependencies
- Phase 2 Clear: When context fills (60-80%), run `/clear`—your plan survives on disk
- Phase 3 Execute: Press `Ctrl+T` or ask "What's next?" to see unblocked tasks and continue
- Cross-session coordination: Use `CLAUDE_CODE_TASK_LIST_ID=project-name` to share task state between terminals

### Common Mistakes

- Treating context as the only place to store your plan—you'll lose it when you need to clear
- Not using dependency relationships—tasks complete in wrong order or overlap
- Forgetting the Writer/Reviewer pattern: shared task lists enable multi-session handoffs without stepping on each other

### Connections

- **Builds on**: Context architecture and knowing when to clear (Lesson 3)
- **Leads to**: Tacit knowledge extraction for persistent domain expertise (Lesson 5)
