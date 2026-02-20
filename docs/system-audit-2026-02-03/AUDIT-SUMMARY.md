# System Audit Summary: Teaching vs Implementation Gap

**Date:** 2026-02-03
**Auditors:** 4 parallel subagents analyzing Chapters 1, 3, 4, 5

---

## CRITICAL FINDING

**The book teaches patterns that the book creation system doesn't follow.**

This creates a credibility gap: we're teaching students to use Claude Code a certain way, but our own infrastructure violates those teachings.

---

## AUDIT RESULTS BY CHAPTER

### Chapter 1: Vision & Agent Maturity Model

| Finding                                                          | Severity | Action                    |
| ---------------------------------------------------------------- | -------- | ------------------------- |
| "Seven Principles" references non-existent "Part 1, Chapter 3"   | CRITICAL | Fix or remove reference   |
| Five Powers framework (See/Hear/Reason/Act/Remember) not encoded | HIGH     | Add to CLAUDE.md          |
| Vibe Coding warning missing from CLAUDE.md                       | HIGH     | Add explicit anti-pattern |
| Digital FTE vision well-aligned                                  | OK       | No action                 |
| Tool Generations (Gen 1-5) not referenced                        | MEDIUM   | Add for context           |

### Chapter 3: Claude Code as Manager (Boris Cherny Workflow)

| Finding                                                | Severity | Action                      |
| ------------------------------------------------------ | -------- | --------------------------- |
| Skills average 371 lines (should be <150)              | CRITICAL | Refactor or move to agents  |
| No Ralph Wiggum Loop usage                             | HIGH     | Adopt for validation cycles |
| No session hygiene skills (/session-review, /techdebt) | HIGH     | Create utility skills       |
| Skills are specialized agents disguised as skills      | CRITICAL | Separate concerns           |
| 24:1 subagent:skill ratio (inverted)                   | HIGH     | Rebalance architecture      |
| CLAUDE.md not self-improving                           | MEDIUM   | Add feedback loops          |

### Chapter 4: Context Engineering

| Finding                                | Severity | Action                     |
| -------------------------------------- | -------- | -------------------------- |
| CLAUDE.md is 632 lines (should be ~60) | CRITICAL | Refactor to Three-Zone     |
| Three-Zone strategy not implemented    | CRITICAL | Apply Zone 1/2/3           |
| Zero progress files                    | CRITICAL | Create project-progress.md |
| Constitution 1996 lines always loaded  | HIGH     | Make read-on-demand        |
| No memory injection documentation      | MEDIUM   | Document hook corpus       |
| Instruction budget at ceiling (~150)   | HIGH     | Reduce to ~35 core         |

### Chapter 5: SDD Native vs SpecKit Plus

| Finding                                                | Severity | Decision         |
| ------------------------------------------------------ | -------- | ---------------- |
| Chapter 5 teaches NATIVE Claude Code, not SpecKit Plus | INFO     | Clarify in docs  |
| sp.specify duplicates native file writing              | LOW      | DROP             |
| sp.plan marginally useful                              | LOW      | CONDITIONAL KEEP |
| sp.tasks extraction automation valuable                | MEDIUM   | KEEP             |
| sp.clarify interview scaffolding valuable              | MEDIUM   | KEEP             |
| sp.implement duplicates Chapter 5 Lesson 7             | LOW      | DROP             |
| sp.analyze orthogonal to SDD                           | LOW      | DROP             |
| sp.chapter essential for content work                  | HIGH     | KEEP             |

---

## ARCHITECTURE DECISION: What to Keep/Drop

### KEEP (Native + Essential Custom)

```
Native Claude Code:
├── Tasks system (TaskCreate, TaskUpdate, TaskList)
├── Plan Mode
├── Subagent spawning
├── AskUserQuestion
├── CLAUDE.md (project memory)
└── File system (specs as markdown files)

Custom (Essential):
├── Constitution (governance principles)
├── sp.chapter (content orchestration)
├── sp.tasks (task extraction)
├── sp.clarify (interview discipline)
├── sp.git.* (git workflow helpers)
└── Templates (spec, plan, tasks as reference)
```

### DROP or DEPRECATE

```
Redundant Commands:
├── sp.specify → Write specs to files directly
├── sp.implement → Chapter 5 Lesson 7 pattern
├── sp.analyze → Manual grep/analysis
├── sp.adr → Optional documentation

Bloated Infrastructure:
├── 632-line CLAUDE.md → Refactor to 55 lines
├── Skills >200 lines → Move logic to agents or split
├── Always-loaded constitution → Read-on-demand
└── Missing progress files → Create coordination mechanism
```

---

## THE PATH FORWARD

### Phase 1: Fix Critical Infrastructure (1-2 days)

```
□ Fix "Seven Principles" broken reference in CLAUDE.md
□ Refactor CLAUDE.md to Three-Zone strategy (~55 lines)
□ Create project-progress.md template
□ Add Vibe Coding warning to CLAUDE.md Zone 1
□ Document which sp.* commands to keep vs drop
```

### Phase 2: Apply Own Teaching (2-3 days)

```
□ Move 800+ line skills to agent definitions or split
□ Create session hygiene skills (/session-review)
□ Implement Ralph Wiggum Loop for validation cycles
□ Make constitution read-on-demand via hooks
□ Extract Zone 2 content to docs/ folder
```

### Phase 3: Package as Plugin (3-5 days)

```
□ Define book-generation-plugin manifest
□ Extract portable components
□ Create self-validation mechanism
□ Document minimal SDD setup (native only)
□ Test plugin on fresh project
```

### Phase 4: Self-Recurring Capability

```
□ Plugin reads chapters to verify alignment
□ Plugin updates itself when teachings change
□ Plugin generates progress reports
□ Plugin validates it follows its own rules
```

---

## QUANTITATIVE SUMMARY

| Metric                 | Current             | Target                 | Gap     |
| ---------------------- | ------------------- | ---------------------- | ------- |
| CLAUDE.md lines        | 632                 | 55                     | 10.5x   |
| Constitution load      | Always (1996 lines) | On-demand (~150 lines) | 13x     |
| Skill average size     | 371 lines           | <150 lines             | 2.5x    |
| Skills utilized        | 38% (8/21)          | 80%+                   | 2x      |
| Agents with tools      | 42% (5/12)          | 100%                   | 2.4x    |
| Progress files         | 0                   | 1+                     | Missing |
| Ralph Loop usage       | 0%                  | Active                 | Missing |
| Session hygiene skills | 0                   | 3-5                    | Missing |

---

## DECISION POINT: SpecKit Plus

**Recommendation: SIMPLIFY**

1. **Keep for content work**: sp.chapter, sp.tasks, sp.clarify, sp.git.\*
2. **Drop as redundant**: sp.specify, sp.implement, sp.analyze, sp.adr
3. **Keep templates as reference**: spec-template.md, plan-template.md, tasks-template.md
4. **Keep constitution**: Core governance document
5. **Update documentation**: Chapter 5 teaches native SDD; SpecKit Plus is optional convenience

**The book's SDD chapter doesn't depend on SpecKit Plus. Students learn native Claude Code patterns.**

---

## FILES GENERATED

```
.claude/research/system-audit-2026-02-03/
├── AUDIT-SUMMARY.md           ← This file
├── ch1-vision-audit.md        ← Chapter 1 detailed findings
├── ch3-claude-code-manager-audit.md  ← Chapter 3 detailed findings
├── ch4-context-engineering-audit.md  ← Chapter 4 detailed findings
└── ch5-sdd-speckit-audit.md   ← Chapter 5 detailed findings
```

---

## NEXT STEPS

1. Review this summary
2. Decide on SpecKit Plus keep/drop for each command
3. Prioritize Phase 1 fixes (critical infrastructure)
4. Create GitHub issues for tracking
5. Begin refactoring CLAUDE.md to Three-Zone strategy

**The meta-irony**: This audit itself should have used our own Chapter 4 progress file pattern. We didn't. That's the gap.
