# PHR-007-001: Secure Cookie Prefix Logout Fix

## Metadata
- **ID**: PHR-007-001
- **Date**: 2025-12-06
- **Stage**: green (bug fix)
- **Feature**: OIDC RP-Initiated Logout
- **Tags**: better-auth, cookies, security, oidc, logout

## Prompt (Summary)

Bug: `/api/auth/oauth2/endsession` not clearing SSO session. Users could log out from client apps but remain logged in at the SSO server. The fix required multiple iterations to identify the root cause.

## Response (Summary)

Fixed the endsession endpoint to properly clear cookies in production. The issue had two layers:

1. **First layer**: The original code called `auth.api.signOut()` but didn't capture the Set-Cookie headers from the response. Fixed by using `response.cookies.set()` directly.

2. **Second layer (root cause)**: Better Auth uses `__Secure-` prefix for cookies in production when `secure: true`. We were clearing `robolearn.session_token` but production uses `__Secure-robolearn.session_token`.

## Key Learnings

### 1. Better Auth Cookie Naming in Production

When Better Auth runs with secure cookies enabled (production), it prepends `__Secure-` to all cookie names:

| Environment | Cookie Name |
|-------------|-------------|
| Development | `{prefix}.session_token` |
| Production | `__Secure-{prefix}.session_token` |

**Implication**: Any custom logout logic must clear BOTH variants.

### 2. Debugging Cookie Issues

When debugging cookie-clearing issues:
1. Check browser DevTools → Application → Cookies for **actual cookie names**
2. Don't assume cookie names from code - production may differ
3. The `__Secure-` prefix is a browser security feature for HTTPS-only cookies

### 3. Better Auth Cookie Structure

Better Auth creates these cookies:
- `{prefix}.session_token` - The main session token
- `{prefix}.session_data` - Cached session data (may be chunked: `.0`, `.1`, etc.)
- `{prefix}.dont_remember` - Remember-me preference

## Code Pattern (Reusable Intelligence)

```typescript
// Cookie prefix from auth config
const AUTH_COOKIE_PREFIX = "robolearn";

// Base cookie names
const BASE_COOKIE_NAMES = [
  `${AUTH_COOKIE_PREFIX}.session_token`,
  `${AUTH_COOKIE_PREFIX}.session_data`,
  `${AUTH_COOKIE_PREFIX}.dont_remember`,
];

// Production uses __Secure- prefix
const SECURE_PREFIX = "__Secure-";

// Get all cookie variants to clear
function getSessionCookieNames(): string[] {
  const names: string[] = [];
  for (const name of BASE_COOKIE_NAMES) {
    names.push(name); // Development
    names.push(`${SECURE_PREFIX}${name}`); // Production
  }
  return names;
}

// Clear cookies on response
const cookieClearOptions = {
  expires: new Date(0),
  maxAge: 0,
  path: "/",
  httpOnly: true,
  secure: process.env.NODE_ENV === "production",
  sameSite: "lax" as const,
};

for (const name of getSessionCookieNames()) {
  response.cookies.set(name, "", cookieClearOptions);
}
```

## Related Files

- `src/app/api/auth/oauth2/endsession/route.ts` - The fixed endpoint
- `src/lib/auth.ts` - AUTH_COOKIE_PREFIX definition

## Commits

- `90cf7f0` - fix: ensure endsession properly clears SSO session cookies
- `347edec` - fix: clear __Secure- prefixed cookies in production logout

## Future Considerations

1. Consider adding integration test that verifies cookie headers include `__Secure-` prefix in production mode
2. Document this behavior in troubleshooting guide
3. Consider making cookie prefix configurable via environment variable for multi-tenant deployments
