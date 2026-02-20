/**
 * Organization Access Control & Custom Roles
 *
 * Defines 7 roles with a hierarchy for the organization plugin.
 * Client-safe — no server secrets, importable from both auth.ts and auth-client.ts.
 *
 * Hierarchy:
 *   owner (7) > admin (6) > manager (5) > teacher/proctor (4) > editor (3) > member (2)
 */

import { createAccessControl } from "better-auth/plugins/access";
import {
  defaultStatements,
  adminAc,
  memberAc,
  ownerAc,
} from "better-auth/plugins/organization/access";

// ── Statements ──────────────────────────────────────────────────────────
// Extend Better Auth's default org/member/invitation statements with
// domain-specific resources.

const statement = {
  ...defaultStatements,
  content: ["read", "create", "update", "delete"],
  assessment: ["read", "create", "update", "grade"],
} as const;

export const ac = createAccessControl(statement);

// ── Roles ───────────────────────────────────────────────────────────────

export const owner = ac.newRole({
  ...ownerAc.statements,
  content: ["read", "create", "update", "delete"],
  assessment: ["read", "create", "update", "grade"],
});

export const admin = ac.newRole({
  ...adminAc.statements,
  content: ["read", "create", "update", "delete"],
  assessment: ["read", "create", "update", "grade"],
});

export const manager = ac.newRole({
  ...adminAc.statements,
  content: ["read"],
  assessment: ["read"],
});

export const teacher = ac.newRole({
  content: ["read"],
  assessment: ["read"],
});

export const proctor = ac.newRole({
  content: ["read"],
  assessment: ["read", "create", "update", "grade"],
});

export const editor = ac.newRole({
  content: ["read", "create", "update", "delete"],
  assessment: ["read"],
});

export const member = ac.newRole({
  ...memberAc.statements,
  content: ["read"],
  assessment: ["read"],
});
