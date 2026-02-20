# Implementation Plan: Freemium Token Tracker (v5)

**Branch**: `001-freemium-tracker` | **Date**: 2026-02-05 | **Spec**: [spec.md](./spec.md)

---

## Summary

**Balance-only token metering** for 900k+ users:

```
NEW USER (50k tokens) → USE BALANCE → BLOCKED at 0 → PAY/GRANT → CONTINUE
```

**v5 Key Features**:

- 50,000 starter tokens (no request counting)
- Single `balance` field (O(1) reads)
- Inactivity expiry (365 days)
- Sorted set reservations with lazy cleanup

**Removed from v4**:

- ~~Trial request counting (`lifetime_used`)~~
- ~~Separate `BalanceSource.TRIAL`~~
- ~~Counter-based reservations~~

---

## Technical Context

**Language**: Python 3.13+
**Dependencies**: FastAPI, SQLModel, asyncpg, redis-py
**Storage**: PostgreSQL + Redis
**Performance**: O(1) DB read + O(k) Redis scan (k = active reservations, typically 1-3)

---

## Architecture (v5)

```
┌─────────────────────────────────────────────────────────────────┐
│                     TOKEN METERING API (v5)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ENDPOINTS:                                                    │
│   ├── POST /metering/check   → Pre-check + reserve (Lua)        │
│   ├── POST /metering/deduct  → Finalize + ZREM                  │
│   ├── POST /metering/release → Cancel + ZREM                    │
│   ├── GET  /balance          → User's balance                   │
│   ├── POST /admin/grant      → Admin grants tokens              │
│   └── POST /admin/topup      → Admin adds paid tokens           │
│                                                                 │
│   MODELS (v5):                                                  │
│   ├── TokenAccount           → user_id, balance, status,        │
│   │                            last_activity_at                 │
│   ├── TokenAllocation        → Audit-only (starter/grant/topup) │
│   └── TokenTransaction       → Immutable audit log              │
│                                                                 │
│   REDIS (v5):                                                   │
│   └── metering:reservations:{user_id} → Sorted set (ZSET)       │
│       Score: expiry timestamp                                   │
│       Member: {request_id}:{tokens}                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The v5 Logic

```python
STARTER_TOKENS = 50000
INACTIVITY_EXPIRY_DAYS = 365


async def check_balance(user_id: str, estimated_tokens: int, model: str):
    account = await get_or_create_account(user_id)  # Auto-creates with STARTER_TOKENS

    # 1. Suspended?
    if account.status == SUSPENDED:
        return BLOCK("ACCOUNT_SUSPENDED")

    # 2. Expired? (365+ days inactive)
    if account.is_expired:
        return BLOCK("INSUFFICIENT_BALANCE", is_expired=True)

    # 3. Available balance? (effective_balance - reserved_total)
    reserved_total = await lua_reserve(user_id, request_id, estimated_tokens)
    available = account.effective_balance - reserved_total

    if available < 0:
        await lua_release(user_id, request_id)  # Undo reservation
        return BLOCK("INSUFFICIENT_BALANCE")

    return ALLOW(reservation_id=f"{user_id}:{request_id}")


async def finalize_usage(user_id: str, request_id: str, input_tokens: int, output_tokens: int, model: str):
    # 1. Idempotency check
    existing = await get_transaction_by_request_id(request_id)
    if existing:
        return ALREADY_PROCESSED(existing)

    # 2. Deduct balance
    account = await get_account(user_id)
    total = input_tokens + output_tokens
    account.balance -= total
    account.last_activity_at = now()

    # 3. Log transaction with 20% markup
    tx = create_transaction(account, total, model, markup=20)

    # 4. Release Redis reservation
    await lua_release(user_id, request_id)

    return FINALIZED(tx)
```

---

## Implementation Phases

### Phase 1: Update Models (Migration)

| Task | Description | Status |
|------|-------------|--------|
| 1.1 | Add `balance` field to TokenAccount (default=STARTER_TOKENS) | TODO |
| 1.2 | Add `last_activity_at` field to TokenAccount | TODO |
| 1.3 | Remove `lifetime_used` from TokenAccount | TODO |
| 1.4 | Add `STARTER` to AllocationType enum | TODO |
| 1.5 | Make TokenAllocation audit-only (remove remaining_amount, expires_at) | TODO |
| 1.6 | Update TokenTransaction (nullable fields for non-usage) | TODO |

### Phase 2: Update Redis Layer

| Task | Description | Status |
|------|-------------|--------|
| 2.1 | Create `reserve.lua` (ZREMRANGEBYSCORE + ZADD + sum) | TODO |
| 2.2 | Create `release.lua` (ZREM) | TODO |
| 2.3 | Remove old counter-based scripts | TODO |
| 2.4 | Update Redis key patterns in code | TODO |

### Phase 3: Update Metering Service

| Task | Description | Status |
|------|-------------|--------|
| 3.1 | Rewrite `check_balance()` with v5 logic | TODO |
| 3.2 | Rewrite `finalize_usage()` with v5 logic | TODO |
| 3.3 | Add inactivity expiry check | TODO |
| 3.4 | Update `release_reservation()` to use ZREM | TODO |

### Phase 4: Update Admin Service

| Task | Description | Status |
|------|-------------|--------|
| 4.1 | Update `grant_tokens()` - add balance, create audit record | TODO |
| 4.2 | Update `topup_tokens()` - add balance | TODO |
| 4.3 | Create starter allocation on new account | TODO |

### Phase 5: Update API Schemas

| Task | Description | Status |
|------|-------------|--------|
| 5.1 | Add `is_expired` to BlockedResponse | TODO |
| 5.2 | Add `available_balance` to BlockedResponse | TODO |
| 5.3 | Update BalanceResponse (remove trial fields) | TODO |
| 5.4 | Add error codes (INSUFFICIENT_BALANCE, ACCOUNT_SUSPENDED) | TODO |

### Phase 6: Update Tests

| Task | Description | Status |
|------|-------------|--------|
| 6.1 | Update conftest.py fixtures for v5 | TODO |
| 6.2 | Add test: new user gets 50,000 tokens | TODO |
| 6.3 | Add test: balance exhausted returns INSUFFICIENT_BALANCE | TODO |
| 6.4 | Add test: inactivity expiry (365 days) | TODO |
| 6.5 | Add test: concurrent reservations (sorted set) | TODO |
| 6.6 | Add test: idempotency on check/deduct/release | TODO |
| 6.7 | Remove trial-related tests | TODO |

### Phase 7: Cleanup

| Task | Description | Status |
|------|-------------|--------|
| 7.1 | Remove unused imports | TODO |
| 7.2 | Remove old Redis key patterns | TODO |
| 7.3 | Run ruff format + check | TODO |
| 7.4 | Run full test suite | TODO |
| 7.5 | Verify all tests pass | TODO |

---

## Files to Modify

| File | Action |
|------|--------|
| `models/account.py` | Add balance, last_activity_at; remove lifetime_used |
| `models/allocation.py` | Add STARTER; make audit-only |
| `models/transaction.py` | Make fields nullable; add STARTER type |
| `services/metering.py` | Rewrite check_balance, finalize_usage with v5 logic |
| `services/admin.py` | Update grant/topup; add starter allocation |
| `routes/metering.py` | Update schemas, error codes |
| `routes/balance.py` | Update response schema |
| `routes/schemas.py` | Add new request/response models |
| `scripts/reserve.lua` | New: sorted set reserve script |
| `scripts/release.lua` | New: sorted set release script |
| `core/redis.py` | Update key patterns |
| `tests/conftest.py` | Update fixtures for v5 |
| `tests/test_*.py` | Update all tests for v5 |

---

## Configuration (v5)

```python
# config.py
STARTER_TOKENS: int = 50000          # Initial balance for new users
INACTIVITY_EXPIRY_DAYS: int = 365    # Days before balance expires
RESERVATION_TTL_SECONDS: int = 300   # 5 minutes
MARKUP_PERCENT: float = 20.0         # Cost markup

# Default pricing (fallback)
DEFAULT_PRICING = {
    "input_cost_per_1k": 0.001,
    "output_cost_per_1k": 0.002,
    "version": "default-v1",
}
```

---

## Redis Keys (v5)

| Key | Type | Purpose |
|-----|------|---------|
| `metering:reservations:{user_id}` | Sorted Set | Active reservations (score=expiry, member=request_id:tokens) |
| `metering:balance:{user_id}` | String | Optional balance cache (5 min TTL) |

**Removed**:
- ~~`metering:inflight:{user_id}:{request_id}`~~ (hash per reservation)
- ~~`metering:reserved:{user_id}`~~ (counter)

---

## Verification Checklist

After implementation, verify:

- [ ] New user gets 50,000 tokens (not 5 requests)
- [ ] Balance exhausted returns 402 with `INSUFFICIENT_BALANCE`
- [ ] User inactive 365+ days returns `is_expired: true`
- [ ] Concurrent requests use sorted set reservations
- [ ] Duplicate request_id returns idempotent response
- [ ] Release works (LLM failure = no charge)
- [ ] 20% markup logged in transactions
- [ ] All tests pass
- [ ] Linting passes

---

## v4 to v5 Changes Summary

| Aspect | v4 | v5 |
|--------|----|----|
| New user experience | 5 free requests (trial) | 50,000 starter tokens |
| Trial tracking | `lifetime_used` counter | None - just balance |
| Balance source | "trial" or "balance" | "balance" only |
| Reservations | Hash + counter | Sorted set (lazy cleanup) |
| Expiry | Per-allocation | Inactivity-based (365 days) |
| Complexity | Simple | **Simpler** |
