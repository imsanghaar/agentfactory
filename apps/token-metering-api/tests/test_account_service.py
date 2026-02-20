"""TDD tests for AccountService (v5 - Balance Only).

Tests for the extracted AccountService which handles:
1. get_or_create - Get existing account or create with starter tokens
2. invalidate_balance_cache - Clear cached balance data from Redis
"""

from datetime import UTC, datetime

from token_metering_api.config import settings
from token_metering_api.models import (
    AccountStatus,
    AllocationType,
    TokenAccount,
    TokenAllocation,
    TokenTransaction,
    TransactionType,
)


class TestAccountServiceGetOrCreate:
    """Test AccountService.get_or_create method."""

    async def test_returns_existing_account(self, test_session):
        """Should return existing account without modification."""
        # Setup: Create existing account
        account = TokenAccount(
            user_id="existing-user-001",
            balance=75000,
            last_activity_at=datetime.now(UTC),
        )
        test_session.add(account)
        await test_session.commit()
        await test_session.refresh(account)
        original_id = account.id

        # Import after setting up fixtures to avoid circular imports
        from token_metering_api.services.account import AccountService

        service = AccountService(test_session)
        result = await service.get_or_create("existing-user-001")

        # Should return the same account
        assert result.id == original_id
        assert result.balance == 75000
        assert result.user_id == "existing-user-001"

    async def test_creates_new_account_with_starter_tokens(self, test_session):
        """New user should get STARTER_TOKENS."""
        from token_metering_api.services.account import AccountService

        service = AccountService(test_session)
        result = await service.get_or_create("brand-new-user-001")

        assert result.user_id == "brand-new-user-001"
        assert result.balance == settings.starter_credits
        assert result.status == AccountStatus.ACTIVE
        assert result.last_activity_at is not None

    async def test_creates_starter_allocation_audit(self, test_session):
        """New user should have starter allocation audit record."""
        from sqlalchemy import select

        from token_metering_api.services.account import AccountService

        service = AccountService(test_session)
        await service.get_or_create("audit-user-001")

        # Verify allocation audit record
        stmt = select(TokenAllocation).where(
            TokenAllocation.user_id == "audit-user-001",
            TokenAllocation.allocation_type == AllocationType.STARTER,
        )
        result = await test_session.execute(stmt)
        allocation = result.scalar_one_or_none()

        assert allocation is not None
        assert allocation.amount == settings.starter_credits

    async def test_creates_starter_transaction(self, test_session):
        """New user should have starter transaction record."""
        from sqlalchemy import select

        from token_metering_api.services.account import AccountService

        service = AccountService(test_session)
        await service.get_or_create("transaction-user-001")

        # Verify transaction record
        stmt = select(TokenTransaction).where(
            TokenTransaction.user_id == "transaction-user-001",
            TokenTransaction.transaction_type == TransactionType.STARTER,
        )
        result = await test_session.execute(stmt)
        transaction = result.scalar_one_or_none()

        assert transaction is not None
        assert transaction.total_tokens == settings.starter_credits

    async def test_idempotent_create(self, test_session):
        """Multiple calls for same user should return same account."""
        from token_metering_api.services.account import AccountService

        service = AccountService(test_session)

        # First call creates
        result1 = await service.get_or_create("idempotent-user-001")
        # Second call returns existing
        result2 = await service.get_or_create("idempotent-user-001")

        assert result1.id == result2.id
        assert result1.balance == result2.balance


class TestAccountServiceInvalidateCache:
    """Test AccountService.invalidate_balance_cache method."""

    async def test_invalidate_cache_without_redis(self, test_session):
        """Should not raise when Redis is not available."""
        from token_metering_api.services.account import AccountService

        service = AccountService(test_session)
        # Should not raise even without Redis
        await service.invalidate_balance_cache("any-user")

    async def test_invalidate_cache_function(self, test_session):
        """Test standalone invalidate_balance_cache function."""
        from token_metering_api.services.account import invalidate_balance_cache

        # Should not raise even without Redis
        await invalidate_balance_cache(None, "any-user")


class TestAccountServiceIntegration:
    """Integration tests with MeteringService and AdminService."""

    async def test_metering_service_uses_account_service(self, test_session):
        """MeteringService should use AccountService internally."""
        from token_metering_api.services.metering import MeteringService

        service = MeteringService(test_session)
        result = await service.check_balance(
            user_id="metering-test-001",
            request_id="req-001",
            estimated_tokens=1000,
        )

        # Should have created account via AccountService
        assert result["allowed"] is True

    async def test_admin_service_uses_account_service(self, test_session):
        """AdminService should use AccountService internally."""
        from token_metering_api.services.admin import AdminService

        service = AdminService(test_session)
        result = await service.grant_credits(
            user_id="admin-test-001",
            credits=10000,
            reason="Test grant",
            admin_id="admin-001",
        )

        # Should have created account via AccountService
        assert result["success"] is True
        # Account should have starter tokens + grant
        assert result["new_balance"] == settings.starter_credits + 10000
