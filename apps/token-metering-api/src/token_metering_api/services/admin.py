"""Admin service for credits management operations (v6 - Credits).

v6 Changes:
- Grant/topup directly increments account.balance (in credits)
- TokenAllocation is audit-only
- Updates last_activity_at (reactivates expired accounts) - FR-027
"""

import logging
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.redis import get_redis
from ..models import (
    TokenAccount,
    TokenAllocation,
    TokenTransaction,
    TransactionType,
)
from .account import AccountService

logger = logging.getLogger(__name__)


class AdminService:
    """Service for administrative credits operations (v6 - Credits)."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.redis = get_redis()
        self._account_service = AccountService(session, self.redis)

    async def grant_credits(
        self,
        user_id: str,
        credits: int,
        reason: str | None,
        admin_id: str,
    ) -> dict[str, Any]:
        """
        Grant institutional credits to a user (FR-009).

        Adds credits directly to account.balance.
        Creates audit record in TokenAllocation.
        Updates last_activity_at (reactivates expired accounts) - FR-027.
        """
        # Ensure account exists - delegated to AccountService
        await self._account_service.get_or_create(user_id)

        now = datetime.now(UTC)

        # Atomically add to balance (FR-032: balance = balance + X)
        result = await self.session.execute(
            update(TokenAccount)
            .where(TokenAccount.user_id == user_id)
            .values(
                balance=TokenAccount.balance + credits,
                last_activity_at=now,  # Reactivates if expired - FR-027
                updated_at=now,
            )
            .returning(TokenAccount.balance)
        )
        new_balance = result.scalar_one()

        # Create audit record (FR-031)
        allocation = TokenAllocation.create_grant(
            user_id=user_id,
            amount=credits,
            reason=reason,
            admin_id=admin_id,
        )

        # Create transaction for ledger completeness (FR-015)
        transaction = TokenTransaction(
            user_id=user_id,
            transaction_type=TransactionType.GRANT,
            total_tokens=credits,
            extra_data={
                "reason": reason,
                "admin_id": admin_id,
                "granted_at": now.isoformat(),
            },
        )

        self.session.add(allocation)
        self.session.add(transaction)
        await self.session.commit()
        await self.session.refresh(allocation)
        await self.session.refresh(transaction)

        # Invalidate cache (FR-056) - delegated to AccountService
        await self._account_service.invalidate_balance_cache(user_id)

        logger.info(f"[Admin] Granted {credits} credits to {user_id} by {admin_id}: {reason}")

        return {
            "success": True,
            "transaction_id": transaction.id,
            "allocation_id": allocation.id,
            "credits_granted": credits,
            "new_balance": new_balance,
        }

    async def topup_credits(
        self,
        user_id: str,
        credits: int,
        payment_reference: str | None,
        admin_id: str,
    ) -> dict[str, Any]:
        """
        Add topped-up credits to user's balance (FR-010).

        Adds credits directly to account.balance.
        Creates audit record in TokenAllocation.
        Updates last_activity_at (reactivates expired accounts) - FR-027.
        """
        # Ensure account exists - delegated to AccountService
        await self._account_service.get_or_create(user_id)

        now = datetime.now(UTC)

        # Atomically add to balance (FR-032: balance = balance + X)
        result = await self.session.execute(
            update(TokenAccount)
            .where(TokenAccount.user_id == user_id)
            .values(
                balance=TokenAccount.balance + credits,
                last_activity_at=now,  # Reactivates if expired - FR-027
                updated_at=now,
            )
            .returning(TokenAccount.balance)
        )
        new_balance = result.scalar_one()

        # Create audit record (FR-031)
        allocation = TokenAllocation.create_topup(
            user_id=user_id,
            amount=credits,
            payment_reference=payment_reference,
            admin_id=admin_id,
        )

        # Create transaction for ledger completeness (FR-015)
        transaction = TokenTransaction(
            user_id=user_id,
            transaction_type=TransactionType.TOPUP,
            total_tokens=credits,
            extra_data={
                "payment_reference": payment_reference,
                "admin_id": admin_id,
                "topup_at": now.isoformat(),
            },
        )

        self.session.add(allocation)
        self.session.add(transaction)
        await self.session.commit()
        await self.session.refresh(allocation)
        await self.session.refresh(transaction)

        # Invalidate cache (FR-056) - delegated to AccountService
        await self._account_service.invalidate_balance_cache(user_id)

        logger.info(
            f"[Admin] Topup {credits} credits to {user_id} by {admin_id}: {payment_reference}"
        )

        return {
            "success": True,
            "transaction_id": transaction.id,
            "allocation_id": allocation.id,
            "credits_added": credits,
            "new_balance": new_balance,
        }
