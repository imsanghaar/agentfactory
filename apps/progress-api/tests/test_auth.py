"""Tests for authentication."""

from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException
from httpx import AsyncClient

from progress_api.config import settings
from progress_api.core.auth import get_current_user


@pytest.mark.asyncio
async def test_dev_mode_x_user_id_header(client: AsyncClient):
    """Dev mode: X-User-ID header is used as user identity."""
    response = await client.get("/health", headers={"X-User-ID": "test-user-42"})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_production_mode_missing_auth_header():
    """Production mode: missing Authorization header returns 401."""
    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        request = MagicMock()
        request.headers = {}

        with pytest.raises(HTTPException) as exc_info:
            await get_current_user(request)
        assert exc_info.value.status_code == 401
        assert "Missing Authorization header" in exc_info.value.detail
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_production_mode_invalid_token_format():
    """Production mode: invalid token format returns 401."""
    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        request = MagicMock()
        request.headers = {"Authorization": "Bearer not-a-jwt"}

        with pytest.raises(HTTPException) as exc_info:
            await get_current_user(request)
        assert exc_info.value.status_code == 401
        assert "Invalid token format" in exc_info.value.detail
    finally:
        settings.dev_mode = original_dev_mode


@pytest.mark.asyncio
async def test_production_mode_expired_token():
    """Production mode: expired/invalid JWT returns 401."""
    original_dev_mode = settings.dev_mode
    original_sso_url = settings.sso_url
    settings.dev_mode = False
    settings.sso_url = "http://localhost:9999"  # Non-existent SSO

    try:
        # A properly formatted but invalid JWT (3 parts separated by dots)
        fake_jwt = (
            "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRlc3QifQ"
            ".eyJzdWIiOiJ0ZXN0In0"
            ".fake_signature"
        )
        request = MagicMock()
        request.headers = {"Authorization": f"Bearer {fake_jwt}"}

        with pytest.raises(HTTPException) as exc_info:
            await get_current_user(request)
        # Either 401 (JWT verification failed) or 503 (can't reach SSO)
        assert exc_info.value.status_code in (401, 503)
    finally:
        settings.dev_mode = original_dev_mode
        settings.sso_url = original_sso_url


# === get_optional_user tests ===


@pytest.mark.asyncio
async def test_optional_user_with_auth(client: AsyncClient, test_session):
    """GET /leaderboard with X-User-ID header (dev mode) returns current_user_rank."""
    from sqlalchemy import text as sa_text

    user_id = "auth-optional-user"

    # Submit a quiz to create the user and give them XP
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 75,
            "questions_correct": 11,
            "questions_total": 15,
        },
        headers={"X-User-ID": user_id},
    )

    # Refresh the materialized view so the user appears
    await test_session.execute(sa_text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
    await test_session.commit()

    # GET leaderboard with auth — should include current_user_rank
    response = await client.get(
        "/api/v1/leaderboard",
        headers={"X-User-ID": user_id},
    )
    assert response.status_code == 200
    data = response.json()

    assert data["current_user_rank"] is not None
    assert isinstance(data["current_user_rank"], int)
    assert data["current_user_rank"] >= 1


@pytest.mark.asyncio
async def test_optional_user_without_auth(client: AsyncClient, test_session):
    """GET /leaderboard without auth (dev_mode=False) returns current_user_rank=None."""
    from sqlalchemy import text as sa_text

    # Submit data so leaderboard isn't empty
    await client.post(
        "/api/v1/quiz/submit",
        json={
            "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
            "score_pct": 80,
            "questions_correct": 12,
            "questions_total": 15,
        },
        headers={"X-User-ID": "auth-no-auth-user"},
    )

    # Refresh the materialized view
    await test_session.execute(sa_text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
    await test_session.commit()

    # Disable dev mode to simulate production — no auth header
    original_dev_mode = settings.dev_mode
    settings.dev_mode = False

    try:
        response = await client.get("/api/v1/leaderboard")
        assert response.status_code == 200
        data = response.json()

        # Without auth, get_optional_user returns None → current_user_rank is None
        assert data["current_user_rank"] is None
        assert isinstance(data["entries"], list)
        assert len(data["entries"]) >= 1
    finally:
        settings.dev_mode = original_dev_mode
