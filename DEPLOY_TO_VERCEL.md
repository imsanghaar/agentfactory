# 🚀 Deploy to Vercel - Step by Step Guide

## ⚡ Quick Fix - Why Vercel Isn't Deploying

Your `vercel.json` configuration looks correct, but here are the common issues and solutions:

---

## 🔧 Solution 1: Update vercel.json (Recommended)

Replace your root `vercel.json` with this **simplified version**:

```json
{
  "buildCommand": "cd apps/learn-app && pnpm install && pnpm run build",
  "outputDirectory": "apps/learn-app/build",
  "installCommand": "pnpm install --frozen-lockfile",
  "framework": null
}
```

**Changes Made:**
- Removed complex rewrites (causing issues)
- Simplified build command
- Kept essential configuration only

---

## 📋 Solution 2: Deploy via Vercel Dashboard (Easiest)

### Step 1: Go to Vercel
1. Visit [https://vercel.com](https://vercel.com)
2. Login with GitHub
3. Click **"Add New Project"**

### Step 2: Import Repository
- Select: **`imsanghaar/agentfactory`**
- Click **"Import"**

### Step 3: Configure Build Settings

**Framework Preset:** `Other`

**Root Directory:** `./` (leave empty)

**Build Command:**
```bash
cd apps/learn-app && pnpm install && pnpm run build
```

**Output Directory:**
```bash
apps/learn-app/build
```

**Install Command:**
```bash
pnpm install --frozen-lockfile
```

### Step 4: Add Environment Variables

Click **"Environment Variables"** → Add these:

| Key | Value |
|-----|-------|
| `NODE_VERSION` | `20` |
| `CI` | `false` |

### Step 5: Deploy
- Click **"Deploy"**
- Wait 10-15 minutes (first build takes longer)
- View logs to monitor progress

---

## 🖥️ Solution 3: Deploy via Vercel CLI

### Install Vercel CLI
```bash
npm install -g vercel
```

### Login to Vercel
```bash
vercel login
```

### Deploy to Preview
```bash
cd E:\agentfactory
vercel
```

### Deploy to Production
```bash
vercel --prod
```

---

## 🐛 Common Deployment Errors & Fixes

### Error 1: "Command failed: pnpm"

**Problem:** Vercel can't find pnpm

**Fix:** Add to `vercel.json`:
```json
{
  "installCommand": "corepack enable && pnpm install --frozen-lockfile"
}
```

### Error 2: "Output directory not found"

**Problem:** Build didn't create the output folder

**Fix:** 
1. Test build locally first:
```bash
cd apps/learn-app
pnpm install
pnpm run build
ls build/  # Should show files
```

2. If build fails locally, fix errors first

### Error 3: "Build timeout"

**Problem:** Build takes too long (>15 min)

**Fix:** 
- Enable **Build Cache** in Vercel settings
- Set `DEV_MODE=true` temporarily to skip heavy features
- Check for infinite loops in build scripts

### Error 4: "Module not found"

**Problem:** Missing dependencies

**Fix:**
```bash
# Delete and reinstall
rm -rf node_modules apps/*/node_modules pnpm-lock.yaml
pnpm install
git add .
git commit -m "Fix dependencies"
git push
```

### Error 5: "Node version mismatch"

**Problem:** Wrong Node.js version

**Fix:**
1. Ensure `.nvmrc` contains: `20`
2. Add environment variable in Vercel: `NODE_VERSION=20`

---

## ✅ Pre-Deployment Checklist

Before deploying, verify:

- [ ] Code pushed to GitHub (`imsanghaar/agentfactory`)
- [ ] On `main` branch
- [ ] `.nvmrc` file exists with `20`
- [ ] `pnpm-lock.yaml` exists in root
- [ ] `vercel.json` exists in root
- [ ] Build works locally: `cd apps/learn-app && pnpm run build`
- [ ] `apps/learn-app/build/` folder created after build

---

## 🔍 How to Check Deployment Status

### 1. Vercel Dashboard
- Go to: [https://vercel.com/dashboard](https://vercel.com/dashboard)
- Click on your project
- View "Deployments" tab
- Click latest deployment → "View Build Logs"

### 2. Look for Success Messages
```
✓ Build completed successfully
✓ Output directory found
✓ Deployment is ready
🎉 Your site is live!
```

### 3. Check for Errors
- Red ❌ icons indicate failures
- Click on error to see details
- Common errors listed above

---

## 🎯 After Successful Deployment

### Your Site URLs

**Production:**
```
https://agentfactory-imsanghaar.vercel.app
```

**Preview (for future branches):**
```
https://agentfactory-git-[branch-name].vercel.app
```

### Verify Deployment

Test these pages:
- ✅ Homepage: `/`
- ✅ Preface: `/docs/preface-agent-native`
- ✅ Video Modal: Click Play button on Preface
- ✅ Mobile: Test on phone or use DevTools

---

## 🚨 Emergency: Still Not Working?

### Option 1: Check Build Logs
1. Vercel Dashboard → Project → Deployments
2. Click failed deployment
3. Open "Build Logs"
4. Screenshot error and share with team

### Option 2: Test Build Locally
```bash
cd E:\agentfactory\apps\learn-app
pnpm install
pnpm run build
# If this fails, fix local build first
```

### Option 3: Simplify Further
Temporarily remove `vercel.json` and use Vercel's auto-detection:
1. Delete `vercel.json`
2. Deploy via Dashboard
3. Let Vercel auto-detect settings

### Option 4: Contact Support
- Vercel Community: [GitHub Discussions](https://github.com/vercel/vercel/discussions)
- Share build log screenshot
- Mention: Docusaurus + pnpm monorepo

---

## 📊 Deployment Timeline

```
0:00 - Click Deploy
0:01 - Build starts
0:02 - Dependencies installing
0:05 - Build running
0:12 - Build complete
0:13 - Deployment ready ✅
```

**First deployment:** 10-15 minutes  
**Subsequent deployments:** 5-8 minutes (with cache)

---

## 🎉 Success Indicators

You'll know it worked when:
- ✅ Green checkmark in Vercel dashboard
- ✅ "Deployment ready" message
- ✅ Live URL is clickable
- ✅ Site loads without errors
- ✅ Video modal works on Preface page

---

**Need Help?** Share your Vercel build log screenshot for specific troubleshooting.

**Last Updated:** February 2026  
**For:** imsanghaar/agentfactory
