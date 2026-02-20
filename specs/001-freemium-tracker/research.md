# Research: Freemium Token Tracker

**Feature**: 001-freemium-tracker
**Date**: 2026-02-04
**Status**: Complete

---

## Reference Codebase Analysis

### 1. taskforce_agent1/apps/api (FastAPI + SQLModel Patterns)

**Location**: `/Users/mjs/Documents/code/mjunaidca/taskforce_agent1/apps/api`

#### Project Structure

```
apps/api/
├── main.py                          # Entry point (dev convenience)
├── src/taskflow_api/
│   ├── main.py                      # FastAPI app with lifespan
│   ├── config.py                    # pydantic_settings configuration
│   ├── database.py                  # Async SQLAlchemy engine + session
│   ├── auth.py                      # JWT/JWKS authentication
│   ├── models/                      # SQLModel entities
│   │   ├── audit.py                 # Immutable audit log
│   │   ├── project.py               # Entity with relationships
│   │   ├── task.py                  # Entity with foreign keys
│   │   └── worker.py                # User/agent entity
│   ├── schemas/                     # Pydantic request/response models
│   ├── routers/                     # FastAPI APIRouter modules
│   ├── services/                    # Business logic (audit, setup)
│   └── tests/
│       └── conftest.py              # SQLite in-memory test setup
```

#### Key Patterns Extracted

**1. Configuration (config.py)**

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    database_url: str
    sso_url: str
    debug: bool = False
    dev_mode: bool = False
```

**Decision**: Use pydantic_settings for type-safe configuration from environment.

**2. Async Database (database.py)**

```python
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

def get_async_database_url(url: str) -> str:
    # postgresql:// -> postgresql+asyncpg://
    # sslmode=require -> ssl=require
    ...

engine = create_async_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,      # Essential for Neon (check alive)
    pool_recycle=300,        # Recycle after 5 min (Neon closes idle)
)

async def get_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session
```

**Decision**: Use asyncpg driver with pool_pre_ping for Neon compatibility.

**3. Audit Logging (models/audit.py)**

```python
class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_log"

    id: int | None = Field(default=None, primary_key=True)
    entity_type: str = Field(index=True)
    entity_id: int = Field(index=True)
    action: str
    actor_id: int = Field(foreign_key="worker.id", index=True)
    actor_type: str  # "human" or "agent"
    details: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSONB, nullable=False, server_default="{}"),
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

**Decision**: Adopt immutable audit log pattern with JSONB details column for TokenTransaction.

**4. JWT Authentication (auth.py)**

```python
class CurrentUser:
    def __init__(self, payload: dict[str, Any]) -> None:
        self.id: str = payload.get("sub", "")
        self.email: str = payload.get("email", "")
        self.tenant_id: str | None = payload.get("tenant_id")

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> CurrentUser:
    # Dev mode bypass, JWT verification, opaque token fallback
    ...
```

**Decision**: Extract user_id from JWT sub claim. Support dev_mode bypass for local testing.

**5. Lifespan Pattern (main.py)**

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await create_db_and_tables()
    yield
    # Shutdown
    ...

app = FastAPI(lifespan=lifespan)
```

**Decision**: Use lifespan for DB init and Redis connection management.

**6. Test Setup (tests/conftest.py)**

```python
# Patch JSONB -> JSON for SQLite compatibility
import sqlalchemy.dialects.postgresql as pg_dialects
pg_dialects.JSONB = JSON

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

@pytest.fixture(autouse=True)
async def setup_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
```

**Decision**: Use SQLite in-memory for unit tests with JSONB->JSON patch.

---

### 2. enrollment microservice (Redis Caching Patterns)

**Location**: `/Users/mjs/Documents/code/panaversity-official/project-coding/staging-merge/microservices/enrollment`

#### Project Structure

```
microservices/enrollment/
├── app/
│   ├── main.py                      # FastAPI app
│   ├── settings.py                  # Starlette Config
│   ├── core/
│   │   ├── redis_cache.py           # Redis client + caching decorator
│   │   ├── rate_limit.py            # Lua-based rate limiting
│   │   ├── lifespan.py              # Redis startup/shutdown
│   │   └── db_eng.py                # Sync SQLModel engine
│   ├── models/                      # SQLModel entities
│   ├── data/                        # Data access layer
│   ├── api/v1/routes/               # Endpoint modules
│   └── service/                     # Business logic
└── tests/
    ├── conftest.py
    └── package/test_redis_cache.py
```

#### Key Patterns Extracted

**1. Redis Client Management (redis_cache.py)**

```python
import redis.asyncio
import redis.asyncio.retry
import redis.backoff

_aredis: redis.asyncio.Redis | None = None

async def start_redis() -> None:
    global _aredis
    _aredis = redis.asyncio.Redis.from_url(
        REDIS_URL,
        password=str(REDIS_PASSWORD),
        decode_responses=True,
        max_connections=REDIS_MAX_CONNECTIONS,
        retry=redis.asyncio.retry.Retry(
            backoff=redis.backoff.ExponentialBackoff(),
            retries=5,
        ),
        retry_on_error=[
            redis.exceptions.ConnectionError,
            redis.exceptions.TimeoutError,
        ],
    )
    await _aredis.ping()

async def stop_redis() -> None:
    if _aredis:
        await _aredis.aclose()

def get_redis() -> redis.asyncio.Redis:
    if not _aredis:
        raise ValueError("Redis not initialized")
    return _aredis
```

**Decision**: Use global Redis client with exponential backoff retry. Start/stop in lifespan.

**2. Safe Redis Operations (redis_cache.py)**

```python
async def safe_redis_get(cache_key: str) -> Optional[str]:
    try:
        redis_client = get_redis()
        return await redis_client.get(cache_key)
    except Exception as e:
        logger.error(f"Failed to get cache: {e}")
        return None  # Fail-open: return None, don't crash

async def safe_redis_set(cache_key: str, value: str, ttl: int) -> None:
    try:
        redis_client = get_redis()
        await redis_client.setex(cache_key, ttl, value)
    except Exception as e:
        logger.error(f"Failed to set cache: {e}")
```

**Decision**: Wrap Redis ops in try/except. Fail-open by default (log + continue).

**3. Caching Decorator (redis_cache.py)**

```python
def cache_response(ttl: int = CACHE_TTL):
    def decorator(func: Callable[..., Any]):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if not _aredis:
                return await func(*args, **kwargs)  # No Redis = skip cache

            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached = await safe_redis_get(cache_key)
            if cached:
                return json.loads(cached)

            result = await func(*args, **kwargs)
            await safe_redis_set(cache_key, serialize(result), ttl)
            return result
        return wrapper
    return decorator
```

**Decision**: Create similar decorator for balance caching, but simpler (key = user_id).

**4. Rate Limiting with Lua (rate_limit.py)**

```python
RATE_LIMIT_SCRIPT = """
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local current = redis.call('incr', key)
if current == 1 then
    redis.call('pexpire', key, window)
end
local ttl = redis.call('pttl', key)
if current > limit then
    return {current, window, ttl}
end
return {current, window, 0}
"""

# Execute atomically
current, window, ttl = await redis.evalsha(script_sha, 1, key, limit, window_ms)
```

**Decision**: Use Lua scripts for atomic token operations (check + deduct in one call).

**5. Graceful Degradation**

```python
# In rate_limit.py
except Exception as e:
    logger.error(f"Rate limit check failed: {e}")
    # Fail open but log the error
    return {"current": 1, "limit": limit, "remaining": limit - 1, ...}
```

**Decision**: Fail-open with logging when Redis unavailable. Configurable per spec.

---

## Technology Decisions

| Component     | Technology              | Rationale                                      |
| ------------- | ----------------------- | ---------------------------------------------- |
| **Framework** | FastAPI                 | Already used in study-mode-api, async-first    |
| **ORM**       | SQLModel                | Type-safe, async support, used in references   |
| **Database**  | PostgreSQL (Neon)       | Required by spec, proven patterns available    |
| **Cache**     | Redis (Upstash)         | Required by spec, sub-5ms reads                |
| **Auth**      | JWT verification        | Reuse existing SSO, extract user_id from sub   |
| **Testing**   | pytest-asyncio + SQLite | In-memory tests, JSONB patch for compatibility |
| **Config**    | pydantic_settings       | Type-safe env var loading                      |

---

## Architecture Approach

### Microservice Separation

```
study-mode-api                    token-metering-api
     |                                   |
     | HTTP (pre-check)                  |
     | ------------------>               |
     |                                   | Redis (fast)
     | <-- 200 OK / 402 Blocked          | PostgreSQL (persist)
     |                                   |
     | LLM call happens                  |
     |                                   |
     | HTTP (deduct)                     |
     | ------------------>               |
     |                                   | Atomic deduction
     | <-- 200 OK                        |
```

### Redis-First Architecture

**Why Redis-first?**

- Balance checks must complete in <5ms (spec FR-004)
- PostgreSQL round-trip is ~10-50ms to Neon
- Redis Upstash round-trip is ~1-3ms

**Cache Strategy**:

```
Read: Redis -> (cache miss) -> PostgreSQL -> write to Redis
Write: Redis + PostgreSQL (write-through)
```

**Key Schema** (metering: namespace per spec):

```
metering:account:{user_id}          # Cached account state (JSON)
metering:balance:{user_id}          # Quick balance lookup (integer)
metering:daily:{user_id}:{date}     # Daily counter
metering:monthly:{user_id}:{month}  # Monthly counter
metering:lifetime:{user_id}         # Lifetime counter
```

### Functional Service Layer

**Per spec constraint**: Prefer pure functions over classes.

```python
# services/metering.py - Functional style

async def check_balance(
    user_id: str,
    estimated_tokens: int,
    redis: Redis,
    session: AsyncSession,
) -> CheckResult:
    """Pure function: inputs -> outputs, no side effects on success path."""
    account = await get_cached_account(user_id, redis, session)
    tier = await get_tier(account.tier_name, redis, session)

    # Calculate available balance based on tier limits
    available = calculate_available(account, tier)

    if estimated_tokens > available:
        return CheckResult(allowed=False, reason=..., reset_at=...)

    return CheckResult(allowed=True, remaining=available - estimated_tokens)
```

### Atomic Token Operations

**Problem**: Race conditions between check and deduct.

**Solution**: Lua script for atomic operations (from enrollment pattern).

```lua
-- check_and_deduct.lua
local balance_key = KEYS[1]
local amount = tonumber(ARGV[1])

local balance = tonumber(redis.call('get', balance_key) or 0)
if balance < amount then
    return {0, balance}  -- Insufficient
end

local new_balance = redis.call('decrby', balance_key, amount)
return {1, new_balance}  -- Success
```

---

## Implementation Phases

### Phase 1: Core Metering (P1 User Story)

1. Database schema + migrations
2. Redis client setup
3. Check endpoint (pre-request)
4. Deduct endpoint (post-request)
5. Balance endpoint (query)

### Phase 2: Credit System (P2 User Story)

1. Grant endpoint (admin)
2. Two-balance consumption logic
3. Tier management endpoints

### Phase 3: Top-up & Analytics (P3-P4)

1. Top-up endpoint
2. Usage analytics endpoints
3. Admin dashboard queries

### Phase 4: Trial Users (P5)

1. Lifetime limit support
2. No-reset behavior

---

## Open Questions (Resolved)

| Question                                               | Resolution                                       |
| ------------------------------------------------------ | ------------------------------------------------ |
| How to handle negative balance from estimate mismatch? | Allow negative, flag for review (spec edge case) |
| Fail-open or fail-closed default?                      | Fail-open with logging (spec assumption)         |
| Sync vs async PostgreSQL?                              | Async (asyncpg) for consistency with reference   |
| Separate Redis connection pool?                        | Use existing Upstash, namespace isolation        |

---

## References

- taskforce_agent1/apps/api: FastAPI structure, SQLModel, auth, audit
- enrollment microservice: Redis caching, rate limiting, graceful degradation
- Spec: `/specs/001-freemium-tracker/spec.md`
