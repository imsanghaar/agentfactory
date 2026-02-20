# Chapter 46: TDD for Agents — Task List

**Generated**: 2025-12-30
**Source**: plan.md
**Branch**: 001-ch46-tdd-agents
**Status**: Ready for implementation

---

## Task Overview

| Category | Count | Status |
|----------|-------|--------|
| Lesson Implementation | 9 | Pending |
| Quiz | 1 | Pending |
| README | 1 | Pending |
| Validation | 1 | Pending |
| **Total** | 12 | |

---

## Tasks

### T01: Implement L00 — Build Your Testing Skill
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/00-build-your-testing-skill.md`
**Duration**: 15 min lesson
**Layer**: L1 (Manual Foundation)
**Priority**: P1 (Skill-First pattern requires this first)

**Checklist**:
- [ ] Write YAML frontmatter with skills metadata (B1 proficiency)
- [ ] Document Step 1: Clone skills-lab
- [ ] Write skill creation prompt template
- [ ] Include Done statement connecting to chapter arc
- [ ] Add Next link to L01

**Quality Reference**: Ch34 L00 pattern

---

### T02: Implement L01 — TDD Philosophy for Agents
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/01-tdd-philosophy-for-agents.md`
**Duration**: 20 min lesson
**Layer**: L1 (Manual Foundation)
**Priority**: P1

**Checklist**:
- [ ] Write compelling narrative (the $50 test suite problem)
- [ ] Create TDD vs Evals comparison table
- [ ] Document what TDD tests (code correctness)
- [ ] Document what TDD does NOT test (reasoning quality)
- [ ] Write 3 "Try With AI" prompts with "What you're learning" explanations
- [ ] Write "Reflect on Your Skill" section (Test/Identify Gaps/Improve)

---

### T03: Implement L02 — pytest Fundamentals for Async Code
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/02-pytest-async-fundamentals.md`
**Duration**: 25 min lesson
**Layer**: L1 (Manual Foundation)
**Priority**: P1

**Checklist**:
- [ ] Document project setup with uv (`uv add --dev pytest pytest-asyncio httpx respx pytest-cov`)
- [ ] Write pytest configuration (pyproject.toml asyncio_mode = "auto")
- [ ] Show first async test example
- [ ] Document session-scoped event loop fixture
- [ ] Show async fixtures pattern
- [ ] Create hands-on exercise (3 async tests)
- [ ] Write 3 "Try With AI" prompts
- [ ] Write "Reflect on Your Skill" section

---

### T04: Implement L03 — Testing FastAPI Endpoints
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/03-testing-fastapi-endpoints.md`
**Duration**: 30 min lesson
**Layer**: L2 (AI Collaboration)
**Priority**: P1

**Checklist**:
- [ ] Write opening narrative connecting to Chapter 40 Task API
- [ ] Document httpx AsyncClient with ASGITransport pattern
- [ ] Show dependency override pattern for auth and database
- [ ] Include complete conftest.py template
- [ ] Document Three Roles demonstrations (Teacher/Student/Co-Worker)
- [ ] Show testing all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- [ ] Include error response testing (404, 422, 401)
- [ ] Create hands-on exercise
- [ ] Write 3 "Try With AI" prompts
- [ ] Write "Reflect on Your Skill" section

---

### T05: Implement L04 — Testing SQLModel Operations
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/04-testing-sqlmodel-operations.md`
**Duration**: 25 min lesson
**Layer**: L2 (AI Collaboration)
**Priority**: P1

**Checklist**:
- [ ] Document in-memory SQLite with StaticPool configuration
- [ ] Show database fixture with table creation/teardown
- [ ] Include model test examples (CRUD, relationships)
- [ ] Document cascade delete testing
- [ ] Document constraint violation testing
- [ ] Address SQLite vs PostgreSQL differences (JSONB)
- [ ] Document Three Roles demonstrations
- [ ] Create hands-on exercise
- [ ] Write 3 "Try With AI" prompts
- [ ] Write "Reflect on Your Skill" section

---

### T06: Implement L05 — Mocking LLM Calls
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/05-mocking-llm-calls.md`
**Duration**: 30 min lesson
**Layer**: L2 (AI Collaboration)
**Priority**: P1 (Key differentiator from Evals)

**Checklist**:
- [ ] Write opening narrative about cost savings (zero API calls)
- [ ] Document respx basics (decorator, context manager, fixture)
- [ ] Show OpenAI API response mocking
- [ ] Show tool call response mocking
- [ ] Document error response mocking (429, 500, timeout)
- [ ] Show mock verification (respx.calls.call_count)
- [ ] Include Anthropic API mocking
- [ ] Document Three Roles demonstrations
- [ ] Create hands-on exercise
- [ ] Write 3 "Try With AI" prompts
- [ ] Write "Reflect on Your Skill" section

---

### T07: Implement L06 — Testing Agent Tools
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/06-testing-agent-tools.md`
**Duration**: 25 min lesson
**Layer**: L2/L3 (Collaboration/Skill Design)
**Priority**: P2

**Checklist**:
- [ ] Write opening narrative (isolating tool vs agent failures)
- [ ] Document tool isolation pattern (test function without decorator)
- [ ] Show input validation testing (security focus)
- [ ] Document external dependency mocking in tools
- [ ] Document tool error handling tests
- [ ] Include skill pattern extraction section
- [ ] Create hands-on exercise
- [ ] Write 3 "Try With AI" prompts
- [ ] Write "Reflect on Your Skill" section

---

### T08: Implement L07 — Integration Test Patterns
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/07-integration-test-patterns.md`
**Duration**: 30 min lesson
**Layer**: L3 (Intelligence Design)
**Priority**: P2

**Checklist**:
- [ ] Write opening narrative (unit vs integration testing)
- [ ] Document multi-turn mock sequence (side_effect list)
- [ ] Show database state verification after agent actions
- [ ] Document error handling path testing
- [ ] Include recommended test organization structure
- [ ] Document skill pattern extraction for agent-tdd skill
- [ ] Create hands-on exercise
- [ ] Write 3 "Try With AI" prompts
- [ ] Write "Reflect on Your Skill" section

---

### T09: Implement L08 — Capstone: Full Test Suite
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/08-capstone-task-api-test-suite.md`
**Duration**: 35 min lesson
**Layer**: L4 (Spec-Driven Integration)
**Priority**: P2

**Checklist**:
- [ ] Write opening narrative (compose patterns into production suite)
- [ ] Include test specification template
- [ ] Document test factories pattern
- [ ] Show coverage configuration (pyproject.toml, 80% threshold)
- [ ] Show running with coverage (`pytest --cov`)
- [ ] Include GitHub Actions CI/CD workflow
- [ ] Document complete test suite structure
- [ ] Create verification checklist (coverage, speed, zero API calls)
- [ ] Write 3 "Try With AI" prompts
- [ ] Write final skill reflection (finalize agent-tdd skill)

---

### T10: Create Chapter Quiz
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/quiz.md`
**Priority**: P3

**Checklist**:
- [ ] Write 10 questions covering key concepts
- [ ] Include TDD vs Evals distinction questions (2-3)
- [ ] Include pytest-asyncio pattern questions (2-3)
- [ ] Include respx mocking questions (2-3)
- [ ] Include integration testing questions (2)
- [ ] Provide answer key with explanations

---

### T11: Create Chapter README
**File**: `apps/learn-app/docs/06-AI-Native-Software-Development/46-tdd-for-agents/README.md`
**Priority**: P3

**Checklist**:
- [ ] Write chapter overview
- [ ] Document Skill-First learning arc
- [ ] Create lesson structure table with layers and durations
- [ ] Document prerequisites (Ch40, Part 5)
- [ ] Include "What Students Will Own" section (agent-tdd skill)
- [ ] Add TDD vs Evals distinction summary

---

### T12: Run Validators
**Priority**: P1 (after all lessons complete)

**Checklist**:
- [ ] Run educational-validator on all lessons
- [ ] Run factual-verifier on content with claims
- [ ] Verify Skill-First pattern implemented (L00 creates skill)
- [ ] Verify "Reflect on Your Skill" in every lesson
- [ ] Verify Three Roles invisible in L2 lessons
- [ ] Verify layer progression (L1→L2→L3→L4)
- [ ] Verify cognitive load limits (max 4 new concepts per lesson)

---

## Implementation Order

**Phase 1: Foundation (T01-T03)**
1. T01: L00 — Build Your Testing Skill
2. T02: L01 — TDD Philosophy
3. T03: L02 — pytest Fundamentals

**Phase 2: Core Patterns (T04-T06)**
4. T04: L03 — FastAPI Testing
5. T05: L04 — SQLModel Testing
6. T06: L05 — LLM Mocking

**Phase 3: Advanced & Capstone (T07-T09)**
7. T07: L06 — Tool Testing
8. T08: L07 — Integration Patterns
9. T09: L08 — Capstone

**Phase 4: Polish (T10-T12)**
10. T11: README
11. T10: Quiz
12. T12: Validators

---

## Success Criteria Mapping

| Success Criterion | Verified By |
|-------------------|-------------|
| SC-001: Tests pass in <10s | T09 (Capstone verification) |
| SC-002: 80%+ coverage | T09 (Coverage configuration) |
| SC-003: Write tests in <5 min | T04-T06 (Pattern templates) |
| SC-004: Zero LLM API calls | T06 (respx mocking) |
| SC-005: Reusable agent-tdd skill | T01 (Skill creation) |
| SC-006: CI/CD automation | T09 (GitHub Actions) |
| SC-007: TDD vs Evals distinction | T02 (Comparison table) |
| SC-008: Mock any LLM response | T06 (respx patterns) |
| SC-009: Diagnose test failures | T08 (Error paths) |
| SC-010: Transferable patterns | T09 (Complete suite) |

---

**Ready for implementation**: Yes
**Estimated total time**: 6-8 hours
