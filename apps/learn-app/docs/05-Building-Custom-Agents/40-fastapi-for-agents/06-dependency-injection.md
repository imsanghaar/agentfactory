---
sidebar_position: 6
title: "Dependency Injection"
description: "Organize shared resources with FastAPI's Depends()—the pattern that powers everything that follows"
keywords: [dependency-injection, depends, fastapi, clean-code, lru-cache]
chapter: 40
lesson: 6
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "Depends() Pattern"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student creates and uses dependency functions"

  - name: "Dependency Caching"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student explains when to use lru_cache vs yield"

  - name: "Resource Cleanup"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student uses yield dependencies for cleanup"

learning_objectives:
  - objective: "Create custom dependency functions"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Dependency provides resource to endpoint"

  - objective: "Use lru_cache for expensive dependencies"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Settings-like dependencies cached correctly"

  - objective: "Implement yield dependencies for cleanup"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Resources properly cleaned up after request"

cognitive_load:
  new_concepts: 3
  assessment: "Depends(), lru_cache, yield dependencies"

differentiation:
  extension_for_advanced: "Create dependency chains and class-based dependencies"
  remedial_for_struggling: "Focus on simple function dependencies before yield"
---

# Dependency Injection

Every endpoint in your API needs shared resources: configuration, connections, services. You could create these inside each function, but that's repetitive and makes testing hard. Dependency injection solves this—FastAPI creates what your endpoint needs and passes it in.

This pattern powers everything in the rest of this chapter. Settings, database sessions, authentication—all use `Depends()`.

## The Problem: Repeated Setup

Without dependency injection:

```python
@app.get("/tasks")
def list_tasks():
    # Setup code repeated in EVERY endpoint
    config = load_config_from_env()
    logger = setup_logger("tasks")
    return {"config": config.app_name}

@app.get("/users")
def list_users():
    # Same setup, repeated again
    config = load_config_from_env()
    logger = setup_logger("users")
    return {"config": config.app_name}
```

Problems:
- Same code in every function
- Hard to test (can't swap config for test config)
- If setup logic changes, you update everywhere

## The Solution: Depends()

With dependency injection:

```python
from fastapi import FastAPI, Depends

app = FastAPI()


def get_config():
    """Provide configuration to endpoints."""
    return {"app_name": "Task API", "version": "1.0"}


@app.get("/tasks")
def list_tasks(config: dict = Depends(get_config)):
    return {"app": config["app_name"]}


@app.get("/users")
def list_users(config: dict = Depends(get_config)):
    return {"app": config["app_name"]}
```

FastAPI:
1. Sees `Depends(get_config)`
2. Calls `get_config()` automatically
3. Passes the result to your function

**Output:**
```json
{"app": "Task API"}
```

## A Dependency Is Just a Function

Any callable works as a dependency:

```python
def get_request_id() -> str:
    """Generate unique ID for this request."""
    import uuid
    return str(uuid.uuid4())


@app.get("/debug")
def debug_info(request_id: str = Depends(get_request_id)):
    return {"request_id": request_id}
```

**Output:**
```json
{"request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"}
```

Each request gets a new UUID. The dependency runs fresh for every request.

## Caching with lru_cache

Some dependencies are expensive—reading config files, creating connections. You want them created once, not per-request:

```python
from functools import lru_cache


@lru_cache
def get_settings():
    """Load settings once, reuse forever."""
    print("Loading settings...")  # Only prints once!
    return {
        "app_name": "Task API",
        "debug": True
    }


@app.get("/info")
def app_info(settings: dict = Depends(get_settings)):
    return {"app": settings["app_name"]}
```

Call `/info` ten times—you'll see "Loading settings..." printed only once.

**When to use `@lru_cache`:**
- Configuration that doesn't change
- Expensive initialization (parsing files, creating clients)
- Anything you'd normally put in a global variable

## Yield Dependencies for Cleanup

Some resources need cleanup—file handles, connections, temporary files. Use `yield` instead of `return`:

```python
def get_temp_file():
    """Provide a temporary file that gets cleaned up."""
    import tempfile
    import os

    # Setup: create the file
    fd, path = tempfile.mkstemp()
    file = os.fdopen(fd, 'w')

    try:
        yield file  # Provide to endpoint
    finally:
        # Cleanup: runs after endpoint completes
        file.close()
        os.unlink(path)


@app.post("/upload")
def process_upload(temp: file = Depends(get_temp_file)):
    temp.write("data")
    return {"status": "processed"}
```

The `finally` block runs after your endpoint finishes—even if it raises an exception. This is how database sessions will work in later lessons.

## Complete Example: Request Logger

Here's a practical dependency that logs every request:

```python
from fastapi import FastAPI, Depends, Request
from datetime import datetime

app = FastAPI()


def get_request_logger(request: Request):
    """Log request details and provide logger to endpoint."""
    start = datetime.now()
    method = request.method
    path = request.url.path

    print(f"[{start}] {method} {path} - started")

    yield {"method": method, "path": path, "start": start}

    end = datetime.now()
    duration = (end - start).total_seconds()
    print(f"[{end}] {method} {path} - completed in {duration:.3f}s")


@app.get("/tasks")
def list_tasks(log: dict = Depends(get_request_logger)):
    return {"tasks": [], "logged_path": log["path"]}


@app.post("/tasks")
def create_task(log: dict = Depends(get_request_logger)):
    return {"id": 1, "logged_method": log["method"]}
```

**Console output:**
```
[2024-01-15 10:30:00] GET /tasks - started
[2024-01-15 10:30:00] GET /tasks - completed in 0.002s
```

Notice how `Request` is also injected—FastAPI provides it automatically.

## Why This Matters

In the next lessons, you'll use `Depends()` for:

| Lesson | Dependency | Purpose |
|--------|------------|---------|
| Environment Variables | `get_settings()` | Configuration from .env |
| SQLModel | `get_session()` | Database connection |
| Authentication | `get_current_user()` | Verify JWT tokens |

Understanding `Depends()` now means these patterns will make sense immediately.

## Hands-On Exercise

Build a simple API with dependencies:

**Step 1:** Create the app with a config dependency:

```python
from fastapi import FastAPI, Depends
from functools import lru_cache

app = FastAPI()


@lru_cache
def get_config():
    return {
        "app_name": "My API",
        "max_items": 100,
        "debug": True
    }


@app.get("/config")
def show_config(config: dict = Depends(get_config)):
    return config
```

**Step 2:** Add a request counter (using a class for state):

```python
class RequestCounter:
    def __init__(self):
        self.count = 0

    def increment(self) -> int:
        self.count += 1
        return self.count


counter = RequestCounter()


def get_request_count() -> int:
    return counter.increment()


@app.get("/count")
def show_count(count: int = Depends(get_request_count)):
    return {"request_number": count}
```

**Step 3:** Test it:

```bash
# First request
curl http://localhost:8000/count
# {"request_number": 1}

# Second request
curl http://localhost:8000/count
# {"request_number": 2}
```

## Common Mistakes

**Mistake 1:** Calling the function instead of passing it

```python
# Wrong - function called at import time!
@app.get("/tasks")
def list_tasks(config = Depends(get_config())):  # () is wrong!
    ...

# Correct - pass the function itself
@app.get("/tasks")
def list_tasks(config = Depends(get_config)):  # No ()
    ...
```

**Mistake 2:** Forgetting to yield in cleanup dependencies

```python
# Wrong - return doesn't allow cleanup code
def get_file():
    f = open("data.txt")
    return f  # File never closed!

# Correct - yield allows cleanup
def get_file():
    f = open("data.txt")
    try:
        yield f
    finally:
        f.close()
```

**Mistake 3:** Caching things that should be fresh

```python
# Wrong - request ID should be different each time!
@lru_cache
def get_request_id():
    return str(uuid.uuid4())

# Correct - no cache for per-request values
def get_request_id():
    return str(uuid.uuid4())
```

## Try With AI

After completing the exercise, explore these patterns.

**Prompt 1: Dependency Chains**

```text
I have a config dependency and want to create a logger dependency
that uses the config. How do dependencies depend on other dependencies?
Show me how to chain get_logger(config = Depends(get_config)).
```

**What you're learning:** Dependencies can depend on other dependencies. FastAPI resolves the chain automatically.

**Prompt 2: Testing Dependencies**

```text
I want to test my endpoints without using the real config.
How do I override a dependency in tests? Show me
app.dependency_overrides and how to use it.
```

**What you're learning:** The power of DI is testability. Override any dependency with a mock for testing.

**Prompt 3: Class Dependencies**

```text
Instead of functions, can I use a class as a dependency?
I want TaskService with methods like list() and create().
Show me how Depends() works with classes.
```

**What you're learning:** Classes with `__init__` parameters work as dependencies. FastAPI resolves the constructor parameters.

---

## Reflect on Your Skill

You built a `fastapi-agent` skill in Lesson 0. Test and improve it based on what you learned.

### Test Your Skill

```
Using my fastapi-agent skill, help me organize code with dependencies.
Does my skill include Depends() patterns, caching, and yield for cleanup?
```

### Identify Gaps

Ask yourself:
- Did my skill include creating custom dependency functions with Depends()?
- Did it explain when to use lru_cache vs fresh per-request?
- Did it cover yield dependencies for resource cleanup?

### Improve Your Skill

If you found gaps:

```
My fastapi-agent skill is missing dependency injection basics.
Update it to include Depends() pattern, lru_cache for configuration,
and yield dependencies for cleanup.
```
