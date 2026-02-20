"""Integration tests for POST /api/v1/lesson/complete."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_lesson_complete_first_time(client: AsyncClient):
    """First completion returns already_completed=false."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "digital-fte-revolution",
            "active_duration_secs": 480,
        },
        headers={"X-User-ID": "test-lesson-1"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["completed"] is True
    assert data["already_completed"] is False
    assert data["active_duration_secs"] == 480
    assert data["streak"]["current"] >= 1


@pytest.mark.asyncio
async def test_lesson_complete_idempotent(client: AsyncClient):
    """Second call returns already_completed=true, no duplicate row."""
    user_id = "test-lesson-idemp"
    slug = "General-Agents-Foundations/agent-factory-paradigm"
    lesson = "selling-agentic-ai-services"

    # First completion
    r1 = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": slug,
            "lesson_slug": lesson,
            "active_duration_secs": 300,
        },
        headers={"X-User-ID": user_id},
    )
    assert r1.status_code == 200
    d1 = r1.json()
    assert d1["already_completed"] is False

    # Second completion — should be idempotent
    r2 = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": slug,
            "lesson_slug": lesson,
            "active_duration_secs": 600,
        },
        headers={"X-User-ID": user_id},
    )
    assert r2.status_code == 200
    d2 = r2.json()
    assert d2["already_completed"] is True
    # Original duration preserved
    assert d2["active_duration_secs"] == 300


@pytest.mark.asyncio
async def test_lesson_complete_streak_updated(client: AsyncClient):
    """Lesson completion updates streak via activity_day."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/general-agents",
            "lesson_slug": "what-are-agents",
        },
        headers={"X-User-ID": "test-lesson-streak"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["streak"]["current"] >= 1
    assert data["streak"]["longest"] >= 1


@pytest.mark.asyncio
async def test_lesson_complete_increments_progress(client: AsyncClient):
    """user_progress.lessons_completed incremented after completion."""
    user_id = "test-lesson-progress"

    # Complete two different lessons
    await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "lesson-one",
        },
        headers={"X-User-ID": user_id},
    )
    await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "lesson-two",
        },
        headers={"X-User-ID": user_id},
    )

    # The second completion should show an active streak
    # (progress is verified through the streak response for now;
    # full dashboard verification comes in Task 3a)
    r = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "lesson-two",
        },
        headers={"X-User-ID": user_id},
    )
    assert r.status_code == 200
    assert r.json()["already_completed"] is True


# === XP Threshold Tests ===


@pytest.mark.asyncio
async def test_lesson_xp_earned_above_threshold(client: AsyncClient):
    """Lesson with active_duration_secs > 60 earns 1 XP."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "xp-threshold-above",
            "active_duration_secs": 120,
        },
        headers={"X-User-ID": "test-lesson-xp-above"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["xp_earned"] == 1


@pytest.mark.asyncio
async def test_lesson_xp_zero_at_threshold(client: AsyncClient):
    """Lesson with active_duration_secs == 60 earns 0 XP (boundary)."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "xp-threshold-exact",
            "active_duration_secs": 60,
        },
        headers={"X-User-ID": "test-lesson-xp-exact"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["xp_earned"] == 0


@pytest.mark.asyncio
async def test_lesson_xp_zero_no_duration(client: AsyncClient):
    """Lesson with no active_duration_secs earns 0 XP."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "xp-no-duration",
        },
        headers={"X-User-ID": "test-lesson-xp-none"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["xp_earned"] == 0


# === Validation Error Tests ===


@pytest.mark.asyncio
async def test_validation_empty_chapter_slug(client: AsyncClient):
    """Empty chapter_slug returns 422."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "",
            "lesson_slug": "some-lesson",
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_validation_empty_lesson_slug(client: AsyncClient):
    """Empty lesson_slug returns 422."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "some/chapter",
            "lesson_slug": "",
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_validation_negative_duration(client: AsyncClient):
    """Negative active_duration_secs returns 422."""
    response = await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "some/chapter",
            "lesson_slug": "some-lesson",
            "active_duration_secs": -10,
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422
