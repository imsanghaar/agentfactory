# Failure Modes Reference

Read this when you need examples of what NOT to do.

## Chapter 9: Wrong Pedagogical Layer

**Date**: 2025-11-18

**Error**: Applied Layer 4 (Spec-Driven) thinking to a Layer 1 (Manual Foundation) chapter.

**What went wrong**:

- Did NOT read chapter-index.md to check Part number
- Did NOT verify what students know at this stage
- Assumed "no code examples" meant "teach specifications instead of syntax"
- Created 5 new lessons before user pointed out fundamental misunderstanding

**Fix**: Always read chapter-index.md first. Part 3 = students have NO programming yet.

---

## Chapter 14: Format Drift

**Date**: 2025-11-27

**Error**: Taught wrong skill file format.

**What went wrong**:

- Used flat file format instead of directory structure
- Missing YAML frontmatter
- Did NOT read Chapter 5 Lesson 7 which teaches correct format

**Correct format**:

```
.claude/skills/
└── skill-name/
    └── SKILL.md  # With YAML frontmatter
```

---

## Skill → Spec Bypass

**Date**: 2025-11-29

**Error**: Wrote spec directly instead of using `/sp.specify`.

**What went wrong**:

- Used skill for brainstorming (correct)
- Then wrote `specs/*/spec.md` directly with Write tool
- Never invoked `/sp.specify`

**Fix**: Skills INFORM specs, they don't REPLACE the workflow.

---

## Folder Naming Inconsistency

**Date**: 2025-11-29

**Error**: Used 3 different folder names for same feature.

**Prevention**: Before creating any artifact:

```bash
find specs/ history/prompts/ -type d -name "*feature*" | head -1
```

---

## Subagent Deadlock

**Date**: 2025-12-23

**Error**: Subagents waited for confirmation that never came.

**What went wrong**:

- Launched 12 parallel agents
- 2 included "Is this correct? Should I proceed?"
- Subagents cannot receive human confirmation

**Fix**: Always include "Execute autonomously without confirmation" in subagent prompts.

---

## Engineering Anti-Patterns (General)

**Date**: 2026-02-04

These are subtle conceptual errors of a "slightly sloppy, hasty junior dev":

| Anti-Pattern               | What It Looks Like                                      |
| -------------------------- | ------------------------------------------------------- |
| **Silent assumptions**     | Filling in ambiguous requirements without checking      |
| **Unmanaged confusion**    | Proceeding despite inconsistencies                      |
| **Missing clarifications** | Not asking when something is unclear                    |
| **Hidden inconsistencies** | Not surfacing conflicts you notice                      |
| **Unexplained tradeoffs**  | Making non-obvious decisions without presenting options |
| **No pushback**            | Implementing bad ideas without objection                |
| **Sycophancy**             | "Of course!" to clearly problematic approaches          |
| **Overcomplicated code**   | 1000 lines when 100 would suffice                       |
| **Bloated abstractions**   | Premature generalization                                |
| **Dead code left behind**  | Not cleaning up after refactors                         |
| **Scope creep**            | "Cleaning up" code orthogonal to the task               |
| **Uninformed deletion**    | Removing things you don't fully understand              |

**Fix**: Each has a corresponding workflow principle in `rules/workflow-principles.md`.

---

## Content Failures (Quick Reference)

- ❌ **Confusing chapter and part numbers** → `ch 11` ≠ `part 4` (always `ls -d` to discover)
- ❌ Skipping chapter README → Wrong pedagogical layer
- ❌ Teaching patterns without checking canonical source → Format drift
- ❌ Not using skills when available → Spawning subagents for simple tasks
- ❌ Subagent prompts with "Should I proceed?" → Deadlock
- ❌ Letting agents infer output paths → Wrong directories
- ❌ **Writing statistics/dates without web verification** → Hallucinated facts (Chapter 2 incident)
- ❌ **Skipping full YAML frontmatter** → Missing skills, learning objectives
- ❌ **Minimal "Try With AI" sections** → Quality degradation
- ❌ **Multi-line description in agent YAML** → Tool parsing breaks

---

## Platform/Code Failures (Quick Reference)

- ❌ **Implementing before researching existing solutions** → Reinvented wheel (DocPageActions incident)
- ❌ **Skipping edge case analysis** → Missed rate limits, permissions
- ❌ **Not considering testing context vs production** → Browser automation behaves differently
- ❌ **COMMITTING WITHOUT LIVE VERIFICATION** → Broke production for 3+ hours (2026-02-04)

---

## Session Productivity Failures (Usage Report 2026-02-05)

These patterns were identified across 12,260 sessions:

| Anti-Pattern | Evidence | Impact |
|--------------|----------|--------|
| **Redundant file reading** | conftest.py 6x, schemas.py 5x per session | Wasted 40%+ tokens and time |
| **No completion criteria** | 336/344 sessions "partially_achieved" | Work abandoned mid-flight |
| **Broad interpretation** | 309 "misunderstood request" instances | Implemented wrong thing |
| **Unstructured research** | 5+ OpenClaw sessions with similar outputs | Redundant exploration |

**Fixes integrated into workflow**:
- File Memory Protocol in CLAUDE.md
- Session Completion Protocol in CLAUDE.md
- Domain Term Clarification in CLAUDE.md
- Research templates in skills

---

## Prevention Summary

1. Always read context first
2. Always use absolute paths for subagents
3. Always use `/sp.*` commands for workflows
4. Verify file exists after subagent writes: `ls -la [path]`
5. Research existing solutions before implementing
6. **Live verify before committing to main**
7. **Read files ONCE per session** — summarize, then reference summary
8. **Define "done" upfront** — state deliverables before starting
9. **Clarify ambiguous terms** — ask before assuming
