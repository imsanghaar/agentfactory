# 🚨 URGENT: Book App Environment Variables Update Required

## Problem

Your book app (`agentfactory-imsanghaar.vercel.app`) is still trying to authenticate with the **old auth domain**:

```
❌ Old (wrong): https://auth-imsanghaar.vercel.app
✅ New (correct): https://auth-imsanghaar-agentfactory.vercel.app
```

This is why you're getting CORS errors - the book app is sending requests to the wrong domain!

---

## ✅ Solution: Update Book App's Vercel Environment Variables

### Step 1: Go to Vercel Dashboard

1. Visit: https://vercel.com/dashboard
2. Select your project: **agentfactory-imsanghaar** (the book/learn app)
3. Go to **Settings** → **Environment Variables**

### Step 2: Update These Variables

Find and **UPDATE** these existing variables:

| Variable | OLD Value (❌ Wrong) | NEW Value (✅ Correct) |
|----------|---------------------|------------------------|
| `AUTH_URL` | `https://agentfactory.imsanghaar-sso.vercel.app` | `https://auth-imsanghaar-agentfactory.vercel.app` |
| `SSO_URL` | `https://agentfactory.imsanghaar-sso.vercel.app` | `https://auth-imsanghaar-agentfactory.vercel.app` |

### Step 3: Redeploy

After updating environment variables:

1. Go to **Deployments** tab
2. Click **Redeploy** on the latest deployment
3. Wait ~2-3 minutes for deployment to complete

---

## 🧪 Test After Redeploy

1. Visit: https://agentfactory-imsanghaar.vercel.app
2. Click "Sign In" in navbar
3. Sign in with your credentials
4. ✅ Should redirect to **new** auth domain and back successfully

---

## 📝 Summary of Domains

| App | URL | Purpose |
|-----|-----|---------|
| **Auth Server (NEW)** | `https://auth-imsanghaar-agentfactory.vercel.app` | Handles login/signup |
| **Book/Learn App** | `https://agentfactory-imsanghaar.vercel.app` | The main learning platform |
| **Auth Server (OLD)** | `https://auth-imsanghaar.vercel.app` | ❌ Deprecated - don't use |

---

## ⚠️ Why This Happens

When you changed the auth server domain, the book app's environment variables weren't updated. The book app reads `AUTH_URL` from Vercel environment variables to know where to send authentication requests.

**Before:**
```
Book App → AUTH_URL=https://agentfactory.imsanghaar-sso.vercel.app → Old Domain
```

**After:**
```
Book App → AUTH_URL=https://auth-imsanghaar-agentfactory.vercel.app → New Domain ✅
```

---

## ✅ Checklist

- [ ] Updated `AUTH_URL` in book app's Vercel environment
- [ ] Updated `SSO_URL` in book app's Vercel environment
- [ ] Redeployed the book app
- [ ] Tested sign-in from book app
- [ ] Verified redirect goes to new auth domain

---

## 🔗 Quick Links

- **Book App Vercel:** https://vercel.com/dashboard (find `agentfactory-imsanghaar`)
- **Auth Server Vercel:** https://vercel.com/dashboard (find `auth-imsanghaar-agentfactory`)
- **Book App (Live):** https://agentfactory-imsanghaar.vercel.app
- **Auth Server (Live):** https://auth-imsanghaar-agentfactory.vercel.app
