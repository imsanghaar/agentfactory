# Production Authentication Setup

## What Changed

The Progress API is now configured for **production authentication** instead of dev mode:
- `DEV_MODE=false` - JWT tokens are now required for authenticated endpoints
- The API will verify tokens using JWKS from the SSO server (`http://localhost:3001`)
- Your real user account will be shown on the leaderboard instead of "test-user"

## Current Status

✅ **Progress API**: Running on `http://localhost:8002` with production auth  
✅ **Learn App**: Running on `http://localhost:3000`  
✅ **SSO Server**: Running on `http://localhost:3001`  
✅ **Database**: Fresh database created (old test data cleared)

## How to Test the Full Flow

### Step 1: Sign In

1. Open your browser to: `http://localhost:3000`
2. Click **"Sign In"** in the navbar (top right)
3. You'll be redirected to the SSO server
4. Enter your credentials and sign in
5. You'll be redirected back to `/auth/callback`
6. After successful authentication, you'll be back on the home page

### Step 2: Verify You're Logged In

1. Look at the navbar - you should see your **avatar/initials** instead of "Sign In" buttons
2. Click on your avatar to open the dropdown
3. You should see:
   - Your name and email
   - Your XP counter (if you have any)
   - Software/Hardware tier info

### Step 3: Mark a Lesson as Complete

1. Navigate to any lesson (e.g., `/docs/...`)
2. Scroll to the bottom of the lesson
3. Click **"Mark as complete"**
4. You should see:
   - ✓ Checkmark icon
   - "+1 XP" badge
   - "Lesson complete — less than a minute of reading"

### Step 4: Check the Leaderboard

1. Click **"Leaderboard"** in the navbar
2. You should see **YOUR NAME** at rank #1 with 1 XP
3. No more "test-user" entries!

## How It Works

```
┌──────────────────────────────────────────────────────────────┐
│  You click "Mark as complete" in the browser                │
└──────────────────────────────────────────────────────────────┘
                          │
                          │ Sends POST request with JWT token
                          ▼
┌──────────────────────────────────────────────────────────────┐
│  Progress API (port 8002)                                    │
│  - Extracts JWT from Authorization header                    │
│  - Fetches JWKS from SSO server (port 3001)                  │
│  - Verifies token signature                                  │
│  - Extracts user info (sub, name, email)                     │
└──────────────────────────────────────────────────────────────┘
                          │
                          │ User is verified
                          ▼
┌──────────────────────────────────────────────────────────────┐
│  Database (SQLite)                                           │
│  - Creates user record with your real info                   │
│  - Records lesson completion                                 │
│  - Awards 1 XP                                               │
│  - Updates streak                                            │
└──────────────────────────────────────────────────────────────┘
                          │
                          │ Returns success
                          ▼
┌──────────────────────────────────────────────────────────────┐
│  Browser shows: "✓ Lesson complete +1 XP"                    │
└──────────────────────────────────────────────────────────────┘
```

## Troubleshooting

### "Could not save — check your connection"

**Cause**: Progress API not running or JWT token missing

**Fix**:
1. Make sure Progress API is running: `http://localhost:8002/health`
2. Make sure you're signed in (check navbar)
3. Try signing out and signing in again

### Leaderboard shows "null" or empty

**Cause**: No users have XP yet

**Fix**: Complete a lesson first, then check the leaderboard

### Token verification failed

**Cause**: SSO server not running or JWKS endpoint unavailable

**Fix**:
1. Check SSO server: `http://localhost:3001/api/auth/jwks`
2. Restart SSO server if needed

### "Invalid or expired token"

**Cause**: Token expired (tokens have limited validity)

**Fix**: Sign out and sign in again to get fresh tokens

## API Testing with curl

### Test without auth (should fail):
```bash
curl -X POST http://localhost:8002/api/v1/lesson/complete \
  -H "Content-Type: application/json" \
  -d '{"chapter_slug":"test","lesson_slug":"test","active_duration_secs":120}'
# Expected: 401 Unauthorized
```

### Test with valid JWT:
```bash
# Get token from browser console:
# localStorage.getItem('ainative_id_token')

curl -X POST http://localhost:8002/api/v1/lesson/complete \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE" \
  -d '{"chapter_slug":"test","lesson_slug":"test","active_duration_secs":120}'
# Expected: {"completed":true,"xp_earned":1,...}
```

## Server Management

### Restart Progress API:
```bash
cd E:\agentfactory\apps\progress-api
taskkill /F /IM python.exe
uv run uvicorn progress_api.main:app --port 8002
```

### Check if servers are running:
```bash
# Progress API
curl http://localhost:8002/health

# SSO Server
curl http://localhost:3001/api/auth/.well-known/openid-configuration

# Learn App
curl http://localhost:3000
```

## Security Notes

- JWT tokens are stored in `localStorage` (not cookies)
- Tokens are verified using JWKS public keys from SSO server
- Token audience is validated against `agent-factory-public-client`
- HTTPS is required in production (localhost HTTP is fine for dev)

---

## Status
✅ **PRODUCTION MODE ACTIVE** - Real authentication enabled
