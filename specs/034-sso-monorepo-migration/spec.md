# Feature Specification: SSO Monorepo Migration

**Feature Branch**: `034-sso-monorepo-migration`
**Created**: 2025-12-16
**Status**: Draft
**Input**: User description: "Migrate SSO repository (https://github.com/panaversity/sso) into this Nx monorepo using git subtree. Delete foundations/ folder, add Nx Next.js plugin, place SSO app in apps/sso/. Leave .claude/.specify/CLAUDE.md for human review."

## Overview

Migrate the standalone SSO (Single Sign-On) authentication server from its separate repository into this Nx monorepo. The SSO project is a Next.js application that provides OAuth2/OIDC authentication services. This migration consolidates the platform's core infrastructure into a single, cohesive codebase while preserving git history.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Runs SSO Locally (Priority: P1)

A developer clones the monorepo and wants to run the SSO authentication server alongside the learn-app for local development.

**Why this priority**: Without the ability to run SSO locally, developers cannot test authentication flows or work on auth-related features.

**Independent Test**: Developer runs `pnpm nx serve sso` from repo root and SSO server starts on port 3001, accessible at http://localhost:3001.

**Acceptance Scenarios**:

1. **Given** a fresh clone of the monorepo, **When** developer runs `pnpm install && pnpm nx serve sso`, **Then** SSO server starts successfully on port 3001
2. **Given** SSO server is running, **When** developer accesses http://localhost:3001, **Then** the SSO login/admin interface loads correctly
3. **Given** SSO server is running, **When** developer makes code changes to apps/sso/src/, **Then** Next.js hot reload reflects changes immediately

---

### User Story 2 - CI Builds SSO as Affected Project (Priority: P1)

When a developer modifies SSO code and opens a PR, CI should detect SSO as affected and run lint/test/build for it.

**Why this priority**: CI integration ensures SSO quality gates work within the monorepo's affected-based workflow.

**Independent Test**: Modify a file in apps/sso/, push to PR, observe CI runs `nx affected -t lint test build` and includes SSO project.

**Acceptance Scenarios**:

1. **Given** a PR with changes only in apps/sso/, **When** CI runs, **Then** only SSO project (and its dependents) are tested/built
2. **Given** SSO lint target configured, **When** `pnpm nx lint sso` runs, **Then** ESLint checks pass (or report fixable issues)
3. **Given** SSO build target configured, **When** `pnpm nx build sso` runs, **Then** Next.js production build completes successfully

---

### User Story 3 - Git History Preserved (Priority: P2)

A developer wants to trace the history of a file in apps/sso/ to understand when and why changes were made.

**Why this priority**: Preserving history enables debugging, blame tracking, and understanding architectural decisions.

**Independent Test**: Run `git log --oneline apps/sso/src/app/page.tsx` and see commit history from original SSO repository.

**Acceptance Scenarios**:

1. **Given** SSO migrated via git subtree, **When** developer runs `git log apps/sso/`, **Then** commits from original SSO repo appear in history
2. **Given** a specific file in apps/sso/, **When** developer runs `git blame`, **Then** original authors and commit messages are visible

---

### User Story 4 - Human Reviews Conflicting Files (Priority: P3)

After migration, a human reviewer examines .claude/, .specify/, and CLAUDE.md files to decide what to merge, keep, or discard.

**Why this priority**: Dot files contain project-specific intelligence that requires human judgment to merge properly.

**Independent Test**: After migration, conflicting files are clearly identified in a TODO list or marked for review.

**Acceptance Scenarios**:

1. **Given** SSO has .claude/ folder, **When** migration completes, **Then** apps/sso/.claude/ exists for human review
2. **Given** SSO has CLAUDE.md, **When** migration completes, **Then** apps/sso/CLAUDE.md exists alongside root CLAUDE.md
3. **Given** list of conflicting files, **When** human reviews, **Then** clear documentation exists on what each file contains

---

### Edge Cases

- What happens if git subtree add fails due to merge conflicts? → Migration aborts cleanly, no partial state
- What happens if SSO's pnpm-lock.yaml conflicts with root? → SSO's lockfile is deleted; dependencies merge into root
- What happens if SSO uses different Node/pnpm versions? → Root versions take precedence; document any compatibility issues
- What happens to SSO's .env.example? → Preserved in apps/sso/ for reference; developers create apps/sso/.env locally

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST use git subtree to import SSO repository into apps/sso/ prefix, preserving commit history
- **FR-002**: System MUST delete apps/sso/foundation/ directory after import (contains course content, not needed)
- **FR-003**: System MUST add @nx/next plugin to enable Next.js project support
- **FR-004**: System MUST create apps/sso/project.json with standard Nx targets (serve, build, lint, test)
- **FR-005**: System MUST update pnpm-workspace.yaml if needed (apps/* pattern already covers apps/sso/)
- **FR-006**: System MUST delete SSO's standalone pnpm-lock.yaml (root lockfile governs all JS/TS deps)
- **FR-007**: System MUST preserve SSO's .env.example for reference
- **FR-008**: System MUST preserve SSO's drizzle/ folder and database configuration
- **FR-009**: System MUST preserve SSO's tests/ folder for future CI integration
- **FR-010**: System MUST NOT automatically merge .claude/, .specify/, or CLAUDE.md files (human review required)

### Non-Functional Requirements

- **NFR-001**: Migration MUST complete in a single git subtree operation (atomic import)
- **NFR-002**: Migration MUST NOT break existing learn-app or panaversity-fs-py projects
- **NFR-003**: SSO MUST be runnable via `pnpm nx serve sso` after migration

### Key Entities

- **SSO App**: Next.js authentication server, provides OAuth2/OIDC endpoints, admin UI for client management
- **Drizzle Schema**: Database schema definitions for users, sessions, OAuth clients, organizations
- **Tests**: API tests, E2E tests using Playwright for OAuth flows

## Constraints

- **C-001**: SSO runs on port 3001 (different from learn-app's 3000) - this must be preserved
- **C-002**: SSO uses Neon PostgreSQL - database connection requires separate .env configuration
- **C-003**: SSO's Next.js version must be compatible with @nx/next plugin
- **C-004**: Cannot modify SSO's core authentication logic during migration (scope is infrastructure only)

## Non-Goals (Out of Scope)

- **NG-001**: NOT integrating SSO authentication into learn-app (separate feature)
- **NG-002**: NOT migrating SSO's database or running migrations (infrastructure only)
- **NG-003**: NOT resolving .claude/.specify/CLAUDE.md conflicts (human review phase)
- **NG-004**: NOT modifying SSO's source code beyond what's needed for Nx integration
- **NG-005**: NOT setting up SSO deployment pipelines (existing deploy.yml may need updates later)

## Assumptions

- SSO repository is accessible at https://github.com/panaversity/sso and can be fetched
- @nx/next plugin is compatible with SSO's Next.js version
- SSO's dependencies don't conflict with existing monorepo dependencies
- pnpm workspace's apps/* pattern will automatically include apps/sso/
- Human reviewer will handle .claude/, .specify/, CLAUDE.md integration as a follow-up task

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pnpm nx serve sso` starts SSO server successfully within 30 seconds
- **SC-002**: `pnpm nx build sso` produces production build without errors
- **SC-003**: `pnpm nx lint sso` runs without configuration errors (lint issues may exist)
- **SC-004**: `git log --oneline apps/sso/ | head -20` shows commits from original SSO repository
- **SC-005**: `pnpm nx graph` shows sso project in the project graph
- **SC-006**: CI workflow (`nx affected -t build`) correctly detects SSO as affected when apps/sso/ changes
- **SC-007**: apps/sso/foundation/ directory does NOT exist after migration
- **SC-008**: Root pnpm-lock.yaml includes SSO dependencies (no separate lockfile in apps/sso/)

## Dependencies

- Existing monorepo Nx setup (nx.json, pnpm-workspace.yaml)
- @nx/next plugin (to be added)
- SSO repository on GitHub (https://github.com/panaversity/sso)

## Files to Review (Human Task)

After migration, the following files require human review to determine integration strategy:

| SSO File | Monorepo Equivalent | Action Needed |
|----------|---------------------|---------------|
| apps/sso/.claude/ | .claude/ | Merge useful agents/skills or delete |
| apps/sso/.specify/ | .specify/ | Merge templates or delete |
| apps/sso/CLAUDE.md | CLAUDE.md | Extract SSO-specific rules or delete |
| apps/sso/.mcp.json | .mcp.json | Merge MCP server configs or delete |
| apps/sso/specs/ | specs/ | Archive or merge historical specs |
| apps/sso/history/ | history/ | Archive or merge PHRs |
