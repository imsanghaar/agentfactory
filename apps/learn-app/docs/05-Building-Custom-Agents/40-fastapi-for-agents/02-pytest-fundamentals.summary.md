### Core Concept
Write tests manually before using AI assistance—understand what makes tests useful so you can evaluate AI-generated tests critically. Red-green cycle: write failing test (RED), make it pass (GREEN), refactor. TestClient wraps FastAPI for HTTP testing with assert statements.

### Key Mental Models
- **Test-first mindset**: Testing isn't added later—it's how you verify code works
- **Red-green cycle**: Fail → Pass → Refactor; feel the rhythm before automating
- **Self-contained tests**: Each test independent; create what you need, don't assume state
- **TestClient pattern**: Wraps FastAPI app; `client.get("/")` simulates real HTTP

### Critical Patterns
- Test file: `test_main.py` with `from fastapi.testclient import TestClient`
- Test function: `def test_something():` with assert statements
- POST with JSON: `client.post("/items", json={"name": "Widget"})`
- Error testing: Assert 404, 422 for unhappy paths
- Class grouping: `class TestTaskCreation:` organizes related tests

### AI Collaboration Keys
- Prompt 1: Review your tests—ask AI what edge cases you're missing
- Prompt 2: Understand failures—AI explains what `assert 404 == 200` means
- Prompt 3: Learn fixtures—AI explains pytest patterns for reducing duplication

### Common Mistakes
- Forgetting to import app (`client` undefined)
- Testing `.json()` on 204 responses (no body to parse)
- Tests depending on each other (test_get assumes test_create ran)

### Connections
- **Builds on**: Hello FastAPI (Lesson 1)
- **Leads to**: POST and Pydantic Models (Lesson 3)
