# Tasks: Panaversity SSO Auth Server

**Feature ID**: 001-auth-server
**Last Updated**: 2025-12-04
**Status**: ✅ IMPLEMENTATION COMPLETE (Pending Deployment)
**Spec**: [spec.md](./spec.md) | **Plan**: [plan.md](./plan.md)

---

## Task Summary

| Phase | Description | Tasks | Completed |
|-------|-------------|-------|-----------|
| 1 | Project Setup | 6 | ✅ 6 |
| 2 | Better Auth Core | 6 | ✅ 6 |
| 3 | Registration (US1) | 6 | ✅ 6 |
| 4 | Login (US2) | 4 | ✅ 4 |
| 5 | Logout (US3) | 3 | ✅ 3 |
| 6 | Profile API (US4) | 4 | ✅ 4 |
| 7 | Update Profile (US5) | 2 | ✅ 2 |
| 8 | OAuth/OIDC Provider | 7 | ✅ 7 |
| 9 | Email Verification | 4 | ✅ 4 |
| 10 | Multi-Tenancy | 4 | ✅ 4 |
| 11 | Admin Dashboard | 5 | ✅ 5 |
| 12 | Security & Scale | 5 | ✅ 5 |
| 13 | Testing | 6 | ✅ 6 |
| 14 | Deployment | 3 | ⏳ 0 |
| **Total** | | **65** | **62** |

---

## Phase 1: Project Setup ✅

**Goal**: Next.js project with Drizzle ORM connected to Neon Postgres.

- [x] T001 Create Next.js 15 project with TypeScript
- [x] T002 Install dependencies: better-auth, drizzle-orm, @neondatabase/serverless
- [x] T003 Create environment template (.env.example)
- [x] T004 Configure Drizzle with Neon serverless driver
- [x] T005 Create Drizzle database client (src/lib/db/index.ts)
- [x] T006 Generate Better Auth schema (auth-schema.ts)

---

## Phase 2: Better Auth Core ✅

**Goal**: Better Auth with email/password provider working.

- [x] T007 Configure Better Auth with Drizzle adapter (src/lib/auth.ts)
- [x] T008 Configure session settings (7-day, HTTP-only cookies)
- [x] T009 Create Better Auth catch-all API route
- [x] T010 Create client-side auth helpers (src/lib/auth-client.ts)
- [x] T011 Configure CORS for trusted origins
- [x] T012 Run database migration (db:push)

---

## Phase 3: US1 - New User Registration ✅

**User Story**: Visitor creates account with email, password, and profile data.

- [x] T013 Create software background selector component
- [x] T014 Create hardware tier selector component
- [x] T015 Create sign-up form component with validation
- [x] T016 Create auth layout with Panaversity branding
- [x] T017 Create sign-up page with onboarding flow
- [x] T018 Add user profile fields (softwareBackground, hardwareTier)

---

## Phase 4: US2 - Existing User Login ✅

**User Story**: Returning user signs in with credentials.

- [x] T019 Create sign-in form component
- [x] T020 Create sign-in page
- [x] T021 Add error handling with generic "Invalid credentials"
- [x] T022 Create root page redirect (session → home, no session → sign-in)

---

## Phase 5: US3 - User Logout ✅

**User Story**: User signs out of their account.

- [x] T023 Create logout button component
- [x] T024 Add logout to authenticated pages
- [x] T025 Verify session invalidation

---

## Phase 6: US4 - Profile Data Access ✅

**User Story**: Clients fetch user profile for personalization.

- [x] T026 Create GET /api/profile endpoint
- [x] T027 Add session validation middleware
- [x] T028 Return 401 for unauthenticated requests
- [x] T029 Test profile endpoint (authenticated/unauthenticated)

---

## Phase 7: US5 - Update Profile ✅

**User Story**: User updates their profile settings.

- [x] T030 Add PUT /api/profile endpoint
- [x] T031 Create account profile page (/account/profile)

---

## Phase 8: OAuth/OIDC Provider ✅

**Goal**: Auth server as OAuth 2.1 / OIDC Provider with PKCE and JWKS.

- [x] T032 Add JWT plugin with JWKS configuration (RS256)
- [x] T033 Configure OIDC Provider plugin with useJWTPlugin
- [x] T034 Create trusted clients configuration (src/lib/trusted-clients.ts)
- [x] T035 Add custom JWT claims (tenant_id, role, software_background)
- [x] T036 Create admin client registration endpoint
- [x] T037 Create OAuth consent page (/auth/consent)
- [x] T038 Create seed scripts for trusted clients

---

## Phase 9: Email Verification ✅

**Goal**: Email verification on signup and password reset.

- [x] T039 Configure Resend email provider
- [x] T040 Configure SMTP fallback (Gmail, custom)
- [x] T041 Add email verification templates (HTML)
- [x] T042 Add password reset templates and flow
- [x] T043 Create forgot password page
- [x] T044 Create reset password page
- [x] T045 Create resend verification page

---

## Phase 10: Multi-Tenancy ✅

**Goal**: Organization support with auto-join on signup.

- [x] T046 Add Organization plugin to Better Auth
- [x] T047 Create default Panaversity organization
- [x] T048 Add databaseHook for auto-join on signup
- [x] T049 Add tenant_id, organization_ids to JWT claims

---

## Phase 11: Admin Dashboard ✅

**Goal**: Admin UI for managing users and OAuth clients.

- [x] T050 Create admin layout with sidebar
- [x] T051 Create admin dashboard page (/admin)
- [x] T052 Create client management page (/admin/clients)
- [x] T053 Create user management page (/admin/users)
- [x] T054 Protect first-party clients from deletion

---

## Phase 12: Security & Scale ✅

**Goal**: Production-ready security and scalability.

- [x] T055 Configure rate limiting (per-endpoint rules)
- [x] T056 Add Redis support for distributed rate limiting
- [x] T057 Add HIBP (Have I Been Pwned) password checking
- [x] T058 Add Username plugin (optional usernames)
- [x] T059 Create health check endpoint (/api/health)

---

## Phase 13: Testing ✅

**Goal**: Comprehensive test coverage for all features.

- [x] T060 Create OAuth flow API tests (test-oauth-flows.js)
- [x] T061 Create multi-tenant claim tests (test-tenant-claims.js)
- [x] T062 Create edge case tests (test-edge-cases.js)
- [x] T063 Create confidential client tests (test-confidential-client.js)
- [x] T064 Create E2E SSO tests (test-complete-sso.js)
- [x] T065 Create Playwright PKCE tests (test-pkce-playwright.mjs)

---

## Phase 14: Deployment ⏳

**Goal**: Deploy to production environment.

- [ ] T066 Deploy auth-server to Vercel (or Cloud Run)
- [ ] T067 Configure production environment variables
- [ ] T068 Run pnpm seed:prod on production database

---

## Validation Checklist ✅

### Authentication
- [x] Registration completes with email, password, profile (<60s)
- [x] Sign-in completes (<10s)
- [x] 100% of users have organization membership
- [x] Sessions persist 7 days
- [x] Logout invalidates session
- [x] No plaintext passwords in database
- [x] Rate limiting blocks brute force
- [x] HIBP rejects compromised passwords

### OAuth/OIDC
- [x] GET /.well-known/openid-configuration works
- [x] GET /api/auth/jwks returns valid RS256 public keys
- [x] OAuth authorization flow with PKCE succeeds
- [x] Token exchange with code_verifier (no secret) works
- [x] GET /api/auth/oauth2/userinfo returns custom claims
- [x] Public clients have clientSecret = null
- [x] First-party clients skip consent screen

### Email
- [x] Verification email sent on signup
- [x] Email verification link works (auto-signs in)
- [x] Password reset email sent
- [x] Password reset flow completes

### Multi-Tenancy
- [x] New users auto-join default organization
- [x] JWT contains tenant_id claim
- [x] JWT contains organization_ids array
- [x] JWT contains org_role claim

### Admin
- [x] Admin can view all OAuth clients
- [x] Admin can register new clients
- [x] Admin can edit/delete non-protected clients
- [x] First-party clients are protected
- [x] Non-admin users get 403

### Deployment (Pending)
- [ ] Auth server deployed to production
- [ ] Production environment variables configured
- [ ] Trusted clients seeded in production database
- [ ] JWKS endpoint accessible from production
- [ ] OAuth flow tested from client apps

---

## Test Commands

```bash
# Run all API tests (~60 seconds)
pnpm test-api

# Run E2E browser tests (~30 seconds)
pnpm test-e2e

# Run complete test suite (~90 seconds)
pnpm test-all

# Run specific test categories
node tests/test-oauth-flows.js        # OAuth authorization
node tests/test-tenant-claims.js      # Multi-tenant JWT claims
node tests/test-edge-cases.js         # Error handling
node tests/test-confidential-client.js # Confidential clients
node tests/test-default-organization.js # Auto-join org
```

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-29 | Initial task breakdown |
| 2.0 | 2025-12-01 | Added OAuth/OIDC, email tasks |
| 3.0 | 2025-12-02 | Added multi-tenancy, admin tasks |
| 3.1 | 2025-12-04 | Updated to reflect full implementation |
