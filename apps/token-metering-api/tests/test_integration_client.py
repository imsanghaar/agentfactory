"""Integration tests for metering client (study-mode-api pattern) - v5.

These tests validate the metering API can be called correctly from
a client like study-mode-api. They test the flow:

1. PRE-CHECK: POST /check → reservation_id (or 402 blocked)
2. LLM CALL: (external)
3a. SUCCESS: POST /deduct → transaction_id
3b. FAILURE: POST /release → released

v5 uses balance stored directly on TokenAccount with STARTER_TOKENS for new users.
"""

from datetime import UTC, datetime

from httpx import AsyncClient

from tests.helpers import make_request_id
from token_metering_api.models import (
    STARTER_TOKENS,
    AccountStatus,
    TokenAccount,
)


class TestMeteringClientFlow:
    """Test the complete metering flow as study-mode-api would call it."""

    async def test_complete_flow_user_with_balance(self, client: AsyncClient, test_session):
        """Test complete check → deduct flow for user with balance."""
        account = TokenAccount(
            user_id="flow-test-1",
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: PRE-CHECK (before LLM call)
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-1",
                "request_id": make_request_id("req-flow-001"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-1"},
        )

        assert check_response.status_code == 200
        check_data = check_response.json()
        assert check_data["allowed"] is True
        assert "reservation_id" in check_data
        reservation_id = check_data["reservation_id"]

        # Step 2: LLM CALL (simulated - would return actual tokens)
        actual_input_tokens = 3500
        actual_output_tokens = 1200

        # Step 3a: DEDUCT (after successful LLM call)
        deduct_response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "flow-test-1",
                "request_id": make_request_id("req-flow-001"),
                "reservation_id": reservation_id,
                "input_tokens": actual_input_tokens,
                "output_tokens": actual_output_tokens,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-1"},
        )

        assert deduct_response.status_code == 200
        deduct_data = deduct_response.json()
        assert deduct_data["status"] == "finalized"
        assert deduct_data["total_tokens"] == actual_input_tokens + actual_output_tokens
        assert "transaction_id" in deduct_data

        # v6: verify account.balance was updated (credits, not raw tokens)
        from tests.helpers import calculate_expected_credits

        await test_session.refresh(account)
        expected_credits = calculate_expected_credits(actual_input_tokens, actual_output_tokens)
        assert account.balance == 100000 - expected_credits

    async def test_complete_flow_new_user_with_starter_tokens(
        self, client: AsyncClient, test_session
    ):
        """Test complete flow for new user (gets STARTER_TOKENS)."""
        user_id = "flow-test-new"

        # Step 1: PRE-CHECK (user auto-created with STARTER_TOKENS)
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("req-new-flow-001"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        assert check_response.status_code == 200
        check_data = check_response.json()
        assert check_data["allowed"] is True
        reservation_id = check_data["reservation_id"]

        # Step 3a: DEDUCT
        deduct_response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("req-new-flow-001"),
                "reservation_id": reservation_id,
                "input_tokens": 3000,
                "output_tokens": 2000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        assert deduct_response.status_code == 200
        deduct_data = deduct_response.json()
        assert deduct_data["status"] == "finalized"
        assert deduct_data["balance_source"] == "balance"

        # Verify account was created with starter credits minus usage (in credits)
        from sqlalchemy import select

        from tests.helpers import calculate_expected_credits

        result = await test_session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one()
        expected_credits = calculate_expected_credits(3000, 2000)
        assert account.balance == STARTER_TOKENS - expected_credits

    async def test_flow_blocked_zero_balance(self, client: AsyncClient, test_session):
        """Test flow when user has zero balance."""
        account = TokenAccount(
            user_id="flow-test-blocked",
            balance=0,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: PRE-CHECK → Should be blocked
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-blocked",
                "request_id": make_request_id("req-blocked-001"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-blocked"},
        )

        # Should return 402 Payment Required
        assert check_response.status_code == 402
        error_data = check_response.json()
        assert error_data["allowed"] is False
        assert error_data["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_flow_blocked_suspended(self, client: AsyncClient, test_session):
        """Test flow when account is suspended."""
        account = TokenAccount(
            user_id="flow-test-suspended",
            status=AccountStatus.SUSPENDED,
            balance=1000000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: PRE-CHECK → Should be blocked
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-suspended",
                "request_id": make_request_id("req-suspended-001"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-suspended"},
        )

        assert check_response.status_code == 403
        error_data = check_response.json()
        assert error_data["error_code"] == "ACCOUNT_SUSPENDED"

    async def test_flow_release_on_llm_failure(self, client: AsyncClient, test_session):
        """Test release flow when LLM call fails."""
        account = TokenAccount(
            user_id="flow-test-release",
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        initial_balance = account.balance

        # Step 1: PRE-CHECK
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-release",
                "request_id": make_request_id("req-release-001"),
                "estimated_tokens": 10000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-release"},
        )

        assert check_response.status_code == 200
        reservation_id = check_response.json()["reservation_id"]

        # Step 2: LLM CALL FAILS (simulated)

        # Step 3b: RELEASE (cancel reservation)
        release_response = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": "flow-test-release",
                "request_id": make_request_id("req-release-001"),
                "reservation_id": reservation_id,
            },
            headers={"X-User-ID": "flow-test-release"},
        )

        assert release_response.status_code == 200
        release_data = release_response.json()
        assert release_data["status"] == "released"

        # v5: verify account.balance unchanged (no deduction)
        await test_session.refresh(account)
        assert account.balance == initial_balance

    async def test_idempotent_deduct(self, client: AsyncClient, test_session):
        """Test that duplicate deduct calls are idempotent."""
        account = TokenAccount(
            user_id="flow-test-idempotent",
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Check
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-idempotent",
                "request_id": make_request_id("req-idem-001"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-idempotent"},
        )
        reservation_id = check_response.json()["reservation_id"]

        # First deduct
        deduct_response1 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "flow-test-idempotent",
                "request_id": make_request_id("req-idem-001"),
                "reservation_id": reservation_id,
                "input_tokens": 2000,
                "output_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-idempotent"},
        )

        assert deduct_response1.status_code == 200
        tx_id1 = deduct_response1.json()["transaction_id"]

        # v5: verify account.balance after first deduct
        await test_session.refresh(account)
        balance_after_first = account.balance

        # Second deduct (same request_id) - should return same result
        deduct_response2 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "flow-test-idempotent",
                "request_id": make_request_id("req-idem-001"),
                "reservation_id": reservation_id,
                "input_tokens": 2000,
                "output_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-idempotent"},
        )

        assert deduct_response2.status_code == 200
        assert deduct_response2.json()["status"] == "already_processed"
        assert deduct_response2.json()["transaction_id"] == tx_id1

        # Verify no double charge
        await test_session.refresh(account)
        assert account.balance == balance_after_first


class TestMeteringClientEstimation:
    """Test token estimation scenarios."""

    async def test_actual_exceeds_estimate(self, client: AsyncClient, test_session):
        """Test when actual tokens exceed estimate (common case)."""
        account = TokenAccount(
            user_id="flow-test-exceed",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Check with low estimate
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-exceed",
                "request_id": make_request_id("req-exceed-001"),
                "estimated_tokens": 1000,  # Low estimate
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-exceed"},
        )
        reservation_id = check_response.json()["reservation_id"]

        # Deduct with higher actual
        deduct_response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "flow-test-exceed",
                "request_id": make_request_id("req-exceed-001"),
                "reservation_id": reservation_id,
                "input_tokens": 3000,
                "output_tokens": 2000,  # Total 5000 (5x estimate)
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-exceed"},
        )

        assert deduct_response.status_code == 200
        assert deduct_response.json()["total_tokens"] == 5000

        # v6: verify credits were deducted (not raw tokens)
        from tests.helpers import calculate_expected_credits

        await test_session.refresh(account)
        expected_credits = calculate_expected_credits(3000, 2000)
        assert account.balance == 10000 - expected_credits

    async def test_actual_less_than_estimate(self, client: AsyncClient, test_session):
        """Test when actual tokens less than estimate."""
        account = TokenAccount(
            user_id="flow-test-less",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Check with high estimate
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "flow-test-less",
                "request_id": make_request_id("req-less-001"),
                "estimated_tokens": 8000,  # High estimate
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-less"},
        )
        reservation_id = check_response.json()["reservation_id"]

        # Deduct with lower actual
        deduct_response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": "flow-test-less",
                "request_id": make_request_id("req-less-001"),
                "reservation_id": reservation_id,
                "input_tokens": 500,
                "output_tokens": 500,  # Total 1000 (much less than estimate)
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "flow-test-less"},
        )

        assert deduct_response.status_code == 200
        assert deduct_response.json()["total_tokens"] == 1000

        # v6: verify only actual was deducted (in credits)
        from tests.helpers import calculate_expected_credits

        await test_session.refresh(account)
        expected_credits = calculate_expected_credits(500, 500)
        assert account.balance == 10000 - expected_credits


class TestMeteringClientNewUser:
    """Test auto-creation behavior for new users."""

    async def test_new_user_auto_created_on_check(self, client: AsyncClient):
        """Test that new user account is auto-created on first check with STARTER_TOKENS."""
        # No account exists for this user

        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": "brand-new-user-auto",
                "request_id": make_request_id("req-new-001"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": "brand-new-user-auto"},
        )

        # Should succeed (new user gets starter tokens)
        assert check_response.status_code == 200
        assert check_response.json()["allowed"] is True

    async def test_new_user_full_flow(self, client: AsyncClient):
        """Test complete flow for brand new user."""
        user_id = "brand-new-full-flow"

        # Check (auto-creates account with STARTER_TOKENS)
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("req-new-full-001"),
                "estimated_tokens": 2000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        assert check_response.status_code == 200
        reservation_id = check_response.json()["reservation_id"]

        # Deduct
        deduct_response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("req-new-full-001"),
                "reservation_id": reservation_id,
                "input_tokens": 1000,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        assert deduct_response.status_code == 200
        assert deduct_response.json()["balance_source"] == "balance"
