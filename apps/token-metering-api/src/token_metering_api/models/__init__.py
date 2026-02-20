"""Token metering data models (v6 - Credits).

v6 Changes (from v5):
- TokenAccount: balance now represents credits (1 credit = $0.0001)
- STARTER_CREDITS = 20,000 (~$2.00 budget), replaces STARTER_TOKENS = 50,000
- Cost-weighted credit deductions based on model pricing
- Inactivity-based expiry via INACTIVITY_EXPIRY_DAYS (365 days)
"""

from sqlmodel import SQLModel

from .account import (
    INACTIVITY_EXPIRY_DAYS,
    STARTER_CREDITS,
    STARTER_TOKENS,
    AccountStatus,
    TokenAccount,
)
from .allocation import AllocationType, TokenAllocation
from .pricing import Pricing
from .transaction import BalanceSource, TokenTransaction, TransactionType

__all__ = [
    "SQLModel",
    # Account (v6)
    "TokenAccount",
    "AccountStatus",
    "INACTIVITY_EXPIRY_DAYS",
    "STARTER_CREDITS",
    "STARTER_TOKENS",  # backward-compat alias
    # Allocation (v6 - audit only, includes STARTER)
    "TokenAllocation",
    "AllocationType",
    # Transaction (v6 - includes STARTER)
    "TokenTransaction",
    "TransactionType",
    "BalanceSource",
    # Pricing
    "Pricing",
]
