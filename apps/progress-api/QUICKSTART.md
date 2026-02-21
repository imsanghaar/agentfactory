# Quick Start Guide - Fixing Both Issues

## Issue 1: OAuth Callback Page Not Found

**Problem:** You accessed `http://localhost:3000/callback` but the page is at `/auth/callback`

**Solution:** The callback URL is already correctly configured. When you sign in, it will redirect to:
```
http://localhost:3000/auth/callback
```

This is configured in:
- `apps/sso/src/lib/trusted-clients.ts` - OAuth client redirect URLs
- `apps/learn-app/src/pages/auth/callback.tsx` - The callback page handler

**You don't need to change anything** - just make sure you're signing in through the proper OAuth flow (clicking "Sign In" button on the navbar).

---

## Issue 2: "Mark as Complete" Button Not Working

**Problem:** The Progress API server needs to be running on `http://localhost:8002`

**Solution:** Start the Progress API server

### Option A: Using the Start Script (Easiest)

1. **Open Command Prompt** and navigate to the progress-api folder:
   ```cmd
   cd E:\agentfactory\apps\progress-api
   ```

2. **Run the start script:**
   ```cmd
   start.bat
   ```

3. **Wait for the server to start** - you should see:
   ```
   ========================================
   Progress API - Starting Server
   ========================================
   
   Installing dependencies...
   
   ========================================
   Starting Progress API on port 8002
   ========================================
   
   Server will start at: http://localhost:8002
   Health check: http://localhost:8002/health
   ```

### Option B: Manual Start

1. **Navigate to the folder:**
   ```cmd
   cd E:\agentfactory\apps\progress-api
   ```

2. **Install dependencies (first time only):**
   ```cmd
   uv sync
   ```

3. **Start the server:**
   ```cmd
   uv run uvicorn progress_api.main:app --reload --port 8002
   ```

---

## Verify Everything is Working

### 1. Check Progress API Health

Open your browser and go to:
```
http://localhost:8002/health
```

You should see:
```json
{"status":"healthy"}
```

### 2. Test the OAuth Flow

1. Go to `http://localhost:3000`
2. Click "Sign In" in the navbar
3. You should be redirected to the auth server
4. After signing in, you'll be redirected to `http://localhost:3000/auth/callback`
5. The callback page will exchange the code for tokens
6. You'll be redirected back to the home page

### 3. Test "Mark as Complete"

1. Navigate to any lesson page (e.g., `/docs/...`)
2. Scroll to the bottom of the lesson
3. Click the "Mark as complete" button
4. You should see:
   - A checkmark icon
   - "+1 XP" badge
   - "Lesson complete — less than a minute of reading"

---

## Troubleshooting

### Progress API Won't Start

**Error: Database connection failed**

The `.env` file is configured to use SQLite by default. If you're still getting database errors:

1. Make sure the `.env` file exists:
   ```cmd
   if not exist .env copy .env.example .env
   ```

2. Check that it contains:
   ```env
   DATABASE_URL=sqlite+aiosqlite:///progress.db
   DEV_MODE=true
   ```

### "Mark as Complete" Still Not Working

1. **Check if the server is running:**
   ```cmd
   curl http://localhost:8002/health
   ```

2. **Check browser console for errors:**
   - Press F12 to open DevTools
   - Look for errors in the Console tab
   - Check the Network tab for failed API calls

3. **Make sure you're logged in:**
   - The button requires authentication
   - Check if your XP counter is visible in the navbar

### OAuth Callback Fails

1. **Check the redirect URI:**
   - It should be exactly: `http://localhost:3000/auth/callback`
   - No trailing slashes
   - Case-sensitive

2. **Clear browser cache:**
   ```javascript
   localStorage.clear()
   ```

3. **Check auth server is running:**
   ```cmd
   # Auth server should be on port 3001
   curl http://localhost:3001/api/auth/.well-known/openid-configuration
   ```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│  Learn App (Docusaurus) - http://localhost:3000            │
│  - Lesson pages with "Mark as complete" button             │
│  - OAuth callback handler at /auth/callback                │
└─────────────────────────────────────────────────────────────┘
         │                                    │
         │ OAuth flow                         │ Lesson completion
         ▼                                    ▼
┌────────────────────────┐        ┌────────────────────────────┐
│  Auth Server (SSO)     │        │  Progress API              │
│  http://localhost:3001 │        │  http://localhost:8002     │
│  - User authentication │        │  - XP tracking             │
│  - JWT token issuance  │        │  - Streak calculation      │
│  - JWKS endpoint       │        │  - Leaderboard             │
└────────────────────────┘        └────────────────────────────┘
                                          │
                                          ▼
                                 ┌────────────────────────────┐
                                 │  SQLite Database           │
                                 │  progress.db               │
                                 │  - User progress           │
                                 │  - Lesson completions      │
                                 │  - Quiz scores             │
                                 └────────────────────────────┘
```

---

## Next Steps

Once everything is working:

1. **Explore the Progress Dashboard:**
   - Visit `/progress` to see your learning stats
   - Check `/leaderboard` to see your ranking

2. **Customize Settings:**
   - Edit `.env` to use PostgreSQL instead of SQLite
   - Enable Redis for better caching
   - Configure production settings

3. **Development Mode:**
   - `DEV_MODE=true` bypasses authentication for easier testing
   - Set to `false` for production-like behavior

---

## Need Help?

If you encounter any issues:

1. Check the logs in the Command Prompt where the server is running
2. Look at browser console for client-side errors
3. Review the full documentation in `SETUP-WINDOWS.md`
