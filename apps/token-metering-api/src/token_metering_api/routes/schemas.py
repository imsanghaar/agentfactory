"""Pydantic schemas for API requests and responses (v6 - Credits)."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

# === Validation Patterns ===

# UUID pattern: standard hyphenated lowercase format only (no colons allowed)
UUID_PATTERN = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"

# Reservation ID pattern: must start with res_ or failopen_ prefix
RESERVATION_ID_PATTERN = r"^(res_|failopen_)[a-f0-9-]+$"


# === Request Schemas ===


class CheckRequest(BaseModel):
    """Pre-request balance check (reservation) - FR-018."""

    user_id: str = Field(..., description="User ID from JWT")
    request_id: str = Field(
        ...,
        pattern=UUID_PATTERN,
        description="Client-generated UUID for idempotency (no colons)",
    )
    estimated_tokens: int = Field(..., ge=1, description="Estimated total tokens")
    model: str = Field(..., description="Model for cost calculation")
    context: dict[str, Any] | None = Field(default=None, description="Additional context")


class DeductRequest(BaseModel):
    """Post-request token deduction (finalize) - FR-019."""

    user_id: str = Field(..., description="User ID from JWT")
    request_id: str = Field(
        ...,
        pattern=UUID_PATTERN,
        description="Matching request_id from check",
    )
    reservation_id: str = Field(
        ...,
        pattern=RESERVATION_ID_PATTERN,
        description="Reservation ID from check response (res_ or failopen_ prefix)",
    )
    input_tokens: int = Field(..., ge=0, description="Actual input tokens")
    output_tokens: int = Field(..., ge=0, description="Actual output tokens")
    model: str = Field(..., description="Model used")
    thread_id: str | None = Field(default=None, description="Conversation/thread identifier")
    usage_details: dict[str, Any] | None = Field(
        default=None,
        description="Rich usage details (requests, cached_tokens, reasoning_tokens)",
    )


class ReleaseRequest(BaseModel):
    """Cancel reservation (on LLM failure) - FR-020."""

    user_id: str = Field(..., description="User ID from JWT")
    request_id: str = Field(
        ...,
        pattern=UUID_PATTERN,
        description="Matching request_id from check",
    )
    reservation_id: str = Field(
        ...,
        pattern=RESERVATION_ID_PATTERN,
        description="Reservation ID from check response (res_ or failopen_ prefix)",
    )


class GrantRequest(BaseModel):
    """Admin: Grant credits to user - FR-022."""

    user_id: str = Field(..., description="Target user ID")
    credits: int = Field(..., ge=1, le=100_000_000, description="Credits to grant (max 100M)")
    reason: str | None = Field(default=None, description="Reason for grant")


class TopupRequest(BaseModel):
    """Admin: Add topped-up credits - FR-023."""

    user_id: str = Field(..., description="Target user ID")
    credits: int = Field(..., ge=1, le=100_000_000, description="Credits to add (max 100M)")
    payment_reference: str | None = Field(default=None, description="Payment reference")


# === Response Schemas ===


class CheckResponse(BaseModel):
    """Successful balance check (reservation created)."""

    allowed: bool = True
    reservation_id: str
    reserved_credits: int
    expires_at: datetime


class BlockedResponse(BaseModel):
    """Balance check failed (v6 error format per spec)."""

    allowed: bool = False
    error_code: str = Field(
        ...,
        description=(
            "INSUFFICIENT_BALANCE | ACCOUNT_SUSPENDED | "
            "REQUEST_ID_CONFLICT | ESTIMATED_TOKENS_EXCEEDS_LIMIT"
        ),
    )
    message: str
    balance: int
    available_balance: int = Field(
        ..., description="effective_balance - reserved_total"
    )
    required: int = Field(
        ...,
        description="Estimated credits required (or tokens for pre-estimation errors)",
    )
    is_expired: bool


class DeductResponse(BaseModel):
    """Successful token deduction."""

    status: str = Field(
        ..., description="finalized | already_processed"
    )
    transaction_id: int
    total_tokens: int
    credits_deducted: int
    balance_after: int
    balance_source: str = Field(default="balance", description="Always 'balance' in v6")
    thread_id: str | None = None
    pricing_version: str


class ReleaseResponse(BaseModel):
    """Reservation released."""

    status: str = "released"
    reserved_credits: int


class BalanceResponse(BaseModel):
    """User balance information (v6 - per spec GET /balance)."""

    user_id: str
    status: str
    balance: int
    effective_balance: int = Field(..., description="0 if expired")
    last_activity_at: str | None
    is_expired: bool


class GrantResponse(BaseModel):
    """Credits granted response."""

    success: bool = True
    transaction_id: int
    allocation_id: int
    credits_granted: int
    new_balance: int


class TopupResponse(BaseModel):
    """Credits topped up response."""

    success: bool = True
    transaction_id: int
    allocation_id: int
    credits_added: int
    new_balance: int


class TransactionInfo(BaseModel):
    """Transaction record."""

    id: int
    transaction_type: str
    input_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None
    credits_deducted: int | None
    base_cost_usd: str | None
    total_cost_usd: str | None
    model: str | None
    thread_id: str | None
    request_id: str | None
    pricing_version: str | None
    created_at: str


class TransactionsResponse(BaseModel):
    """Paginated transactions response."""

    transactions: list[TransactionInfo]
    total: int
    limit: int
    offset: int


class AllocationInfo(BaseModel):
    """Token allocation record (v6 - audit only)."""

    id: int
    allocation_type: str  # "starter", "grant", or "topup"
    amount: int
    reason: str | None
    admin_id: str | None
    payment_reference: str | None
    created_at: str


class AllocationsResponse(BaseModel):
    """User's token allocations (audit history)."""

    user_id: str
    allocations: list[AllocationInfo]


class ErrorResponse(BaseModel):
    """Error response."""

    error_code: str
    message: str
    detail: dict[str, Any] | None = None
