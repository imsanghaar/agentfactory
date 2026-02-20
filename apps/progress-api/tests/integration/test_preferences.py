"""Integration tests for PATCH /api/v1/progress/me/preferences."""

import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def _ensure_user_exists(client: AsyncClient, user_id: str) -> None:
    """Helper: create a user by submitting a quiz."""
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 50,
            "questions_correct": 8,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )


@pytest.mark.asyncio
async def test_preferences_toggle_off(client: AsyncClient, test_session: AsyncSession):
    """User can opt out of leaderboard."""
    user_id = "test-pref-off"
    await _ensure_user_exists(client, user_id)

    response = await client.patch(
        "/api/v1/progress/me/preferences",
        json={"show_on_leaderboard": False},
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["show_on_leaderboard"] is False

    # Verify in database
    result = await test_session.execute(
        text("SELECT show_on_leaderboard FROM users WHERE id = :uid"),
        {"uid": user_id},
    )
    row = result.first()
    assert row is not None
    assert row.show_on_leaderboard is False


@pytest.mark.asyncio
async def test_preferences_toggle_on(client: AsyncClient, test_session: AsyncSession):
    """User can opt back into leaderboard."""
    user_id = "test-pref-on"
    await _ensure_user_exists(client, user_id)

    # Opt out first
    await client.patch(
        "/api/v1/progress/me/preferences",
        json={"show_on_leaderboard": False},
        headers={"X-User-ID": user_id},
    )

    # Opt back in
    response = await client.patch(
        "/api/v1/progress/me/preferences",
        json={"show_on_leaderboard": True},
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["show_on_leaderboard"] is True

    # Verify in database
    result = await test_session.execute(
        text("SELECT show_on_leaderboard FROM users WHERE id = :uid"),
        {"uid": user_id},
    )
    row = result.first()
    assert row is not None
    assert row.show_on_leaderboard is True


@pytest.mark.asyncio
async def test_preferences_new_user(client: AsyncClient):
    """Preferences work for a brand-new user (upsert)."""
    response = await client.patch(
        "/api/v1/progress/me/preferences",
        json={"show_on_leaderboard": False},
        headers={"X-User-ID": "test-pref-new"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["show_on_leaderboard"] is False


@pytest.mark.asyncio
async def test_preferences_requires_auth(client: AsyncClient):
    """Missing auth header returns 401."""
    from progress_api.config import settings

    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        response = await client.patch(
            "/api/v1/progress/me/preferences",
            json={"show_on_leaderboard": False},
        )
        assert response.status_code == 401
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_preferences_leaderboard_exclusion(client: AsyncClient, test_session: AsyncSession):
    """Opted-out user excluded from leaderboard after view refresh."""
    user_id = "test-pref-exclude"
    await _ensure_user_exists(client, user_id)

    # Opt out
    await client.patch(
        "/api/v1/progress/me/preferences",
        json={"show_on_leaderboard": False},
        headers={"X-User-ID": user_id},
    )

    # Refresh materialized view
    await test_session.execute(text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
    await test_session.commit()

    # Check leaderboard
    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    user_ids = [e["user_id"] for e in data["entries"]]
    assert user_id not in user_ids
