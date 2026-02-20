"""Integration tests for POST /api/v1/quiz/submit."""

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_quiz_submit_happy_path(client: AsyncClient):
    """First quiz submit returns XP, badges, and streak."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 85,
            "questions_correct": 13,
            "questions_total": 15,
            "duration_secs": 420,
        },
        headers={"X-User-ID": "test-user-1"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["xp_earned"] == 85
    assert data["total_xp"] == 85
    assert data["attempt_number"] == 1
    assert data["best_score"] == 85
    assert data["streak"]["current"] >= 1

    # Should earn first-steps badge
    badge_ids = [b["id"] for b in data["new_badges"]]
    assert "first-steps" in badge_ids


@pytest.mark.asyncio
async def test_quiz_submit_perfect_score(client: AsyncClient):
    """100% score awards perfect-score and ace badges."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/general-agents",
            "score_pct": 100,
            "questions_correct": 15,
            "questions_total": 15,
        },
        headers={"X-User-ID": "test-user-2"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["xp_earned"] == 100
    assert data["attempt_number"] == 1
    assert data["best_score"] == 100

    badge_ids = [b["id"] for b in data["new_badges"]]
    assert "perfect-score" in badge_ids
    assert "ace" in badge_ids
    assert "first-steps" in badge_ids


@pytest.mark.asyncio
async def test_quiz_reattempt_diminished_xp(client: AsyncClient):
    """Second attempt earns diminished XP based on improvement."""
    user_id = "test-user-reattempt"
    slug = "General-Agents-Foundations/seven-principles"

    # First attempt: 60%
    r1 = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": slug,
            "score_pct": 60,
            "questions_correct": 9,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )
    assert r1.status_code == 200
    d1 = r1.json()
    assert d1["xp_earned"] == 60
    assert d1["attempt_number"] == 1

    # Second attempt: 80% (improvement of 20 * 0.5 = 10 XP)
    r2 = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": slug,
            "score_pct": 80,
            "questions_correct": 12,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )
    assert r2.status_code == 200
    d2 = r2.json()
    assert d2["xp_earned"] == 10  # (80-60) * 0.5
    assert d2["attempt_number"] == 2
    assert d2["best_score"] == 80
    assert d2["total_xp"] == 70  # 60 + 10


@pytest.mark.asyncio
async def test_quiz_reattempt_no_improvement_zero_xp(client: AsyncClient):
    """Reattempt with lower score earns 0 XP."""
    user_id = "test-user-no-improve"
    slug = "General-Agents-Foundations/agent-factory-paradigm"

    # First attempt: 90%
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": slug,
            "score_pct": 90,
            "questions_correct": 14,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Second attempt: 70% (no improvement)
    r2 = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": slug,
            "score_pct": 70,
            "questions_correct": 11,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )
    assert r2.status_code == 200
    d2 = r2.json()
    assert d2["xp_earned"] == 0
    assert d2["attempt_number"] == 2
    assert d2["best_score"] == 90  # best is still 90


@pytest.mark.asyncio
async def test_badge_idempotency(client: AsyncClient):
    """Same badge is not awarded twice."""
    user_id = "test-user-badge-idemp"

    # First quiz: gets first-steps badge
    r1 = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 50,
            "questions_correct": 8,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )
    d1 = r1.json()
    assert "first-steps" in [b["id"] for b in d1["new_badges"]]

    # Second quiz (different chapter): should NOT get first-steps again
    r2 = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/general-agents",
            "score_pct": 50,
            "questions_correct": 8,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )
    d2 = r2.json()
    assert "first-steps" not in [b["id"] for b in d2["new_badges"]]


# === Streak Badge Tests ===


@pytest.mark.asyncio
async def test_quiz_streak_badge_on_fire(client: AsyncClient, test_session: AsyncSession):
    """3-day streak awards the on-fire badge."""
    user_id = "test-user-streak-badge"
    from datetime import date, timedelta

    today = date.today()

    # First: submit a quiz to create the user + chapter via API
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 70,
            "questions_correct": 11,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Seed activity_days for the previous 2 days (simulating past activity)
    for days_ago in [2, 1]:
        past_date = today - timedelta(days=days_ago)
        await test_session.execute(
            text(
                "INSERT INTO activity_days (user_id, activity_date, activity_type, reference_id)"
                " VALUES (:uid, :dt, 'quiz', 'seed')"
                " ON CONFLICT DO NOTHING"
            ),
            {"uid": user_id, "dt": past_date},
        )
    await test_session.commit()

    # Now submit another quiz — today is the 3rd consecutive day
    r2 = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/general-agents",
            "score_pct": 75,
            "questions_correct": 11,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )
    assert r2.status_code == 200
    d2 = r2.json()

    badge_ids = [b["id"] for b in d2["new_badges"]]
    assert "on-fire" in badge_ids
    assert d2["streak"]["current"] >= 3


# === Concurrent Submission Tests ===


@pytest.mark.asyncio
async def test_concurrent_quiz_submissions(client: AsyncClient):
    """Concurrent quiz submissions both succeed without crashing."""
    import asyncio

    user_id = "test-user-concurrent"
    slug = "General-Agents-Foundations/agent-factory-paradigm"

    # Fire two concurrent submissions
    async def submit():
        return await client.post(
            "/api/v1/quiz/submit",
            json={
                "chapter_slug": slug,
                "score_pct": 80,
                "questions_correct": 12,
                "questions_total": 15,
            },
            headers={"X-User-ID": user_id},
        )

    r1, r2 = await asyncio.gather(submit(), submit())

    # Both should succeed (200) — no crashes or 500s
    assert r1.status_code == 200
    assert r2.status_code == 200

    # Total XP should reflect both submissions
    d1 = r1.json()
    d2 = r2.json()
    total_xp_values = sorted([d1["total_xp"], d2["total_xp"]])
    # At least one should have 80 XP (first attempt), and the later total
    # should be >= 80 (the second sees 0 improvement → 0 XP, so still 80)
    assert total_xp_values[-1] >= 80


# === Validation Error Tests (T3) ===


@pytest.mark.asyncio
async def test_validation_score_pct_too_high(client: AsyncClient):
    """score_pct > 100 returns 422."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "test/chapter",
            "score_pct": 101,
            "questions_correct": 16,
            "questions_total": 15,
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_validation_score_pct_negative(client: AsyncClient):
    """score_pct < 0 returns 422."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "test/chapter",
            "score_pct": -1,
            "questions_correct": 0,
            "questions_total": 15,
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_validation_empty_chapter_slug(client: AsyncClient):
    """Empty chapter_slug returns 422."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "",
            "score_pct": 85,
            "questions_correct": 13,
            "questions_total": 15,
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_validation_questions_total_zero(client: AsyncClient):
    """questions_total = 0 returns 422."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "test/chapter",
            "score_pct": 85,
            "questions_correct": 0,
            "questions_total": 0,
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_validation_negative_duration(client: AsyncClient):
    """Negative duration_secs returns 422."""
    response = await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "test/chapter",
            "score_pct": 85,
            "questions_correct": 13,
            "questions_total": 15,
            "duration_secs": -10,
        },
        headers={"X-User-ID": "test-user"},
    )
    assert response.status_code == 422
