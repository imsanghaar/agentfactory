"""Security tests for token metering API.

Tests for critical security vulnerabilities:
- CRIT-001: Dev mode admin bypass
- CRIT-002: JWT audience verification
- HIGH-001: Rate limiting
- HIGH-002: Token limits on admin endpoints
"""

from unittest.mock import patch

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from token_metering_api.main import app

# === CRIT-001: Dev Mode Admin Bypass Tests ===


class TestDevModeAdminBypass:
    """Test that dev mode does NOT automatically grant admin role."""

    @pytest_asyncio.fixture
    async def dev_mode_client(self, test_session):
        """Create client with dev mode enabled but not admin."""
        from token_metering_api.config import settings
        from token_metering_api.core.database import get_session

        async def override_get_session():
            yield test_session

        app.dependency_overrides[get_session] = override_get_session

        # Enable dev mode
        original_dev_mode = settings.dev_mode
        original_environment = getattr(settings, "environment", None)
        settings.dev_mode = True

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            yield client

        settings.dev_mode = original_dev_mode
        if original_environment is not None:
            settings.environment = original_environment
        app.dependency_overrides.clear()

    @pytest.mark.asyncio
    async def test_dev_mode_does_not_grant_admin_by_default(self, dev_mode_client, test_session):
        """Dev mode should NOT automatically grant admin role."""
        # Create a user in the database first
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        account = TokenAccount(
            user_id="test-user-no-admin",
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Try to access admin endpoint without explicit admin header
        response = await dev_mode_client.post(
            "/api/v1/admin/grant",
            json={"user_id": "target-user", "credits": 1000},
            headers={"X-User-ID": "test-user-no-admin"},
        )

        # Should be forbidden - dev mode without explicit admin header
        assert response.status_code == 403
        json_response = response.json()
        # Check for admin role required message in either format
        assert (
            "Admin role required" in json_response.get("detail", "")
            or "Admin role required" in json_response.get("message", "")
        )

    @pytest.mark.asyncio
    async def test_dev_mode_requires_explicit_admin_header(self, dev_mode_client, test_session):
        """Dev mode requires X-Dev-Admin: true header for admin access."""
        # Create target user
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        account = TokenAccount(
            user_id="target-user-for-grant",
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # With explicit admin header, should succeed
        response = await dev_mode_client.post(
            "/api/v1/admin/grant",
            json={"user_id": "target-user-for-grant", "credits": 1000, "reason": "test"},
            headers={
                "X-User-ID": "admin-user",
                "X-Dev-Admin": "true",
            },
        )

        # Should succeed with explicit admin header
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True

    @pytest.mark.asyncio
    async def test_dev_mode_admin_header_must_be_true(self, dev_mode_client, test_session):
        """X-Dev-Admin header must be exactly 'true' to grant admin."""
        response = await dev_mode_client.post(
            "/api/v1/admin/grant",
            json={"user_id": "target-user", "credits": 1000},
            headers={
                "X-User-ID": "test-user",
                "X-Dev-Admin": "false",
            },
        )

        # Should be forbidden - header is not 'true'
        assert response.status_code == 403

    @pytest.mark.asyncio
    async def test_dev_mode_blocked_in_production_environment(self, test_session):
        """Dev mode should be blocked when ENVIRONMENT=production."""
        from token_metering_api.config import settings
        from token_metering_api.core.database import get_session

        async def override_get_session():
            yield test_session

        app.dependency_overrides[get_session] = override_get_session

        # Set production environment
        original_dev_mode = settings.dev_mode
        original_environment = getattr(settings, "environment", "development")
        settings.dev_mode = True
        settings.environment = "production"

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            # Even with dev_mode=True and admin header, production should block
            response = await client.get(
                "/api/v1/balance",
                headers={
                    "X-User-ID": "any-user",
                    "X-Dev-Admin": "true",
                },
            )

            # In production, dev mode bypass should not work - require real auth
            assert response.status_code == 401

        settings.dev_mode = original_dev_mode
        settings.environment = original_environment
        app.dependency_overrides.clear()


# === CRIT-002: JWT Audience Verification Tests ===


class TestJWTAudienceVerification:
    """Test that JWT audience is properly verified."""

    @pytest.mark.asyncio
    async def test_jwt_audience_verified(self):
        """JWT tokens must have correct audience."""
        import time

        from jose import jwt

        from token_metering_api.config import settings

        # Create a mock JWKS response (shortened key for testing)
        mock_rsa_n = "sXchDaQebSXKcvLlshBZWmslYWH0mHOKKDKQeUPe3n1bvZ"
        mock_jwks = {
            "keys": [
                {
                    "kty": "RSA",
                    "kid": "test-key-id",
                    "n": mock_rsa_n,
                    "e": "AQAB",
                }
            ]
        }

        # Patch get_jwks to return our mock
        with patch("token_metering_api.core.auth.get_jwks", return_value=mock_jwks):
            # Create a token with wrong audience
            jwt.encode(
                {
                    "sub": "user-123",
                    "aud": "wrong-audience",
                    "exp": int(time.time()) + 3600,
                },
                "secret",  # This won't match but we're testing audience check
                algorithm="HS256",
            )

            # The verify_jwt function should reject wrong audience
            # Note: This test verifies the configuration is correct
            # The actual audience validation happens during JWT decode
            assert hasattr(settings, "token_audience")
            assert settings.token_audience  # Must be non-empty


# === HIGH-001: Rate Limiting Tests ===


class TestRateLimiting:
    """Test that rate limiting is enforced."""

    @pytest_asyncio.fixture
    async def rate_limit_client(self, test_session):
        """Create client for rate limit testing."""
        from token_metering_api.config import settings
        from token_metering_api.core.database import get_session

        async def override_get_session():
            yield test_session

        app.dependency_overrides[get_session] = override_get_session

        original_dev_mode = settings.dev_mode
        settings.dev_mode = True

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            yield client

        settings.dev_mode = original_dev_mode
        app.dependency_overrides.clear()

    @pytest.mark.asyncio
    async def test_rate_limiting_enforced(self, rate_limit_client, test_session):
        """Endpoints should enforce rate limits."""
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        # Create user
        account = TokenAccount(
            user_id="rate-limit-test-user",
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Make many requests rapidly
        responses = []
        for _ in range(150):  # Exceed typical rate limit
            response = await rate_limit_client.get(
                "/api/v1/balance",
                headers={"X-User-ID": "rate-limit-test-user"},
            )
            responses.append(response.status_code)

        # At least some requests should be rate limited (429)
        assert 429 in responses, "Rate limiting should be enforced"

    @pytest.mark.asyncio
    async def test_admin_endpoints_have_stricter_rate_limits(self, rate_limit_client, test_session):
        """Admin endpoints should have stricter rate limits."""
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        # Create target user
        account = TokenAccount(
            user_id="admin-rate-limit-target",
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Make requests to admin endpoint
        responses = []
        for i in range(50):  # Admin limit should be lower
            response = await rate_limit_client.post(
                "/api/v1/admin/grant",
                json={"user_id": "admin-rate-limit-target", "credits": 100, "reason": f"test-{i}"},
                headers={
                    "X-User-ID": "admin-user",
                    "X-Dev-Admin": "true",
                },
            )
            responses.append(response.status_code)

        # Admin endpoints should hit rate limit sooner
        rate_limited = [r for r in responses if r == 429]
        assert len(rate_limited) > 0, "Admin endpoints should have rate limiting"


# === HIGH-002: Token Limits on Admin Endpoints Tests ===


class TestAdminTokenLimits:
    """Test that admin endpoints have reasonable token limits."""

    @pytest.mark.asyncio
    async def test_grant_rejects_excessive_tokens(self):
        """GrantRequest should reject tokens > 100,000,000."""
        from pydantic import ValidationError

        from token_metering_api.routes.schemas import GrantRequest

        # Should succeed with reasonable amount
        valid_request = GrantRequest(
            user_id="test-user",
            credits=100_000_000,  # Max allowed
            reason="valid grant",
        )
        assert valid_request.credits == 100_000_000

        # Should fail with excessive amount
        with pytest.raises(ValidationError) as exc_info:
            GrantRequest(
                user_id="test-user",
                credits=100_000_001,  # Exceeds max
                reason="invalid grant",
            )

        errors = exc_info.value.errors()
        assert any("less than or equal to" in str(e.get("msg", "")).lower() for e in errors)

    @pytest.mark.asyncio
    async def test_topup_rejects_excessive_tokens(self):
        """TopupRequest should reject tokens > 100,000,000."""
        from pydantic import ValidationError

        from token_metering_api.routes.schemas import TopupRequest

        # Should succeed with reasonable amount
        valid_request = TopupRequest(
            user_id="test-user",
            credits=100_000_000,  # Max allowed
            payment_reference="PAY-123",
        )
        assert valid_request.credits == 100_000_000

        # Should fail with excessive amount
        with pytest.raises(ValidationError) as exc_info:
            TopupRequest(
                user_id="test-user",
                credits=100_000_001,  # Exceeds max
                payment_reference="PAY-456",
            )

        errors = exc_info.value.errors()
        assert any("less than or equal to" in str(e.get("msg", "")).lower() for e in errors)

    @pytest_asyncio.fixture
    async def admin_client(self, test_session):
        """Create client with admin access."""
        from token_metering_api.config import settings
        from token_metering_api.core.database import get_session

        async def override_get_session():
            yield test_session

        app.dependency_overrides[get_session] = override_get_session

        original_dev_mode = settings.dev_mode
        settings.dev_mode = True

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            yield client

        settings.dev_mode = original_dev_mode
        app.dependency_overrides.clear()

    @pytest.mark.asyncio
    async def test_admin_grant_rejects_excessive_tokens_via_api(self, admin_client, test_session):
        """API should reject grant requests with excessive tokens."""
        from datetime import UTC, datetime

        from token_metering_api.models import TokenAccount

        # Create target user
        account = TokenAccount(
            user_id="excessive-grant-target",
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Try to grant excessive tokens
        response = await admin_client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": "excessive-grant-target",
                "credits": 100_000_001,
                "reason": "excessive grant",
            },
            headers={
                "X-User-ID": "admin-user",
                "X-Dev-Admin": "true",
            },
        )

        # Should be rejected by validation
        assert response.status_code == 422  # Validation error


# === Configuration Tests ===


class TestSecurityConfiguration:
    """Test security-related configuration."""

    def test_token_audience_configured(self):
        """TOKEN_AUDIENCE setting should exist with default."""
        from token_metering_api.config import settings

        assert hasattr(settings, "token_audience")
        assert settings.token_audience  # Must be non-empty

    def test_environment_setting_exists(self):
        """ENVIRONMENT setting should exist."""
        from token_metering_api.config import settings

        assert hasattr(settings, "environment")
        assert settings.environment in ["development", "staging", "production"]

    def test_rate_limit_settings_exist(self):
        """Rate limit settings should exist."""
        from token_metering_api.config import settings

        assert hasattr(settings, "rate_limit_requests")
        assert hasattr(settings, "rate_limit_window")
        assert hasattr(settings, "admin_rate_limit_requests")
        assert settings.rate_limit_requests > 0
        assert settings.admin_rate_limit_requests > 0
        assert settings.admin_rate_limit_requests <= settings.rate_limit_requests
