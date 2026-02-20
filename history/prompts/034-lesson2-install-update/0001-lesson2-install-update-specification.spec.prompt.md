---
id: 0001
title: lesson2-install-update-specification
stage: spec
date: 2025-12-06
surface: terminal
model: claude-sonnet-4-5
feature: 034-lesson2-install-update
branch: 034-lesson2-install-update
user: orchestrator
command: /sp.specify
labels: [content-update, lesson-revision, installation-methods, platform-specific, B1-proficiency]
links:
  spec: specs/034-lesson2-install-update/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/034-lesson2-install-update/spec.md
  - specs/034-lesson2-install-update/checklists/requirements.md
tests: []
---

## Prompt

User request via /sp.orchestrator:
"Our chapter 5 lesson 2 @book-source\docs\02-AI-Tool-Landscape\05-claude-code-features-and-workflows\02-installation-and-authentication.md has claude code installation. Now the claude code has updated its installation methods which have become more simplified and now the user can install without npm. We have to update our lesson 2 and its summary as per new installation method. Here is the link of official claude code installation https://code.claude.com/docs/en/setup. Follow this link and update lesson 2 and its summary using SDD-RI."

User clarification (Phase 0):
"The user can have windows, linux, macos or windows on wsl. For recommended, it should be platform specific rather than recommended among all platforms like windows, linux, macos."

Task: Create specification for updating Chapter 5 Lesson 2 with new simplified Claude Code installation methods, organized by platform with platform-specific recommendations.

Context:
- Feature number: 034 (auto-calculated from existing branches/specs)
- Feature slug: lesson2-install-update
- Source of truth: https://code.claude.com/docs/en/setup
- Pedagogical context: B1 proficiency, Layer 1 (Manual Foundation), Part 2 (AI Tool Landscape)
- Current issue: npm-centric approach outdated, no platform-specific guidance, cognitive load violation

## Response snapshot

**Specification Created**: `specs/034-lesson2-install-update/spec.md`

**Key Design Decisions**:

1. **Platform-Specific Organization**: Restructure installation section by platform (Windows, macOS, Linux/WSL) instead of global 4-method presentation. Reduces cognitive load from "6+ global options" to "2-4 platform-specific options."

2. **Recommended Method Per Platform**:
   - Windows: PowerShell (primary), curl/bash (Git Bash), CMD, npm
   - macOS: Homebrew (primary), curl/bash, npm
   - Linux/WSL: curl/bash (primary), npm
   - Rationale: Aligns with platform conventions (Homebrew for macOS devs, PowerShell for Windows 10+)

3. **Authentication Expansion**: Updated from 2 to 3 authentication paths (Console API, Claude.ai Pro/Max, Enterprise) with decision criteria for each.

4. **Pedagogical Preservation**: Maintains B1 cognitive load limits (≤10 concepts per section), Layer 1 foundation approach, existing "Why This Matters" and "Try With AI" sections.

5. **Factual Accuracy Priority**: All 18 functional requirements trace to official documentation (https://code.claude.com/docs/en/setup). Acceptance Test 4 requires factual-verifier validation.

6. **Summary File Update**: FR-014 requires summary file rewrite to match main lesson (prevents student confusion from outdated summary).

**User Stories Prioritized**:
- P1: Windows/macOS/Linux installation (3 stories) + Authentication (1 story) = 4 critical paths
- P2: npm alternative (1 story) + Summary update (1 story) = 2 supporting paths

**Success Criteria Highlights**:
- 90% installation success rate on first attempt (SC-002)
- 10-minute setup time (SC-004, down from 15+)
- 60% support request reduction (SC-003)
- 100% factual accuracy (SC-007)

**Validation Results** (spec-architect):
- Readiness: ✅ READY (9.5/10)
- Testability: 10/10 (8 quantitative metrics, 5 acceptance tests)
- Completeness: 10/10 (18 FRs, 6 user stories, 6 edge cases, 10 assumptions)
- Formal verification: PASS (5 invariants hold, no counterexamples in 3-platform small scope test)
- Issues: 0 critical, 0 major, 1 minor (missing chapter-index citation - non-blocking)

**Checklist Generated**: `specs/034-lesson2-install-update/checklists/requirements.md` (43/44 criteria passed, 97.7%)

## Outcome

- ✅ Impact: Specification complete and validated, ready for planning phase
- 🧪 Tests: 5 acceptance tests defined (platform installation, auth selection, summary standalone, factual accuracy, cognitive load)
- 📁 Files: spec.md (330 lines), requirements.md checklist
- 🔁 Next prompts: /sp.plan 034-lesson2-install-update
- 🧠 Reflection: Platform-specific recommendations resolve user feedback and reduce cognitive load. Formal verification confirmed no coverage gaps.

## Evaluation notes (flywheel)

- Failure modes observed: None - user clarification in Phase 0 prevented generic "recommended method" ambiguity
- Graders run and results (PASS/FAIL): spec-architect validation PASS (9.5/10)
- Prompt variant (if applicable): Standard /sp.specify with user clarification loop
- Next experiment (smallest change to try): Apply factual-verifier during planning to catch command inaccuracies before implementation
