---
sidebar_position: 7
title: "Lesson 7: Text Processing & Automation"
description: "Parse agent logs with grep, sed, and awk, compose multi-tool pipelines, and schedule recurring tasks with cron for automated monitoring."
keywords: ["grep", "sed", "awk", "text processing", "regular expressions", "cron", "crontab", "log parsing", "pipeline", "automation", "log rotation"]
chapter: 11
lesson: 7
duration_minutes: 55

# HIDDEN SKILLS METADATA
skills:
  - name: "grep Pattern Matching"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can use grep with basic strings and extended regular expressions (-E) to search log files and count matches"

  - name: "sed Stream Editing"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can use sed for text substitution and in-place file editing with the -i flag"

  - name: "awk Field Extraction"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can use awk to extract specific fields from structured text and aggregate data with associative arrays"

  - name: "Multi-Tool Pipelines"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can chain grep, sed, and awk with pipes to build multi-step data processing workflows"

  - name: "cron Job Scheduling"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create and manage cron jobs using crontab -e with correct timing syntax and output redirection"

  - name: "Log Rotation Basics"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can implement basic log rotation to prevent disk exhaustion on long-running agent servers"

learning_objectives:
  - objective: "Use grep with regular expressions to search log files for patterns"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student locates ERROR entries in a sample log file using grep with -c, -C, -v, and -E flags"

  - objective: "Use sed for text transformation and substitution in files"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student transforms log lines by removing timestamps and replacing text patterns using sed"

  - objective: "Use awk for field extraction from structured data"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student extracts specific fields from log entries and counts occurrences of each error type using awk"

  - objective: "Create cron jobs for scheduled automation tasks"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student writes a crontab entry that runs a log analysis script on a schedule with output redirection"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "grep pattern matching (basic strings + regex with -E)"
    - "sed stream editing (substitution, in-place with -i)"
    - "awk field extraction and processing"
    - "Multi-tool pipelines (grep | sed | awk chains)"
    - "cron scheduling (crontab syntax, output redirection)"
    - "Log rotation basics"
  assessment: "6 concepts at B2 level (within 7-10 limit). Each tool builds on the previous, culminating in composed pipelines."

differentiation:
  extension_for_advanced: "Explore awk associative arrays for multi-field grouping, combine grep with -P for Perl-compatible regex, investigate logrotate(8) for production log management, and create cron jobs that send alerts via curl to a webhook."
  remedial_for_struggling: "Start with grep only -- master basic string matching before adding -E regex. Use awk to print single fields ($1, $2) before attempting aggregation. Copy crontab syntax from examples rather than composing from scratch."

teaching_guide:
  lesson_type: "core"
  session_group: 3
  session_title: "Text Processing and Automation"
  key_points:
    - "grep, sed, and awk form a processing pipeline: grep finds lines, sed transforms them, awk extracts and computes across fields — each tool has a distinct role"
    - "The multi-tool pipeline pattern (grep | sed | sort | uniq -c | sort -rn) is the standard approach for log analysis and recurs in debugging (lesson 11) and production monitoring (lesson 14)"
    - "cron scheduling with output redirection (>> file 2>&1) turns manual analysis into automated monitoring — but cron runs with a minimal environment, so scripts must use absolute paths"
    - "Log rotation prevents disk exhaustion on long-running agents — without it, a 100-line/min agent fills a disk in days"
  misconceptions:
    - "Students think grep and awk do the same thing — grep finds matching lines while awk processes fields within lines; they complement each other in pipelines"
    - "Students expect sed -i to be reversible — in-place editing is permanent with no undo; always test without -i first or make a backup"
    - "Students forget that cron runs with a minimal PATH — scripts that work interactively fail in cron because PATH is different; define PATH in the script"
    - "Students assume crontab -r removes one job — it removes ALL jobs; use crontab -e to edit specific entries"
  discussion_prompts:
    - "Your agent produces 50,000 lines of logs per day. How would you use the tools from this lesson to create a daily summary report that fits on one screen?"
    - "What is the advantage of chaining small tools with pipes versus writing a single Python script that does all the processing?"
  teaching_tips:
    - "Use the sample log file throughout — creating it at the start gives students a consistent dataset for all exercises, which builds confidence"
    - "Build the error summary pipeline incrementally: run grep alone, then grep | sed, then add sort | uniq -c — showing each transformation stage"
    - "The crontab five-field syntax diagram is a whiteboard moment — draw it large and have students decode example schedules"
    - "Spend less time on sed (substitution is the main use case) and more on awk field extraction — awk is harder to learn but more powerful for log analysis"
  assessment_quick_check:
    - "Ask students to find all ERROR lines from agent-01 and count them (expected: grep ERROR file | grep agent-01 | wc -l)"
    - "Ask: what does the cron expression '0 2 * * *' mean? (Expected: run at 2:00 AM every day)"
    - "Give students a log line and ask them to extract the third field using awk (expected: awk '{print $3}' file)"

teaching_approach: "Error analysis -- students parse real log files to find problems, then automate the analysis."
modality: "Error Analysis"

generated_by: "content-implementer"
created: "2026-02-09"
version: "1.0.0"
---

# Text Processing & Automation

In Lesson 6, you wrote bash scripts with variables, functions, and error handling. Those scripts can create directories, deploy agents, and verify workspaces. But your agents generate something scripts alone cannot handle: **logs**. Thousands of lines of timestamped messages, buried errors, intermittent warnings, patterns that only emerge across hundreds of entries.

When your Digital FTE runs for 12 hours and produces a 50,000-line log file, you need tools that extract meaning from that volume. Scrolling through manually is not an option. This lesson teaches you three text processing tools -- `grep`, `sed`, and `awk` -- that turn raw log files into actionable intelligence. Then you'll schedule these analyses to run automatically with `cron`, so your monitoring works even when you're not watching.

## Setting Up a Sample Log File

Every example in this lesson works with the same log file. Create it now so you can follow along:

```bash
cat > /tmp/agent.log << 'EOF'
2026-02-09 08:00:01 INFO agent-01: Service started on port 8000
2026-02-09 08:00:02 INFO agent-01: Connected to database
2026-02-09 08:05:14 WARNING agent-01: High memory usage: 82%
2026-02-09 08:10:33 ERROR agent-01: Connection timeout to database
2026-02-09 08:10:34 INFO agent-01: Retrying database connection...
2026-02-09 08:10:36 INFO agent-01: Database reconnected
2026-02-09 08:15:45 ERROR agent-02: Failed to process request: invalid JSON
2026-02-09 08:20:01 INFO agent-03: Health check passed
2026-02-09 08:25:17 ERROR agent-01: Connection timeout to database
2026-02-09 08:25:18 INFO agent-01: Retrying database connection...
2026-02-09 08:25:20 INFO agent-01: Database reconnected
2026-02-09 08:30:55 WARNING agent-02: Disk usage at 91%
2026-02-09 08:35:12 ERROR agent-03: Out of memory: killed process
2026-02-09 08:40:01 INFO agent-01: Health check passed
2026-02-09 08:45:33 ERROR agent-01: Connection timeout to database
2026-02-09 08:50:00 INFO agent-02: Scheduled backup completed
EOF
```

**Output:**
```
(no output -- file created)
```

This log simulates three agents running over 50 minutes with a mix of INFO, WARNING, and ERROR entries. You will use it throughout this lesson.

---

## grep: Finding Patterns in Text

`grep` searches files line by line and prints lines that match a pattern. It is the first tool you reach for when something goes wrong and you need to find it in the logs.

### Basic String Matching

Find all error lines:

```bash
grep ERROR /tmp/agent.log
```

**Output:**
```
2026-02-09 08:10:33 ERROR agent-01: Connection timeout to database
2026-02-09 08:15:45 ERROR agent-02: Failed to process request: invalid JSON
2026-02-09 08:25:17 ERROR agent-01: Connection timeout to database
2026-02-09 08:35:12 ERROR agent-03: Out of memory: killed process
2026-02-09 08:45:33 ERROR agent-01: Connection timeout to database
```

Five error lines out of 16 total. grep found them instantly.

### Counting Matches

```bash
grep -c ERROR /tmp/agent.log
```

**Output:**
```
5
```

The `-c` flag returns a count instead of the matching lines. Useful for dashboards and threshold checks.

### Context Around Matches

When you find an error, you often need the lines before and after it to understand what happened:

```bash
grep -C 1 "Out of memory" /tmp/agent.log
```

**Output:**
```
2026-02-09 08:30:55 WARNING agent-02: Disk usage at 91%
2026-02-09 08:35:12 ERROR agent-03: Out of memory: killed process
2026-02-09 08:40:01 INFO agent-01: Health check passed
```

The `-C 1` flag shows 1 line of context before and after the match. Use `-B` for lines before only, `-A` for lines after only.

### Inverted Matching

Show everything except ERROR lines:

```bash
grep -v ERROR /tmp/agent.log | head -5
```

**Output:**
```
2026-02-09 08:00:01 INFO agent-01: Service started on port 8000
2026-02-09 08:00:02 INFO agent-01: Connected to database
2026-02-09 08:05:14 WARNING agent-01: High memory usage: 82%
2026-02-09 08:10:34 INFO agent-01: Retrying database connection...
2026-02-09 08:10:36 INFO agent-01: Database reconnected
```

The `-v` flag inverts the match -- it prints lines that do NOT contain the pattern.

### Extended Regular Expressions

Basic grep matches literal strings. The `-E` flag enables regular expressions for more powerful patterns:

```bash
grep -E "ERROR|WARNING" /tmp/agent.log
```

**Output:**
```
2026-02-09 08:05:14 WARNING agent-01: High memory usage: 82%
2026-02-09 08:10:33 ERROR agent-01: Connection timeout to database
2026-02-09 08:15:45 ERROR agent-02: Failed to process request: invalid JSON
2026-02-09 08:25:17 ERROR agent-01: Connection timeout to database
2026-02-09 08:30:55 WARNING agent-02: Disk usage at 91%
2026-02-09 08:35:12 ERROR agent-03: Out of memory: killed process
2026-02-09 08:45:33 ERROR agent-01: Connection timeout to database
```

The `|` means "or" -- match ERROR or WARNING. Other useful regex patterns:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `ERROR\|WARNING` | Either word (basic grep) | `grep "ERROR\|WARNING" file` |
| `ERROR\|WARNING` | Either word (extended) | `grep -E "ERROR\|WARNING" file` |
| `agent-0[12]` | agent-01 or agent-02 | `grep -E "agent-0[12]" file` |
| `08:[0-2][0-9]` | Times 08:00 through 08:29 | `grep -E "08:[0-2][0-9]" file` |
| `timeout.*database` | "timeout" followed by "database" | `grep -E "timeout.*database" file` |

Find errors from agent-01 only:

```bash
grep ERROR /tmp/agent.log | grep "agent-01"
```

**Output:**
```
2026-02-09 08:10:33 ERROR agent-01: Connection timeout to database
2026-02-09 08:25:17 ERROR agent-01: Connection timeout to database
2026-02-09 08:45:33 ERROR agent-01: Connection timeout to database
```

Chaining two grep commands narrows results progressively. The first grep finds all errors; the second filters to agent-01.

---

## sed: Stream Editing

`sed` transforms text as it flows through -- substituting, deleting, or rearranging content. Where grep finds lines, sed changes them.

### Basic Substitution

Replace "ERROR" with a more visible marker:

```bash
sed 's/ERROR/*** ERROR ***/' /tmp/agent.log | grep ERROR
```

**Output:**
```
2026-02-09 08:10:33 *** ERROR *** agent-01: Connection timeout to database
2026-02-09 08:15:45 *** ERROR *** agent-02: Failed to process request: invalid JSON
2026-02-09 08:25:17 *** ERROR *** agent-01: Connection timeout to database
2026-02-09 08:35:12 *** ERROR *** agent-03: Out of memory: killed process
2026-02-09 08:45:33 *** ERROR *** agent-01: Connection timeout to database
```

The `s/old/new/` syntax replaces the first occurrence of `old` with `new` on each line. Add `g` at the end (`s/old/new/g`) to replace all occurrences on the line.

### Deleting Lines by Pattern

Remove all INFO lines to see only problems:

```bash
sed '/INFO/d' /tmp/agent.log
```

**Output:**
```
2026-02-09 08:05:14 WARNING agent-01: High memory usage: 82%
2026-02-09 08:10:33 ERROR agent-01: Connection timeout to database
2026-02-09 08:15:45 ERROR agent-02: Failed to process request: invalid JSON
2026-02-09 08:25:17 ERROR agent-01: Connection timeout to database
2026-02-09 08:30:55 WARNING agent-02: Disk usage at 91%
2026-02-09 08:35:12 ERROR agent-03: Out of memory: killed process
2026-02-09 08:45:33 ERROR agent-01: Connection timeout to database
```

The `/pattern/d` syntax deletes every line matching the pattern. The original file is unchanged -- sed outputs the modified version to stdout.

### Extracting Parts of Lines

Strip timestamps to see just the log level and message:

```bash
sed 's/^[0-9-]* [0-9:]* //' /tmp/agent.log | head -5
```

**Output:**
```
INFO agent-01: Service started on port 8000
INFO agent-01: Connected to database
WARNING agent-01: High memory usage: 82%
ERROR agent-01: Connection timeout to database
INFO agent-01: Retrying database connection...
```

The pattern `^[0-9-]* [0-9:]* ` matches the date, space, time, and space at the start of each line, replacing them with nothing.

### In-Place Editing

To modify a file directly instead of printing to stdout, use `-i`:

```bash
cp /tmp/agent.log /tmp/agent-copy.log
sed -i 's/agent-01/primary-agent/g' /tmp/agent-copy.log
head -3 /tmp/agent-copy.log
```

**Output:**
```
2026-02-09 08:00:01 INFO primary-agent: Service started on port 8000
2026-02-09 08:00:02 INFO primary-agent: Connected to database
2026-02-09 08:05:14 WARNING primary-agent: High memory usage: 82%
```

:::warning
`sed -i` changes the file permanently. Always make a copy first or test without `-i` to preview the result before committing changes.
:::

---

## awk: Field Extraction and Processing

`awk` treats each line as a record divided into fields by whitespace. Where grep finds lines and sed edits them, awk extracts and computes across fields.

### Printing Specific Fields

Each space-separated word is a field. `$1` is the first, `$2` the second, `$NF` the last:

```bash
awk '{print $1, $2, $3}' /tmp/agent.log | head -5
```

**Output:**
```
2026-02-09 08:00:01 INFO
2026-02-09 08:00:02 INFO
2026-02-09 08:05:14 WARNING
2026-02-09 08:10:33 ERROR
2026-02-09 08:10:34 INFO
```

This extracts the date, time, and log level from each line.

### Filtering with Patterns

Process only lines matching a pattern:

```bash
awk '/ERROR/ {print $2, $4, $NF}' /tmp/agent.log
```

**Output:**
```
08:10:33 agent-01: database
08:15:45 agent-02: JSON
08:25:17 agent-01: database
08:35:12 agent-03: process
08:45:33 agent-01: database
```

The `/ERROR/` pattern filters to error lines only. Then `{print $2, $4, $NF}` prints the time, agent name, and last word (which often identifies the root cause).

### Counting Error Types

awk can aggregate data using associative arrays:

```bash
awk '/ERROR/ {count[$4]++} END {for (agent in count) print agent, count[agent]}' /tmp/agent.log
```

**Output:**
```
agent-01: 3
agent-02: 1
agent-03: 1
```

How this works:

- `/ERROR/` -- Only process ERROR lines
- `count[$4]++` -- Use field 4 (the agent name) as an array key and increment its count
- `END {...}` -- After all lines are processed, loop through the array and print each agent with its error count

### Extracting Timestamps and Messages

Combine field selection to build a clean error report:

```bash
awk '/ERROR/ {
    timestamp = $1 " " $2
    agent = $4
    msg = ""
    for (i=5; i<=NF; i++) msg = msg " " $i
    print timestamp " | " agent msg
}' /tmp/agent.log
```

**Output:**
```
2026-02-09 08:10:33 | agent-01: Connection timeout to database
2026-02-09 08:15:45 | agent-02: Failed to process request: invalid JSON
2026-02-09 08:25:17 | agent-01: Connection timeout to database
2026-02-09 08:35:12 | agent-03: Out of memory: killed process
2026-02-09 08:45:33 | agent-01: Connection timeout to database
```

The loop `for (i=5; i<=NF; i++)` reconstructs the message by joining all fields from position 5 to the end.

---

## Multi-Tool Pipelines

The real power of Unix text processing emerges when you chain tools together with pipes (`|`). Each tool handles one transformation, passing its output to the next.

### Error Type Summary Pipeline

Count each distinct error message and sort by frequency:

```bash
grep ERROR /tmp/agent.log | sed 's/.*ERROR [a-z-]*: //' | sort | uniq -c | sort -rn
```

**Output:**
```
      3 Connection timeout to database
      1 Out of memory: killed process
      1 Failed to process request: invalid JSON
```

The data flows through four stages:

1. `grep ERROR` -- Select only error lines
2. `sed 's/.*ERROR [a-z-]*: //'` -- Strip everything before the error message
3. `sort | uniq -c` -- Group identical messages and count occurrences
4. `sort -rn` -- Sort by count, highest first

Three database timeouts in 50 minutes is a pattern worth investigating.

### Agent Activity Timeline

Show when each agent was last active:

```bash
awk '{print $4, $1, $2}' /tmp/agent.log | sort -k1,1 -k2,2 -k3,3 | awk '
{last[$1] = $2 " " $3}
END {for (a in last) print a, "last seen:", last[a]}
'
```

**Output:**
```
agent-01: last seen: 2026-02-09 08:45:33
agent-02: last seen: 2026-02-09 08:50:00
agent-03: last seen: 2026-02-09 08:40:01
```

### Quick Health Dashboard Script

Combine everything into a reusable script:

```bash
cat > /tmp/log-dashboard.sh << 'EOF'
#!/bin/bash
set -euo pipefail

LOG_FILE="${1:-/tmp/agent.log}"

if [[ ! -f "${LOG_FILE}" ]]; then
    echo "ERROR: Log file not found: ${LOG_FILE}" >&2
    exit 1
fi

TOTAL=$(wc -l < "${LOG_FILE}")
ERRORS=$(grep -c ERROR "${LOG_FILE}" || echo "0")
WARNINGS=$(grep -c WARNING "${LOG_FILE}" || echo "0")

echo "=== Log Dashboard ==="
echo "File: ${LOG_FILE}"
echo "Total lines: ${TOTAL}"
echo "Errors: ${ERRORS}"
echo "Warnings: ${WARNINGS}"
echo ""
echo "--- Error Summary ---"
grep ERROR "${LOG_FILE}" | sed 's/.*ERROR [a-z-]*: //' | sort | uniq -c | sort -rn
echo ""
echo "--- Last 3 Errors ---"
grep ERROR "${LOG_FILE}" | tail -3
EOF

chmod +x /tmp/log-dashboard.sh
/tmp/log-dashboard.sh /tmp/agent.log
```

**Output:**
```
=== Log Dashboard ===
File: /tmp/agent.log
Total lines: 16
Errors: 5
Warnings: 2

--- Error Summary ---
      3 Connection timeout to database
      1 Out of memory: killed process
      1 Failed to process request: invalid JSON

--- Last 3 Errors ---
2026-02-09 08:25:17 ERROR agent-01: Connection timeout to database
2026-02-09 08:35:12 ERROR agent-03: Out of memory: killed process
2026-02-09 08:45:33 ERROR agent-01: Connection timeout to database
```

This script combines grep for counting, sed for message extraction, and awk-style pipelines for summarization -- all in a reusable tool you can run against any log file.

---

## cron: Scheduling Automated Tasks

Running your log dashboard manually is useful. Running it automatically every hour is automation. `cron` is the Linux scheduler that executes commands on a time-based schedule.

### crontab Syntax

Every cron entry follows five time fields plus the command to run:

```
* * * * * command-to-run
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, where 0 and 7 = Sunday)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

Common schedules:

| Schedule | cron Expression | Meaning |
|----------|----------------|---------|
| Every 5 minutes | `*/5 * * * *` | Runs at :00, :05, :10, :15... |
| Every hour | `0 * * * *` | Runs at the top of each hour |
| Daily at 2 AM | `0 2 * * *` | Runs once per day at 02:00 |
| Every Sunday at 3 AM | `0 3 * * 0` | Weekly maintenance window |
| Mon-Fri at 9 AM | `0 9 * * 1-5` | Business hours start |

### Viewing Your crontab

```bash
crontab -l 2>/dev/null || echo "No crontab configured yet"
```

**Output:**
```
No crontab configured yet
```

### Creating a Scheduled Job

Schedule the log dashboard to run every 5 minutes and append output to a monitoring file:

```bash
(crontab -l 2>/dev/null; echo "*/5 * * * * /tmp/log-dashboard.sh /tmp/agent.log >> /tmp/monitor-output.log 2>&1") | crontab -
```

**Output:**
```
(no output -- crontab updated silently)
```

Verify the job was added:

```bash
crontab -l
```

**Output:**
```
*/5 * * * * /tmp/log-dashboard.sh /tmp/agent.log >> /tmp/monitor-output.log 2>&1
```

Key details:

- `>> /tmp/monitor-output.log` -- Appends stdout to a file (use `>>` not `>` to avoid overwriting previous output)
- `2>&1` -- Redirects stderr to the same file as stdout, so errors are captured too
- `crontab -` -- Reads the new crontab from stdin (the pipe)

:::note
cron runs commands with a minimal environment. If your script depends on custom `PATH` settings or environment variables, define them inside the script or at the top of your crontab file: `PATH=/usr/local/bin:/usr/bin:/bin`.
:::

### Removing a Scheduled Job

To remove all cron jobs:

```bash
crontab -r
```

**Output:**
```
(no output -- all cron jobs removed)
```

To remove a specific job, edit the crontab and delete that line:

```bash
crontab -e
```

This opens your crontab in the default editor. Delete the line you no longer want, save, and exit.

---

## Log Rotation Basics

Long-running agents produce logs continuously. Without rotation, log files grow until they fill the disk and your agent crashes.

### The Problem

An agent logging 100 lines per minute produces:

- 6,000 lines per hour
- 144,000 lines per day
- Over 1 million lines per week

Left unchecked, this fills your disk.

### Simple Rotation Script

```bash
cat > /tmp/rotate-logs.sh << 'EOF'
#!/bin/bash
set -euo pipefail

LOG_DIR="${1:-/tmp/agent-logs}"
MAX_SIZE_KB=1024  # Rotate files larger than 1 MB

if [[ ! -d "${LOG_DIR}" ]]; then
    echo "Log directory not found: ${LOG_DIR}" >&2
    exit 1
fi

for logfile in "${LOG_DIR}"/*.log; do
    if [[ ! -f "${logfile}" ]]; then
        continue
    fi

    size_kb=$(du -k "${logfile}" | awk '{print $1}')

    if [[ ${size_kb} -gt ${MAX_SIZE_KB} ]]; then
        mv "${logfile}" "${logfile}.old"
        touch "${logfile}"
        echo "Rotated: $(basename "${logfile}") (was ${size_kb} KB)"
    fi
done
EOF

chmod +x /tmp/rotate-logs.sh
```

**Output:**
```
(no output -- script created)
```

Test it with a large file:

```bash
mkdir -p /tmp/agent-logs
dd if=/dev/zero of=/tmp/agent-logs/test.log bs=1K count=2048 2>/dev/null
ls -lh /tmp/agent-logs/test.log
```

**Output:**
```
-rw-r--r-- 1 user user 2.0M Feb  9 14:30 /tmp/agent-logs/test.log
```

```bash
/tmp/rotate-logs.sh /tmp/agent-logs
```

**Output:**
```
Rotated: test.log (was 2048 KB)
```

```bash
ls -lh /tmp/agent-logs/test.log*
```

**Output:**
```
-rw-r--r-- 1 user user    0 Feb  9 14:30 /tmp/agent-logs/test.log
-rw-r--r-- 1 user user 2.0M Feb  9 14:30 /tmp/agent-logs/test.log.old
```

The oversized log was renamed to `.old` and a fresh empty file created. Schedule this with cron for automatic rotation:

```bash
# Example crontab entry (add with crontab -e):
# 0 * * * * /tmp/rotate-logs.sh /var/log/agents >> /var/log/rotation.log 2>&1
```

:::note
For production systems, Linux includes `logrotate` -- a dedicated tool that handles rotation, compression, and retention policies. The manual approach above teaches the concept; `logrotate` handles the edge cases (concurrent writes, compression, mail notifications) that production environments require.
:::

---

## Safety Note

Text processing commands read files by default but can modify them destructively:

- `sed -i` edits files in place with no undo. Always test without `-i` first.
- Piping to the same file you are reading (`grep pattern file > file`) truncates the file to zero bytes. Use a temporary file or `sponge` from `moreutils`.
- `crontab -r` removes ALL scheduled jobs, not just one. Use `crontab -e` to remove specific entries.
- cron jobs run silently. Without output redirection (`>> file 2>&1`), you will never see errors.

---

## Exercises

### Exercise 1: Find ERROR Lines and Count Them

**Task:** Find all ERROR lines in the sample log from a specific agent using grep.

```bash
grep ERROR /tmp/agent.log | grep "agent-01" | wc -l
```

**Output:**
```
3
```

**Verify:** The count should be 3 (all three database timeout errors came from agent-01).

### Exercise 2: Extract Timestamps and Messages with awk

**Task:** Extract only the time and the error message (everything after the agent name) for each ERROR line.

```bash
awk '/ERROR/ {
    time = $2
    msg = ""
    for (i=5; i<=NF; i++) msg = msg " " $i
    print time ":" msg
}' /tmp/agent.log
```

**Output:**
```
08:10:33: Connection timeout to database
08:15:45: Failed to process request: invalid JSON
08:25:17: Connection timeout to database
08:35:12: Out of memory: killed process
08:45:33: Connection timeout to database
```

**Verify:** Five lines, each showing time and error message without the date or agent name.

### Exercise 3: Create a Disk Usage cron Job

**Task:** Create a cron job that appends disk usage to a file every 5 minutes.

```bash
(crontab -l 2>/dev/null; echo "*/5 * * * * df -h / >> /tmp/disk-usage.log 2>&1") | crontab -
```

**Output:**
```
(no output -- crontab updated)
```

**Verify:**

```bash
crontab -l | grep "df -h"
```

**Output:**
```
*/5 * * * * df -h / >> /tmp/disk-usage.log 2>&1
```

The cron entry exists and will run `df -h` every 5 minutes.

Clean up when done:

```bash
crontab -r 2>/dev/null
```

---

## Try With AI

```
I have agent logs in this format:
[2026-02-09 14:23:01] ERROR agent-03: Connection timeout to database
[2026-02-09 14:23:05] WARNING agent-01: High memory usage: 88%
[2026-02-09 14:24:12] ERROR agent-03: Connection timeout to database

Write me a grep+awk pipeline that extracts just the timestamp and
error message for all ERROR entries. The output should look like:
14:23:01 Connection timeout to database
14:24:12 Connection timeout to database
```

**What you're learning:** AI translates your specific log format into a precise command pipeline. Describing your exact input format and desired output format produces a targeted solution faster than learning regex syntax from scratch. Compare what AI generates with the awk commands from this lesson -- you will notice similar patterns.

```
Now tell Claude: "My logs also have WARNING entries I care about,
and I need to sort the output by timestamp and then count how many
times each unique error message appears. Show me the full pipeline
and explain what each stage does."
```

**What you're learning:** Adding requirements to an existing pipeline reveals how tools compose. AI will likely chain grep, awk, sort, and uniq in ways that build on this lesson's patterns. Asking it to explain each stage reinforces your understanding of how data flows through pipes.

```
Ask Claude: "Write a cron job that runs this log analysis pipeline
every hour and saves the report to /var/log/agent-report.log. Also
add a check -- if the ERROR count exceeds 10 in the past hour, write
an alert to a separate file /var/log/agent-alerts.log with the
current timestamp."

After Claude responds, review the solution and ask: "What happens
if the log file is being written to while the analysis runs? Is there
a race condition? How do production systems handle this?"
```

**What you're learning:** Production automation requires thinking beyond the happy path. Asking about concurrent access reveals that simple pipelines can miss lines or double-count when files are actively written to. AI may suggest `cp` + analyze the copy, or log rotation as a solution -- both patterns from this lesson applied to a real constraint.
