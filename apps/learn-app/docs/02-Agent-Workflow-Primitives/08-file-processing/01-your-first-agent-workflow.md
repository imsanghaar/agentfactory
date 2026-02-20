---
sidebar_position: 1
title: "Your First Agent Workflow"
chapter: 8
lesson: 1
layer: L2
duration_minutes: 25
description: "See a General Agent solve a real problem, then learn the prompt pattern that made it work"
keywords:
  [
    "agent workflow",
    "file analysis",
    "claude code",
    "general agent",
    "prompting",
    "observability",
    "division of labor",
    "problem description",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Problem-to-Prompt Translation"
    proficiency_level: "A1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Communication"
    measurable_at_this_level: "Student can translate a messy real-world problem into a clear prompt for a General Agent"

  - name: "Observing Agent Behavior"
    proficiency_level: "A1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can watch what a General Agent does and identify which principles are in action"

  - name: "Prompt Pattern Recognition"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can recognize and reuse prompt patterns across different problem domains"

learning_objectives:
  - objective: "Direct a General Agent to analyze a cluttered folder"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student successfully prompts Claude Code to produce a folder analysis report"

  - objective: "Identify the Seven Principles in agent behavior"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student can point to specific agent actions and name the principle being demonstrated"

  - objective: "Apply the 'Help me understand' prompt pattern to new problems"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student uses the pattern to analyze a different folder or problem domain"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (problem description, agent direction, observing actions, prompt patterns) within A1-A2 limit of 5"

differentiation:
  extension_for_advanced: "Try the prompt pattern on non-file problems: 'Help me understand my calendar this week' or 'Help me understand this codebase'"
  remedial_for_struggling: "Focus on just the first conversation. Watch what the agent does. Don't worry about identifying every principle. Just notice that the agent ran commands and reported back."

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "First Agent Workflow and Safety"
  key_points:
    - "The 'Help me understand [problem], show me [what I need]' prompt pattern is the foundation for all file-processing workflows in this chapter"
    - "Division of labor is the core insight: human judgment (what matters) + agent execution (how to get it) — neither can do the other's job"
    - "Agent self-correction (23 items vs 847 files) demonstrates OODA in action — students saw this principle in Ch 3 and now see it live"
    - "The rule of thumb 'describe faster than do = agent, do faster than describe = manual' sets the decision boundary for the entire chapter"
  misconceptions:
    - "Students think agents are always faster — lesson explicitly shows single-file lookup is faster manually, agents win at scale (847 files)"
    - "Students confuse 'I don't need to know bash' with 'bash doesn't matter' — the command anatomy section shows why reading agent output matters for verification"
    - "Students may think the agent's self-correction was a bug — it's actually the desired behavior showing Observe-Orient-Decide-Act working correctly"
  discussion_prompts:
    - "When was the last time you avoided organizing files because the task felt too big? What would change if you could describe the problem in one sentence?"
    - "The agent got the file count wrong, then corrected itself. Would you trust it more or less after seeing that mistake? Why?"
    - "What kinds of file decisions should never be delegated to an agent, even with the right prompt?"
  teaching_tips:
    - "Start with the 847-file Downloads folder scenario — every student has a cluttered folder, so the pain point is universal and immediate"
    - "Walk through the self-correction moment (23 vs 847) as a live teaching moment about why OODA matters in practice, not just theory"
    - "The command anatomy diagram (find | wc -l breakdown) is worth putting on the board — students will see these commands repeatedly in lessons 3-7"
    - "Have students actually run the checkpoint exercise on their own folders before moving on — lesson 2 builds on having a real FILE-INVENTORY.md"
  assessment_quick_check:
    - "Ask students to state the 'Help me understand' prompt pattern from memory and apply it to a non-file problem"
    - "Ask: 'Why did the agent switch from ls to find?' — tests whether they understood the self-correction, not just watched it"
    - "Have students explain when they would NOT use an agent for a file task — tests the rule of thumb boundary"
---

# Your First Agent Workflow

Let's be honest about something before we start.

If you need to check whether a file exists, you're faster than any AI agent. Type `ls budget.csv` — done in two seconds. The agent would need to think, pick a command, ask permission, then respond. Fifteen seconds for a two-second task.

So why are you reading a chapter about directing agents to handle files?

Because your Downloads folder has 847 files in it. You don't know what's in half of them. Three of them are tax documents you'll need in April. One is a duplicate that's eating 2 GB of disk space. And the file your boss asked about yesterday? It's in there somewhere, buried under six months of random downloads.

You could spend an afternoon sorting through them manually. Or you could describe the problem in one sentence:

```
You: I have a cluttered Downloads folder. Help me understand what's
in here. How many files, what types, what's taking up space?
```

That's it. No commands, no technical details, no specifying _how_ to analyze it. The agent ran six commands, self-corrected when its first count was wrong, and produced a complete breakdown in 30 seconds.

**The rule of thumb you'll internalize in this chapter:** If you can describe the task faster than you can do it, ask the agent. If you can do it faster than you can describe it, just do it. Three files to move? Drag them. Three hundred files to categorize by type, date, and project? That's agent territory.

The pattern you'll learn today — describe the problem, let the agent figure out the solution — applies to data analysis, project management, research, and any domain where you work with General Agents.

## The Conversation

Open Claude Code. Here's the full exchange — including the parts most tutorials edit out.

```
You: I have a cluttered Downloads folder. Help me understand what's
in here. How many files, what types, what's taking up space?
```

```
Claude Code: I'll analyze your Downloads folder. Let me take a look.

> Allow Claude Code to run: ls -la ~/Downloads | head -20
> [Y/n]: Y

You have 23 items in your Downloads folder. Actually, let me
recount — that's just the top-level view. Some of those are
folders with files inside them. Let me get the real number.

> Allow Claude Code to run: find ~/Downloads -type f | wc -l
> [Y/n]: Y

You have 847 files in your Downloads folder — much more than the
23 items that ls showed, because many are nested in subfolders.
```

Pause. Did you catch what just happened? The agent got it wrong the first time — 23 items — and then corrected itself. It didn't hide the mistake or pretend the first answer was right. It noticed that `ls` only shows the top level, switched to `find -type f`, and got the real number. That self-correction is what good agent work looks like.

```
Claude Code: Let me break down what types of files you have.

[Runs: find ~/Downloads -type f -name "*.pdf" | wc -l]
[Runs: find ~/Downloads -type f -name "*.xlsx" -o -name "*.csv" | wc -l]
[Runs: find ~/Downloads -type f -name "*.jpg" -o -name "*.png" | wc -l]
[Runs: find ~/Downloads -type f -name "*.zip" | wc -l]

Here's what I found:

| File Type     | Count | Notes                         |
|---------------|-------|-------------------------------|
| PDFs          | 234   | Documents, reports, receipts  |
| Spreadsheets  | 89    | .xlsx and .csv files          |
| Images        | 156   | Screenshots, photos           |
| Archives      | 43    | .zip files (may contain more) |
| Other         | 325   | Mixed: .docx, .dmg, .exe     |

Now let me see what's taking up the most space.

[Runs: du -sh ~/Downloads]
[Runs: du -ah ~/Downloads | sort -rh | head -10]

Total folder size: 12.4 GB

Your largest files:
1. project-backup.zip (2.1 GB)
2. video-recording.mp4 (1.8 GB)
3. database-export.sql (890 MB)
4. presentation-final.pptx (456 MB)
5. dataset.csv (312 MB)

Just these 5 files account for 5.5 GB. Almost half your folder.

Would you like me to help you organize these, or should I look
for duplicates first?
```

That took about 30 seconds. You now know:

- Total file count (847)
- Breakdown by type
- Total size (12.4 GB)
- Where the space is going

You didn't run a single command. You described a problem, and the agent solved it.

## The Division of Labor

Look at what just happened through a different lens. You described the problem in language: "cluttered Downloads folder." The agent chose the solution in code: `ls`, `find`, `wc`, `du`. You couldn't have chosen those commands (you don't know bash). The agent couldn't have chosen what to analyze (it doesn't know what matters to you). Neither of you could have done the other's job. That's the insight — the value isn't automation. It's the combination of your judgment with the agent's technical execution.

### And Sometimes the Agent is the Wrong Tool Entirely

Not every file task belongs in a terminal:

- **Browsing photos**: You need to _see_ thumbnails to decide which to keep. The agent sees filenames and metadata. You see memories.
- **Network drives and NAS**: File operations on mounted network storage can behave differently — latency, permission models, case sensitivity. The agent doesn't know your NAS has a 2-second round trip per operation.
- **Decisions that need human eyes**: That folder of old photos from college? Don't let an agent bulk-delete based on file size rules. Some decisions aren't computational.

The best collaborators know when to hand off and when to handle it themselves. Acknowledging the agent's limits is part of the skill — not a weakness.

---

### The Agent's Toolkit: What Those Commands Mean

The agent ran several commands. Let's decode them.

#### The Building Blocks

- **`ls`** — **l**i**s**t files in a folder
- **`find`** — **find** files matching a pattern
- **`wc`** — **w**ord **c**ount (counts lines, words, or characters)
- **`du`** — **d**isk **u**sage (measures sizes)
- **`sort`** — **sort** results in order

#### Anatomy of a Command

Let's break down one command the agent ran:

```
find  ~/Downloads  -type f  -name "*.pdf"  |  wc -l
  |        |          |          |         |    |
  |        |          |          |         |    +-- -l = count Lines only
  |        |          |          |         |
  |        |          |          |         +-- pipe: "then do this..."
  |        |          |          |
  |        |          |          +-- -name = match this filename pattern
  |        |          |
  |        |          +-- -type f = only Files (not folders)
  |        |
  |        +-- where to search
  |
  +-- the command
```

Read it left to right: "**Find** in **Downloads**, only **files**, named `*.pdf`, **then** count **lines**."

#### Common Flags You'll See

| Flag | Means                        | Memory Trick |
| ---- | ---------------------------- | ------------ |
| `-l` | Lines (or Long listing)      | **l**ines    |
| `-h` | Human-readable (KB, MB, GB)  | **h**uman    |
| `-r` | Reverse order                | **r**everse  |
| `-s` | Summary (totals only)        | **s**ummary  |
| `-a` | All (including hidden files)  | **a**ll      |

When the agent ran `du -sh`, that's "**d**isk **u**sage, **s**ummary, **h**uman-readable."

When it ran `sort -rh`, that's "**sort**, **r**everse order, **h**uman-readable" — biggest first.

#### The Pipe: Chaining Tools Together

The pipe (`|`) connects commands. Output from the left feeds into the right:

```bash
find ~/Downloads -name "*.pdf" | wc -l
```

"Find PDFs, **then** count them."

Small tools, chained together, solving big problems. That's what makes the shell so powerful.

You don't need to memorize these commands. But recognizing them helps you understand what the agent is doing — and verify it's doing the right thing.

## The Pattern

Here's the prompt pattern you just used:

```
"Help me understand [my problem]. Show me [what I need to know]."
```

This pattern works because it does two things:

1. **Describes the problem, not the solution.** You said "cluttered Downloads folder," not "run `find` and `du` commands." You let the agent figure out _how_ to help.

2. **Specifies the outcome you want.** You asked for "how many files, what types, what's taking up space." The agent knew what success looked like.

This is fundamentally different from learning bash commands yourself. You're not memorizing syntax. You're describing problems and letting the agent choose the right tools.

The pattern generalizes. Try these variations:

| Your Problem                     | The Prompt                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------- |
| Messy Desktop                    | "Help me understand my Desktop. What's here, what's old, what's taking up space?"            |
| Mystery disk usage               | "Help me understand where my disk space is going. What folders are largest?"                  |
| Project scattered across folders | "Help me understand where files related to [project name] are scattered."                    |
| Duplicate photos                 | "Help me understand if I have duplicate photos. Show me likely duplicates."                   |

The specifics change. The pattern stays the same.

## ✅ Checkpoint: Do This Now

Stop reading. Open Claude Code and run the survey on YOUR Downloads folder.

Use this prompt (modify if needed):

```
Help me understand what's in my Downloads folder. How many files,
what types, what's taking up space? Show me the full picture.
```

After Claude Code finishes, ask it to save the results:

```
Save this analysis as FILE-INVENTORY.md in a new folder called file-organizer/
```

You should now have: A `file-organizer/FILE-INVENTORY.md` file with your actual file analysis.

**Don't move to Lesson 2 until you've created this file.** Everything that follows builds on understanding YOUR files, not the example files in this book.

> **What to do if your Downloads folder is empty or tiny:** Pick a different folder — Documents, Desktop, or any folder with at least 20 files. Adjust the prompt accordingly.

---

## Try With AI

### Prompt 1: Go Deeper

```
I tried the "help me understand" pattern on my Downloads folder.
Now I want to go deeper. Based on what you found, what should
I investigate next? Pick the most interesting finding and
help me understand that in more detail.
```

**What you're practicing:** Iterative prompting. One analysis leads to the next question. You're building a habit of drilling down, not stopping at the first answer.

### Prompt 2: Translate to a new domain

```
The "help me understand [problem], show me [what I need]" pattern
worked for files. I want to apply it to something else.

Help me understand my recent shell history. What commands have I
run most often? What patterns do you see in how I use my computer?
```

**What you're practicing:** Pattern transfer. The same prompt structure works for different problems. You're learning that General Agents respond to well-structured requests regardless of domain.

### Prompt 3: Reflect on the agent's approach

```
I watched you analyze my Downloads folder. You used commands
like find, wc, and du.

Why did you choose those specific commands? What alternatives
did you consider? What would you have done differently if I'd
asked a slightly different question?
```

**What you're practicing:** Understanding agent reasoning. By asking the agent to explain its choices, you learn how it thinks. This makes you better at directing it in the future.

### Prompt 4: The Bash Tutor

```
Break down this command for me piece by piece:

du -ah ~/Downloads | sort -rh | head -10

What does each part do? What do the flags like '-ah', '-rh',
and '-10' mean? Teach me to read this command.
```

**What you're practicing:** Just-in-time learning. Instead of memorizing a textbook, you ask the agent to teach you the specific syntax relevant to the problem you just solved. The agent becomes your tutor, explaining commands in context.

---

Your Downloads folder is visible now. But visibility creates a new problem. You can see exactly what's there — and some of it matters. Tax documents. Financial spreadsheets. Irreplaceable photos buried under random downloads. If the next step goes wrong, those files could disappear. And unlike code, your files don't have `git revert`.
