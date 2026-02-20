---
sidebar_position: 5
title: "Your Permanent Toolkit"
chapter: 9
lesson: 4
layer: L2
duration_minutes: 20
description: "Transform scattered scripts into permanent commands you can run from anywhere, forever"
keywords:
  [
    "alias",
    "chmod",
    "shebang",
    "shell config",
    "bashrc",
    "zshrc",
    "PATH",
    "permanent commands",
    "tools directory",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Creating Permanent Commands"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "System Administration"
    measurable_at_this_level: "Student creates alias in shell config and verifies it persists across terminal sessions"

  - name: "Understanding Shell Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Digital Environment"
    measurable_at_this_level: "Student can explain the role of .bashrc/.zshrc and how aliases persist"

  - name: "Tool Organization Pattern"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student organizes scripts in ~/tools and creates reusable aliases"

learning_objectives:
  - objective: "Create a persistent shell alias for a Python script"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student creates alias that works after terminal restart"

  - objective: "Explain how shell config files make aliases permanent"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can describe the role of .bashrc/.zshrc in alias persistence"

  - objective: "Organize scripts into a personal tools directory"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student has ~/tools with executable scripts and working aliases"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (shell config files, aliases, executable permissions) within A2 limit"

differentiation:
  extension_for_advanced: "Add ~/tools to PATH instead of using aliases, explore creating bash completion for custom commands"
  remedial_for_struggling: "Focus on just one alias for sum-expenses. Get that working before adding more."

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Real Data and Permanent Tools"
  key_points:
    - "'If you have to remember where a tool lives, it is not a tool yet' is the lesson's thesis — the gap between 'script that works' and 'tool you actually use' is installation"
    - "The four-step installation process (organize in ~/tools, chmod +x, alias in shell config, source to reload) is a repeatable pattern for any script in any language"
    - "The shebang line (#!/usr/bin/env python3) is what makes a script executable without explicitly calling python3 — it bridges the gap between Python scripts and shell commands"
    - "The checkpoint (close terminal, reopen, verify command works) is the only way to prove the alias is truly permanent — not just loaded in the current session"
  misconceptions:
    - "Students think aliases are the same as running 'python3 script.py' — the alias makes the script available by name from any directory, which is a fundamentally different level of accessibility"
    - "Students may skip the checkpoint because 'it worked in this terminal' — the source command only affects the current session, and the alias is not truly permanent until it survives a terminal restart"
    - "Students confuse chmod +x (file permission) with the alias (shell shortcut) — both are needed but serve different purposes in making a script behave like a command"
  discussion_prompts:
    - "Have you ever rebuilt a script from scratch because you could not find where you saved the original? What would have been different if it were an installed command?"
    - "The lesson says 'you described the outcome, the agent handled every step.' How is specifying 'cat file.csv | sum-expenses' as the desired format a design decision?"
    - "Why does the agent check which shell you are using before adding the alias? What would go wrong if it guessed?"
  teaching_tips:
    - "Start with the frustration scenario: type 'sum-expenses' in a random directory and see 'command not found' — that visceral failure motivates the entire lesson"
    - "The command table (mkdir -p, chmod +x, alias, source) with memory tricks is worth putting on the board — students will reference it repeatedly"
    - "Make sure students actually close and reopen their terminals for the checkpoint — many will try 'source' alone and think they are done"
    - "Connect back to Chapter 8 Lesson 4: rename-screenshots.sh was a reusable script, but it was not installed as a command — this lesson shows the missing step"
  assessment_quick_check:
    - "Ask: 'What is the difference between having sum-expenses.py in a folder and having sum-expenses as an alias?' — tests understanding of tool installation"
    - "Ask students to explain what the shebang line does and why it matters for making scripts executable"
    - "Ask: 'You open a new terminal and sum-expenses is not found. What three things should you check?' — tests understanding of the full installation chain"
---

# Your Permanent Toolkit

It's next month. You're sitting in `~/finances/` with a fresh bank statement. You know you built a script that handles CSV parsing perfectly — it dealt with quoted fields, commas inside merchant names, the works. But where did you put it? Was it in `~/projects/chapter8/`? Or `~/Desktop/scripts/`? You try `python3 sum-expenses.py` and get `No such file or directory`. The script exists somewhere on your machine, and you can't find it.

**If you have to remember where a tool lives, it's not a tool yet.**

This isn't hypothetical. People build useful scripts, forget to make them permanent, and six months later rebuild the same thing from scratch because they can't find the original. The script worked. The workflow worked. But it was never installed, so it rotted in a forgotten folder. Twenty minutes of setup now saves hours of "I know I built this already" frustration later.

Real tools are available everywhere, instantly, by name. You type `ls` from any folder, not `/usr/bin/ls`. Your scripts deserve the same treatment. This lesson makes that happen.

## The Problem

Here's what that frustration looks like in practice:

```bash
cd ~/finances
cat january-statement.csv | python3 sum-expenses.py
```

**Output:**

```
python3: can't open file 'sum-expenses.py': No such file or directory
```

You'd need the full path:

```bash
cat january-statement.csv | python3 ~/projects/chapter8/sum-expenses.py
```

That works, but it's fragile. You have to remember the exact path. If you move the script, every command breaks. This is the gap between "a script that works" and "a tool you actually use."

## The Conversation

Ask Claude Code to solve this permanently:

```
You: I want to use sum-expenses from anywhere on my system.
Make it a permanent command I can run like: cat file.csv | sum-expenses
```

```
Claude Code: I'll set that up. First, let me create a dedicated
tools directory and move your script there.

[Runs: mkdir -p ~/tools]
[Runs: cp sum-expenses.py ~/tools/sum-expenses.py]
[Runs: chmod +x ~/tools/sum-expenses.py]

Now I need to check which shell you're using.

[Runs: echo $SHELL]
/bin/zsh

You're using zsh, so I'll add an alias to your .zshrc.

[Appends to ~/.zshrc:]
alias sum-expenses='python3 ~/tools/sum-expenses.py'

[Runs: source ~/.zshrc]

Done! Try it from any directory:
cat any_file.csv | sum-expenses
```

Notice what the agent did: it didn't just create the alias. It organized your script into `~/tools`, made it executable, checked your shell, and reloaded the config. You described the outcome you wanted. The agent handled every step to get there.

And notice where you refined the interaction: you specified the exact command format you wanted (`cat file.csv | sum-expenses`). That specificity told the agent you wanted a pipe-compatible alias, not just "make it accessible." Your clear intent shaped the solution.

## The Agent's Toolkit

Each command the agent ran serves a specific purpose:

| Command                | What It Does                       | Memory Trick                      |
| ---------------------- | ---------------------------------- | --------------------------------- |
| `mkdir -p ~/tools`     | Creates your personal tools folder | **p** = create **p**arents too    |
| `chmod +x script.py`   | Makes file executable              | **ch**ange **mod**e + e**x**ecute |
| `alias name='command'` | Creates a shortcut                 | Like a **nickname** for a command |
| `source ~/.zshrc`      | Reloads shell config               | Load the **source** of settings   |

## The Shebang Line

Your script starts with this line:

```python
#!/usr/bin/env python3
```

This is called a **shebang** (the `#!` characters). It tells your operating system: "When someone runs this file directly, use `python3` to execute it."

Without the shebang, your OS wouldn't know this is a Python script — it would try to run it as raw shell commands and fail. The `env` part finds `python3` wherever it's installed on your system, making the script portable across different setups.

## Shell Config Files

Every time you open a terminal, your shell reads a config file and runs whatever's inside it. Which file depends on your shell:

```bash
echo $SHELL
```

**Output (one of these):**

```
/bin/zsh     → Edit ~/.zshrc
/bin/bash    → Edit ~/.bashrc
```

When the agent added `alias sum-expenses='python3 ~/tools/sum-expenses.py'` to your `.zshrc`, it put the alias where your shell will find it every single time you open a terminal. That's what makes it permanent — not magic, just a config file that runs on startup.

`source ~/.zshrc` reloads that file in your current terminal so you don't have to close and reopen it.

## The Pattern

Whenever you build a script worth keeping:

```
"I want to use [script] from anywhere. Make it a permanent command."
```

The agent will follow the same steps: organize, make executable, alias, reload. This pattern works for any script in any language.

:::warning Checkpoint: Prove It's Permanent

This is the moment where a script becomes a tool. Don't skip it.

1. Close your terminal completely
2. Open a brand new terminal
3. Navigate to your home directory: `cd ~`
4. Type: `sum-expenses`
5. If you see usage info or an error about missing input — your command is installed
6. If you see "command not found" — go back and check your alias

The new terminal has no memory of what you did before. It only knows what's in your shell config file. If `sum-expenses` works here, it works everywhere, forever.

:::

Your tools are installed, permanent, and available from any directory on your system. You can sum any CSV with a single pipe command. But summing is all they do — they can't tell the difference between a pharmacy visit and a grocery run. Your accountant doesn't want "Total: $4,215.52." They want medical, charitable, and business broken out separately. And buried in your bank data, Dr. Pepper is waiting to be misclassified as a doctor visit.

---

## Try With AI

### Prompt 1: Batch Install Multiple Scripts

```
I have 3 scripts I use regularly: sum.py, sum-expenses.py, and a
count-lines.py I wrote earlier. Help me set up ~/tools with all of
them and create aliases for each one. Show me the final state of
my .zshrc aliases section.
```

**What you're learning:** Batch tool installation. Instead of repeating the process three times, you describe the full scope and the agent handles the repetitive setup for multiple scripts at once. This is the "300 files vs 3 files" principle from Chapter 8 — when the task is repetitive, hand it to the agent.

### Prompt 2: PATH vs Aliases

```
Instead of aliases, can I add ~/tools to my PATH so I can run
scripts directly by name without an alias? What are the pros and
cons of PATH vs aliases?
```

**What you're learning:** Advanced tool installation. PATH modification is how professional developers make tools available system-wide. The agent explains when aliases are sufficient and when modifying PATH is the better approach — and helps you understand the tradeoff between simplicity and flexibility.
