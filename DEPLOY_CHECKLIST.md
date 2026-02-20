# ⚡ Vercel Deployment - Quick Checklist

## Before Deploying

- [ ] Code pushed to GitHub (`imsanghaar/agentfactory`)
- [ ] On `main` branch
- [ ] No uncommitted changes
- [ ] `pnpm-lock.yaml` exists in repository
- [ ] `.nvmrc` file contains `20`
- [ ] Root `vercel.json` exists and is configured

## Deploy Steps

### 1. Go to Vercel
- Visit: [https://vercel.com](https://vercel.com)
- Login with GitHub account

### 2. Import Project
- Click **"Add New Project"**
- Select **"Import Git Repository"**
- Choose: `imsanghaar/agentfactory`

### 3. Configure Build Settings

**Framework Preset:** `Other`

**Root Directory:** `./` (leave as default)

**Build Command:**
```
cd apps/learn-app && node scripts/build.js
```

**Output Directory:**
```
apps/learn-app/build
```

**Install Command:**
```
pnpm install --frozen-lockfile
```

### 4. Environment Variables (Optional)

Click **"Environment Variables"** and add:

| Name | Value |
|------|-------|
| `NODE_VERSION` | `20` |
| `DEV_MODE` | `false` |

### 5. Deploy
- Click **"Deploy"**
- Wait 5-10 minutes for build to complete
- View deployment logs

### 6. Verify Deployment

After deployment completes, check:

- [ ] Homepage loads: `https://agentfactory-imsanghaar.vercel.app`
- [ ] Preface page works: `/docs/preface-agent-native`
- [ ] Video modal plays (click Play button)
- [ ] Navigation works
- [ ] Mobile view is responsive
- [ ] No console errors

---

## 🐛 If Deployment Fails

### Check Build Logs

1. Click on failed deployment in Vercel dashboard
2. Open "Build Logs"
3. Look for error messages

### Common Fixes

**Error: "Output directory not found"**
- Verify build runs locally: `cd apps/learn-app && pnpm run build`
- Check `vercel.json` has correct `outputDirectory`

**Error: "Module not found"**
- Delete `node_modules` and `pnpm-lock.yaml`
- Run: `pnpm install`
- Commit and push changes

**Error: "Build timeout"**
- Enable build cache in Vercel settings
- Set `DEV_MODE=true` temporarily

**Error: "Node version mismatch"**
- Ensure `.nvmrc` contains `20`
- Add `NODE_VERSION=20` in Vercel environment variables

---

## 📞 Need Help?

1. **Check Logs:** Vercel Dashboard → Deployments → View Logs
2. **Test Locally:** Run `pnpm run build` before pushing
3. **Review Config:** Check `vercel.json` and `package.json`
4. **Contact Team:** Open GitHub issue

---

## ✅ Successful Deployment

You should see:
```
✓ Build completed successfully
✓ Deployment ready
🎉 Your deployment is live!
```

**Production URL:** `https://agentfactory-imsanghaar.vercel.app`

---

**Quick Reference:** [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md) for detailed guide
