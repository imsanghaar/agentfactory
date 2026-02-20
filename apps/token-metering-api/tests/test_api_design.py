"""Tests for API design consistency (TDD for design fixes)."""

import uuid

import pytest
from httpx import AsyncClient


class TestUUIDValidation:
    """Test that request_id must be a valid UUID format."""

    @pytest.mark.asyncio
    async def test_invalid_uuid_request_id_rejected(self, client: AsyncClient, new_user):
        """Invalid UUID format for request_id should return 422."""
        response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": "not-a-valid-uuid",
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data

    @pytest.mark.asyncio
    async def test_uuid_with_colons_rejected(self, client: AsyncClient, new_user):
        """UUID with colons should be rejected (OpenAI format not allowed)."""
        response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": "12345678:1234:1234:1234:123456789012",
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_valid_uuid_accepted(self, client: AsyncClient, new_user):
        """Valid UUID format should be accepted."""
        valid_uuid = str(uuid.uuid4())
        response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": valid_uuid,
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        # Should get 200 (allowed) or 402/403/409 (blocked for business reasons)
        # but NOT 422 (validation error)
        assert response.status_code != 422


class TestReservationIdValidation:
    """Test that reservation_id must match expected format."""

    @pytest.mark.asyncio
    async def test_invalid_reservation_id_rejected_deduct(self, client: AsyncClient, new_user):
        """Invalid reservation_id format should return 422."""
        response = await client.post(
            "/api/v1/metering/deduct",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": str(uuid.uuid4()),
                "reservation_id": "invalid-format",
                "input_tokens": 100,
                "output_tokens": 200,
                "model": "deepseek-chat",
            },
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_invalid_reservation_id_rejected_release(self, client: AsyncClient, new_user):
        """Invalid reservation_id format should return 422 on release."""
        response = await client.post(
            "/api/v1/metering/release",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": str(uuid.uuid4()),
                "reservation_id": "bad_format_123",
            },
        )
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_valid_res_prefix_accepted(self, client: AsyncClient, new_user):
        """reservation_id with res_ prefix should pass validation."""
        # First make a check to get a real reservation
        check_response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": str(uuid.uuid4()),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        if check_response.status_code == 200:
            reservation_id = check_response.json()["reservation_id"]
            # The reservation_id should match the expected format
            assert reservation_id.startswith("res_") or reservation_id.startswith("failopen_")

    @pytest.mark.asyncio
    async def test_failopen_prefix_accepted(self, client: AsyncClient, new_user):
        """reservation_id with failopen_ prefix should pass validation."""
        # This tests that failopen_ prefix is valid format
        # Note: We can't easily trigger failopen mode in tests without Redis failure
        # but the format validation should accept it
        response = await client.post(
            "/api/v1/metering/deduct",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": new_user.user_id,
                "request_id": str(uuid.uuid4()),
                "reservation_id": "failopen_abc123def456",
                "input_tokens": 100,
                "output_tokens": 200,
                "model": "deepseek-chat",
            },
        )
        # Should not be 422 (validation error) - may be 404 (not found) which is OK
        assert response.status_code != 422


class TestErrorResponseFormat:
    """Test that error responses have consistent format."""

    @pytest.mark.asyncio
    async def test_insufficient_balance_error_format(self, client: AsyncClient, zero_balance_user):
        """402 error should have consistent error format."""
        response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": zero_balance_user.user_id},
            json={
                "user_id": zero_balance_user.user_id,
                "request_id": str(uuid.uuid4()),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        assert response.status_code == 402
        data = response.json()
        # BlockedResponse format
        assert "error_code" in data
        assert "message" in data
        assert data["error_code"] == "INSUFFICIENT_BALANCE"
        assert data["allowed"] is False

    @pytest.mark.asyncio
    async def test_suspended_account_error_format(self, client: AsyncClient, suspended_user):
        """403 error for suspended account should have consistent format."""
        response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": suspended_user.user_id},
            json={
                "user_id": suspended_user.user_id,
                "request_id": str(uuid.uuid4()),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        assert response.status_code == 403
        data = response.json()
        assert "error_code" in data
        assert "message" in data
        assert data["error_code"] == "ACCOUNT_SUSPENDED"

    @pytest.mark.asyncio
    async def test_user_mismatch_error_format(self, client: AsyncClient, new_user):
        """403 error for user mismatch should use MeteringAPIException format."""
        # Use the new_user's header but different user_id in body
        response = await client.post(
            "/api/v1/metering/check",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": "different-user-id",
                "request_id": str(uuid.uuid4()),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
        )
        assert response.status_code == 403
        data = response.json()
        # Should have error_code and message at top level (not nested in detail)
        assert "error_code" in data
        assert "message" in data
        assert data["error_code"] == "USER_MISMATCH"

    @pytest.mark.asyncio
    async def test_not_found_error_format(self, client: AsyncClient, new_user):
        """404 error should use consistent format."""
        # Need admin role to access this endpoint
        response = await client.get(
            "/api/v1/balance/nonexistent-user-12345",
            headers={"X-User-ID": new_user.user_id, "X-Dev-Admin": "true"},
        )
        # Should get 404 for non-existent user (with admin access)
        assert response.status_code == 404
        data = response.json()
        # After fix, should have consistent format
        assert "error_code" in data
        assert "message" in data

    @pytest.mark.asyncio
    async def test_admin_forbidden_error_format(self, client: AsyncClient, new_user):
        """Admin endpoint 403 (non-admin) should use consistent format."""
        # Without X-Dev-Admin header, should get 403
        response = await client.post(
            "/api/v1/admin/grant",
            headers={"X-User-ID": new_user.user_id},
            json={
                "user_id": "test-user",
                "credits": 1000,
            },
        )
        # Should get 403 for non-admin
        assert response.status_code == 403
        data = response.json()
        # After fix, should have consistent format
        assert "error_code" in data
        assert "message" in data


class TestAPIVersion:
    """Test API version consistency."""

    @pytest.mark.asyncio
    async def test_version_is_6_0_0(self, client: AsyncClient):
        """API version should be 6.0.0 per spec."""
        response = await client.get("/")
        data = response.json()
        assert data["version"] == "6.0.0"

    @pytest.mark.asyncio
    async def test_openapi_version_matches(self, client: AsyncClient):
        """OpenAPI spec version should match API version."""
        response = await client.get("/openapi.json")
        data = response.json()
        assert data["info"]["version"] == "6.0.0"


class TestOpenAPICompleteness:
    """Test that OpenAPI spec includes all endpoints."""

    @pytest.mark.asyncio
    async def test_metrics_endpoint_exists(self, client: AsyncClient):
        """GET /metrics endpoint should exist."""
        response = await client.get("/metrics")
        # Should return 200 with Prometheus metrics
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_balance_by_user_id_endpoint_exists(self, client: AsyncClient, new_user):
        """GET /api/v1/balance/{user_id} endpoint should exist."""
        # This will return 403 without admin role, but endpoint should exist
        response = await client.get(f"/api/v1/balance/{new_user.user_id}")
        # 403 (not admin) or 200 (if admin) - but NOT 404 (endpoint not found)
        assert response.status_code in [200, 403]
