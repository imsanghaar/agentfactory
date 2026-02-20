# Feature Specification: Panaversity SSO Auth Server

**Feature ID**: 001-auth-server
**Created**: 2025-11-29
**Last Updated**: 2025-12-04
**Status**: ✅ IMPLEMENTED (Production Ready)

## Executive Summary

A centralized OAuth 2.1 / OIDC authentication server serving multiple Panaversity applications. Built with Next.js 15, Better Auth, Drizzle ORM, and Neon Postgres. Provides single sign-on across RoboLearn, AI Native, and future Panaversity platforms.

**Key Capabilities**:
- OAuth 2.1 Authorization Code Flow with PKCE
- OIDC Provider with JWKS (RS256 signing)
- Multi-tenancy with organizations
- Role-based access control (admin/user + org roles)
- Custom JWT claims (software_background, hardware_tier, tenant_id)
- Rate limiting with Redis support for scale
- Admin dashboard for user/client management

---

## Platform Clients

| Client | Type | Purpose | Status |
|--------|------|---------|--------|
| **RoboLearn** | Public (PKCE) | Educational platform | ✅ Configured |
| **Panaversity SSO** | Public (PKCE) | SSO Dashboard | ✅ Configured |
| **AI Native** | Public (PKCE) | AI Development Platform | ✅ Configured |
| **RoboLearn Backend** | Confidential | Server-side integration (test) | ✅ Configured |

---

## User Scenarios & Testing

### US1 - New User Registration (P1) ✅ IMPLEMENTED

A visitor creates an account with email, password, and optional profile data.

**Acceptance Scenarios**:
1. ✅ Valid email + password (8+ chars) → account created, verification email sent
2. ✅ Duplicate email → clear error with sign-in link
3. ✅ Short password → validation feedback
4. ✅ Compromised password (HIBP) → rejection with message
5. ✅ Email verification completes → auto-signed in
6. ✅ User auto-joins default Panaversity organization

### US2 - Existing User Login (P1) ✅ IMPLEMENTED

A returning user signs in to continue using Panaversity apps.

**Acceptance Scenarios**:
1. ✅ Correct credentials → session created (7 days)
2. ✅ Incorrect credentials → generic "Invalid credentials" message
3. ✅ Session persists across browser close
4. ✅ Rate limiting blocks rapid attempts (10/min)
5. ✅ Unverified email → prompted to verify first

### US3 - User Logout (P2) ✅ IMPLEMENTED

A logged-in user signs out of their account.

**Acceptance Scenarios**:
1. ✅ Logout → session invalidated, redirected to login
2. ✅ Back button after logout → cannot access protected content

### US4 - OAuth/OIDC Flow (P1) ✅ IMPLEMENTED

External clients authenticate users via OAuth 2.1 with PKCE.

**Acceptance Scenarios**:
1. ✅ Authorization request with PKCE → redirect to login
2. ✅ First-party clients → skip consent screen
3. ✅ Third-party clients → show consent screen
4. ✅ Token exchange with code_verifier → returns tokens
5. ✅ ID token contains custom claims (tenant_id, role, etc.)
6. ✅ JWKS endpoint returns RS256 public keys
7. ✅ Client-side token verification works (no server call)

### US5 - Profile Data Access (P2) ✅ IMPLEMENTED

Clients fetch user profile data for personalization.

**Acceptance Scenarios**:
1. ✅ Authenticated GET /api/profile → returns user + profile data
2. ✅ PUT /api/profile → updates softwareBackground, hardwareTier
3. ✅ Unauthenticated request → 401 Unauthorized
4. ✅ OAuth userinfo endpoint → returns claims

### US6 - Admin Dashboard (P2) ✅ IMPLEMENTED

Admins manage users and OAuth clients.

**Acceptance Scenarios**:
1. ✅ Admin can view all registered OAuth clients
2. ✅ Admin can register new OAuth clients
3. ✅ Admin can edit/delete non-protected clients
4. ✅ First-party clients are protected from deletion
5. ✅ Admin can view user list
6. ✅ Non-admin users → 403 Forbidden

### US7 - Password Reset (P2) ✅ IMPLEMENTED

A user resets their forgotten password via email.

**Acceptance Scenarios**:
1. ✅ Request reset → email sent with secure link
2. ✅ Click link → password reset form
3. ✅ Submit new password → updated, auto-signed in
4. ✅ Link expires after 1 hour

---

## Requirements

### Functional Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| FR-001 | Email/password account creation | ✅ Done |
| FR-002 | Email format validation | ✅ Done |
| FR-003 | Password min 8 characters | ✅ Done |
| FR-004 | Secure password hashing (scrypt) | ✅ Done |
| FR-005 | 7-day sessions | ✅ Done |
| FR-006 | Session invalidation on logout | ✅ Done |
| FR-007 | Software background capture | ✅ Done |
| FR-008 | Profile data API | ✅ Done |
| FR-009 | Rate limiting | ✅ Done (Redis optional) |
| FR-010 | CORS for trusted origins | ✅ Done |
| FR-011 | User-friendly error messages | ✅ Done |
| FR-012 | Duplicate email prevention | ✅ Done |
| FR-013 | OAuth 2.1 / OIDC Provider with PKCE | ✅ Done |
| FR-014 | JWKS endpoint (RS256) | ✅ Done |
| FR-015 | Admin client registration endpoint | ✅ Done |
| FR-016 | Email verification on signup | ✅ Done |
| FR-017 | Password reset via email | ✅ Done |
| FR-018 | Public vs confidential client distinction | ✅ Done |
| FR-019 | Multi-tenancy with organizations | ✅ Done |
| FR-020 | Custom JWT claims (tenant_id, role) | ✅ Done |
| FR-021 | Admin dashboard UI | ✅ Done |
| FR-022 | Have I Been Pwned password checking | ✅ Done |
| FR-023 | Username support (optional) | ✅ Done |
| FR-024 | Health check endpoint | ✅ Done |

### Non-Functional Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| NFR-001 | Standalone deployment | ✅ Done |
| NFR-002 | Future OAuth providers support | ✅ Architecture ready |
| NFR-003 | SSO/OIDC provider capabilities | ✅ Done |
| NFR-004 | HTTP-only cookies for sessions | ✅ Done |
| NFR-005 | Distributed rate limiting (Redis) | ✅ Done |
| NFR-006 | Auto JWKS key rotation (90 days) | ✅ Done |
| NFR-007 | Multi-instance deployment support | ✅ Done |

---

## Key Entities

### User
Core identity managed by Better Auth.

```typescript
user {
  id: text PK
  email: text UNIQUE
  name: text
  emailVerified: boolean
  role: text  // "user" | "admin"
  banned: boolean
  username: text UNIQUE (optional)
  // OIDC Standard Claims
  givenName: text
  familyName: text
  phoneNumber: text
  locale: text
  // Custom fields
  softwareBackground: text  // "beginner" | "intermediate" | "advanced"
  hardwareTier: text  // "basic" | "gpu_local" | "cloud_gpu"
  createdAt: timestamp
  updatedAt: timestamp
}
```

### Session
Active login sessions.

```typescript
session {
  id: text PK
  userId: text FK → user.id
  token: text UNIQUE
  expiresAt: timestamp
  ipAddress: text
  userAgent: text
  activeOrganizationId: text (optional)
}
```

### Organization (Multi-Tenancy)
Tenant entities for multi-app architecture.

```typescript
organization {
  id: text PK
  name: text
  slug: text UNIQUE
  logo: text
  metadata: text (JSON)
}

member {
  id: text PK
  organizationId: text FK → organization.id
  userId: text FK → user.id
  role: text  // "owner" | "admin" | "member"
}
```

### OAuth Application
Registered OAuth clients.

```typescript
oauth_application {
  id: text PK
  clientId: text UNIQUE
  clientSecret: text (null for public clients)
  name: text
  redirectUrls: text (comma-separated)
  type: text  // "public" | "web" (confidential)
  disabled: boolean
}
```

### JWKS
RSA key pairs for token signing.

```typescript
jwks {
  id: text PK
  publicKey: text
  privateKey: text (encrypted AES-256-GCM)
  createdAt: timestamp
  expiresAt: timestamp
}
```

---

## Constraints

| ID | Constraint | Satisfied |
|----|------------|-----------|
| C-001 | Better Auth library | ✅ v1.4.4 |
| C-002 | Neon Postgres | ✅ Serverless |
| C-003 | Next.js framework | ✅ v15.1.0 |
| C-004 | Drizzle ORM | ✅ v0.36.0 |
| C-005 | No social OAuth initially | ✅ Architecture ready |

---

## Non-Goals

| ID | Non-Goal | Status |
|----|----------|--------|
| NG-001 | Social login (Google, GitHub) | Deferred - architecture ready |
| NG-002 | Full hardware survey | Simplified to enum |
| NG-003 | ~~Password reset~~ | ✅ COMPLETED |
| NG-004 | ~~Email verification~~ | ✅ COMPLETED |
| NG-005 | Two-factor authentication | Deferred |
| NG-006 | ~~Admin dashboard~~ | ✅ COMPLETED |
| NG-007 | ~~SSO provider~~ | ✅ COMPLETED |
| NG-008 | ~~JWKS support~~ | ✅ COMPLETED |
| NG-009 | ~~Multi-app architecture~~ | ✅ COMPLETED |

---

## Success Criteria

### Authentication (All Verified ✅)
- [x] Registration completes in <60 seconds
- [x] Sign-in completes in <10 seconds
- [x] 100% of users have organization membership
- [x] Sessions persist 7 days
- [x] Zero plaintext passwords in database
- [x] Rate limiting blocks brute force

### OAuth/OIDC (All Verified ✅)
- [x] OAuth flow completes with PKCE in <5 seconds
- [x] JWKS endpoint returns valid RS256 public keys
- [x] ID tokens contain tenant_id, role claims
- [x] Client-side token verification works
- [x] Access tokens expire after 6 hours
- [x] Refresh tokens expire after 7 days

### Email (All Verified ✅)
- [x] Verification emails delivered within 30 seconds
- [x] Password reset flow works end-to-end
- [x] Email templates are professional (HTML)

### Admin (All Verified ✅)
- [x] Admin can manage OAuth clients
- [x] First-party clients are protected
- [x] Admin can view users

### Scale Readiness
- [x] Redis rate limiting for multi-instance
- [x] 3000 req/min global limit (100k user scale)
- [x] Automatic JWKS key rotation

---

## Dependencies

| ID | Dependency | Status |
|----|------------|--------|
| D-001 | Neon Postgres instance | ✅ Provisioned |
| D-002 | Auth server domain | ✅ localhost:3001 (dev) |
| D-003 | Client app integration | ✅ RoboLearn configured |
| D-004 | Email provider (Resend/SMTP) | ✅ Optional, configurable |
| D-005 | Redis (Upstash) | ✅ Optional, for scale |

---

## Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| Runtime | Node.js | 20+ |
| Framework | Next.js (App Router) | 15.1.0 |
| Auth Library | Better Auth | 1.4.4 |
| ORM | Drizzle | 0.36.0 |
| Database | Neon Postgres | Serverless |
| Cache | Upstash Redis | Optional |
| Email | Resend / SMTP | Optional |
| Testing | Node.js + Playwright | Native |

---

## API Endpoints

### Authentication
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/sign-up/email` | POST | Create account |
| `/api/auth/sign-in/email` | POST | Sign in |
| `/api/auth/sign-out` | POST | Sign out |
| `/api/auth/session` | GET | Get session |
| `/api/auth/forgot-password` | POST | Request reset |
| `/api/auth/reset-password` | POST | Reset password |

### OAuth/OIDC
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/.well-known/openid-configuration` | GET | OIDC Discovery |
| `/api/auth/jwks` | GET | Public keys |
| `/api/auth/oauth2/authorize` | GET | Start OAuth flow |
| `/api/auth/oauth2/token` | POST | Exchange code |
| `/api/auth/oauth2/userinfo` | GET | Get user info |

### Admin
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/admin/clients` | GET | List clients |
| `/api/admin/clients/register` | POST | Register client |
| `/api/admin/clients/[clientId]` | PUT/DELETE | Manage client |

### Profile
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/profile` | GET | Get profile |
| `/api/profile` | PUT | Update profile |

### Utility
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/oauth/client-info` | GET | Client info (for consent) |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-29 | Initial spec (email/password only) |
| 2.0 | 2025-12-01 | Added OAuth/OIDC Provider |
| 3.0 | 2025-12-02 | Added multi-tenancy, admin dashboard |
| 3.1 | 2025-12-04 | Updated to reflect full implementation |
