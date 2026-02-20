"""Token allocation model - audit record for grants/topups/starter (v5).

v5 Changes (from v4):
- Added: STARTER allocation type for new user starter tokens
- Audit-only: NOT used for balance calculation
- Balance is on TokenAccount (STARTER_TOKENS default)
"""

from datetime import UTC, datetime
from enum import StrEnum

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel


class AllocationType(StrEnum):
    """Types of token allocations."""

    STARTER = "starter"  # Initial tokens for new users (automatic)
    GRANT = "grant"  # Admin-granted tokens (institutional, promo)
    TOPUP = "topup"  # User-purchased tokens (Stripe)


class TokenAllocation(SQLModel, table=True):
    """Audit record for token allocations (v5 - Audit Only).

    v5 Model:
    - This is an IMMUTABLE audit record
    - NOT used for balance calculation (balance is on TokenAccount)
    - Records when tokens were added and why

    Allocation Types:
    - starter: Initial tokens for new users (automatic)
    - grant: Admin-granted tokens (institutional, promo)
    - topup: User-purchased tokens (Stripe)
    """

    __tablename__ = "token_allocations"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(max_length=100, index=True, foreign_key="token_accounts.user_id")

    # Allocation type
    allocation_type: AllocationType = Field(sa_column_kwargs={"nullable": False})

    # Token amount (immutable - what was added)
    amount: int = Field(gt=0)

    # Context
    reason: str | None = Field(default=None, max_length=500)  # Why allocated (admin note)
    admin_id: str | None = Field(default=None, max_length=100)  # Who created this
    payment_reference: str | None = Field(default=None, max_length=100)  # Stripe reference

    # Metadata
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    @classmethod
    def create_starter(cls, user_id: str, amount: int) -> "TokenAllocation":
        """Create a starter allocation audit record (FR-012).

        Called automatically when new account is created.
        """
        return cls(
            user_id=user_id,
            allocation_type=AllocationType.STARTER,
            amount=amount,
            reason="Initial starter tokens for new user",
        )

    @classmethod
    def create_grant(
        cls,
        user_id: str,
        amount: int,
        reason: str | None = None,
        admin_id: str | None = None,
    ) -> "TokenAllocation":
        """Create a grant audit record."""
        return cls(
            user_id=user_id,
            allocation_type=AllocationType.GRANT,
            amount=amount,
            reason=reason,
            admin_id=admin_id,
        )

    @classmethod
    def create_topup(
        cls,
        user_id: str,
        amount: int,
        payment_reference: str | None = None,
        admin_id: str | None = None,
    ) -> "TokenAllocation":
        """Create a topup audit record."""
        return cls(
            user_id=user_id,
            allocation_type=AllocationType.TOPUP,
            amount=amount,
            payment_reference=payment_reference,
            admin_id=admin_id,
        )
