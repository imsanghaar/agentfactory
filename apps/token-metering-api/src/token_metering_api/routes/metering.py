"""Core metering endpoints: check, deduct, release (v6 - Credits)."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser, get_current_user
from ..core.database import get_session
from ..core.exceptions import MeteringAPIException
from ..core.rate_limit import limiter
from ..services.metering import MeteringService
from .schemas import (
    BlockedResponse,
    CheckRequest,
    CheckResponse,
    DeductRequest,
    DeductResponse,
    ReleaseRequest,
    ReleaseResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/check", response_model=CheckResponse)
@limiter.limit("100/minute")
async def check_balance(
    request: Request,
    check_request: CheckRequest,
    user: Annotated[CurrentUser, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Pre-request balance check with reservation (FR-018).

    Creates an atomic reservation for estimated tokens via Redis sorted set.
    Must complete in <5ms for 99% of requests (FR-004).

    Returns:
        200: CheckResponse with reservation_id if allowed
        402: BlockedResponse if INSUFFICIENT_BALANCE
        403: BlockedResponse if ACCOUNT_SUSPENDED or USER_MISMATCH
        409: BlockedResponse if REQUEST_ID_CONFLICT
    """
    logger.info(
        f"[Metering] /check: user={check_request.user_id}, "
        f"request_id={check_request.request_id}, "
        f"model={check_request.model}, "
        f"estimated_tokens={check_request.estimated_tokens}"
    )

    # Verify user_id matches JWT subject (FR-051)
    if check_request.user_id != user.id:
        logger.warning(
            f"[Metering] User ID mismatch: jwt={user.id}, "
            f"request={check_request.user_id}"
        )
        raise MeteringAPIException(
            status_code=403,
            error_code="USER_MISMATCH",
            message="user_id doesn't match JWT",
        )

    service = MeteringService(session)
    result = await service.check_balance(
        user_id=check_request.user_id,
        request_id=check_request.request_id,
        estimated_tokens=check_request.estimated_tokens,
        model=check_request.model,
        context=check_request.context,
    )

    if result.get("allowed"):
        logger.info(
            f"[Metering] /check allowed: reservation={result['reservation_id']}, "
            f"reserved_credits={result['reserved_credits']}"
        )
        return CheckResponse(
            allowed=True,
            reservation_id=result["reservation_id"],
            reserved_credits=result["reserved_credits"],
            expires_at=result["expires_at"],
        )

    # Determine HTTP status based on error_code
    error_code = result.get("error_code", "INSUFFICIENT_BALANCE")
    if error_code == "ACCOUNT_SUSPENDED":
        status_code = 403
    elif error_code == "REQUEST_ID_CONFLICT":
        status_code = 409
    else:  # INSUFFICIENT_BALANCE
        status_code = 402

    logger.info(f"[Metering] /check blocked: error={error_code}")
    return JSONResponse(
        status_code=status_code,
        content=BlockedResponse(
            allowed=False,
            error_code=error_code,
            message=result.get("message", "Request blocked"),
            balance=result.get("balance", 0),
            available_balance=result.get("available_balance", 0),
            required=result.get("required", 0),
            is_expired=result.get("is_expired", False),
        ).model_dump(),
    )


@router.post("/deduct", response_model=DeductResponse)
async def deduct_tokens(
    request: Request,
    deduct_request: DeductRequest,
    user: Annotated[CurrentUser, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Post-request token deduction - finalize reservation (FR-019).

    Converts reservation to actual usage, deducts from balance,
    and creates audit transaction. Idempotent via request_id (FR-061).

    Returns:
        200: DeductResponse with transaction details
    """
    total_tokens = deduct_request.input_tokens + deduct_request.output_tokens
    logger.info(
        f"[Metering] /deduct: user={deduct_request.user_id}, "
        f"model={deduct_request.model}, tokens={total_tokens}"
    )

    # Verify user_id matches JWT subject (FR-051)
    if deduct_request.user_id != user.id:
        logger.warning(
            f"[Metering] User ID mismatch: jwt={user.id}, "
            f"request={deduct_request.user_id}"
        )
        raise MeteringAPIException(
            status_code=403,
            error_code="USER_MISMATCH",
            message="user_id doesn't match JWT",
        )

    service = MeteringService(session)
    result = await service.finalize_usage(
        user_id=deduct_request.user_id,
        request_id=deduct_request.request_id,
        reservation_id=deduct_request.reservation_id,
        input_tokens=deduct_request.input_tokens,
        output_tokens=deduct_request.output_tokens,
        model=deduct_request.model,
        thread_id=deduct_request.thread_id,
        usage_details=deduct_request.usage_details,
    )

    status = result.get("status", "finalized")
    logger.info(
        f"[Metering] /deduct {status}: tx={result['transaction_id']}, "
        f"credits={result['credits_deducted']}, "
        f"pricing={result['pricing_version']}, "
        f"balance={result['balance_after']}"
    )

    return DeductResponse(
        status=status,
        transaction_id=result["transaction_id"],
        total_tokens=result["total_tokens"],
        credits_deducted=result["credits_deducted"],
        balance_after=result["balance_after"],
        balance_source=result.get("balance_source", "balance"),
        thread_id=result.get("thread_id"),
        pricing_version=result["pricing_version"],
    )


@router.post("/release", response_model=ReleaseResponse)
async def release_reservation(
    request: Request,
    release_request: ReleaseRequest,
    user: Annotated[CurrentUser, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """
    Cancel reservation on LLM failure (FR-020).

    Removes the reservation from Redis without deducting tokens.
    Idempotent - releasing twice returns success (FR-063).

    Returns:
        200: ReleaseResponse with released tokens
    """
    logger.info(
        f"[Metering] /release: user={release_request.user_id}, "
        f"request_id={release_request.request_id}"
    )

    # Verify user_id matches JWT subject (FR-051)
    if release_request.user_id != user.id:
        logger.warning(
            f"[Metering] User ID mismatch: jwt={user.id}, "
            f"request={release_request.user_id}"
        )
        raise MeteringAPIException(
            status_code=403,
            error_code="USER_MISMATCH",
            message="user_id doesn't match JWT",
        )

    service = MeteringService(session)
    result = await service.release_reservation(
        user_id=release_request.user_id,
        request_id=release_request.request_id,
        reservation_id=release_request.reservation_id,
    )

    return ReleaseResponse(
        status="released",
        reserved_credits=result.get("reserved_credits", 0),
    )
