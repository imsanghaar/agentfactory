# Tasks: API Key M2M Authentication

**Input**: Design documents from `/specs/004-api-key-m2m-auth/`
**Prerequisites**: plan.md ✅, spec.md ✅
**Branch**: `004-api-key-m2m-auth`

**Tests**: Included per user request - API tests and E2E tests required

**Organization**: Tasks grouped by user story for independent implementation and testing

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US5)
- Exact file paths included in descriptions

---

## Phase 1: Setup (Backend Infrastructure)

**Purpose**: Enable Better Auth API Key plugin and database schema

- [ ] T001 Add `apiKey` plugin import to `src/lib/auth.ts`
- [ ] T002 Configure API Key plugin with rate limiting options in `src/lib/auth.ts`
- [ ] T003 [P] Add `apiKeyClient` plugin to `src/lib/auth-client.ts`
- [ ] T004 [P] Add `apiKey` table schema to `auth-schema.ts`
- [ ] T005 Generate database migration with `pnpm db:generate`
- [ ] T006 Push migration to database with `pnpm db:push`
- [ ] T007 Verify dev server starts without TypeScript errors

**Checkpoint**: API Key endpoints available at `/api/auth/api-key/*`

---

## Phase 2: Foundational (UI Component Setup)

**Purpose**: Install shadcn/ui components required for admin dashboard

**⚠️ CRITICAL**: Admin UI cannot be built without these components

- [ ] T008 Initialize shadcn/ui with `npx shadcn@latest init`
- [ ] T009 [P] Install button component: `npx shadcn@latest add button`
- [ ] T010 [P] Install dialog component: `npx shadcn@latest add dialog`
- [ ] T011 [P] Install input component: `npx shadcn@latest add input`
- [ ] T012 [P] Install table component: `npx shadcn@latest add table`
- [ ] T013 [P] Install badge component: `npx shadcn@latest add badge`
- [ ] T014 [P] Install alert component: `npx shadcn@latest add alert`
- [ ] T015 [P] Install card component: `npx shadcn@latest add card`
- [ ] T016 Verify shadcn components work with existing Tailwind config

**Checkpoint**: UI component library ready for admin pages

---

## Phase 3: User Story 1 - Admin Creates Service API Key (Priority: P1) 🎯 MVP

**Goal**: Admin can create API keys with name and optional expiration

**Independent Test**: Admin signs in → navigates to Service Keys → creates key → sees key displayed once → key appears in list

### Tests for User Story 1

- [ ] T017 [P] [US1] API test: create key with name succeeds in `tests/test-api-key.js`
- [ ] T018 [P] [US1] API test: create key without auth fails 401 in `tests/test-api-key.js`
- [ ] T019 [P] [US1] API test: create key with empty name fails in `tests/test-api-key.js`
- [ ] T020 [P] [US1] E2E test: admin can create key via UI in `tests/test-api-key-e2e.js`
- [ ] T021 [P] [US1] E2E test: key display shows once warning in `tests/test-api-key-e2e.js`
- [ ] T022 [P] [US1] E2E test: non-admin cannot access service keys page in `tests/test-api-key-e2e.js`

### Implementation for User Story 1

- [ ] T023 [US1] Create Service Keys page at `src/app/admin/service-keys/page.tsx`
- [ ] T024 [P] [US1] Create CreateKeyDialog component at `src/app/admin/service-keys/components/create-key-dialog.tsx`
- [ ] T025 [P] [US1] Create KeyDisplayDialog component at `src/app/admin/service-keys/components/key-display-dialog.tsx`
- [ ] T026 [US1] Create ApiKeyList component at `src/app/admin/service-keys/components/api-key-list.tsx`
- [ ] T027 [US1] Wire CreateKeyDialog to `authClient.apiKey.create()` in page
- [ ] T028 [US1] Wire KeyDisplayDialog to show key once with copy button
- [ ] T029 [US1] Add "I've saved this key" confirmation before closing KeyDisplayDialog

**Checkpoint**: Admin can create keys, see them once, and view list. US1 fully testable.

---

## Phase 4: User Story 2 - Service Authenticates with API Key (Priority: P1)

**Goal**: External services can verify API keys via POST endpoint

**Independent Test**: Create key → use key in `x-api-key` header → call verify endpoint → receive valid:true response

### Tests for User Story 2

- [ ] T030 [P] [US2] API test: verify valid key returns valid:true in `tests/test-api-key.js`
- [ ] T031 [P] [US2] API test: verify invalid key returns valid:false in `tests/test-api-key.js`
- [ ] T032 [P] [US2] API test: verify key response includes metadata in `tests/test-api-key.js`

### Implementation for User Story 2

- [ ] T033 [US2] Add custom rate limit rule for `/api/auth/api-key/verify` in `src/lib/auth.ts`
- [ ] T034 [US2] Test verify endpoint with curl command manually
- [ ] T035 [US2] Verify lastUsed timestamp updates after verification

**Checkpoint**: Services can authenticate with API keys. US2 fully testable.

---

## Phase 5: User Story 3 - Admin Revokes Compromised API Key (Priority: P2)

**Goal**: Admin can immediately disable a potentially compromised key

**Independent Test**: Create key → verify it works → revoke it → verify it fails

### Tests for User Story 3

- [ ] T036 [P] [US3] API test: revoked key returns valid:false in `tests/test-api-key.js`
- [ ] T037 [P] [US3] E2E test: admin can revoke key via UI in `tests/test-api-key-e2e.js`
- [ ] T038 [P] [US3] E2E test: revoke shows confirmation dialog in `tests/test-api-key-e2e.js`

### Implementation for User Story 3

- [ ] T039 [P] [US3] Create RevokeKeyDialog component at `src/app/admin/service-keys/components/revoke-key-dialog.tsx`
- [ ] T040 [US3] Wire RevokeKeyDialog to `authClient.apiKey.update({ keyId, enabled: false })`
- [ ] T041 [US3] Add status badge (Active/Revoked) to ApiKeyList component
- [ ] T042 [US3] Update list immediately after revoke action

**Checkpoint**: Compromised keys can be disabled instantly. US3 fully testable.

---

## Phase 6: User Story 4 - Admin Views API Key Usage (Priority: P2)

**Goal**: Admin can see when keys were last used

**Independent Test**: Use key several times → view key list → see Last Used timestamp updated

### Tests for User Story 4

- [ ] T043 [P] [US4] API test: list keys includes lastUsed field in `tests/test-api-key.js`
- [ ] T044 [P] [US4] E2E test: key list shows last used date in `tests/test-api-key-e2e.js`

### Implementation for User Story 4

- [ ] T045 [US4] Add Last Used column to ApiKeyList table in `src/app/admin/service-keys/components/api-key-list.tsx`
- [ ] T046 [US4] Format Last Used as relative time (e.g., "2 hours ago")
- [ ] T047 [US4] Show "Never" for keys that haven't been used

**Checkpoint**: Admins can monitor key usage. US4 fully testable.

---

## Phase 7: User Story 5 - Admin Sets Key Expiration (Priority: P3)

**Goal**: Admin can create time-limited API keys

**Independent Test**: Create key with 30-day expiration → verify expiration date shown → after expiry verify fails

### Tests for User Story 5

- [ ] T048 [P] [US5] API test: expired key returns valid:false in `tests/test-api-key.js`
- [ ] T049 [P] [US5] E2E test: can select expiration option when creating key in `tests/test-api-key-e2e.js`

### Implementation for User Story 5

- [ ] T050 [US5] Add expiration dropdown to CreateKeyDialog (Never, 30 days, 90 days, 1 year)
- [ ] T051 [US5] Pass expiresAt to `authClient.apiKey.create()` call
- [ ] T052 [US5] Add Expires column to ApiKeyList showing expiration date or "Never"
- [ ] T053 [US5] Add "Expired" status badge for expired keys

**Checkpoint**: Time-limited keys work correctly. US5 fully testable.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Navigation, cleanup, and documentation

- [ ] T054 Add "Service Keys" nav link to `src/app/admin/layout.tsx`
- [ ] T055 [P] Create DeleteKeyDialog component at `src/app/admin/service-keys/components/delete-key-dialog.tsx`
- [ ] T056 Wire DeleteKeyDialog with name confirmation to `authClient.apiKey.delete()`
- [ ] T057 [P] Add loading states to all dialogs and list
- [ ] T058 [P] Add empty state for when no keys exist
- [ ] T059 [P] API test: delete key removes from list in `tests/test-api-key.js`
- [ ] T060 [P] API test: rate limit returns 429 after threshold in `tests/test-api-key.js`
- [ ] T061 Update `docs/integration-guide.md` with API key section
- [ ] T062 Add GitHub issue #6 comment with completion status
- [ ] T063 Run all tests and verify pass: `pnpm test-api && pnpm test-e2e`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - backend must be enabled first
- **Foundational (Phase 2)**: Depends on Setup - shadcn required for UI
- **User Stories (Phase 3-7)**: All depend on Phase 1 + 2 completion
  - US1 + US2 (P1): Can proceed in parallel after Phase 2
  - US3 + US4 (P2): Can proceed after US1 (need list component)
  - US5 (P3): Can proceed after US1 (need create dialog)
- **Polish (Phase 8)**: Depends on all user stories complete

### User Story Dependencies

- **US1 (P1)**: Can start after Foundational - Creates base page and list
- **US2 (P1)**: Can start after Setup (Phase 1 only) - No UI dependency
- **US3 (P2)**: Depends on US1 (needs ApiKeyList component)
- **US4 (P2)**: Depends on US1 (needs ApiKeyList component)
- **US5 (P3)**: Depends on US1 (needs CreateKeyDialog component)

### Within Each User Story

- Tests written and verified to fail before implementation
- Components before page integration
- Core implementation before polish

### Parallel Opportunities

- Phase 2: All shadcn component installs (T009-T015) can run in parallel
- Phase 3: All US1 tests (T017-T022) can run in parallel
- Phase 3: CreateKeyDialog and KeyDisplayDialog (T024-T025) can run in parallel
- Phase 5: RevokeKeyDialog (T039) is independent
- Phase 8: Loading states, empty state, docs all parallel

---

## Parallel Example: Phase 2 (shadcn Install)

```bash
# Launch all shadcn component installs together:
npx shadcn@latest add button
npx shadcn@latest add dialog
npx shadcn@latest add input
npx shadcn@latest add table
npx shadcn@latest add badge
npx shadcn@latest add alert
npx shadcn@latest add card
```

## Parallel Example: User Story 1 Tests

```bash
# Launch all US1 tests together:
Task: "API test: create key with name succeeds in tests/test-api-key.js"
Task: "API test: create key without auth fails 401 in tests/test-api-key.js"
Task: "E2E test: admin can create key via UI in tests/test-api-key-e2e.js"
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 Only)

1. Complete Phase 1: Setup - Backend enabled
2. Complete Phase 2: Foundational - UI components ready
3. Complete Phase 3: User Story 1 - Admin can create keys
4. Complete Phase 4: User Story 2 - Services can verify keys
5. **STOP and VALIDATE**: Test create + verify flow end-to-end
6. Deploy if ready - MVP complete!

### Incremental Delivery

1. Setup + Foundational → Backend + UI ready
2. Add US1 + US2 → Create + Verify works → Deploy (MVP!)
3. Add US3 → Revoke works → Deploy
4. Add US4 → Usage tracking works → Deploy
5. Add US5 → Expiration works → Deploy
6. Polish → Docs, cleanup, GitHub issue closed

---

## Summary

| Phase | Tasks | Parallel |
|-------|-------|----------|
| Setup | T001-T007 | 2 |
| Foundational | T008-T016 | 7 |
| US1 (P1) | T017-T029 | 8 |
| US2 (P1) | T030-T035 | 3 |
| US3 (P2) | T036-T042 | 4 |
| US4 (P2) | T043-T047 | 2 |
| US5 (P3) | T048-T053 | 2 |
| Polish | T054-T063 | 6 |

**Total Tasks**: 63
**MVP Tasks**: T001-T035 (35 tasks for US1 + US2)
