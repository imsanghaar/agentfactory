---
sidebar_position: 5
chapter: 8
lesson: 5
layer: L2
title: "Error Recovery & Resilience"
description: "Deliberately break something and practice fixing it. Build recovery muscle memory so real mistakes don't cause panic"
duration_minutes: 20
keywords:
  [
    "error recovery",
    "resilience",
    "backup restore",
    "state comparison",
    "deliberate practice",
    "fire drill",
  ]

skills:
  - name: "Deliberate Error Practice"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can intentionally create and recover from file operation errors"

  - name: "Backup Recovery Execution"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can restore files from a verified backup after a failed operation"

  - name: "State Comparison"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can compare current state against backup to identify what changed"

learning_objectives:
  - objective: "Create a test environment, break it deliberately, and recover from backup"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes the full create-break-recover cycle on test files"

  - objective: "Compare current state against backup to diagnose what went wrong"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student directs agent to compare directories and identifies differences"

  - objective: "Apply recovery prompts to common file operation failures"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can articulate the correct recovery prompt for different failure scenarios"

cognitive_load:
  new_concepts: 3
  concepts_list:
    - "Deliberate practice (intentionally breaking things to learn recovery)"
    - "State comparison (diff between current and backup)"
    - "Recovery workflow (restore, verify, proceed)"
  assessment: "3 concepts within A2 limit of 5"

differentiation:
  extension_for_advanced: "Create a recovery script that automates the compare-and-restore workflow"
  remedial_for_struggling: "Focus on the basic cycle: backup exists → something broke → copy backup back. Don't worry about selective recovery."

teaching_guide:
  lesson_type: "hands-on"
  session_group: 2
  session_title: "Batch Operations and Error Recovery"
  key_points:
    - "The fire drill metaphor is the lesson's thesis: practicing recovery when stakes are low builds muscle memory so real mistakes produce workflow, not panic"
    - "'The agent is ephemeral, code is eternal' (Principle 2) is the key insight — asking the agent to write restore.sh is fundamentally different from asking it to restore files"
    - "State comparison (current vs backup) is the most powerful diagnostic tool — when you do not know what went wrong, systematic comparison reveals exactly what changed"
    - "Recovery is messy in practice (permission errors on 3 files) — the lesson deliberately shows non-clean recovery to set realistic expectations"
  misconceptions:
    - "Students think recovery means 'undo' — it actually means re-applying rules.md to the current state, not reverting to a snapshot"
    - "Students may resist the deliberate destruction step because it feels wasteful — emphasize that the backup from Lesson 2 makes this completely safe and the learning is irreplaceable"
    - "Students assume the agent will recover identically each time — the ephemeral vs eternal distinction shows why scripts produce consistent results but agents may interpret differently each session"
  discussion_prompts:
    - "Have you ever frozen when something went wrong with your files? What would change if you had practiced recovery beforehand?"
    - "The lesson says 'fix the process, not the file' (from Lesson 4) and 'the agent is ephemeral, code is eternal.' How do these two ideas connect?"
    - "When would you choose selective recovery (restore just one category) over full recovery? What makes that decision?"
  teaching_tips:
    - "This lesson must be done hands-on — reading about recovery does not build the muscle memory the lesson is designed to create"
    - "The emotional arc matters: students should feel the anxiety of destroying their organized folders, then the relief of successful recovery — that emotional imprint is the learning"
    - "Connect this back to Lesson 2's safety-first pattern: the backup created there pays off here, closing the loop across three lessons"
    - "The session management note is important for workshops — five lessons of accumulated context is the point where a fresh session becomes valuable"
  assessment_quick_check:
    - "Ask students: 'Your organized folder looks wrong but you are not sure what happened. What is your first prompt to the agent?' — answer should involve state comparison against backup"
    - "Ask: 'Why should you create restore.sh instead of just asking the agent to restore your files next time?' — tests the ephemeral vs eternal distinction"
---

# Error Recovery & Resilience

We're about to do something most tutorials would never let you do. You're going to deliberately destroy the organization you just built. On purpose. With your real files.

Look at your `organized/` folder. That structure took you the last three lessons to build — survey, backup, categorization rules, batch moves. You're about to flatten it back to chaos in 5 seconds.

The goal isn't to get good at fixing mistakes. The goal is to stop being afraid of making them. Fire drills don't teach you to fight fires. They teach you to stop freezing when the alarm goes off. By the end of this lesson, the word "oops" will be followed by a recovery workflow, not a panic response.

---

## Exercise: The Deliberate Mistake

You're going to intentionally run a bad organization command and then recover from it. This is safe because you have a verified backup from Lesson 2.

### Step 1: Confirm Your Safety Net

First, verify that the backup you created in Lesson 2 still exists and is complete:

```
You: Check my file-organizer/backup/ folder. Is my backup from Lesson 2
still there? How many files does it contain? Compare it against what's
currently in file-organizer/organized/.
```

```
Claude Code:
[Runs: ls file-organizer/backup/]
[Runs: find file-organizer/backup/ -type f | wc -l]
[Runs: find file-organizer/organized/ -type f | wc -l]

Your backup contains 136 files across 5 categories.
Your organized/ folder currently has 486 files.
The backup covers your important files (PDFs and recent files).
Safety net confirmed.
```

### Step 2: Run a Deliberately Wrong Reorganization

Ready? Look at your organized/ folder one more time. Five categories. 486 files, each in its place. You built that. You're about to destroy it in one command.

```
You: Take everything in file-organizer/organized/ and merge all the
category folders back into a single flat folder. Dump all files from
documents/, spreadsheets/, images/, code/, and misc/ into organized/
directly. Remove the empty category folders.
```

```
Claude Code:
[Runs: mv file-organizer/organized/documents/* file-organizer/organized/]
[Runs: mv file-organizer/organized/spreadsheets/* file-organizer/organized/]
[Runs: mv file-organizer/organized/images/* file-organizer/organized/]
... (moves all files, removes empty folders)

Done. All 486 files are now in a single flat folder.
The category structure from Lesson 3 is gone.
```

### Step 3: Watch the Structure Collapse

Check what happened to the organization you built in Lesson 3:

```
You: Show me what file-organizer/organized/ looks like now.
Is there any way to tell which files were documents vs images
vs spreadsheets?
```

```
Claude Code:
[Runs: ls file-organizer/organized/ | head -20]

organized/ now contains 486 files in a single flat list.
report.pdf sits next to photo.jpg sits next to budget.xlsx.
There's no way to tell which category they belonged to —
the folder structure was the only metadata, and it's gone.
```

### Step 4: Discover the Problem

The damage is done. Now diagnose it:

```
You: Compare what's in file-organizer/organized/ now against my
backup. Show me what I lost and what changed.
```

```
Claude Code:
[Runs: ls file-organizer/organized/ | wc -l]
[Runs: ls -d file-organizer/organized/*/  2>/dev/null]

organized/ now has 486 files in a flat list.
No subdirectories remain — all category folders are gone.

The files themselves are intact, but the STRUCTURE is destroyed.
Your rules.md still describes the categories, but the folders
that implemented those categories no longer exist.
```

The "mistake" here is real — you lost the entire organization from Lesson 3. In real workflows, this kind of destructive flatten could also overwrite files with the same name across categories, break relative paths, or mix incompatible file types.

### Step 5: Recover from Backup

Here's the payoff. You have a backup. But more importantly, you have `rules.md`. Recovery means re-applying your documented rules:

```
You: That reorganization was wrong. I want to restore my organized/
folder structure. Use the backup to recover any files that were lost,
and re-apply the rules from rules.md to recreate the category folders.
```

```
Claude Code: Restoring organization...

[Runs: # Recreates category folders from rules.md]
[Runs: # Re-sorts files by extension into proper categories]

Error: Permission denied on 3 files in organized/ — they're
marked read-only.

I'll adjust permissions and retry those files.

[Runs: chmod u+w organized/restricted-report.pdf organized/budget-locked.xlsx organized/template.docx]
[Runs: # Re-sorts the 3 failed files]

Second attempt successful. All 486 files sorted.

[Runs: # Compares against backup to verify no files lost]

Restored. organized/ now has 5 category folders matching rules.md.
486 files sorted back into their categories.
Verified against backup — no files missing.
```

Notice the recovery wasn't clean. Permission errors on 3 files. The agent adjusted and retried. Real recovery is like this — messy, iterative, but it gets there. The point isn't perfection on the first try. The point is having a process that converges on the right answer.

You're back to where you started. The careless flatten is undone. No data lost.

---

## Common Recovery Scenarios

Here are real situations where recovery saves you, and the prompt patterns to handle them:

**"I organized files with the wrong rules"**

```
The organization rules were wrong — financial files ended up in misc/
instead of spreadsheets/. Restore from backup and let's fix the rules
before re-organizing.
```

**"The rename script mangled filenames"**

```
The rename script produced garbled filenames. Show me the rename log,
then restore the original filenames from backup.
```

**"I accidentally deleted files I needed"**

```
I deleted some files from misc/ that I actually needed. Check my backup
for these files: [list filenames]. Copy them back to their original
location.
```

**"I'm not sure what went wrong"**

```
Something is off — my organized/ folder has fewer files than it should.
Compare the current state against the backup and show me what's missing
or different.
```

That last pattern — comparing current state against backup — is the most powerful recovery tool. When you're not sure what went wrong, a systematic comparison reveals exactly what changed.

---

## Building Recovery Into Your Workflow

The lesson from this exercise isn't just "backups are useful." It's that recovery should be a planned step, not an emergency response.

Here's how to build recovery thinking into every workflow:

| When                     | What to Do                                    |
| ------------------------ | --------------------------------------------- |
| Before you start         | Ask: "What's my recovery plan if this goes wrong?" |
| Before destructive ops   | Create or verify backup                       |
| After batch operations   | Compare results against expectations          |
| When something's off     | Compare current state vs backup               |
| After recovery           | Verify the restoration is complete            |

### The Agent is Ephemeral, Code is Eternal

Notice something about this lesson. Every time you needed recovery, you typed a prompt and the agent ran commands. That works. But what happens next month when you need to recover again? You'll describe the same thing from scratch. The agent might interpret your request slightly differently. It might use different flags, skip the verification step, or restore to the wrong location.

Now look at Try With AI Prompt 3 below — it asks you to create `restore.sh`. That script is fundamentally different from asking the agent to "restore my files." Here's why:

| Approach | Today | Next Month |
|----------|-------|------------|
| **Ask the agent** | Agent interprets your request, picks commands, runs them | Agent may interpret differently, pick different commands, produce different results |
| **Run a script** | Script executes the exact same steps every time | Script executes the exact same steps every time |

This is **Principle 2: Code as the Universal Interface** in action. When you ask the agent to _do_ something, you get a one-time result that depends on the agent's interpretation in that moment. When you ask the agent to _write code_ that does something, you get a deterministic tool that works the same way every time — even without the agent.

The agent is ephemeral. Your conversation ends, context resets, and the next session starts fresh. But a script saved to disk? That persists. It captures the exact recovery workflow you verified today and makes it repeatable forever.

**The pattern**: Whenever you find yourself asking the agent to do the same task twice, stop and ask it to write a script instead. You've traded a conversation for a tool.

---

## ✅ Checkpoint: Do This Now

Stop reading. Open Claude Code and run the recovery exercise.

1. Verify your backup from Lesson 2 is still intact
2. Deliberately flatten your `organized/` folder (merge all categories into one)
3. Compare the damage against your backup
4. Restore using your backup and `rules.md`
5. Verify the restoration matches the original structure

This should take less than 5 minutes. But the muscle memory you build will save you hours when a real mistake happens.

You can now break things and fix them. That's a superpower most people never develop. But there's one category of file problem where backups and recovery aren't enough — when you can't find the file in the first place. You know it exists. You downloaded it months ago. The filename is something your bank auto-generated. Where is it?

---

## 🔄 Session Management Note

You've now completed five lessons of file processing work. If your Claude Code context is getting long — or if responses feel slower or less focused — this is a natural point to start fresh.

**Why now:** Recovery exercises generate a lot of back-and-forth. Combined with Lessons 1-4, your context may be carrying exploration, organization, batch operations, and recovery all at once. That's the Kitchen Sink pattern from Chapter 6.

**How to reset:** Commit your work, then start a new session for Lesson 6. Your `rules.md`, `FILE-INVENTORY.md`, backups, and scripts are all saved in files — your progress carries forward across sessions.

---

## Try With AI: Extended Practice

**Prompt 1: Selective Recovery**

```
I organized my Downloads folder but only the spreadsheet categorization
was wrong. Help me restore JUST the spreadsheet files from backup
without undoing the rest of the organization.
```

**What you're practicing:** Surgical recovery. Sometimes you don't want to undo everything — just fix the part that went wrong.

**Prompt 2: Recovery Audit**

```
Compare my organized/ folder against my backup/ folder. Show me:
- Files that exist in backup but not in organized (lost files)
- Files that exist in organized but not in backup (new files)
- Files that changed size (possible corruption)
Create an audit report.
```

**What you're practicing:** Systematic comparison. This is the detective work that tells you exactly what changed and what might be wrong.

**Prompt 3: Recovery Script**

```
Create a script called restore.sh that takes a backup folder and a
target folder as arguments and restores the target from the backup.
Include verification that the restoration was complete.
```

**What you're practicing:** Automating recovery. Just like you created scripts for organization, you can create scripts for recovery. The pattern is the same.
