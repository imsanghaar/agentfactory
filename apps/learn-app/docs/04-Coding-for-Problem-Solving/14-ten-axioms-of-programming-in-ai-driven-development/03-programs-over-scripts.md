---
sidebar_position: 3
title: "Axiom III: Programs Over Scripts"
description: "Production work requires proper programs with types, tests, error handling, and CI integration. Scripts are for exploration; programs are for shipping."
keywords: ["programs over scripts", "type annotations", "pytest", "pyright", "ruff", "uv", "Python discipline", "CI/CD", "agentic development", "production code"]
chapter: 14
lesson: 3
duration_minutes: 22

# HIDDEN SKILLS METADATA
skills:
  - name: "Distinguishing Scripts from Programs"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify at least five structural differences between a script and a program (types, tests, error handling, CLI interface, package structure) and explain why each matters"

  - name: "Applying the Python Discipline Stack"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can describe the role of uv (dependency management), pyright (type checking), ruff (linting/formatting), and pytest (testing) and explain how they form a verification pipeline"

  - name: "Evaluating Code Readiness for Production"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Given a code sample, student can assess whether it meets program-level quality (types, error handling, tests, packaging) or remains at script level, and recommend specific improvements"

learning_objectives:
  - objective: "Distinguish programs from scripts using five structural criteria"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can list and explain: type annotations, error handling, test coverage, CLI interface, and package structure as the five markers of a program"

  - objective: "Apply the Python discipline stack (uv, pyright, ruff, pytest) to evaluate code quality"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can describe what each tool catches and how they form layers of verification that prevent different classes of defects"

  - objective: "Explain why AI-generated code requires program-level discipline"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate three reasons: types catch hallucinated APIs, tests prevent drift, CI enforces standards across sessions"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (script-program continuum, type annotations, error handling discipline, discipline stack tools, AI-code verification, decision framework) within A2-B1 range (5-7)"

differentiation:
  extension_for_advanced: "Research how pyright strict mode catches more subtle type errors than basic mode; explore how pre-commit hooks automate the discipline stack before every commit"
  remedial_for_struggling: "Focus on one concrete transformation: take a 10-line script and add type hints and one test, then observe what pyright and pytest catch"
---

# Axiom III: Programs Over Scripts

Axiom II asked where knowledge should live. James learned the answer the hard way — two weeks of work discarded because a decision lived in Slack instead of markdown. After that, he became the team's most disciplined documentation writer. Every decision got an ADR. Every convention went into CLAUDE.md. Knowledge problem solved. Now Axiom II left a different question hanging: when you ask an AI agent to build something, should it produce a quick script or a proper program?

Emma answered that question by asking James to write a script.

The team needed a utility to normalize image filenames before uploading them to the CDN — lowercase, no spaces, no special characters. Fifteen lines of Python. James wrote it in twenty minutes: a `for` loop over `os.listdir`, a regex substitution, an `os.rename`. It worked. He committed it as `rename_images.py` and moved on.

Three months later, the marketing team adopted the script for their asset pipeline. Then the design team. Then the client services team started running it on deliverables. Nobody told James. Nobody asked permission. The script just spread — because it worked, and because working code attracts dependencies the way a lit window attracts moths.

On a Friday afternoon, the client services team ran the script on a folder of 2,000 files for a product launch. The script encountered a filename with a Unicode em-dash, crashed on file 847, and left the folder in a state where 846 files had been renamed and 1,154 had not. There were no logs to show which files had been processed. There was no `--dry-run` flag to preview changes. There was no error handling to skip the problem file and continue. There were no tests that would have caught the Unicode edge case before it reached production. The team spent the weekend manually sorting 2,000 files, matching renamed versions to originals using file timestamps and sizes.

James stared at his fifteen lines of code — no tests, no error handling, no logging, no dry-run flag — and realized three teams depended on it every day. The code had not changed. The responsibility around it had.

## The Problem Without This Axiom

James's fifteen-line script did not announce its promotion to production infrastructure. No one sent an email saying "this utility is now load-bearing code for three teams." It happened one convenience at a time — someone copied the script, someone else added it to a Makefile target, someone scheduled it in a cron job. By the time it failed, it had accumulated responsibilities it was never built to carry.

This pattern is universal. Without the discipline that separates scripts from programs, every team accumulates a graveyard of fragile utilities:

- A data processing script runs in production for months. One day the input format changes slightly. The script crashes at 2am with no error message beyond `KeyError: 'timestamp'`. Nobody knows what it expected or why — because there are no type annotations to declare the expected input shape.
- An AI agent generates a utility function. It works for the test case. Three weeks later, it fails on edge cases the AI never considered. There are no tests to reveal this, and no type annotations to show what the function actually accepts.
- A deployment script uses hardcoded paths. It works on the author's machine. On the CI server, it fails silently and deploys a broken build — because nobody added the validation that a program demands.

The root cause is the same every time: code that grew beyond script-level complexity while retaining script-level discipline. The code did not change. The expectations around it changed. And nobody upgraded the discipline to match.

## The Axiom Defined

> **Axiom III: Production work requires proper programs, not ad-hoc scripts. Programs have types, tests, error handling, and CI integration. Scripts are for exploration; programs are for shipping.**

This axiom draws a clear line: scripts serve exploration and experimentation; programs serve reliability and collaboration. Both are valuable. The failure mode is not writing scripts. The failure mode is shipping scripts as if they were programs.

<details>
<summary><strong>Historical Background: The Long Argument for Types (click to expand)</strong></summary>

The debate between "move fast and break things" and "move carefully and prove things" is older than most developers realize. It traces back to the earliest days of programming language design, and the side that favors discipline has been winning — slowly, then all at once.

In 1973, Robin Milner at the University of Edinburgh created ML, a programming language with a type system so precise that if your program compiled, entire categories of bugs were mathematically impossible. The idea was radical: let the machine verify your logic before you run it. Milner's work earned him the Turing Award in 1991 and launched a lineage of typed languages — Haskell, OCaml, F# — that influenced every modern language with a type system.

For decades, Python existed on the opposite end of this spectrum. Guido van Rossum designed Python for readability and rapid prototyping, deliberately leaving out static types. The language thrived. It also accumulated a reputation: Python was where scripts became programs by accident, and where bugs hid until runtime because nothing checked your assumptions before execution.

The turning point came in 2014, when Guido van Rossum — Python's creator himself — co-authored PEP 484, introducing optional type hints to the language. The proposal was not a concession. It was a recognition that Python had grown beyond scripting. Millions of lines of Python were running in production at Dropbox, Instagram, Google, and Netflix. At that scale, "run it and see if it crashes" was no longer an engineering strategy. Type hints let developers declare their intentions — `def process(data: list[Record]) -> Summary` — and let tools like mypy and later pyright verify those intentions before a single line executed.

Python's journey from untyped scripting language to gradually typed systems language mirrors exactly what Axiom III teaches. The same forces that pushed Python toward types — growing codebases, production reliability, collaboration across teams — push every script toward program discipline once the stakes become real.

</details>

---

## From Principle to Axiom

In Chapter 3, you learned **Principle 2: Code as Universal Interface** -- the idea that code solves problems precisely where prose fails. Code is unambiguous. Code is executable. Code is the language machines understand natively.

Axiom III builds on that foundation: if code is your universal interface, then the **quality** of that code determines the reliability of your interface. A vague specification is bad. A vague program is worse, because it compiles and runs -- giving the false appearance of correctness while hiding fragility beneath the surface.

Principle 2 says: *use code to solve problems*.
Axiom III says: *make that code worthy of the problems it solves*.

The principle is about choosing the right medium. The axiom is about discipline within that medium.

![Fragile Scripts versus Robust Programs: comparing maintainability, reliability, scalability, collaboration, and structured programming principles](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-4/chapter-14/03-programs-over-scripts.png)

## The Script-to-Program Continuum

James's mistake was not writing a script. His mistake was not recognizing when the script stopped being a script. Scripts and programs are not binary categories — they exist on a continuum, and code naturally moves along it as its responsibilities grow. The key is recognizing when your code has moved far enough that script-level practices become dangerous.

| Dimension | Script | Program |
|-----------|--------|---------|
| **Purpose** | Explore, prototype, one-off task | Reliable, repeatable, shared |
| **Type annotations** | None or minimal | Complete on all public interfaces |
| **Error handling** | Bare `except` or crash-and-fix | Specific exceptions with recovery |
| **Tests** | Manual verification ("it printed the right thing") | Automated test suite (pytest) |
| **CLI interface** | Hardcoded values, `sys.argv[1]` | Typed CLI (typer/click/argparse) |
| **Dependencies** | `pip install` globally | Locked in `pyproject.toml` (uv) |
| **Configuration** | Magic strings in source | Typed config objects or env vars |
| **Documentation** | Comments (maybe) | Docstrings, README, usage examples |
| **CI/CD** | None | Linted, type-checked, tested on every push |

### When Does a Script Become a Program?

A script should become a program when any of these conditions become true:

1. **Someone else will run it.** If another human (or an automated system) depends on your code, it needs to communicate its expectations through types and handle failures gracefully.
2. **It will run more than once.** One-off scripts can crash and you re-run them with a fix. Repeated execution requires reliability.
3. **It processes important data.** If the input or output matters (client files, financial records, deployment artifacts), silent failures are unacceptable.
4. **It grew beyond 50 lines.** This is not a strict threshold, but complexity compounds. Beyond 50 lines, you cannot hold the full logic in your head while debugging.
5. **An AI generated it.** AI-generated code deserves extra scrutiny because you did not write it line-by-line. Types and tests become your verification layer.

## A Script Becomes a Program: James's Fifteen Lines

Here is what James originally wrote — the script that three teams came to depend on:

:::tip Don't worry about the Python syntax yet
You will learn Python later in Part 4. For now, compare the *length and structure* of these two versions — not the syntax. Notice what the script is missing (error handling, tests, types) and what the program adds. The difference between a script and a program is the lesson, not the language.
:::

```python static
# rename_images.py (SCRIPT version)
import os, re

folder = "/Users/james/photos"
for f in os.listdir(folder):
    if f.endswith(".jpg"):
        new_name = re.sub(r'\s+', '_', f.lower())
        os.rename(os.path.join(folder, f), os.path.join(folder, new_name))
        print(f"Renamed: {f} -> {new_name}")
```

Twelve lines. No error handling. No way to preview changes. No protection against overwriting existing files. Hardcoded paths. When it hits a Unicode character it cannot process, it crashes mid-operation and leaves the folder half-renamed. This is the code that ruined a client team's weekend.

After the incident, Emma sat down with James and walked through the transformation. The program version is longer — necessarily so — but every additional line exists to prevent a specific category of failure:

```python static
# src/image_renamer/cli.py (PROGRAM version)
"""Batch rename image files with safe, reversible operations."""
from pathlib import Path
from dataclasses import dataclass
import re, logging, typer

app = typer.Typer(help="Safely rename image files in a directory.")
logger = logging.getLogger(__name__)

@dataclass
class RenameOperation:
    source: Path
    destination: Path

    @property
    def would_overwrite(self) -> bool:
        return self.destination.exists()

def normalize_filename(name: str) -> str:                    # ← Types declare intent
    normalized = re.sub(r'\s+', '_', name.lower())
    return re.sub(r'[^\w\-.]', '', normalized)

def plan_renames(                                            # ← Separate planning from execution
    folder: Path, extensions: tuple[str, ...] = (".jpg", ".png")
) -> list[RenameOperation]:
    if not folder.exists():
        raise FileNotFoundError(f"Directory not found: {folder}")  # ← Specific exceptions
    return [
        RenameOperation(source=fp, destination=fp.parent / f"{normalize_filename(fp.stem)}{fp.suffix.lower()}")
        for fp in sorted(folder.iterdir())
        if fp.suffix.lower() in extensions
        and fp.parent / f"{normalize_filename(fp.stem)}{fp.suffix.lower()}" != fp
    ]

@app.command()
def rename(
    folder: Path = typer.Argument(..., help="Directory containing images"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Preview without renaming"),
) -> None:
    """Rename image files to normalized lowercase with underscores."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    operations = plan_renames(folder)
    for op in operations:
        if op.would_overwrite:                               # ← Overwrite protection
            logger.warning("Skipping %s: would overwrite", op.source.name)
        elif dry_run:                                        # ← Preview mode
            logger.info("[DRY RUN] %s -> %s", op.source.name, op.destination.name)
        else:
            try:
                op.source.rename(op.destination)
                logger.info("Renamed: %s -> %s", op.source.name, op.destination.name)
            except OSError as e:                             # ← Graceful failure
                logger.error("Failed: %s — %s", op.source.name, e)
```

And the tests that would have caught the Unicode crash before it reached production:

```python static
# tests/test_renamer.py
from pathlib import Path
from image_renamer.cli import normalize_filename, plan_renames

def test_normalize_removes_spaces() -> None:
    assert normalize_filename("My Photo Name") == "my_photo_name"

def test_normalize_handles_unicode_dashes() -> None:         # ← The test that was missing
    assert normalize_filename("file\u2014name") == "filename"

def test_plan_renames_raises_on_missing_directory() -> None:
    import pytest
    with pytest.raises(FileNotFoundError):
        plan_renames(Path("/nonexistent/path"))
```

The key differences between James's script and the program are not cosmetic. Each one prevents a specific class of failure:

| Aspect | Script | Program |
|--------|--------|---------|
| Errors | Crashes on missing folder | Raises specific exceptions with context |
| Safety | Can overwrite files | Checks for conflicts, skips with warning |
| Preview | No way to see what will happen | `--dry-run` flag shows planned changes |
| Types | None | Full annotations on all functions |
| Testing | "I ran it and it looked right" | Automated tests covering normal and edge cases |
| Interface | Edit source code to change folder | CLI with `--help`, arguments, options |
| Logging | `print()` | Structured logging with levels |

## The Python Discipline Stack

![Python Discipline Stack: four layered tools from uv at the foundation to pytest at the top, each catching a different class of defect](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-4/chapter-14/03-python-discipline-stack.png)

After the Friday incident, Emma set up the team's repository with what she called "the four walls" — four tools that together make it nearly impossible for a script-level mistake to reach production. Python is flexible enough to be used as both a scripting language and a systems programming language. The discipline stack is what transforms it from "quick and loose" into "verified and reliable."

| Tool | Role | What It Catches |
|------|------|-----------------|
| **uv** | Dependency management | Wrong versions, missing packages, environment conflicts |
| **pyright** | Static type checker | Wrong argument types, missing attributes, incompatible returns |
| **ruff** | Linter and formatter | Unused imports, style violations, common bugs, inconsistent formatting |
| **pytest** | Test runner | Logic errors, edge cases, regressions after changes |

These tools form layers of verification, each catching a different class of defect:

```
Layer 4: pytest     → Does the logic produce correct results?
Layer 3: pyright    → Do the types align across function boundaries?
Layer 2: ruff       → Does the code follow consistent patterns?
Layer 1: uv         → Are the dependencies resolved and reproducible?
```

### How They Work Together

A minimal `pyproject.toml` that activates the full stack:

```toml
[project]
name = "image-renamer"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["typer>=0.9.0"]

[project.scripts]
image-renamer = "image_renamer.cli:app"

[tool.pyright]
pythonVersion = "3.12"
typeCheckingMode = "standard"

[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

Running the full stack:

```bash
# Install dependencies in an isolated environment
uv sync

# Check types (catches mismatched arguments, wrong return types)
uv run pyright src/

# Lint and format (catches style issues, common bugs)
uv run ruff check src/ tests/
uv run ruff format src/ tests/

# Run tests (catches logic errors)
uv run pytest
```

Each tool catches problems the others miss. Pyright will not tell you that your rename logic is wrong -- that requires tests. Pytest will not tell you that you are passing a `str` where a `Path` is expected -- that requires pyright. Ruff will not tell you either of those things, but it will catch the unused import and the inconsistent formatting that make code harder to read and maintain.

## Why AI-Generated Code Requires Program Discipline

James's script was written by a human who understood the problem — he just did not apply the discipline the problem eventually demanded. AI-generated code introduces a sharper version of the same risk. When you write code yourself, you build a mental model of how it works as you type each line. You know the assumptions, the edge cases you considered, and the shortcuts you took deliberately. AI-generated code arrives fully formed with no trace of the reasoning behind it. You receive the output without the thought process.

This creates three specific risks that program discipline addresses:

### 1. Types Catch Hallucinated APIs

AI models sometimes generate code that calls functions or methods that do not exist, or passes arguments in the wrong order. Type checking catches this immediately:

```python static
# AI generated this -- looks reasonable
from pathlib import Path

def process_files(directory: str) -> list[str]:
    path = Path(directory)
    return path.list_files()  # pyright error: "Path" has no attribute "list_files"
```

Without pyright, this code would crash at runtime when a user first triggers that code path -- possibly in production, possibly weeks later. With pyright, you catch it before you ever run the code.

### 2. Tests Prevent Drift

AI does not remember previous sessions. Each time you ask it to modify code, it works from the current file content without understanding the history of decisions that shaped it. Tests encode your expectations permanently:

```python static
def test_normalize_preserves_hyphens() -> None:
    """This test exists because a previous AI edit removed hyphens.
    Hyphens are valid in filenames and should be preserved."""
    assert normalize_filename("my-photo-name") == "my-photo-name"
```

When a future AI edit accidentally changes `normalize_filename` to strip hyphens, this test fails immediately. The test is your memory; the AI has none.

### 3. CI Enforces Standards Across Sessions

You might forget to run pyright before committing. The AI certainly will not remind you. CI (Continuous Integration) enforces the discipline stack on every push, regardless of who or what wrote the code:

```yaml
# .github/workflows/check.yml
name: Verify
on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync
      - run: uv run pyright src/
      - run: uv run ruff check .
      - run: uv run pytest
```

This pipeline does not care whether a human or an AI wrote the code. It applies the same standards to both. Code that fails any check does not merge. This is your safety net against AI-generated code that looks correct but contains subtle issues.

## Anti-Patterns: Scripts Masquerading as Programs

Every company has a Script That Became Infrastructure. It is the Jupyter notebook that a data scientist wrote to clean up a CSV file — now running every Monday as part of the billing pipeline, with a comment that says `# TODO: handle empty dates` that has been there for fourteen months. It is the payment processing script from a hackathon — forty lines, no tests, a bare `except` on line 23 that silently swallows every error, including the one where a customer gets charged ten times the correct amount.

These scripts run. They run until they don't. And when they fail, they fail in ways that no one can diagnose — because there are no types to read, no tests to run, and no error messages to follow.

| Anti-Pattern | Why It Fails | Program Alternative |
|--------------|--------------|---------------------|
| Jupyter notebooks as production code | No tests, no types, cell execution order matters, hidden state between cells | Extract logic into modules, test independently |
| No type hints on functions | Callers cannot verify they are passing the right data; AI cannot validate its own output | Add type annotations: `def process(data: list[Record]) -> Summary:` |
| Bare `except Exception:` | Hides real errors, makes debugging impossible | Catch specific exceptions: `except FileNotFoundError:` |
| Hardcoded values in source code | Breaks in any environment besides your machine | Use environment variables or typed configuration |
| "It's too simple to test" | Simple code becomes complex code; tests document expected behavior | Even one test proves the function works and prevents regressions |

### The "Too Simple to Test" Trap

This anti-pattern deserves special attention because it sounds reasonable. A function that adds two numbers does not need a test. But production code is never that simple for long. The function that "just renames files" eventually needs to handle Unicode filenames, skip hidden files, preserve file permissions, and log operations. Each addition is "too simple to test" individually, but together they create untested complexity.

The cost of adding a test is low. The cost of debugging production failures in untested code is high. Write the test.

## The Decision Framework

Had James asked himself five questions before committing `rename_images.py`, the Friday incident would never have happened. These questions form a simple decision framework — a checklist that tells you whether your code has moved past the script boundary:

```
1. Will this code run more than once?
   YES → It needs tests.

2. Will someone else read or run this code?
   YES → It needs types and docstrings.

3. Does this code handle external input (files, APIs, user input)?
   YES → It needs specific error handling.

4. Will this code run in CI or production?
   YES → It needs all of the above, plus packaging (pyproject.toml).

5. Did an AI generate this code?
   YES → Apply extra scrutiny. Run pyright. Add tests for edge cases
         the AI may not have considered.
```

If you answered YES to any question, your code has moved past the script boundary. Apply program discipline proportional to the number of YES answers.

## Try With AI

### Prompt 1: Transform a Script into a Program

```
Here is a Python script I wrote to [describe your actual script -- processing CSV data,
calling an API, generating reports, etc.]:

[paste your script here]

Help me transform this into a proper program. Specifically:
1. Add type annotations to all functions
2. Replace bare except blocks with specific exceptions
3. Add a typer CLI interface so I can pass arguments
4. Write 3-5 pytest tests covering the main logic and one edge case
5. Create a pyproject.toml with pyright and ruff configuration

Walk me through each change and explain what class of bug it prevents.
```

**What you're learning**: The mechanical process of applying program discipline to existing code. By watching the transformation step-by-step, you internalize which changes catch which categories of bugs, and you develop an intuition for what "production-ready" looks like compared to "it works on my machine."

### Prompt 2: Audit AI-Generated Code

```
I asked an AI to generate this Python function:

```python static
def fetch_user_data(user_id):
    import requests
    resp = requests.get(f"http://api.example.com/users/{user_id}")
    data = resp.json()
    return {"name": data["name"], "email": data["email"], "age": data["age"]}
```

Audit this code against the "Programs Over Scripts" axiom. For each issue you find:
1. Name the specific anti-pattern
2. Explain what could go wrong in production
3. Show the fixed version with proper types, error handling, and structure

Then write 3 pytest tests that would catch the most dangerous failure modes.
```

**What you're learning**: Critical evaluation of AI-generated code. You are building the skill of reading code skeptically -- identifying missing error handling, absent type information, and implicit assumptions. This is the core verification skill for AI-era development: the AI generates, you verify.

### Prompt 3: Design a Discipline Stack for Your Project

```
I'm starting a new Python project that will [describe your project:
a CLI tool for file processing / an API client / a data pipeline / etc.].

Help me set up the complete Python discipline stack from scratch:
1. Project structure (src layout with pyproject.toml)
2. uv configuration for dependency management
3. pyright configuration (what strictness level and why)
4. ruff rules (which rule sets to enable for my use case)
5. pytest setup with a single example test
6. A pre-commit hook or Makefile that runs all four tools in sequence

Explain WHY each configuration choice matters -- don't just give me the config,
help me understand what each setting protects against.
```

**What you're learning**: Setting up verification infrastructure from the ground up. Understanding the "why" behind each tool configuration builds judgment about when to be strict (public APIs, shared code) versus lenient (prototypes, experiments). You are learning to create environments where bad code cannot survive.

## The Prototype Trap

Axiom III is not a prohibition against scripts. Scripts are the right tool for exploration — trying out an API, prototyping a data transformation, testing whether an approach works before committing to it. The axiom does not say "never write scripts." It says "do not ship scripts as if they were programs."

The danger has a name: the Prototype Trap. It works like this. You write a script to solve an immediate problem. It works. Someone asks to use it. You say yes — it is just a quick thing, after all. A month passes. The script now has three users, a cron job, and an implicit SLA that nobody agreed to but everyone depends on. You know you should add types and tests, but the script is working, and there are more urgent things to build. Six months pass. The script fails. Now you are debugging production infrastructure that has no types to read, no tests to run, and no error messages to follow — exactly the situation James found himself in.

The trap is not ignorance. James knew how to write a program. The trap is timing. The moment your script acquires its first external dependency — a second user, a cron schedule, a downstream process — it has crossed the boundary. That is the moment to stop and apply program discipline: types, tests, error handling, packaging. Not next sprint. Not when it breaks. Now. Because every week you delay, the script accumulates more dependencies and more expectations, and the cost of upgrading it from script to program grows. The Friday incident cost James's team a weekend. If the script had been running for a year instead of three months, it could have cost far more.

---

## Key Takeaways

James wrote fifteen lines of Python that worked perfectly — until three teams depended on them and a Unicode em-dash brought the house down. The axiom exists because every script wants to become a program, and the ones that do so without acquiring the discipline of a program become the production incidents that ruin weekends.

- **Scripts are for exploration; programs are for shipping.** The boundary is not about line count. It is about who depends on the code and what happens when it fails.
- **Five signals mark the crossing point**: someone else runs it, it runs more than once, it processes important data, it exceeds 50 lines of logic, or an AI generated it. Any one of these means program discipline applies.
- **The Python discipline stack — uv, pyright, ruff, pytest — forms four layers of verification.** Each catches a different class of defect. Together, they make it nearly impossible for a script-level mistake to reach production.
- **AI-generated code requires extra discipline, not less.** Types catch hallucinated APIs before runtime. Tests encode expectations that survive across AI sessions. CI enforces standards regardless of who or what wrote the code.
- **The Prototype Trap is about timing, not knowledge.** You know how to write a program. The axiom's discipline is applying that knowledge at the moment the script crosses the boundary — not after the first production incident.

---

## Looking Ahead

Your shell orchestrates programs. Your knowledge lives in markdown. Your programs have types, tests, and discipline. But each of these — the Makefile, the ADR, the well-typed module — is a single unit doing a single job. How do you combine them into something larger? How do you build a system from pieces that were designed to be composed?

In Axiom IV, you will discover that the answer is older than most programming languages — and that the Unix philosophy of small, composable tools is not just a preference. It is an architectural law.
