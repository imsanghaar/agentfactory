# Data Model: Freemium Token Tracker (v5)

**Feature**: 001-freemium-tracker
**Created**: 2026-02-04
**Updated**: 2026-02-05
**Version**: v5 - Balance Only (No Trial Tracking)

---

## Design Decisions

### Why Single Balance Field (v5) vs Allocations (v3)?

**v3 had**: `TokenAllocation` table with `remaining_amount` and `expires_at` for FIFO deduction.

**Problems**:
- O(n) balance calculation (SUM of allocations)
- Complex FIFO deduction logic
- Per-allocation expiry adds complexity

**v5 solution**: Single `balance` field on `TokenAccount`.
- O(1) balance reads
- Inactivity-based expiry (365 days) instead of per-allocation expiry
- `TokenAllocation` becomes audit-only (no state)

---

## PostgreSQL Schema

### Table: token_accounts

User's identity and balance state. Balance is stored directly (source of truth).

```sql
CREATE TABLE token_accounts (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(100) UNIQUE NOT NULL,

    -- Status
    status VARCHAR(20) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'suspended')),

    -- Balance (SINGLE FIELD - source of truth)
    balance INTEGER NOT NULL DEFAULT 50000,  -- STARTER_TOKENS

    -- Inactivity tracking
    last_activity_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Metadata
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_token_accounts_user ON token_accounts(user_id);
CREATE INDEX idx_token_accounts_status ON token_accounts(status);
CREATE INDEX idx_token_accounts_activity ON token_accounts(last_activity_at);
```

### Table: token_allocations

Audit-only record of token additions. NOT used for balance calculation.

```sql
CREATE TABLE token_allocations (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL REFERENCES token_accounts(user_id),

    -- Allocation type
    allocation_type VARCHAR(20) NOT NULL
        CHECK (allocation_type IN ('starter', 'grant', 'topup')),

    -- Token amount (immutable audit record)
    amount INTEGER NOT NULL,

    -- Context
    reason VARCHAR(500),
    admin_id VARCHAR(100),
    payment_reference VARCHAR(100),

    -- Metadata
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_token_allocations_user ON token_allocations(user_id);
CREATE INDEX idx_token_allocations_type ON token_allocations(allocation_type);
```

### Table: token_transactions

Immutable audit log of all token movements (usage and allocations).

```sql
CREATE TABLE token_transactions (
    id BIGSERIAL PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,

    -- Transaction classification
    transaction_type VARCHAR(20) NOT NULL CHECK (
        transaction_type IN ('usage', 'grant', 'topup', 'starter')
    ),

    -- Token details (nullable for non-usage)
    input_tokens INTEGER,
    output_tokens INTEGER,
    total_tokens INTEGER NOT NULL,

    -- Cost calculation (nullable for non-usage)
    base_cost_usd DECIMAL(10, 6),
    markup_percent DECIMAL(5, 2),
    total_cost_usd DECIMAL(10, 6),

    -- Deduction details (nullable for non-usage)
    credits_deducted INTEGER,  -- Positive value: tokens removed from balance

    -- Context
    model VARCHAR(100),
    lesson_path VARCHAR(500),
    request_id VARCHAR(100) UNIQUE,
    thread_id VARCHAR(100),
    pricing_version VARCHAR(20),

    -- Immutable timestamp
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Additional context
    metadata JSONB DEFAULT '{}'::JSONB
);

CREATE INDEX idx_token_transactions_user ON token_transactions(user_id);
CREATE INDEX idx_token_transactions_type ON token_transactions(transaction_type);
CREATE INDEX idx_token_transactions_created ON token_transactions(created_at);
CREATE INDEX idx_token_transactions_request ON token_transactions(request_id);
CREATE INDEX idx_token_transactions_thread ON token_transactions(thread_id);
```

### Table: pricing

Model pricing configuration for cost calculation.

```sql
CREATE TABLE pricing (
    id SERIAL PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    pricing_version VARCHAR(20) NOT NULL,
    effective_date DATE DEFAULT CURRENT_DATE,

    -- Cost per 1000 tokens
    input_cost_per_1k DECIMAL(10, 6) NOT NULL,
    output_cost_per_1k DECIMAL(10, 6) NOT NULL,

    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_pricing_model ON pricing(model);
CREATE INDEX idx_pricing_active ON pricing(is_active) WHERE is_active = TRUE;

-- Seed default pricing
INSERT INTO pricing (model, pricing_version, input_cost_per_1k, output_cost_per_1k) VALUES
    ('deepseek-chat', 'v1', 0.00014, 0.00028),
    ('gpt-4o', 'v1', 0.0025, 0.01);
```

---

## SQLModel Definitions

### models/account.py

```python
"""Token account model - user's balance state (v5)."""

from datetime import UTC, datetime, timedelta
from enum import StrEnum

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel

INACTIVITY_EXPIRY_DAYS = 365


class AccountStatus(StrEnum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


class TokenAccount(SQLModel, table=True):
    """User's account with balance (v5 - single balance field)."""

    __tablename__ = "token_accounts"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(unique=True, max_length=100, index=True)
    status: AccountStatus = Field(default=AccountStatus.ACTIVE)

    # Balance (source of truth)
    balance: int = Field(default=50000)  # STARTER_TOKENS

    # Inactivity tracking
    last_activity_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    @property
    def is_expired(self) -> bool:
        """Check if account is inactive for 365+ days."""
        return (datetime.now(UTC) - self.last_activity_at) >= timedelta(
            days=INACTIVITY_EXPIRY_DAYS
        )

    @property
    def effective_balance(self) -> int:
        """Return 0 if expired, else balance."""
        return 0 if self.is_expired else self.balance
```

### models/allocation.py

```python
"""Token allocation model - audit-only records (v5)."""

from datetime import UTC, datetime
from enum import StrEnum

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel


class AllocationType(StrEnum):
    STARTER = "starter"  # Initial tokens for new users
    GRANT = "grant"      # Admin-granted tokens
    TOPUP = "topup"      # User-purchased tokens


class TokenAllocation(SQLModel, table=True):
    """Audit record of token allocation (v5 - no state, just audit)."""

    __tablename__ = "token_allocations"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(max_length=100, index=True, foreign_key="token_accounts.user_id")

    allocation_type: AllocationType = Field(sa_column_kwargs={"nullable": False})

    # Token amount (immutable)
    amount: int = Field(gt=0)

    # Context
    reason: str | None = Field(default=None, max_length=500)
    admin_id: str | None = Field(default=None, max_length=100)
    payment_reference: str | None = Field(default=None, max_length=100)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
```

### models/transaction.py

```python
"""Token transaction model - immutable audit log (v5)."""

from datetime import UTC, datetime
from decimal import Decimal
from enum import StrEnum
from typing import Any

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


class TransactionType(StrEnum):
    USAGE = "usage"
    GRANT = "grant"
    TOPUP = "topup"
    STARTER = "starter"


class BalanceSource(StrEnum):
    BALANCE = "balance"  # From account.balance


class TokenTransaction(SQLModel, table=True):
    """Immutable record of all token movements (v5)."""

    __tablename__ = "token_transactions"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(max_length=100, index=True)
    transaction_type: TransactionType = Field(sa_column_kwargs={"nullable": False})

    # Token details (nullable for non-usage)
    input_tokens: int | None = Field(default=None)
    output_tokens: int | None = Field(default=None)
    total_tokens: int = Field()  # For usage: input+output; for grant/topup: amount

    # Cost calculation (nullable for non-usage)
    base_cost_usd: Decimal | None = Field(default=None, max_digits=10, decimal_places=6)
    markup_percent: Decimal | None = Field(default=None, max_digits=5, decimal_places=2)
    total_cost_usd: Decimal | None = Field(default=None, max_digits=10, decimal_places=6)

    # Deduction (nullable for non-usage)
    credits_deducted: int | None = Field(default=None)  # Positive: tokens removed

    # Context
    model: str | None = Field(default=None, max_length=100)
    lesson_path: str | None = Field(default=None, max_length=500)
    request_id: str | None = Field(default=None, max_length=100, index=True, unique=True)
    thread_id: str | None = Field(default=None, max_length=100, index=True)
    pricing_version: str | None = Field(default=None, max_length=20)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column("extra_data", JSONB, nullable=False, server_default="{}"),
    )
```

---

## Redis Data Structure (v5)

### Sorted Set for Reservations

| Key Pattern | Type | Purpose |
|-------------|------|---------|
| `metering:reservations:{user_id}` | Sorted Set | Active reservations |

**Sorted Set Structure**:
- **Score**: Expiry timestamp (unix epoch)
- **Member**: `{request_id}:{tokens}` (e.g., `req-123:5000`)

**Parsing**: Split on last `:` to extract tokens. `request_id` MUST NOT contain `:` (use UUID format).

### Lua Script: Check Balance

```lua
-- reserve.lua: Atomically cleanup + check idempotency + reserve + compute total
-- Returns: {status, reserved_total, existing_tokens}
--   status: 0=new, 1=idempotent (same tokens), 2=conflict (different tokens)
local key = KEYS[1]  -- metering:reservations:{user_id}
local now = tonumber(ARGV[1])  -- current timestamp
local request_id = ARGV[2]
local tokens = tonumber(ARGV[3])
local ttl = tonumber(ARGV[4])  -- expiry timestamp

-- 1. Remove expired reservations
redis.call('ZREMRANGEBYSCORE', key, '-inf', now)

-- 2. Check for existing request_id (idempotency)
local members = redis.call('ZRANGE', key, 0, -1)
local prefix = request_id .. ':'
for _, m in ipairs(members) do
    if string.sub(m, 1, #prefix) == prefix then
        -- Found existing - check if same tokens
        local existing_tokens = tonumber(string.match(m, ':(%d+)$'))
        local reserved_total = 0
        for _, m2 in ipairs(members) do
            local t = tonumber(string.match(m2, ':(%d+)$'))
            if t then reserved_total = reserved_total + t end
        end
        if existing_tokens == tokens then
            return {1, reserved_total, existing_tokens}  -- idempotent
        else
            return {2, reserved_total, existing_tokens}  -- conflict
        end
    end
end

-- 3. Add new reservation
local member = request_id .. ':' .. tokens
redis.call('ZADD', key, ttl, member)

-- 4. Compute reserved_total (re-fetch since we added)
members = redis.call('ZRANGE', key, 0, -1)
local reserved_total = 0
for _, m in ipairs(members) do
    local t = tonumber(string.match(m, ':(%d+)$'))
    if t then reserved_total = reserved_total + t end
end

return {0, reserved_total, tokens}  -- new reservation
```

**Return Values**:
- `{0, reserved_total, tokens}` → New reservation added
- `{1, reserved_total, existing_tokens}` → Idempotent (same request_id, same tokens)
- `{2, reserved_total, existing_tokens}` → Conflict (same request_id, different tokens)

### Optional: Balance Cache

| Key Pattern | Type | TTL | Purpose |
|-------------|------|-----|---------|
| `metering:balance:{user_id}` | String | 5 min | Cached balance (optional) |

---

## Balance Calculation (v5)

### Direct Read (O(1))

```python
async def get_balance(user_id: str) -> int:
    """O(1) balance read from account."""
    account = await session.get(TokenAccount, user_id)
    return account.effective_balance if account else 0
```

### Available Balance (with reservations)

```python
async def get_available_balance(user_id: str, redis: Redis) -> int:
    """effective_balance - reserved_total"""
    account = await session.get(TokenAccount, user_id)
    if not account:
        return 0

    effective = account.effective_balance
    reserved = await redis.execute_command(
        'EVAL', RESERVE_LUA, 1, f'metering:reservations:{user_id}',
        int(time.time()), '', 0, 0  # Just compute total, don't add
    )
    return effective - reserved
```

### Deduction Logic (Simple)

```python
async def deduct_balance(account: TokenAccount, tokens: int) -> None:
    """Atomic balance deduction."""
    account.balance -= tokens
    account.last_activity_at = datetime.now(UTC)
    # Note: balance can go negative (grace for streaming overages)
```

---

## Configuration (v5)

| Variable | Default | Description |
|----------|---------|-------------|
| `STARTER_TOKENS` | 50000 | Tokens for new users |
| `INACTIVITY_EXPIRY_DAYS` | 365 | Days before balance expires |
| `RESERVATION_TTL_SECONDS` | 300 | TTL for reservations (5 min) |
| `MARKUP_PERCENT` | 20.0 | Cost markup percentage |

---

## v3 to v5 Migration

```sql
-- 1. Add new columns to token_accounts
ALTER TABLE token_accounts ADD COLUMN balance INTEGER DEFAULT 0;
ALTER TABLE token_accounts ADD COLUMN last_activity_at TIMESTAMPTZ DEFAULT NOW();

-- 2. Migrate balance from allocations
UPDATE token_accounts ta SET balance = (
    SELECT COALESCE(SUM(remaining_amount), 0)
    FROM token_allocations
    WHERE user_id = ta.user_id AND expires_at > NOW()
);

-- 3. Remove obsolete columns
ALTER TABLE token_accounts DROP COLUMN IF EXISTS lifetime_used;
ALTER TABLE token_accounts DROP COLUMN IF EXISTS granted_tokens;
ALTER TABLE token_accounts DROP COLUMN IF EXISTS topped_up_tokens;

-- 5. Make allocations audit-only (remove state columns)
ALTER TABLE token_allocations DROP COLUMN IF EXISTS remaining_amount;
ALTER TABLE token_allocations DROP COLUMN IF EXISTS expires_at;
ALTER TABLE token_allocations ADD COLUMN IF NOT EXISTS amount INTEGER;
UPDATE token_allocations SET amount = original_amount WHERE amount IS NULL;
ALTER TABLE token_allocations DROP COLUMN IF EXISTS original_amount;

-- 6. Add starter allocation type
ALTER TABLE token_allocations DROP CONSTRAINT IF EXISTS token_allocations_allocation_type_check;
ALTER TABLE token_allocations ADD CONSTRAINT token_allocations_allocation_type_check
    CHECK (allocation_type IN ('starter', 'grant', 'topup'));
```
