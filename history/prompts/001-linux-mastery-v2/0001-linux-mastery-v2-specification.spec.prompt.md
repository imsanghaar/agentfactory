---
id: "0001"
title: "Linux Mastery v2 Specification"
stage: spec
date: 2026-02-08
surface: claude-code
model: claude-opus-4-6
feature: 001-linux-mastery-v2
branch: 001-linux-mastery-v2
user: user
command: /sp.specify
labels: [linux, chapter-rewrite, v2, spec]
links:
  spec: specs/001-linux-mastery-v2/spec.md
  ticket: ""
  adr: ""
  pr: ""
files:
  - specs/001-linux-mastery-v2/spec.md
  - specs/001-linux-mastery-v2/checklists/requirements.md
tests:
  - spec-architect validation (sonnet): PASS after fixes
---

## Prompt

User invoked `/sp.specify` with the full Chapter 10 Linux Mastery analysis report (21 identified issues across 4 priority tiers). Request: create v2 specification addressing all identified issues. Explicitly instructed to ignore chapter numbering conflicts and focus on content quality improvements. Input included complete analysis covering structural issues, missing topics, pedagogical weaknesses, factual errors, quiz bugs, and redundancies.

## Response snapshot

Created comprehensive v2 specification (specs/001-linux-mastery-v2/spec.md) restructuring chapter from 9 to 13 lessons + quiz. Key changes: 4 new lessons (File Operations, Text Editing & Pipes, Networking & SSH), 2 lesson splits (old L4 and L8), Three Roles Framework made invisible with grep validation criteria, all factual errors corrected, prerequisites fixed (no forward references), sample agent file spec'd. Spec validated by spec-architect agent which found 3 counterexamples (L05 layer conflict, FR precision gaps, cross-cutting FR mapping). All issues resolved: L05 moved to L2, FR-006/016/017/018/021 made precise with validation commands, cross-cutting requirements added (FR-CC1, FR-CC2).

## Outcome

- Impact: Complete v2 specification ready for planning phase; addresses all 21 identified issues
- Tests: spec-architect validation PASS (improved from 7.5/10 to ~9/10 after fixes)
- Files: 2 files created (spec.md, checklists/requirements.md)
- Next prompts: `/sp.plan` to create implementation plan, then content-implementer for lessons
- Reflection: Spec-architect caught a genuine layer/CEFR contradiction that would have caused confusion during implementation. Worth the validation pass.

## Evaluation notes (flywheel)

- Failure modes observed: Initial spec had L05 in L1 with B2 proficiency (contradiction); FRs used vague terms ("meta-commentary", "interactive exercises") that needed precision
- Graders run and results (PASS/FAIL): spec-architect PASS (after fixes)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Consider adding Success Eval → User Story explicit mapping table in future specs
