---
sidebar_position: 2
title: "pytest Fundamentals for Async Code"
description: "Configure pytest-asyncio and write async test functions with proper event loop management for agent testing"
keywords: [pytest, pytest-asyncio, async testing, event loop, fixtures, python testing]
chapter: 46
lesson: 2
duration_minutes: 25

skills:
  - name: "pytest-asyncio Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student configures pytest-asyncio in pyproject.toml with correct mode and fixture loop scope settings"

  - name: "Async Test Function Writing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student writes async test functions using @pytest.mark.asyncio decorator and await syntax"

  - name: "Event Loop Management"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student explains why session-scoped event loops are needed for shared fixtures and can implement the pattern"

  - name: "Async Fixture Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student creates async fixtures with proper setup/teardown using yield pattern"

learning_objectives:
  - objective: "Configure pytest-asyncio with auto mode and function-scoped event loops"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates pyproject.toml with correct [tool.pytest.ini_options] configuration"

  - objective: "Write async test functions that correctly await asynchronous operations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student writes 3 passing async tests using @pytest.mark.asyncio decorator"

  - objective: "Implement session-scoped event loop fixture for shared async resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates conftest.py with working event_loop fixture"

  - objective: "Create async fixtures with proper setup and teardown"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student implements async fixture using yield for cleanup"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (pytest-asyncio config, async test functions, event loop scope, async fixtures) within B1 limit of 7-10 concepts"

differentiation:
  extension_for_advanced: "Explore pytest-asyncio strict mode and fixture scope interactions; investigate asyncio.timeout() patterns"
  remedial_for_struggling: "Focus on basic async test with @pytest.mark.asyncio; defer event loop fixture until comfortable with basics"
---

# pytest Fundamentals for Async Code

Agent code is async. Your tests must be async too.

When you call an LLM API, query a database, or make an HTTP request, you're using `async def` functions that return coroutines. These coroutines need an event loop to run. Regular pytest doesn't know how to handle `await`—it will simply fail with a cryptic error about coroutines never being awaited.

This lesson teaches you to configure pytest for async testing. You'll set up pytest-asyncio, write your first async tests, and understand the event loop patterns that make async testing reliable. By the end, you'll have a working test foundation for all the agent testing patterns in this chapter.

---

## Project Setup

First, install the testing dependencies. Open your terminal in your project directory:

```bash
uv add --dev pytest pytest-asyncio httpx respx pytest-cov
```

**Output:**

```
Resolved 12 packages in 1.2s
Installed 5 packages in 0.8s
 + httpx==0.28.1
 + pytest==8.3.4
 + pytest-asyncio==0.24.0
 + pytest-cov==6.0.0
 + respx==0.22.0
```

Each package serves a specific purpose:

| Package | Purpose |
|---------|---------|
| `pytest` | Test framework |
| `pytest-asyncio` | Async test support |
| `httpx` | Async HTTP client for API testing |
| `respx` | HTTP mocking for LLM calls |
| `pytest-cov` | Test coverage reporting |

---

## pytest Configuration

Configure pytest in your `pyproject.toml`. Add this section:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
testpaths = ["tests"]
```

What each setting does:

| Setting | Value | Effect |
|---------|-------|--------|
| `asyncio_mode` | `"auto"` | Automatically detect async tests (no decorator needed in most cases) |
| `asyncio_default_fixture_loop_scope` | `"function"` | Each test gets a fresh event loop |
| `testpaths` | `["tests"]` | Look for tests in the `tests/` directory |

The `function` scope for event loops means each test runs in isolation. No test can pollute another test's event loop state. This is crucial for reliable, reproducible tests.

---

## Your First Async Test

Create a `tests/` directory and add your first test file:

```bash
mkdir -p tests
touch tests/test_async_basics.py
```

Write a simple async test:

```python
# tests/test_async_basics.py
import pytest
import asyncio

async def fetch_data():
    """Simulate an async operation."""
    await asyncio.sleep(0.01)  # Simulate network delay
    return {"status": "success", "data": [1, 2, 3]}

@pytest.mark.asyncio
async def test_fetch_data_returns_success():
    """Test that fetch_data returns success status."""
    result = await fetch_data()

    assert result["status"] == "success"
    assert len(result["data"]) == 3
```

Run the test:

```bash
pytest tests/test_async_basics.py -v
```

**Output:**

```
========================= test session starts ==========================
platform darwin -- Python 3.12.0, pytest-8.3.4, pluggy-1.5.0
plugins: asyncio-0.24.0, cov-6.0.0
asyncio: mode=auto, default_loop_scope=function
collected 1 item

tests/test_async_basics.py::test_fetch_data_returns_success PASSED  [100%]

========================== 1 passed in 0.05s ===========================
```

Notice the `@pytest.mark.asyncio` decorator. This tells pytest-asyncio to:

1. Create an event loop for this test
2. Run the async test function as a coroutine
3. Clean up the event loop when done

With `asyncio_mode = "auto"`, you can often skip the decorator—pytest-asyncio detects `async def` automatically. However, explicitly marking async tests is a good habit for clarity.

---

## Event Loop Scope

By default, each test function gets its own event loop. But what if you need to share expensive resources—like a database connection—across multiple tests?

That's where the session-scoped event loop comes in.

### The Problem

Consider this scenario:

```python
# This WON'T work with function-scoped loops
@pytest.fixture(scope="session")
async def database_connection():
    """Expensive connection we want to share."""
    conn = await create_connection()
    yield conn
    await conn.close()
```

A session-scoped async fixture needs a session-scoped event loop. If the fixture outlives the event loop, you get "Event loop is closed" errors.

### The Solution

Create a session-scoped event loop fixture in `tests/conftest.py`:

```python
# tests/conftest.py
import asyncio
import pytest

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for session-scoped fixtures.

    Required when:
    - Using session-scoped async fixtures
    - Sharing database connections across tests
    - Expensive setup that should run once
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
```

This fixture:

1. Creates a new event loop at the start of the test session
2. Yields the loop for all tests to use
3. Closes the loop when the session ends

Now session-scoped async fixtures work correctly:

```python
# tests/conftest.py (continued)
@pytest.fixture(scope="session")
async def shared_resource(event_loop):
    """Session-scoped async fixture."""
    resource = await expensive_setup()
    yield resource
    await expensive_teardown(resource)
```

### When to Use Each Scope

| Scope | Event Loop | Use When |
|-------|------------|----------|
| `function` | Fresh per test | Default. Each test is isolated. |
| `session` | Shared | Expensive setup (DB connections, API clients) |

For this chapter, we'll use function-scoped loops for isolation. The session-scoped pattern becomes important when test speed matters and setup is expensive.

---

## Async Fixtures

Fixtures provide test data and resources. Async fixtures work the same way as regular fixtures, but they can `await` operations.

### Basic Async Fixture

```python
# tests/conftest.py
import pytest

@pytest.fixture
async def sample_data():
    """Async fixture that provides test data."""
    # Simulate fetching data from an async source
    await asyncio.sleep(0.01)
    return {"id": 1, "name": "Test Item", "active": True}
```

Use it in a test:

```python
# tests/test_fixtures.py
import pytest

@pytest.mark.asyncio
async def test_sample_data_has_required_fields(sample_data):
    """Test that sample_data fixture provides expected structure."""
    assert "id" in sample_data
    assert "name" in sample_data
    assert sample_data["active"] is True
```

### Fixture with Cleanup

Many resources need cleanup after tests. Use `yield` to separate setup from teardown:

```python
# tests/conftest.py
@pytest.fixture
async def temporary_file():
    """Async fixture with cleanup."""
    import aiofiles
    import os

    # Setup: create file
    filepath = "/tmp/test_file.txt"
    async with aiofiles.open(filepath, "w") as f:
        await f.write("test content")

    yield filepath  # Test runs here

    # Teardown: remove file
    if os.path.exists(filepath):
        os.remove(filepath)
```

The pattern is:

1. **Setup** (before `yield`): Create resources
2. **Yield**: Provide the resource to the test
3. **Teardown** (after `yield`): Clean up resources

Teardown runs even if the test fails. This prevents resource leaks.

### Fixture Dependencies

Fixtures can depend on other fixtures:

```python
# tests/conftest.py
@pytest.fixture
async def database_session():
    """Create async database session."""
    session = await create_session()
    yield session
    await session.close()

@pytest.fixture
async def user_in_database(database_session):
    """Create a user that depends on database session."""
    user = User(name="Test User", email="test@example.com")
    database_session.add(user)
    await database_session.commit()
    await database_session.refresh(user)
    yield user
    # Cleanup handled by database_session fixture
```

pytest resolves the dependency chain automatically.

---

## Hands-On Exercise

Create a complete async test setup for a simple async function.

### Step 1: Create conftest.py

Create `tests/conftest.py` with the event loop fixture:

```python
# tests/conftest.py
import asyncio
import pytest

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for session-scoped fixtures."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def async_counter():
    """Fixture that provides an async counter."""
    class Counter:
        def __init__(self):
            self.value = 0

        async def increment(self):
            await asyncio.sleep(0.001)  # Simulate async operation
            self.value += 1
            return self.value

        async def reset(self):
            await asyncio.sleep(0.001)
            self.value = 0

    counter = Counter()
    yield counter
    await counter.reset()  # Cleanup
```

### Step 2: Write Three Async Tests

Create `tests/test_counter.py`:

```python
# tests/test_counter.py
import pytest

@pytest.mark.asyncio
async def test_counter_starts_at_zero(async_counter):
    """Test that counter initializes to zero."""
    assert async_counter.value == 0

@pytest.mark.asyncio
async def test_increment_increases_value(async_counter):
    """Test that increment increases counter by one."""
    result = await async_counter.increment()

    assert result == 1
    assert async_counter.value == 1

@pytest.mark.asyncio
async def test_multiple_increments(async_counter):
    """Test that multiple increments accumulate correctly."""
    await async_counter.increment()
    await async_counter.increment()
    result = await async_counter.increment()

    assert result == 3
    assert async_counter.value == 3
```

### Step 3: Run the Tests

```bash
pytest tests/test_counter.py -v
```

**Expected Output:**

```
========================= test session starts ==========================
platform darwin -- Python 3.12.0, pytest-8.3.4, pluggy-1.5.0
plugins: asyncio-0.24.0
asyncio: mode=auto, default_loop_scope=function
collected 3 items

tests/test_counter.py::test_counter_starts_at_zero PASSED          [ 33%]
tests/test_counter.py::test_increment_increases_value PASSED       [ 66%]
tests/test_counter.py::test_multiple_increments PASSED             [100%]

========================== 3 passed in 0.08s ===========================
```

All three tests pass. Each test gets a fresh counter due to function-scoped fixtures.

---

## Common Mistakes

### Mistake 1: Forgetting the Decorator

```python
# WRONG - Missing @pytest.mark.asyncio
async def test_something():
    result = await async_function()
    assert result

# RIGHT - Decorator present
@pytest.mark.asyncio
async def test_something():
    result = await async_function()
    assert result
```

Without the decorator (and without auto mode), pytest treats the function as synchronous and the coroutine never executes.

### Mistake 2: Missing await

```python
# WRONG - Forgot await
@pytest.mark.asyncio
async def test_data():
    result = fetch_data()  # Returns coroutine, not result!
    assert result["status"] == "success"  # Fails!

# RIGHT - Proper await
@pytest.mark.asyncio
async def test_data():
    result = await fetch_data()  # Actually executes
    assert result["status"] == "success"  # Works!
```

Forgetting `await` is the most common async mistake. The test might pass but not actually test anything.

### Mistake 3: Mixing Sync and Async Fixtures Incorrectly

```python
# WRONG - Async fixture used in sync test
@pytest.fixture
async def async_data():
    return await get_data()

def test_sync_test(async_data):  # async_data is a coroutine here!
    assert async_data["key"] == "value"  # Fails!

# RIGHT - Async test for async fixture
@pytest.fixture
async def async_data():
    return await get_data()

@pytest.mark.asyncio
async def test_async_test(async_data):  # Properly awaited
    assert async_data["key"] == "value"  # Works!
```

Async fixtures must be used in async tests.

### Mistake 4: Not Using yield in Fixtures

```python
# WRONG - Cleanup never runs if test fails
@pytest.fixture
async def resource():
    r = await create_resource()
    # If test fails, this cleanup never runs:
    await cleanup_resource(r)
    return r

# RIGHT - Cleanup always runs
@pytest.fixture
async def resource():
    r = await create_resource()
    yield r  # Test runs here
    await cleanup_resource(r)  # Always runs, even on failure
```

Use `yield` to guarantee cleanup.

---

## Try With AI

### Prompt 1: Debug Event Loop Error

```
My test fails with "Event loop is closed". Here's my test:

@pytest.mark.asyncio
async def test_something():
    await my_async_function()

And my conftest.py has session-scoped fixtures. What's causing this
and how do I fix it?
```

**What you're learning:** Event loop errors are the most common async testing issue. Understanding the relationship between fixture scope and event loop scope is essential.

### Prompt 2: Fixture Scope Decision

```
I have an async database connection. Should this be a function-scoped
or session-scoped fixture? Explain the trade-offs:
- Test isolation
- Test speed
- Resource cleanup
- Potential for test interference
```

**What you're learning:** Fixture scope affects both isolation and speed. Understanding this trade-off helps you design efficient test suites.

### Prompt 3: Convert Sync Tests

```
I have 10 synchronous tests that work. Now my code is async.
What's the minimum change to make them async-compatible?
Walk me through the pattern step by step.
```

**What you're learning:** Migrating existing tests to async is a common task. The pattern is mechanical once you understand it.

---

## Reflect on Your Skill

### Test Your Skill

```
Using my agent-tdd skill, show me how to configure pytest-asyncio.
Does my skill include the pyproject.toml configuration and
event loop fixture pattern?
```

### Identify Gaps

Review your skill's response:
- Does it explain `asyncio_mode = "auto"`?
- Does it include the `asyncio_default_fixture_loop_scope` setting?
- Does it show the session-scoped event loop fixture?
- Does it explain when to use each fixture scope?

### Improve Your Skill

```
My agent-tdd skill needs pytest-asyncio patterns. Add the
pyproject.toml configuration, event loop fixture, async fixture
patterns with yield for cleanup, and common error handling.
```

