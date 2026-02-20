# Exercise Review Rubric

Quality criteria for reviewing exercise packs, lessons, and GitHub setup. Each section uses **Pass/Fail** per criterion with specific check items.

---

## 1. Exercise Quality (INSTRUCTIONS.md + Starter Files)

### INSTRUCTIONS.md Completeness

| #   | Check Item                                                                     | Pass/Fail |
| --- | ------------------------------------------------------------------------------ | --------- |
| 1.1 | Has a clear title and one-sentence description of the exercise                 |           |
| 1.2 | States what the student will practice or learn                                 |           |
| 1.3 | Lists all files included in the exercise folder and what each contains         |           |
| 1.4 | Provides a clear task description — what the student should ask Claude to do   |           |
| 1.5 | Includes success criteria — how the student knows they're done                 |           |
| 1.6 | Includes at least one "stretch goal" or extension challenge                    |           |
| 1.7 | Does NOT include the solution or expected output (students should discover it) |           |
| 1.8 | Specifies whether to use Claude Code, Cowork, or either                        |           |

### Starter File Quality

| #   | Check Item                                                                                                                  | Pass/Fail |
| --- | --------------------------------------------------------------------------------------------------------------------------- | --------- |
| 2.1 | Starter files are realistic (not obviously fake data)                                                                       |           |
| 2.2 | Files contain enough complexity to require AI assistance (not trivially solvable by hand)                                   |           |
| 2.3 | Files do NOT contain errors that would prevent Claude from processing them (corrupted encoding, binary where text expected) |           |
| 2.4 | File formats are appropriate (CSV for data, TXT/MD for text, actual images for image tasks)                                 |           |
| 2.5 | Filenames are descriptive or intentionally messy (matching the exercise theme)                                              |           |
| 2.6 | No placeholder content like "TODO" or "Lorem ipsum" unless that IS the exercise                                             |           |

### Difficulty Appropriateness

| #   | Check Item                                                                                | Pass/Fail |
| --- | ----------------------------------------------------------------------------------------- | --------- |
| 3.1 | Module 1-2 exercises are completable with a single, simple prompt                         |           |
| 3.2 | Module 3-5 exercises require multi-step prompting or iteration                            |           |
| 3.3 | Module 6-7 exercises require judgment, evaluation, or creative thinking                   |           |
| 3.4 | Module 8 capstones combine multiple skills from earlier modules                           |           |
| 3.5 | Exercise difficulty matches its position in the progression                               |           |
| 3.6 | No exercise requires external tools, accounts, or installations beyond Claude Code/Cowork |           |

---

## 2. Lesson Quality (Walkthrough in learn-app)

### Walkthrough Accuracy

| #   | Check Item                                                                       | Pass/Fail |
| --- | -------------------------------------------------------------------------------- | --------- |
| 4.1 | Lesson references the correct exercise folder path as it exists in the ZIP       |           |
| 4.2 | All filenames mentioned in the lesson exist in the exercise folder               |           |
| 4.3 | Sample prompts in the lesson actually work when tried against the exercise files |           |
| 4.4 | Screenshots or code blocks match the current exercise content (if present)       |           |
| 4.5 | The lesson does not describe exercise content that was changed or removed        |           |

### Pedagogical Value

| #   | Check Item                                                                                                    | Pass/Fail |
| --- | ------------------------------------------------------------------------------------------------------------- | --------- |
| 5.1 | Lesson explains WHY the exercise matters (not just WHAT to do)                                                |           |
| 5.2 | Lesson teaches a transferable skill, not just exercise-specific steps                                         |           |
| 5.3 | Lesson includes reflection prompts or "what to notice" guidance                                               |           |
| 5.4 | Lesson connects to the Problem-Solving Framework (Define, Gather, Specify, Execute, Verify, Iterate, Reflect) |           |
| 5.5 | Lesson builds on skills from previous lessons (progressive complexity)                                        |           |
| 5.6 | Lesson includes common mistakes or "what if it doesn't work" troubleshooting                                  |           |

### Lesson File Standards

| #   | Check Item                                                                                                       | Pass/Fail |
| --- | ---------------------------------------------------------------------------------------------------------------- | --------- |
| 6.1 | YAML frontmatter is present and complete (title, sidebar_label, sidebar_position, slug)                          |           |
| 6.2 | Download link is present and uses correct format: `**[Download ... (ZIP)](URL)**`                                |           |
| 6.3 | Download URL matches the pattern: `https://github.com/panaversity/{{REPO}}/releases/latest/download/{{ZIP}}.zip` |           |
| 6.4 | MDX imports are valid (no broken imports)                                                                        |           |
| 6.5 | Admonitions use correct Docusaurus syntax (`:::tip`, `:::info`, etc.)                                            |           |

---

## 3. GitHub Setup Quality

### Workflow

| #   | Check Item                                                           | Pass/Fail |
| --- | -------------------------------------------------------------------- | --------- |
| 7.1 | `.github/workflows/release.yml` exists                               |           |
| 7.2 | Workflow triggers on push to `main` branch                           |           |
| 7.3 | ZIP excludes `.github/*` and `.git/*` directories                    |           |
| 7.4 | ZIP filename follows convention: `<topic>-exercises.zip`             |           |
| 7.5 | Release uses `tag_name: latest` and `make_latest: true`              |           |
| 7.6 | Workflow ran successfully at least once (green check in Actions tab) |           |

### Release and Download

| #   | Check Item                                                                                                                      | Pass/Fail |
| --- | ------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 8.1 | Release tagged `latest` exists on the repo                                                                                      |           |
| 8.2 | Release has exactly one ZIP asset attached                                                                                      |           |
| 8.3 | Download URL returns a valid ZIP file (not 404): `https://github.com/panaversity/{{REPO}}/releases/latest/download/{{ZIP}}.zip` |           |
| 8.4 | Downloaded ZIP extracts without errors                                                                                          |           |
| 8.5 | Extracted ZIP contains all exercise folders with INSTRUCTIONS.md                                                                |           |
| 8.6 | Extracted ZIP does NOT contain `.github/` or `.git/` directories                                                                |           |
| 8.7 | ZIP file size is reasonable (<500KB for text-only exercises, <5MB if images included)                                           |           |

### Repository

| #   | Check Item                                                    | Pass/Fail |
| --- | ------------------------------------------------------------- | --------- |
| 9.1 | Repo is public                                                |           |
| 9.2 | Repo has a README.md                                          |           |
| 9.3 | README describes the exercise pack and how to get started     |           |
| 9.4 | Repo name follows convention: `claude-code-<topic>-exercises` |           |
| 9.5 | Default branch is `main`                                      |           |
| 9.6 | Actions are enabled                                           |           |

---

## 4. Cross-Reference Accuracy

### Lesson-to-Repo Links

| #    | Check Item                                                                | Pass/Fail |
| ---- | ------------------------------------------------------------------------- | --------- |
| 10.1 | Every lesson with exercises has a download link                           |           |
| 10.2 | Download link repo name matches the actual GitHub repo                    |           |
| 10.3 | Download link ZIP name matches the actual release asset name              |           |
| 10.4 | No lessons reference the archived `claude-code-exercises` repo            |           |
| 10.5 | Lesson exercise folder paths match the actual folder structure in the ZIP |           |

### Navigation and Progression

| #    | Check Item                                                                                               | Pass/Fail |
| ---- | -------------------------------------------------------------------------------------------------------- | --------- |
| 11.1 | Each exercise lesson has a "What's Next" section pointing to the next lesson                             |           |
| 11.2 | "What's Next" links are valid (target lesson exists)                                                     |           |
| 11.3 | Previous lesson's "What's Next" points to this lesson                                                    |           |
| 11.4 | Exercise lessons appear in correct `sidebar_position` order                                              |           |
| 11.5 | The chapter's lesson progression makes pedagogical sense (theory before practice, simple before complex) |           |

### Pack Consistency

| #    | Check Item                                                                   | Pass/Fail |
| ---- | ---------------------------------------------------------------------------- | --------- |
| 12.1 | All exercises in the pack are referenced by at least one lesson              |           |
| 12.2 | No lesson references exercises that don't exist in the pack                  |           |
| 12.3 | Module numbering in the pack matches the lesson progression in the book      |           |
| 12.4 | The pack README's recommended order aligns with the lesson order in the book |           |

---

## 5. Scoring Summary

### Per-Section Scores

| Section                               | Total Checks | Passed | Failed | Score   |
| ------------------------------------- | ------------ | ------ | ------ | ------- |
| 1. Exercise Quality (INSTRUCTIONS.md) | 8            |        |        | /8      |
| 1. Exercise Quality (Starter Files)   | 6            |        |        | /6      |
| 1. Exercise Quality (Difficulty)      | 6            |        |        | /6      |
| 2. Lesson Quality (Walkthrough)       | 5            |        |        | /5      |
| 2. Lesson Quality (Pedagogical)       | 6            |        |        | /6      |
| 2. Lesson Quality (File Standards)    | 5            |        |        | /5      |
| 3. GitHub Setup (Workflow)            | 6            |        |        | /6      |
| 3. GitHub Setup (Release)             | 7            |        |        | /7      |
| 3. GitHub Setup (Repository)          | 6            |        |        | /6      |
| 4. Cross-Reference (Links)            | 5            |        |        | /5      |
| 4. Cross-Reference (Navigation)       | 5            |        |        | /5      |
| 4. Cross-Reference (Consistency)      | 4            |        |        | /4      |
| **TOTAL**                             | **69**       |        |        | **/69** |

### Gate Criteria

| Gate             | Requirement                                                         | Verdict |
| ---------------- | ------------------------------------------------------------------- | ------- |
| **Ship**         | All 69 checks pass                                                  |         |
| **Fix and Ship** | 60+ pass, no fails in GitHub Setup or Cross-Reference sections      |         |
| **Revise**       | Any fail in GitHub Setup (section 3) or Cross-Reference (section 4) |         |
| **Rework**       | 10+ total fails, or any entire section scores 0                     |         |

### Notes

- **GitHub Setup (section 3) and Cross-Reference (section 4) are blocking gates.** A working download link is the minimum viable requirement -- without it, the exercises are inaccessible.
- **Exercise Quality (section 1) is the hardest to assess** because it requires actually attempting the exercise. At minimum, verify INSTRUCTIONS.md completeness (checks 1.1-1.8) and spot-check one starter file per module.
- **Lesson Quality (section 2)** should be verified against the actual exercise ZIP, not the repo source, since students download the ZIP.
