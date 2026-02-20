"""Tests for authentication module (auth.py).

Tests JWT validation, dev mode authentication, and admin role requirements.
"""

from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException
from httpx import ASGITransport, AsyncClient

from token_metering_api.config import settings
from token_metering_api.core.auth import (
    CurrentUser,
    _check_dev_mode_safety,
    get_current_user,
    get_jwks,
    require_admin,
    verify_jwt,
)
from token_metering_api.core.exceptions import MeteringAPIException
from token_metering_api.main import app


class TestCurrentUser:
    """Test CurrentUser dataclass."""

    def test_current_user_from_payload(self):
        """CurrentUser should extract fields from payload dict."""
        payload = {
            "sub": "user-123",
            "email": "user@example.com",
            "name": "Test User",
            "roles": ["user", "admin"],
        }
        user = CurrentUser(payload)

        assert user.id == "user-123"
        assert user.email == "user@example.com"
        assert user.name == "Test User"
        assert user.roles == ["user", "admin"]

    def test_current_user_has_role(self):
        """has_role should check if user has specific role."""
        user = CurrentUser({"sub": "user-123", "roles": ["user", "editor"]})

        assert user.has_role("user") is True
        assert user.has_role("editor") is True
        assert user.has_role("admin") is False

    def test_current_user_is_admin(self):
        """is_admin should return True for admin role."""
        admin_user = CurrentUser({"sub": "admin-123", "roles": ["admin"]})
        regular_user = CurrentUser({"sub": "user-123", "roles": ["user"]})

        assert admin_user.is_admin is True
        assert regular_user.is_admin is False

    def test_current_user_missing_roles(self):
        """CurrentUser should handle missing roles gracefully."""
        user = CurrentUser({"sub": "user-123"})

        assert user.roles == []
        assert user.has_role("admin") is False
        assert user.is_admin is False

    def test_current_user_none_roles(self):
        """CurrentUser should handle None roles gracefully."""
        user = CurrentUser({"sub": "user-123", "roles": None})

        # roles is None, so has_role returns False
        assert user.roles is None
        assert user.has_role("admin") is False


class TestDevModeAuthentication:
    """Test dev mode authentication behavior."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock FastAPI Request object."""
        request = MagicMock()
        request.headers = {}
        return request

    @pytest.mark.asyncio
    async def test_dev_mode_uses_x_user_id_header(self, mock_request):
        """Dev mode should use X-User-ID header."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "development"

        mock_request.headers = {"X-User-ID": "custom-user-from-header"}

        try:
            user = await get_current_user(mock_request)
            assert user.id == "custom-user-from-header"
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env

    @pytest.mark.asyncio
    async def test_dev_mode_falls_back_to_config_user_id(self, mock_request):
        """Dev mode should use config user_id if header missing."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        original_dev_user_id = settings.dev_user_id
        settings.dev_mode = True
        settings.environment = "development"
        settings.dev_user_id = "fallback-dev-user"

        mock_request.headers = {}

        try:
            user = await get_current_user(mock_request)
            assert user.id == "fallback-dev-user"
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env
            settings.dev_user_id = original_dev_user_id

    @pytest.mark.asyncio
    async def test_dev_mode_admin_requires_explicit_header(self, mock_request):
        """Dev mode admin requires X-Dev-Admin: true header."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "development"

        # Without X-Dev-Admin header - no admin role
        mock_request.headers = {"X-User-ID": "user-123"}
        user_no_admin = await get_current_user(mock_request)
        assert user_no_admin.is_admin is False

        # With X-Dev-Admin: true - has admin role
        mock_request.headers = {"X-User-ID": "user-123", "X-Dev-Admin": "true"}
        user_with_admin = await get_current_user(mock_request)
        assert user_with_admin.is_admin is True

        # With X-Dev-Admin: false - no admin role
        mock_request.headers = {"X-User-ID": "user-123", "X-Dev-Admin": "false"}
        user_false_admin = await get_current_user(mock_request)
        assert user_false_admin.is_admin is False

        settings.dev_mode = original_dev_mode
        settings.environment = original_env

    @pytest.mark.asyncio
    async def test_dev_mode_blocked_in_production(self, mock_request):
        """Dev mode in production should raise 401."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "production"

        try:
            with pytest.raises(HTTPException) as exc_info:
                await get_current_user(mock_request)
            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Authentication required"
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env


class TestJWTAuthentication:
    """Test JWT validation flow."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock FastAPI Request object."""
        request = MagicMock()
        request.headers = {}
        return request

    @pytest.mark.asyncio
    async def test_missing_authorization_header_returns_401(self, mock_request):
        """Request without Authorization header should return 401."""
        original_dev_mode = settings.dev_mode
        settings.dev_mode = False

        mock_request.headers = {}

        try:
            with pytest.raises(HTTPException) as exc_info:
                await get_current_user(mock_request)
            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Missing Authorization header"
        finally:
            settings.dev_mode = original_dev_mode

    @pytest.mark.asyncio
    async def test_invalid_token_format_returns_401(self, mock_request):
        """Token not starting with 'Bearer ' should return 401."""
        original_dev_mode = settings.dev_mode
        settings.dev_mode = False

        # Token without "Bearer " prefix
        mock_request.headers = {"Authorization": "just-a-token"}

        try:
            with pytest.raises(HTTPException) as exc_info:
                await get_current_user(mock_request)
            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Missing Authorization header"
        finally:
            settings.dev_mode = original_dev_mode

    @pytest.mark.asyncio
    async def test_malformed_jwt_returns_401(self, mock_request):
        """Invalid JWT structure (not 3 parts) should return 401."""
        original_dev_mode = settings.dev_mode
        settings.dev_mode = False

        # JWT should have exactly 2 dots (3 parts)
        mock_request.headers = {"Authorization": "Bearer invalid.token"}

        try:
            with pytest.raises(HTTPException) as exc_info:
                await get_current_user(mock_request)
            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Invalid token format"
        finally:
            settings.dev_mode = original_dev_mode

    @pytest.mark.asyncio
    async def test_get_current_user_extracts_user_id(self, mock_request):
        """Valid dev mode should extract user_id correctly."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "development"

        mock_request.headers = {"X-User-ID": "extracted-user-id"}

        try:
            user = await get_current_user(mock_request)
            assert user.id == "extracted-user-id"
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env

    @pytest.mark.asyncio
    async def test_admin_role_from_jwt_claims(self, mock_request):
        """Admin role should be extracted from JWT roles claim in dev mode."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "development"

        mock_request.headers = {"X-User-ID": "admin-user", "X-Dev-Admin": "true"}

        try:
            user = await get_current_user(mock_request)
            assert user.is_admin is True
            assert "admin" in user.roles
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env


class TestGetJWKS:
    """Test JWKS fetching."""

    @pytest.mark.asyncio
    async def test_jwks_requires_sso_url(self):
        """get_jwks should raise 500 if SSO_URL not configured."""
        original_sso_url = settings.sso_url
        settings.sso_url = ""

        # Clear cache to force fetch
        import token_metering_api.core.auth as auth_module

        auth_module._jwks_cache = None
        auth_module._jwks_cache_time = 0

        try:
            with pytest.raises(HTTPException) as exc_info:
                await get_jwks()
            assert exc_info.value.status_code == 500
            assert exc_info.value.detail == "SSO_URL not configured"
        finally:
            settings.sso_url = original_sso_url

    @pytest.mark.asyncio
    async def test_jwks_returns_cached_value(self):
        """get_jwks should return cached value within TTL."""
        import time

        import token_metering_api.core.auth as auth_module

        cached_jwks = {"keys": [{"kid": "test-key", "kty": "RSA"}]}
        auth_module._jwks_cache = cached_jwks
        auth_module._jwks_cache_time = time.time()  # Fresh cache

        result = await get_jwks()
        assert result == cached_jwks

        # Clean up
        auth_module._jwks_cache = None
        auth_module._jwks_cache_time = 0

    @pytest.mark.asyncio
    async def test_jwks_fetch_failure_returns_stale_cache(self):
        """get_jwks should return stale cache on fetch failure."""
        import time

        import token_metering_api.core.auth as auth_module

        original_sso_url = settings.sso_url
        settings.sso_url = "http://invalid-sso-url.local"

        # Set up stale cache (past TTL)
        stale_jwks = {"keys": [{"kid": "stale-key", "kty": "RSA"}]}
        auth_module._jwks_cache = stale_jwks
        auth_module._jwks_cache_time = time.time() - settings.jwks_cache_ttl - 100

        try:
            result = await get_jwks()
            # Should return stale cache because fetch fails
            assert result == stale_jwks
        finally:
            settings.sso_url = original_sso_url
            auth_module._jwks_cache = None
            auth_module._jwks_cache_time = 0


class TestVerifyJWT:
    """Test JWT verification."""

    @pytest.mark.asyncio
    async def test_verify_jwt_with_invalid_header(self):
        """verify_jwt should raise 401 for JWT with invalid header."""
        import time

        import token_metering_api.core.auth as auth_module

        # Set up JWKS cache
        auth_module._jwks_cache = {"keys": [{"kid": "test-key", "kty": "RSA"}]}
        auth_module._jwks_cache_time = time.time()

        try:
            with pytest.raises(HTTPException) as exc_info:
                # Valid JWT structure but invalid/undecodable
                await verify_jwt("eyJ.eyJ.sig")
            assert exc_info.value.status_code == 401
        finally:
            auth_module._jwks_cache = None
            auth_module._jwks_cache_time = 0

    @pytest.mark.asyncio
    async def test_verify_jwt_key_not_found(self):
        """verify_jwt should raise 401 if key ID not in JWKS."""
        import time

        import token_metering_api.core.auth as auth_module

        # Set up JWKS cache with different key
        auth_module._jwks_cache = {"keys": [{"kid": "other-key", "kty": "RSA"}]}
        auth_module._jwks_cache_time = time.time()

        # Create a mock unverified header that returns a different kid
        with patch("token_metering_api.core.auth.jwt") as mock_jwt:
            mock_jwt.get_unverified_header.return_value = {"kid": "missing-key"}

            try:
                with pytest.raises(HTTPException) as exc_info:
                    await verify_jwt("header.payload.signature")
                assert exc_info.value.status_code == 401
                assert exc_info.value.detail == "Unable to find appropriate key"
            finally:
                auth_module._jwks_cache = None
                auth_module._jwks_cache_time = 0


class TestRequireAdmin:
    """Test admin requirement dependency."""

    @pytest.mark.asyncio
    async def test_require_admin_passes_for_admin_user(self):
        """Admin user should pass require_admin check."""
        admin_user = CurrentUser({"sub": "admin-user", "roles": ["admin"]})

        result = await require_admin(admin_user)
        assert result.id == "admin-user"
        assert result.is_admin is True

    @pytest.mark.asyncio
    async def test_require_admin_raises_403_for_non_admin(self):
        """Non-admin user should get 403."""
        regular_user = CurrentUser({"sub": "user-123", "roles": ["user"]})

        with pytest.raises(MeteringAPIException) as exc_info:
            await require_admin(regular_user)

        assert exc_info.value.status_code == 403
        assert exc_info.value.error_code == "FORBIDDEN"
        assert exc_info.value.message == "Admin role required"

    @pytest.mark.asyncio
    async def test_require_admin_raises_403_for_no_roles(self):
        """User without roles should get 403."""
        no_role_user = CurrentUser({"sub": "user-123"})

        with pytest.raises(MeteringAPIException) as exc_info:
            await require_admin(no_role_user)

        assert exc_info.value.status_code == 403


class TestDevModeSafetyCheck:
    """Test _check_dev_mode_safety function."""

    def test_dev_mode_logs_warning_in_development(self):
        """Dev mode should log warning in non-production."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "development"

        try:
            # Should not raise, just log warning
            _check_dev_mode_safety()
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env

    def test_dev_mode_raises_401_in_production(self):
        """Dev mode should raise 401 in production."""
        original_dev_mode = settings.dev_mode
        original_env = settings.environment
        settings.dev_mode = True
        settings.environment = "production"

        try:
            with pytest.raises(HTTPException) as exc_info:
                _check_dev_mode_safety()
            assert exc_info.value.status_code == 401
        finally:
            settings.dev_mode = original_dev_mode
            settings.environment = original_env


class TestAuthEndpoints:
    """Integration tests for auth in API endpoints."""

    @pytest.mark.asyncio
    async def test_endpoint_without_auth_header_returns_401(self, test_session):
        """Endpoint without auth header should return 401 when dev mode disabled."""
        from token_metering_api.core.database import get_session

        original_dev_mode = settings.dev_mode
        settings.dev_mode = False

        async def override_get_session():
            yield test_session

        app.dependency_overrides[get_session] = override_get_session

        try:
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                response = await client.get("/api/v1/balance")

            assert response.status_code == 401
        finally:
            settings.dev_mode = original_dev_mode
            app.dependency_overrides.clear()

    @pytest.mark.asyncio
    async def test_admin_endpoint_requires_admin_role(self, client, test_session):
        """Admin endpoint should return 403 for non-admin user."""
        # In dev mode, X-Dev-Admin header controls admin access
        response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": "some-user",
                "credits": 1000,
                "reason": "test",
            },
            headers={"X-User-ID": "non-admin-user"},  # No X-Dev-Admin header
        )

        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_admin_endpoint_allows_admin_user(self, client, test_session):
        """Admin endpoint should allow admin user."""
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        # Create the target account first
        account = TokenAccount(
            user_id="target-user",
            balance=0,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": "target-user",
                "credits": 1000,
                "reason": "test grant",
            },
            headers={"X-User-ID": "admin-user", "X-Dev-Admin": "true"},
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
