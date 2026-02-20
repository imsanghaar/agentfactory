import { createAuthClient } from "better-auth/react";
import { oidcClient } from "better-auth/client/plugins";
import { adminClient } from "better-auth/client/plugins";
import { organizationClient } from "better-auth/client/plugins";
import { usernameClient } from "better-auth/client/plugins";
import { apiKeyClient } from "better-auth/client/plugins";
import { inferAdditionalFields } from "better-auth/client/plugins";
import type { auth } from "./auth";
import {
  ac,
  owner as ownerRole,
  admin as adminRole,
  manager as managerRole,
  teacher as teacherRole,
  proctor as proctorRole,
  editor as editorRole,
  member as memberRole,
} from "./permissions";

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || "http://localhost:3001",
  plugins: [
    inferAdditionalFields<typeof auth>(), // Infer custom fields from server
    oidcClient(),
    adminClient(),
    organizationClient({
      ac,
      roles: {
        owner: ownerRole,
        admin: adminRole,
        manager: managerRole,
        teacher: teacherRole,
        proctor: proctorRole,
        editor: editorRole,
        member: memberRole,
      },
    }),
    usernameClient(), // Matches server's username() plugin for profile usernames
    apiKeyClient(), // M2M authentication - API key management
  ],
});

export const {
  signIn,
  signUp,
  signOut,
  useSession,
  getSession,
  // Password reset methods
  requestPasswordReset,
  resetPassword,
  // Email verification
  sendVerificationEmail,
  // OIDC methods
  oauth2,
  // Admin methods
  admin,
  // Organization methods
  organization,
  useActiveOrganization,
} = authClient;
