# Project Lessons

Patterns learned from corrections. Review at session start.

---

## 2025-11-18 Pedagogical Layer

**Mistake**: Applied L4 (Spec-Driven) thinking to L1 (Manual Foundation) chapter
**Pattern**: Assumed "no code examples" meant "teach specs instead of syntax"
**Rule**: Always check Part number via `ls -d` before assuming student knowledge level

---

## 2025-11-27 Format Drift

**Mistake**: Taught flat skill file format instead of directory structure
**Pattern**: Didn't read canonical source (Chapter 5 Lesson 7) before teaching format
**Rule**: Always read canonical source for any pattern being taught

---

## 2025-12-26 Content Quality (Chapter 2)

**Mistake**: Hallucinated facts, missing YAML frontmatter, weak "Try With AI" sections
**Pattern**: Bypassed subagent orchestration, wrote content directly
**Rule**: NEVER write lesson content directly - always use content-implementer subagent

---

## 2026-01-15 DocPageActions

**Mistake**: Implemented GitHub fetch when Turndown library already existed
**Pattern**: Started coding before researching existing solutions
**Rule**: WebSearch for existing plugins/libraries BEFORE implementing any feature

---

## 2026-02-03 Agent Tool Access

**Mistake**: Assumed agents without `tools:` field had NO tools
**Pattern**: Guessed framework behavior instead of verifying
**Rule**: Omitting `tools:` = ALL tools. Verify framework behavior, don't assume.

---

## 2026-02-03 Skill References

**Mistake**: 7 agents referenced 9 non-existent skills
**Pattern**: Skills were removed but agent references weren't updated
**Rule**: When removing a skill, grep all agents for references: `grep -r "skill-name" .claude/agents/`

---

## 2026-02-04 Live Verification Before Commits (CRITICAL)

**Mistake**: Pushed ChatKit model picker + wrong import path to main without local testing - broke production for 3+ hours
**Pattern**: Made code changes, assumed they would work, committed and pushed without running the actual server
**Rule**: NEVER commit to main branch without live verification:
1. Start the services yourself: `pnpm nx serve study-mode-api`, `pnpm nx serve learn-app`
2. Make a real request through the UI or API
3. Verify the full flow works end-to-end
4. Check logs for errors
5. Only then commit and push

**Especially critical for**:
- Import statements (modules may not exist in all environments)
- API/SDK features (documentation may not match installed version)
- Any changes touching startup/initialization code

**Don't assume user is running services** - start them yourself and test.

---

## 2026-02-05 Redundant File Reading (Usage Report)

**Mistake**: Read conftest.py 6+ times and schemas.py 5+ times in single sessions, wasting tokens and time
**Pattern**: "Let me check that file again to confirm..." instead of trusting initial read
**Rule**: Read each file ONCE per session. Create a mental summary immediately. Reference the summary, never re-read.

**Signs of violation**:
- Reading a file "to double-check"
- Opening a file "to see how it handles X" when you already read it
- Re-reading specs "to make sure I understood"

---

## 2026-02-05 Premature Session Termination (Usage Report)

**Mistake**: 336 of 344 sessions ended "partially_achieved" — work abandoned mid-flight without clear stopping point
**Pattern**: Starting ambitious multi-step work without defining what "done" looks like
**Rule**: Before starting ANY task, state: "This task is DONE when [specific deliverable]. Checkpoints at [milestones]."

**For multi-agent work**:
- Each agent must have clear exit criteria
- Parent agent must verify all child agents completed
- If session ends early, document: "STOPPED AT: [state] | NEXT: [action]"

---

## 2026-02-05 Intent Misinterpretation (Usage Report)

**Mistake**: 309 "misunderstood request" instances — interpreted "model costs" as "remove model restrictions" instead of "tiered pricing per model"
**Pattern**: Interpreting ambiguous terms broadly when user meant something specific
**Rule**: When a term could mean multiple things, STOP and ask: "Do you mean (a) X or (b) Y?"

**Common ambiguities to catch**:
- "model costs" → pricing tiers vs access restrictions
- "fix this" → minimal fix vs refactor
- "improve" → which dimension?
- "chapter X" → chapter X vs part X

**Never interpret broadly when narrow interpretation exists.**

---

## 2026-02-10 Server Hot Reload Issues

**Mistake**: Server errors after code changes due to corrupted hot reload state
**Pattern**: Hot reload can leave server in inconsistent state, especially with async code
**Rule**: When debugging server errors after code changes:
1. Kill all server processes completely: `taskkill /F /IM python.exe`
2. Restart fresh with `PYTHONUNBUFFERED=1` for immediate log output
3. Use `--log-level debug` when debugging
4. Clean restart fixes many "phantom" errors that appear after hot reloads
