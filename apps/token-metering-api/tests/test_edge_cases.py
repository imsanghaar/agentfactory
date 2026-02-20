"""Edge case tests for token metering model (v5 - Balance Only).

v5 model logic:
1. Suspended account -> blocked (ACCOUNT_SUSPENDED)
2. Expired (inactive 365+ days) -> blocked (INSUFFICIENT_BALANCE, is_expired=true)
3. Balance >= estimated_tokens -> allowed (create reservation)
4. Otherwise -> blocked (INSUFFICIENT_BALANCE)

Balance stored directly on TokenAccount.balance.
No trial tracking - new users get STARTER_TOKENS (50,000).
"""

from datetime import UTC, datetime, timedelta

from sqlalchemy import select

from token_metering_api.models import (
    INACTIVITY_EXPIRY_DAYS,
    STARTER_TOKENS,
    AccountStatus,
    TokenAccount,
)
from token_metering_api.services.metering import MeteringService


class TestEdgeCases:
    """Tests for spec-defined edge cases."""

    async def test_zero_token_request(self, test_session):
        """Zero token request should be allowed (no cost)."""
        account = TokenAccount(
            user_id="edge-zero",
            balance=100,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="edge-zero",
            request_id="req-zero",
            estimated_tokens=0,
        )

        assert result["allowed"] is True

    async def test_exact_balance_amount(self, test_session):
        """Request for exact balance amount should be allowed."""
        account = TokenAccount(
            user_id="edge-exact",
            balance=1000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="edge-exact",
            request_id="req-exact",
            estimated_tokens=1000,
        )

        assert result["allowed"] is True

    async def test_one_credit_under_estimate_blocked(self, test_session):
        """Balance 1 credit below pessimistic estimate should be blocked."""
        from tests.helpers import estimate_credits_pessimistic

        estimated_credits = estimate_credits_pessimistic(1000)
        account = TokenAccount(
            user_id="edge-over",
            balance=estimated_credits - 1,  # 1 credit short
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="edge-over",
            request_id="req-over",
            estimated_tokens=1000,
        )

        # v6: Blocked because balance < estimated_credits
        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_large_token_request(self, test_session):
        """Large token request within model limits handles correctly.

        Note: FR-069 limits estimated_tokens to model's max_tokens (128k default).
        This test uses a large but valid request amount.
        """
        account = TokenAccount(
            user_id="edge-large",
            balance=200_000,  # 200k tokens
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="edge-large",
            request_id="req-large",
            estimated_tokens=128_000,  # Max allowed by default (FR-069)
        )

        assert result["allowed"] is True

    async def test_multiple_consecutive_requests_drain_balance(self, test_session):
        """Multiple requests drain balance correctly (v6: credits deducted)."""
        from tests.helpers import calculate_expected_credits

        credits_per_deduct = calculate_expected_credits(500, 500)  # = 18
        initial_balance = credits_per_deduct * 3  # Exactly enough for 3 deductions

        account = TokenAccount(
            user_id="edge-multi",
            balance=initial_balance,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)

        # Request 1: 500i+500o
        await service.finalize_usage(
            user_id="edge-multi",
            request_id="req-multi-1",
            reservation_id="res_1",
            input_tokens=500,
            output_tokens=500,
            model="deepseek-chat",
        )

        await test_session.refresh(account)
        assert account.balance == initial_balance - credits_per_deduct

        # Request 2: 500i+500o
        await service.finalize_usage(
            user_id="edge-multi",
            request_id="req-multi-2",
            reservation_id="res_2",
            input_tokens=500,
            output_tokens=500,
            model="deepseek-chat",
        )

        await test_session.refresh(account)
        assert account.balance == initial_balance - 2 * credits_per_deduct

        # Request 3: 500i+500o
        await service.finalize_usage(
            user_id="edge-multi",
            request_id="req-multi-3",
            reservation_id="res_3",
            input_tokens=500,
            output_tokens=500,
            model="deepseek-chat",
        )

        await test_session.refresh(account)
        assert account.balance == 0

        # Request 4: No balance, should be blocked
        result = await service.check_balance(
            user_id="edge-multi",
            request_id="req-multi-4",
            estimated_tokens=1000,
        )
        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_balance_can_go_negative_from_streaming(self, test_session):
        """Balance can go negative from streaming overage (v5)."""
        account = TokenAccount(
            user_id="edge-negative",
            balance=100,  # Only 100 tokens
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)

        # Deduct more than available (streaming overage scenario)
        await service.finalize_usage(
            user_id="edge-negative",
            request_id="req-negative",
            reservation_id="res_1",
            input_tokens=1000,
            output_tokens=500,  # Total 1500, but only had 100
            model="deepseek-chat",
        )

        await test_session.refresh(account)
        # v6: balance can go negative (in credits)
        from tests.helpers import calculate_expected_credits

        expected_credits = calculate_expected_credits(1000, 500)
        assert account.balance == 100 - expected_credits

    async def test_suspended_account_blocked(self, test_session):
        """Suspended account is always blocked, regardless of balance."""
        account = TokenAccount(
            user_id="edge-suspended",
            status=AccountStatus.SUSPENDED,
            balance=1_000_000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="edge-suspended",
            request_id="req-suspended",
            estimated_tokens=1,  # Even tiny request
        )

        assert result["allowed"] is False
        assert result["error_code"] == "ACCOUNT_SUSPENDED"

    async def test_unknown_model_uses_default_pricing(self, test_session):
        """Unknown model falls back to default pricing."""
        account = TokenAccount(
            user_id="edge-model",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.finalize_usage(
            user_id="edge-model",
            request_id="req-model",
            reservation_id="res_1",
            input_tokens=1000,
            output_tokens=500,
            model="unknown-model-xyz",  # Unknown model
        )

        # Should still work with default pricing
        assert result["status"] == "finalized"
        assert result["total_tokens"] == 1500


class TestInactivityExpiry:
    """Test inactivity-based balance expiry (v5)."""

    async def test_inactive_user_blocked_with_is_expired(self, test_session):
        """User inactive for 365+ days is blocked with is_expired=true."""
        account = TokenAccount(
            user_id="inactive-test",
            balance=50000,  # Has balance
            last_activity_at=datetime.now(UTC) - timedelta(days=400),  # Inactive
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="inactive-test",
            request_id="req-inactive",
            estimated_tokens=1000,
        )

        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"
        assert result["is_expired"] is True

    async def test_user_at_expiry_boundary_allowed(self, test_session):
        """User at exactly 364 days is still allowed (not expired)."""
        account = TokenAccount(
            user_id="boundary-test",
            balance=50000,
            last_activity_at=datetime.now(UTC) - timedelta(days=364),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="boundary-test",
            request_id="req-boundary",
            estimated_tokens=1000,
        )

        assert result["allowed"] is True

    async def test_user_at_exactly_365_days_expired(self, test_session):
        """User at exactly 365 days is expired."""
        account = TokenAccount(
            user_id="exact-365",
            balance=50000,
            last_activity_at=datetime.now(UTC) - timedelta(days=INACTIVITY_EXPIRY_DAYS),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="exact-365",
            request_id="req-365",
            estimated_tokens=1000,
        )

        assert result["allowed"] is False
        assert result["is_expired"] is True


class TestNegativeBalance:
    """Test negative balance handling (v5)."""

    async def test_negative_balance_user_blocked(self, test_session):
        """User with negative balance is blocked."""
        account = TokenAccount(
            user_id="negative-check",
            balance=-500,  # Negative from streaming overage
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="negative-check",
            request_id="req-neg",
            estimated_tokens=100,
        )

        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_negative_balance_recovery_with_topup(self, test_session):
        """User can recover from negative balance with topup."""
        from token_metering_api.services.admin import AdminService

        account = TokenAccount(
            user_id="negative-recover",
            balance=-500,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        # Top up more than the deficit
        admin_service = AdminService(test_session)
        await admin_service.topup_credits(
            user_id="negative-recover",
            credits=1000,
            payment_reference="recovery-payment",
            admin_id="admin",
        )

        await test_session.refresh(account)
        assert account.balance == 500  # -500 + 1000 = 500

        # Now should be allowed
        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="negative-recover",
            request_id="req-recover",
            estimated_tokens=100,
        )

        assert result["allowed"] is True


class TestStarterTokens:
    """Test starter tokens for new users (v5)."""

    async def test_new_user_gets_starter_tokens(self, test_session):
        """New user auto-created with STARTER_TOKENS."""
        service = MeteringService(test_session)

        # User doesn't exist, will be auto-created with STARTER_TOKENS
        result = await service.check_balance(
            user_id="brand-new-starter",
            request_id="req-new",
            estimated_tokens=100,
        )

        assert result["allowed"] is True

        # Verify account was created with starter tokens
        stmt = select(TokenAccount).where(TokenAccount.user_id == "brand-new-starter")
        account_result = await test_session.execute(stmt)
        account = account_result.scalar_one()

        # Balance is full STARTER_TOKENS - reservations don't deduct from balance
        # (they use Redis ZSET, deduction happens on finalize)
        assert account.balance == STARTER_TOKENS

    async def test_starter_credits_allows_max_token_request(self, test_session):
        """New user can make max-token request (estimate << starter credits)."""
        service = MeteringService(test_session)

        # With credits model, even 128k tokens only costs ~3072 credits
        # which is well under 20,000 starter credits
        result = await service.check_balance(
            user_id="starter-large-req",
            request_id="req-large",
            estimated_tokens=128_000,  # Max tokens, still affordable
        )

        assert result["allowed"] is True

    async def test_starter_credits_blocks_when_depleted(self, test_session):
        """User with depleted starter credits is blocked."""
        from tests.helpers import estimate_credits_pessimistic

        # Create user with balance just under the estimate for 1000 tokens
        estimated = estimate_credits_pessimistic(1000)
        account = TokenAccount(
            user_id="starter-over-req",
            balance=estimated - 1,  # 1 credit short
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="starter-over-req",
            request_id="req-over",
            estimated_tokens=1000,
        )

        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"


class TestCostTracking:
    """Test cost calculation and tracking."""

    async def test_transaction_records_markup(self, test_session):
        """Transaction records 20% markup correctly."""
        from token_metering_api.models import TokenTransaction

        account = TokenAccount(
            user_id="cost-markup",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        await service.finalize_usage(
            user_id="cost-markup",
            request_id="req-cost",
            reservation_id="res_1",
            input_tokens=1000,
            output_tokens=1000,
            model="deepseek-chat",
        )

        # Verify transaction
        tx_result = await test_session.execute(
            select(TokenTransaction).where(TokenTransaction.request_id == "req-cost")
        )
        tx = tx_result.scalar_one()

        assert tx.markup_percent == 20
        assert tx.total_cost_usd > tx.base_cost_usd
        # total = base * 1.20
        expected_total = tx.base_cost_usd * (1 + tx.markup_percent / 100)
        assert abs(tx.total_cost_usd - expected_total) < 0.000001
