---
id: "0002"
title: "linux-mastery-chapter-plan"
stage: "plan"
date: "2026-02-08T01:00:00Z"
surface: "cli"
model: "claude-opus-4-6"
feature: "001-linux-mastery"
branch: "001-linux-mastery"
user: "unknown"
command: "/sp.plan"
labels: ["chapter", "linux", "educational-content", "planning"]
links:
  spec: "../../specs/001-linux-mastery/spec.md"
  plan: "../../specs/001-linux-mastery/plan.md"
  ticket: ""
  adr: ""
  pr: ""
files:
  - path: "specs/001-linux-mastery/plan.md"
    status: "created"
  - path: "specs/001-linux-mastery/spec.md"
    status: "referenced"
tests: []

## Prompt

/sp.plan

User requested creation of implementation plan for Linux Mastery chapter following the specification created in previous session. The specification covered 6 major topics (Terminal, tmux, Shell Scripting, Security, systemd, Networking/Logs) with 30 functional requirements and 10 success criteria.

## Response snapshot

Created comprehensive chapter plan for Linux Mastery for Digital FTEs with 9 lessons organized in pedagogical arc from Foundation to Mastery.

**Key Planning Decisions**:

1. **Chapter Type**: Technical/Code-Focused (hands-on CLI skills)
2. **Lesson Count**: 9 lessons (justified by 12 core concepts across 6 topics at B1-B2 proficiency)
3. **Pedagogical Arc**:
   - Phase 1 (Lessons 1-2): CLI Mindset & Environment - Direct Teaching
   - Phase 2 (Lessons 3-5): Core Agent Operations - Hands-On Discovery + Collaborative Debugging
   - Phase 3 (Lessons 6-7): Process Control & Troubleshooting - Error Analysis
   - Phase 4 (Lessons 8-9): Digital FTE Production - Specification-First

4. **Stage Progression** (4-Layer Framework):
   - Layer 1 (Lessons 1-2): Manual Foundation - No AI, build mental models
   - Layer 2 (Lessons 3-7): AI Collaboration with Three Roles - All three roles explicitly planned
   - Layer 3 (Lesson 8): Intelligence Design - Create reusable skills
   - Layer 4 (Lesson 9): Spec-Driven Integration - Capstone produces Digital FTE

5. **Cognitive Load Validation**: All lessons respect CEFR limits (5-9 concepts per lesson, within B1-B2 limits)

6. **Three Roles Demonstrations**: Every Layer 2 lesson includes explicit AI as Teacher/Student/Co-Worker demonstrations

7. **Intelligence Creation**:
   - Lesson 6: deployment-automation skill
   - Lesson 8: linux-agent-ops skill (major artifact)

8. **Capstone Strategy**: Production FastAPI agent deployment using specification-first methodology

9. **Safety Requirements**: All dangerous operations (sudo, rm -rf, chmod 777, kill -9, SSH) include explicit warnings

10. **Anti-Convergence Achieved**: Multiple teaching modalities (Direct Teaching, Hands-On Discovery, Collaborative Debugging, Error Analysis, Specification-First)

**Learning Objectives Mapped**:
- LO-LINUX-001: Explain CLI architect mindset → Lesson 1
- LO-LINUX-002: Configure Linux dev environment → Lesson 2
- LO-LINUX-003: Create and manage tmux sessions → Lesson 3
- LO-LINUX-004: Write bash scripts for agent automation → Lesson 4
- LO-LINUX-005: Implement least privilege security → Lesson 5
- LO-LINUX-006: Deploy agents as systemd services → Lesson 6
- LO-LINUX-007: Diagnose agent failures → Lesson 7
- LO-LINUX-008: Evaluate Linux command patterns → Lesson 8
- LO-LINUX-009: Design complete deployment workflow → Lesson 9 (Capstone)

**All Success Evals Covered**: SC-001 through SC-010 mapped to specific lessons

## Outcome

- ✅ Impact: Complete chapter plan created with 9 lessons, pedagogical arc, stage progression, and intelligence creation opportunities
- 🧪 Tests: Cognitive load validation passed (all lessons within CEFR limits), Three Roles validation passed (all Layer 2 lessons include explicit demonstrations), dependency validation passed (linear progression satisfied)
- 📁 Files: specs/001-linux-mastery/plan.md (created), specs/001-linux-mastery/spec.md (referenced)
- 🔁 Next prompts: Content implementation phase - invoke content-implementer subagent with plan and reference lesson for each lesson
- 🧠 Reflection: Plan successfully balances technical depth with pedagogical soundness. Chapter-planner subagent effectively applied constitutional principles (4-layer framework, Three Roles, anti-convergence) to create comprehensive learning progression that avoids common patterns like arbitrary lesson counts and skipped stages.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning completed successfully on first attempt
- Graders run and results (PASS/FAIL):
  - Cognitive load validation: PASS (all lessons within CEFR limits)
  - Three Roles validation: PASS (all Layer 2 lessons include explicit AI as Teacher/Student/Co-Worker demonstrations)
  - Dependency validation: PASS (linear progression with no circular dependencies)
  - Stage progression validation: PASS (1→2→3→4 without skipping, spec-first only in Layer 4)
  - Anti-convergence validation: PASS (multiple teaching modalities, not just direct teaching)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Consider creating more detailed lesson-level task breakdown before content implementation to parallelize lesson creation across multiple content-implementer subagents
