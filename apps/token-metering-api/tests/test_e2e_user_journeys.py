"""End-to-end tests for complete user journeys (v6 - Credits).

These tests simulate real-world usage patterns through the full API.
Uses the v6 model with credits-based balance on TokenAccount.

The v6 model:
- Balance stored directly on TokenAccount.balance (source of truth, in credits)
- TokenAllocation is audit-only (no remaining_amount, no expires_at)
- Inactivity-based expiry (365 days of no activity)
- New users get STARTER_CREDITS (20,000)
- Balance deductions use cost-weighted credits, not raw tokens
"""

from datetime import UTC, datetime, timedelta

import pytest
from httpx import AsyncClient

from tests.helpers import (
    calculate_expected_credits,
    estimate_credits_pessimistic,
    make_request_id,
)
from token_metering_api.models import (
    STARTER_TOKENS,
    TokenAccount,
)


class TestNewUserJourney:
    """E2E: New user gets STARTER_CREDITS and uses them."""

    async def test_new_user_complete_lifecycle(self, client: AsyncClient, test_session):
        """New user: gets starter credits, uses them, needs topup."""
        user_id = "e2e-new-user"

        # Step 1: First request auto-creates account with STARTER_CREDITS
        check_response = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("new-req-1"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_response.status_code == 200
        check_data = check_response.json()
        assert check_data["allowed"] is True

        # Deduct 500i+500o = 18 credits
        deduct_response = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("new-req-1"),
                "reservation_id": check_data["reservation_id"],
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct_response.status_code == 200

        # Verify account has STARTER_CREDITS - 18 credits
        from sqlalchemy import select

        result = await test_session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one()
        expected_credits = calculate_expected_credits(500, 500)  # = 18
        assert account.balance == STARTER_TOKENS - expected_credits

        # Deplete starter credits via check+deduct loop.
        # Use 60k_i + 60k_o = 2,160 credits each. ~9 iterations for 20k credits.
        # estimated_tokens must stay under max_tokens (128k).
        deduct_credits = calculate_expected_credits(60_000, 60_000)
        credits_used = expected_credits
        request_num = 2
        while credits_used + deduct_credits <= STARTER_TOKENS:
            check = await client.post(
                "/api/v1/metering/check",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"new-req-{request_num}"),
                    "estimated_tokens": 120_000,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )
            if check.status_code != 200:
                break

            await client.post(
                "/api/v1/metering/deduct",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"new-req-{request_num}"),
                    "reservation_id": check.json()["reservation_id"],
                    "input_tokens": 60_000,
                    "output_tokens": 60_000,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )
            credits_used += deduct_credits
            request_num += 1

            # Safety: prevent infinite loop
            if request_num > 20:
                break

        # Now balance should be low, next large request should be blocked
        await test_session.refresh(account)
        _ = account.balance

        # Remaining balance should be less than one more deduct's estimated credits
        # estimated_credits for 120k tokens = 2880, remaining < 2880
        check_blocked = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("new-req-blocked"),
                "estimated_tokens": 120_000,  # Same as loop, exceeds remaining credits
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_blocked.status_code == 402
        assert check_blocked.json()["error_code"] == "INSUFFICIENT_BALANCE"


class TestBalanceUserJourney:
    """E2E: User with granted balance uses credits until depleted."""

    async def test_balance_use_deplete_cycle(self, client: AsyncClient, test_session):
        """User with balance: use credits -> deplete -> blocked -> grant more -> use."""
        user_id = "e2e-balance-user"

        # Create user with small balance (100 credits, not new, so no starter)
        account = TokenAccount(
            user_id=user_id,
            balance=100,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: Use credits until depleted
        # 1000i+500o = 24 credits per request. 100/24 = 4.16, so 4 requests
        requests_made = 0
        while True:
            check = await client.post(
                "/api/v1/metering/check",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"balance-req-{requests_made + 1}"),
                    "estimated_tokens": 1500,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )

            if check.status_code == 402:
                # Depleted
                break

            assert check.status_code == 200
            check_data = check.json()

            # Deduct (1000i+500o = 24 credits)
            await client.post(
                "/api/v1/metering/deduct",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"balance-req-{requests_made + 1}"),
                    "reservation_id": check_data["reservation_id"],
                    "input_tokens": 1000,
                    "output_tokens": 500,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )
            requests_made += 1

            # Safety: prevent infinite loop
            if requests_made > 10:
                pytest.fail("Too many requests - should have depleted by now")

        # Verify depleted: 100 balance, 24 credits deducted per request but
        # pessimistic estimate = 36 credits. After 3 deductions (72 credits used),
        # remaining = 28 < 36 estimated → blocked on 4th check.
        await test_session.refresh(account)
        assert requests_made == 3

        # Step 2: Grant more credits
        grant_response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": user_id,
                "credits": 200,
                "reason": "Additional allocation",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert grant_response.status_code == 200

        # Step 3: Can make requests again
        check_again = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("balance-req-after-grant"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_again.status_code == 200
        assert check_again.json()["allowed"] is True


class TestIdempotencyJourney:
    """E2E: Verify duplicate requests don't double-charge."""

    async def test_idempotent_deduct_no_double_charge(self, client: AsyncClient, test_session):
        """Same request_id returns same result without double deduction."""
        user_id = "e2e-idempotent-user"

        account = TokenAccount(
            user_id=user_id,
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # First request
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-req-1"),
                "estimated_tokens": 2000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200

        # First deduct (1000i+1000o = 36 credits)
        deduct1 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-req-1"),
                "reservation_id": check.json()["reservation_id"],
                "input_tokens": 1000,
                "output_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct1.status_code == 200
        tx_id_1 = deduct1.json()["transaction_id"]

        await test_session.refresh(account)
        balance_after_first = account.balance
        assert balance_after_first == 10000 - 36  # 9964

        # Duplicate deduct (same request_id)
        deduct2 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-req-1"),  # SAME request_id
                "reservation_id": check.json()["reservation_id"],
                "input_tokens": 1000,
                "output_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct2.status_code == 200
        assert deduct2.json()["status"] == "already_processed"
        assert deduct2.json()["transaction_id"] == tx_id_1

        # Balance should NOT have changed
        await test_session.refresh(account)
        assert account.balance == balance_after_first, "No double charge!"


class TestReleaseOnFailureJourney:
    """E2E: When LLM fails, reservation is released without charge."""

    async def test_release_after_llm_failure(self, client: AsyncClient, test_session):
        """Check -> LLM fails -> Release -> No credits deducted."""
        user_id = "e2e-release-user"

        account = TokenAccount(
            user_id=user_id,
            balance=5000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        initial_balance = account.balance

        # Check balance (creates reservation)
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("release-req-1"),
                "estimated_tokens": 2000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        reservation_id = check.json()["reservation_id"]

        # Simulate LLM failure - call release instead of deduct
        release = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": user_id,
                "request_id": make_request_id("release-req-1"),
                "reservation_id": reservation_id,
            },
            headers={"X-User-ID": user_id},
        )
        assert release.status_code == 200
        assert release.json()["status"] == "released"

        # v6: verify account.balance unchanged
        await test_session.refresh(account)
        assert account.balance == initial_balance, "No deduction after release"


class TestSuspendedAccountJourney:
    """E2E: Suspended account is blocked regardless of balance."""

    async def test_suspended_account_blocked(self, client: AsyncClient, test_session):
        """Suspended account cannot make any requests."""
        from token_metering_api.models import AccountStatus

        user_id = "e2e-suspended-user"

        account = TokenAccount(
            user_id=user_id,
            status=AccountStatus.SUSPENDED,
            balance=1_000_000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Even tiny request blocked
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("suspended-req-1"),
                "estimated_tokens": 1,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 403
        assert check.json()["error_code"] == "ACCOUNT_SUSPENDED"


class TestInactivityExpiryJourney:
    """E2E: Inactive users are blocked with is_expired=true."""

    async def test_inactive_user_blocked(self, client: AsyncClient, test_session):
        """User inactive for 365+ days is blocked."""
        user_id = "e2e-inactive-user"

        account = TokenAccount(
            user_id=user_id,
            balance=100000,  # Has balance
            last_activity_at=datetime.now(UTC) - timedelta(days=400),  # Inactive
        )
        test_session.add(account)
        await test_session.commit()

        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("inactive-req-1"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 402
        data = check.json()
        assert data["error_code"] == "INSUFFICIENT_BALANCE"
        assert data["is_expired"] is True


class TestCostTrackingJourney:
    """E2E: Verify 20% markup is correctly recorded in transactions."""

    async def test_markup_recorded_in_transaction(self, client: AsyncClient, test_session):
        """Transaction records base cost and 20% markup correctly."""
        from sqlalchemy import select

        from token_metering_api.models import TokenTransaction

        user_id = "e2e-cost-user"

        account = TokenAccount(
            user_id=user_id,
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Make a request
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("cost-req-1"),
                "estimated_tokens": 2000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200

        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("cost-req-1"),
                "reservation_id": check.json()["reservation_id"],
                "input_tokens": 1000,
                "output_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200

        # Verify transaction in database
        req_id = make_request_id("cost-req-1")
        result = await test_session.execute(
            select(TokenTransaction).where(TokenTransaction.request_id == req_id)
        )
        tx = result.scalar_one()

        assert tx.markup_percent == 20
        assert tx.total_cost_usd > tx.base_cost_usd
        # Verify: total = base * 1.20
        expected_total = float(tx.base_cost_usd) * 1.20
        assert abs(float(tx.total_cost_usd) - expected_total) < 0.000001


class TestBalanceQueryJourney:
    """E2E: Balance endpoint returns accurate v6 data."""

    async def test_balance_reflects_all_operations(self, client: AsyncClient, test_session):
        """Balance endpoint shows correct state after operations."""
        user_id = "e2e-balance-query-user"

        account = TokenAccount(
            user_id=user_id,
            balance=15000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Check initial balance
        balance1 = await client.get(
            "/api/v1/balance",
            headers={"X-User-ID": user_id},
        )
        assert balance1.status_code == 200
        data1 = balance1.json()
        assert data1["balance"] == 15000
        assert data1["effective_balance"] == 15000
        assert data1["is_expired"] is False

        # Make a request
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("balance-query-req-1"),
                "estimated_tokens": 3000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("balance-query-req-1"),
                "reservation_id": check.json()["reservation_id"],
                "input_tokens": 1500,
                "output_tokens": 1500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        # Check balance after deduction
        # 1500i+1500o = 54 credits
        balance2 = await client.get(
            "/api/v1/balance",
            headers={"X-User-ID": user_id},
        )
        assert balance2.status_code == 200
        data2 = balance2.json()
        expected_credits = calculate_expected_credits(1500, 1500)  # = 54
        assert data2["balance"] == 15000 - expected_credits
        assert data2["effective_balance"] == 15000 - expected_credits


class TestNewUserAutoCreation:
    """E2E: New user is auto-created with STARTER_CREDITS."""

    async def test_new_user_auto_created_on_check(self, client: AsyncClient, test_session):
        """Unknown user is auto-created when making first request."""
        user_id = "brand-new-e2e-user"

        # User doesn't exist yet - make a check request
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("new-user-req-1"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        # Should be allowed (gets STARTER_CREDITS)
        assert check.status_code == 200
        assert check.json()["allowed"] is True

        # User should now exist in database with STARTER_CREDITS
        from sqlalchemy import select

        result = await test_session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one_or_none()
        assert account is not None, "User should be auto-created"
        assert account.balance == STARTER_TOKENS  # v6: starts with starter credits


class TestNewUserStarterTokensJourney:
    """E2E: Test complete journey for a new user with starter credits."""

    async def test_new_user_gets_starter_tokens(self, client: AsyncClient, test_session):
        """First request should create account with 20k starter credits."""
        from sqlalchemy import select

        user_id = "starter-token-user-1"

        # User does not exist yet - first check request
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("starter-req-1"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        assert check.json()["allowed"] is True

        # Verify account created with STARTER_CREDITS
        result = await test_session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one()
        assert account.balance == STARTER_TOKENS

    async def test_new_user_can_immediately_use_tokens(self, client: AsyncClient, test_session):
        """New user should be able to check -> deduct -> verify balance."""
        from sqlalchemy import select

        user_id = "starter-use-user-1"

        # Step 1: Check (creates account with starter credits)
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("starter-use-req-1"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        reservation_id = check.json()["reservation_id"]

        # Step 2: Deduct (2500i+2500o = 90 credits)
        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("starter-use-req-1"),
                "reservation_id": reservation_id,
                "input_tokens": 2500,
                "output_tokens": 2500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200
        expected_credits = calculate_expected_credits(2500, 2500)  # = 90
        assert deduct.json()["credits_deducted"] == expected_credits

        # Step 3: Verify balance
        result = await test_session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one()
        assert account.balance == STARTER_TOKENS - expected_credits

    async def test_starter_allocation_recorded(self, client: AsyncClient, test_session):
        """Starter credit grant should appear in allocations."""
        user_id = "starter-alloc-user-1"

        # Trigger account creation
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("starter-alloc-req-1"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200

        # Get allocations
        alloc_response = await client.get(
            "/api/v1/allocations",
            headers={"X-User-ID": user_id},
        )
        assert alloc_response.status_code == 200
        allocations = alloc_response.json()["allocations"]

        # Starter allocation should be recorded
        assert len(allocations) >= 1
        starter_alloc = next(
            (a for a in allocations if a["allocation_type"] == "starter"), None
        )
        assert starter_alloc is not None
        assert starter_alloc["amount"] == STARTER_TOKENS


class TestAdminGrantJourney:
    """E2E: Test admin granting credits to users."""

    async def test_admin_grants_tokens_to_existing_user(self, client: AsyncClient, test_session):
        """Admin grant should increase balance."""
        user_id = "admin-grant-existing-user"

        # Create user with some balance
        account = TokenAccount(
            user_id=user_id,
            balance=1000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Admin grants credits
        grant_response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": user_id,
                "credits": 10000,
                "reason": "Course enrollment bonus",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert grant_response.status_code == 200
        assert grant_response.json()["credits_granted"] == 10000
        assert grant_response.json()["new_balance"] == 11000  # 1000 + 10000

    async def test_admin_grants_tokens_to_new_user(self, client: AsyncClient, test_session):
        """Admin grant to new user should create account first."""
        from sqlalchemy import select

        user_id = "admin-grant-new-user"

        # Grant to non-existent user
        grant_response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": user_id,
                "credits": 25000,
                "reason": "Premium membership",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert grant_response.status_code == 200

        # User should now exist with grant + starter credits
        result = await test_session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one()
        # New users get STARTER_CREDITS + grant
        assert account.balance == STARTER_TOKENS + 25000

    async def test_admin_grant_creates_allocation_record(self, client: AsyncClient, test_session):
        """Grant should appear in allocation history."""
        user_id = "admin-grant-alloc-user"

        # Create user
        account = TokenAccount(
            user_id=user_id,
            balance=0,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Admin grants
        await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": user_id,
                "credits": 5000,
                "reason": "Test grant allocation",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )

        # Check allocations
        alloc_response = await client.get(
            "/api/v1/allocations",
            headers={"X-User-ID": user_id},
        )
        assert alloc_response.status_code == 200
        allocations = alloc_response.json()["allocations"]

        grant_alloc = next(
            (a for a in allocations if a["allocation_type"] == "grant"), None
        )
        assert grant_alloc is not None
        assert grant_alloc["amount"] == 5000
        assert grant_alloc["reason"] == "Test grant allocation"

    async def test_admin_topup_clears_negative_balance(self, client: AsyncClient, test_session):
        """Topup should bring negative balance positive."""
        user_id = "admin-topup-negative-user"

        # Create user with negative balance (streaming overage)
        account = TokenAccount(
            user_id=user_id,
            balance=-500,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Admin topup
        topup_response = await client.post(
            "/api/v1/admin/topup",
            json={
                "user_id": user_id,
                "credits": 5000,
                "payment_reference": "PAY-123-ABC",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert topup_response.status_code == 200
        assert topup_response.json()["new_balance"] == 4500  # -500 + 5000


class TestErrorRecoveryJourneys:
    """E2E: Test error scenarios and recovery."""

    async def test_insufficient_balance_recovery(self, client: AsyncClient, test_session):
        """User with insufficient balance can recover after topup."""
        user_id = "error-recovery-user"

        # Create user with low balance
        account = TokenAccount(
            user_id=user_id,
            balance=1,  # Very low in credits
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: Request blocked due to insufficient balance
        check_blocked = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("recovery-req-1"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_blocked.status_code == 402
        assert check_blocked.json()["error_code"] == "INSUFFICIENT_BALANCE"

        # Step 2: Admin topup
        await client.post(
            "/api/v1/admin/topup",
            json={
                "user_id": user_id,
                "credits": 10000,
                "payment_reference": "RECOVERY-PAY",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )

        # Step 3: Can now make requests
        check_success = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("recovery-req-2"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_success.status_code == 200
        assert check_success.json()["allowed"] is True

    async def test_suspended_account_recovery(self, client: AsyncClient, test_session):
        """Suspended user can recover after admin unsuspends."""
        from token_metering_api.models import AccountStatus

        user_id = "suspended-recovery-user"

        # Create suspended account with balance
        account = TokenAccount(
            user_id=user_id,
            balance=50000,
            status=AccountStatus.SUSPENDED,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: Request blocked due to suspension
        check_blocked = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("suspended-recovery-req-1"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_blocked.status_code == 403
        assert check_blocked.json()["error_code"] == "ACCOUNT_SUSPENDED"

        # Step 2: Admin unsuspends (simulate by updating status directly)
        account.status = AccountStatus.ACTIVE
        await test_session.commit()

        # Step 3: Can now make requests
        check_success = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("suspended-recovery-req-2"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_success.status_code == 200
        assert check_success.json()["allowed"] is True

    async def test_expired_account_reactivation(self, client: AsyncClient, test_session):
        """Expired account reactivates on admin grant (FR-027)."""
        user_id = "expired-reactivate-user"

        # Create expired account (inactive 400+ days)
        account = TokenAccount(
            user_id=user_id,
            balance=10000,
            last_activity_at=datetime.now(UTC) - timedelta(days=400),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: Request blocked due to expiry
        check_blocked = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("expired-reactivate-req-1"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_blocked.status_code == 402
        assert check_blocked.json()["is_expired"] is True

        # Step 2: Admin grant reactivates
        grant_response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": user_id,
                "credits": 5000,
                "reason": "Reactivation grant",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert grant_response.status_code == 200

        # Step 3: Account should now be active (last_activity_at updated)
        await test_session.refresh(account)
        assert not account.is_expired

        # Step 4: Can now make requests
        check_success = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("expired-reactivate-req-2"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check_success.status_code == 200
        assert check_success.json()["allowed"] is True


class TestIdempotencyJourneys:
    """E2E: Test idempotency in real scenarios."""

    async def test_retry_after_network_timeout(self, client: AsyncClient, test_session):
        """Simulated retry with same request_id should succeed without double-deduct."""
        user_id = "idempotent-retry-user"

        account = TokenAccount(
            user_id=user_id,
            balance=20000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Step 1: Check succeeds
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-retry-req"),
                "estimated_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        reservation_id = check.json()["reservation_id"]

        # Step 2: First deduct (2500i+2500o = 90 credits)
        deduct1 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-retry-req"),
                "reservation_id": reservation_id,
                "input_tokens": 2500,
                "output_tokens": 2500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct1.status_code == 200
        tx_id_1 = deduct1.json()["transaction_id"]
        assert deduct1.json()["status"] == "finalized"

        await test_session.refresh(account)
        balance_after_first = account.balance

        # Step 3: Retry with same request_id (simulating timeout + retry)
        deduct2 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-retry-req"),
                "reservation_id": reservation_id,
                "input_tokens": 2500,
                "output_tokens": 2500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct2.status_code == 200
        assert deduct2.json()["status"] == "already_processed"
        assert deduct2.json()["transaction_id"] == tx_id_1

        # Step 4: Balance should NOT change
        await test_session.refresh(account)
        assert account.balance == balance_after_first

    async def test_duplicate_check_succeeds_in_failopen(
        self, client: AsyncClient, test_session
    ):
        """In fail-open mode (no Redis), duplicate checks both succeed."""
        user_id = "idempotent-check-user"

        account = TokenAccount(
            user_id=user_id,
            balance=30000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # First check
        check1 = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-check-req"),
                "estimated_tokens": 3000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check1.status_code == 200
        res1 = check1.json()["reservation_id"]
        # In test mode, we get failopen_ reservations
        assert res1.startswith("failopen_") or res1.startswith("res_")

        # Duplicate check with same request_id - in fail-open mode, both succeed
        check2 = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("idempotent-check-req"),
                "estimated_tokens": 3000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check2.status_code == 200

    async def test_release_after_finalize_is_idempotent(self, client: AsyncClient, test_session):
        """Releasing after finalize should succeed (idempotent no-op)."""
        user_id = "release-after-finalize-user"

        account = TokenAccount(
            user_id=user_id,
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Check
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("release-after-finalize-req"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        reservation_id = check.json()["reservation_id"]

        # Finalize (deduct)
        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("release-after-finalize-req"),
                "reservation_id": reservation_id,
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200

        # Try to release after already finalized - should succeed (idempotent)
        release = await client.post(
            "/api/v1/metering/release",
            json={
                "user_id": user_id,
                "request_id": make_request_id("release-after-finalize-req"),
                "reservation_id": reservation_id,
            },
            headers={"X-User-ID": user_id},
        )
        assert release.status_code == 200
        assert release.json()["status"] == "released"


class TestNegativeBalanceJourneys:
    """E2E: Test streaming overage handling."""

    async def test_streaming_overage_allows_negative(self, client: AsyncClient, test_session):
        """Finalize can take balance negative (streaming overage scenario)."""
        user_id = "streaming-overage-user"

        # Start with only 2 credits (minimum for pessimistic estimate of 50 tokens)
        account = TokenAccount(
            user_id=user_id,
            balance=2,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Reserve only 50 tokens (estimated) - pessimistic estimate is 2 credits
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("overage-req"),
                "estimated_tokens": 50,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        reservation_id = check.json()["reservation_id"]

        # Finalize with MORE tokens than reserved/available (streaming overage)
        # 5000i+5000o = 180 credits, way more than 2 credit balance
        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("overage-req"),
                "reservation_id": reservation_id,
                "input_tokens": 5000,
                "output_tokens": 5000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200
        assert deduct.json()["credits_deducted"] == 180

        # Balance should be negative: 2 - 180 = -178
        await test_session.refresh(account)
        assert account.balance == 2 - 180

    async def test_negative_balance_blocks_next_request(self, client: AsyncClient, test_session):
        """Negative balance should block subsequent requests."""
        user_id = "negative-blocks-user"

        # User already has negative balance
        account = TokenAccount(
            user_id=user_id,
            balance=-1000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Try to make a request - should be blocked
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("negative-block-req"),
                "estimated_tokens": 100,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 402
        assert check.json()["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_topup_recovers_from_negative(self, client: AsyncClient, test_session):
        """Topup should bring negative balance back to positive."""
        user_id = "negative-topup-user"

        # Start with negative balance
        account = TokenAccount(
            user_id=user_id,
            balance=-2000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Topup
        topup = await client.post(
            "/api/v1/admin/topup",
            json={
                "user_id": user_id,
                "credits": 10000,
                "payment_reference": "NEGATIVE-RECOVERY",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert topup.status_code == 200
        assert topup.json()["new_balance"] == 8000  # -2000 + 10000

        # Can now make requests
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("negative-recovered-req"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        assert check.json()["allowed"] is True


class TestMultiModelJourneys:
    """E2E: Test different model pricing."""

    async def test_different_models_deduct_same_credits(self, client: AsyncClient, test_session):
        """With default pricing, credits_deducted is same regardless of model."""
        user_id = "multi-model-user"

        account = TokenAccount(
            user_id=user_id,
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Request with deepseek-chat (500i+500o = 18 credits with default pricing)
        check1 = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("model-ds-req"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        deduct1 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("model-ds-req"),
                "reservation_id": check1.json()["reservation_id"],
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )

        # Request with a different model (same default pricing in tests)
        check2 = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("model-other-req"),
                "estimated_tokens": 1000,
                "model": "gpt-4o",
            },
            headers={"X-User-ID": user_id},
        )
        deduct2 = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("model-other-req"),
                "reservation_id": check2.json()["reservation_id"],
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "gpt-4o",
            },
            headers={"X-User-ID": user_id},
        )

        # Both use default pricing: 500i+500o = 18 credits
        expected = calculate_expected_credits(500, 500)  # = 18
        assert deduct1.json()["credits_deducted"] == expected
        assert deduct2.json()["credits_deducted"] == expected

    async def test_unknown_model_uses_default_pricing(self, client: AsyncClient, test_session):
        """Unknown model should use default pricing."""
        user_id = "unknown-model-user"

        account = TokenAccount(
            user_id=user_id,
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("unknown-model-req"),
                "estimated_tokens": 2000,
                "model": "totally-fake-model-xyz",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200

        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("unknown-model-req"),
                "reservation_id": check.json()["reservation_id"],
                "input_tokens": 1000,
                "output_tokens": 1000,
                "model": "totally-fake-model-xyz",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200
        # Default pricing: 1000i+1000o = 36 credits
        expected = calculate_expected_credits(1000, 1000)  # = 36
        assert deduct.json()["credits_deducted"] == expected


class TestThreadTracking:
    """E2E: Test conversation/thread tracking."""

    async def test_transactions_grouped_by_thread(self, client: AsyncClient, test_session):
        """Transactions with same thread_id should be retrievable together."""
        user_id = "thread-tracking-user"
        thread_id = "conversation-abc-123"

        account = TokenAccount(
            user_id=user_id,
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Make multiple requests with same thread_id
        for i in range(3):
            check = await client.post(
                "/api/v1/metering/check",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"thread-req-{i}"),
                    "estimated_tokens": 1000,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )
            await client.post(
                "/api/v1/metering/deduct",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"thread-req-{i}"),
                    "reservation_id": check.json()["reservation_id"],
                    "input_tokens": 500,
                    "output_tokens": 500,
                    "model": "deepseek-chat",
                    "thread_id": thread_id,
                },
                headers={"X-User-ID": user_id},
            )

        # Make one request with different thread_id
        check_other = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("thread-other-req"),
                "estimated_tokens": 1000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("thread-other-req"),
                "reservation_id": check_other.json()["reservation_id"],
                "input_tokens": 500,
                "output_tokens": 500,
                "model": "deepseek-chat",
                "thread_id": "different-thread",
            },
            headers={"X-User-ID": user_id},
        )

        # Get transactions filtered by thread_id
        tx_response = await client.get(
            f"/api/v1/transactions?thread_id={thread_id}",
            headers={"X-User-ID": user_id},
        )
        assert tx_response.status_code == 200
        transactions = tx_response.json()["transactions"]

        # Should return only the 3 transactions from our thread
        assert len(transactions) == 3
        for tx in transactions:
            assert tx["thread_id"] == thread_id


class TestBalanceExpiryJourney:
    """E2E: Test inactivity expiry behavior."""

    async def test_expired_user_shows_zero_effective_balance(
        self, client: AsyncClient, test_session
    ):
        """User inactive for 365+ days should have effective_balance=0."""
        user_id = "expired-effective-user"

        # Create expired account
        account = TokenAccount(
            user_id=user_id,
            balance=100000,  # Has balance
            last_activity_at=datetime.now(UTC) - timedelta(days=400),  # Inactive
        )
        test_session.add(account)
        await test_session.commit()

        # Check balance via API
        balance_response = await client.get(
            "/api/v1/balance",
            headers={"X-User-ID": user_id},
        )
        assert balance_response.status_code == 200
        data = balance_response.json()

        # Raw balance preserved, effective is 0
        assert data["balance"] == 100000
        assert data["effective_balance"] == 0
        assert data["is_expired"] is True

    async def test_expired_user_balance_preserved(self, client: AsyncClient, test_session):
        """Raw balance should remain unchanged even when expired."""
        user_id = "expired-preserved-user"

        # Create expired account
        account = TokenAccount(
            user_id=user_id,
            balance=75000,
            last_activity_at=datetime.now(UTC) - timedelta(days=500),
        )
        test_session.add(account)
        await test_session.commit()

        # Verify in DB
        assert account.balance == 75000
        assert account.is_expired is True
        assert account.effective_balance == 0

        # Raw balance field is unchanged
        await test_session.refresh(account)
        assert account.balance == 75000

    async def test_admin_grant_reactivates_expired_account(self, client: AsyncClient, test_session):
        """Admin grant should reset last_activity_at and reactivate (FR-027)."""
        user_id = "expired-reactivate-grant-user"

        # Create expired account
        account = TokenAccount(
            user_id=user_id,
            balance=25000,
            last_activity_at=datetime.now(UTC) - timedelta(days=400),
        )
        test_session.add(account)
        await test_session.commit()

        # Verify initially expired
        assert account.is_expired is True

        # Admin grant
        grant_response = await client.post(
            "/api/v1/admin/grant",
            json={
                "user_id": user_id,
                "credits": 10000,
                "reason": "Re-activation",
            },
            headers={"X-User-ID": "admin", "X-Dev-Admin": "true"},
        )
        assert grant_response.status_code == 200

        # Refresh and check - should be reactivated
        await test_session.refresh(account)
        assert account.is_expired is False
        assert account.balance == 35000  # 25000 + 10000

        # Effective balance should equal raw balance now
        assert account.effective_balance == 35000


class TestConcurrentUsageJourney:
    """E2E: Test concurrent request handling."""

    async def test_multiple_requests_and_finalizations(self, client: AsyncClient, test_session):
        """Multiple requests can be checked and finalized independently."""
        user_id = "concurrent-user"

        account = TokenAccount(
            user_id=user_id,
            balance=100000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Create multiple reservations
        reservations = []
        for i in range(5):
            check = await client.post(
                "/api/v1/metering/check",
                json={
                    "user_id": user_id,
                    "request_id": make_request_id(f"concurrent-req-{i}"),
                    "estimated_tokens": 5000,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )
            assert check.status_code == 200
            req_id = make_request_id(f"concurrent-req-{i}")
            res_id = check.json()["reservation_id"]
            reservations.append((req_id, res_id))

        # Finalize some reservations (2000i+2000o = 72 credits each)
        for request_id, reservation_id in reservations[:3]:
            deduct = await client.post(
                "/api/v1/metering/deduct",
                json={
                    "user_id": user_id,
                    "request_id": request_id,
                    "reservation_id": reservation_id,
                    "input_tokens": 2000,
                    "output_tokens": 2000,
                    "model": "deepseek-chat",
                },
                headers={"X-User-ID": user_id},
            )
            assert deduct.status_code == 200

        # Release remaining reservations
        for request_id, reservation_id in reservations[3:]:
            release = await client.post(
                "/api/v1/metering/release",
                json={
                    "user_id": user_id,
                    "request_id": request_id,
                    "reservation_id": reservation_id,
                },
                headers={"X-User-ID": user_id},
            )
            assert release.status_code == 200

        # Balance should reflect only the 3 finalized deductions
        # 2000i+2000o = 72 credits each, 3 * 72 = 216
        expected_credits = calculate_expected_credits(2000, 2000) * 3  # = 216
        await test_session.refresh(account)
        assert account.balance == 100000 - expected_credits

    async def test_balance_insufficient_for_large_request(self, client: AsyncClient, test_session):
        """Large request that exceeds balance should be blocked."""
        user_id = "large-request-user"

        account = TokenAccount(
            user_id=user_id,
            balance=5,  # Very low in credits
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Request more than available balance
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("large-req"),
                "estimated_tokens": 10000,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 402
        assert check.json()["error_code"] == "INSUFFICIENT_BALANCE"


class TestUsageDetailsJourney:
    """E2E: Test rich usage details tracking."""

    async def test_usage_details_recorded(self, client: AsyncClient, test_session):
        """Usage details should be recorded with transaction."""
        from sqlalchemy import select

        from token_metering_api.models import TokenTransaction

        user_id = "usage-details-user"

        account = TokenAccount(
            user_id=user_id,
            balance=50000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("usage-details-req"),
                "estimated_tokens": 5000,
                "model": "deepseek-reasoner",
            },
            headers={"X-User-ID": user_id},
        )

        # Deduct with rich usage_details
        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("usage-details-req"),
                "reservation_id": check.json()["reservation_id"],
                "input_tokens": 1000,
                "output_tokens": 2000,
                "model": "deepseek-reasoner",
                "usage_details": {
                    "reasoning_tokens": 1500,
                    "cached_tokens": 200,
                    "requests_made": 1,
                },
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200

        # Verify in database
        result = await test_session.execute(
            select(TokenTransaction).where(
                TokenTransaction.request_id == make_request_id("usage-details-req")
            )
        )
        tx = result.scalar_one()
        assert tx.extra_data is not None
        assert tx.extra_data.get("usage_details", {}).get("reasoning_tokens") == 1500


class TestCheckDeductConsistency:
    """E2E: Verify check→deduct credit consistency (pessimistic >= actual)."""

    async def test_reserved_credits_match_pessimistic_and_deducted_lte_reserved(
        self, client: AsyncClient, test_session
    ):
        """Check returns pessimistic estimate, deduct returns actual, actual <= reserved."""
        user_id = "consistency-user"

        account = TokenAccount(
            user_id=user_id,
            balance=100_000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        estimated_tokens = 3000
        input_tokens = 1200
        output_tokens = 1800

        # Step 1: Check — reserved_credits should match pessimistic estimate
        check = await client.post(
            "/api/v1/metering/check",
            json={
                "user_id": user_id,
                "request_id": make_request_id("consistency-req"),
                "estimated_tokens": estimated_tokens,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert check.status_code == 200
        check_data = check.json()
        reserved_credits = check_data["reserved_credits"]
        expected_reserved = estimate_credits_pessimistic(estimated_tokens)
        assert reserved_credits == expected_reserved

        # Step 2: Deduct — credits_deducted should match actual calculation
        deduct = await client.post(
            "/api/v1/metering/deduct",
            json={
                "user_id": user_id,
                "request_id": make_request_id("consistency-req"),
                "reservation_id": check_data["reservation_id"],
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "model": "deepseek-chat",
            },
            headers={"X-User-ID": user_id},
        )
        assert deduct.status_code == 200
        deduct_data = deduct.json()
        credits_deducted = deduct_data["credits_deducted"]
        expected_deducted = calculate_expected_credits(input_tokens, output_tokens)
        assert credits_deducted == expected_deducted

        # Step 3: Pessimistic reservation >= actual deduction
        assert credits_deducted <= reserved_credits, (
            f"Deducted {credits_deducted} > reserved {reserved_credits} — "
            "pessimistic estimate failed to cover actual usage"
        )
