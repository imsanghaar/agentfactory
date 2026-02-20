# SSO Organization & Role Management UI

## Status: READY FOR IMPLEMENTATION

All questions answered. See plan.md for implementation steps.

---

## 1. Executive Summary

The SSO app has **full backend support** for organizations, members, invitations, and roles via Better Auth's organization plugin, but **lacks all management UI**. A reference implementation exists at `taskforce_agent1/apps/sso` that can be adapted with minimal changes.

**Scope**: Add organization management UI for both regular users and admins.

**Effort Estimate**: 2-3 days (primarily copying and adapting existing components)

---

## 2. Current State Analysis

### 2.1 What EXISTS (Backend)

| Feature               | Status                | Location                         |
| --------------------- | --------------------- | -------------------------------- |
| Organization plugin   | ✅ Configured         | `src/lib/auth.ts` line 6         |
| organizationClient    | ✅ Configured         | `src/lib/auth-client.ts` line 16 |
| organization table    | ✅ Schema exists      | `auth-schema.ts`                 |
| member table          | ✅ Schema exists      | `auth-schema.ts`                 |
| invitation table      | ✅ Schema exists      | `auth-schema.ts`                 |
| Default org auto-join | ✅ On signup          | `src/lib/auth.ts` lines 35-71    |
| Admin plugin          | ✅ Configured         | User role management             |
| Scopes system         | ✅ 23 granular scopes | `src/lib/scopes.ts`              |

### 2.2 What EXISTS (UI)

| Page                    | Status | Path                  |
| ----------------------- | ------ | --------------------- |
| Admin Dashboard         | ✅     | `/admin`              |
| User Management         | ✅     | `/admin/users`        |
| OAuth Clients           | ✅     | `/admin/clients`      |
| Service Keys (API Keys) | ✅     | `/admin/service-keys` |
| User Profile            | ✅     | `/account/profile`    |

### 2.3 What's MISSING (UI)

| Feature                        | Priority | Notes                        |
| ------------------------------ | -------- | ---------------------------- |
| **Organization list page**     | P0       | User's orgs with switching   |
| **Create organization dialog** | P0       | Form with name, slug, logo   |
| **Member management page**     | P0       | List, invite, remove members |
| **Role management**            | P0       | Change member roles          |
| **Pending invitations**        | P1       | View, resend, cancel         |
| **Accept invitation page**     | P1       | `/accept-invitation/[id]`    |
| **Org general settings**       | P1       | Update name, logo            |
| **Org danger zone**            | P2       | Transfer ownership, delete   |
| **Admin org dashboard**        | P2       | System-wide org oversight    |

---

## 3. Reference Implementation Analysis

### 3.1 Source Codebase

Location: `/Users/mjs/Documents/code/mjunaidca/taskforce_agent1/apps/sso`

This is a fork of the same SSO codebase, updated with full org management UI.

### 3.2 Components to Copy

#### User-Facing Organization UI

```
src/app/account/organizations/
├── page.tsx                    # Org list with grid cards
├── components/
│   ├── CreateOrgDialog.tsx     # Create org modal
│   ├── OrgSwitcher.tsx         # Quick org switch dropdown
│   ├── OrganizationCard.tsx    # Org card with actions
│   └── OrganizationCardSkeleton.tsx
├── [orgId]/settings/
│   ├── layout.tsx              # Settings sidebar layout
│   ├── page.tsx                # Redirects to general
│   ├── general/
│   │   ├── page.tsx
│   │   └── components/GeneralSettingsForm.tsx
│   ├── members/
│   │   ├── page.tsx            # Members list + invitations
│   │   └── components/
│   │       ├── InviteMemberDialog.tsx
│   │       ├── MemberList.tsx
│   │       ├── PendingInvitations.tsx
│   │       ├── RoleChangeDialog.tsx
│   │       └── RemoveMemberDialog.tsx
│   └── danger/
│       ├── page.tsx
│       └── components/
│           ├── TransferOwnershipSection.tsx
│           └── DeleteOrgSection.tsx
```

#### Accept Invitation Flow

```
src/app/accept-invitation/
├── [invitationId]/
│   ├── page.tsx
│   └── components/AcceptInvitationCard.tsx
```

#### Admin Organization Dashboard (Optional)

```
src/app/admin/organizations/
├── page.tsx                    # Admin org list with stats
└── components/
    ├── AdminOrgTable.tsx       # Paginated table
    ├── BulkActionsBar.tsx      # Bulk operations
    └── OrgDetailsModal.tsx     # View org details
```

#### Shared Components

```
src/components/organizations/
├── OrgBadge.tsx               # Role badge with colors
├── OrgLogo.tsx                # Logo/avatar display
└── SlugInput.tsx              # Slug validation input
```

#### Utility Functions

```
src/lib/utils/
└── organization.ts            # formatMemberCount, getRoleDisplay, etc.
```

### 3.3 Adaptation Required

| Item            | Change Needed                                  |
| --------------- | ---------------------------------------------- |
| Import paths    | `@/lib/db/schema-export` → `../../auth-schema` |
| Brand colors    | `taskflow-500` → appropriate brand colors      |
| Logo references | TaskFlow logo → RoboLearn/AgentFactory         |
| Toast system    | Verify compatibility with existing toast       |

---

## 4. Role System Analysis

### 4.1 Current Roles

**Global Level** (user.role):

- `user` (default)
- `admin`

**Organization Level** (member.role):

- `owner` - Full control, can delete org
- `admin` - Full control except ownership transfer/deletion
- `member` - Read-only access

### 4.2 Better Auth Default Permissions

| Role   | organization   | member                 | invitation     |
| ------ | -------------- | ---------------------- | -------------- |
| owner  | update, delete | create, update, delete | create, cancel |
| admin  | update         | create, update, delete | create, cancel |
| member | (none)         | (none)                 | (none)         |

### 4.3 Static Custom Roles - CONFIRMED APPROACH

**Decision**: Use **hardcoded/static roles** defined in code. No database changes.

**Why static over dynamic**:
- ✅ No database migration needed
- ✅ Safer - roles defined in code, not runtime
- ✅ Simpler - no role CRUD UI needed
- ✅ Type-safe - TypeScript knows all roles

**Implementation** (in code, not DB):

```typescript
// src/lib/permissions.ts
import { createAccessControl } from "better-auth/plugins/access";
import { defaultStatements } from "better-auth/plugins/organization/access";

const statement = {
  ...defaultStatements,
  content: ["create", "read", "update", "delete"],
  courses: ["create", "read", "update", "delete", "publish"],
  billing: ["read", "update"],
} as const;

export const ac = createAccessControl(statement);

export const owner = ac.newRole({ /* full permissions */ });
export const admin = ac.newRole({ /* admin permissions */ });
export const editor = ac.newRole({ content: ["create", "read", "update"], courses: ["read", "update"] });
export const member = ac.newRole({ content: ["read"], courses: ["read"] });
```

```typescript
// In auth.ts organization plugin config
import { ac, owner, admin, editor, member } from "./permissions";

organization({
  ac,
  roles: { owner, admin, editor, member },
  // NO dynamicAccessControl - roles are static
})
```

**UI needed**:
- Update RoleChangeDialog to show all hardcoded roles in dropdown
- No role management page needed (roles are fixed in code)
- To add new roles: update permissions.ts and redeploy

---

## 5. Implementation Plan

### Phase 1: Core Organization UI (P0) - Day 1

1. **Copy shared components**
   - `src/components/organizations/` (OrgBadge, OrgLogo, SlugInput)
   - `src/lib/utils/organization.ts`

2. **Add organization list page**
   - Copy `src/app/account/organizations/page.tsx`
   - Copy `components/` (CreateOrgDialog, OrganizationCard, etc.)
   - Adapt import paths

3. **Add member management**
   - Copy `[orgId]/settings/members/` structure
   - All member components (InviteMemberDialog, MemberList, etc.)

4. **Update navigation**
   - Add "Organizations" link to account layout
   - Add org switcher to header (optional)

### Phase 2: Settings & Invitations (P1) - Day 2

1. **General settings page**
   - Copy `[orgId]/settings/general/`
   - Org name, slug, logo update

2. **Accept invitation flow**
   - Copy `src/app/accept-invitation/`
   - Verify invitation email sending is configured

3. **Settings layout**
   - Copy settings sidebar layout
   - Navigation between settings tabs

### Phase 3: Admin & Danger Zone (P2) - Day 3

1. **Danger zone**
   - Transfer ownership
   - Delete organization

2. **Admin organizations dashboard** (if needed)
   - System-wide org management
   - Bulk operations

---

## 6. Questions Requiring Answers

### Q1: Invitation Email Configuration ⚠️ BLOCKER IDENTIFIED

**FINDING**: Invitation emails are **NOT configured**. The organization plugin at line 812-815 only has:

```typescript
organization({
  allowUserToCreateOrganization: true,
}),
```

**Missing**: The `sendInvitationEmail` callback is not present.

**Impact**: Member invitations will be created in the database, but no email will be sent. Users won't know they've been invited.

**Required fix**: Add `sendInvitationEmail` to the organization plugin config using the existing `sendEmail()` helper function. Template should match the existing password reset and verification email styles.

---

### Q2: Default Organization Behavior ✅ ANSWERED

**Current**: New users auto-join `DEFAULT_ORG_ID` on signup.

**Answers**:

1. ❌ Regular users CANNOT create organizations - **Admin only**
2. No limit on organizations
3. Yes, show default org in the list

**Implementation Change Required**:

```typescript
organization({
  allowUserToCreateOrganization: async (user) => {
    // Only admins can create organizations
    return user.role === "admin";
  },
  // ... sendInvitationEmail
}),
```

**UI Impact**:

- Hide "Create Organization" button for non-admin users
- Only admins see the create org dialog

---

### Q3: Admin Org Dashboard ✅ ANSWERED

**Answer**: Yes, add `/admin/organizations` page for admin-only system-wide org management.

**Implementation**:
- Add "Organizations" link in admin navbar (Dashboard | Users | **Organizations** | Clients | Service Keys)
- Stats cards: Total orgs, orgs created this month
- Table of ALL organizations with search, filter, view details
- Click into any org to manage its members/roles

---

### Q4: Schema Export Path

**Reference uses**: `@/lib/db/schema-export`

**Current SSO uses**: `../../auth-schema` (relative imports)

**Question**: Should we create a schema-export.ts for cleaner imports, or keep current pattern?

**Recommendation**: Keep current pattern for consistency, just adapt imports.

---

### Q5: Navigation Placement ✅ ANSWERED

**Answer**: Yes to org switcher in admin header for quick org switching when managing users/roles.

**Implementation**:
- Add org switcher dropdown in admin header
- Shows current active org + quick switch to other orgs
- Useful when admin needs to manage users/roles within specific orgs
- "Organizations" also appears in admin navbar for full org list

---

## 7. Technical Specifications

### 7.1 New Routes

| Route                                             | Purpose             | Auth Required         |
| ------------------------------------------------- | ------------------- | --------------------- |
| `/account/organizations`                          | List user's orgs    | Session               |
| `/account/organizations/[orgId]/settings`         | Org settings layout | Session + Membership  |
| `/account/organizations/[orgId]/settings/general` | General settings    | Session + Owner/Admin |
| `/account/organizations/[orgId]/settings/members` | Member management   | Session + Membership  |
| `/account/organizations/[orgId]/settings/danger`  | Danger zone         | Session + Owner       |
| `/accept-invitation/[invitationId]`               | Accept invite       | Session               |
| `/admin/organizations`                            | Admin org list      | Session + Admin role  |

### 7.2 API Endpoints (Already Exist via Better Auth)

All these are provided by Better Auth's organization plugin:

```
POST /api/auth/organization/create
POST /api/auth/organization/update
POST /api/auth/organization/delete
POST /api/auth/organization/set-active
GET  /api/auth/organization/list
GET  /api/auth/organization/get-full-organization

POST /api/auth/organization/invite-member
POST /api/auth/organization/accept-invitation
POST /api/auth/organization/reject-invitation
POST /api/auth/organization/cancel-invitation
GET  /api/auth/organization/list-invitations

GET  /api/auth/organization/list-members
POST /api/auth/organization/update-member-role
POST /api/auth/organization/remove-member
```

### 7.3 Database Schema (Already Exists)

```sql
-- organization table
id, name, slug, logo, metadata, createdAt

-- member table
id, organizationId, userId, role, createdAt

-- invitation table
id, organizationId, email, role, status, expiresAt, inviterId, createdAt
```

---

## 8. Acceptance Criteria

### Must Have (P0)

- [ ] User can view list of their organizations
- [ ] User can create a new organization
- [ ] User can switch active organization
- [ ] Owner/Admin can invite members via email
- [ ] Owner/Admin can view pending invitations
- [ ] Owner/Admin can change member roles
- [ ] Owner/Admin can remove members
- [ ] User can accept invitation (if invitation email is configured)

### Should Have (P1)

- [ ] Owner/Admin can update org name and logo
- [ ] Owner/Admin can cancel pending invitations
- [ ] Owner/Admin can resend invitation emails
- [ ] Settings navigation with tabs (General, Members)

### Should Have (P2) - Confirmed

- [ ] Owner can transfer ownership
- [ ] Owner can delete organization
- [ ] **Admin can view ALL organizations system-wide** (`/admin/organizations`)
- [ ] **Org switcher in admin header** for quick org switching

### Must Have (P0) - Static Role Assignment

- [ ] Define custom roles in `src/lib/permissions.ts` (owner, admin, editor, member, etc.)
- [ ] Pass roles to organization plugin in auth.ts
- [ ] Update RoleChangeDialog to show ALL roles (not just hardcoded 3)
- [ ] **Admin can assign any predefined role to members**
- [ ] ❌ NO database changes for roles
- [ ] ❌ NO runtime role creation UI (roles are in code)

---

## 9. Risk Assessment

| Risk                               | Impact | Mitigation                                          |
| ---------------------------------- | ------ | --------------------------------------------------- |
| Invitation emails not configured   | High   | Verify sendInvitationEmail in auth.ts before launch |
| Import path mismatches             | Low    | Test all pages after copying                        |
| Toast/notification incompatibility | Low    | Verify toast system matches                         |
| Brand color inconsistencies        | Low    | Search-replace brand colors                         |

---

## 10. File Copy Checklist

```bash
# From: /Users/mjs/Documents/code/mjunaidca/taskforce_agent1/apps/sso
# To:   /Users/mjs/Documents/code/panaversity-official/tutorsgpt/agentfactory/apps/sso

# Phase 1 - Core (Day 1)
src/components/organizations/          → adapt imports
src/lib/utils/organization.ts          → adapt imports
src/app/account/organizations/         → adapt imports, remove [orgId]/settings initially

# Phase 2 - Settings (Day 2)
src/app/account/organizations/[orgId]/ → full settings structure
src/app/accept-invitation/             → invitation acceptance flow

# Phase 3 - Admin (Day 3)
src/app/admin/organizations/           → if needed
```

---

## 11. Next Steps

1. **Review this spec** - Confirm scope and priorities
2. **Answer Questions** - Especially Q1 (invitation emails), Q2 (default org behavior)
3. **Begin Phase 1** - Copy core components, test org list page
4. **Iterate** - Add settings and admin as needed

---

## Appendix A: Reference Component Dependencies

### Components Used by OrganizationCard

```typescript
// UI components (should exist in current SSO)
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader } from "@/components/ui/card"
import { DropdownMenu, ... } from "@/components/ui/dropdown-menu"

// Custom components (need to copy)
import { OrgBadge } from "@/components/organizations/OrgBadge"
```

### Components Used by MemberList

```typescript
import { Table, TableBody, ... } from "@/components/ui/table"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { RoleChangeDialog } from "./RoleChangeDialog"
import { RemoveMemberDialog } from "./RemoveMemberDialog"
```

### Auth Client Methods Used

```typescript
// All from authClient.organization namespace
authClient.organization.create();
authClient.organization.setActive();
authClient.organization.inviteMember();
authClient.organization.cancelInvitation();
authClient.organization.acceptInvitation();
authClient.organization.updateMemberRole();
authClient.organization.removeMember();
authClient.organization.delete();
```

All these methods are already available via the configured `organizationClient()` plugin.
