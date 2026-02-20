# Chapter 12: Meet Your First AI Employee — Replan

## Review Date: 2026-02-13

## Review Method

All 15 lessons + README read directly. Cross-referenced against user-provided research material: Lex Fridman Podcast #491 (Peter Steinberger), YC interview, Matt Wolfe walkthrough, comedy sketch about installation complexity, and comprehensive study guide. CLI verification completed against official OpenClaw docs (see `cli-verification.md`). Reference quality bar: Chapter 3 Lesson 2 (Claude Code installation).

---

## Executive Summary

**The chapter teaches a compelling vision but delivers an unusable experience.** Installation (L2) is fiction. Six lessons (L6-L11) teach email-specific skills when the chapter should teach OpenClaw. L10 teaches a fictional "Gmail MCP" integration that doesn't exist. The user couldn't get past installation.

**Decision: Cut L6-L11. Fix remaining lessons. Produce a focused 10-lesson chapter.**

The 6 deleted email lessons (email-drafter, email-templates, email-summarizer, hiring specialists, granting email access via fictional Gmail MCP, bronze capstone) are replaced with one consolidated skill lesson (new L6) that teaches SKILL.md creation using a non-email domain, then the remaining production lessons (watchers, HITL, deployment) are renumbered.

---

## Phase 0: CLI Verification — COMPLETE

**Deliverable**: `specs/043-chapter-12-openclaw-replan/cli-verification.md`

**Key findings**:

- ~70% of commands correct
- **L10 is entirely fictional** — Gmail uses `gog` (gogcli) + webhooks, NOT MCP
- Three fictional commands: `openclaw mcp auth gmail`, `clawhub install gmail-mcp`, `openclaw config set mcp.gmail.enabled true`
- `openclaw config edit` doesn't exist (use `config get/set/unset` or edit file directly)
- L2 skips `openclaw onboard` (the official recommended wizard)
- L12-L14 are largely accurate

---

## Final Approved Structure (10 Lessons)

| New #  | File Name                             | Title                         | Source               | Action                                                                |
| ------ | ------------------------------------- | ----------------------------- | -------------------- | --------------------------------------------------------------------- |
| L1     | `01-ai-employee-revolution.md`        | The AI Employee Revolution    | Current L1           | Fact-check stats, integrate Lex Fridman quotes                        |
| L2     | `02-setup-your-ai-employee.md`        | Setup Your AI Employee        | Current L2           | **MAJOR REWRITE**: `openclaw onboard`, decision tree, troubleshooting |
| L3     | `03-first-real-work.md`               | Your First Real Work          | Current L3           | Minor edit, add Matt Wolfe "north star" reference                     |
| L4     | `04-how-it-works.md`                  | How Your Employee Works       | Current L4           | Fix `onboard` reference, integrate Steinberger quotes                 |
| L5     | `05-your-employees-memory.md`         | Your Employee's Memory        | Current L5           | No major changes needed                                               |
| L6     | `06-teaching-your-employee-skills.md` | Teaching Your Employee Skills | **NEW**              | Consolidated skill creation + composition + subagents concept         |
| L7     | `07-connecting-real-services.md`      | Connecting Real Services      | Current L12 reframed | Reframe with real `gog` integration, introduce `gog` properly         |
| L8     | `08-trust-but-verify.md`              | Trust But Verify              | Current L13          | Simplify exec-approvals examples, fix `config edit` refs              |
| L9     | `09-always-on-duty.md`                | Always On Duty                | Current L14          | Fix `gog` references (now introduced in L7)                           |
| L10    | `10-chapter-assessment.md`            | Chapter Assessment            | Current L15          | Rewrite quiz for 10-lesson scope, fix broken questions                |
| README | `README.md`                           | Chapter Overview              | Current README       | Update lesson table, fix claims                                       |

### Files to DELETE

| File                                          | Reason                                                             |
| --------------------------------------------- | ------------------------------------------------------------------ |
| `06-teaching-to-write.md` + `.summary.md`     | Email-specific skill (email-drafter) — concepts folded into new L6 |
| `07-professional-formats.md` + `.summary.md`  | Email-specific skill (email-templates) — too narrow                |
| `08-email-intelligence.md` + `.summary.md`    | Email-specific skill (email-summarizer) — too narrow               |
| `09-hiring-specialists.md` + `.summary.md`    | Email subagents — concept folded into new L6                       |
| `10-granting-email-access.md` + `.summary.md` | **FICTIONAL**: Gmail MCP doesn't exist                             |
| `11-bronze-capstone.md` + `.summary.md`       | Email capstone — no longer needed                                  |

### Files to RENAME (after deletion)

| Current File                       | New File                                 |
| ---------------------------------- | ---------------------------------------- |
| `12-employees-senses.md`           | `07-connecting-real-services.md`         |
| `12-employees-senses.summary.md`   | `07-connecting-real-services.summary.md` |
| `13-trust-but-verify.md`           | `08-trust-but-verify.md`                 |
| `13-trust-but-verify.summary.md`   | `08-trust-but-verify.summary.md`         |
| `14-always-on-duty.md`             | `09-always-on-duty.md`                   |
| `14-always-on-duty.summary.md`     | `09-always-on-duty.summary.md`           |
| `15-chapter-assessment.md`         | `10-chapter-assessment.md`               |
| `15-chapter-assessment.summary.md` | `10-chapter-assessment.summary.md`       |

---

## Execution Plan

### Phase 1: File Operations (Delete + Rename + Create)

1. Delete L6-L11 files (12 files: 6 lessons + 6 summaries)
2. Rename L12→L7, L13→L8, L14→L9, L15→L10 (8 files)
3. Create new L6 stub (`06-teaching-your-employee-skills.md`)
4. Update `sidebar_position` in all renamed files
5. Update README lesson table

### Phase 2: Critical Fixes (verified against official docs)

**Every edit in this phase must be verified against official OpenClaw documentation before writing.**

1. **L2: Major rewrite** — installation lesson
   - Replace manual config with `openclaw onboard` wizard
   - Add LLM selection decision tree (Gemini free / Kimi best / Ollama local)
   - Add OS-specific notes (macOS, Linux, Windows/WSL)
   - Replace "5 minutes" with honest "15-30 minutes"
   - Add structured troubleshooting section modeled on Ch3 L2
   - Reference comedy video context

2. **NEW L6: Teaching Your Employee Skills** — consolidated skill lesson
   - Teach SKILL.md format (from current L6's structure)
   - Teach skill composition (from current L7's concept)
   - Introduce subagent concept briefly (from current L9)
   - Use a NON-EMAIL domain example (e.g., research assistant, note-taker)
   - Reference Matt Wolfe's professional skills as "what's possible"

3. **L7 (was L12): Connecting Real Services**
   - Reframe from "Employee's Senses" to "Connecting Real Services"
   - Properly introduce `gog` (gogcli) as the real Gmail integration tool
   - Replace any `openclaw config edit` with correct commands
   - Keep webhook/Pub/Sub content (verified accurate)
   - Add `gog` installation and auth flow

4. **L8 (was L13): Trust But Verify**
   - Replace any `openclaw config edit` references
   - Simplify exec-approvals examples (minimal → recommended → production)

5. **L9 (was L14): Always On Duty**
   - Fix `gog` references (now properly introduced in L7)
   - Keep PM2 + Oracle Cloud content (verified accurate)

6. **L10 (was L15): Chapter Assessment**
   - Rewrite quiz for 10-lesson scope
   - Remove Q10 (gmail-mcp-server — fictional)
   - Remove Q14 (`@invoke` directive — never taught)
   - Add questions about skills, `gog`, and real OpenClaw patterns
   - Update portfolio tiers to match new scope (no email assistant)

### Phase 3: Quality Fixes

1. **L1**: Fact-check stats (60K stars in 72h, 145K+ stars, etc.) via WebSearch
2. **L1**: Integrate 2-3 Lex Fridman podcast quotes for authenticity
3. **L3**: Add Matt Wolfe "north star" showing what professional usage looks like
4. **L4**: Integrate YC interview context about architecture decisions
5. **L4**: Fix `openclaw onboard --install-daemon` reference (consistent with L2 rewrite)
6. **README**: Update lesson table and chapter claims

### Phase 4: Frontmatter Enrichment

1. Add `teaching_guide` to all 10 lessons
2. Verify `keywords`, `differentiation`, `cognitive_load` blocks present
3. Update `sidebar_position` values (1-10)

### Phase 5: Verification

1. `pnpm nx build learn-app` — verify no MDX rendering failures
2. Read-through L2 as a student — can you actually install OpenClaw?
3. Read-through new L6 — does skill creation flow make sense?
4. Verify all cross-references between lessons are consistent
5. Generate summary files for new/rewritten lessons

---

## What NOT To Do

- **Do NOT write lesson prose directly** — use `content-implementer` subagent
- **Do NOT invent CLI commands** — verify against official docs first
- **Do NOT keep email-specific content** — L6-L11 are deleted
- **Do NOT touch L3 or L5 heavily** — they are already good
- **Do NOT add more than 10 lessons** — the structure is locked
- **Do NOT fact-check with AI memory** — use WebSearch only

---

## Quality Bar (from Ch3 L2)

Every lesson should have after fixes:

1. Full structured YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
2. Clean Try With AI section with 3-4 structured prompts, each with learning context
3. Verified CLI commands (checked against official OpenClaw docs)
4. Realistic time estimates
5. Decision trees for complex choices
6. Teaching_guide metadata
7. Invisible pedagogical frameworks (no leaked framework labels)
