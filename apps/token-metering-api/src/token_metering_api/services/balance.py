"""Balance query service (v6 - Credits).

v6 Changes:
- Balance read directly from TokenAccount.balance in credits (O(1))
- Uses effective_balance property for inactivity expiry
- TokenAllocation queries are for audit history only
"""

import json
import logging
from typing import Any

from redis.asyncio import Redis
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.cache import BALANCE_CACHE_TTL_SECONDS, BALANCE_KEY_PREFIX
from ..models import (
    TokenAccount,
    TokenAllocation,
    TokenTransaction,
    TransactionType,
)

logger = logging.getLogger(__name__)


class BalanceService:
    """Service for balance queries and transaction history (v6 - Credits)."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_balance(
        self, user_id: str, redis: Redis | None = None
    ) -> dict[str, Any] | None:
        """
        Get user's balance and usage information (v5 - O(1) read).

        Reads balance directly from TokenAccount (FR-004, FR-007).
        Uses effective_balance for inactivity expiry check (FR-026).
        Checks Redis cache first if available.
        """
        # 1. Check Redis cache first
        if redis is None:
            logger.debug("[Cache] Redis not available for balance lookup")
        else:
            try:
                cached = await redis.get(f"{BALANCE_KEY_PREFIX}{user_id}")
                if cached is not None:
                    logger.info(f"[Cache] Balance cache hit for {user_id}")
                    return json.loads(cached)
                logger.info(f"[Cache] Balance cache miss for {user_id}")
            except Exception as e:
                logger.warning(f"[Cache] Failed to read balance for {user_id}: {e}")

        # 2. Cache miss → query DB
        result = await self.session.execute(
            select(TokenAccount).where(TokenAccount.user_id == user_id)
        )
        account = result.scalar_one_or_none()

        if not account:
            return None

        # v6: Use effective_balance (respects inactivity expiry)
        effective_balance = account.effective_balance

        balance_dict = {
            "user_id": account.user_id,
            "status": account.status.value,
            "balance": account.balance,  # Actual stored balance
            "effective_balance": effective_balance,  # 0 if expired
            "last_activity_at": account.last_activity_at.isoformat()
            if account.last_activity_at
            else None,
            "is_expired": account.is_expired,
        }

        # 3. Cache the response dict
        if redis is not None:
            try:
                cache_key = f"{BALANCE_KEY_PREFIX}{user_id}"
                cache_value = json.dumps(balance_dict)
                ttl = BALANCE_CACHE_TTL_SECONDS
                await redis.setex(cache_key, ttl, cache_value)
                logger.info(
                    f"[Cache] Cached balance for {user_id} "
                    f"(key={cache_key}, ttl={ttl}s)"
                )
            except Exception as e:
                logger.warning(f"[Cache] Failed to cache balance for {user_id}: {e}")

        return balance_dict

    async def get_allocations(self, user_id: str) -> list[dict[str, Any]]:
        """
        Get all allocations for a user (audit history - FR-008, FR-031).

        Allocations are audit records only (no remaining_amount or expires_at).
        """
        result = await self.session.execute(
            select(TokenAllocation)
            .where(TokenAllocation.user_id == user_id)
            .order_by(TokenAllocation.created_at.desc())
        )
        allocations = result.scalars().all()

        return [
            {
                "id": alloc.id,
                "allocation_type": alloc.allocation_type.value,
                "amount": alloc.amount,
                "reason": alloc.reason,
                "admin_id": alloc.admin_id,
                "payment_reference": alloc.payment_reference,
                "created_at": alloc.created_at.isoformat(),
            }
            for alloc in allocations
        ]

    async def get_transactions(
        self,
        user_id: str,
        limit: int = 50,
        offset: int = 0,
        transaction_type: TransactionType | None = None,
        thread_id: str | None = None,
    ) -> dict[str, Any]:
        """Get paginated transaction history (FR-015)."""
        # Build query
        query = select(TokenTransaction).where(TokenTransaction.user_id == user_id)

        if transaction_type:
            query = query.where(TokenTransaction.transaction_type == transaction_type)

        if thread_id:
            query = query.where(TokenTransaction.thread_id == thread_id)

        # Get total count
        count_filters = [TokenTransaction.user_id == user_id]
        if transaction_type:
            count_filters.append(TokenTransaction.transaction_type == transaction_type)
        if thread_id:
            count_filters.append(TokenTransaction.thread_id == thread_id)

        count_query = select(func.count()).select_from(
            select(TokenTransaction).where(*count_filters).subquery()
        )

        total_result = await self.session.execute(count_query)
        total = total_result.scalar_one()

        # Get paginated results
        query = query.order_by(TokenTransaction.created_at.desc()).offset(offset).limit(limit)

        result = await self.session.execute(query)
        transactions = result.scalars().all()

        return {
            "transactions": [
                {
                    "id": t.id,
                    "transaction_type": t.transaction_type.value,
                    "input_tokens": t.input_tokens,
                    "output_tokens": t.output_tokens,
                    "total_tokens": t.total_tokens,
                    "credits_deducted": t.credits_deducted,
                    "base_cost_usd": str(t.base_cost_usd) if t.base_cost_usd else None,
                    "total_cost_usd": str(t.total_cost_usd) if t.total_cost_usd else None,
                    "model": t.model,
                    "thread_id": t.thread_id,
                    "request_id": t.request_id,
                    "pricing_version": t.pricing_version,
                    "created_at": t.created_at.isoformat(),
                }
                for t in transactions
            ],
            "total": total,
            "limit": limit,
            "offset": offset,
        }
