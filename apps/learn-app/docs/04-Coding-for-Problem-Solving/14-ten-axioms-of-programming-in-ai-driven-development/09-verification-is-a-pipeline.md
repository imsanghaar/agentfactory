---
sidebar_position: 9
title: "Axiom IX: Verification is a Pipeline"
description: "CI/CD automates verification of all changes — linting, types, tests, security — every time, without exception. If the pipeline fails, the code doesn't ship."
keywords: ["CI/CD", "GitHub Actions", "continuous integration", "verification pipeline", "Makefile", "automated testing", "linting", "type checking", "security audit"]
chapter: 14
lesson: 9
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding CI/CD as Automated Verification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can explain why automated verification pipelines are essential for AI-generated code and describe the verification pyramid layers"

  - name: "Configuring GitHub Actions Workflows"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can read and modify a GitHub Actions YAML workflow that runs linting, type checking, tests, and security audits"

  - name: "Implementing Local CI with Makefiles"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can create and use a Makefile that mirrors the CI pipeline locally, running all verification steps before pushing code"

  - name: "CI Culture and Anti-Pattern Recognition"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can identify CI anti-patterns (normalizing failures, shallow pipelines, skipping local checks) and explain why each undermines the verification guarantee"

learning_objectives:
  - objective: "Explain why automated CI pipelines are more critical for AI-generated code than for human-written code"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can articulate three reasons AI-generated code demands stronger automated verification (speed of generation, inconsistent quality, human review fatigue)"

  - objective: "Configure a GitHub Actions workflow that implements the full verification pyramid"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can write a ci.yml file with formatting, linting, type checking, unit tests, and security audit steps"

  - objective: "Create a Makefile that mirrors CI checks locally for fast feedback"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can run `make ci` locally and verify all checks pass before pushing to remote"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (verification pyramid, GitHub Actions, workflow YAML, matrix testing, Makefile targets, CI culture) within B1 range (5-7 concepts)"

differentiation:
  extension_for_advanced: "Add branch protection rules, required status checks, and deployment gates to the pipeline; implement parallel job execution and artifact caching strategies"
  remedial_for_struggling: "Focus on just two layers: run pytest and ruff check locally first, then translate those two commands into a minimal GitHub Actions workflow"
---

# Axiom IX: Verification is a Pipeline

Axiom VIII gave James a disciplined git history — every decision recorded, every change traceable. But git records *what happened*. It does not verify *whether it should have happened*. James had tests, types, and database constraints each running separately, on his machine, when he remembered to run them. He had never run all of them together, in order, automatically.

His first push to main since adopting the previous eight axioms failed in four minutes.

The formatter caught inconsistent indentation the AI had introduced in `shipping.py` — tabs mixed with spaces that looked identical in his editor. The linter found an unused import in `discount.py` that `ruff check` flagged but James had never run locally. The type checker discovered that `calculate_shipping()` returned `Optional[float]` in one branch but the calling code assumed `float` — a mismatch his tests never triggered because they only tested the happy path. And `pip-audit` reported a known vulnerability in a package the AI had suggested three weeks earlier.

None of these failures were exotic. They were routine — the kind of mistakes that slip through when the only verification is "I ran pytest on my machine and it passed." James had done everything right *within each axiom*. But he had never run all the checks *together*, in order, automatically.

"Your tests verify logic," Emma told him when he messaged her, frustrated. "But tests do not check formatting. Tests do not check types. Tests do not audit dependencies. You need a pipeline — a sequence of checks that runs *every* check, *every* time, automatically. If the pipeline fails, the code does not ship. No exceptions."

This is Axiom IX.

## The Problem Without This Axiom

James's failed push exposed a pattern that every developer who works with AI will recognize. He had verified his code — but only partially. He ran pytest. He did not run the formatter, the linter, the type checker, or the security auditor. Each tool catches a different category of error, and skipping any one of them leaves a gap.

**The "Works on My Machine" trap.** James's code passed on his laptop because he had Python 3.12, a specific OS, and packages installed from previous experiments. The GitHub Actions runner used a clean Ubuntu environment with Python 3.11. The type syntax `list[str]` worked on 3.12 but would fail on 3.10 — and production ran 3.11. Without a standardized verification environment, "it works on my machine" means nothing.

**The "I Already Tested It" illusion.** James ran pytest and saw green. But he did not run `ruff format --check`. He did not run `ruff check`. He did not run `pyright`. He did not run `pip-audit`. Manual verification is inherently incomplete because developers skip steps — especially late at night, especially when the AI assured them the code was correct.

**The "Review Fatigue" problem.** The AI had generated five hundred lines of order management code in thirty seconds. James could not meaningfully review every line. He skimmed, trusted the types, trusted the tests, and pushed. Without automated checks catching the issues his eyes missed, subtle bugs accumulated. The more code the AI generated, the more essential automated verification became.

## The Axiom Defined

> **Axiom IX: Verification is a Pipeline.** CI/CD automates the verification of all changes — formatting, linting, type checking, tests, security audits — every time, without exception. If the pipeline fails, the code does not ship.

This axiom transforms verification from a human discipline problem into an infrastructure guarantee. James did not need to *remember* to run the linter — the pipeline ran it. He did not need to *trust* that tests passed — the pipeline proved it. He did not need to *hope* there were no security vulnerabilities — the pipeline checked.

"The pipeline is the gatekeeper that never sleeps," Emma told him. "It never gets tired. It never decides 'it is probably fine.' It runs every check, every time, and it does not care that you are in a hurry."

## From Principle to Axiom

In Chapter 4, you learned **Principle 3: Verification as Core Step** — the mindset that every action should be verified. You learned to check that files exist after creating them, to confirm commands succeeded before moving on, to validate outputs before declaring victory.

Axiom IX elevates that principle from personal discipline to **infrastructure enforcement**:

| Principle 3 (Mindset) | Axiom IX (Infrastructure) |
|---|---|
| "Always verify your work" | "The pipeline always verifies all work" |
| Relies on human discipline | Runs automatically on every push |
| Can be forgotten or skipped | Cannot be bypassed (branch protection) |
| Checks what you remember to check | Checks everything, every time |
| Individual responsibility | Team-wide guarantee |

The principle taught you *why* to verify. The axiom teaches you *how* to make verification unavoidable. James had internalized the principle — he ran pytest before pushing. But the principle relies on human discipline, and human discipline has gaps. James forgot to run the linter. He forgot to run the type checker. He forgot to audit dependencies. The pipeline forgets nothing.

<details>
<summary>The Discipline That Preceded CI</summary>

The idea that integration should be continuous — not a painful event at the end of a project — emerged from the Extreme Programming movement in the late 1990s. In 2000, Martin Fowler published his influential article "Continuous Integration," describing a practice his team at ThoughtWorks had refined: every developer integrates their work at least daily, and every integration is verified by an automated build that runs the full test suite.

Before CI, integration was a dreaded phase. Teams worked in isolation for weeks or months, then spent days or weeks merging their changes together — a process so painful it earned the name "integration hell." Bugs that could have been caught in minutes festered for months because nobody verified how the pieces fit together until the end.

Fowler's insight was that integration pain grows exponentially with delay. If you integrate daily, each integration is small and manageable. If you integrate monthly, each integration is a nightmare. The solution was automation: a server that watches your repository, detects every change, and runs the full verification suite automatically. CruiseControl (2001) was one of the first CI servers. Jenkins (2011) made it mainstream. GitHub Actions (2019) made it accessible to every project with a repository.

James's failed push was a textbook example of what CI was designed to prevent. He had been working locally for two weeks, verifying only the checks he remembered to run. The pipeline ran *all* the checks — and found four problems that manual verification had missed.

</details>

## The Verification Pyramid

![Verification Timeline: six stages from fast Format checks to slow Security Audit, each gating the next](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-4/chapter-14/09-verification-timeline.png)

After James's failed push, Emma walked him through the architecture of a proper CI pipeline. "Not all checks are equal," she said. "They form a pyramid — fast, cheap checks at the base catch the most common issues, while slower, more thorough checks at the top catch deeper problems."

Each level catches different categories of problems:

| Level | Tool | What It Catches | Speed |
|-------|------|-----------------|-------|
| 1. Formatting | `ruff format --check` | Inconsistent style, whitespace | < 1 second |
| 2. Linting | `ruff check` | Unused imports, bad patterns, common bugs | 1-2 seconds |
| 3. Type Checking | `pyright` | Type mismatches, missing attributes, wrong signatures | 3-10 seconds |
| 4. Unit Tests | `pytest` | Logic errors, broken functions, regressions | 5-30 seconds |
| 5. Integration Tests | `pytest -m integration` | Component interaction failures | 30-120 seconds |
| 6. Security Audit | `pip-audit` | Known vulnerabilities in dependencies | 5-15 seconds |

**Why the pyramid matters**: If formatting fails, there is no need to wait for tests to run. Each level gates the next. Fast failures save time — and James learned to appreciate this when a one-second formatting check saved him from a three-minute test run.

### Why Each Level Exists

Emma walked James through each level, connecting it to a specific failure from his own project:

**Level 1 — Formatting** catches the trivial but distracting. The AI had introduced tabs mixed with spaces in `shipping.py` — invisible in James's editor but a failure in `ruff format --check`. This is the cheapest possible check: if the code cannot even be formatted consistently, there is no point running deeper analysis.

**Level 2 — Linting** catches the bugs hiding in plain sight. James's `discount.py` had an unused `import os` that the AI left behind from a previous generation. `ruff check` also catches variables assigned but never read, f-strings without placeholders, and `assert` statements with tuples (always truthy). These patterns look correct to a casual reader but indicate real problems.

**Level 3 — Type Checking** catches the structural errors. James's `calculate_shipping()` returned `Optional[float]` in one branch but the calling code assumed `float` — a mismatch his tests never triggered. `pyright` catches type mismatches, missing attributes, and wrong signatures statically, without running the code. It is like having a compiler for Python.

**Level 4 — Unit Tests** catch the logic errors — the exact category that produced the $12,000 discount bug. If `assert apply_discount(order, 0.15).total == 85.0` had existed in the pipeline, the wrong implementation would never have reached main. These are semantic bugs that only running the code can reveal.

**Level 5 — Integration Tests** catch the interaction failures. James's discount function worked in isolation, but when the shipping calculator called it with a large order, the rounding produced a one-cent discrepancy that compounded across line items. Components that work alone may fail together.

**Level 6 — Security Audit** catches the invisible threats. The AI had suggested `pip install requests==2.28.0` for James's order notification system. `pip-audit` flagged it: that version had a known vulnerability (PYSEC-2023-74). Three levels deep in the dependency tree, a package James had never heard of was compromised.

## GitHub Actions: Your Pipeline

After understanding the pyramid, James was ready to build it. Emma showed him GitHub Actions — the CI platform that runs verification pipelines on every push and pull request, using YAML workflow files stored in the repository itself.

"The pipeline lives in your code," Emma told him. "Version-controlled, reviewed, and permanent — just like the commit messages from Axiom VIII."

Here is the complete CI workflow James created for his order management project:

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  verify:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Cache pip dependencies
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements*.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      # Level 1: Formatting — catches tabs-vs-spaces in shipping.py
      - name: Check formatting
        run: ruff format --check .

      # Level 2: Linting — catches unused imports like `import os` in discount.py
      - name: Run linter
        run: ruff check .

      # Level 3: Type checking — catches Optional[float] vs float mismatches
      - name: Type check
        run: pyright

      # Level 4: Unit tests — catches logic errors like the $12,000 discount bug
      - name: Run unit tests
        run: pytest tests/ -v --tb=short

      # Level 5: Integration tests — catches rounding errors across modules
      - name: Run integration tests
        run: pytest tests/ -m integration -v --tb=short

      # Level 6: Security audit — catches vulnerable dependencies like requests 2.28.0
      - name: Security audit
        run: pip-audit
```

Each section serves a specific purpose:

**Triggers** (`on:`): The pipeline runs on every push to `main` and every pull request targeting `main`. No code reaches `main` without passing all checks. This was the rule James had been violating — pushing directly to main without any automated gate.

**Matrix Testing** (`strategy.matrix`): The pipeline runs against *both* Python 3.11 and 3.12. This catches version-specific issues — exactly the kind James hit when the AI generated `list[str]` syntax that worked on 3.12 but would fail on older versions. If the AI generates code using a newer Python feature, the matrix catches it.

**Caching** (`actions/cache`): Dependencies are cached between runs using a hash of the requirements files. First run installs everything; subsequent runs restore from cache unless dependencies change. This cut James's pipeline from three minutes to forty-five seconds.

**Sequential Steps**: The verification pyramid runs top-to-bottom. If formatting fails, linting never runs. This "fail fast" approach gives the quickest possible feedback — James's tab-vs-space error was caught in one second, not after a three-minute test suite.

### Branch Protection: Making CI Mandatory

"A pipeline that runs but can be ignored is theater, not verification," Emma told James. She showed him how to make CI truly enforceable:

1. Go to your repository Settings > Branches > Branch protection rules
2. Enable "Require status checks to pass before merging"
3. Select the `verify` job as a required check
4. Enable "Require branches to be up to date before merging"

Now the pipeline was not advisory — it was a gate. If CI failed, the merge button was disabled. No exceptions, no overrides. James could no longer push broken code to main even if he wanted to. The infrastructure enforced what discipline alone could not.

## Local CI: The Makefile

After two days of waiting three minutes for GitHub Actions to tell him about formatting errors, James asked Emma if there was a faster way. "Run the same checks locally before pushing," she said. "A Makefile gives you a single command that mirrors your CI pipeline."

```makefile
# Makefile

.PHONY: format lint typecheck test test-integration security ci clean

# Individual targets
format:
	ruff format --check .

lint:
	ruff check .

typecheck:
	pyright

test:
	pytest tests/ -v --tb=short

test-integration:
	pytest tests/ -m integration -v --tb=short

security:
	pip-audit

# Fix targets (auto-correct what can be fixed)
fix-format:
	ruff format .

fix-lint:
	ruff check --fix .

# The full CI pipeline — same checks as GitHub Actions
ci: format lint typecheck test security
	@echo "All CI checks passed."

# Run everything including integration tests
ci-full: format lint typecheck test test-integration security
	@echo "All CI checks (including integration) passed."

# Quick check — just formatting and linting (< 5 seconds)
quick:
	ruff format --check . && ruff check .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
```

### The Workflow With Local CI

James's daily development workflow became:

```bash
# 1. Write TDG tests, then have AI generate implementation
# 2. Quick check — catches 80% of issues in 2 seconds
make quick

# 3. Fix any formatting/linting issues automatically
make fix-format
make fix-lint

# 4. Full CI check before pushing
make ci

# 5. Only push if CI passes
git add src/shipping.py tests/test_shipping.py
git commit -m "feat(shipping): add international surcharge calculation"
git push
```

This workflow meant James almost never saw CI failures on GitHub. The pipeline became a safety net, not a bottleneck. He caught issues in five seconds locally rather than waiting three minutes for a remote failure.

### Why a Makefile?

James asked Emma why a Makefile instead of a shell script. The Makefile has specific advantages:

- **Convention**: Most open-source projects use Makefiles. Developers know to look for one.
- **Self-documenting**: Run `make` with no arguments to see available targets.
- **Composable**: `ci` is just `format + lint + typecheck + test + security` chained together.
- **Universal**: Make is installed on every Unix system. No extra dependencies.
- **Matches CI exactly**: Each Makefile target corresponds to one pipeline step. If `make ci` passes locally, GitHub Actions will pass remotely.

## Why CI Matters More With AI-Generated Code

Traditional CI protects against human error. With AI-generated code, the case for CI becomes overwhelming — and James experienced each reason firsthand:

**AI generates faster than humans can review.** The AI had generated five hundred lines of order management code in thirty seconds. James could not meaningfully verify every line. His eyes skipped the unused import, missed the type mismatch, and never noticed the vulnerable dependency. The pipeline caught all three in four minutes.

**AI makes confident-looking mistakes.** When a human writes buggy code, there are often signals — commented-out attempts, TODO markers, inconsistent naming that reveals uncertainty. The AI's `calculate_shipping()` had a perfect docstring, clean type annotations, and logical structure. It still returned `None` in one branch instead of `0.0`. The pipeline did not care how polished the code looked — it checked whether it *worked*.

**AI does not remember project conventions.** James had told the AI "use ruff for linting" in his CLAUDE.md, but it generated code with unused imports anyway. He specified "all functions need type annotations" but the AI forgot on the helper functions. The pipeline enforced conventions the AI forgot between prompts.

**AI introduces dependency risks.** The AI had suggested `pip install requests==2.28.0` for the order notification feature. Without `pip-audit` in the pipeline, James would never have known that version had a known security vulnerability.

## Anti-Patterns: What Bad CI Looks Like

Ask a team lead about their CI pipeline and watch their face. If they wince, you already know the story. The badge has been red so long that nobody looks at it anymore. "Just re-run it" is the standard response to failures. The pipeline technically exists but checks so little that it provides false confidence instead of real verification.

A developer merged a pull request while CI was still running because "it is probably fine." Flaky tests were disabled one by one until the suite tested nothing meaningful. The security audit was removed because "it kept failing on things we cannot fix." The pipeline takes forty-five minutes, so developers push without waiting and discover failures the next morning — if they check at all.

None of this happened in a single decision. It happened in a hundred five-second shortcuts: ignoring a red badge, skipping a slow check, disabling a noisy test. A hundred five-second shortcuts became a team that ships unverified code with confidence.

These specific patterns destroy the pipeline's value. Recognize and avoid them:

| Anti-Pattern | Why It Fails | The Fix |
|---|---|---|
| "I tested it on my machine" | Different environment, different results | CI runs in a standardized container |
| CI that only runs tests | Types, linting, security all skipped | Implement the full verification pyramid |
| Ignoring flaky tests | "It's just flaky" normalizes CI failures | Fix or quarantine flaky tests immediately |
| No local CI equivalent | Surprises at push time, slow feedback | Create `make ci` that mirrors the pipeline |
| CI takes 30+ minutes | Developers push without waiting, bypass CI | Cache aggressively, parallelize jobs, fail fast |
| Optional CI (no branch protection) | "I'll merge anyway, it's urgent" | Required status checks, no exceptions |
| Secrets in code | API keys committed, exposed in logs | Use GitHub Secrets and environment variables |
| CI that passes but doesn't check enough | False confidence from green checkmarks | Audit what CI actually verifies quarterly |

### The Most Dangerous Anti-Pattern

The single most destructive CI anti-pattern is **normalizing failures**. James saw it on a previous team: it started small — "That test is flaky, just re-run it." Then it became: "CI is red but it is not related to my change." Then: "We will fix CI next sprint." Within weeks, the pipeline was permanently red, nobody looked at it, and the team had lost their automated safety net entirely.

The rule Emma insisted on: **CI must always be green on main.** If a test is flaky, fix it or delete it. If a check is wrong, fix the check. Never let "red is normal" become the culture.

## CI as Culture

The deepest lesson of Axiom IX is not technical — it is cultural. Emma taught James three rules that shaped how he thought about his pipeline:

**"If it is not in CI, it is not enforced."** James had written "always use type annotations" in CLAUDE.md. The AI forgot on three helper functions. He had written "run `ruff check` before committing" in his project README. He forgot at 11pm. The only standards that actually got followed were the ones enforced by the pipeline. His CLAUDE.md was a *request*. His CI pipeline was a *guarantee*.

**"The pipeline is the source of truth."** At the post-mortem, the team lead had asked "does this code work?" and nobody could answer. With CI, the answer was never "I think so" or "it worked when I tested it." The answer was: "CI is green." The pipeline was the objective arbiter — the same pipeline that would have caught the $12,000 discount bug if it had existed two months earlier.

**"Fast CI is kind CI."** A pipeline that takes thirty minutes punishes developers for pushing code. They batch changes, push less frequently, and avoid small improvements because "it is not worth waiting for CI." James's pipeline took forty-five seconds with caching — fast enough that he ran `make ci` after every AI generation, exactly the way he ran TDG tests after every implementation. Small, frequent verification cycles from Axiom VII, encoded into infrastructure by Axiom IX.

## The Verification Chain

Axiom IX does not stand alone. It connects to the axioms before and after it:

- **Axiom VII (Tests Are the Specification)** gives you tests. Axiom IX *runs them automatically*. James wrote TDG specifications; the pipeline executed them on every push.
- **Axiom VIII (Version Control is Memory)** gives you commits. Axiom IX *verifies them before they reach main*. The disciplined commits from Axiom VIII flow through the pipeline from Axiom IX.
- **Axiom X (Observability Extends Verification)** takes over where CI stops — monitoring the code *after* it ships.

Together, they form a continuous verification chain: tests define correctness, the pipeline proves it before deployment, and observability confirms it in production. But the chain has a gap. James's pipeline verified that `calculate_shipping()` returned the right values for eleven test inputs. It could not verify that the function would survive ten thousand concurrent requests, a network timeout at 3am, or a database connection pool exhaustion under holiday traffic. The pipeline proves code is correct. It does not prove code is resilient — and that is where Axiom X begins.

## The Shallow Pipeline

A month after setting up CI, James helped a colleague on another team configure their pipeline. The colleague's `ci.yml` had two steps: `ruff format --check` and `ruff check`. That was it. No type checking. No tests. No security audit. The badge on their README was green — permanently green — and the colleague pointed to it proudly: "Our CI always passes."

"Your pipeline is shallow," Emma told them when James asked her to review it. "It checks formatting and linting — Level 1 and Level 2 of the pyramid. It does not check types, run tests, or audit dependencies. The green badge means your code is consistently formatted. It does not mean your code is correct, type-safe, or secure."

The Shallow Pipeline is the CI equivalent of the Green Bar Illusion from Axiom VII: a green badge that creates false confidence. The pipeline *technically* passes, but it verifies so little that passing means almost nothing. The colleague's project had a type error that crashed in production, a logic bug that doubled invoices, and a vulnerable dependency — all invisible to a pipeline that only checked formatting.

The fix is the full verification pyramid. Every level exists because it catches problems invisible to the levels below it. A pipeline without tests is like a spell-checker without grammar-checking — it catches some problems but misses the ones that matter most.

CI secrets are also part of pipeline discipline. Never put secrets directly in workflow files:

```yaml
# WRONG — secret exposed in code
- name: Deploy
  run: curl -H "Authorization: Bearer sk-abc123..." https://api.example.com/deploy

# RIGHT — secret stored in GitHub Secrets
- name: Deploy
  run: curl -H "Authorization: Bearer ${{ secrets.DEPLOY_TOKEN }}" https://api.example.com/deploy
```

James remembered the Permanent Record from Axiom VIII — once a secret is committed, it exists in git history forever. The same principle applies to CI: secrets stored in workflow files are visible to anyone with repository access. Store them in GitHub Settings > Secrets, never echo them in logs, and rotate them quarterly.

## Try With AI

### Prompt 1: Build Your CI Pipeline

```
I have a Python order management project with this structure:

order_management/
├── src/
│   └── orders/
│       ├── __init__.py
│       ├── models.py      (SQLModel Order, Customer classes)
│       ├── discount.py    (discount calculation logic)
│       ├── shipping.py    (shipping rate calculator)
│       └── api.py         (FastAPI endpoints)
├── tests/
│   ├── test_discount.py   (TDG specs for discount logic)
│   ├── test_shipping.py   (TDG specs for shipping rates)
│   └── test_api.py        (integration tests)
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── Makefile

Help me create:
1. A GitHub Actions workflow (.github/workflows/ci.yml) that implements the full
   verification pyramid (formatting, linting, types, tests, security)
2. A Makefile with targets for each level plus a combined `make ci`
3. A pyproject.toml section configuring ruff and pyright

For each file, explain what each section does and why it's there.
Then show me how to add branch protection so CI is mandatory.
```

**What you're learning:** Translating the verification pyramid into actual infrastructure files. Each step in the YAML catches a different category of error: formatting caught James's tab-vs-space issue, linting caught his unused import, type checking caught his `Optional[float]` mismatch, tests would have caught the discount bug, and `pip-audit` caught the vulnerable dependency. You are learning to wire these tools into a pipeline that runs automatically on every push.

### Prompt 2: Diagnose CI Failures

```
My CI pipeline for an order management project is failing with these errors.
Help me understand and fix each one:

Error 1 (ruff format):
  src/orders/shipping.py: would reformat

Error 2 (ruff check):
  src/orders/discount.py:3:1: F401 `os` imported but unused
  src/orders/api.py:15:5: B006 Do not use mutable data structures for argument defaults

Error 3 (pyright):
  src/orders/shipping.py:42:12 - error: Return type "float | None" is not assignable
    to declared return type "float"

Error 4 (pytest):
  FAILED tests/test_discount.py::test_fifteen_percent - AssertionError:
    assert 15.0 == 85.0

Error 5 (pip-audit):
  Name     Version  ID             Fix Versions
  requests 2.28.0   PYSEC-2023-74  2.31.0

For each error:
- What verification level caught it?
- Why didn't a lower level catch it?
- What's the fix?
- What would have happened if this reached production?
```

**What you're learning:** Reading and interpreting CI failure messages across all pyramid levels. Notice that Error 4 is exactly James's discount bug — the test caught it because the TDG specification defined what "correct" means. You are building the diagnostic skill of understanding *which* tool catches *which* category of error, and why the layered approach matters.

### Prompt 3: Extend Your Pipeline Beyond the Basics

```
My order management system's CI pipeline currently runs the standard verification
pyramid (formatting, linting, types, unit tests, security). But I need more:

- Integration tests that verify discount + shipping + invoicing work together
- Database migration tests (does schema.sql apply cleanly to a fresh database?)
- API contract tests (do endpoints return the expected response shapes?)
- Performance checks (does calculate_shipping stay under 100ms for 1000 orders?)

Help me design a tiered CI pipeline:
1. Fast checks (< 2 min) — run on every push
2. Medium checks (< 10 min) — run on PRs to main
3. Slow checks (< 30 min) — run nightly or on release branches

For each tier, explain what goes where and why. Show me the GitHub Actions
YAML for all three tiers. How do I handle checks that need a database?
```

**What you're learning:** Extending the verification pyramid beyond generic Python checks to domain-specific validation. James's pipeline caught formatting and type errors, but it did not test whether the discount, shipping, and invoicing modules worked *together*. You are practicing the architectural skill of designing pipelines that balance thoroughness with speed — catching real problems without making developers wait so long they bypass the checks.

## Key Takeaways

James's first push after adopting Axioms I through VIII failed on four checks he had never run manually. Emma's fix was not to run more checks by hand — it was to automate every check into a pipeline that runs on every push, without exception. Martin Fowler described this discipline in 2000 as Continuous Integration. GitHub Actions made it accessible to every project with a repository.

- **Verification is a pipeline, not a step.** James ran pytest and saw green, but he did not run the formatter, the linter, the type checker, or the security auditor. Each tool catches a different category of error. Skipping any one of them leaves a gap that AI-generated code will exploit.
- **The verification pyramid runs fast checks first.** Formatting takes one second. Linting takes two. Type checking takes five. Tests take thirty. Security audit takes ten. If formatting fails, there is no need to wait for tests. Fast failures save time — and keep developers from bypassing the pipeline.
- **Local CI mirrors remote CI.** `make ci` runs the same checks as GitHub Actions, in five seconds instead of three minutes. James caught issues locally before pushing, so the remote pipeline became a safety net rather than a bottleneck.
- **The Shallow Pipeline creates false confidence.** A CI badge that only checks formatting is like a green bar that only checks types — it tells you something passed, but not that your code is correct. The full pyramid is non-negotiable.
- **CI is culture, not configuration.** If it is not in CI, it is not enforced. If CI is always red, it is useless. If CI takes too long, developers bypass it. Fast, comprehensive, and always-green — that is the standard.

---

## Looking Ahead

Your shell orchestrates programs. Your knowledge lives in markdown. Your programs have types, tests, relational data, and disciplined git history. Your pipeline verifies every change before it reaches main. But what happens *after* deployment? James's pipeline proved that `calculate_shipping()` returned the right values for the test inputs. It could not prove that the function would handle ten thousand concurrent requests without running out of memory, or that the database connection pool would survive a network hiccup at 3am, or that the AI-generated retry logic would not create an infinite loop under production load.

In Axiom X, you will discover that observability extends verification beyond deployment — monitoring what your code actually does in the real world, where no test suite can reach.
