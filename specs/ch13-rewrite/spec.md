# Chapter 13 Update Specification

## Summary

**Update** Chapter 13, not rewrite. The existing Bronze tier (L01-L07) is practical, hands-on content that teaches email skills, subagents, MCP, and orchestration. The problem is:

1. **Silver/Gold tiers are empty** — L08-L12 are placeholder stubs
2. **Some tech references are outdated** — Obsidian MCP syntax, PM2 commands
3. **No hackathon assignment** — Hackathon 0 doc exists but isn't connected to the chapter
4. **Assessment is empty** — L13 quiz says "Coming Soon"
5. **L14 is conceptual only** — no hands-on exercise
6. **Missing summary files** — L00, L01, L08-L12 have no `.summary.md`

## Archive

Current Ch13 content backed up at `specs/ch13-rewrite/archive/` (23 files). Original content preserved in git history.

## CRITICAL CONSTRAINT: Implementable & Tested

**Every NEW lesson must produce something the student can actually run and verify.**

For each new lesson, the content must include:

1. **Concrete commands students type** — not "set up a watcher" but the actual code/commands
2. **Expected output** — what students should see after each step
3. **Verification step** — "run this command and you should see X"
4. **Failure recovery** — what to do when it doesn't work

**Test-it-or-cut-it rule**: If a feature can't be demonstrated working, move it to Hackathon assignment.

## What's Changing

### KEEP AS-IS (existing Bronze tier — practical, works)

| Lesson | Title                              | Status                                                     |
| ------ | ---------------------------------- | ---------------------------------------------------------- |
| L00    | Personal AI Employee Specification | **Keep** — good architectural reference                    |
| L01    | Your Employee's Memory             | **Keep** — vault setup, CLAUDE.md, AGENTS.md, Obsidian MCP |
| L02    | Teaching Your Employee to Write    | **Keep** — email-drafter skill, hands-on                   |
| L03    | Teaching Professional Formats      | **Keep** — email-templates skill, practical                |
| L04    | Teaching Email Intelligence        | **Keep** — email-summarizer, DAQ pattern                   |
| L05    | Hiring Specialists                 | **Keep** — subagents, decision framework                   |
| L06    | Granting Email Access              | **Keep** — Gmail MCP, OAuth, draft-first safety            |
| L07    | Bronze Capstone                    | **Keep** — master skill orchestrating everything           |

### UPDATE (fix outdated tech in existing lessons)

| Lesson | What to Update                                                                                                                                      |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| L00    | Fix chapter number mismatch (says "Chapter 10" in YAML). Update tier table to include Hackathon tier. Link to Hackathon 0 doc.                      |
| L01    | Verify Obsidian MCP install command still works. Add troubleshooting section. Add vault security guidance (.env placement).                         |
| L06    | Verify Gmail MCP auth steps match current Google Cloud Console UI. Add rate limit warning. Clarify "known contacts" definition in draft-first rule. |

### WRITE NEW (complete Silver/Gold + Hackathon)

| Lesson | Title                              | Source Material                                                           |
| ------ | ---------------------------------- | ------------------------------------------------------------------------- |
| L08    | Your Employee's Senses             | Distill Hackathon 0 BaseWatcher pattern. Currently placeholder.           |
| L09    | Trust But Verify                   | Distill Hackathon 0 HITL approval workflow. Currently placeholder.        |
| L10    | Always On Duty                     | Distill Hackathon 0 PM2/cron/Ralph Wiggum. Currently placeholder.         |
| L11    | Silver Capstone: CEO Briefing      | Distill Hackathon 0 Business Handover. Currently placeholder.             |
| L12    | Gold Capstone: Autonomous Employee | Distill Hackathon 0 invoice flow + error recovery. Currently placeholder. |
| L13    | Chapter Assessment                 | Write actual quiz (currently "Coming Soon").                              |
| L14    | Hackathon 0 Assignment             | **Replace** current conceptual L14 with Hackathon 0 assignment.           |

### CUT

Nothing. All existing lessons preserved.

## Lesson Specs for NEW Content

### L08: Your Employee's Senses (Watchers)

**Duration**: 30 min | **Type**: Hands-on building
**Currently**: Placeholder with YAML frontmatter only

**What students DO**:

1. Understand why employees need to wake up (reactive vs proactive)
2. Learn the Watcher pattern from Hackathon 0 (poll-based, event-based, scheduled)
3. Write a Python filesystem watcher (~30 lines) using `watchdog` library:
   - Monitors a drop folder (e.g., `~/employee-inbox/`)
   - When file appears → creates `.md` action file in `/Needs_Action/` with metadata frontmatter
   - Runs as background process
4. Test: save a file to drop folder → verify action file appears in vault → verify employee processes it
5. Show Gmail watcher architecture (from Hackathon 0) — assign as hackathon deliverable, not in-lesson

**Deliverable**: Working filesystem watcher that automatically triggers the employee when files arrive.

**Source**: Hackathon 0 Section 2A (BaseWatcher, GmailWatcher, FilesystemWatcher patterns)

---

### L09: Trust But Verify (HITL)

**Duration**: 30 min | **Type**: Hands-on building
**Currently**: Placeholder with YAML frontmatter only

**What students DO**:

1. Add sensitivity classification to the orchestrator (from L07):
   - Safe actions (read, analyze, summarize) → auto-execute
   - Sensitive actions (send email, delete file, external API) → require approval
2. Build file-based approval workflow:
   - Employee writes approval request to `/Pending_Approval/` (YAML frontmatter: action, target, reason, expiry)
   - Human reviews → moves to `/Approved/` or `/Rejected/`
   - Employee watches `/Approved/` → executes → logs → moves to `/Done/`
3. Write permission boundaries into `AGENTS.md` (from Hackathon 0 permission table)
4. Test full cycle: trigger sensitive action → verify pause → approve → verify execution → check log
5. Test rejection: trigger → reject → verify employee logs rejection and does NOT execute

**Deliverable**: Working HITL approval gate. Employee never takes sensitive actions without human approval.

**Source**: Hackathon 0 Section 2C (HITL pattern, permission boundaries), Hackathon 0 Section 6.4 (Permission Boundaries table)

---

### L10: Always On Duty

**Duration**: 30 min | **Type**: Hands-on building
**Currently**: Placeholder with YAML frontmatter only

**What students DO**:

1. Install PM2: `npm install -g pm2`
2. Run watcher (from L08) under PM2:
   - `pm2 start watcher.py --interpreter python3`
   - `pm2 save && pm2 startup`
3. Test crash recovery: `kill -9 <pid>` → verify PM2 restarts watcher → verify no files lost
4. Set up a cron job for scheduled tasks:
   - `crontab -e` → add daily vault audit skill at 8am
   - Verify it fires at next scheduled time
5. Learn Ralph Wiggum loop (from Hackathon 0):
   - Stop hook keeps Claude iterating until task file moves to `/Done/`
   - Max iterations prevent infinite loops
   - Test: start a multi-step task → verify loop continues → verify it stops on completion
6. Implement graceful degradation: if a component is down, queue work instead of crashing

**Deliverable**: Employee runs 24/7. Survives crashes, reboots. Scheduled tasks execute on time.

**Source**: Hackathon 0 Section 2D (Ralph Wiggum), Section 3 (Continuous vs Scheduled), developer note on process management

---

### L11: Silver Capstone — CEO Briefing

**Duration**: 35 min | **Type**: Integration + verification
**Currently**: Placeholder with YAML frontmatter only

**What students DO**:

1. Create `Business_Goals.md` in vault using Hackathon 0 template (revenue targets, key metrics, subscription audit rules)
2. Populate vault with 1 week of sample data:
   - 5 processed email tasks in `/Done/`
   - 5 log entries in `/Logs/`
   - Sample transaction data
3. Write a `ceo-briefing` skill that:
   - Reads `Business_Goals.md` + `/Done/` + `/Logs/`
   - Generates Monday Morning CEO Briefing (revenue, bottlenecks, proactive suggestions)
   - Writes to `/Briefings/YYYY-MM-DD_Monday_Briefing.md`
   - Commits to git
4. Set up cron trigger (Sunday night from L10)
5. Run manually → verify briefing content is accurate → verify git commit
6. Review: does the briefing match the Hackathon 0 CEO Briefing template?

**Deliverable**: Working CEO Briefing skill. Student can demo: "every Monday my employee generates a business report."

**Source**: Hackathon 0 Section 4 (Business Handover), Business_Goals.md template, CEO Briefing template

---

### L12: Gold Capstone — Autonomous Employee

**Duration**: 35 min | **Type**: Integration + verification
**Currently**: Placeholder with YAML frontmatter only

**What students DO**:

1. Wire everything end-to-end:
   - Gmail watcher (or filesystem watcher simulating email) → creates `/Needs_Action/` file
   - Orchestrator classifies → delegates to appropriate skill
   - If response needed → drafts via Gmail MCP → HITL approval → sends
   - Logs everything → updates Dashboard → commits to git
2. Run the invoice flow (from Hackathon 0):
   - Simulate: client message requesting invoice arrives
   - Employee detects → identifies request → drafts email with details → HITL approval → sends → logs → updates Dashboard
3. Test error recovery:
   - Simulate network timeout → verify employee retries with backoff
   - Simulate auth failure → verify employee pauses and writes alert to vault
4. Review audit log: verify every action has timestamp, actor, target, result
5. Draw full architecture diagram of running system

**Deliverable**: Full autonomous employee. Student demos complete pipeline: trigger → classify → act → approve → execute → log.

**Source**: Hackathon 0 End-to-End Invoice Flow, Section 7 (Error States & Recovery)

---

### L13: Chapter Assessment

**Duration**: 20 min | **Type**: Assessment
**Currently**: "Coming Soon" placeholder

**What students DO**:

1. Complete 20-question quiz covering:
   - Skills architecture (SKILL.md structure, three-level loading)
   - Subagent patterns (when skill vs subagent, single-line description rule)
   - MCP integration (Gmail tools, draft-first safety, credential management)
   - Orchestration (master skill delegation, error handling)
   - Watchers (BaseWatcher pattern, poll vs event vs scheduled)
   - HITL (approval workflow, permission boundaries)
   - Production (PM2, cron, Ralph Wiggum, graceful degradation)
   - CEO Briefing (data sources, output format)
2. Self-evaluation rubric by tier

**Deliverable**: Completed assessment.

---

### L14: Hackathon 0 Assignment (REPLACES current L14)

**Duration**: 15 min | **Type**: Assignment
**Currently**: Conceptual "When Your Employee Codes" (no hands-on)

**What students DO**:

1. Read the full Hackathon 0 specification
2. Choose their tier:
   - **Bronze** (8-12h): Vault + one watcher + basic skills
   - **Silver** (20-30h): Multiple watchers + LinkedIn posting + scheduling
   - **Gold** (40h+): Odoo integration + social media + CEO Briefing
   - **Platinum** (60h+): Cloud deployment + local/cloud work-zone specialization
3. Set up hackathon repo (GitHub)
4. Write initial plan as `PLAN.md` in repo
5. Submit tier declaration

**Deliverable**: Hackathon repo initialized with tier choice and plan.

**Source**: Full Hackathon 0 document (tier specs, judging criteria, submission requirements, resources)

## Implementation Plan

### Phase 1: Fix Existing (L00, L01, L06)

1. Update L00 YAML (fix chapter number), add Hackathon tier to table, add link to Hackathon 0 doc
2. Verify L01 Obsidian MCP commands work with current version, add troubleshooting
3. Verify L06 Gmail MCP auth steps, add rate limit warning

### Phase 2: Write Silver Tier (L08-L11)

4. Write L08: Watchers — distill Hackathon 0 BaseWatcher into hands-on lesson
5. Write L09: HITL — distill Hackathon 0 approval workflow
6. Write L10: Always On Duty — distill PM2/cron/Ralph Wiggum
7. Write L11: CEO Briefing capstone — distill Business Handover

### Phase 3: Write Gold + Assignment (L12-L14)

8. Write L12: Gold Capstone — end-to-end autonomous employee
9. Write L13: Assessment — actual 20-question quiz
10. Write L14: Hackathon 0 Assignment (replaces current conceptual L14)

### Phase 4: Quality

11. Generate missing summary files (L00, L01, L08-L14)
12. Verify all new lesson commands actually work
13. Validate YAML frontmatter on new lessons

## Success Criteria

1. **L01-L07 unchanged** — existing Bronze tier preserved (only tech fixes)
2. **L08-L11 complete** — Silver tier fully written with working content
3. **L12 complete** — Gold capstone with end-to-end demo
4. **L13 complete** — actual quiz (not "Coming Soon")
5. **L14 complete** — Hackathon 0 assignment replaces conceptual lesson
6. **Every new lesson** has concrete commands, expected output, and verification steps
7. **All commands verified** against current tool versions (Feb 2026)
8. **Summary files** exist for all lessons
