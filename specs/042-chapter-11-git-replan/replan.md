# Chapter 11: Version Control — Replan

## Review Date: 2026-02-12

## Review Method

4 parallel review agents examined all 8 files in `apps/learn-app/docs/02-Applied-General-Agent-Workflows/11-version-control/`. Reference quality bar: Chapter 3 Lesson 2 (Claude Code installation).

---

## Executive Summary

**Core content is solid. Rendering is broken.** The Git concepts, discovery-based pedagogy, and progression are well-designed. But 4 of 6 lessons have leftover template garbage with unclosed code blocks that break MDX rendering. Students literally cannot read the bottom half of L1, L2, L5, and L6. Combined with HTML entity corruption in L2-L3, inconsistent YAML frontmatter, and ChatGPT branding throughout, the chapter is unusable in its current state.

**Exercises (L7) are excellent** — well-scaffolded, correctly aligned with lessons. **Quiz (L8) content is strong** — 40 scenario-based questions with thorough explanations. These don't need rework.

**Verdict: Fix in place, don't rewrite.** The pedagogical design is good. The problems are mechanical (broken formatting, leftover drafts, metadata gaps). A targeted fix pass is far more efficient than a full rewrite.

---

## Issue Inventory

### Tier 1: CRITICAL — Blocks Student Progress (MDX Rendering Failures)

| #   | Lesson | Issue                                                             | Lines         | Fix                                                                                                  |
| --- | ------ | ----------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------- |
| C1  | L1     | Leftover template garbage in Try With AI section                  | 493-506       | Delete lines 493-506 (orphaned "Expected Outcome" + raw "Prompt 3")                                  |
| C2  | L2     | HTML entity corruption `&lt;&lt;` instead of `<<`                 | 136, 138, 165 | Replace `&lt;&lt;` with `<<` (3 occurrences)                                                         |
| C3  | L2     | Severely broken Try With AI — unclosed code blocks, orphaned text | 503-533       | Delete lines 503-533 (everything after the 4 well-structured prompts)                                |
| C4  | L3     | HTML entity `&lt;&lt;` in explanation                             | 158           | Replace with `<<`                                                                                    |
| C5  | L3     | YAML frontmatter uses FLAT skill format (schema mismatch)         | 5-19          | Rewrite to structured format matching L1-L2                                                          |
| C6  | L5     | Leftover template garbage — unclosed code blocks                  | 384-412       | Delete lines 384-412                                                                                 |
| C7  | L6     | Leftover template garbage — unclosed code blocks                  | 518-556       | Delete lines 518-556                                                                                 |
| C8  | L8     | Quiz missing all YAML frontmatter except title/sidebar_position   | 1-3           | Add full frontmatter: chapter, lesson, duration_minutes, skills, learning_objectives, cognitive_load |

**Estimated effort**: 1-2 hours. Mechanical deletions + find-and-replace.

### Tier 2: MODERATE — Quality/Consistency Issues

| #   | Lesson | Issue                                                                            | Fix                                                                                                                                               |
| --- | ------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| M1  | L1-L5  | "ChatGPT" hardcoded references (L1:2, L2:3, L3:1, L4:1, L5:3)                    | Replace with "your AI assistant" or "[Your AI Tool]"                                                                                              |
| M2  | L2     | Branch name `master` in expected output, but L1 uses `main`                      | Change all `master` to `main` in L2                                                                                                               |
| M3  | L2     | Teaches `git reset HEAD` instead of modern `git restore --staged`                | Teach `git restore --staged` (what Git itself recommends), mention `git reset HEAD` as legacy alternative                                         |
| M4  | L3     | Three Roles framework is VISIBLE — explicit "AI as Teacher" headers              | Remove meta-commentary labels. Keep the interaction patterns, remove the framework names. Per content-quality rule: "Framework must be INVISIBLE" |
| M5  | L3     | Incomplete sentence: "By the end of, you'll have..."                             | Fix to "By the end of this lesson, you'll have..."                                                                                                |
| M6  | L3     | Cognitive load meta-commentary: "5 concepts (within A1 cognitive limits)"        | Remove "within A1 cognitive limits" — internal scaffolding leaked to students                                                                     |
| M7  | L3     | Missing `sidebar_position` in frontmatter                                        | Add `sidebar_position: 3`                                                                                                                         |
| M8  | L3     | Advanced branching strategy diagram overwhelms A1 students                       | Remove or replace with simpler diagram showing just main + 1 feature branch                                                                       |
| M9  | L4     | Missing "Part 2" header — numbering jumps Part 1 to Part 3                       | Add "## Part 2: AI-Guided Setup" header before line 144                                                                                           |
| M10 | L4     | Duplicate Try With AI content at end                                             | Delete lines 474-486 (leftover "Prompt 3: GitHub Best Practices")                                                                                 |
| M11 | L5     | `duration_minutes` stored as string `"50 minutes"` instead of integer            | Change to `duration_minutes: 50`                                                                                                                  |
| M12 | L5     | `cognitive_load` stored as flat string instead of structured block               | Rewrite to structured format: `new_concepts: 4` + `assessment:`                                                                                   |
| M13 | L5     | Missing hands-on merge walkthrough (skill claims "Merge PR" but no activity)     | Add brief Activity showing GitHub merge button click                                                                                              |
| M14 | L6     | Template fence bug — Pattern 2-3 render as lesson text, not copyable template    | Restructure the 4-backtick fencing to properly wrap the entire template                                                                           |
| M15 | L1     | `git config` introduced without context in Activity 4.1                          | Add 1-2 sentences explaining why name/email are needed and that this is one-time setup                                                            |
| M16 | All    | Image paths reference stale `chapter-09` (L1:3 images, L3:3 images, L5:2 images) | Verify images exist at current paths. If renaming, update all 8 references                                                                        |

**Estimated effort**: 3-4 hours. Mix of editing, light rewriting, and one structural fix (L6 template).

### Tier 3: POLISH — Frontmatter Normalization & Teaching Metadata

| #   | Scope | Issue                                                                             | Fix                                                                                                                                                |
| --- | ----- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | L1-L6 | All lessons missing `teaching_guide` block                                        | Add teaching_guide with key_points, misconceptions, discussion_prompts, teaching_tips, assessment_quick_check (use `/enrich-teaching-guide` skill) |
| P2  | L1-L6 | All lessons missing `differentiation` block                                       | Add extension_for_advanced and remedial_for_struggling                                                                                             |
| P3  | L1-L6 | All lessons missing `keywords` array                                              | Add 5-8 SEO keywords per lesson                                                                                                                    |
| P4  | L4    | GitHub PAT instructions may be outdated (classic tokens being phased out)         | Verify current GitHub auth flow, update if needed                                                                                                  |
| P5  | L1    | Git installation section could be expanded (no troubleshooting, no decision tree) | Consider expanding with troubleshooting section like ch3 L2                                                                                        |
| P6  | L6    | Pedagogical jump to Stage 3 "Intelligence Design" may be steep                    | Review scaffolding — the template helps but consider adding more guided examples                                                                   |

**Estimated effort**: 4-6 hours. Mostly frontmatter enrichment (can use `/enrich-teaching-guide` skill for P1).

---

## Lesson-by-Lesson Fix Summary

| Lesson                    | Severity | Action               | Issues                                                                                                                                                                    |
| ------------------------- | -------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **L1**: First Git Repo    | Moderate | Fix in place         | Delete garbage (C1), fix ChatGPT refs (M1), add git config context (M15)                                                                                                  |
| **L2**: Viewing Changes   | Critical | Fix in place         | Fix HTML entities (C2), delete garbage (C3), fix branch names (M2), modernize reset→restore (M3), fix ChatGPT refs (M1)                                                   |
| **L3**: Branches          | Critical | Fix in place         | Rewrite YAML frontmatter (C5), fix HTML entity (C4), remove Three Roles labels (M4), fix incomplete sentence (M5), remove meta-commentary (M6), add sidebar_position (M7) |
| **L4**: Cloud Backup      | Minor    | Fix in place         | Fix ChatGPT ref (M1), add Part 2 header (M9), delete duplicate Try With AI (M10)                                                                                          |
| **L5**: Pull Requests     | Critical | Fix in place         | Delete garbage (C6), fix ChatGPT refs (M1), normalize YAML (M11, M12), add merge walkthrough (M13)                                                                        |
| **L6**: Reusable Patterns | Critical | Fix in place         | Delete garbage (C7), fix template fencing (M14)                                                                                                                           |
| **L7**: Exercises         | Good     | No changes needed    | Exercises are well-designed and aligned                                                                                                                                   |
| **L8**: Quiz              | Moderate | Fix frontmatter only | Add full YAML frontmatter (C8)                                                                                                                                            |

---

## Execution Plan

### Phase 1: Emergency Fixes (Make Chapter Readable)

**Scope**: C1-C8 + M1-M2
**Method**: Direct editing (no subagent needed — these are mechanical fixes)
**Outcome**: Chapter renders correctly in Docusaurus, no broken MDX

Tasks:

1. L1: Delete lines 493-506, replace ChatGPT refs
2. L2: Fix 3x `&lt;&lt;` → `<<`, delete lines 503-533, change `master` → `main`, replace ChatGPT refs
3. L3: Rewrite YAML frontmatter to structured format, fix `&lt;&lt;`, add `sidebar_position: 3`
4. L4: Replace ChatGPT ref, delete lines 474-486
5. L5: Delete lines 384-412, replace ChatGPT refs, fix `duration_minutes` and `cognitive_load` format
6. L6: Delete lines 518-556
7. L8: Add full YAML frontmatter
8. Verify: `pnpm nx build learn-app` succeeds

### Phase 2: Quality Fixes (Make Chapter Professional)

**Scope**: M3-M16
**Method**: Mix of direct editing and content-implementer for larger rewrites
**Outcome**: Consistent quality, invisible frameworks, correct pedagogy

Tasks:

1. L2: Rewrite undo section to teach `git restore --staged` (modern) with `git reset HEAD` as legacy note
2. L3: Remove Three Roles framework labels, remove meta-commentary, fix incomplete sentence, simplify branching diagram
3. L4: Add Part 2 header
4. L5: Normalize YAML, add merge walkthrough activity
5. L6: Fix template fencing structure
6. L1: Add git config explanation
7. All: Verify/update image paths (8 references across L1, L3, L5)

### Phase 3: Frontmatter Enrichment (Make Chapter Complete)

**Scope**: P1-P6
**Method**: Use `/enrich-teaching-guide` skill for P1, direct editing for rest
**Outcome**: Full parity with ch3 L2 quality bar

Tasks:

1. Run `/enrich-teaching-guide` on all 6 content lessons
2. Add `differentiation` blocks to all lessons
3. Add `keywords` arrays to all lessons
4. Verify GitHub PAT instructions are current
5. Consider expanding L1 Git installation section

---

## What NOT To Do

- **Do NOT rewrite lessons from scratch** — the core pedagogy is sound
- **Do NOT restructure the lesson order** — the progression (init → diff/undo → branches → remote → PR → patterns) is correct
- **Do NOT touch exercises (L7)** — they are excellent
- **Do NOT touch quiz content (L8)** — only fix the frontmatter
- **Do NOT add new lessons** — the 6-lesson structure covers Git fundamentals adequately for Part 2's scope

---

## Quality Bar (from Ch3 L2)

Every lesson should have after fixes:

1. Full structured YAML frontmatter (skills as objects, learning_objectives, cognitive_load with new_concepts, differentiation, teaching_guide)
2. Clean Try With AI section with 3-4 structured prompts, each with learning context
3. No tool-specific branding (no "ChatGPT", use "your AI assistant")
4. No leftover template content
5. No HTML entity corruption
6. Invisible pedagogical frameworks (Three Roles used but never named)
7. Consistent branch naming (`main` throughout)
8. Teaching modern Git commands (`git restore --staged` over `git reset HEAD`)
