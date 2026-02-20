# Feature Specification: Chapter 46 - TDD for Agents

**Feature Branch**: `001-ch46-tdd-agents`
**Created**: 2025-12-30
**Status**: Draft
**Part**: 6 - AI Native Software Development
**Phase**: Quality Assurance (Ch 46-47)
**Proficiency Level**: B1-B2 (Intermediate to Upper-Intermediate)

## Chapter Overview

This chapter teaches Test-Driven Development (TDD) for AI agent applications. Students learn to write tests for agent **code correctness** (deterministic, passes/fails) - not for evaluating LLM reasoning quality (probabilistic, scores - covered in Chapter 47: Evals).

**Critical Distinction**:
- **TDD (This Chapter)**: Does the function return correct output? Does the API handle errors? Does the database maintain integrity?
- **Evals (Chapter 47)**: Does the agent's response make sense? Is the output helpful/accurate/safe?

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Python fundamentals (Part 5)
- Basic pytest usage (Part 5, Ch24 Exception Handling)
- FastAPI endpoint creation (Ch40: FastAPI for Agents)
- SQLModel database operations (Ch40)
- Agent SDK patterns (Ch34-36: OpenAI, Google ADK, Claude Agent SDK)
- MCP server development (Ch38)
- The Task API running example from Chapter 40

**What this chapter explains from scratch**:
- pytest-asyncio for async testing
- httpx AsyncClient with ASGITransport for FastAPI testing
- respx for mocking HTTPX requests (LLM API mocking)
- Dependency injection overrides for testing
- Test fixtures and factories
- Integration testing patterns for agent pipelines
- CI/CD integration for automated testing

## Skill-First Learning Pattern

**Student Skill Name**: `agent-tdd`

Students create their testing skill in L00 BEFORE learning content. Each subsequent lesson tests and improves this skill, producing a production-ready testing asset by chapter end.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Build Testing Skill Foundation (Priority: P1)

A student wants to create a reusable skill for testing AI agent applications. They clone the skills-lab, fetch official pytest-asyncio documentation, and create their `agent-tdd` skill using the skill creator.

**Why this priority**: The Skill-First pattern requires students own their testing skill before learning content. This produces a sellable Digital FTE component.

**Independent Test**: Student can invoke their skill and get correct pytest-asyncio patterns for any testing scenario.

**Acceptance Scenarios**:

1. **Given** student has Claude Code installed, **When** they clone skills-lab and run the skill creation prompt, **Then** they have `.claude/skills/agent-tdd/SKILL.md` with pytest-asyncio patterns
2. **Given** student has created their skill, **When** they ask "How do I test an async function?", **Then** the skill provides correct pytest-asyncio patterns

---

### User Story 2 - Test FastAPI Agent Endpoints (Priority: P1)

A student needs to test their Task API endpoints from Chapter 40. They want to verify CRUD operations, error handling, and query parameters work correctly without hitting real databases or LLM APIs.

**Why this priority**: API testing is foundational - all agent applications expose HTTP endpoints.

**Independent Test**: Student can run `pytest tests/test_api.py` and see all endpoint tests pass with in-memory SQLite.

**Acceptance Scenarios**:

1. **Given** Task API from Ch40, **When** student writes endpoint tests with httpx AsyncClient, **Then** tests run against in-memory SQLite and pass
2. **Given** authenticated endpoints, **When** student overrides auth dependency, **Then** tests can run with mocked authentication
3. **Given** validation rules, **When** student sends invalid data, **Then** tests verify 422 responses with correct error messages

---

### User Story 3 - Mock LLM API Calls (Priority: P1)

A student needs to test agent code that calls OpenAI/Anthropic APIs. They want tests to run fast (no API calls), cost nothing (no token usage), and be deterministic (same input = same output).

**Why this priority**: Mocking LLM calls is the key differentiator between TDD and Evals. Without mocking, tests are slow, expensive, and flaky.

**Independent Test**: Student can run agent tests that complete in milliseconds with zero API calls.

**Acceptance Scenarios**:

1. **Given** agent code that calls OpenAI, **When** student uses respx to mock responses, **Then** tests run without hitting OpenAI servers
2. **Given** agent that parses tool calls, **When** student mocks tool call responses, **Then** tests verify correct parsing logic
3. **Given** agent with error handling, **When** student mocks 429 rate limit response, **Then** tests verify retry/backoff logic

---

### User Story 4 - Test SQLModel Operations (Priority: P2)

A student needs to verify their database models work correctly - relationships, constraints, and cascade behavior.

**Why this priority**: Data integrity is critical but API tests often cover the happy path.

**Independent Test**: Student can test model behavior directly without going through API layer.

**Acceptance Scenarios**:

1. **Given** Task model with relationships, **When** student tests cascade delete, **Then** subtasks are deleted with parent
2. **Given** unique constraint on project slug, **When** student tests duplicate creation, **Then** appropriate error is raised
3. **Given** model with default values, **When** student creates without specifying, **Then** defaults are applied correctly

---

### User Story 5 - Test Agent Tools in Isolation (Priority: P2)

A student has created custom tools for their agent. They want to test tool functions independently before testing the agent orchestration.

**Why this priority**: Tool testing enables faster debugging - issues can be isolated to tool vs orchestration.

**Independent Test**: Student can test each tool function with unit tests before integration testing.

**Acceptance Scenarios**:

1. **Given** database search tool, **When** tested with sample queries, **Then** returns correct results
2. **Given** tool with input validation, **When** tested with malicious input, **Then** validation blocks injection
3. **Given** tool that calls external API, **When** mocked with respx, **Then** tests verify request/response handling

---

### User Story 6 - Integration Test Agent Pipeline (Priority: P2)

A student wants to test the complete agent flow: user message → LLM decides tool → tool executes → LLM responds. All with mocked LLM responses.

**Why this priority**: Integration tests catch issues that unit tests miss - interaction bugs between components.

**Independent Test**: Student can run full pipeline tests that verify end-to-end behavior.

**Acceptance Scenarios**:

1. **Given** complete agent with tools, **When** tested with mocked multi-turn conversation, **Then** correct tool calls are made
2. **Given** agent endpoint, **When** tested with mocked LLM, **Then** database state is updated correctly
3. **Given** agent with error handling, **When** tested with timeout scenario, **Then** graceful degradation occurs

---

### User Story 7 - Comprehensive Task API Test Suite (Priority: P3)

A student wants to create a complete test suite for the Task API that could be used as a template for any agent API project.

**Why this priority**: Capstone that brings together all patterns learned.

**Independent Test**: Student can run `pytest --cov` and see 80%+ coverage with all test types.

**Acceptance Scenarios**:

1. **Given** complete test suite, **When** run with coverage, **Then** achieves 80%+ code coverage
2. **Given** test suite with factories, **When** creating test data, **Then** factories produce valid, isolated data
3. **Given** CI/CD workflow file, **When** pushed to GitHub, **Then** tests run automatically on PR

---

### Edge Cases

- What happens when in-memory SQLite doesn't support JSONB (PostgreSQL-specific)?
- How do tests handle async fixture cleanup on test failure?
- What happens when respx mock doesn't match the exact URL pattern?
- How do tests handle streaming responses from LLM APIs?
- What happens when multiple tests try to access the same fixture concurrently?

## Requirements *(mandatory)*

### Functional Requirements

**Skill-First Pattern (L00)**:
- **FR-001**: Lesson 0 MUST have students create their `agent-tdd` skill before any content
- **FR-002**: Skill creation MUST use `/fetching-library-docs` to get official pytest-asyncio docs
- **FR-003**: Every subsequent lesson MUST end with "Reflect on Your Skill" section

**Testing Setup**:
- **FR-004**: Chapter MUST teach pytest-asyncio configuration with `asyncio_mode = "auto"`
- **FR-005**: Chapter MUST teach session-scoped event loops for shared fixtures
- **FR-006**: Chapter MUST teach in-memory SQLite setup with StaticPool

**FastAPI Testing**:
- **FR-007**: Chapter MUST teach httpx AsyncClient with ASGITransport pattern
- **FR-008**: Chapter MUST teach dependency override pattern for auth and database
- **FR-009**: Chapter MUST teach testing all HTTP methods (GET, POST, PUT, PATCH, DELETE)

**LLM Mocking**:
- **FR-010**: Chapter MUST teach respx for mocking httpx requests
- **FR-011**: Chapter MUST teach mocking OpenAI/Anthropic API response formats
- **FR-012**: Chapter MUST teach mocking tool call responses
- **FR-013**: Chapter MUST teach mocking error responses (429, 500, timeout)

**SQLModel Testing**:
- **FR-014**: Chapter MUST teach model isolation with function-scoped fixtures
- **FR-015**: Chapter MUST teach cascade behavior testing
- **FR-016**: Chapter MUST teach constraint violation testing

**Tool Testing**:
- **FR-017**: Chapter MUST teach isolating tool functions for unit testing
- **FR-018**: Chapter MUST teach mocking external dependencies in tools
- **FR-019**: Chapter MUST teach input validation testing

**Integration Testing**:
- **FR-020**: Chapter MUST teach multi-turn agent conversation testing
- **FR-021**: Chapter MUST teach verifying database state after agent actions
- **FR-022**: Chapter MUST teach testing agent error handling paths

**CI/CD**:
- **FR-023**: Chapter MUST include GitHub Actions workflow for automated testing
- **FR-024**: Chapter MUST teach test coverage reporting

**Boundary with Evals (Chapter 47)**:
- **FR-025**: Chapter MUST NOT teach LLM output quality assessment
- **FR-026**: Chapter MUST NOT teach response faithfulness/relevance scoring
- **FR-027**: Chapter MUST clarify that TDD uses mocked LLM, Evals uses real LLM

### Key Entities

- **Test Fixture**: Reusable test setup (database, client, mock user) that provides consistent state
- **Mock Response**: Predetermined LLM API response used instead of real API calls
- **Test Factory**: Helper function that creates test data with sensible defaults
- **Coverage Report**: Analysis of which code paths are exercised by tests

## Lesson Structure

| Lesson | Title | Layer | Duration | Focus |
|--------|-------|-------|----------|-------|
| L00 | Build Your Testing Skill | L1 (Manual) | 15 min | Create agent-tdd skill from docs |
| L01 | TDD Philosophy for Agent Development | L1 (Manual) | 20 min | Why TDD matters for agents, TDD vs Evals |
| L02 | pytest Fundamentals for Async Code | L1 (Manual) | 25 min | pytest-asyncio, fixtures, event loops |
| L03 | Testing FastAPI Endpoints | L2 (Collaboration) | 30 min | httpx, ASGITransport, dependency overrides |
| L04 | Testing SQLModel Operations | L2 (Collaboration) | 25 min | In-memory SQLite, model tests |
| L05 | Mocking LLM Calls | L2 (Collaboration) | 30 min | respx, mock responses, error scenarios |
| L06 | Testing Agent Tools | L2/L3 (Collaboration/Skill) | 25 min | Tool isolation, integration |
| L07 | Integration Test Patterns | L3 (Skill) | 30 min | Full pipeline testing |
| L08 | Capstone: Full Test Suite | L4 (Spec-Driven) | 35 min | Complete Task API test suite |

**Total Duration**: ~235 minutes (~4 hours)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can run `pytest` on Task API with all tests passing in under 10 seconds
- **SC-002**: Students achieve 80%+ code coverage on their agent API
- **SC-003**: Students can write tests for new endpoints in under 5 minutes using learned patterns
- **SC-004**: Zero LLM API calls are made during test execution
- **SC-005**: Students have a reusable `agent-tdd` skill they own and can improve
- **SC-006**: CI/CD workflow runs tests automatically on every PR

### Learning Validation

- **SC-007**: Students can explain the difference between TDD and Evals
- **SC-008**: Students can mock any LLM API response format
- **SC-009**: Students can diagnose why a test is failing (fixture, mock, assertion)
- **SC-010**: Students can add tests to any existing FastAPI + SQLModel project

## Assumptions

1. Students have completed Chapter 40 and have the Task API codebase available
2. Students have basic pytest knowledge from Part 5
3. Students are using Python 3.11+ (asyncio.timeout available)
4. The running example uses SQLModel with PostgreSQL in production, SQLite for tests
5. Students have uv package manager installed

## Dependencies

- **Chapter 40**: FastAPI for Agents (provides Task API codebase)
- **Part 5**: Python fundamentals (basic pytest exposure)
- **Ch34-36**: Agent SDK patterns (code to test)

## Output Files

```
apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/
├── 00-build-your-testing-skill.md
├── 01-tdd-philosophy-for-agents.md
├── 02-pytest-async-fundamentals.md
├── 03-testing-fastapi-endpoints.md
├── 04-testing-sqlmodel-operations.md
├── 05-mocking-llm-calls.md
├── 06-testing-agent-tools.md
├── 07-integration-test-patterns.md
├── 08-capstone-task-api-test-suite.md
├── quiz.md
└── README.md
```

## References

- Expertise Skill: `.claude/skills/testing-ai-agents/SKILL.md`
- Reference Tests: TaskFlow API tests from research phase
- Quality Reference: Chapter 34 L00 pattern
