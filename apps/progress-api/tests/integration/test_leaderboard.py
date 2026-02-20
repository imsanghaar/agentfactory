"""Integration tests for GET /api/v1/leaderboard."""


import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def _submit_quiz(client: AsyncClient, user_id: str, score: int) -> None:
    """Helper: submit a quiz for a given user."""
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": score,
            "questions_correct": int(score * 15 / 100),
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )


async def _refresh_view(test_session: AsyncSession) -> None:
    """Helper: refresh leaderboard materialized view."""
    await test_session.execute(text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
    await test_session.commit()


@pytest.mark.asyncio
async def test_leaderboard_empty(client: AsyncClient, test_session: AsyncSession):
    """Empty leaderboard returns empty entries list."""
    # Refresh view so it reflects current (empty) state
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "test-lb-empty"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["entries"] == []
    assert data["current_user_rank"] is None
    assert data["total_users"] == 0


@pytest.mark.asyncio
async def test_leaderboard_ranked_by_xp(client: AsyncClient, test_session: AsyncSession):
    """Users ranked by total XP descending."""
    # Create users with different scores
    await _submit_quiz(client, "lb-user-low", 50)
    await _submit_quiz(client, "lb-user-mid", 75)
    await _submit_quiz(client, "lb-user-high", 95)

    # Refresh materialized view
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-user-mid"},
    )
    assert response.status_code == 200
    data = response.json()

    assert len(data["entries"]) == 3
    # Verify ordering: highest XP first
    assert data["entries"][0]["total_xp"] >= data["entries"][1]["total_xp"]
    assert data["entries"][1]["total_xp"] >= data["entries"][2]["total_xp"]

    # Verify rank values
    assert data["entries"][0]["rank"] == 1
    assert data["entries"][0]["user_id"] == "lb-user-high"


@pytest.mark.asyncio
async def test_leaderboard_current_user_rank(client: AsyncClient, test_session: AsyncSession):
    """Current user's rank is included in response."""
    await _submit_quiz(client, "lb-rank-1", 90)
    await _submit_quiz(client, "lb-rank-2", 60)
    await _refresh_view(test_session)

    # Request as the lower-ranked user
    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-rank-2"},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["current_user_rank"] == 2


@pytest.mark.asyncio
async def test_leaderboard_excludes_opted_out_user(client: AsyncClient, test_session: AsyncSession):
    """User with show_on_leaderboard=False is excluded."""
    # Create a user who opts out
    await _submit_quiz(client, "lb-opted-out", 80)
    await _submit_quiz(client, "lb-visible", 70)

    # Opt out the user directly in the database
    await test_session.execute(
        text("UPDATE users SET show_on_leaderboard = FALSE WHERE id = :uid"),
        {"uid": "lb-opted-out"},
    )
    await test_session.commit()

    # Refresh materialized view
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-visible"},
    )
    assert response.status_code == 200
    data = response.json()

    user_ids = [e["user_id"] for e in data["entries"]]
    assert "lb-opted-out" not in user_ids
    assert "lb-visible" in user_ids


@pytest.mark.asyncio
async def test_leaderboard_response_shape(client: AsyncClient, test_session: AsyncSession):
    """Response has correct structure."""
    await _submit_quiz(client, "lb-shape-user", 85)
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-shape-user"},
    )
    assert response.status_code == 200
    data = response.json()

    assert "entries" in data
    assert "current_user_rank" in data
    assert "total_users" in data

    entry = data["entries"][0]
    assert "rank" in entry
    assert "user_id" in entry
    assert "display_name" in entry
    assert "avatar_url" in entry
    assert "total_xp" in entry
    assert "badge_count" in entry


@pytest.mark.asyncio
async def test_leaderboard_public_access(client: AsyncClient, test_session: AsyncSession):
    """Leaderboard is publicly accessible without auth."""
    from progress_api.config import settings

    # Submit some data so leaderboard has entries
    await _submit_quiz(client, "lb-public-user", 80)
    await _refresh_view(test_session)

    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        response = await client.get("/api/v1/leaderboard")
        assert response.status_code == 200
        data = response.json()
        # Without auth, current_user_rank should be null
        assert data["current_user_rank"] is None
        assert isinstance(data["entries"], list)
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_leaderboard_lazy_refresh(client: AsyncClient, test_session: AsyncSession):
    """Lazy refresh populates leaderboard when view is empty but data exists."""
    # Submit a quiz — this creates user + user_progress with XP
    await _submit_quiz(client, "lb-lazy-user", 80)

    # Do NOT manually refresh the materialized view.
    # The service's lazy refresh should detect that user_progress has data
    # and refresh the view automatically.

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-lazy-user"},
    )
    assert response.status_code == 200
    data = response.json()

    # Leaderboard should have at least the one user (via lazy refresh or live fallback)
    assert len(data["entries"]) >= 1
    assert data["total_users"] >= 1

    # The user should appear in the entries
    user_ids = [e["user_id"] for e in data["entries"]]
    assert "lb-lazy-user" in user_ids


@pytest.mark.asyncio
async def test_leaderboard_rank_fallback(client: AsyncClient, test_session: AsyncSession):
    """Current user rank is calculated via fallback when view is not refreshed."""
    # Submit a quiz to create data without refreshing the view
    await _submit_quiz(client, "lb-rank-fallback", 70)

    # Do NOT refresh the materialized view — rely on fallback rank calculation.

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-rank-fallback"},
    )
    assert response.status_code == 200
    data = response.json()

    # current_user_rank should not be None — the fallback should calculate it
    assert data["current_user_rank"] is not None
    assert isinstance(data["current_user_rank"], int)
    assert data["current_user_rank"] >= 1


@pytest.mark.asyncio
async def test_leaderboard_top_n_cap(client: AsyncClient, test_session: AsyncSession):
    """Leaderboard returns at most 100 entries even with more users."""
    # Seed 105 users directly in the DB (much faster than 105 API calls)
    for i in range(105):
        uid = f"lb-cap-user-{i:03d}"
        xp = 1000 - i  # descending XP so ranks are deterministic
        await test_session.execute(
            text(
                "INSERT INTO users (id, display_name)"
                " VALUES (:uid, :name)"
                " ON CONFLICT DO NOTHING"
            ),
            {"uid": uid, "name": f"User {i}"},
        )
        await test_session.execute(
            text(
                "INSERT INTO user_progress (user_id, total_xp)"
                " VALUES (:uid, :xp)"
                " ON CONFLICT (user_id) DO UPDATE SET total_xp = :xp"
            ),
            {"uid": uid, "xp": xp},
        )
    await test_session.commit()

    # Refresh view so it picks up the seeded data
    await _refresh_view(test_session)

    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-cap-user-050"},
    )
    assert response.status_code == 200
    data = response.json()

    # Should be capped at 100
    assert len(data["entries"]) == 100
    # The user at index 50 is within top 100, so rank is in entries
    assert data["current_user_rank"] is not None


@pytest.mark.asyncio
async def test_leaderboard_user_rank_beyond_top_n(
    client: AsyncClient, test_session: AsyncSession
):
    """User outside top 100 still gets their rank via fallback."""
    # Seed 105 users
    for i in range(105):
        uid = f"lb-beyond-user-{i:03d}"
        xp = 2000 - i
        await test_session.execute(
            text(
                "INSERT INTO users (id, display_name)"
                " VALUES (:uid, :name)"
                " ON CONFLICT DO NOTHING"
            ),
            {"uid": uid, "name": f"User {i}"},
        )
        await test_session.execute(
            text(
                "INSERT INTO user_progress (user_id, total_xp)"
                " VALUES (:uid, :xp)"
                " ON CONFLICT (user_id) DO UPDATE SET total_xp = :xp"
            ),
            {"uid": uid, "xp": xp},
        )
    await test_session.commit()
    await _refresh_view(test_session)

    # Request as the last user (rank 105, outside top 100)
    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-beyond-user-104"},
    )
    assert response.status_code == 200
    data = response.json()

    assert len(data["entries"]) == 100
    # User 104 is NOT in the top 100 but should still get a rank via fallback
    assert data["current_user_rank"] is not None
    assert data["current_user_rank"] > 100


@pytest.mark.asyncio
async def test_preferences_opt_out_reflected_in_leaderboard(
    client: AsyncClient, test_session: AsyncSession
):
    """Opting out of leaderboard removes user from next leaderboard fetch."""
    # Create two users with XP
    await _submit_quiz(client, "lb-opt-stays", 90)
    await _submit_quiz(client, "lb-opt-leaves", 80)
    await _refresh_view(test_session)

    # Verify both appear
    r1 = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-opt-stays"},
    )
    user_ids_before = [e["user_id"] for e in r1.json()["entries"]]
    assert "lb-opt-leaves" in user_ids_before

    # User opts out
    await client.patch(
        "/api/v1/progress/me/preferences",
        json={"show_on_leaderboard": False},
        headers={"X-User-ID": "lb-opt-leaves"},
    )

    # Refresh view to reflect the opt-out
    await _refresh_view(test_session)

    # Verify the opted-out user is gone
    r2 = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": "lb-opt-stays"},
    )
    user_ids_after = [e["user_id"] for e in r2.json()["entries"]]
    assert "lb-opt-leaves" not in user_ids_after
    assert "lb-opt-stays" in user_ids_after
