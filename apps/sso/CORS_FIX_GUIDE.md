# 🔧 CORS Error Fix Guide

## Problem

```
Access to fetch at 'https://auth-imsanghaar.vercel.app/api/auth/sign-in/email' 
from origin 'https://auth-imsanghaar-agentfactory.vercel.app' has been blocked 
by CORS policy
```

**Root Cause:** Your auth server moved to a new domain (`auth-imsanghaar-agentfactory.vercel.app`) but the environment variables still reference the old domain.

---

## ✅ Solution: Update Vercel Environment Variables

### Step 1: Go to Vercel Dashboard

1. Visit: https://vercel.com/dashboard
2. Select your project: **auth-imsanghaar-agentfactory**
3. Go to **Settings** → **Environment Variables**

### Step 2: Add/Update These Variables

| Variable | Value | Scope |
|----------|-------|-------|
| `BETTER_AUTH_URL` | `https://auth-imsanghaar-agentfactory.vercel.app` | Production |
| `NEXT_PUBLIC_BETTER_AUTH_URL` | `https://auth-imsanghaar-agentfactory.vercel.app` | Production |
| `ALLOWED_ORIGINS` | `https://agentfactory-imsanghaar.vercel.app,https://auth-imsanghaar-agentfactory.vercel.app` | Production |
| `DATABASE_URL` | Your Neon PostgreSQL URL | Production |
| `BETTER_AUTH_SECRET` | Your 32+ char secret | Production |
| `NODE_ENV` | `production` | Production |

### Step 3: Redeploy

After updating environment variables:

1. Go to **Deployments** tab
2. Click **Redeploy** on the latest deployment
3. Wait ~2-3 minutes for deployment to complete

---

## 🔍 Why This Happens

### CORS (Cross-Origin Resource Sharing)

When your browser tries to sign in from `auth-imsanghaar-agentfactory.vercel.app`, it sends a request to the auth API. The server must explicitly allow this origin via the `ALLOWED_ORIGINS` environment variable.

**What was broken:**
- Old domain: `auth-imsanghaar.vercel.app`
- New domain: `auth-imsanghaar-agentfactory.vercel.app`
- `ALLOWED_ORIGINS` didn't include the new domain
- `BETTER_AUTH_URL` still pointed to old domain

---

## ✅ Verification Checklist

After redeploying, test these:

### Test 1: Sign-In Page Loads
```
Visit: https://auth-imsanghaar-agentfactory.vercel.app/auth/sign-in
✅ Should show sign-in form (no errors)
```

### Test 2: Sign-In Works
```
1. Enter email: imamsanghaar@gmail.com
2. Enter password: imsanghaar
3. Click "Sign in"
✅ Should redirect successfully (no CORS error)
```

### Test 3: Sign-Up Works
```
1. Visit: https://auth-imsanghaar-agentfactory.vercel.app/auth/sign-up
2. Fill in the form
3. Click "Create account"
✅ Should show success message
```

### Test 4: Book App Integration
```
1. Visit: https://agentfactory-imsanghaar.vercel.app
2. Click "Sign In" in navbar
✅ Should redirect to auth server and back successfully
```

---

## 🐛 Additional Troubleshooting

### Error: "BETTER_AUTH_SECRET must be at least 32 characters"

**Fix:**
```bash
# Generate a new secret
openssl rand -base64 32
```
Copy the output and update `BETTER_AUTH_SECRET` in Vercel.

### Error: "Database does not exist"

**Fix:**
1. Go to [Neon Dashboard](https://console.neon.tech)
2. Copy your database connection string
3. Update `DATABASE_URL` in Vercel

### Error: "Token exchange failed"

**Possible causes:**
1. OAuth client not registered in database
2. Redirect URI mismatch

**Fix:**
1. Ensure `agent-factory-public-client` is seeded (run `pnpm seed:setup` if needed)
2. Check that redirect URI exactly matches (including trailing slash)

---

## 📝 File Changes Made

The following files were updated to use the new domain:

1. **apps/learn-app/.env.example** - Updated AUTH_URL and SSO_URL
2. **apps/learn-app/docusaurus.config.ts** - Updated default AUTH_URL
3. **apps/sso/.env.vercel.template** - Created template with new domain

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
- **Auth Server (New):** https://auth-imsanghaar-agentfactory.vercel.app
- **Book/Learn App:** https://agentfactory-imsanghaar.vercel.app

---

## ✅ Final Checklist

- [ ] Updated `BETTER_AUTH_URL` to new domain in Vercel
- [ ] Updated `NEXT_PUBLIC_BETTER_AUTH_URL` to new domain
- [ ] Added new domain to `ALLOWED_ORIGINS`
- [ ] Redeployed the application
- [ ] Tested sign-in (no CORS error)
- [ ] Tested sign-up
- [ ] Tested book app integration
- [ ] Created admin user (if not exists)
