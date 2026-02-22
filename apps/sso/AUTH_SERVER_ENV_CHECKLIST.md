# ✅ Auth Server Environment Variables Checklist

## Go to: Vercel Dashboard → **auth-agentfactory** project → Settings → Environment Variables

### 🔑 REQUIRED Variables

| Variable | Value | Why It's Needed |
|----------|-------|-----------------|
| `BETTER_AUTH_URL` | `https://auth-agentfactory.vercel.app` | Auth server's backend URL |
| `NEXT_PUBLIC_BETTER_AUTH_URL` | `https://auth-agentfactory.vercel.app` | Auth server's client-side URL |
| `ALLOWED_ORIGINS` | `https://agentfactory-imsanghaar.vercel.app,https://auth-agentfactory.vercel.app` | CORS - allows book app to connect |
| `DATABASE_URL` | Your Neon PostgreSQL URL | Database connection |
| `BETTER_AUTH_SECRET` | 32+ character secret | JWT signing & encryption |
| `NODE_ENV` | `production` | Environment mode |

### 🎨 OPTIONAL Variables (Recommended)

| Variable | Value | Purpose |
|----------|-------|---------|
| `NEXT_PUBLIC_APP_NAME` | `imsanghaar SSO` | App name in UI |
| `NEXT_PUBLIC_ORG_NAME` | `imsanghaar` | Organization name |
| `NEXT_PUBLIC_CONTINUE_URL` | `https://agentfactory-imsanghaar.vercel.app` | Where users go after auth |
| `RESEND_API_KEY` | Your Resend key | Email verification (if using Resend) |
| `EMAIL_FROM` | `noreply@yourdomain.com` | Email from address |

---

## ⚠️ Critical: ALLOWED_ORIGINS

This is the **most important** variable for CORS to work:

```
ALLOWED_ORIGINS=https://agentfactory-imsanghaar.vercel.app,https://auth-agentfactory.vercel.app
```

**Must include:**
1. Your book app domain: `https://agentfactory-imsanghaar.vercel.app`
2. Your auth server domain: `https://auth-agentfactory.vercel.app`

**Format:** Comma-separated, no spaces, full URLs with `https://`

---

## ✅ After Updating

1. **Save** all environment variables
2. Go to **Deployments** tab
3. Click **Redeploy** on latest deployment
4. Wait 2-3 minutes

---

## 🧪 Test After Redeploy

### Test 1: Auth Server Loads
```
Visit: https://auth-agentfactory.vercel.app/auth/sign-in
✅ Should show sign-in form (no 500 error)
```

### Test 2: Direct Sign-In
```
1. Enter email: imamsanghaar@gmail.com
2. Enter password: imsanghaar  
3. Click "Sign in"
✅ Should redirect to home page (no CORS error)
```

### Test 3: OAuth from Book App
```
1. Visit: https://agentfactory-imsanghaar.vercel.app
2. Click "Sign In" in navbar
3. Should redirect to: https://auth-agentfactory.vercel.app/api/auth/oauth2/authorize...
4. Sign in
5. Should redirect back to book app
✅ No CORS errors in console
```

### Test 4: Admin Panel (if needed)
```
Visit: https://auth-agentfactory.vercel.app/admin
✅ Should show admin dashboard (if user has admin role)
```

---

## 🐛 Troubleshooting

### Error: "BETTER_AUTH_SECRET must be at least 32 characters"

**Generate a new secret:**
```bash
openssl rand -base64 32
```
Copy output and update `BETTER_AUTH_SECRET` in Vercel.

### Error: "Database does not exist"

**Fix:**
1. Go to [Neon Dashboard](https://console.neon.tech)
2. Copy connection string (Pooler mode)
3. Update `DATABASE_URL` in Vercel

### Error: "CORS policy: No 'Access-Control-Allow-Origin'"

**Fix:**
1. Update `ALLOWED_ORIGINS` to include both domains
2. Make sure there are **no spaces** in the value
3. Redeploy

---

## 📋 Quick Summary

**Minimum required to work:**
- ✅ `BETTER_AUTH_URL` = `https://auth-agentfactory.vercel.app`
- ✅ `NEXT_PUBLIC_BETTER_AUTH_URL` = `https://auth-agentfactory.vercel.app`
- ✅ `ALLOWED_ORIGINS` = `https://agentfactory-imsanghaar.vercel.app,https://auth-agentfactory.vercel.app`
- ✅ `DATABASE_URL` = (your Neon URL)
- ✅ `BETTER_AUTH_SECRET` = (32+ chars)
- ✅ `NODE_ENV` = `production`

**After setting these, redeploy!**

---

## 🔗 Quick Links

- **Vercel Dashboard:** https://vercel.com/dashboard
- **Auth Server Project:** Find `auth-agentfactory`
- **Neon Database:** https://console.neon.tech
- **Auth Server Live:** https://auth-agentfactory.vercel.app
