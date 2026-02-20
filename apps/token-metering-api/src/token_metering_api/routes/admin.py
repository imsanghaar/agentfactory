"""Admin endpoints for credits management (v6 - Credits)."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, require_admin
from ..core.database import get_session
from ..core.exceptions import MeteringAPIException
from ..core.rate_limit import limiter
from ..services.admin import AdminService
from .schemas import (
    GrantRequest,
    GrantResponse,
    TopupRequest,
    TopupResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/grant", response_model=GrantResponse)
@limiter.limit("20/minute")  # Stricter limit for admin endpoints
async def grant_credits(
    request: Request,
    grant_request: GrantRequest,
    admin: Annotated[CurrentUser, Depends(require_admin)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Grant institutional credits to a user.

    Adds directly to account.balance. Creates allocation audit record.
    Requires admin role.
    """
    service = AdminService(session)
    result = await service.grant_credits(
        user_id=grant_request.user_id,
        credits=grant_request.credits,
        reason=grant_request.reason,
        admin_id=admin.id,
    )

    if not result.get("success"):
        raise MeteringAPIException(
            status_code=400,
            error_code="GRANT_FAILED",
            message=result.get("error", "Grant failed"),
        )

    return GrantResponse(
        success=True,
        transaction_id=result["transaction_id"],
        allocation_id=result["allocation_id"],
        credits_granted=result["credits_granted"],
        new_balance=result["new_balance"],
    )


@router.post("/topup", response_model=TopupResponse)
@limiter.limit("20/minute")  # Stricter limit for admin endpoints
async def topup_credits(
    request: Request,
    topup_request: TopupRequest,
    admin: Annotated[CurrentUser, Depends(require_admin)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Add topped-up credits to a user's balance.

    Adds directly to account.balance. Creates allocation audit record.
    Requires admin role.
    """
    service = AdminService(session)
    result = await service.topup_credits(
        user_id=topup_request.user_id,
        credits=topup_request.credits,
        payment_reference=topup_request.payment_reference,
        admin_id=admin.id,
    )

    if not result.get("success"):
        raise MeteringAPIException(
            status_code=400,
            error_code="TOPUP_FAILED",
            message=result.get("error", "Topup failed"),
        )

    return TopupResponse(
        success=True,
        transaction_id=result["transaction_id"],
        allocation_id=result["allocation_id"],
        credits_added=result["credits_added"],
        new_balance=result["new_balance"],
    )
