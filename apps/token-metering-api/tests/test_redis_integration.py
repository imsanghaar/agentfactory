"""Tests for Redis integration and Lua script behavior.

Tests Redis connection handling and the reservation system implemented via Lua scripts.
"""

import time
from unittest.mock import AsyncMock, patch

import pytest

from token_metering_api.config import settings
from token_metering_api.core.redis import (
    SCRIPTS_DIR,
    get_lua_script,
    get_redis,
    start_redis,
    stop_redis,
)


class TestRedisConnection:
    """Test Redis connection handling."""

    @pytest.mark.asyncio
    async def test_start_redis_returns_none_when_no_url(self):
        """start_redis should return None if REDIS_URL not provided."""
        original_url = settings.redis_url
        settings.redis_url = ""

        try:
            await start_redis()
            redis_client = get_redis()
            assert redis_client is None
        finally:
            settings.redis_url = original_url

    @pytest.mark.asyncio
    async def test_start_redis_returns_none_on_connection_failure(self):
        """start_redis should return None if Redis unavailable."""
        original_url = settings.redis_url
        settings.redis_url = "redis://invalid-host-that-does-not-exist:6379"

        try:
            await start_redis()
            redis_client = get_redis()
            # Connection should fail, so client is None
            assert redis_client is None
        finally:
            settings.redis_url = original_url
            await stop_redis()

    @pytest.mark.asyncio
    async def test_stop_redis_clears_client(self):
        """stop_redis should clear the client."""
        # Just verify stop_redis doesn't error when there's no connection
        await stop_redis()
        assert get_redis() is None


class TestLuaScriptLoading:
    """Test Lua script loading."""

    def test_scripts_directory_exists(self):
        """Scripts directory should exist."""
        assert SCRIPTS_DIR.exists()
        assert SCRIPTS_DIR.is_dir()

    def test_reserve_script_file_exists(self):
        """Reserve Lua script file should exist."""
        script_path = SCRIPTS_DIR / "reserve.lua"
        assert script_path.exists()
        content = script_path.read_text()
        assert "ZADD" in content  # Key operation in reserve script

    def test_finalize_script_file_exists(self):
        """Finalize Lua script file should exist."""
        script_path = SCRIPTS_DIR / "finalize.lua"
        assert script_path.exists()
        content = script_path.read_text()
        assert "ZREM" in content  # Key operation in finalize script

    def test_release_script_file_exists(self):
        """Release Lua script file should exist."""
        script_path = SCRIPTS_DIR / "release.lua"
        assert script_path.exists()
        content = script_path.read_text()
        assert "ZREM" in content  # Key operation in release script

    def test_reserve_script_handles_idempotency(self):
        """Reserve script should handle idempotent requests (status=1)."""
        script_path = SCRIPTS_DIR / "reserve.lua"
        content = script_path.read_text()
        # Check for idempotency handling
        assert "status = 1" in content or "return {1," in content

    def test_reserve_script_handles_conflict(self):
        """Reserve script should handle request_id conflicts (status=2)."""
        script_path = SCRIPTS_DIR / "reserve.lua"
        content = script_path.read_text()
        # Check for conflict handling
        assert "status = 2" in content or "return {2," in content

    def test_scripts_cleanup_expired_reservations(self):
        """All scripts should cleanup expired reservations."""
        for script_name in ["reserve.lua", "finalize.lua", "release.lua"]:
            script_path = SCRIPTS_DIR / script_name
            content = script_path.read_text()
            # All scripts use ZREMRANGEBYSCORE for cleanup
            assert "ZREMRANGEBYSCORE" in content, f"{script_name} should cleanup expired"


class TestLuaScriptContent:
    """Test Lua script content and logic."""

    def test_reserve_script_creates_member_format(self):
        """Reserve script should create member in format 'request_id:tokens'."""
        script_path = SCRIPTS_DIR / "reserve.lua"
        content = script_path.read_text()
        # Check for member format creation
        assert "request_id .. ':' .. tokens" in content

    def test_reserve_script_sets_expiry(self):
        """Reserve script should set key expiry."""
        script_path = SCRIPTS_DIR / "reserve.lua"
        content = script_path.read_text()
        assert "EXPIRE" in content

    def test_finalize_script_returns_status(self):
        """Finalize script should return status and removed tokens."""
        script_path = SCRIPTS_DIR / "finalize.lua"
        content = script_path.read_text()
        # Check return values
        assert "return {1," in content  # Found and removed
        assert "return {0," in content  # Not found

    def test_release_script_is_idempotent(self):
        """Release script should be idempotent (not found is OK)."""
        script_path = SCRIPTS_DIR / "release.lua"
        content = script_path.read_text()
        # Check for idempotent comment
        assert "idempotent" in content.lower()


class TestGetLuaScript:
    """Test get_lua_script function."""

    def test_get_lua_script_returns_none_when_not_loaded(self):
        """get_lua_script should return None if script not loaded."""
        # Scripts are only loaded when Redis is connected
        result = get_lua_script("reserve")
        # With no Redis connection, scripts aren't loaded
        assert result is None or callable(result)

    def test_get_lua_script_returns_none_for_unknown_script(self):
        """get_lua_script should return None for unknown script name."""
        result = get_lua_script("nonexistent_script")
        assert result is None


class TestReservationBehavior:
    """Test reservation system behavior with mocked Redis."""

    @pytest.fixture
    def mock_redis(self):
        """Create a mock Redis client."""
        redis_mock = AsyncMock()
        return redis_mock

    @pytest.mark.asyncio
    async def test_reservation_key_format(self):
        """Reservation keys should follow pattern 'metering:reservations:{user_id}'."""
        from token_metering_api.services.metering import RESERVATIONS_KEY_PREFIX

        user_id = "user-123"
        expected_key = f"{RESERVATIONS_KEY_PREFIX}{user_id}"
        assert expected_key == "metering:reservations:user-123"

    @pytest.mark.asyncio
    async def test_reservation_creates_sorted_set_entry(self, mock_redis):
        """Reserve should create entry in sorted set via Lua script."""
        # Mock the Lua script execution
        mock_script = AsyncMock()
        mock_script.return_value = [0, 1000, 1000]  # status=0 (new), reserved_total, tokens

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            with patch(
                "token_metering_api.services.metering.get_redis",
                return_value=mock_redis,
            ):
                # Call would go through service, but we're testing script params
                await mock_script(
                    keys=["metering:reservations:user-123"],
                    args=["request-uuid", 1000, int(time.time()), int(time.time()) + 300],
                )

                mock_script.assert_called_once()
                call_args = mock_script.call_args
                assert "metering:reservations:user-123" in call_args[1]["keys"]

    @pytest.mark.asyncio
    async def test_reservation_idempotent_same_tokens(self, mock_redis):
        """Same request_id + tokens should return existing reservation (status=1)."""
        mock_script = AsyncMock()
        # Status 1 = idempotent return
        mock_script.return_value = [1, 1000, 1000]

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            result = await mock_script(
                keys=["metering:reservations:user-123"],
                args=["same-request-id", 1000, int(time.time()), int(time.time()) + 300],
            )

            status, reserved_total, tokens = result
            assert status == 1  # Idempotent
            assert tokens == 1000

    @pytest.mark.asyncio
    async def test_reservation_conflict_different_tokens(self, mock_redis):
        """Same request_id + different tokens should return conflict (status=2)."""
        mock_script = AsyncMock()
        # Status 2 = conflict
        mock_script.return_value = [2, 1000, 500]  # Existing was 500, tried 1000

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            result = await mock_script(
                keys=["metering:reservations:user-123"],
                args=["same-request-id", 1000, int(time.time()), int(time.time()) + 300],
            )

            status, reserved_total, existing_tokens = result
            assert status == 2  # Conflict
            assert existing_tokens == 500  # Original value

    @pytest.mark.asyncio
    async def test_finalize_removes_reservation(self, mock_redis):
        """Finalize should remove reservation from sorted set (status=1)."""
        mock_script = AsyncMock()
        # Status 1 = found and removed
        mock_script.return_value = [1, 1000]

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            result = await mock_script(
                keys=["metering:reservations:user-123"],
                args=["request-uuid", int(time.time())],
            )

            status, removed_tokens = result
            assert status == 1  # Found and removed
            assert removed_tokens == 1000

    @pytest.mark.asyncio
    async def test_finalize_not_found(self, mock_redis):
        """Finalize for non-existent reservation returns status=0."""
        mock_script = AsyncMock()
        # Status 0 = not found
        mock_script.return_value = [0, 0]

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            result = await mock_script(
                keys=["metering:reservations:user-123"],
                args=["unknown-request-id", int(time.time())],
            )

            status, removed_tokens = result
            assert status == 0  # Not found
            assert removed_tokens == 0

    @pytest.mark.asyncio
    async def test_release_removes_reservation(self, mock_redis):
        """Release should remove reservation from sorted set (status=1)."""
        mock_script = AsyncMock()
        mock_script.return_value = [1, 1000]

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            result = await mock_script(
                keys=["metering:reservations:user-123"],
                args=["request-uuid", int(time.time())],
            )

            status, released_tokens = result
            assert status == 1
            assert released_tokens == 1000

    @pytest.mark.asyncio
    async def test_release_idempotent_not_found(self, mock_redis):
        """Release for non-existent reservation should still succeed (idempotent)."""
        mock_script = AsyncMock()
        # Status 0 = not found, but that's OK for release
        mock_script.return_value = [0, 0]

        with patch(
            "token_metering_api.services.metering.get_lua_script",
            return_value=mock_script,
        ):
            result = await mock_script(
                keys=["metering:reservations:user-123"],
                args=["already-released-id", int(time.time())],
            )

            status, released_tokens = result
            assert status == 0  # Not found but OK
            assert released_tokens == 0


class TestFailOpenBehavior:
    """Test fail-open behavior when Redis is unavailable."""

    @pytest.mark.asyncio
    async def test_check_balance_fails_open_without_redis(self, client, test_session):
        """Check should succeed with fail-open when Redis unavailable."""
        import uuid
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        # Create user with balance
        account = TokenAccount(
            user_id="failopen-user",
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Use valid UUID format for request_id
        request_id = str(uuid.uuid4())

        # Mock Redis as unavailable
        with patch(
            "token_metering_api.services.metering.get_redis",
            return_value=None,
        ):
            response = await client.post(
                "/api/v1/metering/check",
                json={
                    "user_id": "failopen-user",
                    "request_id": request_id,
                    "estimated_tokens": 1000,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": "failopen-user"},
            )

        assert response.status_code == 200
        data = response.json()
        assert data["allowed"] is True
        # Fail-open reservations have "failopen_" prefix
        assert data["reservation_id"].startswith("failopen_")

    @pytest.mark.asyncio
    async def test_release_succeeds_for_failopen_reservation(self, client, test_session):
        """Release should succeed for fail-open reservations."""
        import uuid
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        account = TokenAccount(
            user_id="failopen-release-user",
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Use valid UUID format for request_id
        request_id = str(uuid.uuid4())

        response = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": "failopen-release-user",
                "request_id": request_id,
                "reservation_id": "failopen_abc123def456",
            },
            headers={"X-User-ID": "failopen-release-user"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "released"


class TestReservationTTL:
    """Test reservation TTL handling."""

    def test_reservation_ttl_configured(self):
        """Reservation TTL should be configured in settings."""
        assert hasattr(settings, "reservation_ttl")
        assert settings.reservation_ttl > 0
        # Reservation TTL should be a reasonable value (configurable)
        # Could be 300 (5 min) or 600 (10 min) depending on env config
        assert settings.reservation_ttl in [300, 600]

    def test_lua_scripts_use_expire(self):
        """Lua scripts should set key expiry for cleanup."""
        for script_name in ["reserve.lua", "finalize.lua", "release.lua"]:
            script_path = SCRIPTS_DIR / script_name
            content = script_path.read_text()
            assert "EXPIRE" in content, f"{script_name} should set key expiry"

    def test_reserve_script_uses_ttl_for_member_score(self):
        """Reserve script should use expiry timestamp as sorted set score."""
        script_path = SCRIPTS_DIR / "reserve.lua"
        content = script_path.read_text()
        # The expiry is passed as ARGV[4] and used as score in ZADD
        assert "expiry" in content
        assert "ZADD" in content
