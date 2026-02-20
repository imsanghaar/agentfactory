---
sidebar_position: 10
title: "Chapter Quiz"
---

# Chapter 46 Quiz: TDD for Agents

Test your understanding of Test-Driven Development patterns for AI agent applications. This quiz covers the key concepts from the chapter: distinguishing TDD from Evals, configuring pytest-asyncio, mocking LLM calls with respx, and writing integration tests.

**Target**: 70% (7 out of 10 correct)

---

## Question 1

You need to verify that your agent's authentication endpoint correctly rejects invalid JWT tokens. Which testing approach should you use?

- [ ] A) Evals with real LLM calls to assess response quality
- [ ] B) TDD with mocked responses to test code logic
- [ ] C) Manual testing in production environment
- [ ] D) Evals with human judges scoring the output

<details>
<summary>Answer</summary>

**Correct: B**

JWT token validation is **code correctness**—it either works or it doesn't. This is deterministic behavior that TDD tests perfectly. You mock the authentication flow and verify your code correctly accepts valid tokens and rejects invalid ones. Evals measure LLM reasoning quality, which isn't involved in authentication logic.

</details>

---

## Question 2

Your test suite runs 50 tests, each making real OpenAI API calls. At $0.006 per test and 20 runs per day for 30 days, what is the approximate monthly cost?

- [ ] A) $18
- [ ] B) $180
- [ ] C) $1,800
- [ ] D) $0 because testing is free

<details>
<summary>Answer</summary>

**Correct: B**

The calculation: $0.006 per test x 50 tests = $0.30 per run. $0.30 x 20 runs/day x 30 days = **$180/month**. This is why mocking LLM calls matters—mocked tests cost $0.00 and run in milliseconds instead of seconds. The chapter emphasizes this cost-benefit analysis as a key reason to adopt TDD with mocked responses.

</details>

---

## Question 3

Which aspect should be tested with Evals (not TDD)?

- [ ] A) Database cascade delete removes child records
- [ ] B) Agent interprets ambiguous user requests helpfully
- [ ] C) API endpoint returns 404 for missing resources
- [ ] D) Tool function validates input against injection attacks

<details>

<summary>Answer</summary>

**Correct: B**

Interpreting ambiguous requests requires **LLM reasoning quality assessment**—this is probabilistic, not deterministic. There's no single "correct" answer, and quality varies across runs. This requires Evals with real LLM calls and scoring (0-1 scale). Options A, C, and D are deterministic code correctness tests—they pass or fail based on whether the code logic works correctly. These belong in TDD with mocked responses.

</details>

---

## Question 4

What does `asyncio_mode = "auto"` in `pyproject.toml` configure?

- [ ] A) Enables automatic parallel test execution across CPUs
- [ ] B) Automatically detects async test functions without decorators
- [ ] C) Creates automatic database backups before each test
- [ ] D) Enables automatic retry on test failures

<details>
<summary>Answer</summary>

**Correct: B**

The `asyncio_mode = "auto"` setting tells pytest-asyncio to **automatically detect `async def` test functions** and run them with an event loop. Without this setting (or explicit `@pytest.mark.asyncio` decorators), async tests would fail because pytest wouldn't know to await the coroutines. This is configured in `[tool.pytest.ini_options]` section.

</details>

---

## Question 5

Why is `StaticPool` required when using in-memory SQLite for testing?

- [ ] A) It improves test performance by caching queries
- [ ] B) It prevents the database from being destroyed between connections
- [ ] C) It enables async operations that SQLite normally blocks
- [ ] D) It provides automatic schema migration support

<details>
<summary>Answer</summary>

**Correct: B**

In-memory SQLite databases exist only within a single connection. Without `StaticPool`, each new connection creates a fresh (empty) database, losing all data created in previous connections. `StaticPool` ensures all connections share the same in-memory database, so data persists across transactions within a test. This is configured with `poolclass=StaticPool` in `create_async_engine`.

</details>

---

## Question 6

What is the correct way to mock an OpenAI tool call response with respx?

- [ ] A) `respx.post(...).mock(json={"tool_calls": [...]})`
- [ ] B) `respx.post(...).mock(return_value=httpx.Response(200, json={"choices": [{"message": {"tool_calls": [...]}}]}))`
- [ ] C) `respx.mock_tool_call("create_task", {"title": "Test"})`
- [ ] D) `openai.mock_response(tool_calls=[...])`

<details>
<summary>Answer</summary>

**Correct: B**

respx mocks at the HTTP transport layer, so you must return a complete `httpx.Response` object matching the **exact OpenAI API response structure**. Tool calls are nested inside `choices[0].message.tool_calls`, and `function.arguments` must be a JSON string (not a parsed object). The response also needs `finish_reason: "tool_calls"`. Options A, C, and D don't match how respx or the OpenAI API actually work.

</details>

---

## Question 7

How do you test that an agent correctly handles rate limiting (429 response)?

- [ ] A) Wait for production to hit real rate limits
- [ ] B) Use `respx.post(...).mock(return_value=httpx.Response(429, json={...}))`
- [ ] C) Disable rate limiting in test environment
- [ ] D) Mock the rate limit by setting a low token count

<details>
<summary>Answer</summary>

**Correct: B**

You mock the 429 rate limit response using respx, which lets you simulate the error without making real API calls. The mock should include the error JSON structure and `Retry-After` header that OpenAI returns. This lets you verify your agent's retry logic and error handling. You can also use `side_effect` with a list to test retry behavior: first call returns 429, second call succeeds.

</details>

---

## Question 8

What pattern tests a multi-turn agent conversation (tool call followed by final response)?

- [ ] A) Two separate test functions, one for each turn
- [ ] B) `respx.post(...).mock(side_effect=[response1, response2])`
- [ ] C) `respx.sequence([mock1, mock2])`
- [ ] D) Nested `with respx.mock` context managers

<details>
<summary>Answer</summary>

**Correct: B**

The `side_effect` parameter accepts a **list of responses** that are returned sequentially for each call to the same endpoint. First call gets `response1` (tool call), second call gets `response2` (final message). This mirrors the actual multi-turn flow: user message, LLM decides to call tool, tool executes, LLM responds with result. This pattern is essential for integration testing agent pipelines.

</details>

---

## Question 9

In FastAPI testing, what does `app.dependency_overrides[get_session] = get_test_session` accomplish?

- [ ] A) Permanently replaces production database with test database
- [ ] B) Creates a backup of the session before each test
- [ ] C) Substitutes test implementation for production dependency
- [ ] D) Enables automatic session cleanup after failures

<details>
<summary>Answer</summary>

**Correct: C**

Dependency overrides **substitute test implementations** for production dependencies during testing. When your endpoint calls `get_session`, FastAPI returns `get_test_session` instead—typically an in-memory SQLite session. This isolates tests from production resources. The override is cleared with `app.dependency_overrides.clear()` after tests to prevent pollution between test runs.

</details>

---

## Question 10

When testing an agent's complete pipeline, how do you verify the database was actually modified?

- [ ] A) Trust the agent's response message says it was created
- [ ] B) Query the database directly after the agent action completes
- [ ] C) Check the LLM mock was called with correct arguments
- [ ] D) Verify the HTTP response status code is 200

<details>
<summary>Answer</summary>

**Correct: B**

Integration tests must verify **actual database state**, not just agent responses. After the agent says "I created the task," query the database to confirm the record exists with correct attributes. The pattern is: check state before, execute agent action, check state after. This catches bugs where the agent responds successfully but the database operation actually failed. Status codes and mock verification don't prove data was persisted.

</details>

---

## Scoring Guide

| Score | Assessment |
|-------|------------|
| 10/10 | Excellent - Ready for the capstone project |
| 8-9/10 | Good - Solid understanding of core patterns |
| 7/10 | Pass - Review any missed concepts |
| 5-6/10 | Needs Review - Revisit lessons 1, 3, and 5 |
| Below 5 | Study Required - Re-read the chapter |

## Key Concepts Summary

**TDD vs Evals**: TDD tests code correctness (deterministic, mocked, pass/fail). Evals measure LLM quality (probabilistic, real calls, scores).

**pytest-asyncio**: Configure with `asyncio_mode = "auto"` and use `@pytest.mark.asyncio` for async tests.

**respx mocking**: Mock at HTTP transport layer with exact OpenAI/Anthropic response structures. Use `side_effect` for multi-turn sequences.

**Integration testing**: Verify database state changes, not just agent responses. Test error handling paths with mocked failures.
