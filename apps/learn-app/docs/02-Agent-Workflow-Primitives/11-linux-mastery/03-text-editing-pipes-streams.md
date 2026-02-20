---
sidebar_position: 3
chapter: 11
lesson: 3
title: "Text Editing, Pipes & I/O Streams"
description: "Edit configuration files with nano, connect commands with pipes, and control where output goes using I/O redirection -- the Unix philosophy in action."
keywords: ["nano", "pipes", "stdin", "stdout", "stderr", "redirection", "man pages", "I/O streams", "unix philosophy", "linux text editing"]
duration_minutes: 50

# HIDDEN SKILLS METADATA
skills:
  - name: "Text Editing with nano"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can open, edit, save, and exit files using nano with keyboard shortcuts"

  - name: "I/O Stream Understanding"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can identify and distinguish stdin, stdout, and stderr in command output"

  - name: "Pipe Operator Usage"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can chain two or more commands using the pipe operator to transform data"

  - name: "Output Redirection"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can redirect stdout and stderr to files using >, >>, 2>, and 2>&1"

  - name: "Error Stream Management"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can separate or combine stdout and stderr into different files"

  - name: "Self-Help with man and --help"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can use man pages and --help to discover command options independently"

learning_objectives:
  - objective: "Edit files using nano including creating content, saving with Ctrl+O, and exiting with Ctrl+X"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates a configuration file with nano, adds content, saves, and verifies with cat"

  - objective: "Chain commands using pipes and redirect output and errors to files"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student builds multi-command pipelines and redirects stdout and stderr to separate files"

  - objective: "Use man pages and --help to discover command options without external resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student uses man to find a flag they haven't seen before and applies it correctly"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "nano basics (open, edit, save Ctrl+O, exit Ctrl+X)"
    - "stdin/stdout/stderr streams (three data channels)"
    - "Pipe operator | (connecting command output to input)"
    - "Output redirection (> overwrites, >> appends)"
    - "Error redirection (2>, 2>&1)"
    - "Self-help with man pages and --help"
  assessment: "6 concepts (within B1 limit of 7-10) -- manageable for 50-minute lesson"

differentiation:
  extension_for_advanced: "Explore vim basics (modes, :wq, dd, yy). Build complex pipelines with tee to split output to both file and screen simultaneously. Investigate process substitution with <() syntax."
  remedial_for_struggling: "Focus on nano and basic pipe (command | command) only. Skip error redirection until comfortable with stdout redirection. Practice with simple echo commands before moving to multi-step pipelines."

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "CLI Foundations and Navigation"
  key_points:
    - "The Unix philosophy (small tools connected by pipes) is the design principle behind all Linux command-line work — this recurs in bash scripting (lesson 6) and text processing (lesson 7)"
    - "Three I/O streams (stdin=0, stdout=1, stderr=2) are separate channels — understanding this distinction is essential for agent log management in production (lesson 14)"
    - "The difference between > (overwrite) and >> (append) prevents data loss — agents in production always use >> for logs"
    - "nano is the safe default editor for remote servers — students must know Ctrl+O (save) and Ctrl+X (exit) cold before touching production configs"
  misconceptions:
    - "Students think stdout and stderr are the same because both display on screen — demonstrate with 2> to prove they are separate channels that can be redirected independently"
    - "Students confuse > (overwrite) with >> (append) and accidentally destroy log files — emphasize that > wipes the file first, >> adds to the end"
    - "Students expect pipes to pass error messages too — pipes only connect stdout to stdin, stderr bypasses the pipe entirely unless explicitly redirected"
  discussion_prompts:
    - "Your AI agent writes activity logs to stdout and error messages to stderr. Why is separating these streams useful for monitoring a production system?"
    - "The Unix philosophy says each tool should do one thing well. How does this compare to building a single large program that does everything? What are the tradeoffs?"
  teaching_tips:
    - "Demo the three-stream concept live: run ls /home /nonexistent 2>errors.txt and show students that normal output appears on screen while errors go to the file — this is the 'aha' moment"
    - "Build the three-command pipeline (du -sh * | sort -rh | head -5) incrementally — run each stage alone first so students see the data transformation step by step"
    - "The nano shortcut table is a handout moment — students will reference it repeatedly during exercises and in later lessons"
    - "Spend less time on man pages (students already saw --help in lesson 2) and more time on pipe chains — piping is the harder concept and the more useful one"
  assessment_quick_check:
    - "Ask students to redirect stdout to output.txt and stderr to errors.txt from a single command (expected: command > output.txt 2> errors.txt)"
    - "Ask: what does the pipe operator | connect? (Expected: stdout of one command to stdin of the next)"
    - "Have students save and exit nano — if they cannot do Ctrl+O then Ctrl+X from memory, they need more practice"

teaching_approach: "Problem-solution pairs (How do I...? scenarios)"
modality: "Scenario-driven discovery"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-09"
version: "1.0.0"
---

# Text Editing, Pipes & I/O Streams

## The Missing Pieces

You can create files and navigate directories. But what happens when you need to *change* what's inside a file? Or when one command's output is exactly what another command needs as input?

In the previous two lessons, you used `cat` to view files and `touch` to create empty ones. Today, you gain the ability to edit, and you learn the Unix philosophy that makes Linux powerful: **small tools connected by pipes**. Each command does one thing well, and you combine them like building blocks. This is also how your Digital FTEs process data in production: reading input, transforming it, writing output, and logging errors.

---

## How Do I Edit a Configuration File?

Every agent you deploy needs configuration: ports, hostnames, API keys, debug flags. The nano editor lets you create and modify these files directly from the terminal.

### Opening and Editing with nano

```bash
nano agent.conf
```

**Output:**
```
  GNU nano 7.2              agent.conf              New File

^G Help    ^O Write Out  ^W Where Is  ^K Cut       ^T Execute
^X Exit    ^R Read File  ^\ Replace   ^U Paste     ^J Justify
```

You're inside the nano editor. The `^` symbol means "Ctrl key." Type these three lines:

```
port=8000
host=0.0.0.0
debug=false
```

Now save and exit:
1. **Ctrl+O** -- save. Confirm the filename with Enter. Nano reports `[ Wrote 3 lines ]`.
2. **Ctrl+X** -- exit back to your terminal prompt.

Verify your edit:

```bash
cat agent.conf
```

**Output:**
```
port=8000
host=0.0.0.0
debug=false
```

### Essential nano Shortcuts

| Shortcut | Action |
|----------|--------|
| **Ctrl+O** | Save (Write Out) |
| **Ctrl+X** | Exit nano |
| **Ctrl+K** | Cut entire line |
| **Ctrl+U** | Paste cut line |
| **Ctrl+W** | Search for text |
| **Ctrl+G** | Show help screen |

These six shortcuts cover 90% of what you need.

---

## Where Does Command Output Go?

Before learning pipes, you need to understand *streams* -- the three channels every Linux command uses for data.

### The Three Streams

Every command has three data channels:

| Stream | Number | Purpose | Default Destination |
|--------|--------|---------|-------------------|
| **stdin** | 0 | Input to the command | Keyboard |
| **stdout** | 1 | Normal output | Screen |
| **stderr** | 2 | Error messages | Screen |

Both stdout and stderr display on your screen by default. But they are *separate channels* -- and you can redirect them independently. Watch:

```bash
ls /home /nonexistent_directory
```

**Output:**
```
ls: cannot access '/nonexistent_directory': No such file or directory
/home:
yourname
```

Two things happened: the error message came through **stderr** (stream 2), and the directory listing came through **stdout** (stream 1). They look the same on screen, but Linux treats them as separate channels. This distinction becomes critical when you need to log errors separately from regular output.

---

## How Do I Connect Commands Together?

The pipe operator `|` takes the stdout of one command and sends it as stdin to the next command. This is the heart of the Unix philosophy.

### Counting Files in a Directory

**Problem:** "How many items are in my home directory?"

```bash
ls ~ | wc -l
```

**Output:**
```
6
```

`ls ~` listed the items (stdout), the pipe sent that list to `wc -l`, which counted the lines.

### Finding a Specific Process

**Problem:** "Is Python running on this system?"

```bash
ps aux | grep python
```

**Output:**
```
yourname  1234  0.5  1.2 123456 12345 ?  S  10:30  0:05 python3 agent_main.py
yourname  5678  0.0  0.0   6789   890 pts/0  S+ 11:00  0:00 grep python
```

`ps aux` listed all running processes. The pipe sent that list to `grep python`, which filtered for lines containing "python."

### Finding the Largest Items

**Problem:** "What are the 5 largest items in this directory?"

```bash
du -sh * | sort -rh | head -5
```

**Output:**
```
1.2G    node_modules
256M    data
128M    logs
64M     backups
12M     agent_main.py
```

Three commands chained: `du -sh *` shows sizes, `sort -rh` sorts largest first, `head -5` takes the top 5. This pipeline would require writing a script in most languages. In Linux, it's one line.

---

## How Do I Save Command Output to a File?

Redirection operators control where stdout goes instead of the screen.

### Overwrite with >

```bash
echo "Agent started successfully" > agent.log
cat agent.log
```

**Output:**
```
Agent started successfully
```

The `>` operator redirected stdout from the screen into `agent.log`. If the file existed, its contents are replaced.

### Append with >>

```bash
echo "Processing request #1" >> agent.log
echo "Processing request #2" >> agent.log
cat agent.log
```

**Output:**
```
Agent started successfully
Processing request #1
Processing request #2
```

The `>>` operator adds to the end without erasing what was there. This is essential for log files -- you want to accumulate entries, not overwrite them.

---

## How Do I Handle Error Messages?

When agents run in production, you want errors in a separate log file so you can monitor them without sifting through normal output.

### Redirect Errors with 2>

```bash
ls /home /nonexistent_directory 2> errors.txt
```

**Output:**
```
/home:
yourname
```

The normal output appeared on screen, but the error message went into `errors.txt`. Let's verify:

```bash
cat errors.txt
```

**Output:**
```
ls: cannot access '/nonexistent_directory': No such file or directory
```

The `2>` targets stream 2 (stderr) specifically. Normal output (stream 1) still goes to the screen.

### Separate stdout and stderr into Different Files

```bash
ls /home /nonexistent_directory > stdout.txt 2> stderr.txt
cat stdout.txt
```

**Output:**
```
/home:
yourname
```

```bash
cat stderr.txt
```

**Output:**
```
ls: cannot access '/nonexistent_directory': No such file or directory
```

Clean separation. In production, this lets you monitor error logs independently from activity logs.

### Combine Both Streams into One File

```bash
ls /home /nonexistent_directory > combined.txt 2>&1
cat combined.txt
```

**Output:**
```
ls: cannot access '/nonexistent_directory': No such file or directory
/home:
yourname
```

The `2>&1` means "send stderr to wherever stdout is going." Since stdout goes to `combined.txt`, errors go there too. The production pattern for agent logging uses this:

```bash
python3 agent_main.py > /var/log/agent-output.log 2>&1
```

**Output:**
```
(no screen output -- all output captured to log file)
```

---

## How Do I Look Up Commands I Don't Know?

You don't need to memorize every flag. Two built-in tools make you self-sufficient.

### man Pages: The Full Manual

```bash
man ls
```

**Output:**
```
LS(1)                    User Commands                    LS(1)

NAME
       ls - list directory contents

DESCRIPTION
       -a, --all              do not ignore entries starting with .
       -l                     use a long listing format
       -h, --human-readable   print sizes like 1K 234M 2G
```

Navigate with arrow keys, search with `/term` (press **n** for next match), quit with **q**.

### --help: The Quick Reference

```bash
ls --help
```

**Output:**
```
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
  ...
```

Use `--help` for a quick reminder. Use `man` for full details and examples. **The habit to build:** reach for `man` or `--help` before searching the web. The answer is already on your system.

---

## Exercises

### Exercise 1: Create and Edit a Configuration File

**Task:** Create a file called `agent.conf` with nano. Add these three configuration lines:

```
port=8000
host=0.0.0.0
debug=false
```

Save with Ctrl+O, exit with Ctrl+X.

**Verify:**

```bash
cat agent.conf
```

**Expected Output:**
```
port=8000
host=0.0.0.0
debug=false
```

If you see your three lines, you've successfully edited with nano.

### Exercise 2: Build a Pipeline with Error Handling

**Task:** Use pipes to count how many `.conf` files exist anywhere under `/etc`, while sending any permission errors to a separate file:

```bash
find /etc -name "*.conf" 2>/dev/null | wc -l
```

**Expected Output:**
```
42
```

(Your number will vary depending on your system. The important thing is you get a number, not a flood of "Permission denied" errors.)

**What happened:** `find` searched for `.conf` files. `2>/dev/null` discarded permission errors (sent them to `/dev/null`, the system's black hole). The pipe sent the file list to `wc -l` for counting.

### Exercise 3: Separate stdout and stderr

**Task:** Run a command that produces both normal output and errors, redirect them to separate files:

```bash
ls /home /nonexistent_path > stdout.txt 2> stderr.txt
```

**Verify:**

```bash
cat stdout.txt
```

**Expected Output:**
```
/home:
yourname
```

```bash
cat stderr.txt
```

**Expected Output:**
```
ls: cannot access '/nonexistent_path': No such file or directory
```

If stdout.txt has the listing and stderr.txt has the error, you've successfully separated the streams.

---

## Try With AI

**Build a Monitoring Pipeline:**

```
I'm learning Linux pipes and redirection. Help me build a pipeline that:
1. Lists all running processes (ps aux)
2. Filters for only processes using more than 1% CPU
3. Sorts them by CPU usage (highest first)
4. Shows only the top 10
5. Saves the result to a file called cpu-hogs.txt

Show me the complete pipeline and explain what each part does.
```

**What you're learning:** Combining multiple pipe stages into a practical monitoring command. Each stage transforms the data further, demonstrating how small Unix tools compose into powerful workflows you'll use to monitor Digital FTEs.

**Design an Agent Log System:**

```
I want to set up logging for an AI agent running on a Linux server. The agent writes normal activity to stdout and errors to stderr. Help me design:
1. A command to run the agent with stdout going to activity.log and stderr going to errors.log
2. A pipeline to check errors.log for the word "CRITICAL" and count how many critical errors occurred
3. A command to combine both logs into a single combined.log with timestamps

Explain the redirection operators used in each command.
```

**What you're learning:** Applying I/O redirection to a real production scenario. Managing separate log streams is fundamental to operating Digital FTEs -- you need to know what's working (stdout) and what's failing (stderr) at a glance.

**Explore nano's Editing Power:**

```
I'm editing configuration files on a remote Linux server using nano.
Show me how to:
1. Search for a specific setting (like "port=8000") in a large config file
2. Replace all occurrences of one value with another (like changing port 8000 to 9000)
3. Copy a block of 5 lines and paste them elsewhere in the file
4. Jump directly to line 47 of the file

Show the exact keystroke sequences for each operation.
```

**What you're learning:** Terminal editors have powerful features hidden behind keyboard shortcuts. AI can map your editing goals to specific keystrokes, revealing capabilities that manual exploration would miss. These patterns transfer to any remote server where graphical editors aren't available.

:::note Safety Reminder
When using pipes and redirection, be careful with the `>` operator -- it overwrites files without warning. Use `>>` to append instead. When editing configuration files with nano, always make a backup first: `cp config.conf config.conf.bak`. On production servers, test complex pipelines with `echo` or `head` first to verify they produce expected output before piping to destructive commands like `rm` or `tee`.
:::
