# 🚀 Vercel Deployment Guide - The AI Agent Factory

Complete guide to deploying the AI Agent Factory book to Vercel.

---

## ⚡ Quick Deploy (Recommended)

### Option 1: Vercel Dashboard (Easiest)

1. **Go to [vercel.com](https://vercel.com)**
2. **Click "Add New Project"**
3. **Import your GitHub repository** (`imsanghaar/agentfactory`)
4. **Configure Project:**
   - **Framework Preset:** `Other`
   - **Root Directory:** `./` (keep default)
   - **Build Command:** `cd apps/learn-app && pnpm run build`
   - **Output Directory:** `apps/learn-app/build`
   - **Install Command:** `pnpm install --frozen-lockfile`
5. **Set Environment Variables** (if needed):
   - `NODE_VERSION`: `20`
6. **Click "Deploy"**

### Option 2: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Navigate to project root
cd /path/to/agentfactory

# Deploy
vercel --prod
```

---

## 🔧 Configuration Files

### Root `vercel.json` (Already Configured)

```json
{
  "outputDirectory": "apps/learn-app/build",
  "installCommand": "pnpm install --frozen-lockfile",
  "buildCommand": "cd apps/learn-app && pnpm run build",
  "framework": "static",
  "cleanUrls": true,
  "trailingSlash": false,
  "rewrites": [
    {
      "source": "/((?!api|_next|static|favicon|img|assets|search-index|sitemap).*)",
      "destination": "/index.html"
    }
  ]
}
```

### `.nvmrc` (Already Configured)

```
20
```

This ensures Node.js 20 is used (required for the build).

---

## 📋 Pre-Deployment Checklist

### ✅ 1. Verify Build Locally

```bash
# Navigate to learn-app
cd apps/learn-app

# Install dependencies
pnpm install

# Run build
pnpm run build

# Check if build folder exists
ls -la build/
```

**Expected Output:**
- `build/` folder should be created
- Contains `index.html`, `static/`, `assets/`, etc.

### ✅ 2. Check package.json

Ensure `apps/learn-app/package.json` has:
```json
{
  "scripts": {
    "build": "node scripts/build.js"
  },
  "engines": {
    "node": ">=20.0"
  }
}
```

### ✅ 3. Verify vercel.json

Root `vercel.json` must have:
- Correct `outputDirectory`: `apps/learn-app/build`
- Correct `buildCommand`: `cd apps/learn-app && pnpm run build`
- Correct `installCommand`: `pnpm install --frozen-lockfile`

### ✅ 4. Git Repository

- Ensure code is pushed to GitHub
- Branch is `main` (or your deployment branch)
- No uncommitted changes

---

## 🐛 Common Deployment Issues & Solutions

### Issue 1: Build Fails with "Module Not Found"

**Error:**
```
Error: Cannot find module '@docusaurus/core'
```

**Solution:**
```bash
# Clear node_modules and reinstall
rm -rf node_modules apps/*/node_modules pnpm-lock.yaml
pnpm install
```

### Issue 2: Build Timeout

**Error:**
```
Build exceeded maximum duration (15 minutes)
```

**Solution:**
1. Enable build cache in Vercel dashboard
2. Reduce OG image generation (set `DEV_MODE=true`)
3. Split into multiple deployments if needed

### Issue 3: Output Directory Not Found

**Error:**
```
Error: No output directory found at "apps/learn-app/build"
```

**Solution:**
- Verify build script runs successfully locally
- Check `vercel.json` has correct `outputDirectory`
- Ensure build completes without errors

### Issue 4: pnpm Not Recognized

**Error:**
```
sh: pnpm: command not found
```

**Solution:**
Vercel supports pnpm by default. Ensure:
- `pnpm-lock.yaml` exists in repository
- `packageManager` field in root `package.json` is set

### Issue 5: Node Version Mismatch

**Error:**
```
Error: Node.js version 18 is not supported
```

**Solution:**
- Ensure `.nvmrc` contains `20`
- Set `NODE_VERSION=20` in Vercel environment variables

---

## 🎨 Post-Deployment Configuration

### 1. Custom Domain (Optional)

1. Go to Vercel Project Settings
2. Navigate to "Domains"
3. Add your domain: `agentfactory.imsanghaar.vercel.app`
4. Configure DNS records as instructed

### 2. Environment Variables

Add these in Vercel Dashboard → Settings → Environment Variables:

```bash
# Optional: Enable dev mode for faster builds
DEV_MODE=false

# Auth server URL (if using auth features)
AUTH_URL=https://auth.imsanghaar.vercel.app

# Other API URLs
STUDY_MODE_API_URL=https://study-api.imsanghaar.vercel.app
TOKEN_METERING_API_URL=https://token-api.imsanghaar.vercel.app
```

### 3. Preview Deployments

- Every push to a non-main branch creates a preview URL
- Share preview URLs for review before merging
- Auto-updates when branch is updated

---

## 📊 Deployment Workflow

### Development Flow

```
1. Create Feature Branch
   ↓
2. Make Changes Locally
   ↓
3. Test Build: pnpm run build
   ↓
4. Commit & Push to GitHub
   ↓
5. Vercel Auto-Deploys Preview
   ↓
6. Review Preview URL
   ↓
7. Merge to Main
   ↓
8. Vercel Deploys to Production
```

### Production Deployment

```bash
# 1. Ensure you're on main branch
git checkout main

# 2. Pull latest changes
git pull origin main

# 3. Test build locally
cd apps/learn-app && pnpm run build

# 4. Push to GitHub
git push origin main

# 5. Vercel automatically deploys
# Check deployment status at: https://vercel.com/dashboard
```

---

## 🔍 Monitoring & Debugging

### View Deployment Logs

1. **Vercel Dashboard** → Select Project → "Deployments"
2. Click on latest deployment
3. View "Build Logs" for detailed output

### Common Log Messages

✅ **Success:**
```
✓ Build completed successfully
✓ Output directory found
✓ Deployment ready
```

⚠️ **Warnings (Non-Critical):**
```
⚠ Slides Transformer: Could not find injection point
⚠ Summaries Plugin: Found X summary files
```
These are normal and don't affect deployment.

❌ **Errors (Critical):**
```
✗ Build failed
✗ Module not found
✗ Output directory missing
```
Check "Common Deployment Issues" section above.

---

## 🚨 Emergency Rollback

If production deployment has issues:

### Option 1: Rollback via Dashboard

1. Go to Vercel Dashboard → Project → "Deployments"
2. Find last working deployment
3. Click "Promote to Production"

### Option 2: Revert Git Commit

```bash
# Find last good commit
git log --oneline

# Revert to that commit
git revert HEAD~n  # where n is number of commits to revert

# Force deploy
vercel --prod
```

---

## 📈 Performance Optimization

### 1. Enable Caching

Add to `vercel.json`:
```json
{
  "headers": [
    {
      "source": "/static/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

### 2. Reduce Build Time

- Enable "Build Cache" in Vercel settings
- Use `DEV_MODE=true` for preview deployments
- Split large documentation into smaller chunks

### 3. Optimize Images

- Compress images before committing
- Use WebP format where possible
- Lazy load images in components

---

## 🎯 Deployment URLs

After deployment, your site will be available at:

- **Production:** `https://agentfactory-imsanghaar.vercel.app`
- **Preview:** `https://agentfactory-git-branch-name.vercel.app`

### Update Custom Domain

1. Go to Vercel → Project Settings → Domains
2. Add: `agentfactory.imsanghaar.vercel.app`
3. Verify DNS configuration
4. Wait for SSL certificate (5-10 minutes)

---

## 📞 Support & Resources

### Vercel Documentation
- [Deploying with Git](https://vercel.com/docs/deployments/git)
- [Build & Deployment](https://vercel.com/docs/deployments)
- [Environment Variables](https://vercel.com/docs/environment-variables)

### Docusaurus on Vercel
- [Docusaurus Deployment Guide](https://docusaurus.io/docs/deployment#deploying-to-vercel)

### Get Help
- Vercel Community: [GitHub Discussions](https://github.com/vercel/vercel/discussions)
- imsanghaar Team: Contact via GitHub Issues

---

## ✅ Deployment Verification

After deployment, verify:

- [ ] Homepage loads correctly
- [ ] Book navigation works
- [ ] Video modal plays (Preface page)
- [ ] Search functionality works
- [ ] Mobile responsive design works
- [ ] All CSS styles load properly
- [ ] Images and assets load
- [ ] No console errors

**Test URL:** `https://agentfactory.imsanghaar.vercel.app/docs/preface-agent-native`

---

**Last Updated:** February 2026  
**Version:** 1.0.0  
**Maintained By:** imsanghaar Team
