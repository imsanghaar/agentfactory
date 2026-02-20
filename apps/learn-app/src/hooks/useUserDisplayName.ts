import { useMemo } from "react";
import { useAuth } from "../contexts/AuthContext";

/**
 * Extracts a display name from the authenticated user session.
 * Priority: full name > email username > defaultValue.
 */
export function useUserDisplayName(defaultValue?: string): string | undefined {
  const { session } = useAuth();

  return useMemo(() => {
    if (session?.user?.name) return session.user.name;
    if (session?.user?.email) return session.user.email.split("@")[0];
    return defaultValue;
  }, [session?.user?.name, session?.user?.email, defaultValue]);
}
