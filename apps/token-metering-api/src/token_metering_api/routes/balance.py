"""Balance query endpoints (v6 - Credits)."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_current_user, require_admin
from ..core.database import get_session
from ..core.exceptions import MeteringAPIException
from ..core.rate_limit import limiter
from ..core.redis import get_redis
from ..models.transaction import TransactionType
from ..services.balance import BalanceService
from .schemas import (
    AllocationInfo,
    AllocationsResponse,
    BalanceResponse,
    TransactionInfo,
    TransactionsResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/balance", response_model=BalanceResponse)
@limiter.limit("100/minute")
async def get_balance(
    request: Request,
    user: Annotated[CurrentUser, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Get current user's balance and account status (FR-021).

    Returns balance, effective_balance, last_activity_at, and is_expired.
    """
    service = BalanceService(session)
    result = await service.get_balance(user.id, redis=get_redis())

    if not result:
        raise MeteringAPIException(
            status_code=404,
            error_code="NOT_FOUND",
            message="Account not found",
        )

    return BalanceResponse(**result)


@router.get("/balance/{user_id}", response_model=BalanceResponse)
@limiter.limit("20/minute")  # Stricter limit for admin endpoint
async def get_balance_by_user_id(
    request: Request,
    user_id: str,
    admin: Annotated[CurrentUser, Depends(require_admin)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Get specific user's balance (admin only).

    Requires admin role.
    """
    service = BalanceService(session)
    result = await service.get_balance(user_id, redis=get_redis())

    if not result:
        raise MeteringAPIException(
            status_code=404,
            error_code="NOT_FOUND",
            message="Account not found",
        )

    return BalanceResponse(**result)


@router.get("/allocations", response_model=AllocationsResponse)
@limiter.limit("100/minute")
async def get_allocations(
    request: Request,
    user: Annotated[CurrentUser, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Get current user's token allocation audit history (v4).

    Returns all allocations as audit records (no expiry tracking).
    Balance is stored directly on TokenAccount, not computed from allocations.
    """
    service = BalanceService(session)
    allocations = await service.get_allocations(user.id)

    return AllocationsResponse(
        user_id=user.id,
        allocations=[AllocationInfo(**a) for a in allocations],
    )


@router.get("/transactions", response_model=TransactionsResponse)
@limiter.limit("100/minute")
async def get_transactions(
    request: Request,
    user: Annotated[CurrentUser, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    limit: int = Query(default=50, le=100),
    offset: int = Query(default=0, ge=0),
    type: TransactionType | None = Query(default=None),
    thread_id: str | None = Query(default=None, description="Filter by conversation/thread"),
):
    """
    Get transaction history for current user.

    Supports pagination and filtering by transaction type and thread_id.
    """
    service = BalanceService(session)
    result = await service.get_transactions(
        user_id=user.id,
        limit=limit,
        offset=offset,
        transaction_type=type,
        thread_id=thread_id,
    )

    return TransactionsResponse(
        transactions=[TransactionInfo(**t) for t in result["transactions"]],
        total=result["total"],
        limit=limit,
        offset=offset,
    )
