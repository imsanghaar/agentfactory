# Chapter Exercise Factory — Master Checklist

The end-to-end playbook for adding exercises to any chapter. Follows the Ch3 pattern: separate GitHub repo, ZIP releases, dedicated exercise lesson.

**References:**

- Exercise folder standard: `exercise-standard.md`
- Lesson template: `lesson-template.md`
- GitHub setup: `github-setup.md`
- Review rubric: `review-rubric.md`

---

## Phase 1: Chapter Analysis

Before creating anything, understand what exercises the chapter needs.

- [ ] **Identify the chapter** — Run `ls -d apps/learn-app/docs/*/NN-*/` to confirm path
- [ ] **Read the chapter README** — Understand lesson structure, part number, pedagogical layer
- [ ] **Count existing lessons** — Know the current L01-LNN numbering
- [ ] **Determine exercise type** — Task-oriented (basics-style) or Skill-building (skills-style)?

| If the chapter teaches...                                    | Exercise type               | Module naming                  |
| ------------------------------------------------------------ | --------------------------- | ------------------------------ |
| Tool usage, problem decomposition, prompt engineering        | Task-oriented               | `module-N/` (bare)             |
| SKILL.md creation, agent customization, workflow composition | Skill-building              | `module-N-slug/` (descriptive) |
| Both (mixed chapter)                                         | Split into 2 exercise packs | One of each                    |

- [ ] **Define 8 modules** — Each with a title and 3 exercises + module 8 as capstones
- [ ] **Determine placement** — Where in the lesson order does the exercise lesson go?
  - Place basics exercises after the last "foundations" lesson students need
  - Place skills exercises after the last lesson that teaches the exercised concept
- [ ] **Check for inline exercises** — Do any existing lessons have exercise/lab sections to extract?

### Output: Exercise Plan

```
Chapter: [N] [Name]
Path: apps/learn-app/docs/[part]/[chapter]/
Exercise type: [Task-oriented | Skill-building]
Repo name: claude-code-[topic]-exercises
ZIP name: [topic]-exercises
Lesson position: L[NN]
Modules: [list of 8 module titles]
Lessons with inline exercises to remove: [list or "none"]
```

---

## Phase 2: Create Exercise Content

Use `exercise-standard.md` as the reference for all formatting.

### 2A: Repository Structure

- [ ] Create the folder structure locally:
  ```
  claude-code-[topic]-exercises/
  ├── .github/workflows/release.yml
  ├── EXERCISE-GUIDE.md
  ├── README.md
  ├── module-1[-slug]/
  │   ├── exercise-1.1-slug/
  │   ├── exercise-1.2-slug/
  │   └── exercise-1.3-slug/
  ├── module-2[-slug]/ ... module-7[-slug]/
  └── module-8[-slug]/
      ├── capstone-A-slug/
      ├── capstone-B-slug/
      └── capstone-C-slug/
  ```
- [ ] Verify: 8 modules, 3 items per module, 27 total

### 2B: Create Exercises (per exercise)

For each of the 27 exercises, use the single exercise checklist from `exercise-standard.md` §10:

- [ ] Create folder: `module-N/exercise-N.N-slug/`
- [ ] Write `INSTRUCTIONS.md` using the appropriate template (task-oriented or skill-building)
- [ ] Add starter files (realistic data, not placeholders)
- [ ] Verify all file paths in INSTRUCTIONS.md are relative to the exercise folder
- [ ] Verify exercise is completable in 15-45 min (capstones: 2-4 hrs)

### 2C: Create EXERCISE-GUIDE.md

- [ ] Write using the template from `exercise-standard.md` §6
- [ ] Include: How This Guide Works, all 8 modules with exercise descriptions, Assessment Rubric, Framework
- [ ] Verify every exercise is listed with: title, problem, task, learning points

### 2D: Create README.md

- [ ] Write using the template from `exercise-standard.md` §7 or `github-setup.md` §4
- [ ] Include: package structure tree, getting started (Cowork + Claude Code), recommended order

---

## Phase 3: GitHub Repo Setup

Use `github-setup.md` as the reference for all steps.

- [ ] Create repo: `panaversity/claude-code-[topic]-exercises` (public, main branch)
- [ ] Add `.github/workflows/release.yml` with correct ZIP name
- [ ] Push all content to main
- [ ] **Verify**: Actions tab shows green check
- [ ] **Verify**: Releases tab shows `latest` release with ZIP attached
- [ ] **Verify**: Download URL works in unauthenticated browser:
  ```
  https://github.com/panaversity/claude-code-[topic]-exercises/releases/latest/download/[topic]-exercises.zip
  ```
- [ ] **Verify**: ZIP extracts correctly, contains all exercise folders, excludes `.github/` and `.git/`
- [ ] **Verify**: ZIP size is reasonable (<500KB text-only, <5MB with images)

---

## Phase 4: Create Exercise Lesson

Use `lesson-template.md` as the reference for all formatting.

- [ ] Create lesson file: `NN-[topic]-exercises.md` with correct `sidebar_position`
- [ ] Write full YAML frontmatter (all fields per template)
- [ ] Write opening narrative (2-3 paragraphs)
- [ ] Add download section (`:::info` block with ZIP link + fallback)
- [ ] Write "How to Use These Exercises" section
- [ ] Write Tool Guide
- [ ] Write Framework section (chapter-appropriate 5-7 step framework)
- [ ] Write Assessment Rubric (5-6 criteria × 4 levels)
- [ ] Write walkthroughs for all 27 exercises:
  - Each has: The Problem, Your Task, What You'll Learn (3 bullets)
  - Early modules: include Starter Prompt + Better Prompt
  - Later modules: fewer/no prompts (students design their own)
  - Each has: Reflection Questions (3 questions)
  - Optional: The Twist, The Extension, The Challenge (0-1 per exercise)
- [ ] Write capstone section (3 capstones, no starter prompts)
- [ ] Write "What's Next" section pointing to next lesson(s)
- [ ] Create `.summary.md` companion file (3 paragraphs, no headings)
- [ ] **Verify**: Lesson references match actual exercise folder names in the repo

---

## Phase 5: Modify Existing Lessons (if applicable)

If any existing lessons had inline exercises that are now consolidated:

### 5A: Remove Inline Exercises

For each lesson with an exercise section to remove:

- [ ] Identify the section start line (e.g., "Problem Solving Lab", "Practice Lab")
- [ ] Replace the entire exercise section with a pointer paragraph:
  ```markdown
  :::tip Ready to Practice?
  Head to **Lesson NN: [Exercise Lesson Title]** for N hands-on exercises
  with complete walkthroughs. [Value proposition sentence.]
  :::
  ```
- [ ] Verify no exercise content remains in the modified lesson
- [ ] Verify the pointer lesson number is correct

### 5B: Renumber Lessons (if inserting new lesson)

When inserting an exercise lesson into an existing sequence:

- [ ] List all lessons that need renumbering (current position → new position)
- [ ] For each affected lesson file:
  - [ ] Rename file: `NN-slug.md` → `MM-slug.md`
  - [ ] Update `sidebar_position:` in YAML frontmatter
  - [ ] Update `lesson:` number in YAML frontmatter (if present)
- [ ] For each affected `.summary.md` file:
  - [ ] Rename to match new lesson number
  - [ ] Update any internal lesson references

### 5C: Update Cross-References

- [ ] Grep all chapter lesson files for old lesson numbers:
  ```
  grep -rn "Lesson [0-9]" apps/learn-app/docs/[part]/[chapter]/
  ```
- [ ] Update every reference to use new numbering
- [ ] Check "What's Next" sections in adjacent lessons
- [ ] Check lesson body text for "in Lesson N" references
- [ ] Check `.summary.md` files for lesson references
- [ ] Update chapter `README.md` with new lesson list

---

## Phase 6: Quality Review

Use `review-rubric.md` for the full 69-check rubric. At minimum, verify these critical items:

### Blocking Checks (must pass to ship)

- [ ] Download URL returns HTTP 200 and downloads correct ZIP
- [ ] ZIP extracts without errors, contains all 27 exercise folders
- [ ] Every exercise folder has INSTRUCTIONS.md
- [ ] Lesson file has complete YAML frontmatter
- [ ] Download link in lesson matches actual GitHub release URL
- [ ] All lesson walkthroughs reference exercise folders that exist in the ZIP
- [ ] No old/stale lesson numbers in cross-references
- [ ] `sidebar_position` values are sequential with no gaps or duplicates

### Quality Checks (should pass)

- [ ] Spot-check 3+ INSTRUCTIONS.md files — clear, completable, realistic data
- [ ] Spot-check 3+ lesson walkthroughs — match exercise files exactly
- [ ] Exercise difficulty progresses across modules (1-2 easy, 3-5 medium, 6-7 hard, 8 capstone)
- [ ] Framework section is appropriate for the chapter's domain
- [ ] Rubric criteria map to the chapter's core skills

### Full Review (recommended)

- [ ] Run full 69-check rubric from `review-rubric.md`
- [ ] Gate decision: Ship / Fix-and-Ship / Revise / Rework

---

## Phase 7: Commit and Deploy

- [ ] Create feature branch: `feat/[chapter]-exercises`
- [ ] Stage all changed files (new lesson, modified lessons, renamed files, README)
- [ ] Verify no secrets in diff
- [ ] Commit with descriptive message:
  ```
  feat: add [topic] exercises for Chapter N with ZIP downloads
  ```
- [ ] Create PR with summary of:
  - New exercise repo created
  - New exercise lesson added at position LNN
  - Lessons modified (inline exercises removed, pointers added)
  - Lessons renumbered (if applicable)
  - Cross-references updated

---

## Quick Reference: Agent Assignments

When running this with the exercise-factory team:

| Phase            | Primary Agent      | What They Do                                        |
| ---------------- | ------------------ | --------------------------------------------------- |
| 1. Analysis      | team-lead          | Chapter analysis, exercise plan                     |
| 2. Exercises     | exercise-generator | Create repo content, INSTRUCTIONS.md, starter files |
| 3. GitHub        | github-reviewer    | Repo creation, workflow, release verification       |
| 4. Lesson        | lesson-writer      | Exercise lesson .md + .summary.md                   |
| 5. Modifications | lesson-writer      | Pointer paragraphs, renumbering                     |
| 6. Review        | github-reviewer    | Run review rubric, verify cross-references          |
| 7. Commit        | team-lead          | PR creation, final sign-off                         |

---

## Appendix: File Inventory Per Chapter

For each chapter that gets exercises, these files are created or modified:

### New Files

- `NN-[topic]-exercises.md` — Exercise lesson
- `NN-[topic]-exercises.summary.md` — Summary companion

### New GitHub Repo

- `panaversity/claude-code-[topic]-exercises/` — All exercise folders + workflow

### Modified Files

- `README.md` — Updated lesson list
- `NN-*.md` (0-4 files) — Inline exercises removed, pointers added
- `NN-*.md` + `NN-*.summary.md` (0-17 files) — Renumbered if lessons inserted
