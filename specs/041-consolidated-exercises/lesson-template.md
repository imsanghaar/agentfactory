# Exercise Lesson Template

> Extracted from Ch3 L06 (basics-exercises) and Ch3 L10 (skills-exercises).
> Placeholders use `{{PLACEHOLDER}}` syntax. Comments use `<!-- -->`.

---

## Template: YAML Frontmatter

```yaml
---
title: "{{LESSON_TITLE}}"
sidebar_position: {{SIDEBAR_POSITION}}
chapter: {{CHAPTER_NUMBER}}
lesson: {{LESSON_NUMBER}}
duration_minutes: 120

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "{{L1_DESCRIPTION}}"
# <!-- e.g. "Hands-on practice applying Lessons XX-YY concepts through 27 guided exercises" -->
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "{{SKILL_1_NAME}}"
    proficiency_level: "{{A1|A2|B1|B2}}"
    category: "{{Conceptual|Technical|Applied|Soft}}"
    bloom_level: "{{Remember|Understand|Apply|Analyze|Evaluate|Create}}"
    digcomp_area: "{{DIGCOMP_AREA}}"
    measurable_at_this_level: "{{MEASURABLE_OUTCOME}}"
  - name: "{{SKILL_2_NAME}}"
    proficiency_level: "{{A1|A2|B1|B2}}"
    category: "{{Conceptual|Technical|Applied|Soft}}"
    bloom_level: "{{Remember|Understand|Apply|Analyze|Evaluate|Create}}"
    digcomp_area: "{{DIGCOMP_AREA}}"
    measurable_at_this_level: "{{MEASURABLE_OUTCOME}}"
  - name: "{{SKILL_3_NAME}}"
    proficiency_level: "{{A1|A2|B1|B2}}"
    category: "{{Conceptual|Technical|Applied|Soft}}"
    bloom_level: "{{Remember|Understand|Apply|Analyze|Evaluate|Create}}"
    digcomp_area: "{{DIGCOMP_AREA}}"
    measurable_at_this_level: "{{MEASURABLE_OUTCOME}}"
# <!-- 3 skills is the standard. Match to the chapter's core competencies. -->

learning_objectives:
  - objective: "{{OBJECTIVE_1}}"
    proficiency_level: "{{LEVEL}}"
    bloom_level: "{{BLOOM}}"
    assessment_method: "{{HOW_ASSESSED}}"
  - objective: "{{OBJECTIVE_2}}"
    proficiency_level: "{{LEVEL}}"
    bloom_level: "{{BLOOM}}"
    assessment_method: "{{HOW_ASSESSED}}"
  - objective: "{{OBJECTIVE_3}}"
    proficiency_level: "{{LEVEL}}"
    bloom_level: "{{BLOOM}}"
    assessment_method: "{{HOW_ASSESSED}}"
# <!-- Typically 3-4 objectives. Each maps to a skill above. -->

cognitive_load:
  new_concepts: 3
  assessment: "{{COGNITIVE_LOAD_JUSTIFICATION}}"
  # <!-- e.g. "3 concepts (X, Y, Z) — within A2 limit. Exercises reinforce existing LXX-LYY knowledge." -->

differentiation:
  extension_for_advanced: "{{ADVANCED_PATH}}"
  # <!-- e.g. "Complete all 3 capstone projects; attempt exercises with minimal prompts" -->
  remedial_for_struggling: "{{REMEDIAL_PATH}}"
  # <!-- e.g. "Start with Module 1 only; use the starter prompts provided" -->
---
```

---

## Template: Opening Narrative

```markdown
# {{LESSON_TITLE}}

{{OPENING_PARAGRAPH_1}}
<!-- Paragraph 1: Acknowledge what students already know from prior lessons.
     Pattern: "You understand X. You've done Y. That's real knowledge — but..."
     Establishes continuity and sets up the gap this lesson fills. -->

{{OPENING_PARAGRAPH_2}}
<!-- Paragraph 2: Describe what these exercises do and how they work.
     Pattern: "These exercises close the gap between [knowing] and [doing]."
     Name the 3 core skills that run through every exercise. -->

{{OPENING_PARAGRAPH_3_OPTIONAL}}
<!-- Paragraph 3 (optional): The Big Idea or overarching theme.
     Used in skills-exercises: "The Big Idea behind all of this: **a skill is...**"
     Only include if the chapter has a unifying concept worth stating upfront. -->
```

**Pattern notes:**
- Basics used 2 paragraphs (sufficient for straightforward practice)
- Skills used 3 paragraphs (needed to state "The Big Idea")
- Both bold the core skills on first mention
- Tone: direct, no fluff, acknowledges prior learning

---

## Template: Download Section

```markdown
:::info Download Exercise Files
**[Download {{EXERCISE_SET_NAME}} (ZIP)](https://github.com/panaversity/{{REPO_NAME}}/releases/latest/download/{{ZIP_FILENAME}}.zip)**

After downloading, unzip the file. Each exercise has its own folder with an `INSTRUCTIONS.md` and any starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/panaversity/{{REPO_NAME}}/releases) directly.
:::
```

**Pattern notes:**
- Always uses `:::info` admonition block
- Download link points to GitHub releases `/latest/download/`
- Fallback link to releases page
- Consistent wording about unzipping and folder structure

---

## Template: How to Use These Exercises

```markdown
## How to Use These Exercises

{{HOW_TO_USE_DESCRIPTION}}
<!-- Either "The workflow for every exercise is the same:" (basics)
     or "Every exercise follows the same workflow:" (skills) -->

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}
4. {{STEP_4}}
5. {{STEP_5}}
6. {{STEP_6_OPTIONAL}}

{{PACING_NOTE}}
<!-- e.g. "You don't need to complete all 27 in one sitting. Work through one module at a time."
     or module ordering guidance -->
```

**Pattern notes (from both lessons):**

Basics (6 steps):
1. Open the exercise folder from the directory
2. Read the INSTRUCTIONS.md — setup steps and starter files
3. Read the walkthrough below for context
4. Start Claude Code or Cowork and point it at the exercise folder
5. Work through the exercise — write your own prompts
6. Reflect using the questions provided

Skills (5 steps):
1. Navigate to the exercise folder in your terminal
2. Start Claude Code or open the folder in Cowork
3. Tell Claude: `Read INSTRUCTIONS.md and help me build this skill...`
4. Work through each task in the instructions
5. Reflect on the questions at the end

---

## Template: Tool Guide

```markdown
## Tool Guide

{{TOOL_GUIDE_CONTENT}}
```

**Pattern — Use emoji indicators (basics pattern):**
```markdown
- {{EMOJI_1}} = **{{TOOL_1}}** ({{TOOL_1_DESCRIPTION}})
- {{EMOJI_2}} = **{{TOOL_2}}** ({{TOOL_2_DESCRIPTION}})
- Most exercises work with either tool. Start with whichever you're comfortable with.
```

**Concrete example (reusable as-is for most chapters):**
```markdown
- Claude Code — Terminal-based, best for {{TOOL_USE_CASE_1}}
- Cowork — Desktop app, best for {{TOOL_USE_CASE_2}}

Most exercises work with either tool. Where one is clearly better, the exercise notes will say so.
```

**Pattern notes:**
- Basics: used emoji indicators on exercise titles (e.g., `Exercise 1.1 — Title` followed by tool emoji codes)
- Skills: described tools in prose, no emoji codes on titles
- Choose based on chapter context; emoji indicators are more scannable

---

## Template: Framework Section

This is the **pluggable** section that varies by exercise type. Each chapter's exercises should define a framework appropriate to their domain.

```markdown
## {{FRAMEWORK_NAME}}

{{FRAMEWORK_INTRO}}
<!-- e.g. "Use this for every exercise:" or "Use this framework for **every** skill you build:" -->

{{FRAMEWORK_STEPS}}
```

**Pattern A — Numbered steps (basics "Problem-Solving Framework"):**
```markdown
## Problem-Solving Framework

Use this for every exercise:

1. **Define the Problem** — What exactly am I trying to accomplish? What does "done" look like?
2. **Gather Context** — What files, data, or information does Claude need?
3. **Write the Spec** — Describe the desired outcome, constraints, and format
4. **Execute** — Run it with Claude Code or Cowork
5. **Verify** — Does the output match what I asked for? Is it correct?
6. **Iterate** — What would I change? Run it again with improvements
7. **Reflect** — What did I learn about specifying problems clearly?

This framework isn't just for exercises — it's how professionals work with AI agents every day.
```

**Pattern B — Headed sub-steps (skills "Skill-Building Framework"):**
```markdown
## The Skill-Building Framework

Use this framework for **every** skill you build across these exercises:

### 1. DEFINE — What problem does this skill solve?

- What task is being automated?
- What does "good" output look like?
- What's the current pain (without the skill)?

### 2. DRAFT — Write the first version
...

### 6. REPEAT — Until quality is consistent
...

This framework applies whether you're building a simple X or a complex Y. Return to it whenever you get stuck.
```

**Guidelines for new frameworks:**
- Name it after the chapter's core methodology
- 5-7 steps is the sweet spot
- Each step: **Bold Name** + dash + guiding question or description
- End with a sentence connecting the framework to professional practice
- Pattern A (numbered) for simpler/sequential workflows
- Pattern B (headed) for frameworks with sub-bullets under each step

---

## Template: Assessment Rubric

```markdown
## {{RUBRIC_TITLE}}

{{RUBRIC_INTRO}}
<!-- e.g. "For each exercise, evaluate yourself on:" or
     "Use this rubric to evaluate every skill you build. Score yourself honestly:" -->

| Criteria | {{LEVEL_1_LABEL}} (1) | {{LEVEL_2_LABEL}} (2) | {{LEVEL_3_LABEL}} (3) | {{LEVEL_4_LABEL}} (4) |
| --- | :---: | :---: | :---: | :---: |
| **{{CRITERION_1}}** | {{1_BEG}} | {{1_DEV}} | {{1_PRO}} | {{1_ADV}} |
| **{{CRITERION_2}}** | {{2_BEG}} | {{2_DEV}} | {{2_PRO}} | {{2_ADV}} |
| **{{CRITERION_3}}** | {{3_BEG}} | {{3_DEV}} | {{3_PRO}} | {{3_ADV}} |
| **{{CRITERION_4}}** | {{4_BEG}} | {{4_DEV}} | {{4_PRO}} | {{4_ADV}} |
| **{{CRITERION_5}}** | {{5_BEG}} | {{5_DEV}} | {{5_PRO}} | {{5_ADV}} |
| **{{CRITERION_6_OPTIONAL}}** | {{6_BEG}} | {{6_DEV}} | {{6_PRO}} | {{6_ADV}} |

{{SCORING_GUIDANCE_OPTIONAL}}
<!-- e.g. "A score of 18+ (out of 24) means production-ready. Below 12 means another iteration round." -->
```

**Pattern notes:**
- Basics: 5 criteria, 4 levels (Beginner/Developing/Proficient/Advanced), no scoring guidance
- Skills: 6 criteria, 4 levels (same labels), includes scoring thresholds and tracking advice
- Both use a markdown table with center-aligned data columns
- Criteria should map to the chapter's core skills
- 5-6 rows is the sweet spot; fewer feels incomplete, more overwhelms

---

## Template: Module Section

```markdown
## Module {{N}}: {{MODULE_TITLE}}

> **Core Skill:** {{ONE_SENTENCE_CORE_SKILL}}

<!-- The blockquote names the single skill this module develops.
     Pattern: verb-ing + object + "by" + method.
     e.g. "Turning chaos into structure by describing organizational rules clearly."
     e.g. "Before you build skills, you need to read them fluently." (prose variant) -->
```

**Pattern notes:**
- Module heading: `## Module N: Title`
- Immediately followed by a blockquote with "Core Skill:" (basics) or an introductory paragraph (skills)
- Basics used blockquote consistently; Skills used blockquote for some modules, prose intro for others
- Recommendation: Use blockquote for consistency, add 1-2 prose sentences if the module needs more context

---

## Template: Exercise (Standard)

```markdown
### Exercise {{MODULE}}.{{EXERCISE}} — {{EXERCISE_TITLE}} {{TOOL_INDICATORS_OPTIONAL}}

**The Problem:**
{{PROBLEM_DESCRIPTION}}
<!-- 2-4 sentences describing the realistic scenario.
     References specific files/folders from the exercise repo.
     Pattern: "Open the X folder..." or "You have/need..." -->

**Your Task:**
{{TASK_DESCRIPTION}}
<!-- What the student must do. Can be:
     - A paragraph describing the overall task
     - A numbered list of specific sub-tasks (for multi-step exercises)
     - A combination: paragraph intro + numbered list -->

**What You'll Learn:**

- {{LEARNING_POINT_1}}
- {{LEARNING_POINT_2}}
- {{LEARNING_POINT_3}}
<!-- 3 bullet points. Each names a transferable insight, not just the task outcome.
     Pattern: "The difference between X and Y" / "How to Z" / "Why A matters for B" -->

{{PROMPT_SECTION}}
<!-- VARIANT A (basics pattern — vague + better):

**Starter Prompt (Intentionally Vague):**

> "{{VAGUE_PROMPT}}"

**Better Prompt (Build Toward This):**
{{GUIDANCE_TOWARD_BETTER_PROMPT}}
-->

<!-- VARIANT B (skills pattern — single starter):

**Starter Prompt:**

> "{{STARTER_PROMPT}}"
-->

<!-- VARIANT C (no prompt — used for later modules where students design their own approach) -->

**Reflection Questions:**

1. {{REFLECTION_Q1}}
2. {{REFLECTION_Q2}}
3. {{REFLECTION_Q3}}
<!-- 3 questions. Pattern:
     Q1: Did the output match expectations? What was different?
     Q2: What did you learn about the process/specification?
     Q3: How would you improve/generalize/reuse this? -->

---
```

**Optional exercise sections (include when appropriate):**

```markdown
**The Twist:**
{{TWIST_DESCRIPTION}}
<!-- A variation that deepens learning. Common patterns:
     - Do it two different ways and compare
     - Introduce a constraint change after completion
     - Apply to your own real data -->

**The Extension:**
{{EXTENSION_DESCRIPTION}}
<!-- An additional task that goes beyond the core exercise.
     Used when the exercise has a natural "and then also..." step. -->

**The Challenge:**
{{CHALLENGE_DESCRIPTION}}
<!-- A harder variant. Common pattern:
     - Do in two rounds (naive then refined) and compare -->

**The Meta-Exercise:**
{{META_DESCRIPTION}}
<!-- A reflective task about the exercise itself.
     e.g. "Write a critique of the output, then ask Claude to revise." -->

**The Goal:**
{{GOAL_DESCRIPTION}}
<!-- Explicit success criteria, used when the exercise has a clear testable outcome.
     e.g. "Your prompt should be reusable — test by changing data and running again." -->
```

**Pattern notes:**
- Each exercise is separated by `---` (horizontal rule)
- Exercise titles use `###` (H3) under module `##` (H2)
- Tool indicators (emoji codes) appear after title in basics; omitted in skills
- "The Problem" always comes first, always references exercise files
- "Your Task" can be paragraph or numbered list (use list for 3+ sub-tasks)
- "What You'll Learn" is always 3 bullets
- Prompt section varies: early modules have Starter+Better; later modules drop prompts
- "Reflection Questions" are always 3 numbered questions
- Twist/Extension/Challenge/Meta are optional — use 0-1 per exercise
- Every exercise ends with `---`

---

## Template: Capstone Project

```markdown
## Module {{N}}: Capstone Projects

> **Choose one (or more). Spend real time on it. This is where everything comes together.**

{{CAPSTONE_INTRO_OPTIONAL}}
<!-- Optional: 1-2 sentences explaining how capstones differ from exercises.
     e.g. "There are no starter prompts — you design the entire approach yourself." -->

### Capstone {{LETTER}} — {{CAPSTONE_TITLE}} {{TOOL_INDICATORS_OPTIONAL}}

{{CAPSTONE_INTRO}}
<!-- VARIANT A (basics — descriptive paragraph):
     1-2 sentences describing the scenario and what to do.
     References exercise files. -->

<!-- VARIANT B (skills — "The Mission" pattern):

**The Mission:**
{{MISSION_DESCRIPTION}}

**Skills to Build:**

1. **{{SKILL_1}}** — {{DESCRIPTION}}
2. **{{SKILL_2}}** — {{DESCRIPTION}}
...

**Quality Bar:** {{QUALITY_CRITERIA}}
-->

<!-- For basics-style capstones: use a numbered or bulleted list of what Claude should produce -->

**What You'll Learn:**

- {{LEARNING_1}}
- {{LEARNING_2}}
- {{LEARNING_3}}

---
```

**Pattern notes:**
- Capstones are the last module (Module 8 in both lessons)
- Module intro uses a blockquote with "Choose one (or more)" language
- Basics: 3 capstones (A, B, C), each has a scenario paragraph + task list + What You'll Learn
- Skills: 3 capstones (A, B, C), uses "The Mission" + "Skills to Build" + "Quality Bar" + "What You'll Learn"
- Capstone C in skills is unique: "Personal" — student defines their own scope
- No Reflection Questions in capstones (the project IS the reflection)
- No Starter Prompts in capstones (students design their own approach)

---

## Template: What's Next Section

```markdown
## What's Next

{{WHATS_NEXT_PARAGRAPH}}
<!-- Single paragraph. Structure:
     Sentence 1: Summarize what was practiced (name the core skills + exercise count).
     Sentence 2: State the compounding effect ("These skills compound: every exercise makes...")
     Sentence 3+: Preview the next 1-2 lessons with brief descriptions of what they cover.
     Use "Next in Lesson X" and "Then Lesson Y" phrasing. -->
```

**Pattern from basics:**
> You've practiced the three core skills — problem decomposition, specification writing, and quality verification — across 27 exercises. These skills compound: every exercise makes the next one easier because you're building intuition for how to communicate with AI agents. Next in Lesson 7, you'll learn to teach Claude your personal working style through custom instructions. Then Lessons 8-9 introduce **Agent Skills** — reusable expertise files that automate the patterns you've been practicing by hand.

**Pattern from skills:**
> You've built skills from scratch, tested them systematically, composed them into pipelines, and created complete skill suites for real scenarios. You've gone from understanding what a SKILL.md is to building production-ready skill libraries.
> Next in **Lesson 11: Subagents and Orchestration**, you'll learn how Claude delegates complex tasks to specialized sub-agents — the same skill composition principles you practiced here, but automated. Then in **Lesson 12: MCP Integration**, you'll connect your skills to external tools and services through the Model Context Protocol.

---

## Template: Summary File (.summary.md)

```markdown
{{SUMMARY_PARAGRAPH_1}}
<!-- Paragraph 1: What the lesson provides (exercise count, module count, bridge description).
     Name the core skills/competencies with bold formatting.
     Reference the framework by name. -->

{{SUMMARY_PARAGRAPH_2}}
<!-- Paragraph 2: Describe the module progression from concrete to open-ended.
     List all 8 modules by name in a comma-separated sequence. -->

{{SUMMARY_PARAGRAPH_3}}
<!-- Paragraph 3: Self-assessment method and what students are prepared for next.
     Reference the rubric criteria count.
     State what the next lessons are. -->
```

**Pattern notes:**
- 3 paragraphs, no headings, no YAML frontmatter
- Paragraph 1: Scope + core skills (bold)
- Paragraph 2: Framework name + module progression
- Paragraph 3: Assessment + what's next
- Basics summary: ~9 lines; Skills summary: ~5 lines
- Keep concise — this is a summary, not an abstract

---

## Complete Structural Skeleton

For quick reference, this is the full document structure:

```
---
[YAML Frontmatter]
---

# {{LESSON_TITLE}}                          ← H1

[Opening Narrative: 2-3 paragraphs]

:::info Download Exercise Files              ← Admonition
[Download link + fallback]
:::

---

## How to Use These Exercises               ← H2
[Numbered workflow steps]

---

## Tool Guide                               ← H2
[Tool descriptions with indicators]

---

## {{Framework Name}}                       ← H2
[5-7 step framework]

---

## {{Rubric Title}}                         ← H2
[Criteria table: 5-6 rows x 4 levels]

---

## Module 1: {{Title}}                      ← H2
> **Core Skill:** {{description}}

### Exercise 1.1 — {{Title}}               ← H3
[The Problem / Your Task / What You'll Learn / Prompts / Reflection]

---

### Exercise 1.2 — {{Title}}               ← H3
...

---

### Exercise 1.3 — {{Title}}               ← H3
...

---

## Module 2: {{Title}}                      ← H2
...

[Modules 3-7 follow same pattern]

## Module 8: Capstone Projects              ← H2
> Choose one (or more)...

### Capstone A — {{Title}}                  ← H3
### Capstone B — {{Title}}                  ← H3
### Capstone C — {{Title}}                  ← H3

---

## What's Next                              ← H2
[Summary + preview of next lessons]
```

---

## Sizing Guidelines

| Component | Count | Source |
| --- | --- | --- |
| Modules (including capstone) | 8 | Both lessons use 8 |
| Exercises per module (Modules 1-7) | 3 | Both use 3 per module |
| Capstone projects (Module 8) | 3 | Both use 3 (A, B, C) |
| Total exercises | 27 | 21 regular + 3 capstones = 24 minimum; some count capstones in the 27 |
| Skills in YAML | 3 | Both use 3 |
| Learning objectives | 3-4 | Basics: 3, Skills: 4 |
| Rubric criteria | 5-6 | Basics: 5, Skills: 6 |
| Rubric levels | 4 | Both: Beginner/Developing/Proficient/Advanced |
| Reflection questions per exercise | 3 | Consistent across both |
| "What You'll Learn" bullets | 3 | Consistent across both |
| Target lesson length | ~800-860 lines | Basics: 856, Skills: 823 |
