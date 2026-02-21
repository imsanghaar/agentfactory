# Progress API Setup Guide

The Progress API provides gamification features (XP, badges, streaks, leaderboard) for the learning platform.

## Quick Start

### 1. Start Infrastructure (PostgreSQL + Redis)

```bash
cd apps/progress-api
docker compose up -d
```

This starts:
- **PostgreSQL** on port `5433` (database for progress data)
- **Redis** on port `6380` (caching for leaderboard)

### 2. Set Up Environment

```bash
# Copy example environment file
copy .env.example .env
```

### 3. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

### 4. Run the Server

```bash
# Using nx
nx serve progress-api

# Or directly
uv run uvicorn progress_api.main:app --reload --port 8002
```

### 5. Verify It's Working

```bash
# Health check
curl http://localhost:8002/health

# Get leaderboard (should return empty list initially)
curl http://localhost:8002/api/v1/leaderboard
```

## Testing the Leaderboard

### Submit a Quiz Score (to get XP)

```bash
curl -X POST http://localhost:8002/api/v1/quiz/submit ^
  -H "Content-Type: application/json" ^
  -H "X-User-ID: test-user-123" ^
  -d "{\"quiz_id\":\"quiz-1\",\"score\":85,\"time_spent_seconds\":120}"
```

### Check Leaderboard

```bash
curl http://localhost:8002/api/v1/leaderboard
```

Expected response:
```json
{
  "entries": [
    {
      "rank": 1,
      "user_id": "test-user-123",
      "display_name": "Test User",
      "avatar_url": null,
      "total_xp": 85,
      "badge_count": 0,
      "badge_ids": []
    }
  ],
  "current_user_rank": null,
  "total_users": 1
}
```

## Database Initialization

The first time you run the Progress API, you need to initialize the database:

```bash
# Run database migrations / create tables
uv run python -c "from progress_api.core.database import create_tables; import asyncio; asyncio.run(create_tables())"
```

Or visit `http://localhost:8002/docs` and use the interactive API docs.

## Troubleshooting

### "Connection refused" on port 8002
- Make sure the server is running: `netstat -ano | findstr :8002`
- Check for errors in the terminal where you ran `uvicorn`

### "Connection refused" on port 5433 or 6380
- Docker containers may not be running: `docker compose ps`
- Restart them: `docker compose down && docker compose up -d`

### Leaderboard returns empty list
- No users have XP yet - submit some quiz scores first
- The materialized view may need refreshing (automatic on first data)

### Database tables don't exist
- Run the table creation script (see Database Initialization above)
- Check `DATABASE_URL` in `.env` matches your Docker setup

## Architecture

```
┌─────────────────┐
│   Learn App     │
│  (Docusaurus)   │
└────────┬────────
         │ HTTP /api/v1/leaderboard
         ▼
┌─────────────────┐
│  Progress API   │
│   (FastAPI)     │
│   Port: 8002    │
└────────┬────────┘
         │
    ┌────┴────
    ▼         ▼
┌──────┐   ┌──────┐
│Postgres│  │Redis │
│:5433  │   │:6380 │
└──────┘   └──────┘
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+asyncpg://progress:progress@localhost:5433/progress` |
| `REDIS_URL` | Redis connection string | `redis://localhost:6380` |
| `DEV_MODE` | Bypass auth for local dev | `true` |
| `DEV_USER_ID` | Default user ID in dev mode | `dev-user-123` |
| `PORT` | Server port | `8002` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `http://localhost:3000` |

## Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run integration tests only
uv run pytest tests/integration/ -v

# Run with coverage
uv run pytest tests/ --cov=progress_api --cov-report=term-missing
```
