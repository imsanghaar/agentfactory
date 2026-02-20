# ⚡ Vercel Deployment - Quick Reference

## 🎯 Your Configuration (Already Fixed)

**File:** `vercel.json` ✅ Updated
```json
{
  "buildCommand": "cd apps/learn-app && pnpm install && pnpm run build",
  "outputDirectory": "apps/learn-app/build",
  "installCommand": "corepack enable && pnpm install --frozen-lockfile",
  "framework": null
}
```

---

## 📤 Deploy Now (3 Steps)

### 1. Push to GitHub
```bash
git add .
git commit -m "Update vercel.json for deployment"
git push origin main
```

### 2. Go to Vercel
- Visit: [https://vercel.com/new](https://vercel.com/new)
- Import: `imsanghaar/agentfactory`

### 3. Configure & Deploy

**Build Command:**
```
cd apps/learn-app && pnpm install && pnpm run build
```

**Output Directory:**
```
apps/learn-app/build
```

**Install Command:**
```
corepack enable && pnpm install --frozen-lockfile
```

**Environment Variables:**
- `NODE_VERSION`: `20`
- `CI`: `false`

---

## 🔍 What Was Wrong

**Previous Issues:**
1. ❌ Complex rewrites conflicting with Docusaurus
2. ❌ Missing `corepack enable` for pnpm
3. ❌ Extra headers causing conflicts

**Now Fixed:**
- ✅ Simplified configuration
- ✅ Proper pnpm setup with corepack
- ✅ Clean build process

---

## ⏱️ Deployment Time

- **First Deploy:** 10-15 minutes
- **Future Deploys:** 5-8 minutes (with cache)

---

## ✅ After Deployment

**Your URL:**
```
https://agentfactory-imsanghaar.vercel.app
```

**Test Pages:**
- `/` - Homepage
- `/docs/preface-agent-native` - Preface with video modal
- Click Play button - Test projector animation

---

## 🐛 If It Still Fails

### Check Build Locally First
```bash
cd apps/learn-app
pnpm install
pnpm run build
# Should complete without errors
```

### View Vercel Logs
1. [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click your project
3. Click failed deployment
4. Open "Build Logs"
5. Screenshot the error

### Quick Fixes

**Error: "pnpm not found"**
→ Already fixed with `corepack enable`

**Error: "Output directory not found"**
→ Run `pnpm run build` locally first

**Error: "Build timeout"**
→ Wait it out (first build is slow)
→ Or set `DEV_MODE=true` temporarily

---

## 📞 Need Help?

1. **Check Logs:** Vercel Dashboard → Deployments → View Build Logs
2. **Test Locally:** Ensure `pnpm run build` works
3. **Share Error:** Screenshot build log for specific help

---

**Detailed Guide:** [`DEPLOY_TO_VERCEL.md`](./DEPLOY_TO_VERCEL.md)  
**Status:** Ready to Deploy ✅
