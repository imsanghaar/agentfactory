# Feature Specification: Consolidated Exercise Lessons

**Feature Branch**: `041-consolidated-exercises`
**Created**: 2026-02-08
**Status**: Draft
**Input**: Consolidate exercises scattered across 4 lessons into 2 dedicated exercise lessons with one-click ZIP downloads

---

## Problem Statement

Chapter 3 (General Agents, folder `03-general-agents`) has exercises scattered across 4 lessons (L04, L07, L08, L09), each pointing students to a single GitHub repo (`claude-code-exercises`) with clone/download instructions. This creates three problems:

1. **Access friction**: Students must navigate GitHub, find the "Code" button, choose "Download ZIP", then locate the right subfolder. Layer 1 learners (A1 proficiency) find this unnecessarily complex.
2. **Context fragmentation**: Exercise instructions are split across lesson prose and external INSTRUCTIONS.md files. Only 1 of the 48 total exercises receives a walkthrough in the lesson text. Students are left to figure out the other 47 on their own.
3. **Maintenance coupling**: A single monorepo (`claude-code-exercises`) bundles basics and skills exercises together. Students download content they do not need yet, and repo changes affect all lessons simultaneously.

## Solution

Split the existing `claude-code-exercises/` directory into two independent GitHub repos, each with automated ZIP release via GitHub Actions. Create two dedicated exercise lessons with complete walkthroughs for every exercise, embedded in the chapter at pedagogically appropriate positions.

---

## Assumed Knowledge

### Before Basics Exercises Lesson (new L09, inserted after current L08 agent-skills)

Students have completed:

| Lesson | Topic                         | Key Capabilities Gained                                             |
| ------ | ----------------------------- | ------------------------------------------------------------------- |
| L01    | Origin Story                  | Understanding of general agents concept                             |
| L02    | Installation & Authentication | Claude Code installed, API key configured                           |
| L03    | Free Claude Setup             | Alternative backend configuration (OpenRouter/Gemini/DeepSeek)      |
| L04    | Hello World Basics            | CLI interface, slash commands, approval workflow, file creation     |
| L05    | CLAUDE.md Context Files       | Persistent project context, eliminating repetitive instructions     |
| L06    | Teach Claude Your Way         | Custom instructions, behavioral alignment                           |
| L07    | Concept Behind Skills         | Skills architecture, three-level loading, expertise gap             |
| L08    | Agent Skills                  | Creating SKILL.md files, YAML frontmatter, skill-creator meta-skill |

**Students CAN**: Open Claude Code, have conversations, create files, write CLAUDE.md files, create and test skills.
**Students CANNOT yet**: Use subagents, understand delegation/orchestration, use MCP servers.

### Before Skills Exercises Lesson (new L11, inserted after L10 which is current L09 subagents)

Students have additionally completed:

| Lesson        | Topic                       | Key Capabilities Gained                                                   |
| ------------- | --------------------------- | ------------------------------------------------------------------------- |
| L10 (was L09) | Subagents and Orchestration | Built-in subagents (Explore, Plan), parallel invocation, custom subagents |

**Students CAN**: Everything above plus delegate to subagents and compose multi-agent workflows.

---

## Content Structure

### Lesson Placement and Renumbering

**Current lesson order (L01-L26)**:

```
L01  origin-story
L02  installation-and-authentication
L03  free-claude-setup
L04  hello-world-basics              ← has "Problem Solving Lab" (lines 167+)
L05  claude-md-context-files
L06  teach-claude-your-way
L07  concept-behind-skills           ← has "Practice Lab: Understanding Skills" (lines 400+)
L08  agent-skills                    ← has "Practice Lab: Building Skills" (lines 388+)
L09  subagents-and-orchestration     ← has "Practice Lab: Composing Skills" (lines 361+)
L10  mcp-integration
...
L26  chapter-quiz
```

**New lesson order (L01-L28)**:

```
L01  origin-story                           (unchanged)
L02  installation-and-authentication        (unchanged)
L03  free-claude-setup                      (unchanged)
L04  hello-world-basics                     (MODIFIED: exercise section removed, pointer added)
L05  claude-md-context-files                (unchanged)
L06  teach-claude-your-way                  (unchanged)
L07  concept-behind-skills                  (MODIFIED: exercise section removed, pointer added)
L08  agent-skills                           (MODIFIED: exercise section removed, pointer added)
L09  basics-exercises                       (NEW: consolidated basics exercises lesson)
L10  subagents-and-orchestration            (RENUMBERED from 09, MODIFIED: exercise section removed, pointer added)
L11  skills-exercises                       (NEW: consolidated skills exercises lesson)
L12  mcp-integration                        (RENUMBERED from 10)
...
L28  chapter-quiz                           (RENUMBERED from 26)
```

### New Lesson Format

Each new exercise lesson follows this structure:

1. **YAML frontmatter** (full metadata per content quality requirements)
2. **Opening narrative** (2-3 paragraphs connecting to student journey)
3. **Download section** (one-click ZIP link + unzip instructions)
4. **Problem-Solving Framework** (reproduced from EXERCISE-GUIDE.md)
5. **Assessment Rubric** (reproduced from EXERCISE-GUIDE.md)
6. **Module walkthroughs** (8 modules per lesson, 3 exercises each + 3 capstones)
7. **Capstone projects** (extended, open-ended challenges)

### Exercise Walkthrough Format

Each of the 24 exercises (per lesson) follows this pattern:

```markdown
### Exercise X.Y — Title 🖥️🗂️

**The Problem:**
[Setup description — what the student finds in the exercise folder]

**Your Task:**
[What to ask Claude to do]

**What You'll Learn:**

- [Learning outcome 1]
- [Learning outcome 2]
- [Learning outcome 3]

**Starter Prompt (Intentionally Vague):**

> "[Simple prompt]"

**Better Prompt (Build Toward This):**
[Guidance on what makes a better specification]

**Reflection Questions:**

1. [Question prompting metacognition]
2. [Question about specification quality]
```

Capstone projects use an extended format with more open-ended guidance and no starter prompts.

---

## User Scenarios & Testing

### User Story 1 — Student Downloads and Starts Basics Exercises (Priority: P1)

A Layer 1 student reaches the new L09 (basics exercises) after completing the skills lesson (L08). They want to practice what they have learned with hands-on exercises. They click the ZIP download link, unzip the file, and begin working through Module 1 exercises with complete lesson guidance.

**Why this priority**: This is the core value proposition. If students cannot download exercises and follow along, the entire feature fails.

**Independent Test**: Can be fully tested by opening L09 in the learn-app, clicking the download link, verifying the ZIP downloads, unzipping, and confirming exercise files match the walkthrough descriptions.

**Acceptance Scenarios**:

1. **Given** a student reading L09 on the learn-app, **When** they click the ZIP download link, **Then** a file named `basics-exercises.zip` downloads immediately (no GitHub navigation required).
2. **Given** a downloaded and unzipped `basics-exercises.zip`, **When** the student opens `module-1-file-organization/exercise-1.1-messy-downloads/`, **Then** they find an `INSTRUCTIONS.md` file and a `messy-downloads/` folder with 30+ files matching the lesson description.
3. **Given** a student reading the Exercise 1.1 walkthrough in L09, **When** they follow the instructions (open folder in terminal, run `claude`, point Claude at INSTRUCTIONS.md), **Then** Claude reads the instructions and begins organizing the files.
4. **Given** the lesson content, **When** a student reads any exercise walkthrough (1.1 through 8.C), **Then** the walkthrough describes the exact files and folders present in the corresponding ZIP subfolder.

---

### User Story 2 — Student Downloads and Starts Skills Exercises (Priority: P1)

A student reaches the new L11 (skills exercises) after completing L10 (subagents and orchestration). They download the skills exercises ZIP and begin working through Module 1, which focuses on understanding existing skills before building new ones.

**Why this priority**: Equal priority to User Story 1 — the skills exercises are the second half of the consolidation and require the same one-click experience.

**Independent Test**: Can be tested identically to User Story 1 but with `skills-exercises.zip` and skills-specific content.

**Acceptance Scenarios**:

1. **Given** a student reading L11 on the learn-app, **When** they click the ZIP download link, **Then** a file named `skills-exercises.zip` downloads immediately.
2. **Given** a downloaded and unzipped `skills-exercises.zip`, **When** the student opens `module-1-understanding-skills/exercise-1.1-anatomy/`, **Then** they find an `INSTRUCTIONS.md` file and `sample-skills/` folder with 3 sample SKILL.md files matching the lesson description.
3. **Given** the lesson content for L11, **When** a student reads any skills exercise walkthrough, **Then** the walkthrough matches the exact file structure in the corresponding ZIP subfolder.

---

### User Story 3 — Exercise Updates Propagate via GitHub Releases (Priority: P2)

A course maintainer pushes a fix to an exercise file (correcting a typo in `INSTRUCTIONS.md` or adding a new test file). The GitHub Action automatically rebuilds the ZIP and updates the release. Students who download after the fix get the corrected version without any lesson text changes.

**Why this priority**: Important for long-term maintenance but not required for initial launch. Students using existing downloads are unaffected.

**Independent Test**: Push a commit to main branch of the basics repo, verify GitHub Action creates new release with updated ZIP within 5 minutes.

**Acceptance Scenarios**:

1. **Given** a push to main branch of `panaversity/claude-code-basics-exercises`, **When** the GitHub Action runs, **Then** a new GitHub Release is created (or updated) with a ZIP artifact named `basics-exercises.zip`.
2. **Given** the release exists, **When** a user visits `https://github.com/panaversity/claude-code-basics-exercises/releases/latest/download/basics-exercises.zip`, **Then** the ZIP downloads without requiring GitHub authentication or navigation.
3. **Given** the GitHub Action workflow file, **When** the action triggers, **Then** it completes in under 2 minutes for a repo of this size (~50MB).

---

### User Story 4 — Existing Lessons Point to Consolidated Exercises (Priority: P2)

A student reading L04 (hello-world-basics) reaches the end and sees a brief note directing them to the dedicated exercises lesson (L09) instead of inline exercise content. The note is concise (2-3 sentences) and does not break the lesson flow.

**Why this priority**: Required for coherence but is a minor edit to existing lessons, not new content creation.

**Independent Test**: Read L04, L07, L08, L10 and verify each has a pointer paragraph and no remaining exercise sections.

**Acceptance Scenarios**:

1. **Given** L04 (hello-world-basics) after modification, **When** a student reads the lesson, **Then** the "Problem Solving Lab" section (currently starting at line 167) is replaced with a 2-3 sentence pointer to L09.
2. **Given** L07 (concept-behind-skills) after modification, **When** a student reads the lesson, **Then** the "Practice Lab: Understanding Skills" section (currently starting at line 400) is replaced with a pointer to L11.
3. **Given** L08 (agent-skills) after modification, **When** a student reads the lesson, **Then** the "Practice Lab: Building Skills" section (currently starting at line 388) is replaced with a pointer to L11.
4. **Given** L10 (was L09, subagents-and-orchestration) after modification, **When** a student reads the lesson, **Then** the "Practice Lab: Composing Skills" section (currently starting at line 361) is replaced with a pointer to L11.

---

### User Story 5 — Cross-References Updated After Renumbering (Priority: P3)

After inserting 2 new lessons, all existing cross-references between lessons in Chapter 3 correctly reflect the new numbering. A student reading any lesson that mentions another lesson by number sees the correct (renumbered) reference.

**Why this priority**: Important for correctness but lower risk since most lesson references use names rather than numbers.

**Independent Test**: Grep all Chapter 3 lesson files for patterns like "Lesson N", "L0N", "lesson N" and verify each reference points to the correct renumbered lesson.

**Acceptance Scenarios**:

1. **Given** all Chapter 3 lesson files after renumbering, **When** searching for cross-references to other lessons, **Then** every reference matches the new lesson numbering scheme.
2. **Given** the chapter README.md, **When** reviewing the lesson list, **Then** all lesson numbers, titles, and descriptions reflect the new 28-lesson structure.
3. **Given** `sidebar_position` values in YAML frontmatter, **When** the learn-app renders the chapter sidebar, **Then** lessons appear in correct sequential order (L01-L28) with new exercise lessons at positions 9 and 11.

---

### Edge Cases

- **ZIP download link is broken**: If GitHub Release does not exist yet (repo just created, Action has not run), the download link returns 404. The lesson text MUST include a fallback instruction: "If the link does not work, visit the repository page and click Releases."
- **Student has old monorepo clone**: Students who previously cloned `claude-code-exercises` may be confused by references to new repos. The new lessons MUST NOT reference the old monorepo. The old repo README should be updated with a deprecation notice pointing to the two new repos.
- **ZIP filename collision**: If a student downloads both ZIPs to the same folder, the filenames (`basics-exercises.zip`, `skills-exercises.zip`) are distinct and will not overwrite each other.
- **Large ZIP size**: The basics exercises contain SVG files and sample data. The ZIP must remain under 20MB to ensure fast downloads on slow connections. If the current `claude-code-exercises/basics/` exceeds this, large binary files should be excluded or compressed.
- **Lesson renumbering breaks Docusaurus routing**: Docusaurus uses `sidebar_position` from frontmatter, not folder names. Renumbering requires updating both the filename prefix (e.g., `09-` to `10-`) AND the `sidebar_position` value in each affected file's frontmatter.
- **Cross-references in .summary.md files**: Each lesson has a corresponding `.summary.md` file. These may also contain lesson number references that need updating.

---

## Requirements

### Functional Requirements — New Repositories

- **FR-001**: Two new GitHub repositories MUST be created under the `panaversity` organization: `claude-code-basics-exercises` and `claude-code-skills-exercises`.
- **FR-002**: `claude-code-basics-exercises` MUST contain the contents of the current `claude-code-exercises/basics/` directory, including all 8 modules, 24 exercises, 3 capstone projects, and the `EXERCISE-GUIDE.md`.
- **FR-003**: `claude-code-skills-exercises` MUST contain the contents of the current `claude-code-exercises/skills/` directory, including all 8 modules, 24 exercises, 3 capstone projects, and the `EXERCISE-GUIDE.md`.
- **FR-004**: Each repository MUST have a `README.md` explaining the exercise pack, its relationship to the book chapter, and basic usage instructions.
- **FR-005**: Each repository MUST NOT contain the other pack's exercises (no cross-contamination).

### Functional Requirements — GitHub Actions

- **FR-006**: Each repository MUST have a GitHub Actions workflow triggered on push to `main` branch.
- **FR-007**: The workflow MUST create a GitHub Release (or update the `latest` release) containing a ZIP of the repository contents.
- **FR-008**: The ZIP artifact MUST be named `basics-exercises.zip` (for basics repo) or `skills-exercises.zip` (for skills repo).
- **FR-009**: The ZIP MUST be downloadable at a stable URL: `https://github.com/panaversity/{repo-name}/releases/latest/download/{zip-name}.zip`.
- **FR-010**: The workflow MUST exclude `.github/` directory and any CI-only files from the ZIP artifact.
- **FR-011**: The workflow MUST complete in under 5 minutes for repos under 100MB.

### Functional Requirements — New Lessons

- **FR-012**: A new lesson file MUST be created at `09-basics-exercises.md` with `sidebar_position: 9` in YAML frontmatter.
- **FR-013**: A new lesson file MUST be created at `11-skills-exercises.md` with `sidebar_position: 11` in YAML frontmatter.
- **FR-014**: Each new lesson MUST include full YAML frontmatter per content quality requirements: title, description, keywords, chapter, lesson, duration_minutes, pedagogical layer metadata, skills metadata (with proficiency_level, category, bloom_level, digcomp_area, measurable_at_this_level), learning_objectives, cognitive_load, and differentiation.
- **FR-015**: Each new lesson MUST begin with a one-click ZIP download link formatted as a prominent callout/admonition block (Docusaurus `:::info` syntax).
- **FR-016**: Each new lesson MUST include the Problem-Solving Framework (7-step cycle from EXERCISE-GUIDE.md: Define, Gather, Write, Execute, Verify, Iterate, Reflect).
- **FR-017**: Each new lesson MUST include the Assessment Rubric (5-criteria table from EXERCISE-GUIDE.md: Problem Clarity, Specification Quality, Output Verification, Iteration, Reflection).
- **FR-018**: The basics exercises lesson MUST provide a walkthrough for all 24 exercises plus 3 capstone projects across 8 modules: (1) File Organization & Digital Housekeeping, (2) Research & Information Synthesis, (3) Data Wrangling & Analysis, (4) Document Creation & Transformation, (5) Process Automation & Workflows, (6) Problem Solving & Creative Thinking, (7) Quality Control & Critical Thinking, (8) Capstone Projects.
- **FR-019**: The skills exercises lesson MUST provide a walkthrough for all 24 exercises plus 3 capstone projects across 8 modules: (1) Understanding Skills, (2) First Skills, (3) Skills with Examples, (4) Skills with References, (5) Testing and Iteration, (6) Composing Skills, (7) Real-World Skills, (8) Capstone Projects.
- **FR-020**: Each exercise walkthrough MUST include at minimum: exercise title with tool indicators, "The Problem" section, "Your Task" section, and "What You'll Learn" section.
- **FR-021**: Each exercise walkthrough SHOULD include (where pedagogically valuable): starter prompts, better prompts, reflection questions, and twists/extensions.
- **FR-022**: Each new lesson MUST include a corresponding `.summary.md` file for the static summary tab.

### Functional Requirements — Modified Existing Lessons

- **FR-023**: L04 (`04-hello-world-basics.md`) MUST have the "Problem Solving Lab" section (line 167 onward) replaced with a pointer paragraph directing students to the basics exercises lesson (L09).
- **FR-024**: L07 (`07-concept-behind-skills.md`) MUST have the "Practice Lab: Understanding Skills" section (line 400 onward) replaced with a pointer paragraph directing students to the skills exercises lesson (L11).
- **FR-025**: L08 (`08-agent-skills.md`) MUST have the "Practice Lab: Building Skills" section (line 388 onward) replaced with a pointer paragraph directing students to the skills exercises lesson (L11).
- **FR-026**: L09 (`09-subagents-and-orchestration.md`) MUST have the "Practice Lab: Composing Skills" section (line 361 onward) replaced with a pointer paragraph directing students to the skills exercises lesson (L11). This file MUST also be renamed to `10-subagents-and-orchestration.md` with `sidebar_position: 10`.
- **FR-027**: Each pointer paragraph MUST follow this pattern: a brief motivational sentence ("Ready to practice?"), the lesson reference ("Head to Lesson N: [Title]"), and a one-line value proposition ("You'll work through N hands-on exercises with complete walkthroughs.").
- **FR-028**: No exercise content from the removed sections MAY remain in the modified lessons (clean removal, not duplication).

### Functional Requirements — Lesson Renumbering

- **FR-029**: All lessons from current L10 through L26 MUST be renumbered to L12 through L28 by updating both the filename prefix and `sidebar_position` frontmatter value.
- **FR-030**: Current L09 (subagents-and-orchestration) MUST be renumbered to L10 (filename `10-subagents-and-orchestration.md`, `sidebar_position: 10`).
- **FR-031**: All cross-references between Chapter 3 lessons MUST be updated to reflect new numbering. This includes references in lesson body text, `.summary.md` files, and the chapter `README.md`.
- **FR-032**: The chapter `README.md` MUST be updated to list all 28 lessons with correct numbers and descriptions, including the two new exercise lessons.

### Functional Requirements — Old Repository

- **FR-033**: The existing `claude-code-exercises/` directory in the monorepo MUST be retained during the transition period but MUST NOT be referenced by any lesson content after this feature ships.
- **FR-034**: [NEEDS CLARIFICATION: Should the `claude-code-exercises/` directory be deleted from the monorepo after the two new repos are created and verified, or retained indefinitely as an archive? Retaining avoids git history loss; deleting avoids confusion.]

### Key Entities

- **Exercise Pack**: A ZIP archive containing all modules and exercises for one track (basics or skills). Attributes: name, download URL, module count, exercise count, total file size.
- **Exercise Module**: A thematic grouping of 3 exercises within a pack. Attributes: number (1-8), title, core skill description, exercise list.
- **Exercise**: A single hands-on activity with starter files and instructions. Attributes: module number, exercise number, title, tool indicators (Claude Code and/or Cowork), INSTRUCTIONS.md, supporting files/folders.
- **Walkthrough**: The lesson-embedded description of an exercise. Attributes: exercise reference, problem description, task description, learning outcomes, optional prompts/reflections.
- **Lesson Pointer**: A brief paragraph in a modified lesson directing students to a consolidated exercise lesson. Attributes: source lesson, target lesson number, motivational text.

---

## Non-Goals (Explicit Scope Boundaries)

- **NOT building a custom download server or CDN** — GitHub Releases handles hosting. No R2, S3, or custom infrastructure.
- **NOT creating new exercises** — All 48 exercises (24 basics + 24 skills) and 6 capstones already exist in `claude-code-exercises/`. This feature consolidates and documents them, it does not create new ones.
- **NOT modifying exercise content** — The INSTRUCTIONS.md files and supporting data files remain unchanged. Only lesson prose (walkthroughs) is new.
- **NOT adding auto-grading or progress tracking** — Exercises are self-assessed using the rubric. No platform integration for completion tracking.
- **NOT changing exercises in other chapters** — Only Chapter 3 exercises are in scope. Other chapters are unaffected.
- **NOT creating a Docusaurus plugin for ZIP downloads** — Standard markdown links to GitHub Releases URLs are sufficient.
- **NOT versioning exercise packs** — The `latest` release is always current. No version pinning or changelogs for exercise content.

---

## Constraints

- **Content format**: Lessons MUST use Docusaurus-compatible MDX with full YAML frontmatter matching the format in `content-quality-requirements.md`.
- **Pedagogical layer**: Both new lessons are Layer 1 (Manual Foundation) — students practice independently with the exercises, no AI collaboration pedagogy required (exercises themselves teach AI collaboration).
- **Lesson length**: Each exercise lesson will be long (estimated 3,000-5,000 words covering 27 activities). This is acceptable because students are not expected to read linearly — they pick exercises and skip around. The lesson functions as a reference/workbook, not a narrative.
- **No code in lessons**: Exercise walkthroughs describe what to do in natural language. They do not include programming code (the exercises themselves may generate code via Claude, but the lesson text does not).
- **Download link stability**: The GitHub Releases URL pattern (`/releases/latest/download/{filename}`) is stable and has been used by major projects for years. No URL shortener or redirect service needed.
- **File size limit**: Each ZIP MUST be under 20MB. Current `claude-code-exercises/basics/` and `skills/` should be audited for size before repo creation.
- **GitHub Action simplicity**: The workflow should be under 30 lines of YAML. Use `actions/checkout`, `zip` command, and `softprops/action-gh-release` (or equivalent). No custom actions.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Both ZIP download links return HTTP 200 and download the correct ZIP file when accessed from an unauthenticated browser session.
- **SC-002**: Each ZIP file, when unzipped, contains exactly 8 module directories, each with 3 exercise subdirectories (plus 3 capstone entries in Module 8), and each exercise subdirectory contains an `INSTRUCTIONS.md` file.
- **SC-003**: The basics exercises lesson (L09) contains exactly 27 exercise walkthroughs (24 exercises + 3 capstones) and each walkthrough includes at minimum: title, problem description, task description, and learning outcomes.
- **SC-004**: The skills exercises lesson (L11) contains exactly 27 exercise walkthroughs (24 exercises + 3 capstones) with the same minimum structure.
- **SC-005**: Zero exercise/lab sections remain in L04, L07, L08, or L10 after modification. Each has exactly one pointer paragraph to the appropriate consolidated lesson.
- **SC-006**: All 28 lesson files in Chapter 3 have sequential `sidebar_position` values (1-28) with no gaps or duplicates, and the learn-app renders them in correct order.
- **SC-007**: A `grep -rn "Lesson 09\|Lesson 9\|L09\|lesson 9" apps/learn-app/docs/01-General-Agents-Foundations/03-general-agents/` returns zero matches in any file except the new L09 basics exercises lesson itself and L10 (which may reference its own former number contextually). All old L09 references that meant "subagents" now say L10.
- **SC-008**: The GitHub Actions workflow file is under 30 lines and completes in under 5 minutes on a push to main.
- **SC-009**: Both new lesson files pass YAML frontmatter validation (all required fields present: title, sidebar_position, chapter, lesson, duration_minutes, skills, learning_objectives, cognitive_load, differentiation).
- **SC-010**: The chapter README.md lists 28 lessons with correct titles and numbers.

### Content Quality Criteria

- **SC-011**: Each new lesson has a compelling narrative opening (2-3 paragraphs) that connects exercises to the student's learning journey, not a dry list.
- **SC-012**: Exercise walkthroughs match the existing exercise files exactly — every exercise title, folder name, and file reference in the lesson text corresponds to actual files in the ZIP.
- **SC-013**: Both new lessons include tool indicators (Claude Code / Cowork icons) on each exercise matching the current EXERCISE-GUIDE.md conventions.
- **SC-014**: Both new lessons are self-contained — a student does not need to reference the old monorepo, external EXERCISE-GUIDE.md, or any lesson other than the one they are reading to complete exercises.

---

## Implementation Notes

These notes are informational for the implementer, not binding requirements.

### GitHub Actions Workflow Template

```yaml
name: Release Exercise Pack
on:
  push:
    branches: [main]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Create ZIP
        run: zip -r basics-exercises.zip . -x '.github/*' '.git/*'
      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: latest
          files: basics-exercises.zip
          make_latest: true
```

### Pointer Paragraph Template

```markdown
:::tip Ready to Practice?
Head to **Lesson 9: Basics Exercises** for 24 hands-on exercises with complete walkthroughs.
You'll organize messy files, analyze data, create documents, and build problem-solving skills
— all with one-click exercise downloads and step-by-step guidance.
:::
```

### Renumbering Checklist

Files requiring `sidebar_position` and filename prefix updates:

| Current | New | File                              |
| ------- | --- | --------------------------------- |
| 09      | 10  | subagents-and-orchestration       |
| --      | 09  | basics-exercises (NEW)            |
| --      | 11  | skills-exercises (NEW)            |
| 10      | 12  | mcp-integration                   |
| 11      | 13  | compiling-mcp-to-skills           |
| 12      | 14  | settings-hierarchy                |
| 13      | 15  | hooks-and-extensibility           |
| 14      | 16  | plugins-putting-it-all-together   |
| 15      | 17  | ralph-wiggum-loop                 |
| 16      | 18  | creator-workflow                  |
| 17      | 19  | cowork-terminal-to-desktop        |
| 18      | 20  | cowork-getting-started            |
| 19      | 21  | cowork-practical-workflows        |
| 20      | 22  | browser-integration-claude-chrome |
| 21      | 23  | connectors-mcp-for-everyone       |
| 22      | 24  | safety-limitations-whats-coming   |
| 23      | 25  | cowork-built-in-skills            |
| 24      | 26  | code-vs-cowork-decision-framework |
| 25      | 27  | from-skills-to-business           |
| 26      | 28  | chapter-quiz                      |

Total files to rename: 17 existing + 2 new = 19 files requiring frontmatter updates.
Total `.summary.md` files to potentially update: 17 (one per renamed lesson).

### Basics Modules Reference (from existing EXERCISE-GUIDE.md)

| Module | Title                                    | Exercises                                                                           |
| ------ | ---------------------------------------- | ----------------------------------------------------------------------------------- |
| 1      | File Organization & Digital Housekeeping | 1.1 Messy Downloads, 1.2 Photo Album, 1.3 Inbox Zero                                |
| 2      | Research & Information Synthesis         | 2.1 Comparison Matrix, 2.2 Literature Review, 2.3 Decision Document                 |
| 3      | Data Wrangling & Analysis                | 3.1 Messy Spreadsheet, 3.2 Survey Analyzer, 3.3 Budget Tracker                      |
| 4      | Document Creation & Transformation       | 4.1 Meeting Notes, 4.2 Report Generator, 4.3 Presentation Builder                   |
| 5      | Process Automation & Workflows           | 5.1 Batch Renamer, 5.2 Template System, 5.3 Weekly Report Automator                 |
| 6      | Problem Solving & Creative Thinking      | 6.1 Business Plan, 6.2 Troubleshooter, 6.3 Event Planner                            |
| 7      | Quality Control & Critical Thinking      | 7.1 Fact Checker, 7.2 Specification Stress Test, 7.3 Prompt Tournament              |
| 8      | Capstone Projects                        | A: Personal Knowledge Base, B: Small Business Ops Kit, C: Course Material Generator |

### Skills Modules Reference (from existing skills EXERCISE-GUIDE.md)

| Module | Title                  | Exercises                                                                    |
| ------ | ---------------------- | ---------------------------------------------------------------------------- |
| 1      | Understanding Skills   | 1.1 Anatomy, 1.2 When to Skill, 1.3 Skill vs Prompt                          |
| 2      | First Skills           | 2.1 Email Style, 2.2 File Organizer, 2.3 Data Cleaner                        |
| 3      | Skills with Examples   | 3.1 Report Formatter, 3.2 Meeting Minutes, 3.3 Feedback Writer               |
| 4      | Skills with References | 4.1 Brand Voice, 4.2 Policy Checker, 4.3 Curriculum Skill                    |
| 5      | Testing and Iteration  | 5.1 Edge Case Hunt, 5.2 Before/After, 5.3 User Testing                       |
| 6      | Composing Skills       | 6.1 Pipeline, 6.2 Skill Library, 6.3 Team Skills                             |
| 7      | Real-World Skills      | 7.1 Invoice Processor, 7.2 Content Pipeline, 7.3 Research Analyst            |
| 8      | Capstone Projects      | A: Business Operations Suite, B: AI-Native Education Kit, C: Personal AI Set |
