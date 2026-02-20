---
sidebar_position: 2
chapter: 11
lesson: 2
title: "File Operations Mastery"
description: "Learn to create, copy, move, delete, and read files and directories — the building blocks for organizing agent workspaces on Linux servers."
duration_minutes: 45
keywords: ["linux", "file operations", "mkdir", "cp", "mv", "rm", "cat", "head", "tail", "wildcards", "globbing", "cli"]

# HIDDEN SKILLS METADATA
skills:
  - name: "File and Directory Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can create files with touch and nested directory structures with mkdir -p"

  - name: "File Copying"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can copy individual files and entire directories recursively using cp and cp -r"

  - name: "File Moving and Renaming"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can move files between directories and rename files using mv"

  - name: "Safe File Deletion"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student demonstrates safe deletion practices using rm -i before rm -rf, and explains the dangers of recursive force deletion"

  - name: "File Content Reading"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can read files using cat, head, tail, and less, choosing the right tool for the situation"

  - name: "Wildcards and Globbing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can use *, ?, and [] patterns to match groups of files"

learning_objectives:
  - objective: "Create files and nested directory structures for agent workspace organization using touch and mkdir -p"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student builds a multi-level agent workspace and verifies structure with ls -R"

  - objective: "Copy, move, rename, and safely delete files and directories using cp, mv, and rm with appropriate flags"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student completes file manipulation exercises and verifies results with ls"

  - objective: "Select and use the appropriate file reading command (cat, head, tail, less) based on the situation"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student reads files of varying sizes and explains when to use each command"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "Creating files and directories (touch, mkdir -p)"
    - "Copying files and directories (cp, cp -r)"
    - "Moving and renaming (mv)"
    - "Safe deletion (rm -i, rm -r, rm -rf)"
    - "Reading file contents (cat, head, tail, less)"
    - "Wildcards and globbing (*, ?, [])"
  assessment: "6 concepts at B1 level (within 7-10 limit). Each builds on previous, reducing effective load."

differentiation:
  extension_for_advanced: "Explore find command for locating files by name, size, or modification date. Investigate xargs for chaining commands with file lists. Research rsync for efficient file synchronization across servers."
  remedial_for_struggling: "Focus on touch, mkdir, and cp first. Practice creating simple flat directory structures before nested ones. Use ls after every command to confirm what happened."

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "CLI Foundations and Navigation"
  key_points:
    - "mkdir -p is the go-to for workspace creation — it creates all parent directories and never fails on existing dirs, used repeatedly in deployment lessons (lesson 14)"
    - "rm -rf is permanent with no undo — the safe pattern (ls first, rm -i to verify, then rm -rf) must become habit before students touch production servers"
    - "Wildcards (*, ?, []) are not just for listing — they apply to cp, mv, rm and recur in bash scripting (lesson 6) and text processing (lesson 7)"
    - "Choosing the right file reader (cat vs head vs tail vs less) depends on file size and what you need — tail is the default for agent debugging"
  misconceptions:
    - "Students assume deleted files go to a trash folder like on Windows/Mac — Linux rm is permanent, there is no recycle bin"
    - "Students confuse cp (creates a duplicate, original stays) with mv (relocates, original gone) — use the photocopy vs moving boxes analogy"
    - "Students think the ? wildcard matches any number of characters like * — it matches exactly one character, which is how you exclude multi-digit files"
  discussion_prompts:
    - "If Linux has no recycle bin, what strategies would you use to protect against accidental deletion of critical agent configuration files?"
    - "You have 3 agents each producing daily log files. How would you use wildcards to clean up logs older than 7 days without touching today's files?"
  teaching_tips:
    - "Build the agent workspace live with students using mkdir -p and brace expansion — seeing {src,config,logs,data} expand is a powerful demo"
    - "The rm -rf danger box is a whiteboard moment — draw what happens when you run rm -rf / and why the system requires confirmation for directories"
    - "Spend extra time on wildcards — students breeze through file creation/copying but stumble on pattern matching, which is critical for lesson 7 (text processing)"
    - "Have students run ls after every command to build the verify-after-action habit before they reach production scenarios"
  assessment_quick_check:
    - "Ask: create a nested directory structure three levels deep with one command (expected: mkdir -p a/b/c)"
    - "Ask: what is the difference between > and >> for file content, and between cp and mv for file location?"
    - "Give students a directory with files agent-1.log through agent-12.log and ask them to list only single-digit ones (expected: ls agent-?.log)"

teaching_approach: "Scaffolded practice (build an agent workspace step by step)"
modality: "Hands-on discovery"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-09"
version: "1.0.0"
---

# File Operations Mastery

In Lesson 1, you learned to navigate the Linux filesystem -- moving between directories, understanding paths, and building a mental map of where things live. Now it's time to shape that filesystem.

Every AI agent you deploy needs a workspace: directories for source code, configuration files, log output, and data storage. Before any agent can run, someone has to create that structure, populate it with files, and maintain it over time. That someone is you, and your tools are the file operation commands you'll learn in this lesson.

Think of file operations as the construction tools of the CLI architect. Navigation was reading the blueprint. Now you're picking up the hammer, saw, and measuring tape. By the end of this lesson, you'll be able to build, organize, and manage the directory structures that your Digital FTEs depend on.

---

## Creating Files and Directories

Every workspace starts empty. Let's build one from scratch.

### Creating Empty Files with touch

The `touch` command creates an empty file. If the file already exists, it updates its timestamp without changing content.

```bash
cd ~
touch my-first-file.txt
ls -l my-first-file.txt
```

**Output:**
```
-rw-r--r-- 1 yourname yourname 0 Feb  9 14:30 my-first-file.txt
```

Notice the file size is `0` -- `touch` creates the file but puts nothing in it. This is useful for creating placeholder files, empty logs, or files you'll populate later.

You can create multiple files at once:

```bash
touch agent.log config.yaml README.md
ls -l agent.log config.yaml README.md
```

**Output:**
```
-rw-r--r-- 1 yourname yourname 0 Feb  9 14:31 agent.log
-rw-r--r-- 1 yourname yourname 0 Feb  9 14:31 config.yaml
-rw-r--r-- 1 yourname yourname 0 Feb  9 14:31 README.md
```

### Creating Directories with mkdir

Use `mkdir` to create directories:

```bash
mkdir my-agent
ls -d my-agent
```

**Output:**
```
my-agent
```

But what if you need a nested structure? This fails:

```bash
mkdir my-agent/src/handlers
```

**Output:**
```
mkdir: cannot create directory 'my-agent/src/handlers': No such file or directory
```

The parent directory `my-agent/src` doesn't exist yet. The `-p` flag solves this by creating all parent directories as needed:

```bash
mkdir -p my-agent/src/handlers
ls -R my-agent
```

**Output:**
```
my-agent:
src

my-agent/src:
handlers

my-agent/src/handlers:
```

The `-p` flag is your go-to for building workspace structures. It never fails because missing parents exist, and it doesn't complain if directories already exist.

### Building a Complete Agent Workspace

Let's build a realistic workspace structure using brace expansion -- a shell feature that generates multiple directory names from a pattern:

```bash
mkdir -p ~/agents/customer-bot/{src,config,logs,data}
ls -R ~/agents/customer-bot
```

**Output:**
```
/home/yourname/agents/customer-bot:
config  data  logs  src

/home/yourname/agents/customer-bot/config:

/home/yourname/agents/customer-bot/data:

/home/yourname/agents/customer-bot/logs:

/home/yourname/agents/customer-bot/src:
```

One command created a complete agent workspace with four organized subdirectories. This is the kind of structure your deployed agents will use: source code in `src`, settings in `config`, runtime output in `logs`, and persistent storage in `data`.

---

## Copying Files and Directories

Once files exist, you often need duplicates -- backups, templates, or copies for different environments.

### Copying a Single File

```bash
cd ~/agents/customer-bot
touch config/settings.yaml
cp config/settings.yaml config/settings.yaml.backup
ls config/
```

**Output:**
```
settings.yaml  settings.yaml.backup
```

The `cp` command takes two arguments: source and destination. If the destination is a filename, it creates a copy with that name. If the destination is a directory, it copies the file into that directory keeping the original name:

```bash
cp config/settings.yaml data/
ls data/
```

**Output:**
```
settings.yaml
```

### Copying Directories Recursively

To copy an entire directory and its contents, use the `-r` (recursive) flag:

```bash
cp -r config config-staging
ls -R config-staging/
```

**Output:**
```
config-staging/:
settings.yaml  settings.yaml.backup
```

Without `-r`, attempting to copy a directory fails:

```bash
cp config config-test
```

**Output:**
```
cp: -r not specified; omitting directory 'config'
```

This is a safety mechanism -- copying directories involves potentially thousands of files, so the system requires you to explicitly confirm with `-r`.

---

## Moving and Renaming Files

The `mv` command serves two purposes: moving files to a different location and renaming them. Under the hood, both operations are the same -- changing where a file's name points in the filesystem.

### Moving a File to Another Directory

```bash
touch src/main.py
mv src/main.py src/handlers/
ls src/handlers/
```

**Output:**
```
main.py
```

The file is no longer in `src/` -- it has been moved to `src/handlers/`.

### Renaming a File

```bash
mv src/handlers/main.py src/handlers/agent_main.py
ls src/handlers/
```

**Output:**
```
agent_main.py
```

Same command, different effect. When the source and destination are in the same directory, `mv` renames. When they're in different directories, `mv` moves.

### Moving and Renaming at the Same Time

```bash
mv src/handlers/agent_main.py src/app.py
ls src/
```

**Output:**
```
app.py  handlers
```

The file was moved from `src/handlers/` to `src/` and renamed to `app.py` in a single operation.

### Renaming Directories

`mv` works on directories too, without needing any special flags:

```bash
mv config-staging config-production
ls -d config-production
```

**Output:**
```
config-production
```

---

## Deleting Files Safely

Deletion on Linux is permanent. There is no recycle bin, no trash folder, no undo. When a file is deleted, it's gone. This makes safe deletion practices essential.

### Safe Deletion with rm -i

Always start with `rm -i` (interactive mode), which asks for confirmation before each deletion:

```bash
touch temp-file.txt
rm -i temp-file.txt
```

**Output:**
```
rm: remove regular empty file 'temp-file.txt'? y
```

You must type `y` and press Enter to confirm. This gives you a chance to catch mistakes before they become permanent.

### Deleting Multiple Files

```bash
touch old-1.log old-2.log old-3.log
rm -i old-*.log
```

**Output:**
```
rm: remove regular empty file 'old-1.log'? y
rm: remove regular empty file 'old-2.log'? y
rm: remove regular empty file 'old-3.log'? y
```

Each file requires confirmation. For three files, this is manageable. For three hundred, you'll need the recursive approach below -- but only after verifying with `ls` first.

### Deleting Directories with rm -r

To delete a directory and everything inside it:

```bash
rm -ri config-production
```

**Output:**
```
rm: descend into directory 'config-production'? y
rm: remove regular empty file 'config-production/settings.yaml'? y
rm: remove regular empty file 'config-production/settings.yaml.backup'? y
rm: remove directory 'config-production'? y
```

The `-r` flag means recursive (delete contents first, then the directory). Combined with `-i`, you confirm each step.

:::danger rm -rf: The Most Dangerous Command in Linux

The command `rm -rf` removes files and directories recursively (`-r`) without any confirmation (`-f` = force). It executes instantly and cannot be undone.

**Before using rm -rf, ALWAYS verify what will be deleted:**

```bash
# STEP 1: See what will be affected
ls target-directory/

# STEP 2: Only after confirming the contents are correct
rm -rf target-directory/
```

**Commands you must NEVER run:**

- `rm -rf /` -- Deletes every file on the entire system
- `rm -rf ~` -- Deletes your entire home directory and all your work
- `rm -rf *` in the wrong directory -- Deletes everything in the current directory

**The safe pattern**: Use `rm -i` first to see what will be deleted. Once you've confirmed the target is correct, then use `rm -rf` if needed for speed.

:::

---

## Reading File Contents

Agents produce output: logs, reports, data files. You need to read these files without opening a graphical editor.

### Reading Entire Files with cat

The `cat` command prints an entire file to the terminal:

```bash
cd ~/agents/customer-bot
echo "agent_name: customer-bot" > config/settings.yaml
echo "port: 8080" >> config/settings.yaml
echo "log_level: info" >> config/settings.yaml
cat config/settings.yaml
```

**Output:**
```
agent_name: customer-bot
port: 8080
log_level: info
```

`cat` is ideal for short files (under ~50 lines). For long files, it floods your terminal with text.

### Reading the Beginning with head

The `head` command shows the first lines of a file. By default, it shows 10 lines. Use `-n` to specify how many:

```bash
# Create a longer file for demonstration
for i in $(seq 1 20); do echo "Log entry $i: Agent processed request" >> logs/agent.log; done
head -n 5 logs/agent.log
```

**Output:**
```
Log entry 1: Agent processed request
Log entry 2: Agent processed request
Log entry 3: Agent processed request
Log entry 4: Agent processed request
Log entry 5: Agent processed request
```

### Reading the End with tail

The `tail` command shows the last lines of a file. This is especially useful for log files where the most recent entries are at the bottom:

```bash
tail -n 3 logs/agent.log
```

**Output:**
```
Log entry 18: Agent processed request
Log entry 19: Agent processed request
Log entry 20: Agent processed request
```

When debugging an agent, `tail` is usually your first command -- it shows you what happened most recently.

### Scrolling Through Long Files with less

For files too long for `cat` but where you need to read more than just the beginning or end, use `less`:

```bash
less logs/agent.log
```

`less` opens the file in a scrollable viewer:

| Key | Action |
|-----|--------|
| **Arrow keys** | Scroll up/down line by line |
| **Space** | Scroll down one page |
| **b** | Scroll up one page |
| **/search-term** | Search forward for text |
| **n** | Jump to next search match |
| **q** | Quit and return to terminal |

`less` doesn't load the entire file into memory, so it works on files of any size -- even gigabyte log files from long-running agents.

### When to Use Each Reading Command

| Command | Best For | Example |
|---------|----------|---------|
| `cat` | Short files (under 50 lines) | Config files, small scripts |
| `head -n N` | Checking file format or headers | CSV headers, log format |
| `tail -n N` | Recent log entries, latest errors | Agent debugging |
| `less` | Exploring large files interactively | Full log analysis |

---

## Wildcards and Globbing

When you manage multiple agents, each producing logs, configs, and data files, you need to work with groups of files at once. Wildcards let you match patterns instead of typing every filename.

### The * Wildcard (Any Characters)

The `*` matches zero or more characters:

```bash
cd ~/agents/customer-bot/logs
touch agent.log error.log access.log debug.log
ls *.log
```

**Output:**
```
access.log  agent.log  debug.log  error.log
```

You can use `*` anywhere in a pattern:

```bash
touch report-jan.csv report-feb.csv report-mar.csv summary.csv
ls report-*.csv
```

**Output:**
```
report-feb.csv  report-jan.csv  report-mar.csv
```

The pattern `report-*.csv` matched all files starting with `report-` and ending with `.csv`, excluding `summary.csv`.

### The ? Wildcard (Single Character)

The `?` matches exactly one character:

```bash
touch agent-1.log agent-2.log agent-3.log agent-10.log
ls agent-?.log
```

**Output:**
```
agent-1.log  agent-2.log  agent-3.log
```

Notice `agent-10.log` was not matched -- `?` matches exactly one character, not two. This precision helps when you need to target specific file groups.

### The [] Wildcard (Character Set)

Square brackets match any single character from a set:

```bash
ls agent-[12].log
```

**Output:**
```
agent-1.log  agent-2.log
```

You can also specify ranges:

```bash
touch file-a.txt file-b.txt file-c.txt file-1.txt file-2.txt
ls file-[a-c].txt
```

**Output:**
```
file-a.txt  file-b.txt  file-c.txt
```

```bash
ls file-[0-9].txt
```

**Output:**
```
file-1.txt  file-2.txt
```

### Combining Wildcards

Wildcards combine to create precise patterns:

```bash
ls *-[0-9].log
```

**Output:**
```
agent-1.log  agent-2.log  agent-3.log
```

This matched any file ending in a single digit followed by `.log`.

---

## Getting Help: man Pages and --help

When you encounter an unfamiliar command or need to check a specific flag, Linux has built-in documentation.

### Quick Help with --help

Most commands support a `--help` flag that prints a usage summary:

```bash
cp --help
```

**Output (abbreviated):**
```
Usage: cp [OPTION]... SOURCE DEST
Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

  -r, -R, --recursive    copy directories recursively
  -i, --interactive       prompt before overwrite
  -v, --verbose           explain what is being done
```

This gives you a fast reminder of available options without leaving your terminal.

### Detailed Documentation with man

The `man` command opens the full manual page for any command:

```bash
man cp
```

This opens a detailed reference in `less` (the same viewer you learned earlier). Navigate with the same keys:

| Key | Action |
|-----|--------|
| **Arrow keys** | Scroll up/down |
| **/pattern** | Search for text |
| **n** | Next search match |
| **q** | Quit man page |

Man pages are organized into sections: NAME, SYNOPSIS, DESCRIPTION, OPTIONS, and EXAMPLES. When you need to understand a specific flag, search with `/` followed by the flag name (like `/-r`).

---

## Exercises

### Exercise 1: Build an Agent Workspace

**Task:** Create a complete workspace for an agent called `customer-bot` with subdirectories for source code, configuration, logs, and data.

```bash
mkdir -p ~/agents/customer-bot/{src,config,logs,data}
```

**Verify your work:**

```bash
ls -R ~/agents/customer-bot
```

**Expected output:**
```
/home/yourname/agents/customer-bot:
config  data  logs  src

/home/yourname/agents/customer-bot/config:

/home/yourname/agents/customer-bot/data:

/home/yourname/agents/customer-bot/logs:

/home/yourname/agents/customer-bot/src:
```

You should see four subdirectories: `config`, `data`, `logs`, and `src`.

### Exercise 2: Create, Copy, and Move Files

**Task:** Create a configuration file, copy it as a backup, then move the backup to a different directory.

```bash
cd ~/agents/customer-bot
echo "port: 8080" > config/app.yaml
cp config/app.yaml config/app.yaml.backup
mv config/app.yaml.backup data/
```

**Verify your work:**

```bash
ls config/ data/
```

**Expected output:**
```
config/:
app.yaml  settings.yaml

data/:
app.yaml.backup  settings.yaml
```

The original `app.yaml` stays in `config/`, while `app.yaml.backup` was copied then moved to `data/`.

### Exercise 3: Wildcards in Action

**Task:** Create five numbered log files and use wildcards to list only those files.

```bash
cd ~/agents/customer-bot/logs
touch agent-1.log agent-2.log agent-3.log agent-4.log agent-5.log
```

**Verify your work:**

```bash
ls agent-*.log
```

**Expected output:**
```
agent-1.log  agent-2.log  agent-3.log  agent-4.log  agent-5.log
```

Now use the `?` wildcard to match only single-digit agent logs:

```bash
ls agent-?.log
```

**Expected output:**
```
agent-1.log  agent-2.log  agent-3.log  agent-4.log  agent-5.log
```

All five match because each has exactly one character between `agent-` and `.log`.

---

## Try With AI

**Design an Agent Workspace:**

```
I'm deploying 3 AI agents that each need directories for source code,
configuration, logs, and data. Design the directory structure and give
me the mkdir commands to create it all. The agents are:
1. customer-support-bot (handles tickets)
2. analytics-engine (processes data)
3. content-moderator (reviews submissions)

Also suggest what files would go in each directory.
```

**What you're learning:** Translating deployment requirements into filesystem structure. The AI can suggest organizational patterns you might not consider, like shared configuration directories or centralized log locations.

**Understand Copy vs Move:**

```
Explain the difference between cp and mv using a real-world analogy.
Then give me 3 specific scenarios for managing AI agent deployments
where I would use cp, and 3 where I would use mv. For each scenario,
show the exact command I would run.
```

**What you're learning:** Building judgment about when to duplicate files versus relocate them. In agent management, choosing wrong can mean losing your only copy of a configuration file or cluttering your workspace with unnecessary duplicates.

**Recover from Mistakes:**

```
I accidentally deleted an important configuration file with rm.
What are my recovery options on Linux? Also, what practices can
I adopt to prevent accidental deletions when managing agent files?
Give me specific commands and habits I should build.
```

**What you're learning:** Defensive file management practices. Linux doesn't have an undo button, so prevention strategies (aliases, backups, interactive mode defaults) are essential skills for anyone managing production agent deployments.
