# Feature Specification: API Key M2M Authentication

**Feature Branch**: `004-api-key-m2m-auth`
**Created**: 2024-12-04
**Status**: Draft
**Input**: User description: "API Key M2M Authentication for PanaversityFS MCP Server Integration"

## Overview

Enable Machine-to-Machine (M2M) authentication for Panaversity SSO using Better Auth's API Key plugin. This allows services like GitHub Actions, CI/CD pipelines, and MCP servers (e.g., PanaversityFS) to authenticate programmatically without user interaction.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Admin Creates Service API Key (Priority: P1)

An administrator needs to create API keys for automated services that will interact with Panaversity platform resources.

**Why this priority**: Core functionality - without API key creation, no M2M authentication is possible. This is the foundation of the entire feature.

**Independent Test**: Can be fully tested by an admin signing in, navigating to the API key management page, creating a key, and verifying the key appears in the list.

**Acceptance Scenarios**:

1. **Given** an admin user is signed in to the SSO dashboard, **When** they navigate to "Service Keys" in the admin section, **Then** they see a page to manage API keys with a "Create New Key" option.

2. **Given** an admin is on the Service Keys page, **When** they click "Create New Key" and enter a name "github-actions-panaversityfs", **Then** the system generates a unique API key, displays it once, and warns the user to save it securely.

3. **Given** an admin has created an API key, **When** they view the keys list, **Then** they see the key's name, prefix (first characters), creation date, last used date, and status - but NOT the full key.

---

### User Story 2 - Service Authenticates with API Key (Priority: P1)

An external service (e.g., PanaversityFS MCP server) needs to authenticate API requests using an API key.

**Why this priority**: Core functionality - the primary use case for M2M authentication. Services must be able to verify tokens/keys.

**Independent Test**: Can be fully tested by making a POST request to `/api/auth/api-key/verify` with a valid API key and receiving a success response.

**Acceptance Scenarios**:

1. **Given** a valid API key exists, **When** a service sends a request with header `x-api-key: <key>`, **Then** the SSO returns a verification response confirming the key is valid.

2. **Given** a valid API key exists, **When** a service calls the verify endpoint with the key, **Then** the response includes key metadata (name, permissions, user association) but NOT the actual key value.

3. **Given** an invalid or revoked API key, **When** a service attempts to verify it, **Then** the SSO returns a 401 error with `valid: false` and an appropriate error message.

---

### User Story 3 - Admin Revokes Compromised API Key (Priority: P2)

An administrator needs to immediately disable a potentially compromised API key.

**Why this priority**: Security-critical - compromised keys must be revokable instantly. Slightly lower than creation/verification since those are needed first.

**Independent Test**: Can be fully tested by creating a key, verifying it works, revoking it, then verifying it no longer works.

**Acceptance Scenarios**:

1. **Given** an admin views a list of API keys, **When** they click "Revoke" on a specific key and confirm, **Then** the key is immediately disabled and subsequent verification attempts fail.

2. **Given** an API key has been revoked, **When** a service attempts to use it, **Then** the verification returns `valid: false` with error code indicating the key is revoked.

---

### User Story 4 - Admin Views API Key Usage (Priority: P2)

An administrator wants to monitor API key usage for security and operational awareness.

**Why this priority**: Important for operations and security monitoring, but not blocking for basic functionality.

**Independent Test**: Can be fully tested by using an API key several times, then viewing its details and seeing updated usage information.

**Acceptance Scenarios**:

1. **Given** an API key has been used, **When** an admin views the key details, **Then** they see "Last Used" timestamp and request count information.

2. **Given** multiple API keys exist, **When** an admin views the keys list, **Then** they can see at-a-glance which keys are active, expired, or heavily used.

---

### User Story 5 - Admin Sets Key Expiration (Priority: P3)

An administrator wants to create time-limited API keys that automatically expire.

**Why this priority**: Good security practice but not essential for MVP. Can use indefinite keys initially.

**Independent Test**: Can be fully tested by creating a key with expiration, waiting for it to expire, then verifying it no longer works.

**Acceptance Scenarios**:

1. **Given** an admin is creating an API key, **When** they set an expiration date/duration, **Then** the key is created with that expiration and shows the expiry date in the list.

2. **Given** an API key has expired, **When** a service attempts to verify it, **Then** the verification fails with an "expired" error.

---

### Edge Cases

- What happens when an admin tries to create a key without a name? System requires a name for identification - validation error returned.
- How does the system handle concurrent key verification requests? Each verification is independent, no race conditions expected.
- What happens if database is temporarily unavailable during verification? Return 503 Service Unavailable, log error, allow client retry.
- What happens when an admin deletes their account? API keys created by that admin should be soft-deleted or transferred.
- How does the system handle extremely long key names? Reject names over 100 characters with validation error.
- What happens if rate limit is exceeded? Return 429 Too Many Requests with `tryAgainIn` milliseconds.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow authenticated admin users to create API keys with a unique name
- **FR-002**: System MUST generate cryptographically secure API keys with sufficient entropy (minimum 256 bits / 64 characters)
- **FR-003**: System MUST store API keys as secure hashes using argon2id, never in plaintext
- **FR-004**: System MUST display the full API key exactly once at creation time with clear warning to save it securely
- **FR-005**: System MUST provide an endpoint to verify API keys (`POST /api/auth/api-key/verify`)
- **FR-006**: System MUST allow admins to revoke (disable) API keys immediately via dashboard
- **FR-007**: System MUST track when each API key was last used (timestamp updated on verification)
- **FR-008**: System MUST support optional expiration dates for API keys with configurable duration
- **FR-009**: System MUST accept API keys via the `x-api-key` HTTP header (Better Auth default)
- **FR-010**: System MUST rate-limit API key verification to prevent brute force attacks (default: 100 requests/minute per key)
- **FR-011**: System MUST provide a list view of all API keys showing name, prefix, status, created date, and last used date
- **FR-012**: System MUST allow admins to delete API keys permanently
- **FR-013**: System MUST support storing custom metadata with API keys (e.g., service name, description)
- **FR-014**: System MUST provide an admin dashboard page at `/admin/service-keys` for key management
- **FR-015**: System MUST show a confirmation dialog before revoking or deleting an API key

### Non-Functional Requirements

- **NFR-001**: API key verification MUST complete in under 100ms for 95% of requests
- **NFR-002**: API key creation MUST complete in under 500ms
- **NFR-003**: The admin UI MUST be accessible and usable on desktop browsers (Chrome, Firefox, Safari, Edge)
- **NFR-004**: All API key operations MUST be logged for audit purposes
- **NFR-005**: The admin UI MUST use consistent styling with existing admin dashboard (shadcn/ui)

### Key Entities

- **API Key**: Represents a machine credential with id, name, hashed key value, user association (owner), enabled status, creation timestamp, last used timestamp, expiration timestamp, rate limit configuration, and custom metadata
- **User (Admin)**: Existing user entity with admin role who creates and manages API keys
- **Service Consumer**: External system (e.g., GitHub Actions, PanaversityFS MCP server) that authenticates using API keys

## Constraints

- API keys are tied to a user account (the admin who creates them) for audit purposes
- API keys use the standard `x-api-key` header format (Better Auth default)
- API key hashing uses Better Auth's built-in secure hashing (no custom implementation)
- Rate limiting is enforced per API key using sliding window algorithm
- Only users with admin role can create, view, revoke, or delete API keys
- API key operations require active session authentication (cookie-based)

## Non-Goals

- **NOT implementing** OAuth 2.0 Client Credentials Grant (using API Keys as alternative until Better Auth supports it)
- **NOT implementing** fine-grained API key scopes/permissions in this iteration (can be added later via metadata)
- **NOT implementing** automatic key rotation (manual rotation via revoke + create new)
- **NOT implementing** multi-tenant key isolation (all keys visible to all admins of the organization)
- **NOT implementing** API key usage analytics/dashboards beyond basic last-used tracking
- **NOT implementing** IP allowlisting per API key (future enhancement)
- **NOT implementing** webhook notifications for key events (future enhancement)

## Assumptions

- Better Auth v1.4.4+ API Key plugin is stable and production-ready
- Database (Neon Postgres) can handle additional `api_key` table without schema migration issues
- Admin users already exist in the system (created via seed or sign-up with admin role)
- The admin dashboard structure already exists at `/admin` route
- Redis is optional - will use database storage for API key rate limiting initially
- shadcn/ui is already configured in the project for admin UI components

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Admins can create a new API key in under 30 seconds from dashboard access
- **SC-002**: Services can verify API keys with 99.9% availability during normal operations
- **SC-003**: Compromised keys can be revoked and become invalid within 5 seconds of admin action
- **SC-004**: 100% of API key create/revoke/delete operations are logged with timestamp and actor
- **SC-005**: API key verification responds in under 100ms for 95th percentile of requests
- **SC-006**: Zero API keys stored in plaintext in database (verified by database audit)
- **SC-007**: Admin UI pages load in under 2 seconds on standard broadband connection

## Security Considerations

- API keys are secrets - treat creation response as highly sensitive
- Never log full API key values, only prefixes (first 8 characters) for identification
- Enforce HTTPS for all API key operations (handled by deployment)
- Rate limit verification endpoint to prevent enumeration attacks (500 requests/min global)
- Consider IP allowlisting for high-security keys (documented as future enhancement)
- Implement proper CSRF protection on admin dashboard forms
- Ensure API key deletion is permanent and irreversible

## Dependencies

- Better Auth API Key plugin enabled in `src/lib/auth.ts`
- Database migration for `api_key` table via Better Auth CLI or Drizzle
- Admin route protection middleware (existing in codebase)
- shadcn/ui components for admin dashboard UI (Table, Button, Dialog, Input, Badge)
- Better Auth client configured with apiKey plugin on client side
