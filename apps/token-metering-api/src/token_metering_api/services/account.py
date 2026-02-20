"""Account service for token account management (v6 - Credits).

Extracts shared account logic from MeteringService and AdminService:
- get_or_create: Get or create account with starter credits
- invalidate_balance_cache: Clear Redis cache for user balance

FR references:
- FR-011: Auto-create account on first interaction
- FR-012: New accounts get STARTER_CREDITS
- FR-029: Set last_activity_at on creation
- FR-056: Cache invalidation
"""

import logging
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from redis.asyncio import Redis
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..config import settings
from ..core.redis import get_redis
from ..models import (
    TokenAccount,
    TokenAllocation,
    TokenTransaction,
    TransactionType,
)

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

# Cache key prefix for balance data
BALANCE_CACHE_PREFIX = "metering:balance:"


async def invalidate_balance_cache(redis: Redis | None, user_id: str) -> None:
    """Invalidate cached balance data for a user (FR-056).

    Standalone function for use without AccountService instance.

    Args:
        redis: Redis client (can be None if Redis unavailable)
        user_id: User whose cache should be invalidated
    """
    if redis:
        cache_key = f"{BALANCE_CACHE_PREFIX}{user_id}"
        await redis.delete(cache_key)
        logger.debug(f"[Account] Invalidated cache for {user_id}")


class AccountService:
    """Service for token account management operations.

    Centralizes account creation and cache management logic
    previously duplicated in MeteringService and AdminService.
    """

    def __init__(self, session: AsyncSession, redis: Redis | None = None):
        """Initialize AccountService.

        Args:
            session: Database session for account operations
            redis: Optional Redis client (defaults to global instance)
        """
        self.session = session
        self.redis = redis if redis is not None else get_redis()

    async def get_or_create(self, user_id: str) -> TokenAccount:
        """Get existing account or create new one with STARTER_CREDITS.

        FR-011: Auto-create account on first interaction
        FR-012: New accounts get STARTER_CREDITS (configurable via settings)
        FR-029: Set last_activity_at on creation

        Handles race conditions by catching IntegrityError on concurrent creates
        and retrying the lookup.

        Args:
            user_id: Unique user identifier

        Returns:
            TokenAccount: Existing or newly created account
        """
        result = await self.session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one_or_none()

        if not account:
            try:
                account = await self._create_new_account(user_id)
            except IntegrityError:
                # Another request created the account concurrently - rollback and fetch
                await self.session.rollback()
                result = await self.session.execute(
                    select(TokenAccount).where(TokenAccount.user_id == user_id)
                )
                account = result.scalar_one_or_none()
                if not account:
                    # Should not happen, but re-raise if it does
                    raise RuntimeError(
                        f"Account for {user_id} not found after IntegrityError"
                    )
                logger.debug(
                    f"[Account] Recovered from race condition for {user_id}"
                )

        return account

    async def _create_new_account(self, user_id: str) -> TokenAccount:
        """Create a new account with starter credits.

        Creates:
        1. TokenAccount with starter_credits balance
        2. TokenAllocation audit record (STARTER type)
        3. TokenTransaction record for ledger completeness

        Args:
            user_id: Unique user identifier

        Returns:
            TokenAccount: Newly created account
        """
        now = datetime.now(UTC)

        # Create account with starter credits
        account = TokenAccount(
            user_id=user_id,
            balance=settings.starter_credits,
            last_activity_at=now,  # FR-029
            created_at=now,
            updated_at=now,
        )
        self.session.add(account)

        # Create starter allocation audit record (FR-012)
        allocation = TokenAllocation.create_starter(
            user_id=user_id, amount=settings.starter_credits
        )
        self.session.add(allocation)

        # Create starter transaction for ledger completeness
        transaction = TokenTransaction(
            user_id=user_id,
            transaction_type=TransactionType.STARTER,
            total_tokens=settings.starter_credits,
            extra_data={"reason": "Initial starter credits for new user"},
        )
        self.session.add(transaction)

        await self.session.commit()
        await self.session.refresh(account)

        logger.info(
            f"[Account] Created new account for {user_id} "
            f"with {settings.starter_credits} starter credits"
        )

        return account

    async def invalidate_balance_cache(self, user_id: str) -> None:
        """Invalidate cached balance data for a user (FR-056).

        Args:
            user_id: User whose cache should be invalidated
        """
        await invalidate_balance_cache(self.redis, user_id)
