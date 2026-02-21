# Progress API - Quick Setup without Docker

## The Issue
The Progress API requires PostgreSQL and Redis. Since Docker is not available, you need to install them locally.

## Option 1: Install PostgreSQL + Redis Locally (Full Setup)

### Step 1: Install PostgreSQL

1. **Download PostgreSQL 16** from:
   https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
   
2. **During installation:**
   - Keep default port: `5432`
   - Remember the password you set for `postgres` user
   - Install pgAdmin (optional but helpful)

3. **Create the database:**
   ```bash
   # Open Command Prompt and run:
   psql -U postgres
   
   # In psql prompt:
   CREATE DATABASE progress;
   CREATE USER progress WITH PASSWORD 'progress';
   GRANT ALL PRIVILEGES ON DATABASE progress TO progress;
   \q
   ```

### Step 2: Install Redis for Windows

Redis doesn't have official Windows support, but you have options:

**Option A: Use Memurai (Redis-compatible, free for dev)**
- Download: https://www.memurai.com/
- Install and it runs as a Windows service

**Option B: Use WSL2 (Windows Subsystem for Linux)**
```bash
wsl sudo apt update
wsl sudo apt install redis-server
wsl redis-server --daemonize yes
```

**Option C: Skip Redis (caching disabled, slower but works)**
- Just don't set `REDIS_URL` in `.env`
- The app will work without caching

### Step 3: Configure .env

Create `.env` file in `apps/progress-api`:

```env
# Database - update password if you changed it
DATABASE_URL=postgresql+asyncpg://progress:progress@localhost:5432/progress

# Redis - skip this line if not using Redis
REDIS_URL=redis://localhost:6379

# SSO/Auth
SSO_URL=http://localhost:3001
JWKS_CACHE_TTL=3600
TOKEN_AUDIENCE=progress-api

# CORS
ALLOWED_ORIGINS=http://localhost:3000

# Debug
DEBUG=true
LOG_LEVEL=INFO

# Dev mode - bypasses auth for local development
DEV_MODE=true
DEV_USER_ID=dev-user-123

# Server
PORT=8002
ENVIRONMENT=development
```

### Step 4: Run the Progress API

```bash
cd E:\agentfactory\apps\progress-api
uv run uvicorn progress_api.main:app --reload --port 8002
```

---

## Option 2: Use SQLite (Fastest Setup, Limited Features)

I can modify the Progress API to use SQLite for local development. This is the quickest way to get started.

### Create SQLite-compatible config:

1. **Create `.env` file:**
```env
DATABASE_URL=sqlite+aiosqlite:///progress.db
REDIS_URL=
DEV_MODE=true
DEV_USER_ID=dev-user-123
PORT=8002
DEBUG=true
```

2. **Install SQLite support:**
```bash
cd E:\agentfactory\apps\progress-api
uv add aiosqlite
```

3. **Run the API:**
```bash
uv run uvicorn progress_api.main:app --reload --port 8002
```

**Note:** SQLite won't support materialized views (leaderboard will use live queries), but it's perfect for local development.

---

## Verify It's Working

```bash
# Health check
curl http://localhost:8002/health

# Test leaderboard (should return empty list)
curl http://localhost:8002/api/v1/leaderboard
```

---

## Recommended: Quick Start with PostgreSQL

For the best experience, I recommend:

1. **Install PostgreSQL** (5 min download + install)
2. **Skip Redis for now** (app will work, just slower)
3. **Use this `.env`:**

```env
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/progress
REDIS_URL=
DEV_MODE=true
DEV_USER_ID=dev-user-123
PORT=8002
DEBUG=true
ALLOWED_ORIGINS=http://localhost:3000
```

Replace `YOUR_PASSWORD` with the password you set during PostgreSQL installation.

---

## Need Help?

If you want me to:
- Modify the code to support SQLite
- Create a setup script to automate PostgreSQL installation
- Provide alternative solutions

Just ask!
