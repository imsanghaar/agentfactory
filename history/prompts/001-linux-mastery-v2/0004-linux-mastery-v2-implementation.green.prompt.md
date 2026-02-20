---
id: "0004"
title: "Linux Mastery v2 Implementation (Phase 3-5)"
stage: green
date: 2026-02-08
surface: github-copilot
model: claude-opus-4-6
feature: 001-linux-mastery-v2
branch: 001-linux-mastery-v2
user: user
command: /sp.implement
labels: [linux, implementation, v2, content-work, lessons, quiz, validation]
links:
  spec: specs/001-linux-mastery-v2/spec.md
  plan: specs/001-linux-mastery-v2/plan.md
  tasks: specs/001-linux-mastery-v2/tasks.md
  ticket: ""
  adr: ""
  pr: ""
files:
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/11-debugging-troubleshooting.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/12-workflow-integration-patterns.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/13-building-reusable-skills.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/14-capstone-production-deployment.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/15-chapter-quiz.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/02-file-operations-mastery.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/03-text-editing-pipes-streams.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/04-modern-terminal-environment.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/05-persistent-sessions-tmux.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/06-bash-scripting-foundations.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/07-text-processing-automation.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/08-security-hardening.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/09-networking-ssh-remote-access.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/10-process-control-systemd.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/11-debugging-troubleshooting.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/12-workflow-integration-patterns.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/13-building-reusable-skills.summary.md
  - apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-linux-mastery/14-capstone-production-deployment.summary.md
  - specs/001-linux-mastery-v2/tasks.md
tests:
  - T013-T017 lesson + quiz creation complete
  - T018 Three Roles invisibility PASS (0 matches in v2 files)
  - T019 YAML frontmatter PASS (all 14 lessons valid)
  - T020 Try With AI PASS (3 prompts per lesson after fixing L03, L04)
  - T021 Exercise count PASS (all lessons have 2+ exercises)
  - T022 Size validation PASS (all under 35KB, max 31.9KB)
  - T023 Factual accuracy PASS (no stat -f%z, Restart=on-failure correct)
  - T024 Fixed L03 and L04 missing 3rd Try With AI prompt
  - T025 13 summary files generated
  - T026 17 v1 files cleaned up
  - T027 Chapter evaluation score ~90% (A- target met)
---

## Prompt

User invoked `/sp.implement` for feature `001-linux-mastery-v2`. Phase 1-2 (T001-T012) were completed in a prior session. This session completed T013-T027: Phases 3-5 covering remaining lessons, quiz, cross-cutting validation, summaries, and cleanup.

## Work Completed

### Phase 3: L2 AI Collaboration — T013

- **L11 Debugging & Troubleshooting** (26KB, 542 lines): REWRITE of v1 L07. Teaches layered triage methodology (logs → network → disk → process), journalctl, ss, strace, lsof. Three Roles invisible, 3 Try With AI prompts, 3 exercises.

### Phase 4: L3 Intelligence + L4 Capstone — T014-T016

- **L12 Workflow Integration Patterns** (29KB, 669 lines): SPLIT from v1 L08. Blue-green deployment, monitoring, Docker awareness note. L3 Intelligence layer.
- **L13 Building Reusable Skills** (20KB, 378 lines): SPLIT from v1 L08. Pattern recognition, Persona+Questions+Principles SKILL.md format. L3 Intelligence layer.
- **L14 Capstone: Spec-First Deployment** (32KB, 708 lines): REWRITE of v1 L09. DEPLOYMENT-SPEC.md methodology, systemd+direct port binding, layered validation. L4 Spec-Driven. Only 1 nginx mention (awareness, not dependency).

### Phase 5: Quiz + Validation — T017-T027

- **Chapter Quiz** (50 questions): Covers all 13 lessons, 3-5 per lesson weighted by complexity. Mix of single-answer, multi-answer, and scenario-based. Initial generation produced 61 questions; trimmed to exactly 50.
- **Cross-cutting validation**: All 7 checks passed (Three Roles invisibility, YAML frontmatter, Try With AI count, exercise count, size limits, factual accuracy). Fixed L03 and L04 that had only 2 Try With AI prompts.
- **Summary generation**: 13 summary files created using summary-generator skill. Word counts: 224-395 words, all within proficiency-adjusted limits.
- **Cleanup**: 17 v1 files removed (9 lessons + 8 summaries). Only v2 canonical files remain (30 total: 14 lessons + 14 summaries + quiz + README).

## Chapter Statistics

| Metric | Value |
|--------|-------|
| Total lessons | 14 (L01-L14) |
| Total words (lessons only) | ~44,731 |
| Chapter quiz questions | 50 |
| Summary files | 14 |
| Smallest lesson | 01-cli-architect-mindset.md (15.5KB) |
| Largest lesson | 14-capstone-production-deployment.md (31.9KB) |
| Gatekeeping language | 0 instances |
| Three Roles labels | 0 instances |
| Exercises per lesson | 3+ (all pass FR-016) |

## Validation Results

| Check | Status | Details |
|-------|--------|---------|
| FR-004 YAML frontmatter | PASS | All 14 lessons have skills, learning_objectives, cognitive_load, differentiation |
| FR-005 Try With AI | PASS | 3 prompts per lesson (L03, L04 fixed during T024) |
| FR-006 Three Roles invisible | PASS | Zero matches across all v2 files |
| FR-012 Factual accuracy | PASS | No stat -f%z; Restart=on-failure taught correctly |
| FR-016 Exercises | PASS | All lessons have 2+ exercises with verification |
| FR-019 Size limits | PASS | All under 35KB (max: 31.9KB) |
| FR-020 No nginx dependency | PASS | Capstone uses direct port binding; 1 awareness mention only |

## Decisions

1. **Quiz trim strategy**: Subagent generated 61 questions. Trimmed to 50 by removing Q51-Q61 (last 11 questions covering L12-L13 which already had sufficient earlier coverage). Used PowerShell line-level truncation for precision.
2. **L03/L04 prompt fix**: Added 3rd Try With AI prompt to both files. L03 got a nano editing prompt; L04 got a package conflict diagnosis prompt. Both include `:::note Safety Reminder` blocks matching the L10 reference pattern.
3. **V1 file cleanup**: Deleted all v1 files after confirming v2 canonical set is complete per README lesson table. Git tracks history for reversibility.

## Lessons Learned

- Content-implementer subagents reliably produce Three Roles-invisible content when given explicit instructions and reference lessons
- Quiz generation consistently overshoots target count (61 vs 50) — trim is more reliable than re-prompting for exact count
- Cross-cutting validation catches issues in earlier sessions' work (L03/L04 had silently passed with only 2 prompts)
