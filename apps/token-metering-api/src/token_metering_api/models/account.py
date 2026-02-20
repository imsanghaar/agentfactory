"""Token account model - user's identity and credits balance (v6 - Credits).

v6 Changes (from v5):
- balance: Now represents credits (1 credit = $0.0001), default STARTER_CREDITS (20,000)
- Cost-weighted: different models cost different credits per token
- STARTER_TOKENS renamed to STARTER_CREDITS
- last_activity_at: For inactivity-based expiry (365 days)
- effective_balance: Returns 0 if inactive 365+ days, else balance
- available_balance: effective_balance - reserved_total (computed with Redis)
"""

from datetime import UTC, datetime, timedelta
from enum import StrEnum

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel

from ..config import settings

# Exposed for backward compatibility (tests import this).
# Actual expiry logic uses settings.inactivity_expiry_days at runtime.
INACTIVITY_EXPIRY_DAYS = settings.inactivity_expiry_days

# Default starter credits for new users (~$2.00 budget)
STARTER_CREDITS = 20_000

# Backward-compat alias (tests and imports)
STARTER_TOKENS = STARTER_CREDITS


class AccountStatus(StrEnum):
    """Account status states."""

    ACTIVE = "active"
    SUSPENDED = "suspended"


class TokenAccount(SQLModel, table=True):
    """User's account state with credits balance (v6 - Credits).

    v6 Model:
    - balance: Credits balance (1 credit = $0.0001), default STARTER_CREDITS
    - last_activity_at: For inactivity-based expiry
    - effective_balance: Property that returns 0 if inactive 365+ days
    - available_balance: computed as effective_balance - reserved_total

    Balance is stored directly here, NOT computed from allocations.
    TokenAllocation is audit-only.
    """

    __tablename__ = "token_accounts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(unique=True, max_length=100, index=True)

    # Account status
    status: AccountStatus = Field(default=AccountStatus.ACTIVE)

    # v6: Credits balance stored directly (source of truth)
    # New users start with STARTER_CREDITS (20,000 = ~$2.00)
    balance: int = Field(default=STARTER_CREDITS)

    # v6: Last activity for inactivity-based expiry
    # Initialized to created_at on account creation (FR-029)
    last_activity_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    # Metadata
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    @property
    def effective_balance(self) -> int:
        """Return balance, or 0 if inactive for 365+ days (FR-026).

        Active users keep their balance forever.
        Inactive users (no activity for 365 days) have balance expire.
        Balance field is NEVER mutated on expiry (FR-030).
        """
        if self.is_expired:
            return 0
        return self.balance

    @property
    def is_expired(self) -> bool:
        """Check if account is expired due to inactivity (FR-025).

        Returns True if (now - last_activity_at) >= 365 days.
        """
        now = datetime.now(UTC)

        # Handle timezone-naive datetimes (SQLite stores naive)
        last_activity = self.last_activity_at
        if last_activity.tzinfo is None:
            last_activity = last_activity.replace(tzinfo=UTC)

        return now - last_activity >= timedelta(days=settings.inactivity_expiry_days)
