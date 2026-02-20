### Core Concept
Long-horizon work requires the harness architecture: treat each session as independent, coordinated through a shared progress file. The progress file becomes the coordination mechanism between sessions—each session reads it, does work, writes back. Sessions don't share context; they share the file.

### Key Mental Models
- **Two-Agent Mental Model**: The Initializer Agent (first session) breaks down the project and creates the progress file. Working Agents (subsequent sessions) read progress, select tasks, execute, and update. The file bridges session boundaries.
- **Task Decomposition Principle**: "Complete the analysis" isn't a task—it's a project. Decompose into 10-15 concrete items, each verifiable and completable in 30-90 minutes.
- **Checkpoint = Recovery Point**: Never end a session with work in unstable state. Checkpoints (commits, saved drafts) externalize progress so context can be cleared without losing work.

### Critical Patterns
- Progress file anatomy: Completed (with session markers), In Progress (with subtask status), Blocked (specific blockers), Decisions Made (with rationale), Known Issues (with impact/plan), Session Log
- Session initialization: Read progress file → verify baseline → select highest-priority task → establish what exists
- Session exit: Save checkpoint → update progress file with completed tasks, new decisions, session summary

### Common Mistakes
- Vague task descriptions: "Do the research" can't be tracked—break into "Review papers 1-5 and extract themes"
- Missing the Decisions Made section: in Session 7, you'll wonder "why did we choose this approach?" without documented rationale
- Ending sessions with messy, half-done work: next session starts with cleanup instead of progress

### Connections
- **Builds on**: Context lifecycle and checkpoint patterns (Lesson 6)
- **Leads to**: Memory injection for mid-stream context relevance (Lesson 8)
