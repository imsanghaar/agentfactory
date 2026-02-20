---
slug: /General-Agents-Foundations/general-agents/basics-exercises
title: "Practical Problem-Solving Exercises"
practice_exercise: ch3-basics
sidebar_position: 6
chapter: 3
lesson: 6
duration_minutes: 120

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on practice applying Lessons 01-05 concepts through 27 guided exercises"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Problem Decomposition"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can break vague problems into clear, actionable specifications for an AI agent"
  - name: "Specification Writing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can write clear outcome descriptions that produce predictable AI agent results"
  - name: "Quality Verification"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can verify AI output against specifications and iterate to improve results"

learning_objectives:
  - objective: "Decompose vague real-world problems into clear specifications for AI agents"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Completion of exercises with progressively better prompts"
  - objective: "Write outcome-focused instructions that produce predictable AI results"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Quality of prompts written across 8 exercise modules"
  - objective: "Verify AI output against requirements and iterate to improve"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Self-assessment using the 5-criteria rubric"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (problem decomposition, specification writing, quality verification) — within A2 limit. Exercises reinforce existing L01-L05 knowledge."

differentiation:
  extension_for_advanced: "Complete all 3 capstone projects; attempt exercises with minimal prompts"
  remedial_for_struggling: "Start with Module 1 only; use the starter prompts provided"

# TEACHING GUIDE METADATA (visible to teacher role only)
teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Practical Exercises and Problem Solving"
  key_points:
    - "The three skills (problem decomposition, specification writing, quality verification) are the meta-skills — exercises are vehicles, not the destination"
    - "The 5-criteria rubric (Problem Clarity, Specification Quality, Output Verification, Iteration, Reflection) should be introduced before students touch any exercise"
    - "Modules 1-4 require only Lesson 04 knowledge; Modules 5-8 require CLAUDE.md from Lesson 05 — this is a natural split point for pacing"
    - "The progression from intentionally vague starter prompts to better prompts is where the actual learning happens"
  misconceptions:
    - "Students think the goal is to complete all 27 exercises — the goal is to internalize the three core skills, even if they only complete 5 exercises deeply"
    - "Students copy-paste the starter prompts and call it done — the starter prompts are intentionally vague to show why specification quality matters"
    - "Students skip the reflection questions — these are where metacognition happens and must be treated as mandatory, not optional"
    - "Students think 'better prompt' means 'longer prompt' — it means more specific success criteria, not more words"
  discussion_prompts:
    - "After Exercise 1.1, what surprised you about the gap between what you meant and what Claude delivered?"
    - "In the Prompt Tournament (7.3), which style felt most natural to you — and does that match which produced the best results?"
    - "How would you teach the problem decomposition framework to someone who has never used AI?"
  teaching_tips:
    - "Assign Module 1 as the mandatory minimum — Exercise 1.1 (Messy Downloads) produces the fastest visible results and builds immediate confidence"
    - "For the rubric, have students self-score their first exercise, then peer-score a classmate's work — the calibration gap is itself a teaching moment"
    - "Do NOT let students skip the 'run it twice' step in exercises — the comparison between first and refined prompt is where the insight lives"
    - "The Capstone projects work best as group assignments where students divide deliverables and must integrate them — this mirrors real agent orchestration"
  assessment_quick_check:
    - "Ask students to explain the 7-step problem-solving framework from memory"
    - "Have students show their Module 1 Exercise 1.1 prompt — compare who used outcome-focused vs step-by-step instructions"
    - "Ask: What is the difference between a vague prompt and a bad prompt?"
---

# Practical Problem-Solving Exercises

You understand how AI agents work, how to communicate with them through CLAUDE.md. That's real knowledge — but knowledge without practice is just potential.

These exercises close the gap between "I understand AI agents" and "I can use AI agents to solve real problems." Each one gives you a messy, realistic situation and asks you to figure out how to describe it clearly enough for Claude to solve. The learning happens in that gap — between a vague problem and a precise specification.

Three skills run through every exercise: **problem decomposition** (breaking vague problems into clear steps), **specification writing** (describing outcomes precisely enough for an agent to execute), and **quality verification** (checking whether the output actually solves your problem). These aren't abstract concepts. By the end of these exercises, they'll be reflexes.

:::info Download Exercise Files
**[Download Basics Exercises (ZIP)](https://github.com/imsanghaar/claude-code-basic-exercises/releases/latest/download/basics-exercises.zip)**

After downloading, unzip the file. Each exercise has its own folder with an `INSTRUCTIONS.md` and any starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/imsanghaar/claude-code-basic-exercises/releases) directly.
:::

---

## How to Use These Exercises

The workflow for every exercise is the same:

1. **Open the exercise folder** from the `claude-code-basic-exercises/` directory
2. **Read the INSTRUCTIONS.md** inside the folder — it has setup steps and starter files
3. **Read the walkthrough below** for context on what you're practicing and why
4. **Start Claude Code or Cowork** and point it at the exercise folder
5. **Work through the exercise** — write your own prompts, don't just copy the starter
6. **Reflect** using the questions provided — this is where the real learning happens

You don't need to complete all 27 in one sitting. Work through one module at a time. Each module targets a different real-world skill.

---

## Tool Guide

- 🖥️ = **Claude Code** (terminal-based, for students comfortable with the command line)
- 🗂️ = **Cowork** (desktop app — point it at a folder and describe the task)
- Most exercises work with either tool. Start with whichever you're comfortable with.

---

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

---

## Assessment Rubric

For each exercise, evaluate yourself on:

| Criteria                  | Beginner (1)                     | Developing (2)                | Proficient (3)                 | Advanced (4)                     |
| ------------------------- | -------------------------------- | ----------------------------- | ------------------------------ | -------------------------------- |
| **Problem Clarity**       | Copied the starter prompt as-is  | Added some specifics          | Defined clear success criteria | Anticipated edge cases           |
| **Specification Quality** | Vague, one-sentence instructions | Multiple requirements listed  | Structured, unambiguous specs  | Reusable, parameterized specs    |
| **Output Verification**   | Accepted first output            | Checked if output looks right | Verified against requirements  | Tested edge cases and refined    |
| **Iteration**             | Single attempt                   | Made one revision             | Multiple refinements           | Developed a systematic approach  |
| **Reflection**            | None                             | Noted what happened           | Explained why it happened      | Derived principles for next time |

---

## Module 1: File Organization & Digital Housekeeping

> **Core Skill:** Turning chaos into structure by describing organizational rules clearly.

<ExerciseCard id="1.1" title="The Messy Downloads Folder" />

### Exercise 1.1 — The Messy Downloads Folder 🗂️🖥️

**The Problem:**
Open the `messy-downloads/` folder in the exercise directory. You'll find 35+ files of mixed types: PDFs, images (.jpg, .png), Word docs, spreadsheets, text files, and a few random files (.zip, .csv). The names are deliberately inconsistent — some with dates, some without, some with spaces, some with underscores.

**Your Task:**
Write a single clear instruction that tells Claude to organize these files into a logical folder structure. Don't tell Claude _how_ to organize — describe the _outcome_ you want.

**What You'll Learn:**

- Vague instructions produce unpredictable results
- The more specific your outcome description, the better the result
- Claude will make reasonable assumptions — but _your_ assumptions may differ from Claude's

**Starter Prompt (Intentionally Vague):**

> "Organize these files."

**Better Prompt (Build Toward This):**
Think about: What categories make sense? Should files be sorted by type, by date, by topic, or some combination? Should there be a naming convention? What should happen with duplicates?

**Reflection Questions:**

1. Did Claude organize the files the way you expected? If not, what was different?
2. What did you forget to specify that would have changed the result?
3. Rewrite your prompt and run it again. Is the second result better?

---

<ExerciseCard id="1.2" title="Photo Album Builder" />

### Exercise 1.2 — Photo Album Builder 🗂️🖥️

**The Problem:**
Open the `photos/` folder in the exercise directory. You'll find 24 images with a mix of portrait and landscape orientations, including some duplicates and near-duplicates.

**Your Task:**
Ask Claude to:

- Sort images by orientation (portrait vs landscape)
- Identify and flag potential duplicates
- Create a simple HTML gallery page that displays all images as thumbnails with filenames
- Generate a summary report of what was found

**What You'll Learn:**

- When to give Claude autonomy vs. when to be prescriptive
- How Claude handles multi-step tasks differently based on instruction style
- The tradeoff between control and efficiency

**The Twist:**
Write your instructions in TWO different ways:

1. **Outcome-focused:** "I want a photo gallery organized by orientation with duplicates flagged."
2. **Step-by-step:** Give Claude explicit sequential instructions for each sub-task.

Compare the results. Which approach produced a better outcome? Which was faster?

---

<ExerciseCard id="1.3" title="The Inbox Zero Challenge" />

### Exercise 1.3 — The Inbox Zero Challenge 🗂️

**The Problem:**
Open the `inbox/` folder in the exercise directory. You'll find 18 text files, each simulating an email (subject line on line 1, sender on line 2, body below). They include a mix of categories: work requests, personal messages, newsletters, receipts, spam-like content, and urgent items.

**Your Task:**
Ask Claude to triage these "emails" into action categories:

- **Respond Today** — Urgent or time-sensitive
- **This Week** — Important but not urgent
- **Read Later** — Informational, no action needed
- **Archive** — Receipts, confirmations
- **Delete** — Spam or irrelevant

Claude should move each file into the appropriate folder AND create a summary document listing each email, its category, and a one-line reason for the classification.

**What You'll Learn:**

- How to define classification criteria clearly
- That judgment-based tasks require you to define _your_ priorities, not just categories
- The importance of asking for Claude's reasoning (the "why" behind each decision)

**Reflection Questions:**

1. Did Claude's classification match your expectations?
2. Were there emails that could reasonably go in multiple categories? How did you handle that ambiguity in your prompt?
3. If you ran this weekly, what would you change to make the process repeatable?

---

## Module 2: Research & Information Synthesis

> **Core Skill:** Turning a broad question into a structured research task with clear deliverables.

<ExerciseCard id="2.1" title="The Comparison Matrix" />

### Exercise 2.1 — The Comparison Matrix 🗂️🖥️

**The Problem:**
You need to choose between 3-4 options for something (examples: laptop brands, programming languages to learn first, cities to relocate to, project management tools for a small team).

**Your Task:**
Ask Claude to:

1. Research each option
2. Create a comparison table (as a spreadsheet or formatted document) with consistent criteria
3. Write a 1-page recommendation memo with pros/cons
4. Save everything to your working folder

**What You'll Learn:**

- Research quality depends on how well you define what you're looking for
- The same question with different criteria produces completely different recommendations
- How to structure comparison tasks for maximum usefulness

**Starter Prompt (Intentionally Vague):**

> "Compare React, Vue, and Angular for me."

**Better Prompt (Build Toward This):**
Define your context (team size, experience level, project type) and what factors matter (learning curve, community support, job market, performance, etc.). Include 5-7 specific comparison criteria before Claude starts researching.

**Reflection Questions:**

1. How did your choice of comparison criteria change the recommendation?
2. Would a different person with different priorities get a different recommendation from the same data?
3. What criteria did you forget that you'd add next time?

---

<ExerciseCard id="2.2" title="The Literature Review" />

### Exercise 2.2 — The Literature Review 🗂️🖥️

**The Problem:**
Pick a topic you're genuinely curious about (examples: intermittent fasting, remote work productivity, microplastics in water, the future of nuclear energy).

**Your Task:**
Ask Claude to produce a structured literature review document with:

- An executive summary (3-4 sentences)
- Key findings organized by theme (not by source)
- Areas of consensus vs. areas of debate
- A "what we still don't know" section
- All sources cited properly

**What You'll Learn:**

- The difference between "find information" and "synthesize knowledge"
- How specifying audience dramatically changes output quality
- Iterative refinement as a core problem-solving skill

**The Challenge:**
Do this in TWO rounds:

1. First, give Claude just the topic and see what it produces
2. Then, refine your prompt: specify the depth, the audience (explain it like I'm a college student vs. a domain expert), and any angles you specifically want covered

Compare the two outputs. The difference illustrates why specification quality matters.

---

<ExerciseCard id="2.3" title="The Decision Document" />

### Exercise 2.3 — The Decision Document 🗂️🖥️

**The Problem:**
You're facing a real decision in your life or work (or simulate one): Should you learn AI or stick with traditional development? Should your team adopt a new tool? Should you start a side project?

**Your Task:**
Ask Claude to create a structured decision document:

- Frame the decision as a clear question
- List assumptions and constraints
- Analyze 2-3 options with evidence
- Include a risk assessment for each option
- End with a recommended path forward and next steps
- Save as a polished document

**What You'll Learn:**

- How to externalize your thinking into a structured format
- That framing the question correctly is half the battle
- How to use AI as a thinking partner, not just an answer machine

**Reflection Questions:**

1. Did the decision document change your thinking about the problem?
2. Was the recommended path what you expected? If not, was the reasoning sound?
3. How would you change the document structure for a different type of decision?

---

## Module 3: Data Wrangling & Analysis (No Coding Required)

> **Core Skill:** Describing data transformations in plain English and verifying results.

<ExerciseCard id="3.1" title="The Messy Spreadsheet" />

### Exercise 3.1 — The Messy Spreadsheet 🗂️🖥️

**The Problem:**
Open `customer_data_messy.csv` in the exercise directory. It contains deliberately messy data:

- Inconsistent date formats (01/15/2025, Jan 15 2025, 2025-01-15)
- Mixed case names (john smith, JANE DOE, Bob Jones)
- Missing values in some rows
- Duplicate entries
- Phone numbers in different formats

**Your Task:**
Ask Claude to:

1. Clean and standardize all data
2. Remove duplicates
3. Flag rows with missing critical information
4. Export a clean version AND a report of all changes made

**What You'll Learn:**

- How to describe data quality rules in plain language
- The importance of a "dry run" before irreversible changes
- How to verify that cleaning didn't accidentally remove good data

**Starter Prompt (Intentionally Vague):**

> "Clean up this spreadsheet."

**Better Prompt (Build Toward This):**
Include a critical instruction: "Before making changes, show me what you plan to do and get my approval." This teaches the crucial skill of requiring a preview before execution. Specify which date format you want, how names should be capitalized, and what counts as a "duplicate."

**Reflection Questions:**

1. Did Claude's "clean" version match your definition of clean?
2. What rules did you have to make explicit that you assumed were obvious?
3. Why is "show me the plan first" such an important instruction for data tasks?

---

<ExerciseCard id="3.2" title="The Survey Analyzer" />

### Exercise 3.2 — The Survey Analyzer 🗂️🖥️

**The Problem:**
Open `product_survey_results.csv` in the exercise directory. It contains 50+ rows of survey data with:

- Demographic columns (age range, location, role)
- Likert scale responses (1-5) for 5-6 questions
- One open-text feedback column

**Your Task:**
Ask Claude to:

1. Calculate summary statistics for each question
2. Find interesting patterns (e.g., do certain demographics rate things differently?)
3. Categorize the open-text feedback into themes
4. Create a visual summary report with charts
5. Write a 1-page "key findings" memo suitable for sharing with a non-technical manager

**What You'll Learn:**

- How to describe analysis goals without specifying statistical methods
- That "find interesting patterns" requires you to define what "interesting" means to you
- How to request different output formats for different audiences

**Reflection Questions:**

1. Did Claude find patterns you didn't expect?
2. Was the "key findings" memo actually useful for a non-technical audience?
3. What would you change about the analysis if you were doing it for a different stakeholder?

---

<ExerciseCard id="3.3" title="The Budget Tracker" />

### Exercise 3.3 — The Budget Tracker 🗂️🖥️

**The Problem:**
Open the `receipts/` folder in the exercise directory. You'll find 15 receipt text files, each representing a purchase (date, vendor, amount, category). Some have overlapping categories.

**Your Task:**
Ask Claude to:

1. Extract key information from each receipt
2. Create a consolidated spreadsheet with all transactions
3. Categorize spending (food, transport, entertainment, etc.)
4. Calculate totals by category and create a simple chart
5. Flag any unusually large expenses
6. Generate a monthly spending summary report

**What You'll Learn:**

- How to describe an extraction + aggregation pipeline in natural language
- The importance of defining categories upfront vs. letting Claude infer them
- How to chain multiple transformations together in one task description

**Reflection Questions:**

1. Did Claude's categories match the ones you had in mind?
2. Where did Claude struggle with ambiguous receipts?
3. How would this workflow change if you had 100 receipts instead of 15?

---

## Module 4: Document Creation & Transformation

> **Core Skill:** Turning raw information into polished, professional deliverables.

<ExerciseCard id="4.1" title="The Meeting Notes Transformer" />

### Exercise 4.1 — The Meeting Notes Transformer 🗂️🖥️

**The Problem:**
Open `raw_meeting_notes.txt` in the exercise directory. It contains raw, messy meeting notes — bullet fragments, abbreviations, incomplete sentences, off-topic tangents, action items buried in discussion.

**Your Task:**
Ask Claude to transform these notes into THREE different outputs:

1. **Clean meeting minutes** — Formal, organized by topic, with clear decisions listed
2. **Action items list** — Who, what, by when — extracted from the discussion
3. **Executive summary email** — 3-paragraph summary suitable for someone who missed the meeting

**What You'll Learn:**

- How to specify multiple output formats from a single input
- The importance of consistency constraints
- How different audiences need the same information in different forms

**Starter Prompt (Intentionally Vague):**

> "Clean up these meeting notes."

**Better Prompt (Build Toward This):**
Include the constraint: "All three outputs must be consistent — the same decisions and action items should appear across all formats." Specify what counts as an "action item" and how you want the executive summary structured.

**Reflection Questions:**

1. Were the three outputs consistent with each other?
2. Did the executive summary capture the right level of detail for someone who missed the meeting?
3. What would you add to your specification to handle notes from recurring meetings?

---

<ExerciseCard id="4.2" title="The Report Generator" />

### Exercise 4.2 — The Report Generator 🗂️🖥️

**The Problem:**
Open the `project-data/` folder in the exercise directory. You'll find 5 data files (CSVs and text files with notes) related to a hypothetical product launch project.

**Your Task:**
Ask Claude to synthesize all materials into a single professional report with:

- Title page
- Table of contents
- Executive summary
- Findings organized by theme (not by source file)
- Data visualizations where appropriate
- Recommendations section
- Appendix with raw data references

**What You'll Learn:**

- How to describe document structure and formatting expectations
- How Claude handles multi-source synthesis
- The difference between "combine these files" and "synthesize these into a narrative"

**Reflection Questions:**

1. Did Claude organize findings by theme or just summarize each file?
2. Were the recommendations supported by the data in the report?
3. What formatting details did you forget to specify?

---

<ExerciseCard id="4.3" title="The Presentation Builder" />

### Exercise 4.3 — The Presentation Builder 🗂️🖥️

**The Problem:**
Open `written_report.md` in the exercise directory (or use the output you generated in Exercise 4.2).

**Your Task:**
Ask Claude to create a presentation that:

- Distills the document into 8-12 slides
- Has a clear narrative arc (problem → findings → recommendations)
- Includes speaker notes for each slide
- Uses data visualizations instead of text walls
- Follows a consistent visual theme

**What You'll Learn:**

- How to specify "distill" vs. "copy-paste into slides"
- The skill of giving constructive feedback to an AI agent
- That revision is where quality happens

**The Meta-Exercise:**
After Claude creates the presentation, write a critique of it. What would you change? Then ask Claude to revise based on your feedback. This teaches iterative refinement — the same skill you'll use in every professional AI workflow.

---

## Module 5: Process Automation & Workflows

> **Core Skill:** Identifying repetitive patterns and describing them as repeatable processes.

<ExerciseCard id="5.1" title="The Batch Renamer" />

### Exercise 5.1 — The Batch Renamer 🗂️🖥️

**The Problem:**
Open the `files-to-rename/` folder in the exercise directory. You'll find 25+ files with inconsistent naming that need standardization. Examples of what you'll see:

- `IMG_20250115_143022.txt` — timestamps embedded in names
- `Document (1).txt` — generic numbered duplicates
- Mixed naming conventions throughout

**Your Task:**
Define a naming convention and ask Claude to rename all files according to your rules. Your rules must cover:

- Date format preference
- How to handle files without dates
- Separator character (hyphen, underscore, etc.)
- What to do with duplicate names after renaming
- Whether to preserve original names somewhere (e.g., a log file)

**What You'll Learn:**

- How to define rules that handle edge cases
- The importance of thinking about "what if" scenarios in your specifications
- Why a log/undo mechanism matters for batch operations

**Reflection Questions:**

1. Did your naming rules handle every file, or were there edge cases you didn't anticipate?
2. What would happen if you ran the same rename again — would it cause problems?
3. How would you modify your specification to make it idempotent (safe to run repeatedly)?

---

<ExerciseCard id="5.2" title="The Template System" />

### Exercise 5.2 — The Template System 🗂️🖥️

**The Problem:**
You need to send personalized versions of the same document to multiple people.

**Your Task:**

1. Open the exercise directory — you'll find `certificate_template.md` (a template with placeholder fields like `{{NAME}}`, `{{DATE}}`, `{{SCORE}}`) and `student_data.csv` (data for each recipient)
2. Review both files to understand the template + data pattern
3. Ask Claude to generate all personalized documents

**What You'll Learn:**

- How to think in terms of templates + data = output
- The separation of content from presentation
- How to describe a "mail merge" style workflow in natural language

**The Extension:**
After generating documents, ask Claude to create a tracking spreadsheet that lists each recipient, their document filename, and a status column (ready to send / needs review).

**Reflection Questions:**

1. Were all 10 documents correct? Did any have missing or wrong data?
2. How did you handle recipients with special characters or missing fields?
3. Could you reuse this template + data approach for other tasks?

---

<ExerciseCard id="5.3" title="The Weekly Report Automator" />

### Exercise 5.3 — The Weekly Report Automator 🗂️🖥️

**The Problem:**
Imagine you need to produce a weekly status report every Friday. The report pulls from three input files.

**Your Task:**
Open the `week-data/` folder in the exercise directory. You'll find all three input files: `tasks.csv` (tasks, status, owner, due date), `metrics.csv` (numbers like users, revenue, bugs fixed), and `weekly_notes.txt` (free-text highlights and blockers). Write a single comprehensive prompt that:

1. Reads all three files
2. Generates a formatted weekly report document
3. Highlights overdue tasks in red
4. Calculates week-over-week changes in metrics
5. Formats everything into a professional document ready to email

**What You'll Learn:**

- How to write specifications that are reusable, not one-shot
- The concept of separating "data that changes" from "process that stays the same"
- This is the foundation of thinking in systems, not tasks

**The Goal:**
Your prompt should be reusable — if you updated the three input files next week and ran the same prompt, it should produce a new report without modification. Test this by changing the data and running the same prompt again.

---

## Module 6: Problem Solving & Creative Thinking

> **Core Skill:** Using Claude as a thinking partner for open-ended problems.

<ExerciseCard id="6.1" title="The Business Plan Skeleton" />

### Exercise 6.1 — The Business Plan Skeleton 🗂️🖥️

**The Problem:**
Open the exercise directory — you'll find starter idea briefs (like an AI tutoring service, a local food delivery app, or a coworking space). Pick one that interests you, or use your own idea. The exercise is about structuring your thinking, not the idea itself.

**Your Task:**
Ask Claude to help you create:

1. A one-page business concept document
2. A basic financial projection spreadsheet (startup costs, monthly expenses, revenue estimates)
3. A competitor analysis table
4. A simple action plan with milestones

**What You'll Learn:**

- That problem-solving is iterative, not one-shot
- How to use AI as a collaborator, not just an executor
- The value of "what questions should I be asking?" as a prompt

**Starter Prompt (Intentionally Vague):**

> "Write me a business plan."

**Better Prompt (Build Toward This):**
Don't just say "write me a business plan." Instead, have a CONVERSATION with Claude: start with the idea, let Claude ask you clarifying questions (or anticipate what questions matter), iterate on each section, and challenge Claude's assumptions.

**Reflection Questions:**

1. Did Claude's questions help you think about angles you hadn't considered?
2. Were the financial projections realistic? How would you verify them?
3. What's the difference between asking for a document and having a conversation that produces a document?

---

<ExerciseCard id="6.2" title="The Troubleshooter" />

### Exercise 6.2 — The Troubleshooter 🗂️🖥️

**The Problem:**
Open the exercise directory — you'll find starter problem scenarios (like a website traffic drop, declining course engagement, or unproductive team meetings). Pick one that resonates with you, or describe a real problem you're facing.

**Your Task:**
Ask Claude to:

1. Identify possible root causes (aim for at least 5)
2. For each root cause, suggest a diagnostic test (how would you verify this is the real cause?)
3. Rank the causes by likelihood and ease of testing
4. Create an investigation plan starting with the quickest/cheapest tests
5. Save everything as a structured problem-solving document

**What You'll Learn:**

- Systematic problem diagnosis (don't jump to solutions)
- The concept of "cheapest test first"
- How to structure uncertainty into an actionable plan

**Reflection Questions:**

1. Did the root cause analysis surface causes you hadn't thought of?
2. Is the investigation plan actually actionable — could you follow it tomorrow?
3. How does "cheapest test first" change your approach to problem-solving?

---

<ExerciseCard id="6.3" title="The Event Planner" />

### Exercise 6.3 — The Event Planner 🗂️🖥️

**The Problem:**
Open `event-brief.md` in the exercise directory for a starter event scenario, or plan your own realistic event: a team offsite, a community meetup, a workshop for 30 students, or a small conference.

**Your Task:**
Ask Claude to produce a complete event planning package:

1. **Timeline** — Backward plan from event date with all preparation milestones
2. **Budget spreadsheet** — Itemized costs with totals
3. **Checklist** — All tasks grouped by category (venue, food, tech, communications)
4. **Communications** — Draft invitation email, reminder email, and follow-up survey
5. **Day-of schedule** — Minute-by-minute run sheet
6. **Contingency plan** — "What if" scenarios with backup plans

**What You'll Learn:**

- Comprehensive planning requires specifying deliverables, not just topics
- How constraints force creative problem-solving
- The skill of adapting existing plans rather than starting from scratch

**The Twist:**
After Claude generates everything, introduce a constraint change: "The budget just got cut by 30%" or "The venue changed" or "We need to add 20 more people." See how Claude adapts the existing plan rather than starting over.

---

## Module 7: Quality Control & Critical Thinking

> **Core Skill:** Not blindly trusting AI output — learning to verify, critique, and improve.

<ExerciseCard id="7.1" title="The Fact Checker" />

### Exercise 7.1 — The Fact Checker 🗂️🖥️

**The Problem:**
Ask Claude to write a 500-word article about a topic you know well. Then deliberately look for errors.

**Your Task:**

1. Have Claude generate the article
2. Read it carefully and identify any claims that seem wrong, vague, or unverifiable
3. Create a "fact-check report" listing each questionable claim and what you found when you verified it
4. Ask Claude to correct the article based on your findings

**What You'll Learn:**

- AI outputs can sound confident but be wrong
- Fact-checking is a skill that humans MUST provide
- How to give specific, actionable correction feedback

**Reflection Questions:**

1. How many claims did you question? How many turned out to be inaccurate?
2. Were the errors subtle (slightly wrong numbers) or significant (completely wrong claims)?
3. How does this exercise change how you'll read AI output in the future?

---

<ExerciseCard id="7.2" title="The Specification Stress Test" />

### Exercise 7.2 — The Specification Stress Test 🖥️

**The Problem:**
Write a set of instructions for Claude to create a specific file (a formatted document, an organized folder structure, a data report — pick one). Make your instructions as clear as you can.

**Your Task:**

1. Give your instructions to Claude and get the output
2. Now, give the SAME instructions to a classmate (or re-read them as a stranger would)
3. Identify all the ambiguities — places where two people might interpret the instructions differently
4. Rewrite the instructions to eliminate ambiguity
5. Run the improved instructions through Claude and compare results

**What You'll Learn:**

- Writing clear specifications is genuinely hard
- Ambiguity is the #1 source of "the AI didn't do what I wanted"
- This skill transfers directly to working with AI agents, managing teams, and writing requirements

**Reflection Questions:**

1. How many ambiguities did you find in your "clear" instructions?
2. Did the improved instructions produce a noticeably better result?
3. What's the most common type of ambiguity you discovered?

---

<ExerciseCard id="7.3" title="The Prompt Tournament" />

### Exercise 7.3 — The Prompt Tournament 🖥️🗂️

**The Problem:**
Pick any task from the previous exercises. Write THREE different prompts to accomplish the same task:

1. **Minimal** — The shortest prompt you think could work
2. **Detailed** — A comprehensive prompt with all specifications
3. **Conversational** — Achieve the same result through a multi-turn conversation

**Your Task:**
Run all three approaches and compare:

- Which produced the best result?
- Which was fastest?
- Which gave you the most control?
- Which was most enjoyable to use?

Create a comparison document with examples from each approach.

**What You'll Learn:**

- There's no single "right way" to prompt
- Different situations call for different approaches
- Finding your personal prompting style is part of the learning process

**Reflection Questions:**

1. Was the minimal prompt surprisingly effective, or did it fail?
2. Did the detailed prompt produce exactly what you wanted, or was it over-specified?
3. Which approach would you use for a quick task vs. a high-stakes deliverable?

---

## Module 8: Capstone Projects

> **Choose one (or more). Spend real time on it. This is where everything comes together.**

Capstones are different from the exercises above. There are no starter prompts — you design the entire approach yourself. These are open-ended projects that require you to combine problem decomposition, specification writing, and quality verification into a complete workflow.

<ExerciseCard id="A" title="The Personal Knowledge Base" />

### Capstone A — The Personal Knowledge Base 🗂️🖥️

Open the `sample-documents/` folder in the exercise directory — you'll find 8 starter documents (articles, notes, bookmarks). You can add your own documents to the folder for a richer experience. Ask Claude to:

- Read and categorize everything
- Extract key insights from each document
- Create a searchable index (as a markdown file or spreadsheet)
- Generate a "connections map" — which documents relate to each other and why
- Write a personal summary: "Here's what you seem most interested in, and here are gaps in your knowledge"

**What You'll Learn:**

- How to describe a multi-phase workflow from start to finish
- Synthesis across many documents
- Getting Claude to make non-obvious connections

---

<ExerciseCard id="B" title="The Small Business Operations Kit" />

### Capstone B — The Small Business Operations Kit 🗂️🖥️

Create a complete operational toolkit for a hypothetical small business:

- Invoice template (with auto-calculations)
- Client tracking spreadsheet
- Weekly metrics dashboard
- Standard email templates (inquiry response, follow-up, thank-you)
- Monthly reporting template
- A simple operations manual document

All files should be consistent in branding and cross-reference each other.

**What You'll Learn:**

- How to maintain consistency across multiple deliverables
- The challenge of cross-referencing between documents
- Designing systems of documents, not individual files

---

<ExerciseCard id="C" title="The Course Material Generator" />

### Capstone C — The Course Material Generator 🗂️🖥️

Take any topic you understand well. Ask Claude to create:

- A 5-lesson course outline
- Detailed lesson plans for each session
- A student worksheet/exercise for each lesson
- A quiz with answer key
- A reading list with summaries
- A presentation deck for one of the lessons

Everything should be coherent, progressive (each lesson builds on the last), and saved as properly formatted files.

**What You'll Learn:**

- How to specify progressive structure (each piece builds on the last)
- The difficulty of maintaining coherence across many documents
- Quality control when output volume is high

---

## What's Next

You've practiced the three core skills — problem decomposition, specification writing, and quality verification — across 27 exercises. These skills compound: every exercise makes the next one easier because you're building intuition for how to communicate with AI agents. Next in Lesson 7, you'll learn to teach Claude your personal working style through custom instructions. Then Lessons 8-9 introduce **Agent Skills** — reusable expertise files that automate the patterns you've been practicing by hand.
