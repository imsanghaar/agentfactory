---
sidebar_position: 8
title: "Capstone: Full Test Suite for Task API"
description: "Compose all TDD patterns into a production-ready test suite. Write test specifications first, implement with AI, achieve 80%+ coverage, and automate with GitHub Actions."
keywords: [pytest, test coverage, test factories, CI/CD, GitHub Actions, capstone, production testing, test specification, codecov, agent testing]
chapter: 46
lesson: 8
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "Test Coverage Reporting"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can configure pytest-cov with coverage thresholds, generate HTML and XML reports, and identify uncovered code paths for targeted testing"

  - name: "Test Factory Pattern Implementation"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create reusable factory functions for test data generation with sensible defaults and override capabilities"

  - name: "CI/CD Test Automation"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can configure GitHub Actions workflow to run tests on every push and pull request, including coverage reporting and threshold enforcement"

learning_objectives:
  - objective: "Write test specifications before implementing tests using spec-first methodology"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Student produces test specification document with success criteria, test categories, and required test cases before writing code"

  - objective: "Implement test factories for consistent, maintainable test data creation"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates factories.py with reusable async factory functions that accept overrides"

  - objective: "Configure pytest-cov to achieve and enforce 80%+ code coverage"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "pyproject.toml shows coverage configuration with fail_under = 80, and pytest --cov achieves target"

  - objective: "Create GitHub Actions workflow for automated test execution"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Workflow runs on push/PR, executes tests, reports coverage, and blocks merge on failure"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (coverage reporting, test factories, CI/CD integration) at B2 proficiency—appropriate as capstone integration lesson"

differentiation:
  extension_for_advanced: "Add branch coverage, integrate mutation testing with mutmut, create reusable workflow templates for other projects"
  remedial_for_struggling: "Focus on coverage configuration first; add CI/CD after local tests achieve 80%+ coverage"
---

# Capstone: Full Test Suite for Task API

You've learned the patterns. Now compose them into a production test suite.

Over the past seven lessons, you've built expertise in:
- pytest-asyncio configuration and event loop management
- FastAPI endpoint testing with httpx AsyncClient
- SQLModel database testing with in-memory SQLite
- LLM call mocking with respx
- Agent tool isolation testing
- Multi-turn integration testing

This capstone brings everything together. You'll write a **test specification first**, then implement a comprehensive test suite that achieves:

- **80%+ code coverage** (enforced by configuration)
- **Under 10 second runtime** (fast feedback loop)
- **Zero LLM API calls** (zero cost testing)
- **Automated CI/CD** (tests run on every PR)

The spec-driven approach matters because it transforms you from "writing tests" to "designing test strategy." When you specify first, AI implements faster and more accurately.

## The Spec-First Approach

Before writing any test code, you'll create a specification document. This is the pattern you'll use for every project going forward—define success criteria before implementation.

### Test Specification Template

Create a file called `TEST_SPEC.md` in your project root:

```markdown
# Task API Test Suite Specification

## Success Criteria

- [ ] 80%+ code coverage (measured by pytest-cov)
- [ ] All tests pass in under 10 seconds
- [ ] Zero LLM API calls during test execution (respx.mock active)
- [ ] CI/CD workflow runs successfully on GitHub Actions
- [ ] No flaky tests (consistent pass/fail behavior)

## Test Categories

### 1. Unit Tests (tests/unit/)
Test individual functions and models in isolation.

- **test_models.py**: SQLModel CRUD, relationships, constraints
- **test_tools.py**: Agent tool functions (mocked dependencies)
- **test_utils.py**: Utility functions (formatters, validators)

### 2. Integration Tests (tests/integration/)
Test API endpoints and component interactions.

- **test_tasks.py**: Task CRUD endpoints (all HTTP methods)
- **test_auth.py**: Authentication flows (success and failure)
- **test_agent.py**: Agent chat endpoint (mocked LLM)

### 3. End-to-End Tests (tests/e2e/)
Test complete user workflows.

- **test_flows.py**: Multi-step user journeys (mocked LLM)

## Required Test Cases

### Task Model (tests/unit/test_models.py)
- [ ] Create task with required fields
- [ ] Create task with optional fields
- [ ] Update task status
- [ ] Delete task (soft delete if applicable)
- [ ] Cascade delete with project relationship

### Task API (tests/integration/test_tasks.py)
- [ ] POST /api/tasks - create task (201)
- [ ] GET /api/tasks - list all tasks (200)
- [ ] GET /api/tasks/{id} - get single task (200)
- [ ] GET /api/tasks/{id} - task not found (404)
- [ ] PUT /api/tasks/{id} - full update (200)
- [ ] PATCH /api/tasks/{id} - partial update (200)
- [ ] DELETE /api/tasks/{id} - delete task (204)
- [ ] POST /api/tasks - validation error (422)

### Authentication (tests/integration/test_auth.py)
- [ ] Access protected endpoint with valid token (200)
- [ ] Access protected endpoint without token (401)
- [ ] Access protected endpoint with expired token (401)
- [ ] Access protected endpoint with invalid token (401)

### Agent Chat (tests/integration/test_agent.py)
- [ ] Chat with simple query (mocked LLM response)
- [ ] Chat with tool call (mocked LLM tool call + response)
- [ ] Chat with multi-turn conversation (mocked sequence)
- [ ] Handle LLM timeout gracefully

### User Flows (tests/e2e/test_flows.py)
- [ ] Create project -> create task -> complete task
- [ ] Search tasks -> update status -> verify change
- [ ] Ask agent to create task -> verify in database

## Test Data Strategy

Use factories for consistent test data:
- `create_test_user()` - authenticated user
- `create_test_task()` - task with defaults
- `create_test_project()` - project with defaults

## Mocking Strategy

- **LLM calls**: respx at HTTP transport layer
- **Authentication**: dependency override with test user
- **Database**: in-memory SQLite with StaticPool
- **External APIs**: respx for any HTTP calls
```

This specification becomes your contract. Every checkbox is a test you'll implement.

## Test Factories

Factories create consistent test data without repetitive boilerplate. They're the foundation of maintainable test suites.

### Creating the Factories Module

```python
# tests/factories.py
"""
Test data factories for Task API.

Usage:
    user = await create_test_user(session)
    task = await create_test_task(session, user_id=user.id)
    task_with_override = await create_test_task(session, user_id=user.id, title="Custom Title")
"""

from sqlmodel.ext.asyncio.session import AsyncSession
from app.models import User, Task, Project
from datetime import datetime, timezone


async def create_test_user(session: AsyncSession, **overrides) -> User:
    """Create a test user with sensible defaults.

    Args:
        session: Database session
        **overrides: Fields to override (email, name, etc.)

    Returns:
        Created User instance with database ID
    """
    defaults = {
        "email": f"test_{datetime.now().timestamp()}@example.com",
        "name": "Test User",
        "hashed_password": "hashed_test_password",
        "is_active": True,
    }
    user = User(**{**defaults, **overrides})
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def create_test_task(
    session: AsyncSession,
    user_id: int,
    **overrides
) -> Task:
    """Create a test task with sensible defaults.

    Args:
        session: Database session
        user_id: Owner user ID (required)
        **overrides: Fields to override (title, status, priority, etc.)

    Returns:
        Created Task instance with database ID
    """
    defaults = {
        "title": "Test Task",
        "description": "A test task for testing purposes",
        "status": "pending",
        "priority": "medium",
        "user_id": user_id,
    }
    task = Task(**{**defaults, **overrides})
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def create_test_project(
    session: AsyncSession,
    user_id: int,
    **overrides
) -> Project:
    """Create a test project with sensible defaults.

    Args:
        session: Database session
        user_id: Owner user ID (required)
        **overrides: Fields to override (name, description, etc.)

    Returns:
        Created Project instance with database ID
    """
    defaults = {
        "name": "Test Project",
        "description": "A test project for testing purposes",
        "user_id": user_id,
    }
    project = Project(**{**defaults, **overrides})
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project


async def create_test_task_with_project(
    session: AsyncSession,
    user_id: int,
    **overrides
) -> tuple[Task, Project]:
    """Create a task linked to a project.

    Args:
        session: Database session
        user_id: Owner user ID (required)
        **overrides: Task field overrides (project created with defaults)

    Returns:
        Tuple of (Task, Project) instances
    """
    project = await create_test_project(session, user_id=user_id)
    task = await create_test_task(
        session,
        user_id=user_id,
        project_id=project.id,
        **overrides
    )
    return task, project
```

**Output:**
```python
# Using factories in tests:
user = await create_test_user(session)
# User(id=1, email="test_1234567890.123@example.com", name="Test User")

task = await create_test_task(session, user_id=user.id)
# Task(id=1, title="Test Task", status="pending", user_id=1)

custom_task = await create_test_task(
    session,
    user_id=user.id,
    title="Custom Title",
    priority="high"
)
# Task(id=2, title="Custom Title", priority="high", user_id=1)
```

### Why Factories Matter

| Without Factories | With Factories |
|-------------------|----------------|
| Duplicate setup code in every test | Single source of truth |
| Hardcoded values scattered everywhere | Sensible defaults, easy overrides |
| Tests break when model changes | Update factory once |
| Unclear test data intent | Self-documenting parameters |
| Inconsistent test data | Guaranteed consistency |

## Coverage Configuration

pytest-cov measures how much of your code runs during tests. Configure it to **enforce** minimum coverage so quality never regresses.

### pyproject.toml Configuration

```toml
# pyproject.toml

[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
testpaths = ["tests"]
addopts = "-v --tb=short"

[tool.coverage.run]
source = ["app"]
branch = true
omit = [
    "tests/*",
    "migrations/*",
    "app/main.py",  # Entry point, tested via integration
    "*/__init__.py",
]

[tool.coverage.report]
fail_under = 80
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if TYPE_CHECKING:",
    "if __name__ == .__main__.:",
]

[tool.coverage.html]
directory = "htmlcov"
```

**Key settings explained:**

| Setting | Purpose |
|---------|---------|
| `source = ["app"]` | Only measure your application code |
| `branch = true` | Measure branch coverage (if/else paths) |
| `omit = [...]` | Exclude test files, migrations, entry points |
| `fail_under = 80` | **Fail CI if coverage drops below 80%** |
| `show_missing = true` | Show which lines aren't covered |

### Running with Coverage

```bash
# Run tests with coverage report
pytest --cov=app --cov-report=term-missing

# Generate HTML report (opens in browser)
pytest --cov=app --cov-report=html
open htmlcov/index.html

# Generate XML for CI/CD tools (Codecov, etc.)
pytest --cov=app --cov-report=xml

# Combine all reports
pytest --cov=app --cov-report=term-missing --cov-report=html --cov-report=xml
```

**Output:**
```
---------- coverage: platform darwin, python 3.12.0 ----------
Name                      Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------------------
app/models.py                42      3      8      2    91%   45-47
app/routes/tasks.py          65      5     18      3    90%   78, 82-84
app/routes/agent.py          38      8     12      4    76%   29-36
app/tools.py                 28      2      6      1    92%   41-42
----------------------------------------------------------------------
TOTAL                       173     18     44     10    87%

Required test coverage of 80.0% reached. Total coverage: 87.00%
```

### Interpreting Coverage Reports

The HTML report shows exactly which lines are covered:

- **Green lines**: Executed during tests
- **Red lines**: Never executed (need tests)
- **Yellow lines**: Partially covered branches (only one path tested)

Focus on red and yellow lines in critical paths—authentication, error handling, and data validation.

## GitHub Actions CI/CD

Automate testing so every push and pull request runs your full test suite.

### Workflow Configuration

```yaml
# .github/workflows/test.yml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Run tests with coverage
        run: uv run pytest --cov=app --cov-report=xml --cov-report=term-missing
        env:
          DATABASE_URL: "sqlite+aiosqlite:///:memory:"
          OPENAI_API_KEY: "test-key-not-used"

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
          fail_ci_if_error: true
```

**What each step does:**

| Step | Purpose |
|------|---------|
| `actions/checkout@v4` | Clone your repository |
| `actions/setup-python@v5` | Install Python 3.12 |
| `astral-sh/setup-uv@v5` | Install uv package manager |
| `uv sync --all-extras` | Install all dependencies |
| `pytest --cov ...` | Run tests with coverage |
| `codecov/codecov-action@v4` | Upload coverage to Codecov dashboard |

### Branch Protection Rules

After setting up CI/CD, configure branch protection:

1. Go to **Settings > Branches > Branch protection rules**
2. Add rule for `main` branch
3. Enable **Require status checks to pass before merging**
4. Select your test workflow as a required check

Now code cannot merge to main if tests fail.

## Complete Test Suite Structure

Here's the full directory structure after implementing everything:

```
your-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── auth.py
│   ├── tools.py
│   └── routes/
│       ├── __init__.py
│       ├── tasks.py
│       └── agent.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures (from L02, L03)
│   ├── factories.py             # Test data factories (this lesson)
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_models.py       # SQLModel tests (L04)
│   │   ├── test_tools.py        # Tool isolation tests (L06)
│   │   └── test_utils.py        # Utility function tests
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_tasks.py        # Task API tests (L03)
│   │   ├── test_auth.py         # Authentication tests
│   │   └── test_agent.py        # Agent tests with mocked LLM (L05, L07)
│   └── e2e/
│       ├── __init__.py
│       └── test_flows.py        # End-to-end workflows (L07)
├── .github/
│   └── workflows/
│       └── test.yml             # CI/CD workflow (this lesson)
├── TEST_SPEC.md                 # Test specification (this lesson)
├── pyproject.toml               # pytest + coverage config
└── htmlcov/                     # Generated coverage report
```

### Test Count Summary

Following your specification, you should have approximately:

| Category | File | Test Count |
|----------|------|------------|
| Unit | test_models.py | 5 tests |
| Unit | test_tools.py | 4 tests |
| Unit | test_utils.py | 3 tests |
| Integration | test_tasks.py | 8 tests |
| Integration | test_auth.py | 4 tests |
| Integration | test_agent.py | 4 tests |
| E2E | test_flows.py | 3 tests |
| **Total** | | **31 tests** |

Runtime target: **under 10 seconds** for all 31 tests (in-memory DB, mocked LLM).

## Verification Checklist

Before considering your test suite complete, verify:

**Coverage:**
- [ ] `pytest --cov` shows 80%+ coverage
- [ ] No critical paths (auth, validation) below 90%
- [ ] HTML report reviewed for missed branches

**Performance:**
- [ ] Full suite completes in under 10 seconds
- [ ] No individual test takes >1 second
- [ ] No flaky tests (run suite 5 times, all pass)

**Isolation:**
- [ ] `respx.mock` active (zero network calls)
- [ ] Each test runs independently (random order works)
- [ ] No shared state between tests

**CI/CD:**
- [ ] GitHub Actions workflow runs on push
- [ ] PR blocked if tests fail
- [ ] Coverage uploaded to Codecov

**Documentation:**
- [ ] TEST_SPEC.md checkboxes all checked
- [ ] factories.py has docstrings
- [ ] conftest.py fixtures documented

Run this final verification:

```bash
# Verify coverage threshold
pytest --cov=app --cov-fail-under=80

# Verify speed
time pytest

# Verify isolation (random order)
pytest --random-order

# Verify no network calls
pytest --tb=short  # Should complete without API keys
```

**Expected output:**
```
============================= test session starts =============================
collected 31 items

tests/unit/test_models.py .....                                          [ 16%]
tests/unit/test_tools.py ....                                            [ 29%]
tests/unit/test_utils.py ...                                             [ 39%]
tests/integration/test_tasks.py ........                                 [ 64%]
tests/integration/test_auth.py ....                                      [ 77%]
tests/integration/test_agent.py ....                                     [ 90%]
tests/e2e/test_flows.py ...                                              [100%]

---------- coverage: platform darwin, python 3.12.0 ----------
Required test coverage of 80.0% reached. Total coverage: 87.00%

============================= 31 passed in 6.23s ==============================
```

## Try With AI

Work with your AI assistant to implement and refine your test suite.

### Prompt 1: Implement from Specification

```
Here's my test specification for the Task API:

[Paste your TEST_SPEC.md contents]

I have these patterns from my agent-tdd skill:
- conftest.py with AsyncClient and dependency overrides
- respx mocking for LLM calls
- In-memory SQLite with StaticPool

Implement the test suite following this specification. Start with
tests/integration/test_tasks.py since it has the most test cases.
Use the factory pattern for test data.
```

**What you're learning:** Specification-first implementation. You provide the contract; AI provides the code that fulfills it. This is faster and more accurate than ad-hoc test writing.

### Prompt 2: Achieve Coverage Target

```
My coverage report shows 72%. Here are the uncovered lines:

app/routes/tasks.py: 78, 82-84 (error handling for invalid status)
app/routes/agent.py: 29-36 (LLM timeout handling)
app/tools.py: 41-42 (validation edge case)

Generate specific tests to cover these paths. For the agent.py timeout
handling, use respx with side_effect=httpx.TimeoutException.
```

**What you're learning:** Using coverage as a guide for systematic test improvement. Coverage reports tell you exactly what's missing; AI generates tests for those specific paths.

### Prompt 3: Optimize Test Performance

```
My test suite takes 18 seconds. I profiled and found:
- Database setup/teardown: 8 seconds
- Agent tests with multiple mocks: 6 seconds
- Everything else: 4 seconds

How can I optimize without sacrificing isolation? Options I'm considering:
1. Session-scoped database fixture
2. Parameterized tests instead of separate functions
3. Factory optimization

Walk me through the trade-offs and recommend an approach.
```

**What you're learning:** Performance optimization for test suites. Fast tests run more often, which means faster feedback and fewer regressions. AI helps you navigate trade-offs between speed and isolation.

## Final Skill Reflection

This is the last lesson. Your `agent-tdd` skill should now be production-ready.

### Test Your Complete Skill

```
Using my agent-tdd skill, generate a complete test suite specification
for a NEW FastAPI agent project (not Task API—something fresh, like
a document Q&A system).

Verify my skill includes all patterns I learned:
1. pytest-asyncio setup (pyproject.toml configuration)
2. conftest.py with httpx AsyncClient and dependency overrides
3. In-memory SQLite with StaticPool
4. respx LLM mocking with correct OpenAI/Anthropic response structures
5. Tool isolation testing pattern
6. Multi-turn integration testing with side_effect
7. Test factories with defaults and overrides
8. Coverage configuration (80% threshold)
9. GitHub Actions workflow

If any pattern is missing or incomplete, identify the gap.
```

This is the ultimate test of your skill. Can it generate a complete testing strategy for a project you haven't built yet? If yes, you've created a reusable Digital FTE component.

### Finalize Your Skill

After testing, add any missing patterns:

```
My agent-tdd skill is almost complete. Add these final patterns
that I learned in the capstone:

1. Test specification template (TEST_SPEC.md format)
2. Factory pattern with async functions and overrides
3. Coverage configuration in pyproject.toml
4. GitHub Actions workflow with Codecov integration
5. Verification checklist for production-ready test suites

Also add a "Quick Start" section that generates a complete test
setup for any new FastAPI + SQLModel + Agent project in under
30 seconds.
```

### What You've Built

Over 8 lessons, you've built an `agent-tdd` skill that can:

| Capability | Source Lesson |
|------------|---------------|
| Distinguish TDD from Evals | L01 |
| Configure pytest-asyncio | L02 |
| Test FastAPI with httpx | L03 |
| Test SQLModel with in-memory DB | L04 |
| Mock any LLM call with respx | L05 |
| Isolate and test agent tools | L06 |
| Test multi-turn agent flows | L07 |
| Enforce coverage and CI/CD | L08 (Capstone) |

This skill is transferable to any Python agent project. You can:
- Clone a new project
- Invoke your skill
- Get a complete test suite specification
- Implement with AI assistance
- Achieve 80%+ coverage
- Ship with confidence

That's the Digital FTE pattern: **own the skill, scale the output**.

### Next Steps

Your agent-tdd skill is complete. Where to go from here:

1. **Chapter 47 (Evals for Agents)**: Learn probabilistic evaluation for LLM reasoning quality
2. **Apply to your projects**: Use this skill on your next FastAPI + Agent project
3. **Share your skill**: Publish to the Claude Code Skills Lab for others to use
4. **Extend**: Add mutation testing (mutmut), property-based testing (hypothesis), or load testing

You're now equipped to test any AI agent codebase with production-grade confidence.
