---
sidebar_position: 7
chapter: 8
lesson: 7
layer: L2
title: "Capstone: Your File Processing Toolkit"
description: "Synthesize all six workflows into a reusable prompt toolkit, apply them to a new folder, and recognize how the Seven Principles emerged through practice"
duration_minutes: 30
keywords:
  [
    "capstone",
    "prompt toolkit",
    "synthesis",
    "automation bridge",
    "seven principles",
    "workflow selection",
  ]

skills:
  - name: "Workflow Synthesis"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Synthesize"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student combines multiple workflows to solve a complete file management challenge"

  - name: "Prompt Template Creation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student creates reusable prompt templates for future file processing tasks"

  - name: "Principle Recognition"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student identifies which principles emerged during each workflow"

  - name: "Transfer to New Context"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student applies learned workflows to an unfamiliar folder"

learning_objectives:
  - objective: "Apply all six workflows to a new folder (Desktop)"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student completes survey, backup, organize, batch, recover, and verify on Desktop"

  - objective: "Create a personal prompt toolkit document for future use"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student produces MY-PROMPT-TOOLKIT.md with all workflow templates"

  - objective: "Identify which principles emerged during each lesson"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student completes reflection table connecting workflows to principles"

  - objective: "Articulate the bridge from manual workflows to automated AI Employee"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student explains what changes between manual prompting and automated workflows"

cognitive_load:
  new_concepts: 2
  concepts_list:
    - "Workflow selection under pressure (choosing the right workflow for a scenario)"
    - "Workflow-to-automation bridge (what changes when humans leave the loop)"
  assessment: "2 genuinely new concepts plus synthesis of 6 existing workflows at B1 level. The synthesis demand is high — students must combine, not just recall. Total cognitive load is significant despite low new-concept count."

differentiation:
  extension_for_advanced: "Create additional prompt templates for domains beyond files: calendar management, email organization, project tracking"
  remedial_for_struggling: "Focus on just one workflow on the Desktop. Complete the toolkit document with the workflows you found most useful."

teaching_guide:
  lesson_type: "capstone"
  session_group: 3
  session_title: "Search, Synthesis, and Capstone"
  key_points:
    - "The shift from 'knowing six workflows' to 'knowing which one to grab under pressure' is the capstone's core test — workflow selection IS the skill"
    - "The Seven Principles mapping table makes explicit what students practiced implicitly: every principle emerged through action, not lecture"
    - "MY-PROMPT-TOOLKIT.md is the chapter's most durable deliverable — organized folders go stale, but prompt templates are permanently reusable"
    - "The manual-to-automation bridge (Python code preview) shows students that the gap between manual prompts and automated AI Employees is just 'the same skill with a scheduler attached'"
  misconceptions:
    - "Students think the capstone introduces new material — it does not. The challenge is synthesis and judgment, which feels harder than learning individual workflows"
    - "Students may default to the survey-first sequence for every scenario — the urgent search scenario shows that context determines sequence, not a fixed order"
    - "Students might undervalue MY-PROMPT-TOOLKIT.md compared to the organized folders — the toolkit is the only deliverable that transfers to new folders and new domains"
  discussion_prompts:
    - "In Scenario 1 (urgent search), you skip the survey and go straight to search. When is it acceptable to break the standard sequence, and how do you decide?"
    - "Look at the manual-to-automated table. What changes when you remove the human from the loop? What stays exactly the same?"
    - "Which of the six workflows do you think you will use most often in your daily work? Why?"
  teaching_tips:
    - "Run the four triage scenarios as a class activity — have students debate which workflow to use BEFORE revealing the insights. Disagreements are productive learning moments"
    - "The 15-minute real-world test works best when students use their OWN messy folders — the stakes feel real because the files matter to them"
    - "The Seven Principles table is the perfect review tool — walk through it row by row and ask students to recall the specific moment they experienced each principle"
    - "End the chapter by having students read their MY-PROMPT-TOOLKIT.md aloud — hearing their own templates reinforces retention and reveals gaps"
  assessment_quick_check:
    - "Present a new scenario (e.g., 'Your project folder has 200 files and a deadline in 2 hours'). Ask students which workflows they would use and in what order"
    - "Ask students to name all Seven Principles and point to the lesson where each one appeared — tests synthesis across the whole chapter"
    - "Ask: 'What is the difference between the organized folders and the prompt toolkit? Which one would you take to a new computer?' — tests understanding of durable vs ephemeral deliverables"
---

# Capstone: Your File Processing Toolkit

Your accountant just called. They need a 1099-DIV from 2025. You have 300 files on your Desktop. Clock's ticking. Which workflow do you reach for?

That's the real test. Not whether you know six workflows — but whether you know which one to grab when your files are on fire and someone is waiting. Different scenarios require different workflow orders. There's no single correct sequence.

Before we build your permanent prompt toolkit, let's test your judgment.

---

## Triage Under Pressure

For each scenario, decide which workflow(s) to use and in what order BEFORE reading the insight. Then open Claude Code and try your approach.

### Scenario 1: The Urgent Search

Your Desktop has 300+ files. You need one specific tax document. Your accountant is waiting on the phone.

```
You: I need to find a 1099-DIV document from 2025. It's somewhere on
my Desktop. I need it RIGHT NOW.
```

**Before you run this** — think: Do you survey first (Lesson 1), or go straight to search (Lesson 6)?

**Insight:** Urgency overrides the normal sequence. Search first, organize later. When someone is waiting, you don't map the territory — you find the one thing you need. The survey-first pattern is for when you have time to be systematic.

### Scenario 2: The Fresh Start

You want to reorganize your Desktop, but you've never looked at what's there. No backup exists.

```
You: I want to completely reorganize my Desktop. What should I do first?
```

**Before you run this** — think: What's your workflow and in what order?

**Insight:** Survey → Backup → Organize. The order matters. If you skip the survey, your categories won't match your actual files. If you skip the backup, one wrong move and you're panicking. The safety-first pattern from Lesson 2 isn't optional — it's what makes everything else safe to attempt.

### Scenario 3: The Botched Script

You ran a batch rename script on your Desktop and now 40 files have garbled names. Some files seem missing entirely.

```
You: I ran a rename script and it went wrong. Some files have garbled
names and I think some are missing. What do I do?
```

**Before you run this** — think: What do you do FIRST — try to fix the names, or something else?

**Insight:** Compare against backup first. Don't start fixing individual files until you know the full extent of the damage. The recovery workflow from Lesson 5 starts with diagnosis (compare current state vs backup), not treatment. Files that "seem missing" might just be renamed — the backup comparison will tell you.

### Scenario 4: The Recurring Problem

You have 150 screenshots on your Desktop. You want them organized by month. You'll get 20+ more next week.

```
You: I have 150 screenshots cluttering my Desktop. I want them organized
by month. But I'll get more screenshots next week. What's my best approach?
```

**Before you run this** — think: One-time organization or script generation?

**Insight:** Recurring problems need scripts, not one-time commands. The batch operations pattern from Lesson 4 taught you to ask for reusable scripts. If you just organize these 150 files manually, you'll be back here next month. Ask for a script that handles the current backlog AND future screenshots.

---

## The Real Test: Your Desktop in 15 Minutes

Close the book. Open Claude Code. Point it at a folder you haven't touched yet — your Desktop, your Documents, an old project folder. Set a timer for 15 minutes.

Your goal: **survey it, back it up, organize it, and verify the results.** Use the workflows you've learned, in whatever order the situation demands.

```
I need to get my [Desktop / Documents / other folder] under control.
I have 15 minutes. Let's start with a survey so I know what I'm
working with, then create a backup of anything important, then
organize what's left. Go.
```

**What makes this different from the exercises:** Nobody is telling you which workflow to use or in what order. You have to assess the situation and choose. That's the skill — not knowing six workflows, but knowing which one to reach for.

After 15 minutes, check your work:

- Did you survey before organizing? (Or did urgency make you skip it?)
- Did you back up before making changes? (Or did you forget?)
- Did you verify the results? (Or did you assume success?)
- What would you do differently with 15 more minutes?

The answers reveal which patterns have become instinct and which still need practice.

---

## Build Your Prompt Toolkit

Now capture what you've learned in a permanent document.

```
Help me create MY-PROMPT-TOOLKIT.md with fill-in-the-blank templates
for each workflow I've practiced: survey, backup, organize, batch,
recover, search, and verify. For each template, include the key
phrases that trigger the right agent behavior.
```

This toolkit is the chapter's most important deliverable. The organized folders will get messy again. The scripts will need updates. But the *templates* — the patterns for how you direct an agent — those are permanently useful.

---

## The Seven Principles in Action

You've been learning the Seven Principles without memorizing them. Let's make explicit what emerged through practice.

| Lesson                   | What You Did                         | Principle That Emerged              |
| ------------------------ | ------------------------------------ | ----------------------------------- |
| 1. Survey                | Ran bash commands to analyze folder  | **P1: Bash is the Key**             |
| 1. Survey                | Made chaos visible through reports   | **P7: Observability**               |
| 2. Safety First          | Created backup before changes        | **P6: Constraints and Safety**      |
| 2. Safety First          | Verified backup was complete         | **P3: Verification as Core Step**   |
| 3. Organization          | Documented rules in rules.md         | **P5: Persisting State in Files**   |
| 3. Organization          | Tested on one file first             | **P4: Small, Reversible Decomp.**   |
| 4. Batch Operations      | Generated reusable script            | **P2: Code as Universal Interface** |
| 5. Error Recovery        | Restored from backup after mistake   | **P3 + P6: Verify + Safety**        |
| 6. Search & Discovery    | Described problem, agent chose tools | **P1 + P2: Bash + Code**            |
| 6. Search & Discovery    | Created persistent index of results  | **P5: Persisting State in Files**   |

All seven principles showed up naturally. You didn't study them from a textbook. You experienced them through action. And you saw them reinforce each other — safety enabled experimentation, verification caught errors, persistence made rules reusable.

---

## Your Command Vocabulary

Throughout this chapter, you observed the agent using these commands. You don't need to memorize them, but recognizing them helps you understand what the agent is doing.

### Core Commands

| Command    | Plain English                           | Lesson     |
| ---------- | --------------------------------------- | ---------- |
| `ls`       | **List** files in a directory           | 1, 3       |
| `find`     | **Find** files by name or date          | 1, 2, 6   |
| `wc -l`    | **Word count** (count lines)            | 1, 2       |
| `du -sh`   | **Disk usage** (human-readable sizes)   | 1          |
| `cp`       | **Copy** files                          | 2, 5       |
| `mv`       | **Move** (or rename) files              | 3, 4       |
| `rm -rf`   | **Remove** recursively (dangerous!)     | 5          |
| `mkdir`    | **Make directory**                      | 2, 3       |
| `mkdir -p` | **Make directory** (create parents too) | 4          |
| `cat`      | **Display** file contents               | 3          |
| `sort -rh` | **Sort** (reverse, human-readable)      | 1          |
| `head -10` | Show **first 10** lines                 | 4          |
| `diff`     | Show **differences** between files      | 5          |
| `cp -r`    | **Copy** recursively (entire folders)   | 5          |
| `chmod`    | **Change** file permissions             | 5          |
| `grep`     | **Search** inside files                 | 6          |
| `grep -l`  | Search inside, show matching **files**  | 6          |
| `grep -i`  | Search **case-insensitive**             | 6          |

### Connectors

| Symbol      | Plain English                                | Example                                                          |
| ----------- | -------------------------------------------- | ---------------------------------------------------------------- |
| `\|` (pipe) | "**then**" — chain commands together         | `find ... \| wc -l` = "find files, then count them"              |
| `xargs`     | "**for each**" — converts text to arguments  | `find ... \| xargs grep` = "find files, then search inside each" |

### Flags Worth Knowing

| Flag | Meaning                                     | Example                                |
| ---- | ------------------------------------------- | -------------------------------------- |
| `-l` | Show as list (ls) or list files only (grep) | `grep -l "pattern"`                    |
| `-i` | Case-insensitive                            | `find -iname "*.PDF"` matches .pdf too |
| `-r` | Reverse order (or recursive)                | `sort -r`                              |
| `-h` | Human-readable sizes (KB, MB, GB)           | `du -h`                                |
| `-p` | Create parent directories                   | `mkdir -p a/b/c`                       |

You don't need to memorize syntax. You need to recognize patterns. When you see the agent use these commands, you'll know what it's doing — and you can verify it's doing the right thing.

---

## Reflection Questions

Before moving on, consider these questions:

**1. Which workflow will you use most often?**

Everyone's answer is different. Some people struggle with cluttered desktops. Others need to batch rename screenshots weekly. Which pattern solves your recurring problem?

**2. What would you add to your toolkit?**

You might need templates for:

- Finding duplicate files
- Archiving old projects
- Cleaning up specific file types (old logs, cache files)

Think about what's missing for your specific needs.

**3. Where did you observe each principle?**

Look back at the principles table. Can you point to specific moments when you saw the agent apply that principle? The more concrete your memory, the more the patterns will stick.

---

## From Manual to Automated

Everything you did in this chapter was manual. You opened Claude Code, typed prompts, approved actions. You were the trigger.

When you learn automation, you'll build AI Employees that do this automatically:

| This Chapter (Manual)       | Automated Workflow               |
| --------------------------- | -------------------------------- |
| You type "survey my folder" | Agent watches folder for changes |
| You decide when to organize | Agent organizes on schedule      |
| You approve each batch      | Agent follows pre-approved rules |
| You verify results          | Agent reports results to you     |

Your `rules.md` becomes the AI Employee's decision rules. Your verification patterns become its supervision methods. Everything you learned transfers.

Here's a concrete glimpse of what that looks like. Your manual `rules.md` feeds directly into an automated workflow:

```python
# file_organizer_agent.py — what your manual workflows become

import yaml
from pathlib import Path
from datetime import datetime

# YOUR rules.md becomes the agent's decision logic
rules = yaml.safe_load(open("rules.md"))

# YOUR backup pattern becomes an automatic safety step
def organize_new_files(watch_folder: Path):
    new_files = detect_new_files(watch_folder)           # Survey (Lesson 1)
    create_timestamped_backup(new_files)                  # Safety (Lesson 2)

    for file in new_files:
        category = apply_rules(file, rules)               # Rules (Lesson 3)
        move_with_logging(file, category)                  # Batch (Lesson 4)

    verify_all_files_accounted_for(new_files, rules)      # Verify (Lesson 5)
    send_summary_report()                                  # Observability (P7)

# YOUR manual prompt → automated trigger
schedule.every(1).hour.do(organize_new_files, Path("~/Downloads"))
```

Every function in that script maps to a lesson you completed. `create_timestamped_backup` is Lesson 2. `apply_rules` is Lesson 3. `verify_all_files_accounted_for` is Lesson 5. The workflows are identical. Automation just removes *you* as the trigger.

The gap between "I type a prompt" and "it runs automatically" is smaller than you think. It's not a different skill — it's the same skill with a scheduler attached.

---

## ✅ Final Checkpoint: Chapter Deliverables

By completing the checkpoints throughout this chapter, you should now have:

| Item                   | Location                | Status                  |
| ---------------------- | ----------------------- | ----------------------- |
| `FILE-INVENTORY.md`    | In `file-organizer/`    | ✅ Lesson 1 checkpoint  |
| `backup/`              | With timestamped folder | ✅ Lesson 2 checkpoint  |
| `rules.md`             | With edge cases added   | ✅ Lesson 3 checkpoint  |
| `ORGANIZER-LOG.md`     | Full history            | ✅ Lesson 3 checkpoint  |
| `organized/`           | Files categorized       | ✅ Lesson 3 checkpoint  |
| Recovery exercise      | Completed               | ✅ Lesson 5 checkpoint  |
| `MY-PROMPT-TOOLKIT.md` | Your prompt templates   | ✅ This lesson          |

If you're missing any items, go back to the relevant lesson and complete the checkpoint. The toolkit is the most important deliverable — it's what you'll use long after this chapter is done.

---

## What You've Accomplished

When you started this chapter, you had a messy Downloads folder and no systematic way to handle it.

Now you have:

- **A methodology**: Survey, backup, design rules, batch execute, recover, verify
- **Reusable tools**: Scripts and templates you can adapt
- **Pattern recognition**: You see the Seven Principles when agents work
- **Recovery confidence**: You know how to fix mistakes, not just avoid them
- **A permanent toolkit**: Prompt templates that work on any folder, any time

This isn't just about files. The patterns you learned apply to any domain where you direct an AI agent. Describe the problem, establish safety, document rules, test small, scale up, recover from errors, verify.

---

## Try With AI: Extended Practice

**Prompt 1: Domain Transfer**

```
I've learned file organization workflows in this chapter. Help me apply
the same patterns to a different domain: my email inbox. What would
the equivalent of "survey," "backup," "rules," "batch," and "verify"
look like for email management?
```

**What you're practicing:** Abstraction. The workflows aren't about files. They're about systematic problem-solving. You're learning to see the pattern beneath the specific application.

**Prompt 2: Toolkit Expansion**

```
My prompt toolkit has the six core workflows. What other file-related
prompts would be useful to add? Think about tasks like finding duplicates,
archiving old projects, cleaning up cache files, or managing downloads
over time.
```

**What you're practicing:** Anticipation. Good toolkits grow with your needs. You're learning to think ahead about what patterns you'll need.

**Prompt 3: Principle Identification**

```
I'm about to reorganize my Photos folder. Before I start, help me
plan which of the Seven Principles I should apply at each step.
For each principle, tell me specifically what I should do or ask for.
```

**What you're practicing:** Explicit principle application. By planning with principles in mind, you internalize them more deeply. Eventually this becomes automatic.

---

## Conclusion

Here's what changed between Lesson 1 and now.

In Lesson 1, you asked the agent to analyze your Downloads folder. You watched it work. You were impressed that it ran six commands in 30 seconds.

Now? You wouldn't just *watch*. You'd check whether it backed up first. You'd question its categorization rules. You'd ask for a preview before batch operations. You'd verify the results against a known state. You'd ask for a script, not a one-time fix.

That shift — from passive observer to active director — is the real deliverable. Not the organized folder. Not the scripts. Not the toolkit document. The skill of *knowing what to demand from an agent* before trusting its output.

The agent is ephemeral. Your conversation ends, context resets, the next session starts fresh. But the patterns you've internalized — survey before acting, backup before changing, verify before trusting, script before repeating — those persist in *you*. They transfer to email management, project organization, data pipelines, and every domain where you direct AI agents.

Your Downloads folder is organized. Your toolkit is built. You're ready for automation.

---

## 🔄 Session Management Note

You've completed the entire chapter. Commit everything and start a completely fresh session before moving to the next chapter.

**Why this matters:** Seven lessons of file processing generated a lot of context — surveys, organization rules, batch scripts, recovery exercises, search patterns, and this capstone. Carrying all of that into the next chapter would be the Kitchen Sink pattern from Chapter 6. Your deliverables (`MY-PROMPT-TOOLKIT.md`, `rules.md`, scripts) are all saved in files. The next chapter starts clean.
