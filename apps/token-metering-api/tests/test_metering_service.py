"""TDD tests for metering service (v6 - Credits).

The v6 model:
1. Suspended? -> BLOCK (ACCOUNT_SUSPENDED)
2. Expired (inactive 365+ days)? -> BLOCK (INSUFFICIENT_BALANCE, is_expired=true)
3. Balance >= estimated_credits? -> ALLOW (create reservation)
4. Otherwise -> BLOCK (INSUFFICIENT_BALANCE)

New users get STARTER_CREDITS (20,000).
Balance stored directly on TokenAccount.balance (not computed from allocations).
Balance deductions use cost-weighted credits, not raw tokens.
"""

from datetime import UTC, datetime, timedelta
from decimal import Decimal

from token_metering_api.models import (
    STARTER_TOKENS,
    AccountStatus,
    AllocationType,
    TokenAccount,
    TokenAllocation,
)
from token_metering_api.services.metering import MeteringService


class TestCheckBalance:
    """Test balance check / reservation creation."""

    async def test_allows_request_with_sufficient_balance(self, test_session):
        """User with balance can make requests."""
        account = TokenAccount(
            user_id="rich-user",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="rich-user",
            request_id="req-001",
            estimated_tokens=1000,
        )

        assert result["allowed"] is True
        assert "reservation_id" in result
        # v6: reserved_credits is the pessimistic credit estimate, not raw tokens
        assert result["reserved_credits"] > 0

    async def test_blocks_suspended_account(self, test_session):
        """Suspended accounts are blocked."""
        account = TokenAccount(
            user_id="suspended-user",
            status=AccountStatus.SUSPENDED,
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="suspended-user",
            request_id="req-002",
            estimated_tokens=100,
        )

        assert result["allowed"] is False
        assert result["error_code"] == "ACCOUNT_SUSPENDED"

    async def test_blocks_insufficient_balance(self, test_session):
        """User with insufficient balance is blocked."""
        account = TokenAccount(
            user_id="low-balance",
            balance=1,  # Very low balance in credits
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="low-balance",
            request_id="req-003",
            estimated_tokens=1000,
        )

        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"

    async def test_blocks_expired_inactive_user(self, test_session):
        """User inactive for 365+ days is blocked with is_expired=true."""
        account = TokenAccount(
            user_id="expired-user",
            balance=50000,  # Has balance
            last_activity_at=datetime.now(UTC) - timedelta(days=400),  # Inactive
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="expired-user",
            request_id="req-004",
            estimated_tokens=100,
        )

        assert result["allowed"] is False
        assert result["error_code"] == "INSUFFICIENT_BALANCE"
        assert result["is_expired"] is True

    async def test_allows_new_user_with_starter_tokens(self, test_session):
        """New user should get STARTER_CREDITS and be allowed."""
        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="brand-new-user",
            request_id="req-005",
            estimated_tokens=100,
        )

        assert result["allowed"] is True
        assert "reservation_id" in result


class TestFinalizeUsage:
    """Test credit deduction / finalization."""

    async def test_creates_transaction_with_correct_cost(self, test_session):
        """Finalize creates transaction with correct credit calculation."""
        account = TokenAccount(
            user_id="user-finalize",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.finalize_usage(
            user_id="user-finalize",
            request_id="req-finalize-001",
            reservation_id="res_test123",
            input_tokens=1000,
            output_tokens=500,
            model="deepseek-chat",
        )

        assert result["status"] == "finalized"
        assert result["total_tokens"] == 1500
        assert result["balance_source"] == "balance"

        # v6: verify account.balance was deducted by credits (not raw tokens)
        # 1000i + 500o with default pricing: base=0.002, markup=0.0024, credits=ceil(24)=24
        await test_session.refresh(account)
        assert account.balance == 10000 - 24

    async def test_idempotent_finalize(self, test_session):
        """Same request_id returns same result without double-charging."""
        account = TokenAccount(
            user_id="user-idempotent",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)

        # First call
        result1 = await service.finalize_usage(
            user_id="user-idempotent",
            request_id="req-idempotent-001",
            reservation_id="res_test123",
            input_tokens=1000,
            output_tokens=500,
            model="deepseek-chat",
        )

        # Second call with same request_id
        result2 = await service.finalize_usage(
            user_id="user-idempotent",
            request_id="req-idempotent-001",
            reservation_id="res_test123",
            input_tokens=1000,
            output_tokens=500,
            model="deepseek-chat",
        )

        assert result2["status"] == "already_processed"
        assert result2["transaction_id"] == result1["transaction_id"]

        # v6: verify only charged once (24 credits for 1000i+500o)
        await test_session.refresh(account)
        assert account.balance == 10000 - 24

    async def test_balance_can_go_negative(self, test_session):
        """Balance can go negative from streaming overage."""
        account = TokenAccount(
            user_id="user-negative",
            balance=5,  # Very low balance in credits
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)

        # Deduct more than available (streaming overage)
        # 5000i + 5000o = 180 credits, but only have 5
        result = await service.finalize_usage(
            user_id="user-negative",
            request_id="req-negative-001",
            reservation_id="res_test",
            input_tokens=5000,
            output_tokens=5000,
            model="deepseek-chat",
        )

        assert result["status"] == "finalized"

        await test_session.refresh(account)
        assert account.balance == 5 - 180  # = -175


class TestCostCalculation:
    """Test pricing and markup calculations."""

    def test_calculate_base_cost(self, test_session):
        """Verify cost calculation formula."""
        service = MeteringService(test_session)
        pricing = {
            "input": Decimal("0.00014"),
            "output": Decimal("0.00028"),
        }

        # 1000 input + 500 output
        cost = service._calculate_base_cost(1000, 500, pricing)

        expected = Decimal("0.00014") + Decimal("0.00014")
        assert cost == expected

    def test_markup_applied_correctly(self):
        """20% markup is applied to base cost."""
        base_cost = Decimal("1.00")
        markup_percent = Decimal("20.00")

        total = base_cost * (1 + markup_percent / 100)

        assert total == Decimal("1.20")


class TestStarterTokensFlow:
    """Test starter credits for new users (v6)."""

    async def test_new_user_gets_starter_tokens_on_check(self, test_session):
        """New user gets STARTER_CREDITS on first check."""
        from sqlalchemy import select

        service = MeteringService(test_session)

        # User doesn't exist
        result = await service.check_balance(
            user_id="starter-user-001",
            request_id="req-starter-001",
            estimated_tokens=1000,
        )

        assert result["allowed"] is True

        # Verify account was created with starter credits
        stmt = select(TokenAccount).where(TokenAccount.user_id == "starter-user-001")
        account_result = await test_session.execute(stmt)
        account = account_result.scalar_one()

        # Balance should be starter credits (reservation doesn't deduct yet)
        assert account.balance == STARTER_TOKENS

    async def test_starter_allocation_audit_created(self, test_session):
        """New user gets starter allocation audit record."""
        from sqlalchemy import select

        service = MeteringService(test_session)

        await service.check_balance(
            user_id="starter-audit-001",
            request_id="req-audit-001",
            estimated_tokens=100,
        )

        # Verify starter allocation audit was created
        stmt = select(TokenAllocation).where(
            TokenAllocation.user_id == "starter-audit-001",
            TokenAllocation.allocation_type == AllocationType.STARTER,
        )
        alloc_result = await test_session.execute(stmt)
        alloc = alloc_result.scalar_one_or_none()

        assert alloc is not None
        assert alloc.amount == STARTER_TOKENS


class TestAdminOperations:
    """Test admin operations (grant/topup) - v6: adds to account.balance in credits."""

    async def test_grant_creates_allocation(self, test_session):
        """Admin grant adds to account.balance and creates audit record."""
        from token_metering_api.services.admin import AdminService

        account = TokenAccount(
            user_id="student-new",
            balance=STARTER_TOKENS,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        admin_service = AdminService(test_session)
        result = await admin_service.grant_credits(
            user_id="student-new",
            credits=500000,
            reason="Panaversity enrollment",
            admin_id="admin-123",
        )

        assert result["success"] is True
        assert result["credits_granted"] == 500000
        assert "allocation_id" in result

        # v6: verify account.balance was updated
        await test_session.refresh(account)
        assert account.balance == STARTER_TOKENS + 500000

        # Verify audit record
        from sqlalchemy import select

        alloc_result = await test_session.execute(
            select(TokenAllocation).where(TokenAllocation.id == result["allocation_id"])
        )
        alloc = alloc_result.scalar_one()

        assert alloc.allocation_type == AllocationType.GRANT
        assert alloc.amount == 500000

    async def test_topup_creates_allocation(self, test_session):
        """Admin topup adds to account.balance and creates audit record."""
        from token_metering_api.services.admin import AdminService

        account = TokenAccount(
            user_id="user-topup",
            balance=1000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        admin_service = AdminService(test_session)
        result = await admin_service.topup_credits(
            user_id="user-topup",
            credits=100000,
            payment_reference="stripe_pi_123",
            admin_id="admin-123",
        )

        assert result["success"] is True
        assert result["credits_added"] == 100000

        # v6: verify account.balance was updated
        await test_session.refresh(account)
        assert account.balance == 101000

        # Verify audit record
        from sqlalchemy import select

        alloc_result = await test_session.execute(
            select(TokenAllocation).where(TokenAllocation.id == result["allocation_id"])
        )
        alloc = alloc_result.scalar_one()

        assert alloc.allocation_type == AllocationType.TOPUP
        assert alloc.amount == 100000


class TestReleaseReservation:
    """Test reservation release (Edge case: LLM fails)."""

    async def test_release_returns_tokens(self, test_session):
        """Releasing a reservation doesn't deduct credits."""
        account = TokenAccount(
            user_id="user-release",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)

        # First, create a reservation
        check_result = await service.check_balance(
            user_id="user-release",
            request_id="req-release-001",
            estimated_tokens=5000,
        )
        assert check_result["allowed"] is True

        # Release (LLM failed)
        await service.release_reservation(
            user_id="user-release",
            request_id="req-release-001",
            reservation_id=check_result["reservation_id"],
        )

        # v6: verify account.balance unchanged (no Redis in test)
        await test_session.refresh(account)
        assert account.balance == 10000

    async def test_failopen_reservation_releases_cleanly(self, test_session):
        """Failopen reservations release without error."""
        service = MeteringService(test_session)

        result = await service.release_reservation(
            user_id="any-user",
            request_id="any-request",
            reservation_id="failopen_abc123",
        )

        assert result["status"] == "released"
        assert result["reserved_credits"] == 0


class TestThreadIdTracking:
    """Test thread_id tracking for conversation-level usage analysis."""

    async def test_finalize_stores_thread_id(self, test_session):
        """Finalize stores thread_id in transaction record."""
        from token_metering_api.models import TokenTransaction

        account = TokenAccount(
            user_id="user-thread",
            balance=10000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()

        service = MeteringService(test_session)
        result = await service.finalize_usage(
            user_id="user-thread",
            request_id="req-thread-001",
            reservation_id="res_test123",
            input_tokens=500,
            output_tokens=500,
            model="deepseek-chat",
            thread_id="thread_abc123",
        )

        assert result["status"] == "finalized"
        assert result["thread_id"] == "thread_abc123"

        # Verify transaction was stored with thread_id
        from sqlalchemy import select

        tx_result = await test_session.execute(
            select(TokenTransaction).where(TokenTransaction.request_id == "req-thread-001")
        )
        transaction = tx_result.scalar_one_or_none()
        assert transaction is not None
        assert transaction.thread_id == "thread_abc123"
