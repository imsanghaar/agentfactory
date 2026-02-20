# Chapter 4 Redesign Proposal

**Date**: 2026-01-30
**Status**: Awaiting Approval
**Based On**: User feedback, official Claude Code documentation, Greg Foster article framing

---

## Problem Statement

User review identified critical quality issues:

1. **Lesson 1 fails its mission** — Doesn't clearly define what context engineering IS
2. **Content is too long** — Lessons are verbose, excessive forward referencing
3. **Missing Context Architecture lesson** — No explanation of how CLAUDE.md + Skills + Subagents + Hooks form a complete system
4. **Skills not explained** — Only brief mention in Lesson 9, not as strategic context management approach
5. **Labs too code-specific** — "Review authentication module" excludes non-developers
6. **Lacks official grounding** — Doesn't reference Anthropic's own guidance

---

## Redesign Strategy

### New Framing (from Greg Foster + Official Docs)

**Industry Validation**: "Context is AI coding's real bottleneck in 2026" — This establishes WHY context engineering matters from an industry perspective.

**Official Guidance** (from code.claude.com):

> "Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills."

This becomes our authoritative anchor throughout the chapter.

### New Lesson Structure (12 lessons, +1 from current 11)

| #      | Title                                                   | Core Teaching                                                                | Key Change                                                              |
| ------ | ------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **1**  | **The Context Bottleneck: What Context Engineering Is** | Define context engineering, industry validation, official Anthropic guidance | REWRITE: Lead with clear definition, Greg Foster framing, official docs |
| **2**  | The Attention Budget                                    | U-shaped attention curve, 70% threshold, zone system                         | MINOR: Domain-neutral labs                                              |
| **3**  | Lost in the Middle                                      | Position sensitivity, three-zone strategy                                    | MINOR: Domain-neutral labs                                              |
| **4**  | Signal vs Noise                                         | 4-question audit, under-60-line target                                       | MINOR: Domain-neutral labs                                              |
| **5**  | **Context Architecture: The Complete System**           | How CLAUDE.md + Skills + Subagents + Hooks work as integrated context system | **NEW LESSON**                                                          |
| **6**  | Tacit Knowledge Transfer                                | Knowledge extraction, memory lifecycle                                       | RENUMBER (was 5)                                                        |
| **7**  | Context Lifecycle                                       | /clear vs /compact, session management                                       | RENUMBER (was 6)                                                        |
| **8**  | Progress Files                                          | Multi-session architecture, commit checkpoints                               | RENUMBER (was 7)                                                        |
| **9**  | Memory Injection                                        | PreToolUse injection, semantic memory                                        | RENUMBER (was 8)                                                        |
| **10** | Context Isolation                                       | Clean slate vs dirty slate, orchestrator pattern                             | RENUMBER (was 9)                                                        |
| **11** | The Context Engineering Playbook                        | Decision frameworks, full toolkit integration                                | RENUMBER (was 10)                                                       |
| **12** | Chapter Quiz                                            | Assessment                                                                   | RENUMBER (was 11)                                                       |

---

## Detailed Lesson Rewrites

### Lesson 1: The Context Bottleneck (COMPLETE REWRITE)

**Current Problem**: Opens with manufacturing analogy, never clearly defines context engineering

**New Structure**:

```markdown
# The Context Bottleneck: What Context Engineering Is

## Opening: The Real Bottleneck (Greg Foster framing)

If you've used AI coding assistants, you've hit the wall.
Not the "AI isn't smart enough" wall—the "AI forgot what I told it" wall.

Industry analysts are calling this "the context gap"—the difference
between what AI COULD do with perfect context and what it actually
does with the messy reality of accumulated conversations, unread files,
and forgotten instructions.

**Context engineering is the discipline of controlling what your AI
sees so it produces consistent, high-quality output.**

## Official Guidance (Anthropic)

From Claude Code documentation:

> "Most best practices are based on one constraint: Claude's context
> window fills up fast, and performance degrades as it fills."

This isn't a Claude-specific problem. It's the fundamental constraint
of all transformer-based AI. Understanding it changes everything.

## What Context Actually Is

Context is everything the model processes before generating output:
[Table of 5 components with percentages]

## The Asymmetry That Changes Everything

|                  | Prompts       | Context           |
| ---------------- | ------------- | ----------------- |
| Token budget     | 50-200 tokens | 200,000+ tokens   |
| Your control     | What you type | What you engineer |
| Impact on output | 0.1%          | 99.9%             |

If you're optimizing prompts while ignoring context, you're
polishing the doorknob while the house is on fire.

## Context Cost by Feature (Official Data)

[Table from code.claude.com showing context cost by feature:

- CLAUDE.md: Every request
- Skills: Descriptions every request, full content when used
- MCP servers: Every request (tool definitions)
- Subagents: Isolated (doesn't consume main context)
- Hooks: Zero (runs externally)]

This table IS context engineering in action. Choosing between
CLAUDE.md (always loaded) vs Skills (on-demand) is a context
engineering decision.

## Lab: The Context Gap Diagnostic

[Domain-neutral version with non-code examples]

## Try With AI

[3 domain-neutral prompts]
```

---

### Lesson 5: Context Architecture (NEW LESSON)

**Why This Lesson**: Students know how to USE CLAUDE.md, Skills, Subagents, Hooks (Chapter 3). This lesson teaches how they work TOGETHER as a context management SYSTEM.

```markdown
# Context Architecture: The Complete System

## The Question

You have four context management tools:

- CLAUDE.md (persistent, always loaded)
- Skills (on-demand, loaded when relevant)
- Subagents (isolated context, returns summaries)
- Hooks (zero context cost, runs externally)

How do you decide which to use when?

## The Context Loading Timeline

[Diagram showing WHEN each tool loads context]

Session Start:
├─ CLAUDE.md loads (FULL content, every request)
├─ Skill DESCRIPTIONS load (~100 tokens each)
├─ MCP tool DEFINITIONS load
└─ Hooks: Nothing (they run externally)

On Demand:
├─ Skill FULL content loads when invoked
├─ Subagent launches with fresh, isolated context
└─ Hooks return output ONLY if configured

## The Decision Framework

| Information Type                 | Tool      | Why                                 |
| -------------------------------- | --------- | ----------------------------------- |
| **Always needed, never changes** | CLAUDE.md | Loaded once, available everywhere   |
| **Sometimes needed, stable**     | Skills    | On-demand loading saves context     |
| **Needs fresh perspective**      | Subagent  | Isolated context prevents pollution |
| **Must happen every time**       | Hook      | Deterministic, no LLM involved      |

## Example: A Legal Document Project

A paralegal working with contract review:

**CLAUDE.md** (always loaded, ~60 lines):

- Firm's naming conventions
- Standard clause formatting
- Required signature blocks

**Skills** (loaded when relevant):

- `/contract-review` — Full checklist for contract analysis
- `/clause-library` — Standard clause templates
- `/jurisdiction` — State-specific legal requirements

**Subagent** (isolated context):

- Research agent reads 50+ case files, returns 500-token summary
- Main context never sees 200K tokens of case law

**Hook** (zero context cost):

- After every edit, hook validates document format
- Runs externally, returns only pass/fail

## The Math of Context Architecture

Without architecture (everything in CLAUDE.md):

- 500-line CLAUDE.md = ~4,000 tokens
- Loaded EVERY request = context bloat
- Attention diluted across rarely-needed content

With architecture:

- 60-line CLAUDE.md = ~500 tokens (always)
- 3 skills × 100 token descriptions = ~300 tokens (always)
- Full skill content = ~2,000 tokens (only when invoked)
- Research via subagent = 0 tokens in main context

**Result**: 10x less baseline context load

## Lab: Map Your Context Architecture

[Students map their current project to the 4-tool framework]

## Try With AI

[3 prompts for designing context architecture]
```

---

## All Labs: Domain-Neutral Redesign

**Current Problem**: Labs reference "authentication modules", "API endpoints", "code review" — excludes non-developers.

**Solution**: Each lab offers THREE domain examples:

```markdown
## Lab: The Context Gap Diagnostic

**Choose your domain:**

**Developer**: Review your codebase's error handling approach
**Content Creator**: Analyze your content calendar strategy
**Business Analyst**: Evaluate your reporting framework

**Protocol** (same for all):

1. Start fresh session, run your complex task
2. Work on unrelated tasks for 20 minutes
3. Run the SAME task again
4. Document the quality delta

**Example outputs by domain:**

| Domain    | Fresh Session          | Accumulated       | Delta                     |
| --------- | ---------------------- | ----------------- | ------------------------- |
| Developer | Found 8 error patterns | Found 4 patterns  | Missed async handling     |
| Creator   | Identified 6 gaps      | Identified 3 gaps | Missed seasonal timing    |
| Analyst   | Noted 5 metrics        | Noted 3 metrics   | Missed regional breakdown |
```

---

## Implementation Plan

### Phase 1: Lesson 1 Rewrite

- Complete rewrite with Greg Foster framing
- Official Anthropic guidance integration
- Domain-neutral lab
- Word count target: 1,200-1,400 words (down from 2,400)

### Phase 2: New Lesson 5 Creation

- Context Architecture lesson
- How tools work as integrated system
- Decision framework with domain-neutral examples
- Word count target: 1,200-1,400 words

### Phase 3: All Lessons Domain-Neutral Update

- Update all labs with 3-domain examples
- Remove code-specific prompts
- Keep concepts unchanged

### Phase 4: Renumber Lessons 6-12

- Update sidebar_position
- Update internal references
- Update quiz question references

---

## Success Criteria

After redesign:

1. **Lesson 1 clearly defines context engineering** in first paragraph
2. **Context Architecture lesson** shows Skills as strategic context tool
3. **All labs work for non-developers** with domain-neutral examples
4. **Official Anthropic guidance** anchors key claims
5. **Word counts reduced** by 30-40% without losing substance
6. **Quiz updated** with new lesson 5 questions

---

## Approval Request

**Options**:

A. **Full Redesign** — Implement all phases (recommended)
B. **Minimal Fix** — Rewrite Lesson 1 only, add Context Architecture lesson
C. **Custom** — Specify which phases to implement

Please confirm which approach to proceed with.
