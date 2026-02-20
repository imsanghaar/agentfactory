# Exercise Folder Standard

Extracted from `panaversity/claude-code-basic-exercises` and `panaversity/claude-code-skills-exercises`. This document defines the reusable standard for creating exercise repositories for any chapter.

---

## 1. Repository Structure

Each chapter's exercises live in their own GitHub repo under the `panaversity` org.

```
panaversity/claude-code-{topic}-exercises/
├── .github/
│   └── workflows/
│       └── release.yml          # Auto-ZIP and release on push to main
├── EXERCISE-GUIDE.md            # Full pedagogical guide (the "textbook")
├── README.md                    # Quick-start, package structure, schedule
├── module-1[-optional-slug]/    # Module folders (see naming below)
│   ├── exercise-1.1-slug/       # Exercise folders
│   └── exercise-1.2-slug/
├── module-2[-optional-slug]/
│   └── ...
├── ...
└── module-8[-optional-slug]/
    ├── capstone-A-slug/         # Capstones use capstone- prefix
    ├── capstone-B-slug/
    └── capstone-C-slug/
```

### Key structural rules

- **8 modules** per repo (modules 1-7 with 3 exercises each = 21 exercises, module 8 = 3 capstones)
- Total: **24 exercises + 3 capstones = 27 items** (actual shipped repos have ~21-24 exercises + 3 capstones)
- Top-level has exactly 3 files: `.github/`, `EXERCISE-GUIDE.md`, `README.md`
- No other top-level files (no LICENSE, no .gitignore, no package.json)

---

## 2. Module Naming Convention

Two patterns exist depending on exercise type:

### Task-oriented (basics pattern)
Module folders use **bare numbered names** when the topic is clear from the EXERCISE-GUIDE:

```
module-1/
module-2/
module-3/
...
module-8/
```

### Skill-building (skills pattern)
Module folders include a **descriptive slug** to convey the skill progression:

```
module-1-understanding-skills/
module-2-first-skills/
module-3-skills-with-examples/
module-4-skills-with-references/
module-5-testing-and-iteration/
module-6-composing-skills/
module-7-real-world-skills/
module-8-capstone/
```

### Decision rule
- If modules represent a **pedagogical progression** where the module name conveys learning level, use **slugged names** (e.g., skills repo)
- If modules represent **topic categories** where the topic is described in EXERCISE-GUIDE, use **bare numbers** (e.g., basics repo)

---

## 3. Exercise Folder Naming Convention

```
exercise-{module}.{number}-{slug}/
```

Examples:
```
exercise-1.1-messy-downloads/
exercise-3.2-survey-analyzer/
exercise-6.1-pipeline/
```

### Capstone naming:
```
capstone-{letter}-{slug}/
```

Examples:
```
capstone-A-knowledge-base/
capstone-B-business-ops-kit/
capstone-C-course-materials/
```

### Rules
- Module number matches parent folder number
- Exercise number is sequential within module (1.1, 1.2, 1.3)
- Slug is lowercase, hyphen-separated, 2-4 words
- Slug describes the task/scenario, not the skill being learned
- Capstones use letters A/B/C (always 3 capstones in module 8)

---

## 4. Exercise Folder Contents

Every exercise folder contains at minimum:

```
exercise-X.Y-slug/
├── INSTRUCTIONS.md              # REQUIRED: What to do (see template below)
└── [starter files/folders]      # Situational: data, samples, templates
```

### Starter file types (observed patterns)

| Type | Used When | Examples |
|------|-----------|---------|
| **Data files** (csv, txt) | Exercise works on data | `customer_data_messy.csv`, `product_survey_results.csv` |
| **Scenario files** (md) | Multiple scenarios to choose from | `scenario-A-project-management-tools.md`, `decision-B-career-pivot.md` |
| **Folders of files** | Exercise works on batch of files | `messy-downloads/` (35 files), `inbox/` (18 emails), `receipts/` (15 receipts) |
| **Skill files** (SKILL.md) | Exercise analyzes/improves a skill | `sample-skills/`, `email-response-skill-v1/SKILL.md` |
| **Template/reference files** | Exercise uses templates | `starter-template.md`, `rubric.md`, `brand-guide.md` |
| **Test prompts** (md) | Exercise includes prompts to test with | `test-prompts/greeting-prompts.md` |
| **No starter files** | Exercise generates from scratch | Exercise 5.3, 6.2, 6.3 (instructions-only) |

### Starter file naming
- Lowercase with hyphens or underscores (both acceptable, be consistent within a repo)
- Descriptive names that tell students what they contain
- Realistic names for "messy" files (e.g., `Budget 2025 FINAL (1).xlsx`)

---

## 5. INSTRUCTIONS.md Template

### For task-oriented exercises (basics pattern)

```markdown
# Exercise {M}.{N} -- {Title}

## What You Have
{1-3 sentences describing the starter files/data provided.
Be specific about counts and types.}

## Your Task
{Clear description of what the student should ask Claude to do.
Use numbered steps for multi-part tasks.}

## Try This Progression
{OPTIONAL: For early exercises, include 2-3 attempts
showing how to improve prompts iteratively.}

### Attempt 1 -- The Vague Prompt
> "Organize these files."

{Brief note about what to observe.}

### Attempt 2 -- Your Improved Prompt
{Guide what to consider specifying.}

### Attempt 3 -- The Professional Prompt
{Challenge to write production-quality instructions.}

## Important Prompt Detail
{OPTIONAL: One key constraint or specification to include.
Teaches a specific prompt engineering principle.}

## Bonus Challenge
{OPTIONAL: Extension task for advanced students.}

## Reflection
{2-4 questions that build metacognition about prompt quality.}
```

### For skill-building exercises (skills pattern)

```markdown
# Exercise {M}.{N} -- {Title}

## Goal
{1-2 sentences: what skill/concept this exercise teaches.}

## What's New in This Exercise
{OPTIONAL: How this builds on previous exercises.
Only needed for modules 3+ where concepts stack.}

## What You Have
{Description of provided files and their purpose.}

## Skill Structure to Build
{OPTIONAL: Show the target folder structure for the skill.}

```
skill-name/
+-- SKILL.md
+-- examples/
+-- templates/
```

## Your Tasks / Step-by-Step
{Numbered steps. Skills exercises tend to have more structure:}

### Task A / Step 1: {Action}
{Detailed instructions.}

### Task B / Step 2: {Action}
{Detailed instructions.}

### Task C / Step 3: {Action}
{Detailed instructions.}

## Key Insight
{OPTIONAL: A conceptual takeaway that connects this exercise
to the bigger picture of agent building.}
```

### Format comparison

| Section | Basics | Skills |
|---------|--------|--------|
| Title | `Exercise X.Y -- The {Noun}` | `Exercise X.Y -- {Concept/Action}` |
| Opens with | `What You Have` | `Goal` |
| Task section | `Your Task` (open-ended) | `Your Tasks` or `Step-by-Step` (structured) |
| Progression | `Try This Progression` (prompt quality) | Steps that build incrementally |
| Reflection | Present (metacognition focus) | Often replaced by `Key Insight` |
| Rubric | Referenced in EXERCISE-GUIDE only | Sometimes embedded or referenced |

---

## 6. EXERCISE-GUIDE.md Template Structure

The EXERCISE-GUIDE is the pedagogical backbone -- the full "textbook" that explains every exercise in context.

```markdown
# {Title}

**{Subtitle/tagline}**

*By Panaversity -- {Mission phrase}*

---

## How This Guide Works
{3-4 paragraphs explaining:}
- The exercise pattern (what students do each time)
- The 2-3 core skills being developed across all modules
- Tool guide (Claude Code vs Cowork, which to use when)

---

## Module {N}: {Module Title}

> **Core Skill:** {One sentence describing the transferable skill.}

### Exercise {M}.{N} -- {Title} {tool-icons}

**The Problem:**
{2-3 sentences setting the realistic scenario.}

**Your Task:**
{Numbered list of what Claude should produce.}

**{Pedagogical element}:**
{One of: Starter Prompt, Important Constraint, The Twist,
The Challenge, The Meta-Exercise -- varies by exercise.}

**What You'll Learn:**
{3-4 bullet points: transferable principles, not just task completion.}

**Reflection Questions:**
{OPTIONAL: 2-3 self-assessment questions.}

---

{Repeat for all exercises...}

---

## Module 8: Capstone Projects

> **Choose one. Spend real time on it. This is where everything comes together.**

### Capstone A -- {Title} {tool-icons}
{Full description of the capstone project.}

---

## Assessment Rubric

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| {criterion 1} | {description} | {description} | {description} | {description} |
| {criterion 2} | ... | ... | ... | ... |

---

## Quick Reference: {Framework Name}

{Summary of the problem-solving/skill-building framework
used across all exercises.}

---

*Built for Panaversity's AI-Native Development Curriculum.*
```

### Key design rules for EXERCISE-GUIDE
- Each exercise in the guide is **self-contained** (can be read independently)
- Module intro has a `> **Core Skill:**` callout
- Exercises include `What You'll Learn` focusing on **transferable principles**
- The guide includes the full rubric (exercises only reference it)
- Tool icons (if used): designate Claude Code vs Cowork suitability

---

## 7. README.md Template

```markdown
# {Repo Title}

**By Panaversity -- {Tagline}**

{2-3 sentence welcome paragraph.}

---

## Package Structure

```
{repo-name}/
+-- README.md
+-- EXERCISE-GUIDE.md
+-- module-1/
|   +-- exercise-1.1-slug/    (brief description)
|   +-- exercise-1.2-slug/    (brief description)
|   +-- exercise-1.3-slug/    (brief description)
+-- module-2/
|   ...
+-- module-8/
    +-- capstone-A-slug/
    +-- capstone-B-slug/
    +-- capstone-C-slug/
```

---

## How to Get Started

### With Cowork (Recommended for Beginners)
{3-4 steps}

### With Claude Code (For Terminal Users)
{3-4 steps}

---

## Recommended Order

**Week 1:** Exercises 1.1, 1.2, 1.3
**Week 2:** Exercises 2.1, 2.2, 2.3
...
**Week 8:** Choose one capstone project

---

## {Framework Name}

{The 5-7 step framework used across all exercises.}

---

## Self-Assessment Rubric

{Same rubric as EXERCISE-GUIDE, or abbreviated version.}

---

*Built for Panaversity's AI-Native Development Curriculum*
```

---

## 8. Differences: Task-Oriented vs Skill-Building Exercises

| Dimension | Task-Oriented (Basics) | Skill-Building (Skills) |
|-----------|----------------------|------------------------|
| **Repo name** | `claude-code-{topic}-exercises` | `claude-code-{topic}-exercises` |
| **Module naming** | Bare numbers (`module-1/`) | Numbered + slug (`module-1-understanding-skills/`) |
| **What students DO** | Give Claude a task, evaluate output | Build a SKILL.md file, test it, iterate |
| **Starter files** | Data to work ON (csv, txt, folders) | Skills to study/improve + data to test WITH |
| **INSTRUCTIONS.md** | Outcome-focused ("ask Claude to...") | Process-focused ("build a skill that...") |
| **Progression model** | Prompt quality (vague -> precise) | Skill complexity (read -> write -> compose -> test) |
| **Iteration focus** | Refine the PROMPT | Refine the SKILL.MD |
| **Learning signal** | "Did Claude produce what I wanted?" | "Does my skill work consistently across inputs?" |
| **Reflection** | Metacognition about prompt clarity | Conceptual insight about agent architecture |
| **Capstones** | Multi-tool project (combine all task types) | Multi-skill suite (orchestrate multiple skills) |
| **EXERCISE-GUIDE** | Includes full exercise descriptions + starter prompts | Includes framework + module overview (less per-exercise detail) |

### When to use which type
- **Task-oriented**: Chapter teaches Claude Code/Cowork usage, problem decomposition, prompt engineering
- **Skill-building**: Chapter teaches SKILL.md creation, agent customization, workflow composition

---

## 9. GitHub Actions: Release Workflow

Both repos use identical release automation:

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
        run: zip -r {topic}-exercises.zip . -x '.github/*' '.git/*'
      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: latest
          files: {topic}-exercises.zip
          make_latest: true
```

This creates a downloadable ZIP on every push to main, excluding `.github/` and `.git/`.

---

## 10. Checklist: Creating a Single Exercise

Use this checklist when adding an exercise to a repo.

### Planning
- [ ] Exercise has a clear, single learning objective
- [ ] Exercise fits the module's theme/core skill
- [ ] Exercise number follows convention: `exercise-{module}.{seq}-{slug}`
- [ ] Slug is 2-4 lowercase hyphenated words describing the task

### INSTRUCTIONS.md
- [ ] File exists at `module-N/exercise-N.X-slug/INSTRUCTIONS.md`
- [ ] Title follows format: `# Exercise {M}.{N} -- {Title}`
- [ ] Has `What You Have` section (or `Goal` for skills)
- [ ] Has `Your Task` section with clear deliverables
- [ ] Numbered steps for multi-part tasks
- [ ] (Basics) Has `Reflection` questions or prompt progression
- [ ] (Skills) Has `Step-by-Step` with structured tasks
- [ ] No solutions or expected outputs embedded (student discovers these)

### Starter Files
- [ ] All starter files present and realistic
- [ ] File names match what INSTRUCTIONS.md references
- [ ] Data files have enough rows/items to be interesting (10+ minimum)
- [ ] Messy files are genuinely messy (not just renamed clean data)
- [ ] Scenario/choice files (if any) offer meaningfully different options (A/B/C pattern)
- [ ] No placeholder or empty files

### Quality
- [ ] Exercise is completable in 15-45 minutes (capstones: 2-4 hours)
- [ ] Exercise teaches a transferable principle, not just a task
- [ ] Exercise works with BOTH Claude Code and Cowork (or explicitly states which)
- [ ] Instructions are unambiguous (no vague words like "nice" or "proper")
- [ ] All file paths in INSTRUCTIONS.md are relative to the exercise folder

### Integration
- [ ] Exercise is listed in EXERCISE-GUIDE.md with full description
- [ ] Exercise is listed in README.md package structure
- [ ] Module has exactly 3 exercises (or 3 capstones for module 8)
- [ ] Exercise builds on previous module skills (progression check)
