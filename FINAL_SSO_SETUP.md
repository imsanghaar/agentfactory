# 🚀 Final SSO Domain Setup Guide

## ✅ Final Domain Configuration

| App | URL | Status |
|-----|-----|--------|
| **Auth Server** | `https://auth-agentfactory.vercel.app` | ✅ **FINAL** |
| **Book/Learn App** | `https://agentfactory-imsanghaar.vercel.app` | ✅ Active |
| Old Auth Domain 1 | `https://auth-imsanghaar.vercel.app` | ❌ Deprecated |
| Old Auth Domain 2 | `https://auth-imsanghaar-agentfactory.vercel.app` | ❌ Deprecated |

---

## 🔧 Vercel Environment Variables Setup

### 1. Auth Server (`auth-agentfactory.vercel.app`)

Go to: **Vercel Dashboard** → `auth-agentfactory` project → **Settings** → **Environment Variables**

| Variable | Value | Scope |
|----------|-------|-------|
| `BETTER_AUTH_URL` | `https://auth-agentfactory.vercel.app` | Production |
| `NEXT_PUBLIC_BETTER_AUTH_URL` | `https://auth-agentfactory.vercel.app` | Production |
| `ALLOWED_ORIGINS` | `https://agentfactory-imsanghaar.vercel.app,https://auth-agentfactory.vercel.app` | Production |
| `DATABASE_URL` | Your Neon PostgreSQL URL | Production |
| `BETTER_AUTH_SECRET` | Your 32+ character secret | Production |
| `NODE_ENV` | `production` | Production |
| `NEXT_PUBLIC_APP_NAME` | `imsanghaar SSO` | Production (Optional) |
| `NEXT_PUBLIC_ORG_NAME` | `imsanghaar` | Production (Optional) |
| `NEXT_PUBLIC_CONTINUE_URL` | `https://agentfactory-imsanghaar.vercel.app` | Production (Optional) |

**After updating:** Click **Redeploy** on the latest deployment.

---

### 2. Book/Learn App (`agentfactory-imsanghaar.vercel.app`)

Go to: **Vercel Dashboard** → `agentfactory-imsanghaar` project → **Settings** → **Environment Variables**

| Variable | Value | Scope |
|----------|-------|-------|
| `AUTH_URL` | `https://auth-agentfactory.vercel.app` | Production |
| `SSO_URL` | `https://auth-agentfactory.vercel.app` | Production |
| `OAUTH_CLIENT_ID` | `agent-factory-public-client` | Production |
| `DATABASE_URL` | Your Neon PostgreSQL URL | Production |
| `NODE_ENV` | `production` | Production |

**After updating:** Click **Redeploy** on the latest deployment.

---

## ✅ Testing Checklist

### Test 1: Auth Server Loads
```
Visit: https://auth-agentfactory.vercel.app/auth/sign-in
✅ Should show sign-in form without errors
```

### Test 2: Direct Sign-In
```
1. Enter email: imamsanghaar@gmail.com
2. Enter password: imsanghaar
3. Click "Sign in"
✅ Should redirect to home page successfully
```

### Test 3: Book App → Auth Server → Book App Flow
```
1. Visit: https://agentfactory-imsanghaar.vercel.app
2. Click "Sign In" in navbar
3. Should redirect to: https://auth-agentfactory.vercel.app/api/auth/oauth2/authorize...
4. Sign in with credentials
5. Should redirect back to book app
✅ Should show signed-in state in navbar
```

### Test 4: Admin Access (if needed)
```
1. Visit: https://auth-agentfactory.vercel.app/admin
2. Sign in with admin credentials
3. If access denied, run this SQL in Neon:
   UPDATE "user" SET role = 'admin', email_verified = true 
   WHERE email = 'imamsanghaar@gmail.com';
✅ Should show admin dashboard
```

---

## 🐛 Troubleshooting

### CORS Error: "No 'Access-Control-Allow-Origin' header"

**Cause:** `ALLOWED_ORIGINS` doesn't include the book app domain

**Fix:**
1. Update `ALLOWED_ORIGINS` in auth server's Vercel environment
2. Add: `https://agentfactory-imsanghaar.vercel.app`
3. Redeploy auth server

### Error: "Token exchange failed"

**Possible causes:**
1. OAuth client not in database
2. Redirect URI mismatch

**Fix:**
1. Ensure `agent-factory-public-client` is seeded
2. Check redirect URI matches exactly: `https://agentfactory-imsanghaar.vercel.app/auth/callback`

### Error: "Database does not exist"

**Fix:**
1. Go to [Neon Dashboard](https://console.neon.tech)
2. Copy connection string
3. Update `DATABASE_URL` in both Vercel projects

---

## 📝 Files Updated

The following files have been updated with the final domain:

1. ✅ `apps/learn-app/docusaurus.config.ts` - Default AUTH_URL
2. ✅ `apps/learn-app/.env.example` - AUTH_URL and SSO_URL
3. ✅ `apps/sso/.env.vercel.template` - BETTER_AUTH_URL and ALLOWED_ORIGINS

---

## 🔐 Security Notes

1. **Never commit `.env.local`** with real values to Git
2. **Use different secrets** for development and production
3. **HTTPS only** in production (already configured)
4. **Restrict `ALLOWED_ORIGINS`** to only your domains

---

## 📞 Quick Links

- **Vercel Dashboard:** https://vercel.com/dashboard
- **Neon Database:** https://console.neon.tech
- **Auth Server (Final):** https://auth-agentfactory.vercel.app
- **Book/Learn App:** https://agentfactory-imsanghaar.vercel.app
- **Admin Panel:** https://auth-agentfactory.vercel.app/admin

---

## ✅ Final Checklist

- [ ] Updated auth server environment variables in Vercel
- [ ] Updated book app environment variables in Vercel
- [ ] Redeployed auth server
- [ ] Redeployed book app
- [ ] Tested direct sign-in on auth server
- [ ] Tested OAuth flow from book app
- [ ] Created admin user (if needed)
- [ ] Verified no CORS errors in console
