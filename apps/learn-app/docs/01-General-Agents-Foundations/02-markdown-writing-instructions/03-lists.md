---
title: "Lists - Organizing Ideas"
description: "Learning to use unordered and ordered lists to structure requirements and sequential steps"
sidebar_label: "Lists - Organizing Ideas"
sidebar_position: 3
chapter: 2
lesson: 3
duration_minutes: 40
proficiency: "A2"
concepts: 3

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Creating Unordered Lists"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can create bullet lists to organize features and requirements"

  - name: "Creating Ordered Lists"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can create numbered lists for sequential steps"

  - name: "Choosing Appropriate List Type"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can determine when to use unordered vs ordered lists based on context"

learning_objectives:
  - objective: "Create unordered lists using dash or asterisk syntax"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Practice exercise creating feature lists"

  - objective: "Create ordered lists for sequential steps"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Practice exercise creating installation instructions"

  - objective: "Select correct list type based on content purpose"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Decision-making exercise analyzing when each type is appropriate"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (unordered lists, ordered lists, selection principle) within A2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Learn nested lists (lists within lists); explore complex list formatting; practice mixing list types appropriately"
  remedial_for_struggling: "Master unordered lists first before ordered; use simple 3-item lists; practice with provided templates"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Lists, Code Blocks & Specification Detail"
  key_points:
    - "The 'Does order matter?' question is the entire decision framework for list types — make students internalize this before teaching syntax"
    - "Unordered lists signal independent items (AI can implement in any order); ordered lists signal dependencies (AI must follow sequence)"
    - "Nested lists (2-space indent) handle sub-requirements without creating more headings — prevents heading bloat in specifications"
  misconceptions:
    - "Students use numbered lists for features because numbering 'looks more organized' — emphasize that numbers imply required sequence to AI agents"
    - "Students forget the space after dash or number — same syntax pattern as forgetting the space after # in Lesson 2, worth calling out as recurring"
    - "Students think unordered means 'less important' than ordered — it means 'no required sequence,' which is different from priority"
  discussion_prompts:
    - "Think about your morning routine. Which steps must happen in order (shower before dress) and which can happen in any order (check phone, eat breakfast)? How would you list each type?"
    - "If an AI sees a numbered list of features, what might it do differently than if it sees bullet points for the same features?"
  teaching_tips:
    - "Start with the opening paragraph-vs-list comparison — it mirrors Lesson 1's structured vs unstructured theme and reinforces the chapter's core idea"
    - "Use the installation steps example to show why sequence matters — ask 'what happens if you run the program before installing Python?'"
    - "The side-by-side examples (Features with bullets vs Setup with numbers) are a strong whiteboard moment for visual comparison"
    - "Connect the nested list tip to Lesson 2: headings create major sections, nested lists add detail within them"
  assessment_quick_check:
    - "Give students three items and ask whether they should be ordered or unordered, with reasoning"
    - "Ask students when to use nested lists vs adding a new heading level"

# Generation metadata
generated_by: "content-implementer v3.0.0"
source_spec: "specs/001-chapter-11-markdown/spec.md"
created: "2025-11-06"
last_modified: "2025-11-07"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.1"
---

# Lists - Organizing Ideas

Headings gave your document a skeleton. Now you need to fill it in — and that's where **lists** come in.

Imagine you're giving someone installation instructions in paragraph form:

> "First install Python version 3.9 or higher, then download the project files, after that install the required packages using pip, and finally run the program."

Now imagine the same information as a numbered list:

> 1. Install Python 3.9 or higher
> 2. Download the project files
> 3. Install required packages: `pip install requests`
> 4. Run the program: `python app.py`

The second version is instantly clearer. You can see at a glance that there are 4 steps, in a specific order.

Lists are essential in specifications because they help you present information clearly. When an AI agent reads a specification with proper lists, it immediately understands: "These are distinct items" or "These steps must happen in order."

This lesson teaches you two types of lists and when to use each.

---

## Concept 1: Unordered Lists (Bullet Points)

Use **unordered lists** when you have items that don't need to be in any specific order. In markdown, create them with a dash (`-`) or asterisk (`*`) followed by a space.

### Basic Syntax

```text
- First item
- Second item
- Third item
```

Or with asterisks or plus signs (same result):

```text
* First item
* Second item
* Third item

+ First item
+ Second item
+ Third item
```

**Tip**: Pick one style (`-`, `*`, or `+`) and stick with it throughout your document.

### Nested Lists

You can create sub-items by indenting with 2 spaces:

```text
- Main feature
  - Sub-feature A
  - Sub-feature B
- Another feature
  - Sub-feature C
```

:::note
Some markdown parsers require a blank line before lists to render correctly. If your list isn't rendering, add a blank line above it.
:::

### When to Use Unordered Lists

Use bullet points when:
- Items have no specific sequence
- Order doesn't matter for understanding
- You're listing features, requirements, or options
- Items are independent of each other

### Example: Feature List

Here's a feature list for a task tracker app:

```text
# Task Tracker App

## Features
- Add tasks with title and description
- View all tasks with completion status
- Mark tasks as complete or incomplete
- Delete tasks you no longer need
- Save tasks to file (persist between sessions)
```

**Why bullet points work here**: Each feature is independent. Whether "Add tasks" comes before or after "Delete tasks" doesn't change what the app needs to do. The AI can implement these features in any order.

#### 💬 AI Colearning Prompt

> **Explore with your AI**: "I'm learning when to use ordered vs unordered lists. Can you give me three examples of requirements that MUST be ordered lists (sequence matters) and three that should be unordered lists (sequence doesn't matter)? Use real software project examples."

---

## Concept 2: Ordered Lists (Numbered Steps)

Use **ordered lists** when items must be done in a specific sequence. In markdown, create them by typing `1.` followed by a space.

### Basic Syntax

```text
1. First step
2. Second step
3. Third step
```

:::note[Markdown Numbering Behavior]
Markdown auto-numbers based on the **first number** in the list. If you start with `11.`, the next items render as `12, 13, 14...` regardless of what you type:

```text
11. This renders as 11
2. This renders as 12 (not 2!)
3. This renders as 13
```

**For AI-native development**: Always use correct sequential numbers (`1. 2. 3.`) in your raw markdown. AI agents often read the source file directly, not the rendered HTML. Writing all `1.`s may confuse older models parsing your specification.
:::

### When to Use Ordered Lists

Use numbered lists when:
- Steps must be done in sequence
- Order matters for correctness
- You're showing installation steps, procedures, or workflows
- Each step depends on the previous one

### Example: Installation Steps

Here's installation instructions for a weather app:

```text
# Weather Dashboard

## Installation

1. Install Python 3.9 or higher from python.org
2. Download the project files
3. Navigate to the project folder: `cd weather-dashboard`
4. Install required packages: `pip install requests`
5. Run the program: `python weather.py`
```

**Why numbered steps work here**: You **must** install Python before you can install packages. You **must** navigate to the folder before running the program. The sequence matters.

### Example: Troubleshooting Steps

```text
## Troubleshooting: "Module Not Found" Error

If you see this error, try these steps in order:

1. Check that Python 3.9+ is installed: `python --version`
2. Verify you're in the correct folder: `pwd` (Mac/Linux) or `cd` (Windows)
3. Reinstall packages: `pip install --upgrade requests`
4. If still failing, delete venv folder and recreate it
```

The sequence matters here too — you check Python first, then location, then reinstall, then venv.

:::info[Expert Insight]
Notice how ordered lists communicate dependencies. In the installation example, step 2 depends on step 1 completing successfully. This dependency chain is critical for AI agents—they know they can't run the program before installing packages, and can't install packages before verifying Python exists. Clear sequencing prevents AI from generating incorrect workflows where steps run out of order.
:::

---

## Concept 3: Choosing the Right List Type

How do you know which type to use? Ask yourself: **Does order matter?**

### Decision Guide

**Use unordered lists (`-`) when:**
- Describing features of an app
- Listing requirements or constraints
- Showing options or alternatives
- Items can be done in any order

**Use ordered lists (`1.`) when:**
- Showing installation instructions
- Describing a workflow or process
- Giving troubleshooting steps
- Sequence affects outcome

### Examples Side by Side

**Unordered (order doesn't matter):**

```text
## Features
- Dark mode support
- Export to PDF
- Auto-save every 5 minutes
- Keyboard shortcuts
```

These features are independent. Adding dark mode doesn't require export to PDF first.

**Ordered (order matters):**

```text
## Setup Process
1. Create account
2. Verify email address
3. Set up profile
4. Start using the app
```

You **must** create an account before verifying email. You **must** verify email before setting up profile.

#### 🤝 Practice Exercise

> **Ask your AI**: "I'm writing a specification with these items:
> 1. App must run on Windows, Mac, and Linux
> 2. App must support dark mode and light mode
> 3. User must log in before accessing dashboard
> 4. User must verify email before account activation
>
> Which should be unordered lists (bullet points) and which should be ordered lists (numbered)? Explain your reasoning. Help me understand how to spot dependencies."

---

## Practice Exercise: Task Tracker App (Part 2 - Lists)

**Continuing from Lesson 2**: Open the Task Tracker App specification you created in Lesson 2. You'll now **add lists** to organize features and installation steps.

### Your Task for Lesson 3

Add two types of lists to your existing Task Tracker App structure:

**Part 1: Add Feature Descriptions (Unordered Lists)**

Under each Level 3 heading in the Features section, add bullet points describing what that feature does:

```text
## Features

### Add Tasks
- Create tasks with title and description
- Set optional due dates
- Assign priority levels (high, medium, low)

### View Tasks
- Display all tasks with status
- Filter by priority or due date
- Show completed and pending separately

### Mark Complete
- Mark tasks as done
- Track completion timestamps
- Move completed tasks to archive

### Delete Tasks
- Remove tasks permanently
- Confirm before deleting to prevent accidents
```

:::tip[Pro-Tip: Nested Lists vs. More Headings]
If a feature has sub-requirements, use **nested lists** instead of creating more Level 3 headings:

```text
### Add Tasks
- Create tasks with title and description
  - Title is required (max 100 characters)
  - Description is optional
- Set optional due dates
```

**Rule of thumb**: Use headings for major sections, nested lists for details within a section. If you find yourself creating 10+ Level 3 headings, consider consolidating with nested lists.
:::

**Part 2: Add Installation Steps (Ordered List)**

Fill in the Installation section with numbered steps:

```text
## Installation

1. Install Python 3.9 or higher from python.org
2. Download the task tracker files from GitHub
3. Navigate to the project folder: `cd task-tracker`
4. Run the program: `python tracker.py`
```

**Part 3: Add Problem Description**

Under the Problem section, describe what problem this app solves (1-2 sentences as a paragraph, not a list).

### Validation Checklist

Check your updated specification:

1. Feature descriptions use unordered lists (`-`) under each Level 3 heading
2. Installation uses ordered list (`1. 2. 3. 4.`)
3. Each list item starts with dash/number + space
4. Feature lists have no specific order (could be rearranged)
5. Installation steps must be done in sequence
6. Problem section is a paragraph (not a list)

**Save this file!** You'll add code blocks in Lesson 4.

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting the Space

**Wrong:**
```text
-No space after dash
1.No space after number
```

**Correct:**
```text
- Space after dash
1. Space after number
```

Always put a space after the dash or number.

### Mistake 2: Using Ordered Lists for Features

**Wrong (features don't need order):**
```text
## Features
1. Dark mode
2. Export to PDF
3. Auto-save
```

**Correct:**
```text
## Features
- Dark mode
- Export to PDF
- Auto-save
```

Features usually don't have a required order.

### Mistake 3: Using Unordered Lists for Steps

**Wrong (steps need order):**
```text
## Installation
- Install Python
- Run the program
- Install packages
```

**Correct:**
```text
## Installation
1. Install Python
2. Install packages
3. Run the program
```

Installation steps must be in the right sequence.

---

## Why This Matters for AI

When you use lists correctly in specifications, AI agents can:

1. **Identify distinct items** — "This app has 5 features"
2. **Understand dependencies** — "Step 2 requires Step 1 to complete first"
3. **Generate appropriate code** — "Create 5 functions, one for each feature"
4. **Follow sequences** — "Set up installation script with these 4 steps in order"

Lists turn vague intentions into countable, trackable requirements — exactly what AI needs to generate accurate code.

:::info[Expert Insight]
Professional specifications use list type as semantic information. When AI sees an unordered list under "Features," it knows these are parallel capabilities that can be developed independently—perfect for parallel development or modular architecture. When it sees ordered lists under "Installation," it knows to generate sequential scripts or documentation. This semantic clarity reduces miscommunication and speeds up development.
:::

---

## Try With AI

Validate your Task Tracker App lists with AI feedback.

:::tip[Remember the Verification Framework]
When AI reviews your lists, apply the 4-step framework from Lesson 1: check against what you know, ask AI to explain its reasoning, test specific claims, and cross-reference if unsure.
:::

### Setup

Use any AI assistant you have access to — ChatGPT, Claude, Gemini, or another tool.

### Exercise

Take your **updated Task Tracker App specification** (now with lists added) and ask your AI to review it:

**Prompt 1 (List Type Check):**

```
I'm learning markdown lists. Can you check if I used the right list types?
Tell me if my features should be numbered or if my steps should be bullet points:

[Paste your specification here]
```

**Prompt 2 (Clarity Check):**

```
Can you identify:
1. How many features this app has
2. How many installation steps are required
3. Whether the steps must be done in order

Based on my lists?
```

**Prompt 3 (Improvement Suggestion):**

```
Based on my specification, what other lists could I add to make
this clearer? (Like requirements, error messages, or configuration steps)
```

### Expected Outcomes

From **Prompt 1**: Your AI will confirm whether you chose the right list types (ordered vs unordered)

From **Prompt 2**: Your AI should be able to count items and understand sequence requirements from your list choices

From **Prompt 3**: Your AI will suggest additional lists to strengthen your specification
