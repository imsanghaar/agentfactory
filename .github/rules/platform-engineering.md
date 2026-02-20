---
paths:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.py"
  - "**/*.js"
  - "**/*.jsx"
---

# Platform Engineering Protocol (Code Work)

**Before implementing ANY feature, complete this research protocol:**

## 1. Research Existing Solutions (MANDATORY)

```
WebSearch: "[framework] [feature] plugin/library 2025"
Examples:
- "Docusaurus copy markdown plugin" → Found docusaurus-plugin-copy-page-button
- "React clipboard API best practices" → Found navigator.clipboard limitations
```

**Why**: Avoids reinventing wheels. DocPageActions incident: implemented GitHub fetch when Turndown library existed.

## 2. Edge Case Brainstorm (MANDATORY)

Before writing code, list potential failures:

| Category            | Questions to Ask                                               |
| ------------------- | -------------------------------------------------------------- |
| **Rate Limits**     | Does this call external APIs? What are the limits?             |
| **Permissions**     | Does this need user gestures? (clipboard, notifications, etc.) |
| **Browser Compat**  | Safari? Mobile? Offline?                                       |
| **Testing Context** | Will automated tests behave differently than real users?       |
| **Error States**    | What if network fails? API changes? User cancels?              |
| **Performance**     | On slow connections? Large files? Many concurrent users?       |

**Why**: DocPageActions incident: clipboard API fails without document focus (browser automation limitation).

## 3. Validate Approach with User

Before deep implementation:

- Present 2-3 approaches with trade-offs
- Get user sign-off on direction
- Saves iteration cycles

## 4. Implementation Checklist

```
□ Searched for existing plugins/libraries
□ Listed 5+ edge cases and mitigations
□ Confirmed approach handles: offline, mobile, accessibility
□ Added error handling with user-friendly messages
□ Tested in both dev and production-like environments
```

## Quick Reference: Common Gotchas

| API/Feature         | Gotcha                    | Solution                              |
| ------------------- | ------------------------- | ------------------------------------- |
| Clipboard API       | Requires document focus   | Real user click, not JS `.click()`    |
| GitHub Raw URLs     | 60 req/hr unauthenticated | Use client-side extraction (Turndown) |
| fetch() to external | CORS, rate limits         | Proxy or client-side alternative      |
| localStorage        | 5MB limit, sync           | Consider IndexedDB for large data     |
| Service Workers     | Complex lifecycle         | Test registration/updates carefully   |

## LIVE VERIFICATION PROTOCOL (MANDATORY before commits to main)

**⚠️ NEVER commit to main branch without live verification:**

1. **Start the services yourself** (don't assume user is running them)
2. **Make a real request** through UI or API
3. **Verify full flow** works end-to-end
4. **Check logs** for errors or warnings
5. **Only then** commit and push

**Project service commands:**

```bash
pnpm nx serve learn-app        # Frontend (port 3000)
pnpm nx serve study-mode-api   # Study Mode API (port 8000)
pnpm nx serve sso              # Auth service
```

**Verification workflow:**

```bash
# 1. Start backend in background
pnpm nx serve study-mode-api &

# 2. Wait for startup, check logs
sleep 5 && curl http://localhost:8000/health

# 3. Test the actual feature you changed
# 4. Check logs for errors
# 5. Only then commit
```

**High-risk changes requiring extra verification:**

- Import statements (module paths differ between environments)
- API/SDK features (docs may not match installed version)
- Startup/initialization code
- Database migrations
- Environment-dependent configuration
