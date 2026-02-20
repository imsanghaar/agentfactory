# SSO Monorepo Migration Summary

**Migration Date**: 2025-12-16
**Original Repository**: https://github.com/panaversity/sso
**Monorepo Location**: apps/sso/
**Migration Method**: git subtree (history preserved)

## Changes Made

### Imported
- Full SSO codebase with git history (accessible via `git blame -C -C`)
- Source code (src/, public/)
- Database schema (drizzle/)
- Tests (tests/)
- Configuration (.env.example)

### Deleted
- foundation/ (course content, not needed in monorepo)
- pnpm-lock.yaml (root lockfile governs)

### Added
- project.json (Nx targets: serve, build, lint)
- @nx/next plugin (Next.js support in Nx)

## Running SSO

### Development Server
```bash
pnpm nx serve sso
# Opens on http://localhost:3001
```

### Production Build
```bash
pnpm nx build sso
# Output: dist/apps/sso/
```

### Using package.json scripts (alternative)
```bash
pnpm nx run sso:dev   # Uses next dev directly
```

## Configuration Required

### Environment Variables (REQUIRED before running)

Copy `.env.example` to `.env.local` and configure:

```bash
cp apps/sso/.env.example apps/sso/.env.local
```

Required variables:
- `DATABASE_URL`: Neon PostgreSQL connection string
- `BETTER_AUTH_SECRET`: Auth encryption key (generate with `openssl rand -base64 32`)
- `BETTER_AUTH_URL`: http://localhost:3001 (dev)

### Database Setup

SSO uses Neon PostgreSQL. Run migrations:
```bash
cd apps/sso
pnpm db:push  # Push schema to database
```

## Files Requiring Human Review

The following files were preserved for human review:

| File | Action Required |
|------|----------------|
| `apps/sso/.claude/` | Review agents/skills, merge useful ones to root `.claude/` or delete |
| `apps/sso/.specify/` | Review templates, merge to root `.specify/` or delete |
| `apps/sso/CLAUDE.md` | Extract SSO-specific rules, merge to root `CLAUDE.md` or delete |
| `apps/sso/.mcp.json` | Review MCP server configs, merge to root `.mcp.json` or delete |
| `apps/sso/specs/` | Archive historical specs or merge to root `specs/` |
| `apps/sso/history/` | Archive PHRs or merge to root `history/` |

**Do NOT delete these files without review.** They contain project-specific intelligence.

## Success Criteria Status

- [x] SC-001: `pnpm nx serve sso` configured to start server on port 3001 (requires .env.local)
- [ ] SC-002: `pnpm nx build sso` (requires environment variables - see Configuration Required)
- [ ] SC-003: `pnpm nx lint sso` (requires ESLint setup - post-migration task)
- [x] SC-004: `git blame -C -C apps/sso/` shows original SSO commits
- [x] SC-005: `pnpm nx show projects` includes SSO project
- [x] SC-006: Affected detection works (SSO detected when files change)
- [x] SC-007: apps/sso/foundation/ deleted
- [x] SC-008: Root lockfile includes SSO dependencies

**Note**: SC-001, SC-002, SC-003 require environment configuration which is out of scope for the migration itself. These should be verified after configuring `.env.local`.

## Git History Access

The original SSO repository history is preserved. To view:

```bash
# View original commits
git log --oneline a09e7979f27594ba42c56e349d1e23f2091ccd12 | head -20

# View file history with blame
git blame -C -C apps/sso/package.json | head -10

# The -C -C flags enable copy detection to trace history across the subtree merge
```

## Next Steps

1. **Human review**: Address files in "Files Requiring Human Review" table
2. **Environment setup**: Create `apps/sso/.env.local` for local development
3. **ESLint setup**: Run `pnpm nx lint sso` and follow prompts to configure ESLint
4. **CI integration**: Update CI workflow to run SSO tests/builds
5. **Documentation**: Update root README.md to mention SSO app

## Nx Commands Reference

```bash
# Serve (development)
pnpm nx serve sso

# Build (production)
pnpm nx build sso

# Run any package.json script
pnpm nx run sso:<script-name>

# Check if SSO is affected by changes
pnpm nx affected -t build --dry-run

# Show SSO project configuration
pnpm nx show project sso
```
