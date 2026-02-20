### Core Concept

AI agents don't remember between sessions—unless you give them files to read. Persisting state in files (CLAUDE.md, ADRs, session journals) transforms ephemeral conversations into accumulated organizational knowledge, creating a "handshake" that transfers context reliably.

### Key Mental Models

- **The Handshake**: CLAUDE.md is your handshake with Claude—it gets loaded first and sets the terms of engagement. What you put there shapes every response.
- **State Hierarchy**: Ephemeral (current task), Session (WIP tracking), Project (conventions—CLAUDE.md), Permanent (architecture—ADRs). Match persistence level to information type.
- **Documentation-as-Code**: Context files should be committed with the code they document. Same commit = same context = reproducible sessions.
- **ROI Math**: 2-3 minutes to write a CLAUDE.md entry saves 15-30 minutes per session in re-explanation. After 2 sessions, it's pure profit.

### Key Facts

- **CLAUDE.md**: Claude Code automatically reads this file from project root—primary location for project-specific AI context
- **Time saved**: Well-maintained CLAUDE.md saves 15-30 min/session in context re-establishment
- **ADR investment**: 10-15 minutes to write, prevents hours of re-debating the same decisions
- **Break-even point**: Context files pay for themselves after just 2 sessions

### Critical Patterns

- **CLAUDE.md**: Project-wide patterns, coding standards, key decisions (keep under 60 lines)
- **ADRs**: "Why we chose X over Y" with context, decision, and consequences
- **Session Journals (scratchpad.md)**: Current task, completed steps, next steps, blockers—updated as you work
- **The Documentation-as-Code Habit**: Every significant decision gets committed with the code it affects
- Guide AI attention with structured context: indicate which files are relevant for which types of work

### Common Mistakes

- **Context Overload**: CLAUDE.md becomes a dumping ground for every note. Fix: Keep it focused; move domain specifics to skills.
- **Outdated context files**: Documenting old patterns when you've moved on. Fix: Treat context files as living documents.
- **Orphaned Documentation**: Context files exist but aren't committed with code. Fix: Same commit rule.
- **Scattered knowledge**: Decisions in Slack, email, heads—not in git. Fix: If it's not in git, it doesn't exist for AI.
- **No Session Continuity**: Starting fresh each session, re-explaining everything. Fix: Use session journals for multi-day work.

### Connections

- **Builds on**: Principle 4 (Decomposition)—as you break work into steps, document the plan in files
- **Leads to**: Principle 6 (Constraints)—safety rules can be encoded in CLAUDE.md, making constraints persistent
- **Synergy with P3**: Verification results should be documented so future sessions know what's been tested
