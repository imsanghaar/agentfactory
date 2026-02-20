# Implementation Plan: SSO Monorepo Migration

**Feature**: 034-sso-monorepo-migration
**Created**: 2025-12-16
**Status**: Ready for Implementation
**Spec**: specs/034-sso-monorepo-migration/spec.md

---

## Overview

This plan details the step-by-step migration of the standalone SSO repository into the Nx monorepo using git subtree. The migration preserves git history, integrates with Nx build tooling, and leaves conflicting dot files for human review.

**Total Estimated Time**: 2-3 hours
**Risk Level**: Medium (git subtree complexity, dependency conflicts)

---

## Phase 0: Pre-Migration Verification

**Goal**: Ensure clean state and verify prerequisites before migration.

### Step 0.1: Verify Git State

```bash
# Ensure working directory is clean
git status

# Expected: "nothing to commit, working tree clean"
# If dirty: commit or stash changes before proceeding
```

### Step 0.2: Verify Monorepo Structure

```bash
# Check current apps directory
ls -la apps/

# Expected: learn-app/ should exist
# Verify pnpm workspace configuration
cat pnpm-workspace.yaml

# Expected: packages should include 'apps/*'
```

### Step 0.3: Verify Nx Installation

```bash
# Check Nx is installed
pnpm nx --version

# Expected: Nx version 20.x or higher
# Check existing Nx plugins
pnpm nx list

# Expected: Should show installed plugins
```

### Step 0.4: Document Current State

```bash
# Capture current dependency count for comparison
cat pnpm-lock.yaml | wc -l > /tmp/pre-migration-lockfile-lines.txt

# List current Nx projects
pnpm nx show projects > /tmp/pre-migration-projects.txt
```

**Verification**: ✅ Git clean, ✅ Nx installed, ✅ Baseline captured

---

## Phase 1: Git Subtree Import

**Goal**: Import SSO repository with full history into apps/sso/ using git subtree.

### Step 1.1: Add SSO Remote

```bash
# Add SSO repository as a git remote
git remote add sso-repo https://github.com/panaversity/sso.git

# Fetch SSO history
git fetch sso-repo main
```

**Expected Output**: Fetches all branches and tags from SSO repository.

### Step 1.2: Execute Git Subtree Merge

```bash
# Import SSO repository into apps/sso/ prefix
git subtree add --prefix=apps/sso sso-repo main --squash=false

# Note: --squash=false preserves full commit history
# This creates a merge commit that brings in SSO's main branch
```

**Expected Output**:
- Merge commit created with message like "Merge commit '...' as 'apps/sso'"
- All SSO files now present in apps/sso/

**Potential Issues**:
- If merge conflicts occur → abort with `git merge --abort`, investigate conflicts
- If fetch fails → verify network access and repository URL

### Step 1.3: Verify Import Success

```bash
# Check apps/sso directory exists
ls -la apps/sso/

# Expected: src/, public/, package.json, next.config.ts, drizzle/, tests/, etc.

# Verify git history preservation
git log --oneline apps/sso/ | head -20

# Expected: Shows commits from original SSO repository with original authors

# Verify specific file history
git log --follow apps/sso/package.json

# Expected: Shows full history including original SSO commits
```

### Step 1.4: Remove SSO Remote (Cleanup)

```bash
# Remove temporary remote to keep repo clean
git remote remove sso-repo
```

**Verification**: ✅ apps/sso/ exists, ✅ History preserved, ✅ FR-001 satisfied

---

## Phase 2: Post-Import Cleanup

**Goal**: Delete unnecessary files and folders per spec requirements.

### Step 2.1: Delete foundation/ Directory

```bash
# Remove course content folder (not needed in monorepo)
rm -rf apps/sso/foundation/

# Verify deletion
ls -la apps/sso/ | grep foundation

# Expected: No output (directory gone)
```

**Requirement**: FR-002 (Delete foundation/ directory)
**Success Criterion**: SC-007 (foundation/ does not exist)

### Step 2.2: Delete Standalone Lockfile

```bash
# Remove SSO's standalone pnpm-lock.yaml (root lockfile will govern)
rm -f apps/sso/pnpm-lock.yaml

# Verify deletion
ls -la apps/sso/ | grep pnpm-lock.yaml

# Expected: No output (file gone)
```

**Requirement**: FR-006 (Delete standalone lockfile)

### Step 2.3: Preserve Important Files

```bash
# Verify these files are PRESERVED (do NOT delete):
ls -la apps/sso/.env.example    # FR-007
ls -la apps/sso/drizzle/         # FR-008
ls -la apps/sso/tests/           # FR-009
ls -la apps/sso/.claude/         # FR-010 (preserved for human review)
ls -la apps/sso/.specify/        # FR-010
ls -la apps/sso/CLAUDE.md        # FR-010

# All should exist
```

### Step 2.4: Stage Cleanup Changes

```bash
# Stage all deletions
git add apps/sso/

# Create commit for cleanup phase
git commit -m "chore(sso): remove foundation/ and standalone lockfile after subtree import

- Delete apps/sso/foundation/ (course content, not needed)
- Delete apps/sso/pnpm-lock.yaml (root lockfile governs monorepo)
- Preserve .env.example, drizzle/, tests/ for future use
- Leave .claude/, .specify/, CLAUDE.md for human review

Refs: FR-002, FR-006, FR-007, FR-008, FR-009, FR-010"
```

**Verification**: ✅ foundation/ deleted, ✅ Lockfile deleted, ✅ Critical files preserved

---

## Phase 3: Nx Integration

**Goal**: Add @nx/next plugin and configure SSO as an Nx project.

### Step 3.1: Install @nx/next Plugin

```bash
# Add @nx/next plugin to support Next.js projects in Nx
pnpm add -D @nx/next

# Verify installation
pnpm nx list | grep @nx/next

# Expected: @nx/next appears in installed plugins list
```

**Requirement**: FR-003 (Add @nx/next plugin)

### Step 3.2: Create project.json for SSO

Create `apps/sso/project.json`:

```json
{
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "name": "sso",
  "sourceRoot": "apps/sso/src",
  "projectType": "application",
  "tags": ["type:app", "scope:platform", "runtime:node"],
  "targets": {
    "serve": {
      "executor": "@nx/next:server",
      "defaultConfiguration": "development",
      "options": {
        "buildTarget": "sso:build",
        "dev": true,
        "port": 3001
      },
      "configurations": {
        "development": {
          "buildTarget": "sso:build:development",
          "dev": true
        },
        "production": {
          "buildTarget": "sso:build:production",
          "dev": false
        }
      }
    },
    "build": {
      "executor": "@nx/next:build",
      "outputs": ["{options.outputPath}"],
      "defaultConfiguration": "production",
      "options": {
        "outputPath": "dist/apps/sso"
      },
      "configurations": {
        "development": {
          "outputPath": "apps/sso/.next"
        },
        "production": {
          "outputPath": "dist/apps/sso"
        }
      }
    },
    "lint": {
      "executor": "@nx/eslint:lint",
      "outputs": ["{options.outputFile}"],
      "options": {
        "lintFilePatterns": ["apps/sso/**/*.{ts,tsx,js,jsx}"]
      }
    },
    "test": {
      "executor": "@nx/jest:jest",
      "outputs": ["{workspaceRoot}/coverage/{projectRoot}"],
      "options": {
        "jestConfig": "apps/sso/jest.config.ts",
        "passWithNoTests": true
      },
      "configurations": {
        "ci": {
          "ci": true,
          "codeCoverage": true
        }
      }
    }
  }
}
```

**Key Configuration Decisions**:
- **Port 3001**: Constraint C-001 (different from learn-app's 3000)
- **Tags**: `type:app`, `scope:platform`, `runtime:node` for graph organization
- **Executors**: @nx/next for serve/build, @nx/eslint for lint, @nx/jest for test
- **Development config**: Uses apps/sso/.next for faster iteration
- **Production config**: Outputs to dist/apps/sso for deployment

### Step 3.3: Create/Update ESLint Configuration

Check if `apps/sso/.eslintrc.json` exists:

```bash
ls -la apps/sso/.eslintrc.json
```

**If missing**, create `apps/sso/.eslintrc.json`:

```json
{
  "extends": ["../../.eslintrc.json"],
  "ignorePatterns": ["!**/*", ".next/**/*"],
  "overrides": [
    {
      "files": ["*.ts", "*.tsx", "*.js", "*.jsx"],
      "rules": {}
    },
    {
      "files": ["*.ts", "*.tsx"],
      "rules": {}
    },
    {
      "files": ["*.js", "*.jsx"],
      "rules": {}
    }
  ]
}
```

**If exists**, verify it extends root ESLint config. If not, update the `extends` field to include `"../../.eslintrc.json"`.

### Step 3.4: Create Jest Configuration (If Tests Exist)

Check if `apps/sso/tests/` uses Jest:

```bash
ls apps/sso/tests/
cat apps/sso/package.json | grep jest
```

**If Jest detected**, create `apps/sso/jest.config.ts`:

```typescript
/* eslint-disable */
export default {
  displayName: 'sso',
  preset: '../../jest.preset.js',
  testEnvironment: 'node',
  transform: {
    '^.+\\.[tj]s$': ['ts-jest', { tsconfig: '<rootDir>/tsconfig.spec.json' }],
  },
  moduleFileExtensions: ['ts', 'js', 'html'],
  coverageDirectory: '../../coverage/apps/sso',
  testMatch: ['**/tests/**/*.test.ts', '**/tests/**/*.spec.ts'],
};
```

**If no Jest detected**, skip this file (tests may use different framework).

### Step 3.5: Verify pnpm Workspace Includes SSO

```bash
# Check pnpm-workspace.yaml includes apps/*
cat pnpm-workspace.yaml | grep "apps/\*"

# Expected: packages should include 'apps/*' (already covers apps/sso/)
```

**If `apps/*` not found**, add it:

```yaml
packages:
  - 'apps/*'
  - 'libs/*'
```

**Requirement**: FR-005 (Update pnpm-workspace.yaml if needed)

### Step 3.6: Stage Nx Integration Changes

```bash
# Stage new Nx configuration files
git add apps/sso/project.json
git add apps/sso/.eslintrc.json  # If created
git add apps/sso/jest.config.ts  # If created
git add package.json              # For @nx/next plugin
git add pnpm-lock.yaml           # Updated with @nx/next

# Commit Nx integration
git commit -m "feat(sso): integrate SSO as Nx project with @nx/next plugin

- Add @nx/next plugin for Next.js support
- Create apps/sso/project.json with serve, build, lint, test targets
- Configure SSO to run on port 3001 (different from learn-app)
- Add ESLint and Jest configurations extending monorepo standards

Refs: FR-003, FR-004, C-001"
```

**Verification**: ✅ project.json created, ✅ @nx/next installed, ✅ FR-003, FR-004 satisfied

---

## Phase 4: Dependency Resolution

**Goal**: Merge SSO dependencies into root lockfile and resolve conflicts.

### Step 4.1: Install All Dependencies

```bash
# Run pnpm install to merge SSO deps into root lockfile
pnpm install

# This will:
# 1. Read apps/sso/package.json
# 2. Merge dependencies into root pnpm-lock.yaml
# 3. Hoist shared deps to root node_modules/
# 4. Install SSO-specific deps in apps/sso/node_modules/
```

**Expected Output**:
- "Lockfile is up to date, resolution step is skipped" OR
- "Packages: +X" (new packages installed)
- No errors about version conflicts

**Potential Issues**:
- **Peer dependency warnings**: Document for later review, not blocking
- **Version conflicts**: If critical deps conflict, may need to align versions
- **Missing deps**: Verify SSO's package.json lists all required deps

### Step 4.2: Verify Dependency Installation

```bash
# Check SSO's dependencies are in lockfile
cat pnpm-lock.yaml | grep -A 5 "apps/sso"

# Expected: apps/sso listed as importer with its dependencies

# Verify SSO's node_modules (if any local deps)
ls -la apps/sso/node_modules/ || echo "No local node_modules (hoisted to root)"
```

### Step 4.3: Document Dependency Changes

```bash
# Compare lockfile size before/after
cat pnpm-lock.yaml | wc -l
cat /tmp/pre-migration-lockfile-lines.txt

# Calculate added dependencies
# Document in commit message
```

### Step 4.4: Stage Dependency Changes

```bash
# Stage updated lockfile and package.json (if root deps added)
git add pnpm-lock.yaml
git add package.json  # Only if root deps changed

# Commit dependency resolution
git commit -m "chore(deps): merge SSO dependencies into monorepo lockfile

- SSO dependencies now managed by root pnpm-lock.yaml
- Hoisted shared deps (Next.js, React, etc.) to reduce duplication
- SSO-specific deps (Drizzle, Auth libs) installed locally

Lockfile size: [X lines added]

Refs: FR-006, SC-008"
```

**Verification**: ✅ pnpm install succeeds, ✅ SC-008 satisfied (root lockfile includes SSO deps)

---

## Phase 5: Verification & Testing

**Goal**: Verify all success criteria (SC-001 through SC-008) are met.

### Step 5.1: Verify Nx Project Detection

```bash
# SC-005: Check SSO appears in Nx project graph
pnpm nx show projects | grep sso

# Expected: "sso" in project list

# Visualize project graph (optional)
pnpm nx graph

# Expected: SSO node visible, connected to any shared libs (if applicable)
```

**Success Criterion**: SC-005 ✅

### Step 5.2: Verify Serve Target

```bash
# SC-001: Start SSO development server
pnpm nx serve sso

# Expected:
# - Server starts within 30 seconds
# - Listening on http://localhost:3001
# - No fatal errors (warnings acceptable)

# Manual test: Open http://localhost:3001 in browser
# Expected: SSO login or admin interface loads

# Stop server: Ctrl+C
```

**Success Criterion**: SC-001 ✅

**If server fails to start**:
1. Check `.env.example` → create `apps/sso/.env` with required vars
2. Check database connection (Neon PostgreSQL URL required)
3. Check port 3001 not already in use: `lsof -i :3001`

### Step 5.3: Verify Build Target

```bash
# SC-002: Build SSO for production
pnpm nx build sso

# Expected:
# - Build completes without errors
# - Output in dist/apps/sso/ or apps/sso/.next/ (depending on config)
# - Success message: "Successfully ran target build for project sso"

# Verify build output
ls -la dist/apps/sso/.next/

# Expected: Static files, server chunks, build manifest
```

**Success Criterion**: SC-002 ✅

### Step 5.4: Verify Lint Target

```bash
# SC-003: Run ESLint on SSO
pnpm nx lint sso

# Expected:
# - Lint runs without configuration errors
# - May report style/code issues (acceptable for initial migration)
# - No "ESLint config not found" errors

# Check lint output
# If many errors: Document for follow-up, not blocking migration
```

**Success Criterion**: SC-003 ✅

### Step 5.5: Verify Git History Preservation

```bash
# SC-004: Check git history for SSO files
git log --oneline apps/sso/ | head -20

# Expected: Commits from original SSO repository visible

# Check specific file history
git log --follow apps/sso/src/app/page.tsx | head -10

# Expected: Shows original SSO commits with authors

# Check git blame works
git blame apps/sso/package.json | head -10

# Expected: Shows original authors from SSO repo
```

**Success Criterion**: SC-004 ✅

### Step 5.6: Verify Affected Detection (CI Simulation)

```bash
# SC-006: Simulate PR with SSO changes
# Create a test change to trigger affected detection
echo "// test comment" >> apps/sso/src/app/page.tsx

# Check affected projects
pnpm nx affected --target=build --dry-run

# Expected:
# - SSO appears in affected projects list
# - learn-app NOT affected (unless it depends on SSO)

# Revert test change
git restore apps/sso/src/app/page.tsx
```

**Success Criterion**: SC-006 ✅

### Step 5.7: Verify Cleanup Completeness

```bash
# SC-007: Confirm foundation/ deleted
ls -la apps/sso/ | grep foundation

# Expected: No output (directory gone)

# SC-008: Confirm no standalone lockfile
ls -la apps/sso/ | grep pnpm-lock.yaml

# Expected: No output (file deleted)

# Confirm root lockfile includes SSO
cat pnpm-lock.yaml | grep -A 3 "apps/sso"

# Expected: SSO listed as importer
```

**Success Criteria**: SC-007 ✅, SC-008 ✅

### Step 5.8: Verify Preserved Files

```bash
# FR-007: .env.example preserved
ls -la apps/sso/.env.example

# FR-008: drizzle/ preserved
ls -la apps/sso/drizzle/

# FR-009: tests/ preserved
ls -la apps/sso/tests/

# FR-010: Dot files preserved for review
ls -la apps/sso/.claude/
ls -la apps/sso/.specify/
ls -la apps/sso/CLAUDE.md
```

**All should exist** ✅

---

## Phase 6: Documentation & Human Review Setup

**Goal**: Document migration results and flag conflicting files for human review.

### Step 6.1: Create Migration Summary

Create `apps/sso/MIGRATION.md`:

```markdown
# SSO Monorepo Migration Summary

**Migration Date**: 2025-12-16
**Original Repository**: https://github.com/panaversity/sso
**Monorepo Location**: apps/sso/
**Migration Method**: git subtree (history preserved)

## Changes Made

### Imported
- ✅ Full SSO codebase with git history
- ✅ Source code (src/, public/)
- ✅ Database schema (drizzle/)
- ✅ Tests (tests/)
- ✅ Configuration (.env.example)

### Deleted
- ❌ foundation/ (course content, not needed)
- ❌ pnpm-lock.yaml (root lockfile governs)

### Added
- ✅ project.json (Nx targets: serve, build, lint, test)
- ✅ @nx/next plugin (Next.js support)
- ✅ ESLint config (extends monorepo standards)

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

### Linting
```bash
pnpm nx lint sso
```

## Configuration Required

### Environment Variables
Copy `.env.example` to `.env` and configure:
- `DATABASE_URL`: Neon PostgreSQL connection string
- `NEXTAUTH_SECRET`: Auth encryption key
- Other SSO-specific vars per .env.example

### Database Setup
SSO uses Neon PostgreSQL. Run migrations:
```bash
cd apps/sso
pnpm drizzle-kit push:pg  # Or equivalent migration command
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

## Success Criteria Met

- ✅ SC-001: `pnpm nx serve sso` starts server on port 3001
- ✅ SC-002: `pnpm nx build sso` produces production build
- ✅ SC-003: `pnpm nx lint sso` runs without config errors
- ✅ SC-004: `git log apps/sso/` shows original SSO commits
- ✅ SC-005: `pnpm nx graph` includes SSO project
- ✅ SC-006: Affected detection works for SSO changes
- ✅ SC-007: apps/sso/foundation/ deleted
- ✅ SC-008: Root lockfile includes SSO dependencies

## Next Steps

1. **Human review**: Address files in "Files Requiring Human Review" table
2. **Environment setup**: Create `apps/sso/.env` for local development
3. **CI integration**: Update CI workflow to run SSO tests/builds
4. **Documentation**: Update root README.md to mention SSO app
5. **Deployment**: Configure SSO deployment pipeline (if needed)
```

### Step 6.2: Stage Migration Documentation

```bash
# Add migration summary
git add apps/sso/MIGRATION.md

# Commit documentation
git commit -m "docs(sso): add migration summary and human review checklist

- Document migration process and results
- List files requiring human review
- Provide setup instructions for SSO in monorepo
- Confirm all success criteria met (SC-001 through SC-008)

Refs: FR-010"
```

### Step 6.3: Update Root README (Optional)

If root `README.md` exists, add SSO to the apps section:

```markdown
## Applications

- **learn-app** (`apps/learn-app/`): Student learning platform
- **sso** (`apps/sso/`): Single Sign-On authentication server (port 3001)
```

```bash
git add README.md
git commit -m "docs: add SSO app to root README"
```

---

## Phase 7: Final Verification & Completion

### Step 7.1: Run Full Monorepo Tests

```bash
# Ensure existing projects still work
pnpm nx run-many -t build

# Expected: All projects build successfully (learn-app, sso, etc.)

# Run affected tests
pnpm nx affected -t test

# Expected: Tests pass (or skip if no tests configured)
```

**Requirement**: NFR-002 (Migration must not break existing projects)

### Step 7.2: Verify Independent SSO Workflows

```bash
# Test SSO serve target
pnpm nx serve sso &
sleep 10
curl http://localhost:3001 | head
pkill -f "nx serve sso"

# Expected: HTTP 200 or redirect to login page

# Test SSO build target
pnpm nx build sso

# Expected: Build succeeds

# Test SSO lint target
pnpm nx lint sso

# Expected: Lint runs (issues may exist, config errors should not)
```

**Requirement**: NFR-003 (SSO runnable via pnpm nx serve sso)

### Step 7.3: Create Final Migration Commit Summary

```bash
# Review all migration commits
git log --oneline --grep="sso" | head -20

# Expected commits:
# 1. "Merge commit '...' as 'apps/sso'" (subtree import)
# 2. "chore(sso): remove foundation/ and standalone lockfile"
# 3. "feat(sso): integrate SSO as Nx project"
# 4. "chore(deps): merge SSO dependencies"
# 5. "docs(sso): add migration summary"

# Tag migration completion (optional)
git tag sso-migration-complete

# Push to feature branch
git push origin 034-sso-monorepo-migration
git push origin --tags  # If using tag
```

### Step 7.4: Success Criteria Final Check

Run this verification script:

```bash
#!/bin/bash
# verify-sso-migration.sh

echo "=== SSO Migration Verification ==="
echo ""

echo "SC-001: SSO serve target"
pnpm nx serve sso --port 3001 > /tmp/sso-serve.log 2>&1 &
sleep 15
curl -s http://localhost:3001 > /dev/null && echo "✅ Server accessible" || echo "❌ Server not accessible"
pkill -f "nx serve sso"

echo ""
echo "SC-002: SSO build target"
pnpm nx build sso > /dev/null 2>&1 && echo "✅ Build succeeds" || echo "❌ Build fails"

echo ""
echo "SC-003: SSO lint target"
pnpm nx lint sso > /dev/null 2>&1 && echo "✅ Lint configured" || echo "⚠️  Lint issues (acceptable)"

echo ""
echo "SC-004: Git history preserved"
git log --oneline apps/sso/ | head -1 | grep -q "." && echo "✅ History exists" || echo "❌ No history"

echo ""
echo "SC-005: Nx project graph includes SSO"
pnpm nx show projects | grep -q "sso" && echo "✅ SSO in graph" || echo "❌ SSO not in graph"

echo ""
echo "SC-006: Affected detection"
echo "// test" >> apps/sso/src/app/page.tsx
pnpm nx affected --target=build --dry-run 2>&1 | grep -q "sso" && echo "✅ Affected works" || echo "❌ Affected broken"
git restore apps/sso/src/app/page.tsx

echo ""
echo "SC-007: foundation/ deleted"
[ ! -d "apps/sso/foundation" ] && echo "✅ foundation/ removed" || echo "❌ foundation/ still exists"

echo ""
echo "SC-008: Root lockfile includes SSO"
grep -q "apps/sso" pnpm-lock.yaml && echo "✅ SSO in lockfile" || echo "❌ SSO not in lockfile"

echo ""
echo "=== Verification Complete ==="
```

```bash
chmod +x verify-sso-migration.sh
./verify-sso-migration.sh
```

**Expected**: All ✅ (warnings acceptable for lint)

---

## Rollback Plan

If migration fails critically, rollback with these steps:

### Option 1: Revert Commits (Before Push)

```bash
# Find the commit before subtree import
git log --oneline | grep -B 1 "Merge commit.*apps/sso"

# Reset to commit before migration
git reset --hard <commit-sha-before-migration>

# Clean working directory
git clean -fd
```

### Option 2: Delete SSO and Revert Changes (After Push)

```bash
# Remove apps/sso directory
rm -rf apps/sso/

# Revert package.json changes (@nx/next)
git restore package.json
git restore pnpm-lock.yaml

# Reinstall deps
pnpm install

# Commit rollback
git add .
git commit -m "revert: rollback SSO migration due to [reason]"
```

---

## Post-Migration Tasks (Human Review)

After migration completes successfully, assign these tasks to a human reviewer:

### Task 1: Review Conflicting Files (Priority: P3)

**Location**: `apps/sso/MIGRATION.md` (Files Requiring Human Review section)

**Action**:
1. Compare `apps/sso/.claude/` with root `.claude/`
2. Identify unique agents/skills in SSO that should be merged
3. Delete redundant files or merge useful ones
4. Repeat for `.specify/`, `CLAUDE.md`, `.mcp.json`, `specs/`, `history/`

**Completion Criteria**: All conflicting files either merged or deleted

### Task 2: Configure SSO Environment (Priority: P1)

**Location**: `apps/sso/.env`

**Action**:
1. Copy `apps/sso/.env.example` to `apps/sso/.env`
2. Fill in `DATABASE_URL` (Neon PostgreSQL connection string)
3. Fill in `NEXTAUTH_SECRET` (generate with `openssl rand -base64 32`)
4. Fill in any other required environment variables
5. Test SSO locally: `pnpm nx serve sso`

**Completion Criteria**: SSO runs successfully on http://localhost:3001

### Task 3: Update CI Workflow (Priority: P2)

**Location**: `.github/workflows/ci.yml`

**Action**:
1. Ensure CI runs `nx affected -t lint test build` (should already include SSO)
2. Add SSO-specific environment variables to CI secrets (if needed)
3. Test CI on a PR with SSO changes

**Completion Criteria**: CI correctly builds/tests SSO when affected

### Task 4: Update Documentation (Priority: P3)

**Location**: Root `README.md`, `CONTRIBUTING.md`

**Action**:
1. Add SSO to applications list in README
2. Document SSO setup steps in CONTRIBUTING.md
3. Link to `apps/sso/MIGRATION.md` for migration details

**Completion Criteria**: New contributors can set up SSO from docs

---

## Risk Mitigation

### Risk 1: Git Subtree Conflicts

**Likelihood**: Low
**Impact**: High (blocks migration)

**Mitigation**:
- Ensure clean git state before starting (Phase 0)
- Use `--squash=false` to preserve history and avoid complex merge commits
- If conflicts occur, abort and investigate manually

**Recovery**: Rollback plan (delete apps/sso/, revert commits)

### Risk 2: Dependency Version Conflicts

**Likelihood**: Medium
**Impact**: Medium (may require version alignment)

**Mitigation**:
- Review SSO's package.json for known conflicting deps (Next.js, React versions)
- Use pnpm's overrides if critical deps conflict
- Document peer dependency warnings (not blocking)

**Recovery**: Pin specific versions in root package.json, use pnpm overrides

### Risk 3: Port Conflicts (3001 Already in Use)

**Likelihood**: Low
**Impact**: Low (easy workaround)

**Mitigation**:
- Document port requirement (3001) in MIGRATION.md
- Check `lsof -i :3001` before first serve

**Recovery**: Change port in project.json if conflict unavoidable

### Risk 4: Database Connection Failures

**Likelihood**: Medium
**Impact**: Medium (SSO won't start without DB)

**Mitigation**:
- Document `.env` setup as required step
- SSO's .env.example provides template
- Neon PostgreSQL URL required (not part of migration scope)

**Recovery**: Create .env with valid DATABASE_URL, test connection

---

## Estimated Timeline

| Phase | Estimated Time | Dependencies |
|-------|---------------|--------------|
| 0. Pre-Migration Verification | 15 min | Clean git state |
| 1. Git Subtree Import | 10 min | Network access to GitHub |
| 2. Post-Import Cleanup | 10 min | Phase 1 complete |
| 3. Nx Integration | 30 min | @nx/next plugin knowledge |
| 4. Dependency Resolution | 20 min | pnpm install |
| 5. Verification & Testing | 30 min | .env configured for serve test |
| 6. Documentation | 20 min | Migration results |
| 7. Final Verification | 15 min | All phases complete |
| **Total** | **~2.5 hours** | Assuming no major issues |

**Buffer for issues**: +1 hour (dependency conflicts, env setup)

---

## Success Metrics

**Migration is complete when**:
- ✅ All success criteria (SC-001 through SC-008) verified
- ✅ `pnpm nx serve sso` works on port 3001
- ✅ `pnpm nx build sso` produces production build
- ✅ Git history preserved (original SSO commits visible)
- ✅ foundation/ and standalone lockfile deleted
- ✅ Nx project graph includes SSO
- ✅ Conflicting files flagged for human review
- ✅ Migration documentation complete

**Human review tasks assigned** (not blocking migration completion):
- Review `.claude/`, `.specify/`, `CLAUDE.md` conflicts
- Configure `.env` for local development
- Update CI workflow for SSO tests
- Update root documentation

---

## Appendix: Commands Quick Reference

```bash
# Pre-Migration
git status                              # Verify clean state
pnpm nx --version                       # Check Nx installed

# Phase 1: Import
git remote add sso-repo https://github.com/panaversity/sso.git
git fetch sso-repo main
git subtree add --prefix=apps/sso sso-repo main --squash=false
git remote remove sso-repo

# Phase 2: Cleanup
rm -rf apps/sso/foundation/
rm -f apps/sso/pnpm-lock.yaml
git add apps/sso/
git commit -m "chore(sso): cleanup after subtree import"

# Phase 3: Nx Integration
pnpm add -D @nx/next
# Create apps/sso/project.json (see Phase 3.2)
git add apps/sso/project.json package.json pnpm-lock.yaml
git commit -m "feat(sso): integrate as Nx project"

# Phase 4: Dependencies
pnpm install
git add pnpm-lock.yaml
git commit -m "chore(deps): merge SSO dependencies"

# Phase 5: Verification
pnpm nx show projects | grep sso       # SC-005
pnpm nx serve sso                       # SC-001
pnpm nx build sso                       # SC-002
pnpm nx lint sso                        # SC-003
git log --oneline apps/sso/ | head -20  # SC-004

# Rollback (if needed)
git reset --hard <commit-before-migration>
git clean -fd
```

---

**Plan Status**: Ready for Implementation
**Next Step**: Execute Phase 0 (Pre-Migration Verification)
