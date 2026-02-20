# Implementation Plan: Panaversity SSO Auth Server

**Feature ID**: 001-auth-server
**Last Updated**: 2025-12-04
**Status**: ✅ IMPLEMENTED
**Spec**: [spec.md](./spec.md)

## Summary

A centralized OAuth 2.1 / OIDC authentication server for Panaversity applications. Provides single sign-on across RoboLearn, AI Native, and future platforms with multi-tenancy support, admin dashboard, and enterprise-grade security features.

---

## Technical Context

| Aspect | Value |
|--------|-------|
| **Language** | TypeScript 5.6 |
| **Runtime** | Node.js 20+ |
| **Framework** | Next.js 15.1.0 (App Router) |
| **Auth Library** | Better Auth 1.4.4 |
| **ORM** | Drizzle 0.36.0 |
| **Database** | Neon Postgres (Serverless) |
| **Cache** | Upstash Redis (Optional) |
| **Email** | Resend / SMTP (Configurable) |
| **Testing** | Node.js native + Playwright |
| **Deployment** | Vercel / Cloud Run |

---

## Project Structure

```
sso/                                  # Root (not subfolder)
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/[...all]/       # Better Auth routes
│   │   │   ├── admin/clients/       # Client management API
│   │   │   ├── profile/             # Profile API
│   │   │   ├── health/              # Health check
│   │   │   └── oauth/client-info/   # OAuth client info
│   │   ├── auth/                    # Auth UI pages
│   │   │   ├── sign-in/             # Login page
│   │   │   ├── sign-up/             # Registration page
│   │   │   ├── consent/             # OAuth consent
│   │   │   ├── forgot-password/     # Password reset request
│   │   │   ├── reset-password/      # Password reset form
│   │   │   ├── resend-verification/ # Resend verification
│   │   │   └── verify-callback/     # Email verification
│   │   ├── admin/                   # Admin dashboard
│   │   │   ├── clients/             # Client management UI
│   │   │   └── users/               # User management UI
│   │   ├── account/                 # User account pages
│   │   │   └── profile/             # Profile settings
│   │   └── page.tsx                 # Homepage
│   ├── components/
│   │   ├── sign-in-form.tsx         # Login form
│   │   ├── sign-up-form.tsx         # Registration form
│   │   ├── forgot-password-form.tsx # Password reset
│   │   ├── reset-password-form.tsx  # New password form
│   │   ├── background-select.tsx    # Software background
│   │   ├── hardware-tier-select.tsx # Hardware tier
│   │   └── logout-button.tsx        # Logout component
│   └── lib/
│       ├── auth.ts                  # Better Auth configuration
│       ├── auth-client.ts           # Client-side auth
│       ├── trusted-clients.ts       # OAuth client definitions
│       ├── redis.ts                 # Redis configuration
│       └── db/
│           └── index.ts             # Drizzle client
├── auth-schema.ts                   # Better Auth generated schema
├── scripts/
│   ├── seed-setup.ts                # Development seeding
│   ├── seed-prod-client.ts          # Production seeding
│   └── create-admin.ts              # Admin user creation
├── tests/
│   ├── test-oauth-flows.js          # OAuth API tests
│   ├── test-tenant-claims.js        # Multi-tenant tests
│   ├── test-edge-cases.js           # Edge case tests
│   ├── test-complete-sso.js         # E2E SSO tests
│   └── test-pkce-playwright.mjs     # Browser-based PKCE tests
├── package.json
└── drizzle.config.ts
```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      PANAVERSITY SSO (Next.js 15)                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  UI Pages                                 API Routes                     │
│  ┌──────────────────────┐                ┌────────────────────────────┐ │
│  │ /auth/sign-in        │                │ /api/auth/[...all]         │ │
│  │ /auth/sign-up        │                │  └─ Better Auth handler    │ │
│  │ /auth/consent        │─────OAuth─────►│  └─ OAuth 2.1/OIDC        │ │
│  │ /auth/forgot-password│                │  └─ JWT/JWKS              │ │
│  │ /admin/clients       │                │  └─ Session management    │ │
│  │ /admin/users         │                ├────────────────────────────┤ │
│  │ /account/profile     │                │ /api/admin/clients         │ │
│  └──────────────────────┘                │  └─ Client CRUD (admin)   │ │
│                                          ├────────────────────────────┤ │
│  Components                              │ /api/profile               │ │
│  ┌──────────────────────┐                │  └─ User profile CRUD     │ │
│  │ SignInForm           │                ├────────────────────────────┤ │
│  │ SignUpForm           │                │ /api/health                │ │
│  │ BackgroundSelect     │                │  └─ Health check          │ │
│  │ LogoutButton         │                └─────────────┬──────────────┘ │
│  └──────────────────────┘                              │                 │
│                                                        ▼                 │
│                                          ┌────────────────────────────┐ │
│                                          │ Better Auth Core           │ │
│                                          │ ├─ Email/Password         │ │
│                                          │ ├─ OIDC Provider          │ │
│                                          │ ├─ JWT (JWKS)             │ │
│                                          │ ├─ Admin plugin           │ │
│                                          │ ├─ Organization plugin    │ │
│                                          │ ├─ Username plugin        │ │
│                                          │ └─ HIBP plugin            │ │
│                                          └─────────────┬──────────────┘ │
│                                                        │                 │
│                                                        ▼                 │
│                                          ┌────────────────────────────┐ │
│                                          │ Drizzle ORM                │ │
│                                          │ ├─ user                    │ │
│                                          │ ├─ session                 │ │
│                                          │ ├─ account                 │ │
│                                          │ ├─ organization            │ │
│                                          │ ├─ member                  │ │
│                                          │ ├─ oauth_application       │ │
│                                          │ ├─ oauth_access_token      │ │
│                                          │ └─ jwks                    │ │
│                                          └─────────────┬──────────────┘ │
│                                                        │                 │
└────────────────────────────────────────────────────────┼─────────────────┘
                                                         │
                    ┌────────────────────────────────────┼────────────────────┐
                    │                                    │                    │
                    ▼                                    ▼                    ▼
          ┌──────────────────┐              ┌──────────────────┐   ┌───────────────┐
          │ Neon Postgres    │              │ Upstash Redis    │   │ Resend/SMTP   │
          │ (Primary DB)     │              │ (Rate Limiting)  │   │ (Email)       │
          └──────────────────┘              └──────────────────┘   └───────────────┘
```

---

## Database Schema

```typescript
// Better Auth managed tables
user {
  id: text PK
  email: text UNIQUE
  name: text
  emailVerified: boolean
  role: text                  // "user" | "admin"
  banned: boolean
  username: text UNIQUE       // Optional username
  displayUsername: text
  // OIDC Standard Claims
  givenName: text
  familyName: text
  phoneNumber: text
  phoneNumberVerified: boolean
  locale: text
  zoneinfo: text
  // Custom profile fields
  softwareBackground: text    // "beginner" | "intermediate" | "advanced"
  hardwareTier: text          // "basic" | "gpu_local" | "cloud_gpu"
  createdAt: timestamp
  updatedAt: timestamp
}

session {
  id: text PK
  userId: text FK → user.id
  token: text UNIQUE
  expiresAt: timestamp
  ipAddress: text
  userAgent: text
  activeOrganizationId: text  // Current org context
}

account {
  id: text PK
  userId: text FK → user.id
  providerId: text           // "credential" for email/password
  password: text             // Hashed (scrypt)
}

// Multi-tenancy tables
organization {
  id: text PK
  name: text
  slug: text UNIQUE
  logo: text
  metadata: text             // JSON
}

member {
  id: text PK
  organizationId: text FK → organization.id
  userId: text FK → user.id
  role: text                 // "owner" | "admin" | "member"
}

// OAuth/OIDC tables
oauth_application {
  id: text PK
  clientId: text UNIQUE
  clientSecret: text         // NULL for public clients
  name: text
  redirectUrls: text         // Comma-separated
  type: text                 // "public" | "web"
  disabled: boolean
}

oauth_access_token {
  id: text PK
  accessToken: text UNIQUE
  refreshToken: text UNIQUE
  clientId: text FK → oauth_application.clientId
  userId: text FK → user.id
  scopes: text
  accessTokenExpiresAt: timestamp
  refreshTokenExpiresAt: timestamp
}

jwks {
  id: text PK
  publicKey: text
  privateKey: text           // Encrypted AES-256-GCM
  createdAt: timestamp
  expiresAt: timestamp
}
```

---

## Implementation Phases (All Complete)

### Phase 1: Project Setup ✅
- [x] Next.js 15 project at root level
- [x] Better Auth + Drizzle ORM dependencies
- [x] Neon Postgres connection
- [x] Environment configuration

### Phase 2: Better Auth Core ✅
- [x] Email/password authentication
- [x] Session management (7 days, HTTP-only)
- [x] Catch-all API route
- [x] Client-side auth helpers
- [x] CORS configuration

### Phase 3: OAuth/OIDC Provider ✅
- [x] JWT plugin with JWKS (RS256)
- [x] OIDC Provider plugin
- [x] Trusted clients configuration
- [x] Custom JWT claims (tenant_id, role)
- [x] Token expiration (6hr access, 7d refresh)
- [x] Auto key rotation (90 days)

### Phase 4: Multi-Tenancy ✅
- [x] Organization plugin
- [x] Default Panaversity organization
- [x] Auto-join on signup
- [x] Tenant-scoped claims

### Phase 5: Email System ✅
- [x] Email verification on signup
- [x] Password reset flow
- [x] Resend + SMTP fallback
- [x] Professional HTML templates

### Phase 6: Admin Dashboard ✅
- [x] Admin UI layout
- [x] Client management CRUD
- [x] User management view
- [x] First-party client protection

### Phase 7: Security & Scale ✅
- [x] Rate limiting (per-endpoint)
- [x] Redis support for distributed
- [x] HIBP password checking
- [x] Username plugin
- [x] Health endpoint

### Phase 8: Testing ✅
- [x] OAuth flow API tests
- [x] Multi-tenant claim tests
- [x] Edge case tests
- [x] E2E browser tests (Playwright)
- [x] Confidential client tests

---

## Trusted OAuth Clients

```typescript
// src/lib/trusted-clients.ts
TRUSTED_CLIENTS = [
  {
    clientId: "robolearn-public-client",
    name: "RoboLearn Book Interface",
    type: "public",
    redirectUrls: [
      "http://localhost:3000/auth/callback",
      "https://mjunaidca.github.io/robolearn/auth/callback"
    ],
    skipConsent: true
  },
  {
    clientId: "panaversity-sso-public-client",
    name: "Panaversity SSO",
    type: "public",
    redirectUrls: [
      "http://localhost:3000/auth/callback",
      "https://panaversity.org/auth/callback"
    ],
    skipConsent: true
  },
  {
    clientId: "ai-native-public-client",
    name: "AI Native Platform",
    type: "public",
    redirectUrls: [
      "http://localhost:3000/auth/callback",
      "https://ai-native.panaversity.org/auth/callback"
    ],
    skipConsent: true
  }
]
```

---

## Rate Limiting Configuration

```typescript
// Global: 3000 req/min (100k user scale)
// Per-endpoint security rules:
rateLimit: {
  "/sign-in/email": { max: 10, window: 60 },      // 10/min - brute force protection
  "/sign-up/email": { max: 5, window: 60 },       // 5/min - spam protection
  "/forgot-password": { max: 3, window: 300 },    // 3/5min - abuse protection
  "/oauth2/authorize": { max: 200, window: 60 },  // Generous for OAuth
  "/oauth2/token": { max: 100, window: 60 },      // Token exchanges
  "/get-session": false,                          // No limit - called frequently
}
```

---

## JWT Claims Structure

```typescript
// ID Token claims returned by userinfo
{
  // OIDC Standard
  sub: "user-id",
  email: "user@example.com",
  email_verified: true,
  name: "User Name",
  given_name: "User",
  family_name: "Name",
  picture: "https://...",

  // Multi-tenancy
  role: "user",                              // Global role
  tenant_id: "panaversity-default-org-id",   // Primary org
  organization_ids: ["org-1", "org-2"],      // All memberships
  org_role: "member",                        // Role in primary org

  // Custom (RoboLearn)
  software_background: "intermediate",
  hardware_tier: "gpu_local"
}
```

---

## Environment Variables

```env
# Database (Required)
DATABASE_URL=postgresql://user:pass@host/db?sslmode=require

# Better Auth (Required)
BETTER_AUTH_SECRET=your-secret-key-min-32-chars
BETTER_AUTH_URL=http://localhost:3001

# CORS (Required)
ALLOWED_ORIGINS=http://localhost:3000,https://robolearn.example.com

# Redis (Optional - for scale)
UPSTASH_REDIS_REST_URL=https://your-redis.upstash.io
UPSTASH_REDIS_REST_TOKEN=your-token

# Email (Optional - for verification/reset)
# Option 1: Resend
RESEND_API_KEY=re_xxxxxxxxx
EMAIL_FROM=noreply@panaversity.org

# Option 2: SMTP
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@gmail.com
SMTP_PASS=app-password
EMAIL_FROM=your@gmail.com

# Testing (Optional)
DISABLE_EMAIL_VERIFICATION=true  # Skip in test environment
```

---

## Commands Reference

```bash
# Development
pnpm dev                    # Start on port 3001

# Database
pnpm db:push               # Push schema
pnpm db:generate           # Generate migrations
pnpm db:studio             # Drizzle Studio

# Seeding
pnpm seed:setup            # Dev: all clients + test org
pnpm seed:prod             # Prod: Panaversity + AI Native

# Testing
pnpm test-api              # API tests (~60s)
pnpm test-e2e              # E2E tests (~30s)
pnpm test-all              # Full suite (~90s)
```

---

## Deployment Checklist

- [ ] Set production `DATABASE_URL`
- [ ] Generate secure `BETTER_AUTH_SECRET`
- [ ] Set `BETTER_AUTH_URL` to production domain
- [ ] Configure `ALLOWED_ORIGINS` for all clients
- [ ] Set up email provider (Resend or SMTP)
- [ ] Optional: Configure Redis for scale
- [ ] Run `pnpm seed:prod` to create trusted clients
- [ ] Verify JWKS endpoint accessible
- [ ] Test OAuth flow from client app

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-29 | Initial plan (email/password only) |
| 2.0 | 2025-12-01 | Added OAuth/OIDC phases |
| 3.0 | 2025-12-02 | Added multi-tenancy, admin |
| 3.1 | 2025-12-04 | Updated to reflect full implementation |
