"""Token transaction model - immutable audit log (v6 - Credits).

v6 Changes (from v5):
- credits_deducted now reflects cost-weighted credit amount (not raw tokens)
- base_cost_usd and total_cost_usd populated from pricing calculation
- For grant/topup/starter: total_tokens = credits amount added
"""

from datetime import UTC, datetime
from decimal import Decimal
from enum import StrEnum
from typing import Any

from sqlalchemy import JSON, Column, DateTime
from sqlalchemy.types import TypeDecorator
from sqlmodel import Field, SQLModel


class JSONType(TypeDecorator):
    """Dialect-aware JSON type: uses JSONB on PostgreSQL, JSON elsewhere."""

    impl = JSON
    cache_ok = True

    def load_dialect_impl(self, dialect):
        """Return JSONB for PostgreSQL, JSON for others."""
        if dialect.name == "postgresql":
            from sqlalchemy.dialects.postgresql import JSONB

            return dialect.type_descriptor(JSONB())
        return dialect.type_descriptor(JSON())


class TransactionType(StrEnum):
    """Types of token transactions."""

    USAGE = "usage"  # Token consumption (deduction)
    STARTER = "starter"  # Initial starter tokens for new users
    GRANT = "grant"  # Admin-granted tokens (institutional, promo)
    TOPUP = "topup"  # User-purchased tokens (Stripe)


class BalanceSource(StrEnum):
    """Source of tokens for deduction (v5 - balance only)."""

    BALANCE = "balance"  # From account.balance directly


class TokenTransaction(SQLModel, table=True):
    """Immutable record of a token operation (v5 - Balance Only).

    Field semantics by transaction_type:
    - usage: All fields populated. credits_deducted = tokens removed (positive value)
    - grant/topup/starter: Only total_tokens (amount added), user_id, created_at

    Note: For grant/topup/starter, TokenTransaction mirrors TokenAllocation
    for ledger completeness. Both tables serve as audit trails.
    """

    __tablename__ = "token_transactions"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(max_length=100, index=True)

    # Transaction classification
    transaction_type: TransactionType = Field(sa_column_kwargs={"nullable": False})

    # Token details (for 'usage' type)
    input_tokens: int | None = Field(default=None)
    output_tokens: int | None = Field(default=None)
    total_tokens: int | None = Field(default=None)

    # Cost calculation (for 'usage' type)
    base_cost_usd: Decimal | None = Field(default=None, max_digits=10, decimal_places=6)
    markup_percent: Decimal = Field(default=Decimal("20.00"), max_digits=5, decimal_places=2)
    total_cost_usd: Decimal | None = Field(default=None, max_digits=10, decimal_places=6)

    # Balance changes
    credits_deducted: int | None = Field(default=None)
    balance_source: BalanceSource | None = Field(default=None)

    # Allocation reference (v3: which allocation was debited)
    allocation_id: int | None = Field(default=None, foreign_key="token_allocations.id", index=True)

    # Context
    model: str | None = Field(default=None, max_length=100)
    lesson_path: str | None = Field(default=None, max_length=500)
    # request_id indexed for idempotency lookups (unique per usage transaction)
    request_id: str | None = Field(default=None, max_length=100, index=True, unique=True)

    # Pricing version for audit trail
    pricing_version: str | None = Field(default=None, max_length=20)

    # Thread tracking for conversation-level usage analysis
    thread_id: str | None = Field(default=None, max_length=100, index=True)

    # Immutable timestamp (use TIMESTAMPTZ for timezone-aware storage)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    # Additional context (renamed from 'metadata' which is reserved in SQLAlchemy)
    extra_data: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column("metadata", JSONType(), nullable=False, server_default="{}"),
    )
