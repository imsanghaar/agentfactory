"""API endpoint tests for metering routes (v5 - Balance Only).

Tests the v5 token metering model:
- Suspended? → BLOCK (ACCOUNT_SUSPENDED)
- Expired (inactive 365+ days)? → BLOCK (INSUFFICIENT_BALANCE, is_expired=true)
- Balance >= estimated_tokens? → ALLOW (create reservation)
- Otherwise → BLOCK (INSUFFICIENT_BALANCE)

v5: New users get STARTER_TOKENS (50,000). No trial tracking.
Balance is stored directly on TokenAccount.
"""

from datetime import UTC, datetime

from httpx import AsyncClient

from tests.helpers import make_request_id
from token_metering_api.config import settings
from token_metering_api.models import (
    AccountStatus,
    TokenAccount,
)


class TestCheckEndpoint:
    """Tests for POST /api/v1/metering/check."""

    async def test_check_allows_user_with_balance(
        self, client: AsyncClient, user_with_balance, test_session
    ):
        """User with balance gets reservation approved."""
        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-check-001"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "balance-user-456"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["allowed"] is True
        assert "reservation_id" in data
        assert data["reserved_credits"] > 0

    async def test_check_blocks_zero_balance_user(
        self, client: AsyncClient, zero_balance_user, test_session
    ):
        """User with 0 balance gets blocked."""
        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "zero-balance-789",
                "request_id": make_request_id("req-check-002"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "zero-balance-789"},
        )

        assert response.status_code == 402
        data = response.json()
        assert data["allowed"] is False
        assert data["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_check_blocks_suspended_user(self, client: AsyncClient, test_session):
        """Suspended user is blocked even with balance."""
        account = TokenAccount(
            user_id="suspended-user-111",
            status=AccountStatus.SUSPENDED,
            balance=1000000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "suspended-user-111",
                "request_id": make_request_id("req-check-003"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "suspended-user-111"},
        )

        assert response.status_code == 403
        data = response.json()
        assert data["allowed"] is False
        assert data["error_code"] == "ACCOUNT_SUSPENDED"

    async def test_check_returns_403_on_user_mismatch(
        self, client: AsyncClient, user_with_balance, test_session
    ):
        """User ID mismatch returns 403 Forbidden."""
        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-check-004"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "different-user"},
        )

        assert response.status_code == 403

    async def test_check_auto_creates_account_with_starter_tokens(
        self, client: AsyncClient, test_session
    ):
        """Check endpoint auto-creates account with STARTER_TOKENS."""
        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "brand-new-user",
                "request_id": make_request_id("req-check-005"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "brand-new-user"},
        )

        # New user should be allowed with starter tokens
        assert response.status_code == 200
        data = response.json()
        assert data["allowed"] is True


class TestDeductEndpoint:
    """Tests for POST /api/v1/metering/deduct."""

    async def test_deduct_creates_transaction(
        self, client: AsyncClient, user_with_balance, test_session
    ):
        """Successful deduct creates transaction and returns details."""
        response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-deduct-001"),
                "reservation_id": "res_abc123def456",
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "balance-user-456"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "finalized"
        assert data["total_tokens"] == 1000
        # v6: credits_deducted is cost-weighted, not raw tokens
        from tests.helpers import calculate_expected_credits

        expected = calculate_expected_credits(500, 500)
        assert data["credits_deducted"] == expected
        assert "transaction_id" in data

    async def test_deduct_idempotent_on_duplicate_request_id(
        self, client: AsyncClient, user_with_balance, test_session
    ):
        """Duplicate request_id returns same transaction (idempotency)."""
        # First deduct
        response1 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-deduct-dup"),
                "reservation_id": "res_def789abc012",
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "balance-user-456"},
        )
        tx_id1 = response1.json()["transaction_id"]

        # Second deduct with same request_id
        response2 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-deduct-dup"),
                "reservation_id": "res_def789abc012",
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "balance-user-456"},
        )

        assert response2.status_code == 200
        assert response2.json()["status"] == "already_processed"
        assert response2.json()["transaction_id"] == tx_id1


class TestReleaseEndpoint:
    """Tests for POST /api/v1/metering/release."""

    async def test_release_failopen_reservation(
        self, client: AsyncClient, user_with_balance, test_session
    ):
        """Release for fail-open reservation returns success."""
        response = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-release-001"),
                "reservation_id": "failopen_abc123",
            },
            headers={"X-User-ID": "balance-user-456"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "released"

    async def test_release_is_idempotent(
        self, client: AsyncClient, user_with_balance, test_session
    ):
        """Release is idempotent - second call succeeds."""
        # First release
        response1 = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-release-002"),
                "reservation_id": "res_aabbccdd1122",
            },
            headers={"X-User-ID": "balance-user-456"},
        )
        assert response1.status_code == 200

        # Second release
        response2 = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": "balance-user-456",
                "request_id": make_request_id("req-release-002"),
                "reservation_id": "res_aabbccdd1122",
            },
            headers={"X-User-ID": "balance-user-456"},
        )
        assert response2.status_code == 200
        assert response2.json()["status"] == "released"


class TestBalanceEndpoint:
    """Tests for GET /api/v1/balance."""

    async def test_get_balance_returns_v5_fields(self, client: AsyncClient, test_session):
        """Balance endpoint returns v5 fields."""
        account = TokenAccount(
            user_id="api-balance-1",
            balance=60000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        response = await client.get(
            "/api/v1/balance",
            headers={"X-User-ID": "api-balance-1"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == "api-balance-1"
        assert data["balance"] == 60000
        assert data["effective_balance"] == 60000
        assert data["is_expired"] is False

    async def test_get_balance_returns_404_for_unknown_user(
        self, client: AsyncClient, test_session
    ):
        """Balance endpoint returns 404 for non-existent user."""
        response = await client.get(
            "/api/v1/balance",
            headers={"X-User-ID": "nonexistent-user"},
        )

        assert response.status_code == 404


class TestAdminEndpoints:
    """Tests for admin endpoints (grant, topup)."""

    async def test_grant_adds_tokens(self, client: AsyncClient, test_session):
        """Grant endpoint adds tokens to account.balance."""
        account = TokenAccount(
            user_id="grant-target",
            balance=0,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": "grant-target",
                "credits": 500000,
                "reason": "Panaversity enrollment",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["credits_granted"] == 500000

        await test_session.refresh(account)
        assert account.balance == 500000

    async def test_topup_adds_tokens(self, client: AsyncClient, test_session):
        """Topup endpoint adds tokens to account.balance."""
        account = TokenAccount(
            user_id="topup-target",
            balance=1000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        response = await client.post(
            "/api/v1/admin/topup",
            json={
                "user_id": "topup-target",
                "credits": 100000,
                "payment_reference": "stripe_pi_123",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["credits_added"] == 100000

        await test_session.refresh(account)
        assert account.balance == 101000

    async def test_grant_creates_account_with_starter_tokens_plus_grant(
        self, client: AsyncClient, test_session
    ):
        """Grant for new user creates account with starter + grant tokens."""
        response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": "new-grant-user",
                "credits": 100000,
                "reason": "New enrollment",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True

        # Balance should be starter + grant
        assert data["new_balance"] == settings.starter_credits + 100000


class TestInactivityExpiry:
    """Tests for inactivity-based expiry."""

    async def test_check_blocks_inactive_user_with_is_expired(
        self, client: AsyncClient, inactive_user, test_session
    ):
        """Inactive user is blocked with is_expired=true."""
        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "inactive-user-000",
                "request_id": make_request_id("req-inactive-001"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "inactive-user-000"},
        )

        assert response.status_code == 402
        data = response.json()
        assert data["allowed"] is False
        assert data["error_code"] == "INSUFFICIENT_BALANCE"
        assert data["is_expired"] is True


class TestNegativeBalance:
    """Tests for negative balance handling."""

    async def test_check_blocks_negative_balance_user(
        self, client: AsyncClient, negative_balance_user, test_session
    ):
        """User with negative balance is blocked."""
        response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "negative-balance-111",
                "request_id": make_request_id("req-negative-001"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "negative-balance-111"},
        )

        assert response.status_code == 402
        data = response.json()
        assert data["allowed"] is False
        assert data["error_code"] == "INSUFFICIENT_BALANCE"
