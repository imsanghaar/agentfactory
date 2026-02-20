# Chapter 6 Rewrite Plan: File Processing Workflows with General Agent

**Version**: 2.0 (Complete Rewrite)
**Date**: 2025-01-27
**Core Insight**: Students DIRECT the General Agent, they don't manually type commands

---

## The Fundamental Shift

| Old Approach (WRONG)          | New Approach (CORRECT)                           |
| ----------------------------- | ------------------------------------------------ |
| Student types `ls -la`        | Student: "Show me what's in my Downloads folder" |
| Student learns bash syntax    | Student learns effective prompting               |
| Manual command execution      | Agent executes, student supervises               |
| One workflow (organize files) | Multiple practical workflows                     |
| Principles explained          | Principles OBSERVED through agent behavior       |

---

## Chapter Concept: File Processing Workflows

**Tagline**: "Your first day with a Digital Assistant that actually does the work"

**Value Proposition**: By the end of this chapter, students will have automated 5+ real file tasks they do manually today—and understand WHY the agent approaches each task the way it does.

---

## Multiple Workflows Approach

Instead of one long workflow, teach through **multiple practical mini-workflows**:

| Workflow             | Real-World Problem             | Principles Demonstrated        |
| -------------------- | ------------------------------ | ------------------------------ |
| 1. File Survey       | "What's eating my disk space?" | P1 (Bash), P7 (Observability)  |
| 2. Smart Backup      | "Protect before changing"      | P6 (Safety), P3 (Verification) |
| 3. Organized Folders | "End the Downloads chaos"      | P5 (State), P4 (Decomposition) |
| 4. Batch Rename      | "Fix 100 filenames at once"    | P2 (Code), P1 (Bash)           |
| 5. Find & Extract    | "Where's that file from 2023?" | P1 (Bash), P7 (Observability)  |
| 6. Combined Workflow | Full automation pipeline       | ALL principles                 |

---

## Lesson-by-Lesson Breakdown

### Lesson 1: Your First Agent Workflow (25 min)

**Real Problem**: "My Downloads folder is chaos. I don't even know what's in there."

**What Student Does**:

1. Opens Claude Code in Downloads folder
2. Prompts: "I have a cluttered Downloads folder. Help me understand what's in here—how many files, what types, what's taking up space."
3. OBSERVES agent run `ls`, `find`, `du` commands
4. RECEIVES inventory report from agent
5. Learns: "I didn't type commands—I described my problem"

**Principles Observed**:

- **P1 (Bash is the Key)**: Agent uses basic Unix tools, not fancy frameworks
- **P7 (Observability)**: Agent makes chaos visible through reporting

**Teaching Pattern**:

```
Student Prompt → Agent Executes → Student Observes → Student Verifies
```

**Lesson Output**: Understanding of how to prompt for exploration tasks

---

### Lesson 2: The Safety-First Pattern (20 min)

**Real Problem**: "I want to reorganize files but I'm scared of losing something"

**What Student Does**:

1. Prompts: "Before we make any changes, I want a backup of important files"
2. Agent asks clarifying questions: "What counts as important?"
3. Student: "PDFs and any file modified in the last 30 days"
4. OBSERVES agent create timestamped backup
5. VERIFIES backup completeness
6. Learns: "The agent asked before acting destructively—that's P6"

**Principles Observed**:

- **P6 (Safety)**: Agent creates safety net before destructive operations
- **P3 (Verification)**: Agent verifies backup, student double-checks

**Key Learning**: "Always establish safety before allowing destructive operations"

**Prompt Pattern Learned**:

```
"Before doing [destructive action], create [safety mechanism]"
```

---

### Lesson 3: The Organization Workflow (30 min)

**Real Problem**: "These 500 files need to be in proper folders"

**What Student Does**:

1. Prompts: "Help me organize my Downloads. Let's create a categorization system."
2. Agent proposes rules, student refines based on their needs (Three Roles)
3. Agent creates `rules.md` documenting the logic
4. Student: "Test on ONE file first before doing all of them"
5. Agent moves one file, verifies
6. Student: "Looks good. Now do the rest."
7. Agent executes full organization
8. Student verifies results

**Principles Observed**:

- **P5 (State)**: Rules persisted in file for future use
- **P4 (Decomposition)**: Test small before scaling
- **P3 (Verification)**: Check after each major operation

**Key Learning**: "Direct the agent to work incrementally—test before batch"

**Prompt Patterns Learned**:

```
"Let's document the rules before executing"
"Test on one file first"
"Now do the rest, and show me summary when done"
```

---

### Lesson 4: Batch Operations Workflow (25 min)

**Real Problem**: "I have 100 screenshots named 'Screenshot 2024-...' that need better names"

**What Student Does**:

1. Prompts: "I have lots of screenshots with ugly names. Help me rename them to something organized like 'screenshot-YYYY-MM-DD-NNN.png'"
2. OBSERVES agent create a rename script (P2: Code as Interface)
3. Student: "Show me what changes you'll make before doing it"
4. Agent shows preview table
5. Student: "That looks right. Execute it."
6. Agent runs batch rename, logs each change

**Principles Observed**:

- **P2 (Code as Interface)**: Agent writes script for batch operation
- **P7 (Observability)**: Agent shows preview before acting
- **P3 (Verification)**: Preview → Approve → Execute → Log

**Key Learning**: "For repetitive tasks, ask the agent to create a script"

**Prompt Patterns Learned**:

```
"Show me what you'll do before doing it"
"Create a script I can reuse for this"
```

---

### Lesson 5: Search & Discovery Workflow (25 min)

**Real Problem**: "Where's that tax document from 2023? I know I downloaded it..."

**What Student Does**:

1. Prompts: "Help me find a PDF about taxes from sometime in 2023"
2. Agent searches with `find` and `grep`
3. Agent narrows down candidates
4. Student: "That one! Can you also find all similar tax documents?"
5. Agent expands search, creates report

**Principles Observed**:

- **P1 (Bash)**: Agent combines `find`, `grep`, pipes
- **P7 (Observability)**: Agent shows search process and results

**Key Learning**: "Describe what you're looking for, not how to search"

**Prompt Patterns Learned**:

```
"Find files that match [description] from [time period]"
"Show me similar files to this one"
```

---

### Lesson 6: Capstone - Your File Processing Toolkit (30 min)

**Real Problem**: "I want to set up ongoing file management"

**What Student Does**:

1. Combines all learned workflows on a new folder (Desktop)
2. Creates reusable prompt templates for future use
3. Reflects on which principles they observed
4. Documents their personal file processing toolkit

**Principles Demonstrated**: All seven, integrated

**Key Deliverable**: Personal toolkit of prompts for file processing tasks

---

## Teaching Modality: Observation-Based Learning

Each lesson follows this pattern:

```
1. REAL PROBLEM    → Student has actual pain point
2. PROMPT          → Student describes problem to agent
3. OBSERVE         → Student watches agent work
4. VERIFY          → Student checks agent's work
5. REFLECT         → Student identifies principle in action
6. PATTERN         → Student extracts reusable prompt pattern
```

**Why This Works**:

- Students see principles in action, not in lecture
- They learn by observing expert behavior (the agent)
- They build prompt patterns they can reuse
- They develop verification instincts

---

## Principle Observation Guide

How students recognize each principle during agent work:

| Principle         | Student Observes Agent...            | Student Learns To...             |
| ----------------- | ------------------------------------ | -------------------------------- |
| P1: Bash          | Using `ls`, `find`, `grep`, `mv`     | Describe problems, not commands  |
| P2: Code          | Writing scripts for repetitive tasks | Ask for scripts when appropriate |
| P3: Verification  | Checking results after each action   | Always verify, never assume      |
| P4: Decomposition | Testing small before scaling         | Direct incremental work          |
| P5: State         | Creating `rules.md`, logs            | Ask agent to document decisions  |
| P6: Safety        | Creating backups before changes      | Require safety nets              |
| P7: Observability | Logging everything, showing progress | Expect transparency              |

---

## Lesson Structure Template

Each lesson follows:

```markdown
# [Workflow Name]

## The Problem

[Real scenario the student relates to]

## The Conversation

[Actual prompts and agent responses - the CORE of the lesson]

## What Just Happened?

[Principle observation - what student noticed about agent behavior]

## The Pattern

[Reusable prompt pattern student can apply elsewhere]

## Try It Yourself

[Variation student can try immediately]
```

---

## Anti-Patterns to Avoid

| DON'T                            | DO                                                      |
| -------------------------------- | ------------------------------------------------------- |
| "Type this command: `ls -la`"    | "Ask Claude Code: 'Show me what's in this folder'"      |
| Explain bash syntax              | Show agent using bash, explain WHY it chose those tools |
| Step-by-step manual instructions | Conversation-based workflow                             |
| "Key Takeaways" section          | Observation embedded in flow                            |
| One monolithic workflow          | Multiple practical mini-workflows                       |

---

## Success Criteria

After this chapter, students can:

1. **Direct** Claude Code to solve file processing problems
2. **Observe** Seven Principles in agent behavior
3. **Verify** agent work before trusting results
4. **Build** prompt patterns for common tasks
5. **Know when** to intervene vs let agent proceed
6. **Apply** workflows to their own files

---

## Implementation Notes

- Each lesson is a **conversation** between student and agent
- Show actual Claude Code responses (or representative examples)
- Principles emerge from observation, not explanation
- Prompt patterns are the main deliverable
- Students should feel they have a capable assistant, not that they learned bash

---

**Ready for Implementation**
