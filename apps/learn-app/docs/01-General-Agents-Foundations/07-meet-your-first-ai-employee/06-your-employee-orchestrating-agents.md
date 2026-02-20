---
sidebar_position: 6
title: "Your Employee Delegating to Claude Code"
description: "Set a delegation rule so your AI Employee uses Claude Code for coding tasks, verify real work by attaching to live tmux sessions, and experience the two-tier delegation pattern"
keywords:
  [
    ai employee delegation,
    claude code delegation,
    tmux agent orchestration,
    two-tier delegation,
    agent verification,
    openclaw claude code,
    agent factory thesis,
  ]
chapter: 7
lesson: 6
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Delegation Setup"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can instruct their AI Employee to delegate coding tasks to Claude Code via tmux and verify the delegation by attaching to the session"

  - name: "Delegation Verification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can verify whether an AI agent actually performed delegated work (vs hallucinated it) by inspecting tmux sessions and output files"

learning_objectives:
  - objective: "Set up real delegation from an AI Employee to Claude Code using tmux sessions"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student sends a coding task via Telegram, then runs tmux ls and tmux attach to confirm Claude Code is running in a live session"

  - objective: "Verify that an AI agent performed work rather than hallucinated it"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student attaches to a tmux session, observes Claude Code producing files, and checks the output directory for real artifacts"

  - objective: "Explain the two-tier delegation pattern through firsthand experience"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student describes in their own words the chain: human gives intent, employee coordinates, Claude Code executes -- and explains why verification matters"

cognitive_load:
  new_concepts: 4
  concepts_list:
    - "Rule-based delegation (set the rule once, employee handles mechanics)"
    - "tmux as infrastructure (background sessions for agent work)"
    - "Verification over trust (attach to sessions, check output files)"
    - "Two-tier delegation (you manage the employee, employee manages Claude Code)"
  assessment: "4 concepts within B1 range (7-10). tmux is introduced as a simple tool, not a deep topic. Every concept is grounded in a hands-on exercise with verifiable output."

differentiation:
  extension_for_advanced: "Set up three parallel tmux sessions running Claude Code on different tasks simultaneously. Monitor all three and document which finished first and why."
  remedial_for_struggling: "Focus on Exercise 1 only. Run tmux ls to confirm the session exists. If it does not, describe what your employee said it would do vs what actually happened."

teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Agent Delegation and Verification"
  key_points:
    - "The two-tier delegation pattern (you manage, employee coordinates, Claude Code executes) is the concrete manifestation of the Agent Factory thesis from Chapter 1"
    - "Verification over trust is the critical habit — tmux ls and tmux attach prove work happened; without verification, students cannot distinguish real delegation from hallucinated claims"
    - "The hallucination problem with delegation is pedagogically valuable — students experience firsthand that AI agents can claim to have done work they did not actually do"
    - "Rule-based delegation (set it once, employee handles mechanics) demonstrates that managing AI is about setting clear policies, not micromanaging each step"
  misconceptions:
    - "Students think their employee 'knows' Claude Code exists — it does not discover tools on its own; the explicit delegation rule is required, not optional"
    - "Students assume if the employee says it delegated to Claude Code, it actually did — the lesson explicitly teaches that verification (tmux ls) is mandatory because LLMs produce plausible but potentially false claims"
    - "Students think tmux is a complex tool they need to master — in this context it is just a background session manager; they only need tmux ls, tmux attach, and Ctrl+B D"
    - "Students confuse the employee writing code itself with delegating to Claude Code — the whole point is that the employee is a coordinator, not a coder"
  discussion_prompts:
    - "When your employee claimed to have delegated work but tmux ls showed nothing, how did that change your trust model? What verification habits should you build?"
    - "In Exercise 3, your employee did research (its strength) then delegated coding (Claude Code's strength). What other task combinations follow this two-tool pattern?"
    - "Compare this lesson to Chapter 3 where you used Claude Code directly. What did you gain by adding the employee as a coordination layer? What did you lose?"
  teaching_tips:
    - "Have students run tmux ls BEFORE telling them whether delegation worked — the discovery moment when they see a real session (or an empty list) is the most memorable part of this lesson"
    - "If a student's employee hallucinates delegation, do NOT fix it for them — have them send the correction message from the lesson and experience the recovery flow"
    - "Demo Exercise 3 live: show the research phase on Telegram, then the approval step, then switch to terminal and attach to the tmux session — the visual transition from messaging to terminal makes the delegation chain tangible"
    - "Draw the three-layer delegation table on the whiteboard and have students fill in who does what — this reinforces the Agent Factory thesis without requiring re-reading Chapter 1"
  assessment_quick_check:
    - "Ask students: How do you verify your employee actually ran Claude Code? (tmux ls and tmux attach)"
    - "Have students explain the two-tier delegation pattern in their own words using the three roles: manager, coordinator, coder"
    - "Ask: Why did we set a delegation rule instead of specifying tmux commands each time?"
---

# Your Employee Delegating to Claude Code

:::info Prerequisites
This lesson requires **tmux** (a terminal multiplexer) and **Claude Code** (from Chapter 3) installed on your machine. The first exercise checks for tmux and installs it if needed. If you do not have Claude Code installed, revisit Chapter 3 before continuing.
:::

Your employee has been handling tasks on its own: creating files, setting up morning briefings, doing research, managing your schedule. For tasks like "create weekly-goals.md" or "design a daily routine," it uses its own built-in tools and does fine.

But what happens when you need actual code written? A Python script, a data processing tool, a file organizer? Your employee is not a coding specialist. It will try -- and it may produce something -- but it is not the right tool for the job.

You already have the right tool. Claude Code is on your machine from Chapter 3. In this lesson, you are going to teach your employee to delegate coding work to Claude Code -- and then verify the delegation is real.

## Why Delegation Needs to Be Explicit

Your employee will not discover Claude Code on its own. If you ask it to "build a Python calculator," it will attempt to write code itself or, worse, claim it delegated the work to Claude Code when it actually did not. It may even give you a fake session ID and a working directory that does not exist.

This is not a bug. It is how language models work. They produce plausible responses, which sometimes means plausible claims about actions they did not take.

The fix: tell your employee clearly that coding tasks go to Claude Code, and that it should use tmux sessions to run them. You set the rule once. Your employee handles the terminal commands. You verify the work is real.

---

## Connect Your Employee to Claude Code

### Step 1: Make Sure tmux Is Ready

Send this to your AI Employee via Telegram:

```
Check if tmux is installed on this machine. If not, install it.
Confirm with the version number.
```

tmux lets your employee run terminal sessions in the background. Your employee will create tmux sessions, run Claude Code inside them, and report back to you on Telegram. You can attach to these sessions from your own terminal and watch the work happen live.

### Step 2: Set the Delegation Rule

This is the one-time instruction that changes how your employee works:

```
From now on, when I ask you to build or write code, use Claude Code
to do the work -- do not write code yourself.

Run Claude Code inside tmux sessions so I can attach and watch.
Always tell me the session name so I can verify with tmux ls.
```

Your employee should confirm it understands. Something like: "Understood -- for coding tasks, I'll spin up Claude Code in tmux sessions and give you the session name to verify."

That is the entire setup. You told your employee **what tool to use** and **how you will verify**. Your employee already has terminal access -- it knows how to run tmux commands. You do not need to spell out the exact syntax every time. You are the manager setting the rule; your employee handles the mechanics.

---

## Exercise 1: Your First Delegated Task

Send this to your employee:

```
Build me a simple Python calculator with add, subtract, multiply,
and divide functions. Include a demo in the main block.
Tell me the session name when Claude Code is running.
```

That is all you send. Your employee should create a tmux session, launch Claude Code with the task, and report the session name back to you.

Now open a terminal on your machine and verify:

```bash
tmux ls
```

You should see a session in the list. Attach to it:

```bash
tmux attach -t <session-name>
```

You are watching Claude Code work in real time. It is writing files, creating functions, building your calculator. This is real delegation -- verified by your own eyes. Detach with `Ctrl+B` then `D` to let it continue.

When it finishes, find and run the output:

```bash
python calculator.py
```

The files exist. The calculator runs. Your employee handled the tmux commands, Claude Code wrote the code, and you verified every step.

**If tmux ls shows nothing:** Your employee claimed to delegate without actually running the commands. This is the hallucination problem described above. Send this follow-up:

```
I just ran tmux ls and there are no sessions. You did not actually
run Claude Code. Please do it now -- create the tmux session and
run Claude Code for real. I am watching tmux ls in my terminal.
```

Reinforcing that you are actively verifying usually resolves it. If your employee still cannot execute shell commands, it may not have terminal access configured -- check your OpenClaw setup from Lesson 2.

### Exercise 2: A Tool for Your Work

Now build something relevant to YOUR role. Pick one and send it:

```
Build me [CHOOSE ONE]:
- A Python script that reads a CSV file and prints a summary
  with totals and averages
- A Python script that organizes files in the current directory
  into folders by file type
- A Python script that converts a markdown file to a styled
  HTML page

Tell me the session name when it is running.
```

Verify:

```bash
tmux ls
tmux attach -t <session-name>
```

Watch Claude Code build something useful for you. When it finishes, test the output with your actual files.

### Exercise 3: Research Then Build

This one combines what your employee does well with what Claude Code does well:

```
I want to automate [A REPETITIVE TASK FROM YOUR WORK].
First, research the best approach -- what tools exist, what method
would work for my situation. Give me a summary of your research.

Then, once I approve, use Claude Code to build a working prototype.
```

Notice the two phases. Your employee does the research first -- it has your context from MEMORY.md, it knows your work patterns, it can use web search. When you approve the approach, it delegates the coding to Claude Code via tmux. Two different capabilities, one result.

After you approve and it starts building, verify the same way:

```bash
tmux ls
tmux attach -t <session-name>
```

---

## What Just Happened

You built a real delegation chain:

| Layer                        | Who         | What They Did                                              |
| ---------------------------- | ----------- | ---------------------------------------------------------- |
| **You**                      | Manager     | Gave high-level instructions via Telegram                  |
| **Your Employee** (OpenClaw) | Coordinator | Spun up tmux sessions, launched Claude Code, reported back |
| **Claude Code**              | Coder       | Wrote actual code in a verifiable tmux session             |

This is the **two-tier delegation pattern** from Chapter 1 -- and you have seen it work. Not a textbook claim. You ran `tmux ls`, you attached to the session, you watched Claude Code writing code.

The key insight: **you managed, your employee coordinated**. You set one rule -- "use Claude Code for coding tasks" -- and your employee handled the mechanics: creating sessions, launching the right tool, reporting session names. You never typed a single tmux command into Telegram. Your job was deciding what to build and verifying the work was real.

Compare this to Chapter 3, where you used Claude Code directly. You typed every instruction. You watched every output. Now your employee handles the coordination. You say what you want built; it manages the rest.

---

## What Transfers

| Concept                     | What You Experienced                                                     |
| --------------------------- | ------------------------------------------------------------------------ |
| Rule-based delegation       | You set the rule once; your employee handled the mechanics every time    |
| tmux as infrastructure      | Background sessions let agents work while you verify                     |
| Verification over trust     | `tmux ls` and `tmux attach` prove work is real, not hallucinated         |
| Context stays with employee | Research and intent lived with your employee, coding went to Claude Code |
| You are the manager         | You decided what to build, your employee decided how to run it           |

---

## Try With AI

### Prompt 1: Parallel Delegation

```
I need two things built at the same time:
1. [TASK 1 FOR YOUR WORK]
2. [TASK 2 FOR YOUR WORK]

Run them in separate tmux sessions with Claude Code so they work
in parallel. Give me both session names.
```

**What you're learning:** Parallel delegation. Your employee creates two independent tmux sessions, each running Claude Code on a different task. Run `tmux ls` to see both sessions listed, and attach to each one to watch the work happen simultaneously.

### Prompt 2: Fix and Iterate

```
The tool you built in Exercise 2 needs a change:
[YOUR SPECIFIC FEEDBACK].

Send the fix to Claude Code in the same session.
```

**What you're learning:** Iteration through delegation. You give feedback in plain language, your employee sends the update to Claude Code. Same pattern from every lesson -- give intent, let the employee coordinate, verify the result.

### Prompt 3: Explain the Chain

```
Describe in plain language what happened across these exercises.
What tasks did you handle yourself (research, file creation)?
What tasks did Claude Code handle?
Why did I set the rule about using Claude Code for coding instead
of letting you write code yourself?
```

**What you're learning:** Getting your employee to articulate the delegation pattern. Its answer reveals whether it understands the principle: the right tool for the right job, with verification to make sure the work actually happened.
