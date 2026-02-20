---
sidebar_position: 2
title: "From Broken Math to Your First Tool"
chapter: 9
lesson: 1
duration_minutes: 30
description: "Discover why Bash arithmetic and LLM head-math both fail with decimals, then build your first reusable Python utility with Claude Code"
keywords:
  [
    "bash arithmetic",
    "decimal math",
    "python script",
    "stdin",
    "pipe operator",
    "LLM hallucination",
    "calculation accuracy",
    "single-purpose tool",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Recognizing Computation Boundaries"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why Bash fails with decimals and why LLM arithmetic is unreliable at scale"

  - name: "Directing Agent-Built Scripts"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Communication"
    measurable_at_this_level: "Student can direct Claude Code to build a stdin-reading Python script that solves a computation problem"

  - name: "Understanding stdin/pipe Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain how the pipe operator connects Bash commands to Python scripts"

learning_objectives:
  - objective: "Explain why Bash arithmetic fails with decimal numbers and why LLM head-math is unreliable"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student predicts which calculations will fail in Bash and explains why asking AI to calculate is risky"

  - objective: "Direct Claude Code to build a Python script that sums numbers from stdin"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully prompts Claude Code to create working sum.py and runs it on test data"

  - objective: "Trace data flow through a pipe from Bash command to Python script"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can explain what happens in: cat expenses.txt | python sum.py"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Bash integer-only math, LLM prediction vs computation, stdin reading, pipe data flow, reusable scripts) at A2 ceiling"

differentiation:
  extension_for_advanced: "Research how bc and awk handle decimals, or ask Claude Code to add statistics (count, average, min, max) to sum.py"
  remedial_for_struggling: "Focus on two facts: Bash breaks on decimals, Python doesn't. Run the commands, see the difference. Don't worry about understanding every line of sum.py yet."

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "Computation Foundations and Testing"
  key_points:
    - "The rule 'if it is math, ask AI to write code that calculates — never ask AI to calculate' is the chapter's central principle and prevents hallucinated arithmetic"
    - "Bash integer-only arithmetic and LLM prediction-vs-computation are TWO different failure modes that converge on the same solution: Python scripts"
    - "The stdin/pipe pattern (cat data.txt | python script.py) is the Unix composability model students will use for every tool in this chapter"
    - "The Dr. Pepper/medical expenses opening scenario motivates the entire chapter — catching that trap requires computation tools, not just file processing"
  misconceptions:
    - "Students think LLM math failures are rare — they work for 3 numbers but fail silently at scale, which is exactly when accuracy matters most"
    - "Students confuse 'Bash truncates silently' with 'Bash errors on decimals' — both happen, but silent truncation (10/3 = 3) is more dangerous because there is no error message"
    - "Students may think sum.py is trivial — the value is not the script itself but the stdin/pipe composability pattern that makes it chainable with any Bash command"
  discussion_prompts:
    - "If you asked an AI to sum 100 expense amounts and it gave you a wrong total, would you notice? What makes silent math errors so dangerous for financial data?"
    - "The lesson says 'describe the data problem, not the implementation.' How is this different from the prompt patterns in Chapter 8?"
    - "Why does the script read from stdin instead of opening a specific file? What does that design decision enable?"
  teaching_tips:
    - "Start by having students actually type 'echo $((1.2 + 2.3))' in their terminals — seeing the error firsthand is more convincing than reading about it"
    - "The Bash works-vs-fails table and the silent truncation row (10/3 = 3) are worth putting on the board — truncation without error is the scarier failure"
    - "Make sure students complete the checkpoint (building and running sum.py) before moving on — Lesson 2 builds directly on this script"
    - "The pipe data flow diagram is the key conceptual model — draw it on the board and trace data through cat → pipe → stdin → sum.py → stdout"
  assessment_quick_check:
    - "Ask: 'Why should you never ask an AI to calculate your expenses directly?' — tests the prediction-vs-computation distinction"
    - "Ask students to explain what happens when you run 'cat expenses.txt | python sum.py' step by step — tests understanding of the pipe/stdin data flow"
    - "Ask: 'Bash says 10 divided by 3 equals 3. Is that an error or a feature?' — tests understanding of integer truncation"
---

# From Broken Math to Your First Tool

Somewhere in your bank statement, Dr. Pepper is hiding among your medical expenses. Not the drink — the merchant name. A simple keyword search for "DR" flags every Dr. Pepper purchase as a doctor visit, silently inflating your tax deductions. File that return and you've committed fraud by algorithm. By the end of this chapter, you'll build a tool that catches that trap and processes a full year of bank statements into an accountant-ready report with one command.

But first, you need to solve a more fundamental problem: your terminal can't even add decimals.

## Watch Bash Fail

You want to split a restaurant bill. Three friends, total $47.50. Open your terminal and try:

```bash
echo $((47.50 / 3))
```

**Output:**

```
bash: 47.50 / 3: syntax error: invalid arithmetic operator (error token is ".50 / 3")
```

Bash chokes on the decimal point. Try something simpler:

```bash
echo $((1.2 + 2.3))
```

**Output:**

```
bash: 1.2 + 2.3: syntax error: invalid arithmetic operator (error token is ".2 + 2.3")
```

Now try with whole numbers:

```bash
echo $((12 + 23))
```

**Output:**

```
35
```

That works. The difference? No decimal points. Bash's `$((...))` syntax does **integer-only** arithmetic.

| Works in Bash               | Fails in Bash                  |
| --------------------------- | ------------------------------ |
| `$((5 + 3))` = 8           | `$((5.5 + 3.5))` = Error      |
| `$((100 - 25))` = 75       | `$((100.00 - 25.00))` = Error |
| `$((10 / 3))` = 3 (wrong!) | `$((10.0 / 3.0))` = Error     |

Notice that last row. Even when Bash doesn't error, it **truncates**. `10 / 3` returns `3`, not `3.333...`. For financial calculations, that silent data loss is worse than a crash.

Every financial calculation involves decimals. Bash simply cannot do them.

## The Head Math Trap

"Okay, Bash can't do decimals. I'll just ask my AI assistant to calculate it."

Here's the trap: **LLMs don't compute, they predict**. When you ask an AI to add `12.50 + 8.75`, it isn't running arithmetic. It's predicting what text should come next based on patterns. For three numbers, the prediction usually matches reality. For 100 numbers from your expense report, it almost certainly won't.

Asking an LLM to sum your monthly expenses is like asking a poet to recite a calculation from memory. They might get lucky, but you wouldn't bet your tax return on it.

The rule for this chapter:

> **If it's math, it belongs in a script. Don't ask AI to calculate. Ask AI to write code that calculates.**

| Approach                           | Reliability         | Why                              |
| ---------------------------------- | ------------------- | -------------------------------- |
| "What's the sum of these amounts?" | Unreliable at scale | LLM predicts, doesn't compute   |
| "Write Python to sum these numbers"| Reliable            | Python executes, doesn't predict |

## Building sum.py with Claude Code

You have a file of expenses, one decimal number per line. You need the total. Bash errors out. LLM head-math hallucinates. You need code that executes.

Open Claude Code and describe your problem:

```
I have a file with decimal numbers, one per line. Build me a script
that reads numbers from stdin and prints the total.
```

Watch what Claude Code does:

```
Claude Code: I'll create a Python script that reads numbers from
standard input and sums them.

[Creates: sum.py]

#!/usr/bin/env python3
# sum.py - Sum numbers from stdin
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if line:  # Skip empty lines
        total += float(line)

print(f"Total: {total}")

Let me test it:

[Runs: echo -e "127.89\n45.50\n12.99" | python sum.py]

Total: 186.38
```

In seconds, you have a reusable tool. The agent didn't calculate in its head (which would hallucinate). It wrote code that executes. The script is a contract: given numbers, return their exact sum.

### What the Agent Built

Here's a quick walkthrough of sum.py:

- **`#!/usr/bin/env python3`** -- tells the OS to run this with Python 3
- **`for line in sys.stdin`** -- reads piped input one line at a time
- **`float(line)`** -- converts text like `"127.89"` to an actual decimal number
- **`total += float(line)`** -- adds each number to a running total
- **`print(f"Total: {total}")`** -- outputs the result

The key insight is `sys.stdin`. When you pipe data into a Python script, `sys.stdin` is where that data arrives. Your script doesn't know or care where the data came from -- a file, another command, or typed input. It just reads lines and sums them.

### How the Pipe Connects Everything

When you run `cat expenses.txt | python sum.py`, here's the data flow:

```
+-----------------+     +-----------------+
|      cat        |     |    sum.py       |
|                 |---->|                 |
|  reads file     |  |  |  reads stdin    |
|  outputs text   |  |  |  calculates sum |
|                 |  |  |  prints total   |
+-----------------+  |  +-----------------+
                     |
        pipe (|) ----+
   redirects stdout --> stdin
```

The pipe takes whatever `cat` outputs and feeds it directly into your script. Small tools, chained together, solving big problems. That's the Unix philosophy you'll use throughout this chapter.

:::warning Stop. Do This Now.
Open Claude Code. Ask it to build sum.py. Run it on three numbers. Don't proceed to Lesson 2 until you see output in your terminal.

Use this prompt:
```
I have a file with decimal numbers, one per line. Build me a script that reads numbers from stdin and prints the total.
```

Then test it:
```bash
echo -e "100.50\n25.75\n14.25" | python3 sum.py
```

Expected output: `Total: 140.5`
:::

## The Prompt Pattern

Here's the pattern you just used:

```
"I have [data problem]. Build me a script that [reads from stdin]
and [produces output]."
```

This works because you describe the **data problem**, not the implementation. The agent chooses Python. You specify **stdin/stdout**, which signals you want a composable Unix tool. The agent builds something **reusable**, not a one-time answer.

| Your Problem     | The Prompt                                                                  |
| ---------------- | --------------------------------------------------------------------------- |
| Sum numbers      | "Build me a script that reads numbers from stdin and prints their sum"      |
| Calculate average| "Build me a script that reads numbers from stdin and prints their average"  |
| Find maximum     | "Build me a script that reads numbers from stdin and prints the largest one"|
| Count lines      | "Build me a script that reads from stdin and counts how many lines"         |

The structure stays the same. The calculation changes.

You have a working script. It produced a number. But here's the uncomfortable question: how do you know that number is right? The script ran without errors — exit code 0, no red text. Does that mean it's correct? In the next lesson, you'll discover why "it ran" and "it's right" are dangerously different things.

---

## Try With AI

### Prompt 1: Understanding the Bash Limitation

```
I just tried running `echo $((1.2 + 2.3))` in Bash and got a syntax
error. Can you explain why Bash can't handle decimal numbers in
arithmetic? What's happening under the hood that causes this?
```

**What you're learning:** The AI explains technical concepts you encountered through direct experimentation. Notice how it provides context about integer arithmetic and shell design decisions that you wouldn't find by staring at the error message alone.

### Prompt 2: Extend sum.py

```
I have sum.py that reads numbers from stdin and prints the total.
Can you modify it to also print:
- The count of numbers
- The average
- The minimum and maximum values

Keep the stdin reading pattern so it still works with pipes.
```

**What you're learning:** Iterative development with AI. You have a working tool and you're extending it with clear requirements. Notice how specifying "keep the stdin reading pattern" directs the architecture -- you're making design decisions, the agent handles implementation.

### Prompt 3: Handle Bad Input

```
My sum.py crashes when the input has a header line like "Amount"
before the numbers. How do I make it skip non-numeric lines
gracefully instead of crashing?
```

**What you're learning:** Collaborative debugging. You identify the limitation (crashes on headers), the agent suggests the fix (try/except). This is the refinement loop -- you provide real-world context about your data, the AI provides a robust solution.
