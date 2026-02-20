# SSO Organization Management - Implementation Plan

## Status: READY FOR IMPLEMENTATION

---

## Pre-Implementation Checklist

- [x] **Q1** - Add invitation email ✅
- [x] **Q2** - Admin-only org creation ✅
- [x] **Q3** - Add `/admin/organizations` page ✅
- [x] **Q5** - Add org switcher in admin header ✅

**All questions answered - Ready to implement**

---

## Blocker: Invitation Email (Must Fix First)

**File**: `apps/sso/src/lib/auth.ts` around line 812

**Current**:

```typescript
organization({
  allowUserToCreateOrganization: true,
}),
```

**Required**:

```typescript
organization({
  // Only admins can create organizations (confirmed requirement)
  allowUserToCreateOrganization: async (user) => {
    return user.role === "admin";
  },
  async sendInvitationEmail(data) {
    const appName = process.env.NEXT_PUBLIC_APP_NAME || "Panaversity SSO";
    const appDescription = process.env.NEXT_PUBLIC_APP_DESCRIPTION || "Secure Single Sign-On";
    const orgName = process.env.NEXT_PUBLIC_ORG_NAME || "Panaversity";

    const inviteLink = `${process.env.BETTER_AUTH_URL || process.env.NEXT_PUBLIC_BETTER_AUTH_URL}/accept-invitation/${data.id}`;

    await sendEmail({
      to: data.email,
      subject: `You've been invited to join ${data.organization.name}`,
      html: `
        <!DOCTYPE html>
        <html lang="en">
        <head>...</head>
        <body>
          <!-- Invitation email template matching existing style -->
          <!-- Include: inviter name, org name, role, accept button -->
        </body>
        </html>
      `,
    });
  },
}),
```

**Effort**: ~30 minutes (template already exists, just needs adaptation)

---

## Phase 1: Core Organization UI (Day 1)

### Task 1.1: Copy Shared Components

**Copy from**: `taskforce_agent1/apps/sso/src/components/organizations/`
**Copy to**: `agentfactory/apps/sso/src/components/organizations/`

Files:

- `OrgBadge.tsx` - Role badge with colors
- `OrgLogo.tsx` - Logo/avatar display
- `SlugInput.tsx` - Slug validation input

**Adaptations**:

- Replace `taskflow-500` → `primary` (or appropriate brand color)

---

### Task 1.2: Copy Organization Utility Functions

**Copy from**: `taskforce_agent1/apps/sso/src/lib/utils/organization.ts`
**Copy to**: `agentfactory/apps/sso/src/lib/utils/organization.ts`

Functions:

- `formatMemberCount()`
- `getRoleDisplay()`
- `sanitizeSlug()`

---

### Task 1.3: Copy Organization List Page

**Copy from**: `taskforce_agent1/apps/sso/src/app/account/organizations/`
**Copy to**: `agentfactory/apps/sso/src/app/account/organizations/`

Files:

- `page.tsx` - Main org list
- `loading.tsx` - Loading skeleton
- `error.tsx` - Error boundary
- `components/CreateOrgDialog.tsx`
- `components/OrganizationCard.tsx`
- `components/OrganizationCardSkeleton.tsx`
- `components/OrgSwitcher.tsx` (optional)

**Adaptations**:

- Import: `@/lib/db/schema-export` → `../../../auth-schema` (or create schema-export)
- Styling: `taskflow-*` → brand colors
- Branding: TaskFlow → RoboLearn

---

### Task 1.4: Copy Member Management Page

**Copy from**: `taskforce_agent1/apps/sso/src/app/account/organizations/[orgId]/settings/members/`
**Copy to**: `agentfactory/apps/sso/src/app/account/organizations/[orgId]/settings/members/`

Files:

- `page.tsx` - Members list + invitations
- `components/InviteMemberDialog.tsx`
- `components/MemberList.tsx`
- `components/PendingInvitations.tsx`
- `components/RoleChangeDialog.tsx`
- `components/RemoveMemberDialog.tsx`

**Adaptations**:

- Same import path changes
- Ensure toast system compatible

---

### Task 1.5: Update Account Layout Navigation

**File**: `agentfactory/apps/sso/src/app/account/layout.tsx`

**Add**: Link to "Organizations" in sidebar/navigation

---

### Task 1.6: Test Core Functionality

- [ ] View organization list
- [ ] Create new organization
- [ ] Switch active organization
- [ ] View member list
- [ ] Invite member (verify email sends after blocker fix)
- [ ] Change member role
- [ ] Remove member

---

## Phase 2: Settings & Invitations (Day 2)

### Task 2.1: Copy Settings Layout

**Copy from**: `taskforce_agent1/apps/sso/src/app/account/organizations/[orgId]/settings/`

Files:

- `layout.tsx` - Settings sidebar
- `page.tsx` - Redirect to general
- `loading.tsx`
- `error.tsx`

---

### Task 2.2: Copy General Settings Page

**Copy from**: `taskforce_agent1/apps/sso/src/app/account/organizations/[orgId]/settings/general/`

Files:

- `page.tsx`
- `components/GeneralSettingsForm.tsx`

---

### Task 2.3: Copy Accept Invitation Flow

**Copy from**: `taskforce_agent1/apps/sso/src/app/accept-invitation/`
**Copy to**: `agentfactory/apps/sso/src/app/accept-invitation/`

Files:

- `[invitationId]/page.tsx`
- `[invitationId]/components/AcceptInvitationCard.tsx`

---

### Task 2.4: Test Settings & Invitations

- [ ] Update org name
- [ ] Update org logo
- [ ] Navigate between settings tabs
- [ ] Accept invitation flow (end-to-end)

---

## Phase 3: Static Roles Setup (Day 3) - SIMPLE

**Note**: Using hardcoded roles in code. NO database changes.

### Task 3.0: Create Permissions File

**Create**: `apps/sso/src/lib/permissions.ts`

```typescript
import { createAccessControl } from "better-auth/plugins/access";
import { defaultStatements } from "better-auth/plugins/organization/access";

const statement = {
  ...defaultStatements,
  content: ["create", "read", "update", "delete"],
  courses: ["create", "read", "update", "delete", "publish"],
  billing: ["read", "update"],
} as const;

export const ac = createAccessControl(statement);

// Define your fixed roles
export const owner = ac.newRole({
  organization: ["update", "delete"],
  member: ["create", "update", "delete"],
  invitation: ["create", "cancel"],
  content: ["create", "read", "update", "delete"],
  courses: ["create", "read", "update", "delete", "publish"],
  billing: ["read", "update"],
});

export const admin = ac.newRole({
  organization: ["update"],
  member: ["create", "update", "delete"],
  invitation: ["create", "cancel"],
  content: ["create", "read", "update", "delete"],
  courses: ["create", "read", "update", "delete"],
  billing: ["read"],
});

export const manager = ac.newRole({
  member: ["create", "update"],
  invitation: ["create", "cancel"],
  content: ["create", "read", "update"],
  courses: ["read", "update"],
});

export const proctor = ac.newRole({
  content: ["read"],
  courses: ["read"],
  // Add assessment/exam permissions when needed
});

export const editor = ac.newRole({
  content: ["create", "read", "update"],
  courses: ["read", "update"],
});

export const member = ac.newRole({
  content: ["read"],
  courses: ["read"],
});

// Export role names for UI
export const ROLE_OPTIONS = ["owner", "admin", "manager", "proctor", "editor", "member"] as const;
export type RoleName = typeof ROLE_OPTIONS[number];
```

---

### Task 3.1: Update auth.ts with Custom Roles

**Update**: `apps/sso/src/lib/auth.ts`

```typescript
import { ac, owner, admin, editor, member } from "./permissions";

organization({
  ac,
  roles: { owner, admin, editor, member },
  // ... rest of existing config
})
```

---

### Task 3.2: Update auth-client.ts

**Update**: `apps/sso/src/lib/auth-client.ts`

```typescript
import { ac, owner, admin, editor, member } from "./permissions";

organizationClient({
  ac,
  roles: { owner, admin, editor, member },
})
```

---

### Task 3.3: Update RoleChangeDialog

**Update**: `src/app/account/organizations/[orgId]/settings/members/components/RoleChangeDialog.tsx`

Changes:
- Import `ROLE_OPTIONS` from permissions.ts
- Replace hardcoded ["owner", "admin", "member"] with `ROLE_OPTIONS`
- Shows all predefined roles in dropdown

---

## Phase 4: Danger Zone & Admin (Day 4)

### Task 4.1: Copy Danger Zone

**Copy from**: `taskforce_agent1/apps/sso/src/app/account/organizations/[orgId]/settings/danger/`

Files:

- `page.tsx`
- `components/TransferOwnershipSection.tsx`
- `components/DeleteOrgSection.tsx`

---

### Task 4.2: Copy Admin Org Dashboard ✅ CONFIRMED NEEDED

**Copy from**: `taskforce_agent1/apps/sso/src/app/admin/organizations/`

Files:

- `page.tsx`
- `components/AdminOrgTable.tsx`
- `components/BulkActionsBar.tsx`
- `components/OrgDetailsModal.tsx`

**Also add**:

- "Organizations" link in admin navbar

---

### Task 4.3: Add Org Switcher to Admin Header

**Copy from**: `taskforce_agent1/apps/sso/src/app/account/organizations/components/OrgSwitcher.tsx`

**Integrate into**: Admin layout header

**Purpose**: Quick org switching when admin is managing users/roles within orgs

---

### Task 4.4: Final Testing

- [ ] Transfer ownership
- [ ] Delete organization
- [ ] Admin org overview - view all orgs system-wide
- [ ] Admin org switcher in header works
- [ ] Admin can manage users/roles within any org
- [ ] Full end-to-end admin journey

---

## Dependencies

### UI Components (Verify Exist)

These Shadcn components should already exist in the SSO:

- [ ] `@/components/ui/dialog`
- [ ] `@/components/ui/button`
- [ ] `@/components/ui/input`
- [ ] `@/components/ui/badge`
- [ ] `@/components/ui/card`
- [ ] `@/components/ui/table`
- [ ] `@/components/ui/dropdown-menu`
- [ ] `@/components/ui/select`
- [ ] `@/components/ui/avatar`
- [ ] `@/components/ui/textarea`

### NPM Packages (Verify Exist)

- [ ] `date-fns` - Date formatting
- [ ] `zod` - Form validation
- [ ] `react-hook-form` - Form handling

---

## Success Criteria

### Phase 1 Complete When:

- User can list their organizations
- User can create organization
- User can switch active org
- Owner/Admin can manage members

### Phase 2 Complete When:

- Settings pages work
- Invitation emails send
- Accept invitation flow works

### Phase 3 Complete When:

- permissions.ts created with custom roles (owner, admin, editor, member)
- auth.ts updated with ac + roles config
- auth-client.ts updated with matching config
- RoleChangeDialog shows all predefined roles
- Admin can assign any predefined role to members
- NO database migration needed

### Phase 4 Complete When:

- Danger zone operations work (transfer ownership, delete org)
- Admin can view ALL orgs at `/admin/organizations`
- Admin org switcher in header works
- Admin can click into any org and manage its members/roles

---

## Rollback Plan

If issues arise:

1. All new files are in new directories (`/account/organizations/`, `/accept-invitation/`)
2. No existing files modified except:
   - `auth.ts` (invitation email callback)
   - `account/layout.tsx` (navigation link)
3. Easy to revert by deleting new directories and reverting 2 file changes
