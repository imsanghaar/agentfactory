/**
 * Organization Types
 * TypeScript interfaces for Better Auth Organizations
 */

// All predefined roles (matches permissions.ts)
export type OrgRole =
  | "owner"
  | "admin"
  | "manager"
  | "teacher"
  | "proctor"
  | "editor"
  | "member";

export interface Organization {
  id: string;
  name: string;
  slug: string;
  logo?: string | null;
  metadata?: string | null;
  createdAt: Date;
}

export interface Member {
  id: string;
  organizationId: string;
  userId: string;
  role: OrgRole;
  createdAt: Date;
  user?: {
    id: string;
    name: string;
    email: string;
    image?: string | null;
  };
}

export interface Invitation {
  id: string;
  organizationId: string;
  email: string;
  role?: OrgRole | null;
  status: "pending" | "accepted" | "rejected" | "expired";
  expiresAt: Date;
  inviterId: string;
  createdAt: Date;
  inviter?: {
    id: string;
    name: string;
    email: string;
  };
  organization?: Organization;
}

export interface OrganizationWithDetails extends Organization {
  memberCount: number;
  userRole?: OrgRole;
  isActive: boolean;
}
