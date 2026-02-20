### Core Concept

Bash does integer-only arithmetic and LLMs predict text rather than compute — both will silently give you wrong numbers on financial data. The rule: never ask AI to calculate, ask AI to write code that calculates. Python scripts reading from stdin compose with pipes to solve any computation problem.

### Key Mental Models

- **Integer-only trap**: Bash's `$((...))` silently truncates (`10/3` = `3`) or errors on decimals. Every financial calculation involves decimals, so Bash arithmetic is never safe for real data.
- **Prediction vs computation**: LLMs generate plausible-looking numbers by predicting text patterns, not executing math. Reliable for 3 numbers, unreliable for 100. "Fraud by algorithm" starts with trusting the wrong tool.
- **stdin composability**: Scripts that read from `sys.stdin` and write to `stdout` chain together with pipes. `cat data.txt | python sum.py` works because each tool handles one job.

### Critical Patterns

- Prompt pattern: "I have [data problem]. Build me a script that reads from stdin and [produces output]."
- Pipe data flow: `cat file | python script.py` connects file reading to Python processing
- The shebang line (`#!/usr/bin/env python3`) tells the OS which interpreter to use

### Common Mistakes

- Using Bash for any calculation involving decimals — it either errors or silently truncates
- Asking the AI to "add these numbers" instead of "write a script that adds numbers" — the first hallucinates, the second executes
- Assuming a script is correct because it produced output — exit code 0 means "didn't crash," not "right answer"

### Connections

- **Builds on**: Terminal basics and pipe operator from Chapter 8 (File Processing)
- **Leads to**: Verification with test data (Lesson 2) — how do you know that number is right?
