---
id: 0001
title: metadata-driven-slides-spec
stage: spec
date: 2025-11-23T20:00:00Z
surface: claude-code
model: claude-sonnet-4-5-20250929
feature: 035-metadata-driven-slides
branch: 035-metadata-driven-slides
user: mjs
command: /sp.specify
labels: [spec, infrastructure, docusaurus, remark, metadata]
links:
  spec: specs/035-metadata-driven-slides/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: specs/035-metadata-driven-slides/spec.md
    status: created
  - path: specs/035-metadata-driven-slides/checklists/requirements.md
    status: created
tests:
  - type: spec-architect-validation
    result: READY
    score: 9/10
---

## Prompt

**User Request**: "Yes you steps 1, 2, 3 makes sense so let's use full speckitplus loop for this implementation define the business requirements using /sp.specify then we move to technical details in /sp.plan and finally tasks then implementation"

**Context from Phase 0 Constitutional Reasoning**:
- Task Type: Infrastructure (Docusaurus build-time architecture)
- Complexity: Moderate (remark plugins known, integration custom)
- Stakes: Production (affects 84 chapters, recoverable)
- Cloud Migration: 2-3 days (URL support immediate, not future-proofing)
- Composability Requirement: System must handle both local paths AND URLs transparently (no migration needed)

**Key Clarifications Resolved**:
1. Cloud storage timeline: 2-3 days → Full URL support is immediate priority
2. Migration approach: Composable system → NO migration needed, both formats work

**Constitutional Frameworks Applied**:
- Principle 1 (Specification Primacy): Define WHAT (metadata rendering) before HOW (plugin implementation)
- Principle 5 (Intelligence Accumulation): Reuse existing PDFViewer component and Docusaurus patterns
- Principle 7 (Minimal Content): Only essential features (no over-engineering)

**Task from /sp.loopflow**:
Create specification for metadata-driven slides architecture that:
- Decouples content (frontmatter) from presentation (remark plugin)
- Supports both local paths and cloud URLs composably
- Enables centralized maintenance across 84 chapters
- Maintains backward compatibility with existing JSX approach

## Response snapshot

Created comprehensive specification with:

**User Stories** (4 prioritized, independently testable):
- P1: Content creator adds slides via frontmatter (zero markdown changes)
- P1: Content creator uses cloud URL instead of local path (composable, immediate requirement)
- P2: Developer maintains slides across 84 chapters from single location
- P3: Build system validates slide references with graceful degradation

**Functional Requirements** (11 total, all falsifiable):
- FR-001: Parse slides metadata from YAML frontmatter
- FR-002: Detect local path vs URL (http/https prefix detection)
- FR-003: Inject PDFViewer automatically after "What You'll Learn"
- FR-004: Resolve local paths relative to static directory
- FR-005: Use URLs as-is in PDFViewer src
- FR-006: NO imports/JSX required in markdown
- FR-007: Maintain backward compatibility (dual-support)
- FR-008: Reuse existing PDFViewer component
- FR-009: Support chapters without slides (no errors)
- FR-010: Log warnings for invalid references (don't fail build)
- FR-011: Work with Docusaurus/remark pipeline

**Success Criteria** (6 measurable, technology-agnostic):
- SC-001: Zero markdown content changes needed
- SC-002: Local paths and URLs work transparently
- SC-003: Global updates via plugin/component only
- SC-004: All 84 chapters build successfully
- SC-005: No performance degradation
- SC-006: Graceful degradation (warnings, not failures)

**Scope Boundaries**:
- 5 Constraints (no breaking changes, no new component, no build deps, no manual updates, no build failures)
- 7 Non-Goals (no new PDF component, no slide generation, no management UI, no analytics, no automated migration)
- 5 Edge Cases (dual JSX/metadata, malformed URLs, missing sections, path normalization, future object format)

**Validation by spec-architect**:
- Overall Readiness: 9/10 (READY FOR PLANNING)
- Testability: 10/10 (all requirements falsifiable)
- Completeness: 9/10 (minor: performance budget could be more specific)
- Ambiguity: 9/10 (minor: injection logic edge case could be more precise)
- Traceability: 8/10 (could add constitution principle mapping)

## Outcome

- ✅ Impact: Specification created with ZERO [NEEDS CLARIFICATION] markers (all ambiguities resolved in Phase 0)
- 🧪 Tests: spec-architect validation PASSED (9/10), all quality checklist items passed
- 📁 Files: specs/035-metadata-driven-slides/spec.md (150 lines), checklists/requirements.md (generated)
- 🔁 Next prompts: /sp.plan (architectural strategy), /sp.tasks (implementation breakdown)
- 🧠 Reflection: Constitutional reasoning in Phase 0 eliminated need for iterative clarifications. User's composability insight ("why migrate at all?") shaped architecture decisively.

## Evaluation notes (flywheel)

- Failure modes observed: None - spec passed validation on first iteration
- Graders run and results (PASS/FAIL): spec-architect READY (9/10)
- Prompt variant (if applicable): Used /sp.loopflow v2.0 constitutional reasoning pattern
- Next experiment (smallest change to try): Apply Phase 0 reasoning framework to more feature types to validate universal applicability
