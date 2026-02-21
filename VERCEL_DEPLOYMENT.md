# Vercel Deployment Guide - Agent Factory

This guide covers deploying both the **Learn App (Book)** and **SSO Server** to Vercel with automatic deployments on git push.

---

## 📋 Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Repo**: Your code should be pushed to `github.com/imsanghaar/agentfactory`
3. **Vercel CLI** (optional): `npm i -g vercel`

---

## 🚀 Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

#### Step 1: Import Learn App (Book)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **"Import Git Repository"**
3. Select your repo: `imsanghaar/agentfactory`
4. Click **"Import"**

**Configure Project:**
- **Project Name**: `agentfactory-book`
- **Framework Preset**: `Docusaurus`
- **Root Directory**: `apps/learn-app` (click Edit and enter this)
- **Build Command**: `pnpm build`
- **Output Directory**: `build`

**Environment Variables:**
```
AUTH_URL=https://agentfactory-sso-<your-hash>.vercel.app
OAUTH_CLIENT_ID=agent-factory-public-client
STUDY_MODE_API_URL=https://study-mode-api.vercel.app
TOKEN_METERING_API_URL=https://token-metering-api.vercel.app
PROGRESS_API_URL=https://progress-api.vercel.app
CHATKIT_DOMAIN_KEY=your-production-key
SSO_URL=https://agentfactory-sso-<your-hash>.vercel.app
NODE_ENV=production
```

5. Click **"Deploy"**

---

#### Step 2: Import SSO Server

1. Go to [vercel.com/new](https://vercel.com/new) again
2. Select the same repo: `imsanghaar/agentfactory`

**Configure Project:**
- **Project Name**: `agentfactory-sso`
- **Framework Preset**: `Next.js`
- **Root Directory**: `apps/sso`
- **Build Command**: `cd ../../ && pnpm install && cd apps/sso && pnpm build`
- **Install Command**: `cd ../../ && pnpm install`
- **Output Directory**: `.next`

**Environment Variables:**
```
DATABASE_URL=postgresql://user:password@host:5432/dbname
BETTER_AUTH_SECRET=your-32-char-secret-key-here
BETTER_AUTH_URL=https://agentfactory-sso-<your-hash>.vercel.app
NEXT_PUBLIC_BETTER_AUTH_URL=https://agentfactory-sso-<your-hash>.vercel.app
ALLOWED_ORIGINS=https://agentfactory-book-<your-hash>.vercel.app,https://agentfactory-sso-<your-hash>.vercel.app
NEXT_PUBLIC_APP_NAME=Imam Sanghaar SSO
NEXT_PUBLIC_APP_DESCRIPTION=Secure Single Sign-On
NEXT_PUBLIC_ORG_NAME=Imam Sanghaar
NEXT_PUBLIC_CONTINUE_URL=https://agentfactory-book-<your-hash>.vercel.app
NODE_ENV=production
```

5. Click **"Deploy"**

---

### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy Learn App
cd apps/learn-app
vercel --prod

# Deploy SSO Server
cd ../sso
vercel --prod
```

---

## 🔗 Linking Projects for Auto-Deploy

After initial deployment:

1. Go to **Vercel Dashboard** → Select your project
2. Go to **Settings** → **Git**
3. Ensure **"Connected Git Repository"** shows `imsanghaar/agentfactory`
4. Under **"Root Directory"**, verify:
   - Book: `apps/learn-app`
   - SSO: `apps/sso`
5. **"Automatic Deployments"** should be **ON** by default

Now every `git push` to `main` branch will trigger automatic deployment!

---

## 🔄 Updating Environment Variables

After deployment, update the Learn App's `SSO_URL` to point to your deployed SSO:

1. Go to Vercel Dashboard → `agentfactory-book`
2. **Settings** → **Environment Variables**
3. Edit `SSO_URL` to: `https://agentfactory-sso-<your-hash>.vercel.app`
4. **Redeploy** to apply changes

---

## 🎯 Production URLs

After deployment, you'll have:

| Service | URL |
|---------|-----|
| Book (Learn App) | `https://agentfactory-book-<hash>.vercel.app` |
| SSO Server | `https://agentfactory-sso-<hash>.vercel.app` |
| Admin Panel | `https://agentfactory-sso-<hash>.vercel.app/admin` |

---

## 🛡️ Security Checklist

- [ ] Set strong `BETTER_AUTH_SECRET` (32+ characters)
- [ ] Use production database URL (Neon/PostgreSQL)
- [ ] Configure `ALLOWED_ORIGINS` with production URLs
- [ ] Enable HTTPS (automatic on Vercel)
- [ ] Set up custom domain (optional)

---

## 📝 Custom Domain (Optional)

To use your own domain:

1. Go to Vercel Project → **Settings** → **Domains**
2. Add your domain: `imsanghaar.com`
3. Update DNS records as instructed
4. Update environment variables with new URLs

---

## 🐛 Troubleshooting

### Build Fails
- Check **Deployments** → Click failed deployment → View build logs
- Ensure `pnpm-lock.yaml` is committed to git
- Verify root directory path is correct

### Database Connection Errors
- Check `DATABASE_URL` in environment variables
- Ensure database allows connections from Vercel IPs
- Test connection locally with production credentials

### CORS Errors
- Update `ALLOWED_ORIGINS` to include both production URLs
- Redeploy SSO server after changing env vars

---

## 📚 Additional Resources

- [Vercel Docusaurus Guide](https://vercel.com/docs/frameworks/docusaurus)
- [Vercel Next.js Guide](https://vercel.com/docs/frameworks/nextjs)
- [Better Auth Production Setup](https://www.better-auth.com/docs/deployment)

---

**Last Updated**: February 21, 2026
