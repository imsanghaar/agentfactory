---
sidebar_position: 3
title: "The Testing Loop"
chapter: 9
lesson: 2
layer: L2
duration_minutes: 25
description: "Discover why exit code 0 doesn't mean correct, then learn the verification pattern that catches silent bugs"
keywords:
  [
    "exit codes",
    "verification",
    "zero-trust",
    "debugging",
    "test data",
    "echo $?",
    "error handling",
  ]

skills:
  - name: "Directing Verification Workflows"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Quality Assurance"
    measurable_at_this_level: "Student can direct Claude Code to verify script output against known test data"

  - name: "Understanding Exit Codes"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Debugging"
    measurable_at_this_level: "Student can explain why exit code 0 means 'didn't crash' not 'correct answer'"

  - name: "Zero-Trust Verification Pattern"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student applies the pattern: create known data, run script, compare to expected"

learning_objectives:
  - objective: "Direct Claude Code to create test data and verify script correctness"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student prompts agent to test sum.py with known-answer data"

  - objective: "Explain the difference between 'exit code 0' and 'correct output'"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can identify when a script runs successfully but produces wrong results"

  - objective: "Apply zero-trust verification to new scripts"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student uses verification pattern on a different calculation script"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (verification workflow, exit codes, test data, zero-trust mindset) within A2 limit"

differentiation:
  extension_for_advanced: "Research other exit codes (127=not found, 130=Ctrl+C), write automated test scripts"
  remedial_for_struggling: "Focus on the conversation pattern: 'verify this with test data where I know the answer'"

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "Computation Foundations and Testing"
  key_points:
    - "The verification paradox — you built a tool to do work you cannot easily check — is the motivating problem, and known-answer test data is the solution"
    - "'Exit code 0 means did not crash, not correct answer' is the single most important distinction in this lesson — students must internalize this before touching real data"
    - "The buggy_sum.py example (skipping numbers starting with 6-9) demonstrates that logic errors produce exit code 0 and no red text — completely invisible without verification"
    - "The zero-trust workflow (generate code → request verification → create test cases → compare) applies to ALL code from any source, not just scripts built in this chapter"
  misconceptions:
    - "Students equate 'no error message' with 'correct output' — the buggy_sum.py example directly disproves this by producing a wrong answer with exit code 0"
    - "Students think one passing test proves correctness — the buggy script passes the 10,20,30 test but fails on 10,60,30, showing that test data selection matters"
    - "Students may think verification is the agent's job — the lesson shows that the HUMAN chooses test data with known answers, because only the human knows which results are easy to verify mentally"
  discussion_prompts:
    - "The buggy script passes the test with 10, 20, 30 but fails with 10, 60, 30. What does this tell you about how to choose good test data?"
    - "If you cannot verify the answer yourself (say, summing 500 expenses), how can you still use known-answer testing? What would you do?"
    - "The lesson says 'trust is earned through verification, not granted through origin.' Does this change how you think about code from any AI tool?"
  teaching_tips:
    - "Have students run buggy_sum.py themselves and see exit code 0 alongside a wrong answer — the visceral experience of 'no error but wrong' is the lesson's core teaching moment"
    - "The exit code table is reference material, not the main point — spend more time on the verification pattern than on memorizing exit codes"
    - "Emphasize the division of labor: the agent creates multiple test cases (integers, decimals, negatives) but the human chose the known-answer approach in the first place"
    - "Connect back to Chapter 8 Lesson 2's verification pattern — 'verify the backup is complete' uses the same zero-trust philosophy applied to file counts instead of calculations"
  assessment_quick_check:
    - "Ask: 'Your script outputs 186.38 with exit code 0. How do you know if that number is right?' — tests whether students reach for verification, not just trust the exit code"
    - "Give students a buggy scenario: 'A filter script keeps numbers > 20 from input 10, 30, 50 but only returns 30.' Ask what they would check first"
    - "Ask students to recite the zero-trust verification workflow: generate, request verification, create test cases, compare"
---

# The Testing Loop

You have a number. 186.38. You stare at it. Is it right?

You built sum.py in Lesson 1. It ran without errors. Output appeared. No red text. Your terminal says `Total: 186.38` and you have no way to know if that's correct without doing the math yourself. And if you could do the math yourself, you wouldn't need the script.

This is the verification paradox — you built a tool to do work you can't easily check, which means you're trusting code you've never proven works. Most people stop here. Output appeared, no red text, must be fine. This assumption has cost companies millions and produced bugs that lurked for months before anyone noticed.

But there's a trick. What if you tested with numbers you CAN add in your head?

10 + 20 + 30 = 60. If the script says 60, it works. If it says anything else, you've caught a bug before it touched real data.

## The Verification Conversation

Open Claude Code and try this:

```
You: I have sum.py that sums numbers from stdin. I want to verify it
works correctly. Create a test file with 10, 20, 30 -- numbers I can
add in my head. Expected answer: 60. Run it and check.
```

Watch what happens:

```
Claude Code: Good idea -- testing with known answers. Let me set that up.

[Creates: test_simple.txt with contents: 10, 20, 30]

[Runs: cat test_simple.txt | python sum.py]
Total: 60.0

Matches expected (60). Let me also test with decimals:

[Creates: test_decimals.txt with contents: 10.5, 20.5, 19.0]

[Runs: cat test_decimals.txt | python sum.py]
Total: 50.0

Matches expected (50). And negative numbers:

[Creates: test_negative.txt with contents: 100, -30, -20]

[Runs: cat test_negative.txt | python sum.py]
Total: 50.0

All three cases verified:
- Simple integers: 60.0 (correct)
- Decimals: 50.0 (correct)
- Negatives: 50.0 (correct)
```

Notice what the agent did. You asked for one test, and it volunteered two more -- decimals and negatives. That's the agent teaching you something: one test case isn't enough. Different input types can trigger different bugs.

But also notice what YOU did. You chose test data with a known answer. That's the human contribution the agent can't make on its own -- it doesn't know which numbers are easy for you to verify mentally.

## Why Exit Code 0 Is a Lie

Every command in Bash produces an exit code. Check it with `$?`:

```bash
cat test_simple.txt | python sum.py
echo $?
```

**Output:**

```
Total: 60.0
0
```

Exit code 0 means: "the script ran without crashing."

It does NOT mean: "the script produced the right answer."

Here's proof. Consider this buggy version:

```python
# buggy_sum.py - Has a silent bug
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # BUG: Skips lines starting with digits > 5
    if line[0] in '6789':
        continue
    total += float(line)

print(f"Total: {total}")
```

Run it:

```bash
echo -e "10\n60\n30" | python buggy_sum.py
```

**Output:**

```
Total: 40.0
```

Check the exit code:

```bash
echo $?
```

**Output:**

```
0
```

Exit code 0. No errors. No warnings. But 40 is wrong -- the answer should be 100. The script silently skipped "60" because it starts with '6'.

**Exit codes catch crashes. They don't catch logic errors.** That's why verification with known answers matters. Your test data of 10, 20, 30 would have passed -- all start with digits 1-3. Only by testing with numbers like 60, 70, or 80 would you catch this bug.

## The Exit Code Table

Common exit codes you'll encounter:

| Exit Code | Meaning | Example |
|-----------|---------|---------|
| 0 | Success -- command completed without crashing | Script ran, output appeared |
| 1 | General error -- something went wrong | Python raised an exception |
| 2 | Misuse of command -- wrong arguments | `python` with no file |
| 127 | Command not found -- typo or missing program | `pythn sum.py` |
| 130 | Interrupted by Ctrl+C | You cancelled a long run |

One caution: `$?` holds the exit code of the **most recent** command. Run `echo $?` immediately after the command you care about -- any command in between overwrites it.

## The Verification Pattern

Here's the prompt pattern that works every time:

```
"Verify [tool] works correctly. Create test data with a known answer
[X] and check that output matches."
```

This works because:

1. **Known answer first.** You calculate the expected result before running the tool.
2. **Simple test data.** Numbers you can add in your head (10 + 20 + 30 = 60).
3. **Multiple cases.** Test integers, decimals, negatives, edge cases.
4. **Comparison.** Output must match expectation exactly.

### Pattern Variations

| What You're Testing | The Prompt |
|---------------------|------------|
| Sum script | "Verify sum.py with test data 10, 20, 30 (expected: 60)" |
| Average script | "Verify average.py with test data 10, 20, 30 (expected: 20)" |
| Max script | "Verify max.py with test data 10, 50, 30 (expected: 50)" |
| Filter script | "Verify filter.py keeps only numbers > 20 from 10, 30, 50 (expected: 30, 50)" |

The tool changes. The verification pattern stays the same.

## The Zero-Trust Philosophy

This approach embodies a mindset: **assume everything is broken until proven otherwise.**

When Claude Code summed your expenses, it wrote a script, ran it, and showed output. Exit code 0. Everything looked fine. But the agent cannot verify that $186.38 is correct for YOUR expenses unless you give it test data with known answers. The agent ran code -- it didn't validate business logic.

The workflow:

1. **Agent generates and runs code** -- script executes, output appears
2. **You request verification** -- "test this with known data"
3. **Agent creates test cases** -- simple data with calculable answers
4. **Comparison proves correctness** -- output matches expectation

This applies to code from any source. Trust is earned through verification, not granted through origin.

## Checkpoint: Verify YOUR sum.py

Stop reading. Create a file called `test_simple.txt` with three numbers: 10, 20, 30. Run your sum.py from Lesson 1 against it. Does it say 60?

```
You: Create test_simple.txt with 10, 20, 30 on separate lines.
Then run: cat test_simple.txt | python sum.py
Expected output: Total: 60.0
```

If it says 60 -- your script works for simple integers. Now try edge cases:

```
You: Test sum.py with these edge cases:
1. Empty file (expected: 0 or 0.0)
2. Single number: just "42.5" (expected: 42.5)
3. File with blank lines mixed in between numbers
```

If any test fails, you've discovered a bug before it touched real data. Fix it now — Lesson 3 builds on a working sum.py.

Your testing loop works beautifully on clean number lists. But real bank data isn't clean. Open an actual bank statement CSV and you'll find merchant names with commas inside them, dollar signs mixed into amounts, and header rows that aren't numbers at all. Your carefully tested sum.py is about to meet the real world — and the real world cheats. (And somewhere in that data, "DR PEPPER SNAPPLE" is waiting to be counted as a medical expense. But that's a problem for later.)

---

## Try With AI

### Prompt 1: Discover Edge Cases

```
What edge cases might break a script that sums numbers from stdin?
Think about unusual inputs: empty files, non-numeric lines, very
large numbers, special characters. List cases I should test.
```

**What you're learning:** Defensive thinking. The agent anticipates failure modes you haven't considered -- dollar signs in data, overflow on large numbers, Unicode characters. Your verification becomes more thorough than anything you'd design alone.

### Prompt 2: Automate Verification

```
I have 5 test cases for sum.py. Help me write a simple bash script
that runs all tests and reports which passed and which failed. Each
test should compare actual output to expected output.
```

**What you're learning:** Test automation. Instead of manually running tests one at a time, you build a script that runs them all and reports results. This is how professionals keep code correct over time.

### Prompt 3: Debug a Failure

```
My sum.py gives wrong output on this test:
- Input: 10, 60, 30
- Expected: 100
- Actual: 40

The script works fine on other inputs. Exit code is 0.
Help me find the bug. What could cause 60 to be skipped?
```

**What you're learning:** Root cause analysis through collaboration. You present a specific failure with evidence (expected vs. actual), and the agent helps you reason backward from symptoms to cause. Notice you're teaching the agent what the problem is -- it can't debug without your observation that 60 is being skipped. This is collaborative debugging where both sides contribute something the other can't.
