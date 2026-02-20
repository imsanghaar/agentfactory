# Delegation Patterns

## Core Rule: Orchestrate, Don't Implement

Main session MANAGES work, subagents IMPLEMENT work.

**Main session doing heavy work = guaranteed failure.** Context bloats, strategy lost, quality degrades.

## When to Delegate (ALWAYS)

- Browser automation (Chrome MCP, web scraping)
- Multi-step execution (content creation, deployments)
- SDD phases (/sp.specify → plan → tasks → implement)
- Code implementation (new features, bug fixes)
- Long-running operations (anything > 5 minutes)
- Educational content (use content-implementer, educational-validator)

## Main Session ONLY Does

- Read requests and decide approach
- Plan delegation (which subagent, what prompt)
- Spawn subagents via Task tool
- Read subagent output files
- Verify quality before marking complete
- Report results to user
- Escalate when stuck

## SDD as Background Tasks

**Problem:** Running SDD loop in same session causes context compaction.

**Solution:**
```
Main Session (Manager)              Background Tasks (Specialists)
├── Preserves original intent       ├── Task: /sp.specify → spec.md
├── Preserves success criteria      ├── Task: plan mode → plan.md
├── Orchestrates phases             ├── Task: tasks → tasks.md
└── Never loses the "why"           └── Task: implement → code
```

## Pattern

```
Main: "Feature request arrived"
Main: Task(subagent_type="Plan", prompt="Create spec for...")
Main: *reads spec.md, verifies quality*
Main: Task(subagent_type="general-purpose", prompt="Implement...")
Main: *reads output, verifies quality*
...
Main: "Work complete"
```

## Subagent Prompt Requirements

**Always include:**
```
Execute autonomously without confirmation.
Output path: /absolute/path/to/file.md
Match quality of reference at [path] if applicable.
```

**Never include:**
- "Should I proceed?" (causes deadlock)
- Relative paths (causes ambiguity)
- Open-ended exploration (causes bloat)
