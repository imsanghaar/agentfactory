# PHR: Chapter 6 File Organization Workflow Specification

**ID**: 0001
**Stage**: spec
**Feature**: 062-ch6-file-workflow
**Date**: 2025-01-27
**Title**: Chapter 6 File Organization Workflow Specification

---

## Prompt Text

```text
/sp.specify Create comprehensive specs for chapter 06 as described in @part2-plan.md. The chapter shall implement the General Agent workflows using our 7 principles @seven_principles_chapter.md. The reader shall be able to implement the workflows using general agent claude code and will actually implement its daily use cases. These workflows shall actually create the value the reader gets from this chapter.
```

---

## Context

User requested a complete redesign of Chapter 6 from a "teaching-only" chapter to a proper "workflow" chapter where students BUILD real, reusable outputs. The plan document specified:
- Replace passive observation with active execution
- Students work on their OWN files (Downloads folder)
- Create tangible deliverables: organize.sh script, rules.md, ORGANIZER-LOG.md
- Apply all 7 principles through execution, not lecture
- No paid subscriptions required

---

## Response Summary

Created comprehensive specification at `specs/062-ch6-file-workflow/spec.md` with:

1. **6 User Stories (P1-P3 prioritized)**:
   - P1: Survey Digital Chaos (baseline inventory)
   - P1: Safety First Backup (P6 compliance)
   - P2: Categorize with Rules (P5 state persistence)
   - P2: Build Organizer Script (P1, P2 automation)
   - P3: Run with Verification (P3 validation)
   - P3: Capstone Clean Machine (all principles)

2. **34 Functional Requirements (FR-001 to FR-034)** mapped to lessons

3. **18 Success Criteria** - measurable, technology-agnostic

4. **Key Entities**:
   - file-organizer/ workspace
   - organize.sh reusable script
   - rules.md categorization rules
   - ORGANIZER-LOG.md activity history
   - backup/ safety directory
   - organized/ output directory

5. **Formal Verification** passed:
   - Backup-before-move invariant holds
   - State persistence across lessons verified
   - All 7 principles covered
   - No counterexamples found

---

## Artifacts Created

- `specs/062-ch6-file-workflow/spec.md` - Full specification (751 lines)
- `specs/062-ch6-file-workflow/checklists/requirements.md` - Validation report

---

## Next Steps

1. Review specification
2. Run `/sp.clarify` if questions arise
3. Run `/sp.plan` to create implementation plan
4. Test bash commands on Windows/macOS/Linux

---

## Tags

`spec` `chapter-6` `file-organization` `workflow` `part-2` `seven-principles`
