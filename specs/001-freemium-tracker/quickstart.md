# Quickstart: Token Metering API (v5)

**Feature**: 001-freemium-tracker
**Date**: 2026-02-05
**Version**: v5 - Balance Only

---

## Prerequisites

- Python 3.13+
- PostgreSQL 15+ (local or Neon)
- Redis 7+ (local or Upstash)
- uv (recommended) or pip

---

## Local Development Setup

### 1. Clone and Navigate

```bash
cd apps/token-metering-api
```

### 2. Create Virtual Environment

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate

# Or using standard venv
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# Using uv
uv pip install -e ".[dev]"

# Or using pip
pip install -e ".[dev]"
```

### 4. Environment Variables

Create a `.env` file in `apps/token-metering-api/`:

```bash
# Required
DATABASE_URL=postgresql://postgres:password@localhost:5432/metering
REDIS_URL=redis://localhost:6379
SSO_URL=http://localhost:3001

# Optional (defaults shown)
DEBUG=true
DEV_MODE=true
LOG_LEVEL=INFO
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001

# Redis (if using Upstash)
REDIS_PASSWORD=your-upstash-password

# Dev mode user (when DEV_MODE=true)
DEV_USER_ID=dev-user-123
DEV_USER_EMAIL=dev@localhost
DEV_USER_NAME=Dev User
```

### 5. Database Setup

**Option A: Local PostgreSQL**

```bash
# Create database
createdb metering

# Run migrations (auto-creates tables on startup in dev)
```

**Option B: Neon (Cloud)**

```bash
# Get connection string from Neon console
# Format: postgresql://user:pass@ep-xxx.region.aws.neon.tech/metering?sslmode=require
```

### 6. Redis Setup

**Option A: Local Redis**

```bash
# macOS
brew install redis
brew services start redis

# Docker
docker run -d -p 6379:6379 redis:7-alpine
```

**Option B: Upstash (Cloud)**

```bash
# Get connection details from Upstash console
REDIS_URL=rediss://default:xxx@region-xxx.upstash.io:6379
REDIS_PASSWORD=xxx
```

### 7. Start the Server

```bash
# Development with auto-reload
uvicorn src.token_metering_api.main:app --reload --port 8001

# Or using the provided script
./scripts/dev.sh
```

### 8. Verify Installation

```bash
# Health check
curl http://localhost:8001/health

# Expected response:
# {"status":"healthy","version":"1.0.0","redis":"connected","database":"connected"}

# API docs
open http://localhost:8001/docs
```

---

## Environment Variables Reference

| Variable          | Required | Default             | Description                                 |
| ----------------- | -------- | ------------------- | ------------------------------------------- |
| `DATABASE_URL`    | Yes      | -                   | PostgreSQL connection string                |
| `REDIS_URL`       | Yes      | -                   | Redis connection string                     |
| `SSO_URL`         | Yes      | -                   | SSO service URL for JWT validation          |
| `REDIS_PASSWORD`  | No       | -                   | Redis password (Upstash requires)           |
| `DEBUG`           | No       | false               | Enable debug logging                        |
| `DEV_MODE`        | No       | false               | Bypass JWT auth for local dev               |
| `DEV_USER_ID`     | No       | dev-user-123        | User ID when DEV_MODE=true                  |
| `DEV_USER_EMAIL`  | No       | dev@localhost       | Email when DEV_MODE=true                    |
| `DEV_USER_NAME`   | No       | Dev User            | Name when DEV_MODE=true                     |
| `LOG_LEVEL`       | No       | INFO                | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `ALLOWED_ORIGINS` | No       | localhost:3000,3001 | CORS allowed origins                        |
| `FAIL_OPEN`       | No       | true                | Allow requests when Redis unavailable       |
| `STARTER_TOKENS`  | No       | 50000               | Initial tokens for new users                |
| `INACTIVITY_EXPIRY_DAYS` | No | 365              | Days before balance expires                 |

---

## Testing Commands

### Run All Tests

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Verbose output
pytest -v
```

### Run Specific Test Categories

```bash
# Unit tests only (fast, no external deps)
pytest tests/unit/

# Integration tests (requires Redis, PostgreSQL)
pytest tests/integration/

# Single test file
pytest tests/unit/test_metering.py

# Single test function
pytest tests/unit/test_metering.py::test_check_balance_allowed
```

### Test with Coverage Report

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
open htmlcov/index.html
```

### Type Checking

```bash
# Run mypy
mypy src/

# With strict mode
mypy src/ --strict
```

### Linting

```bash
# Run ruff
ruff check src/ tests/

# Auto-fix
ruff check src/ tests/ --fix

# Format
ruff format src/ tests/
```

---

## Quick API Testing (v5)

### Check Balance (Pre-request)

```bash
# All fields required in v5: user_id, request_id, estimated_tokens, model
curl -X POST http://localhost:8001/api/v1/metering/check \
  -H "Content-Type: application/json" \
  -H "X-User-ID: dev-user-123" \
  -d '{
    "user_id": "dev-user-123",
    "request_id": "req-001",
    "estimated_tokens": 1500,
    "model": "deepseek-chat"
  }'
```

### Deduct Tokens (Post-request)

```bash
# Use reservation_id from check response
curl -X POST http://localhost:8001/api/v1/metering/deduct \
  -H "Content-Type: application/json" \
  -H "X-User-ID: dev-user-123" \
  -d '{
    "user_id": "dev-user-123",
    "request_id": "req-001",
    "reservation_id": "res_abc123",
    "input_tokens": 500,
    "output_tokens": 1000,
    "model": "deepseek-chat"
  }'
```

### Release Reservation (LLM Failed)

```bash
curl -X POST http://localhost:8001/api/v1/metering/release \
  -H "Content-Type: application/json" \
  -H "X-User-ID: dev-user-123" \
  -d '{
    "user_id": "dev-user-123",
    "request_id": "req-001",
    "reservation_id": "res_abc123"
  }'
```

### Get Balance

```bash
# v5 returns: balance, effective_balance, is_expired
curl http://localhost:8001/api/v1/balance \
  -H "X-User-ID: dev-user-123"
```

### Grant Tokens (Admin)

```bash
curl -X POST http://localhost:8001/api/v1/admin/grant \
  -H "Content-Type: application/json" \
  -H "X-User-ID: admin-user" \
  -d '{
    "user_id": "user_123",
    "tokens": 500000,
    "reason": "Student enrollment"
  }'
```

### Topup Tokens (Admin)

```bash
curl -X POST http://localhost:8001/api/v1/admin/topup \
  -H "Content-Type: application/json" \
  -H "X-User-ID: admin-user" \
  -d '{
    "user_id": "user_123",
    "tokens": 100000,
    "payment_reference": "stripe_pi_xyz789"
  }'
```

---

## Docker Development

### Build Image

```bash
docker build -t token-metering-api .
```

### Run with Docker Compose

```bash
# Start all services (API, PostgreSQL, Redis)
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop
docker-compose down
```

### docker-compose.yml Example

```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8001:8001"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/metering
      - REDIS_URL=redis://redis:6379
      - SSO_URL=http://host.docker.internal:3001
      - DEV_MODE=true
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=metering
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

## Integration with study-mode-api

### Pre-request Hook

```python
# In study-mode-api/src/hooks/metering.py
import httpx

METERING_API_URL = "http://localhost:8001"

async def pre_request_hook(user_id: str, estimated_tokens: int, model: str) -> bool:
    """Check if user has sufficient balance."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{METERING_API_URL}/api/v1/metering/check",
            json={
                "estimated_tokens": estimated_tokens,
                "model": model,
            },
            headers={"Authorization": f"Bearer {get_user_token(user_id)}"},
            timeout=5.0,  # Fail fast
        )

        if response.status_code == 402:
            # User blocked - return error to frontend
            data = response.json()
            raise InsufficientBalanceError(data["message"])

        return response.json()["allowed"]
```

### Post-request Hook

```python
async def post_request_hook(
    user_id: str,
    input_tokens: int,
    output_tokens: int,
    model: str,
    lesson_path: str | None = None,
) -> None:
    """Deduct tokens after successful LLM response."""
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{METERING_API_URL}/api/v1/metering/deduct",
            json={
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "model": model,
                "lesson_path": lesson_path,
            },
            headers={"Authorization": f"Bearer {get_user_token(user_id)}"},
        )
```

---

## Troubleshooting

### Common Issues

**1. Redis Connection Error**

```
ConnectionError: Error connecting to Redis
```

Solution: Ensure Redis is running and REDIS_URL is correct.

```bash
# Check Redis
redis-cli ping
# Should return: PONG
```

**2. Database Connection Error**

```
OperationalError: could not connect to server
```

Solution: Check PostgreSQL is running and DATABASE_URL is correct.

```bash
# Check PostgreSQL
psql -h localhost -U postgres -c "SELECT 1"
```

**3. JWT Validation Fails**

```
401 Unauthorized: Invalid JWT
```

Solution: Enable DEV_MODE for local testing, or ensure SSO_URL is correct.

```bash
DEV_MODE=true
```

**4. CORS Errors in Browser**

Solution: Add your frontend URL to ALLOWED_ORIGINS.

```bash
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

---

## Performance Testing

### Load Test with k6

```javascript
// load-test.js
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 100,
  duration: "30s",
};

export default function () {
  const res = http.post(
    "http://localhost:8001/api/v1/metering/check",
    JSON.stringify({ estimated_tokens: 1500 }),
    { headers: { "Content-Type": "application/json" } },
  );

  check(res, {
    "status is 200": (r) => r.status === 200,
    "response time < 5ms": (r) => r.timings.duration < 5,
  });

  sleep(0.1);
}
```

```bash
k6 run load-test.js
```

---

## Next Steps

1. Complete Phase 1 implementation (core metering)
2. Add unit tests for all service functions
3. Add integration tests with test database
4. Deploy to development environment
5. Integrate with study-mode-api hooks
