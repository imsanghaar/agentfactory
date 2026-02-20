"""Integration tests for GET /api/v1/progress/me."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_progress_empty_user(client: AsyncClient):
    """Brand-new user gets empty progress with zeroed stats."""
    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": "test-progress-empty"},
    )
    assert response.status_code == 200
    data = response.json()

    # User info
    assert data["user"]["display_name"] is not None

    # Stats should all be zero
    stats = data["stats"]
    assert stats["total_xp"] == 0
    assert stats["quizzes_completed"] == 0
    assert stats["perfect_scores"] == 0
    assert stats["current_streak"] == 0
    assert stats["longest_streak"] == 0
    assert stats["lessons_completed"] == 0
    assert stats["badge_count"] == 0

    # No badges or chapters
    assert data["badges"] == []
    assert data["chapters"] == []


@pytest.mark.asyncio
async def test_progress_after_quiz(client: AsyncClient):
    """Progress reflects quiz submission data."""
    user_id = "test-progress-quiz"

    # Submit a quiz first
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 90,
            "questions_correct": 14,
            "questions_total": 15,
            "duration_secs": 300,
        },
        headers={"X-User-ID": user_id},
    )

    # Now check progress
    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    # Stats should reflect the quiz
    stats = data["stats"]
    assert stats["total_xp"] == 90
    assert stats["quizzes_completed"] == 1
    assert stats["current_streak"] >= 1

    # Should have badges (at least first-steps)
    assert len(data["badges"]) >= 1
    badge_ids = [b["id"] for b in data["badges"]]
    assert "first-steps" in badge_ids

    # Should have one chapter
    assert len(data["chapters"]) >= 1
    chapter = data["chapters"][0]
    assert chapter["best_score"] == 90
    assert chapter["attempts"] == 1
    assert chapter["xp_earned"] == 90


@pytest.mark.asyncio
async def test_progress_after_lesson(client: AsyncClient):
    """Progress reflects lesson completion data."""
    user_id = "test-progress-lesson"

    # Complete a lesson
    await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "digital-fte-revolution",
            "active_duration_secs": 480,
        },
        headers={"X-User-ID": user_id},
    )

    # Check progress
    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    stats = data["stats"]
    assert stats["lessons_completed"] == 1
    assert stats["current_streak"] >= 1

    # Chapter should appear with lesson data
    assert len(data["chapters"]) >= 1
    chapter = next(
        (
            c
            for c in data["chapters"]
            if c["slug"] == "General-Agents-Foundations/agent-factory-paradigm"
        ),
        None,
    )
    assert chapter is not None
    assert len(chapter["lessons_completed"]) == 1
    assert chapter["lessons_completed"][0]["lesson_slug"] == "digital-fte-revolution"
    assert chapter["lessons_completed"][0]["active_duration_secs"] == 480


@pytest.mark.asyncio
async def test_progress_combined_quiz_and_lesson(client: AsyncClient):
    """Progress combines quiz and lesson data for same chapter."""
    user_id = "test-progress-combined"
    slug = "General-Agents-Foundations/general-agents"

    # Submit a quiz
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": slug,
            "score_pct": 75,
            "questions_correct": 11,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Complete a lesson in the same chapter
    await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": slug,
            "lesson_slug": "what-are-agents",
            "active_duration_secs": 300,
        },
        headers={"X-User-ID": user_id},
    )

    # Check progress
    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    # Find the chapter
    chapter = next((c for c in data["chapters"] if c["slug"] == slug), None)
    assert chapter is not None
    assert chapter["best_score"] == 75
    assert chapter["attempts"] == 1
    assert len(chapter["lessons_completed"]) == 1


@pytest.mark.asyncio
async def test_progress_multiple_chapters(client: AsyncClient):
    """Progress shows data across multiple chapters."""
    user_id = "test-progress-multi"

    # Quiz in chapter 1
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 80,
            "questions_correct": 12,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Quiz in chapter 2
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/general-agents",
            "score_pct": 95,
            "questions_correct": 14,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Check progress
    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    stats = data["stats"]
    assert stats["total_xp"] == 175  # 80 + 95
    assert stats["quizzes_completed"] == 2
    assert len(data["chapters"]) >= 2


@pytest.mark.asyncio
async def test_progress_requires_auth(client: AsyncClient):
    """Missing auth header returns 401."""
    # Temporarily disable dev mode to test auth
    from progress_api.config import settings

    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        response = await client.get("/api/v1/progress/me")
        assert response.status_code == 401
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_progress_perfect_scores_and_badge_count(client: AsyncClient):
    """Progress dashboard shows perfect_scores and badge_count correctly."""
    user_id = "test-progress-perfects"

    # Submit a perfect quiz
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 100,
            "questions_correct": 15,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    stats = data["stats"]
    assert stats["perfect_scores"] == 1
    # first-steps + perfect-score + ace = 3 badges
    assert stats["badge_count"] == 3
    assert len(data["badges"]) == 3

    badge_ids = [b["id"] for b in data["badges"]]
    assert "first-steps" in badge_ids
    assert "perfect-score" in badge_ids
    assert "ace" in badge_ids


@pytest.mark.asyncio
async def test_progress_lesson_xp_reflected(client: AsyncClient):
    """Lesson XP (from >60s reading) appears in total_xp on progress dashboard."""
    user_id = "test-progress-lesson-xp"

    # Complete a lesson with long reading time (earns 1 XP)
    await client.post(
        "/api/v1/lesson/complete",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "lesson_slug": "long-read",
            "active_duration_secs": 300,
        },
        headers={"X-User-ID": user_id},
    )

    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["stats"]["total_xp"] == 1
    assert data["stats"]["lessons_completed"] == 1


@pytest.mark.asyncio
async def test_progress_rank_fallback_without_view(client: AsyncClient):
    """Rank is calculated via fallback when materialized view is not refreshed."""
    user_id = "test-progress-rank-fallback"

    # Submit a quiz to create user_progress with XP
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 85,
            "questions_correct": 13,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Do NOT refresh the materialized view.
    # The progress service should calculate rank from user_progress directly.

    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    # stats.rank should be an integer (not null) thanks to the fallback
    assert data["stats"]["rank"] is not None
    assert isinstance(data["stats"]["rank"], int)
    assert data["stats"]["rank"] >= 1


@pytest.mark.asyncio
async def test_progress_response_shape(client: AsyncClient):
    """Response contains all expected top-level keys."""
    response = await client.get(
        "/api/v1/progress/me",
        headers={"X-User-ID": "test-progress-shape"},
    )
    assert response.status_code == 200
    data = response.json()

    # Verify top-level keys
    assert "user" in data
    assert "stats" in data
    assert "badges" in data
    assert "chapters" in data

    # Verify user shape
    assert "display_name" in data["user"]
    assert "avatar_url" in data["user"]

    # Verify stats shape
    expected_stat_keys = {
        "total_xp",
        "rank",
        "quizzes_completed",
        "perfect_scores",
        "current_streak",
        "longest_streak",
        "lessons_completed",
        "badge_count",
    }
    assert set(data["stats"].keys()) == expected_stat_keys
