# Feature Specification: Freemium Token Tracker (v6 - Cost-Weighted Credits)

**Feature Branch**: `001-freemium-tracker`
**Created**: 2026-02-04
**Updated**: 2026-02-06
**Status**: Draft (v6 - Cost-Weighted Credits)
**Input**: Agent Factory Freemium Token Tracking System - Credit-based metering with model-aware pricing.

---

## Overview

A cost-weighted credit metering system designed for 900k+ users:

1. **New users get 20,000 free credits** (~$2.00 budget, ~2,857 DeepSeek interactions)
2. **Single metric: credit balance** - no separate trial tracking
3. **Cost-weighted deductions**: Different models cost different credits (1 credit = $0.0001)
4. **No daily/monthly limits** - just balance
5. **Admin can grant credits** to anyone (students, promos, etc.)
6. **Credits expire only after 365 days of inactivity** (active users keep credits forever)

```
NEW USER (20k credits) → USE BALANCE (cost-weighted) → BLOCKED at 0 → PAY/GRANT → CONTINUE
```

**Budget Examples (per 2,500-token interaction)**:

| Model         | Base Cost | With 20% Markup | Credits | Interactions per 20k |
| ------------- | --------- | --------------- | ------- | -------------------- |
| DeepSeek Chat | $0.000525 | $0.000630       | 7       | ~2,857               |
| GPT-5 Nano    | $0.000563 | $0.000675       | 7       | ~2,857               |

---

## Design Principles (v6)

1. **Pricing and credits are an internal accounting abstraction**: External services deal only in tokens. Conversion happens once, inside the metering service.
2. **Cost-weighted credits**: 1 credit = $0.0001 (configurable via `CREDITS_PER_DOLLAR`). Different models cost different credit amounts.
3. **Single conversion path**: `_calculate_credits()` used for both estimates and finals. No separate code paths that can diverge.
4. **Over-reservation acceptable; under-reservation NEVER allowed**: Pessimistic estimation uses `max(input_rate, output_rate)`.
5. **ROUND_CEILING**: Platform never gives free usage. Always rounds up.
6. **Single source of truth**: `TokenAccount.balance` field (not computed)
7. **O(1) balance reads**: Direct field access, no JOINs or SUMs
8. **One metric only**: Credit balance - no separate trial/request counting
9. **Audit-only allocations**: TokenAllocation tracks history, not state
10. **Inactivity expiry**: Balance expires after 365 days of no activity
11. **Scalable to 900k+ users**: No table bloat, no complexity

---

## User Scenarios & Testing _(mandatory)_

### User Story 1 - New User Experience (Priority: P1)

A new user discovers the AI tutor. They get 20,000 free credits (~$2.00 budget) to experience the product. When exhausted, they must pay or get credits granted.

**Why this priority**: Core conversion funnel - starter → paid.

**Independent Test**: Create new user, verify they have 20,000 credits, use them until blocked.

**Acceptance Scenarios**:

1. **Given** a new user, **When** account is created, **Then** they start with 20,000 credits (configurable via `STARTER_CREDITS`).

2. **Given** a user with 1,000 credits, **When** they make a request, **Then** cost-weighted credits are deducted based on model pricing and token usage.

3. **Given** a user with 0 credits, **When** they make a request, **Then** they are blocked with HTTP 402 and error code `INSUFFICIENT_BALANCE`.

4. **Given** a user with credits, **When** 30 days pass (with activity), **Then** their credits remain (no time-based expiry for active users).

---

### User Story 2 - User Tops Up Balance (Priority: P2)

A user who exhausted their starter credits wants to continue. They pay and receive credits.

**Why this priority**: Revenue generation.

**Acceptance Scenarios**:

1. **Given** a user with 0 balance, **When** they top up 100,000 credits, **Then** their balance becomes 100,000 and they can make requests.

2. **Given** a user with 50,000 credits, **When** they make a request, **Then** cost-weighted credits are deducted based on model pricing and token usage.

3. **Given** a user who exhausts their balance, **When** they make a request, **Then** they are blocked with HTTP 402.

4. **Given** a user inactive for 365+ days, **When** they return, **Then** their balance is expired (effective_balance = 0).

---

### User Story 3 - Admin Grants Credits (Priority: P3)

An admin grants credits to a user (student enrollment, promotional credit, support resolution).

**Why this priority**: Enables institutional access and promotions.

**Acceptance Scenarios**:

1. **Given** a user with 0 balance, **When** admin grants 500,000 credits, **Then** their balance becomes 500,000 and an audit record is created.

2. **Given** a user with 100,000 balance, **When** admin grants 50,000 more, **Then** their balance becomes 150,000.

3. **Given** a student who was inactive for 400 days, **When** admin grants credits, **Then** their `last_activity_at` is updated and balance is set to the granted amount.

4. **Given** a student who exhausts their granted balance, **When** they make a request, **Then** they are blocked with error code `INSUFFICIENT_BALANCE`.

---

### User Story 4 - Administrator Views Usage (Priority: P4)

An admin views a user's balance and usage history.

**Acceptance Scenarios**:

1. **Given** a user with usage history, **When** admin queries their balance, **Then** they see: current_balance, last_activity_at, allocation history.

2. **Given** a user with grants and topups, **When** admin views their account, **Then** they see all allocations (audit records) with amounts and dates.

---

### User Story 5 - Concurrent Request Handling (Priority: P1)

Multiple requests arrive simultaneously for the same user.

**Acceptance Scenarios**:

1. **Given** a user with 1000 tokens, **When** two requests for 600 tokens each arrive simultaneously, **Then** only one succeeds and the other is blocked.

2. **Given** a user with reservations in-flight, **When** a new check arrives, **Then** the reservation is considered in the available balance calculation.

---

### User Story 6 - LLM Failure Recovery (Priority: P2)

The LLM call fails after pre-check but before deduction.

**Acceptance Scenarios**:

1. **Given** a successful pre-check with reservation, **When** the LLM fails, **Then** calling `/release` frees the reservation with no balance change.

2. **Given** a reservation, **When** `/release` is called twice with same `reservation_id`, **Then** the second call returns success (idempotent).

---

## Edge Cases _(mandatory)_

| Scenario                                                 | Behavior                                                        | Error Code             |
| -------------------------------------------------------- | --------------------------------------------------------------- | ---------------------- |
| LLM fails after pre-check                                | Call `/release`, no deduction                                   | N/A                    |
| Redis unavailable                                        | Fail-open with DB `SELECT FOR UPDATE` lock                      | N/A                    |
| Actual usage > estimate                                  | Deduct actual, balance may go negative                          | N/A                    |
| Balance goes negative                                    | Allow (grace), block next request if still negative             | `INSUFFICIENT_BALANCE` |
| User inactive 365+ days                                  | `effective_balance = 0`, block until grant/topup                | `INSUFFICIENT_BALANCE` |
| Estimated > available                                    | Block immediately                                               | `INSUFFICIENT_BALANCE` |
| Duplicate `request_id` on `/check`                       | Return existing reservation (idempotent)                        | N/A                    |
| Duplicate `request_id` on `/check` with different params | Return 409 Conflict                                             | `REQUEST_ID_CONFLICT`  |
| Duplicate `request_id` on `/deduct`                      | Return original transaction (idempotent)                        | N/A                    |
| Suspended account                                        | Block all operations                                            | `ACCOUNT_SUSPENDED`    |
| Failopen reservation (Redis down)                        | Reservation ID starts with `failopen_`, release always succeeds | N/A                    |

---

## Requirements _(mandatory)_

### Functional Requirements

#### Core Metering

- **FR-001**: System MUST track input tokens, output tokens, and total tokens for every LLM request.
- **FR-002**: System MUST calculate marked-up cost (base cost + 20%) for every request, convert to credits, and deduct credits from balance.
- **FR-003**: System MUST support single state: credit-balance-based (no separate trial).
- **FR-004**: System MUST perform pre-request balance check in under 5 milliseconds (O(1) DB read + O(k) Redis scan).
- **FR-005**: System MUST block requests with HTTP 402 when user has insufficient credit balance.
- **FR-006**: System MUST return structured error with `error_code` field.
- **FR-070**: System MUST convert raw tokens to cost-weighted credits using the single `_calculate_credits` conversion path for both estimates and finals.
- **FR-071**: Over-reservation is acceptable; under-reservation is NEVER allowed. Estimation MUST use pessimistic pricing (`max(input_rate, output_rate)` for both halves).
- **FR-072**: Audit record MUST include: model, input_tokens, output_tokens, pricing snapshot (base_cost_usd, total_cost_usd), credits_deducted, balance_after, and pricing_version.
- **FR-075**: Route handlers MUST log model, pricing_version, and credits for all metering operations. Pricing selection MUST log the resolved pricing version (or DEFAULT_PRICING fallback) at INFO level.

#### Balance System

- **FR-007**: System MUST store credit balance as a single field on TokenAccount (source of truth).
- **FR-008**: System MUST track credit source (grant vs topup vs starter) via TokenAllocation audit records.
- **FR-009**: System MUST support admin granting credits to any user.
- **FR-010**: System MUST support adding topped-up credits (for future Stripe integration).
- **FR-011**: New users MUST start with `STARTER_CREDITS` (default 20,000) in their balance.
- **FR-012**: System MUST create a `starter` allocation audit record when new account is created.

**Budget Rationale**: `STARTER_CREDITS = 20,000` represents a ~$2.00 budget. At 2,500 tokens per interaction: DeepSeek costs ~7 credits (~2,857 interactions), GPT-5 Nano costs ~7 credits (~2,857 interactions). Credits = `ceil(cost_with_markup_usd * CREDITS_PER_DOLLAR)` where `CREDITS_PER_DOLLAR = 10,000`.

#### Inactivity Expiry

- **FR-024**: Balance expires after 365 days of inactivity.
- **FR-025**: Inactivity is defined as: `(now - last_activity_at) >= 365 days`.
- **FR-026**: System MUST expose `effective_balance` property: returns 0 if inactive 365+ days, else `balance`.
- **FR-027**: The following operations update `last_activity_at`:
  - `finalize_usage` (deduct)
  - `grant_credits`
  - `topup_credits`
- **FR-028**: The following operations do NOT update `last_activity_at`:
  - `check_balance` (read-only)
  - `get_balance` (read-only)
  - `release_reservation`
- **FR-029**: On account creation, `last_activity_at` MUST be set to `created_at`.
- **FR-030**: Balance field is NEVER mutated on expiry. Only `effective_balance` returns 0.

#### Concurrency & Atomicity

- **FR-032**: System MUST use atomic database operations: `UPDATE ... SET balance = balance - X`.
- **FR-033**: System MUST use Redis reservations when Redis is available; MUST fall back to DB `SELECT FOR UPDATE` if Redis unavailable.

**Redis Data Structure (Sorted Set per User)**:

- **FR-034**: Reservations stored as sorted set: `metering:reservations:{user_id}`
  - Score: expiry timestamp (unix epoch)
  - Member: `{request_id}:{credits}` (e.g., `req-123:24`)
  - **Parsing**: Split on last `:` to extract credits. `request_id` MUST NOT contain `:` (use UUID format).
- **FR-035**: No separate counter needed. Reserved total computed from sorted set.
- **FR-036**: On `/check`, Lua script MUST atomically:
  1. `ZREMRANGEBYSCORE` to remove expired (score < now)
  2. Check if `request_id` already exists in sorted set (scan members for prefix match)
     - If exists with same credits: return existing `reserved_total` (idempotent)
     - If exists with different credits: return error code for 409
  3. `ZADD` new reservation with expiry score
  4. `ZRANGE` + sum credits to compute `reserved_total`
  5. Return `reserved_total` for balance check
- **FR-036a**: If Python balance check fails after Lua returns, Python MUST immediately call `ZREM` to release the reservation (prevent leak).
- **FR-037**: On `/deduct`, Lua script MUST: `ZREM` the reservation member.
- **FR-038**: On `/release`, Lua script MUST: `ZREM` the reservation member.

**Available Balance Formula**:

```
available_balance = effective_balance - reserved_total
```

Where:

- `effective_balance` = 0 if expired, else `balance`
- `reserved_total` = sum of credits from `ZRANGE metering:reservations:{user_id}` (computed in Lua)

**Complexity Analysis**:

- `/check`: O(k) where k = active reservations for user (typically 1-3, bounded by TTL)
- `/deduct`, `/release`: O(log k) for ZREM
- No background reconciliation needed - cleanup happens lazily on each `/check`

**Compensation Rules**:

- If DB commit succeeds but Redis ZREM fails: orphaned member expires via score-based cleanup on next `/check`.
- If Redis succeeds but DB fails: retry DB with idempotency guard on `request_id`.

#### Idempotency

- **FR-058**: `/check` MUST be idempotent on `request_id`.
- **FR-059**: Duplicate `/check` with same `request_id` and same `estimated_tokens` MUST return existing reservation.
- **FR-060**: Duplicate `/check` with same `request_id` but different `estimated_tokens` MUST return 409 Conflict.
- **FR-061**: `/deduct` MUST be idempotent on `request_id`.
- **FR-062**: Duplicate `/deduct` MUST return original transaction with `status: "already_processed"`.
- **FR-063**: `/release` MUST be idempotent on `reservation_id`.
- **FR-064**: Failopen reservations (ID starts with `failopen_`) MUST always succeed on `/release`.

#### Negative Balance Handling

- **FR-041**: System MUST allow balance to go negative (grace for streaming token overages).
- **FR-042**: System MUST block next `/check` if `available_balance < estimated_tokens`.
- **FR-043**: Negative balance is flagged via `balance < 0` (no separate field needed).

#### Cost Calculation & Credit Conversion

- **FR-044**: Costs MUST be calculated using `Decimal` with 6 decimal places precision.
- **FR-045**: Formula: `base_cost = (input_tokens/1000 * input_rate) + (output_tokens/1000 * output_rate)`.
- **FR-046**: Markup: `total_cost = base_cost * (1 + markup_percent/100)`.
- **FR-047**: Default markup: 20%.
- **FR-065**: Rounding mode: `ROUND_CEILING` for credit conversion (platform never gives free usage); store full USD precision in DB.
- **FR-073**: Credit conversion: `credits = ceil(total_cost * CREDITS_PER_DOLLAR)` where `CREDITS_PER_DOLLAR = 10,000` (1 credit = $0.0001).
- **FR-074**: Balance deduction MUST use `credits` (not raw tokens). `UPDATE ... SET balance = balance - credits`.

#### Estimated Tokens

- **FR-066**: `estimated_tokens` is provided by client for `/check`.
- **FR-067**: Recommended formula: `estimated_tokens = input_tokens + max_output_tokens`.
- **FR-068**: `max_output_tokens` SHOULD be retrieved from model config (default: 4096).
- **FR-069**: `estimated_tokens` MUST be <= model's `max_tokens` limit if defined.

#### Pricing Selection

- **FR-048**: Pricing MUST be selected as: `WHERE model = ? AND is_active = true ORDER BY effective_date DESC LIMIT 1`.
- **FR-049**: If no pricing found, use `DEFAULT_PRICING` (input: $0.001/1k, output: $0.002/1k, version: "default-v1").

#### Audit & Persistence

- **FR-015**: System MUST record every transaction in immutable audit log (TokenTransaction).
- **FR-016**: System MUST persist user state to survive restarts (PostgreSQL).
- **FR-017**: Transaction log MUST include: tokens used, cost (with markup), model, timestamp, request_id.
- **FR-031**: System MUST record every grant/topup/starter in TokenAllocation (audit record).

#### Authorization

- **FR-050**: Admin endpoints MUST require `admin` role in JWT.
- **FR-051**: User endpoints MUST validate `user_id` matches JWT subject.
- **FR-052**: Only admins can set `account.status = SUSPENDED`.
- **FR-053**: Suspended accounts block all metering operations but allow admin operations.

#### Integration

- **FR-018**: System MUST expose `POST /metering/check` (pre-request balance check + reservation).
- **FR-019**: System MUST expose `POST /metering/deduct` (post-request finalization).
- **FR-020**: System MUST expose `POST /metering/release` (LLM failure - cancel reservation).
- **FR-021**: System MUST expose `GET /balance` (user dashboard).
- **FR-022**: System MUST expose `POST /admin/grant` (admin grants credits).
- **FR-023**: System MUST expose `POST /admin/topup` (future Stripe webhook).

#### Performance (Redis Caching - Optional)

- **FR-054**: System SHOULD cache balance in Redis for additional performance.
- **FR-055**: Cache key format: `metering:balance:{user_id}`.
- **FR-056**: Cache MUST be invalidated on: grant, topup, deduct, account creation.
- **FR-057**: On cache miss, read from TokenAccount (O(1)) and cache result.

---

## API Schemas _(mandatory)_

### POST /metering/check

**Request:**

```json
{
  "user_id": "string (required)",
  "request_id": "string (required, UUID for idempotency)",
  "estimated_tokens": "int (required, >= 1)",
  "model": "string (required)",
  "context": "object (optional)"
}
```

**Response (Success - 200):**

```json
{
  "allowed": true,
  "reservation_id": "string",
  "reserved_credits": "int (estimated credits reserved)",
  "expires_at": "datetime (ISO8601)"
}
```

**Response (Blocked - 402/403/409):**

```json
{
  "allowed": false,
  "error_code": "INSUFFICIENT_BALANCE | ACCOUNT_SUSPENDED | REQUEST_ID_CONFLICT",
  "message": "string",
  "balance": "int",
  "available_balance": "int (effective_balance - reserved_credits_total)",
  "required": "int (estimated credits required)",
  "is_expired": "bool"
}
```

### POST /metering/deduct

**Request:**

```json
{
  "user_id": "string (required)",
  "request_id": "string (required, must match check)",
  "reservation_id": "string (required)",
  "input_tokens": "int (required, >= 0)",
  "output_tokens": "int (required, >= 0)",
  "model": "string (required)",
  "thread_id": "string (optional)",
  "usage_details": "object (optional)"
}
```

**Response (Success - 200):**

```json
{
  "status": "finalized | already_processed",
  "transaction_id": "int",
  "total_tokens": "int",
  "credits_deducted": "int",
  "balance_after": "int",
  "pricing_version": "string"
}
```

### POST /metering/release

**Request:**

```json
{
  "user_id": "string (required)",
  "request_id": "string (required)",
  "reservation_id": "string (required)"
}
```

**Response (Success - 200):**

```json
{
  "status": "released",
  "reserved_credits": "int"
}
```

### GET /balance

**Response (Success - 200):**

```json
{
  "user_id": "string",
  "status": "active | suspended",
  "balance": "int",
  "effective_balance": "int (0 if expired)",
  "last_activity_at": "datetime (ISO8601)",
  "is_expired": "bool"
}
```

### POST /admin/grant

**Request:**

```json
{
  "user_id": "string (required)",
  "credits": "int (required, >= 1)",
  "reason": "string (optional)"
}
```

**Response (Success - 200):**

```json
{
  "success": true,
  "transaction_id": "int",
  "allocation_id": "int",
  "credits_granted": "int",
  "new_balance": "int"
}
```

### POST /admin/topup

**Request:**

```json
{
  "user_id": "string (required)",
  "credits": "int (required, >= 1)",
  "payment_reference": "string (optional)"
}
```

**Response (Success - 200):**

```json
{
  "success": true,
  "transaction_id": "int",
  "allocation_id": "int",
  "credits_added": "int",
  "new_balance": "int"
}
```

### Error Codes

| Code                   | HTTP Status | Description                                                                          |
| ---------------------- | ----------- | ------------------------------------------------------------------------------------ |
| `INSUFFICIENT_BALANCE` | 402         | available_balance < estimated_credits (covers: expired, negative, zero, or just low) |
| `ACCOUNT_SUSPENDED`    | 403         | Account suspended by admin                                                           |
| `USER_MISMATCH`        | 403         | user_id doesn't match JWT                                                            |
| `ADMIN_REQUIRED`       | 403         | Admin role required                                                                  |
| `REQUEST_ID_CONFLICT`  | 409         | Same request_id reused with different parameters                                     |

**Note**: We consolidated `BALANCE_EXHAUSTED`, `BALANCE_EXPIRED`, and `BALANCE_NEGATIVE` into `INSUFFICIENT_BALANCE`. All insufficient balance cases (zero, negative, expired, or simply too low for the request) return `INSUFFICIENT_BALANCE`. The response body includes `balance`, `available_balance`, and `is_expired` fields for client-side differentiation.

---

## Key Entities (v6 - Cost-Weighted Credits)

### TokenAccount (Source of Truth)

User's current state including credit balance.

```
TokenAccount
├── user_id (string, PK)
├── status (enum: active, suspended)
├── balance (int, default STARTER_CREDITS) - SINGLE CREDIT BALANCE FIELD (1 credit = $0.0001)
├── last_activity_at (datetime, default created_at) - For inactivity expiry
├── created_at
└── updated_at
```

**Computed Properties:**

- `effective_balance`: Returns 0 if `(now - last_activity_at) >= 365 days`, else `balance`.
- `is_expired`: Returns true if inactive 365+ days.
- `available_balance`: `effective_balance - reserved_total` (from Redis).

**REMOVED from v4**:

- ~~lifetime_used~~ (no trial tracking - just use balance)

### TokenAllocation (Audit Only)

Immutable record of credit additions. NOT used for balance calculation.

```
TokenAllocation
├── id (int, PK)
├── user_id (string, FK)
├── allocation_type (enum: starter, grant, topup)
├── amount (int) - Credits added (immutable)
├── reason (string, nullable) - Why allocated
├── admin_id (string, nullable) - Who granted (null for starter)
├── payment_reference (string, nullable) - Stripe reference
└── created_at
```

**Allocation Types**:

- `starter`: Initial credits for new users (automatic)
- `grant`: Admin-granted credits (institutional, promo)
- `topup`: User-purchased credits (Stripe)

### TokenTransaction (Audit Log)

Immutable record of all balance movements (usage deductions in credits and balance additions).

```
TokenTransaction
├── id (int, PK)
├── user_id (string, FK)
├── transaction_type (enum: usage, grant, topup, starter)
├── input_tokens (int, nullable) - Only for usage
├── output_tokens (int, nullable) - Only for usage
├── total_tokens (int) - For usage: input+output; for grant/topup/starter: amount added
├── base_cost_usd (decimal(10,6), nullable), markup_percent (nullable), total_cost_usd (decimal(10,6), nullable)
├── credits_deducted (int, nullable) - Only for usage; cost-weighted credits removed from balance (positive value)
├── model (string, nullable), request_id (string, unique, nullable), thread_id (string, nullable)
├── pricing_version (string, nullable)
└── created_at
```

**Field semantics by transaction_type:**

- `usage`: All fields populated. `credits_deducted` = cost-weighted credits removed from balance (positive value). `total_tokens` = raw token count for transparency. `base_cost_usd` and `total_cost_usd` record the pricing math. `pricing_version` enables audit reconstruction.
- `grant/topup/starter`: Only `total_tokens` (credits amount added), `user_id`, `created_at` populated. Token/cost fields are null.

**Note**: For grant/topup/starter, TokenTransaction mirrors TokenAllocation for ledger completeness. Both tables serve as audit trails — TokenAllocation for allocation history, TokenTransaction for unified balance movement ledger.

### Pricing (Reference)

Model pricing for cost calculation.

```
Pricing
├── id (int, PK)
├── model (string)
├── input_cost_per_1k (decimal(10,6))
├── output_cost_per_1k (decimal(10,6))
├── pricing_version (string)
├── effective_date (datetime)
└── is_active (bool)
```

---

## Test Scenarios _(mandatory)_

### Concurrency Tests

| Test                                           | Setup                               | Action                                | Expected                                                        |
| ---------------------------------------------- | ----------------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| Concurrent double-spend prevention             | User with 1000 balance              | Two `/check` for 600 each in parallel | One succeeds, one blocked                                       |
| Reservation prevents overspend                 | User with 1000, reservation for 800 | New `/check` for 500                  | Blocked (`available_balance = 200`)                             |
| Reserved total computed in Lua                 | User with multiple reservations     | `/check`                              | Lua sums tokens from sorted set (O(k), k = active reservations) |
| Insufficient balance does not leak reservation | User with 100 balance               | `/check` for 500                      | Blocked, sorted set empty after (FR-036a rollback)              |

### Idempotency Tests

| Test                                | Setup                  | Action                                                          | Expected                                       |
| ----------------------------------- | ---------------------- | --------------------------------------------------------------- | ---------------------------------------------- |
| Duplicate `/check` same params      | First check succeeds   | Second `/check` same `request_id` and `estimated_tokens`        | Returns existing reservation                   |
| Duplicate `/check` different params | First check succeeds   | Second `/check` same `request_id`, different `estimated_tokens` | Returns 409 `REQUEST_ID_CONFLICT`              |
| Duplicate `/deduct`                 | First deduct succeeds  | Second `/deduct` same `request_id`                              | Returns original transaction, no double charge |
| Duplicate `/release`                | First release succeeds | Second `/release` same `reservation_id`                         | Returns success, no error                      |

### Expiry Tests

| Test                      | Setup                                     | Action           | Expected                                                 |
| ------------------------- | ----------------------------------------- | ---------------- | -------------------------------------------------------- |
| Expired balance blocked   | User with 1000 balance, inactive 366 days | `/check`         | Blocked with `INSUFFICIENT_BALANCE`, `is_expired = true` |
| Grant reactivates expired | User expired                              | Admin grants 500 | Balance = 500, `last_activity_at` updated, can use       |
| Active user not expired   | User with activity 364 days ago           | `/check`         | Allowed                                                  |
| New user not expired      | User just created                         | `/check`         | Allowed (`last_activity_at = created_at`)                |

### Negative Balance Tests

| Test                  | Setup                 | Action                         | Expected                            |
| --------------------- | --------------------- | ------------------------------ | ----------------------------------- |
| Overage allowed       | User with 100 balance | Deduct 150 (streaming overage) | Balance = -50, transaction recorded |
| Negative blocks next  | User with -50 balance | `/check` for any amount        | Blocked with `INSUFFICIENT_BALANCE` |
| Topup clears negative | User with -50         | Topup 100                      | Balance = 50, can use again         |

### Release Flow Tests

| Test                | Setup                                  | Action     | Expected                                   |
| ------------------- | -------------------------------------- | ---------- | ------------------------------------------ |
| Release after check | Successful `/check`                    | `/release` | Reservation member removed from sorted set |
| Release failopen    | Reservation ID starts with `failopen_` | `/release` | Success, no error (FR-064)                 |

### Compensation Tests

| Test                     | Setup                                  | Action    | Expected                                                               |
| ------------------------ | -------------------------------------- | --------- | ---------------------------------------------------------------------- |
| DB succeeds, Redis fails | Simulate Redis failure after DB commit | `/deduct` | Transaction recorded, reservation expires via TTL                      |
| Redis down on `/check`   | Redis unavailable                      | `/check`  | Fail-open with DB `SELECT FOR UPDATE`, returns `failopen_` reservation |

### Reservation Cleanup Tests

| Test                                   | Setup                                   | Action                            | Expected                                                           |
| -------------------------------------- | --------------------------------------- | --------------------------------- | ------------------------------------------------------------------ |
| Expired reservations cleaned on /check | Create reservation, wait for TTL expiry | `/check`                          | Expired member removed via ZREMRANGEBYSCORE, new reservation added |
| reserved_total excludes expired        | Reservation expired but not yet cleaned | `/check` (Lua runs cleanup first) | reserved_total = only unexpired reservations                       |
| Multiple expired cleaned at once       | 3 expired reservations                  | `/check`                          | All 3 removed, only new reservation counted                        |

---

## Success Criteria _(mandatory)_

- **SC-001**: Pre-request checks complete in under 5 milliseconds (p99) via O(1) DB read + O(k) Redis scan where k = active reservations (bounded by TTL, typically 1-3).
- **SC-002**: New users start with exactly `STARTER_CREDITS` (20,000 default, ~$2.00 budget).
- **SC-003**: Users blocked when `available_balance < estimated_credits`.
- **SC-009**: Same raw token count produces different credit deductions across models (cost-weighted).
- **SC-010**: Markup applied in both estimation and finalization (same `_calculate_credits` path).
- **SC-004**: 20% markup correctly recorded in all transactions.
- **SC-005**: Admin can grant tokens and user can immediately use them.
- **SC-006**: System scales to 900k+ users without table bloat.
- **SC-007**: Concurrent requests do not cause double-spend.
- **SC-008**: Duplicate `request_id` returns idempotent response.

---

## Configuration

| Variable                    | Default                                                | Description                                  |
| --------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| `STARTER_CREDITS`           | 20000                                                  | Credits granted to new users (~$2.00 budget) |
| `CREDITS_PER_DOLLAR`        | 10000                                                  | Credits per USD (1 credit = $0.0001)         |
| `INACTIVITY_EXPIRY_DAYS`    | 365                                                    | Days of inactivity before balance expires    |
| `RESERVATION_TTL`           | 300                                                    | TTL for Redis reservations (5 min)           |
| `MARKUP_PERCENT`            | 20.0                                                   | Markup percentage on base cost               |
| `DEFAULT_MAX_OUTPUT_TOKENS` | 4096                                                   | Default max output tokens for estimation     |
| `DEFAULT_PRICING`           | `{input: 0.001, output: 0.002, version: "default-v1"}` | Fallback pricing when model not found        |
| `FAIL_OPEN`                 | true                                                   | Allow requests when Redis is down            |

---

## Assumptions

1. Redis and PostgreSQL already available.
2. JWT auth provides user_id and roles.
3. OpenAI SDK provides token counts via RunHooks.
4. Stripe integration is future scope (admin API for now).

---

## Constraints

1. Python 3.13+
2. No external billing dependencies
3. Separate microservice with own DB schema

---

## Out of Scope

- ~~Daily limits~~ (REMOVED - too complex)
- ~~Monthly limits~~ (REMOVED - too complex)
- ~~Multiple tier types~~ (REMOVED - just balance)
- ~~Per-allocation expiry~~ (REMOVED - inactivity expiry instead)
- ~~FIFO deduction~~ (REMOVED - single balance field)
- ~~Trial request counting~~ (REMOVED - just use starter tokens)
- Payment processing (Stripe)
- Invoice generation
- Subscription management

---

## The Complete Flow (v6 - Cost-Weighted Credits)

```
┌─────────────────────────────────────────────────────────────────┐
│                       REQUEST ARRIVES                           │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │   1. Get/Create Account     │
              │   (auto-create with         │
              │    STARTER_CREDITS if new)  │
              └─────────────┬───────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │   Account SUSPENDED?        │
              └─────────────┬───────────────┘
                       YES / \ NO
                       /     \
                      ▼       ▼
             [BLOCK         ┌─────────────────────────────┐
           ACCOUNT_         │   Inactive 365+ days?       │
           SUSPENDED]       │   (last_activity_at check)  │
                            └─────────────┬───────────────┘
                                     YES / \ NO
                                    /     \
                                   ▼       ▼
                          [BLOCK       ┌─────────────────────────────┐
                         INSUFFICIENT_ │  available_balance >=       │
                         BALANCE       │  estimated_credits?         │
                         (is_expired   └─────────────┬───────────────┘
                         =true)]
                                                YES / \ NO
                                               /     \
                                              ▼       ▼
                                   ┌──────────────┐ [BLOCK
                                   │ Create Redis │ INSUFFICIENT_
                                   │ Reservation  │ BALANCE]
                                   └──────┬───────┘
                                          │
                                          ▼
                                   [RETURN SUCCESS
                                    + reservation_id]
```

### Deduct Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                       DEDUCT ARRIVES                            │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │  Check request_id exists    │
              │  in TokenTransaction        │
              └─────────────┬───────────────┘
                       YES / \ NO
                       /     \
                      ▼       ▼
              [RETURN      ┌─────────────────────────────┐
             ALREADY_      │  Sequential:                │
             PROCESSED]    │  1. Convert tokens→credits  │
                           │     via _calculate_credits  │
                           │  2. DB: balance -= credits  │
                           │     + last_activity_at      │
                           │     + insert transaction    │
                           │  3. Redis: ZREM reservation │
                           │     from sorted set         │
                           └─────────────┬───────────────┘
                                         │
                                         ▼
                                  [RETURN SUCCESS]
```

---

## Migration Notes (v4 → v5 → v6)

### v4 → v5 (Trial → Balance Only)

1. Remove `lifetime_used` column from `TokenAccount`
2. Add `STARTER` to `AllocationType` enum
3. Remove all trial-related logic from services
4. Remove `BalanceSource.TRIAL` (only `BALANCE` remains)

### v5 → v6 (Raw Tokens → Cost-Weighted Credits)

1. Add `CREDITS_PER_DOLLAR = 10,000` configuration
2. Rename `STARTER_TOKENS = 50,000` → `STARTER_CREDITS = 20,000`
3. Add `CreditCalculation` dataclass and `_calculate_credits` method
4. Update `check_balance` to reserve estimated credits (not raw tokens)
5. Update `finalize_usage` to deduct credits (not raw tokens)
6. Rename API fields: `reserved_tokens` → `reserved_credits`, `tokens` → `credits`, etc.
7. Delete dead `services/types.py`
8. Update all tests to assert credit-based amounts

---

## Version Changes Summary

| Aspect              | v4                      | v5                      | v6                                 |
| ------------------- | ----------------------- | ----------------------- | ---------------------------------- |
| New user experience | 5 free requests (trial) | 50,000 starter tokens   | 20,000 starter credits (~$2)       |
| Balance unit        | Raw tokens              | Raw tokens              | Cost-weighted credits              |
| Deduction model     | 1:1 token:balance       | 1:1 token:balance       | Model-priced credits               |
| Trial tracking      | `lifetime_used` counter | None - just balance     | None - just balance                |
| Balance source      | "trial" or "balance"    | "balance" only          | "balance" only                     |
| Pricing impact      | None (all models equal) | None (all models equal) | Different models = different costs |
| Complexity          | Simple                  | **Simpler**             | Same simplicity + fair pricing     |
