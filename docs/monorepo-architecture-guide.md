# Monorepo Architecture Guide
## Setup, Thinking, Team Management, Task Delegation & Edge Cases

**Version**: 1.0.0
**Status**: Draft - Starting Point for Discussion
**Last Updated**: 2025-12-14

---

## Table of Contents

1. [Mental Models](#part-1-mental-models)
2. [Setup Process](#part-2-setup)
3. [Dependency Management](#part-3-dependency-management)
4. [Team Management & Ownership](#part-4-team-management--ownership)
5. [Daily Workflows](#part-5-working-on-tasks)
6. [CI/CD Configuration](#part-6-cicd)
7. [AI Agent Delegation](#part-7-delegating-to-ai-agents)
8. [Edge Cases & Pitfalls](#part-8-edge-cases--pitfalls)
9. [Tooling Decisions](#part-9-tooling-decision-matrix)
10. [Checklists](#part-10-checklists)
11. [AI Skills for Monorepo Work](#part-11-ai-skills-for-monorepo-work)

---

## Part 1: Mental Models

### 1.1 The Fundamental Insight

A monorepo is **not** just "putting code in one folder." It's a **coordination mechanism** that changes how work flows through teams.

```
Polyrepo Mental Model:
  "Each project is an island. Coordinate via published packages."

Monorepo Mental Model:
  "All projects are one system. Changes are atomic across boundaries."
```

### 1.2 The Three Laws of Monorepos

| Law | Principle | Violation Consequence |
|-----|-----------|----------------------|
| **1. Atomic Changes** | Cross-project changes happen in ONE commit | Version drift, integration hell |
| **2. Unified Tooling** | One build system, one CI, one way | Fragmentation, tribal knowledge |
| **3. Clear Ownership** | Every file has exactly one owner | Tragedy of the commons |

### 1.3 Conway's Law Awareness

> "Organizations design systems that mirror their communication structure."

**Critical insight**: Hard team coupling is more dangerous than software coupling. Until you need to split ownership between team boundaries, things creak.

```
✅ Team structure matches code structure:
   Team A owns /apps/sso/
   Team B owns /apps/docs/

❌ Code structure ignores team boundaries:
   Everyone touches /packages/shared/
   No one owns /packages/legacy/
```

### 1.4 Scale Determines Strategy

| Scale | Engineers | Strategy | Tooling Investment |
|-------|-----------|----------|-------------------|
| **Startup** | 1-10 | Simple monorepo, minimal tooling | Nx or Turborepo, basic CI |
| **Growth** | 10-50 | Structured monorepo, ownership | Nx + Nx Cloud, CODEOWNERS |
| **Scale** | 50-200 | Domain-bounded monorepo | Nx Cloud + distributed caching, merge queues |
| **Enterprise** | 200+ | Federated monorepos or custom | Nx Enterprise, dedicated tooling team |

> **Warning**: The majority of famous monorepos—Windows, Linux kernel, Facebook—all have entire tooling teams dedicated to making them work. Don't apply logic from organizations of a scale you aren't.

### 1.5 Recommended Toolchain (2025)

| Layer | Tool | Why |
|-------|------|-----|
| **Build Orchestrator** | **Nx** | Official MCP server, TypeScript-native, AI-first |
| **JS/TS Package Manager** | **pnpm** | Strict deps, native Nx integration |
| **MCP Integration** | **nx-mcp** | `nx_docs`, `nx_available_plugins` tools for AI agents |
| **Remote Cache** | **Nx Cloud** | Distributed caching, CI integration |
| **Alternative (Simple)** | Turborepo | Simpler setup, but no MCP support |

**Why Nx?**
- **Official MCP server**: Deep AI agent integration via `nx-mcp`
- **TypeScript-native**: Built for JS/TS ecosystem
- **5-minute setup**: vs 3-6 month Bazel learning curve
- **Auto-generates CLAUDE.md/AGENTS.md**: AI assistant context files
- **Affected detection**: `nx affected -t build` for CI optimization

**Why not Bazel?**
- No official MCP server (community only, basic capabilities)
- 3-6 month learning curve for BUILD files and Starlark
- Fights against npm conventions (rules_js complexity)
- Overkill for TypeScript-first projects

See ADR-0020 for full decision rationale (supersedes ADR-0019).

---

## Part 2: Setup

### 2.1 Pre-Setup Decision Framework

Before writing any code, document these decisions:

```yaml
# monorepo-design.yaml

ownership_model:
  question: "How will code ownership work?"
  options:
    - collective: "Anyone can modify anything (< 10 engineers)"
    - team: "Teams own directories (10-50 engineers)"
    - strict: "CODEOWNERS enforced, no exceptions (50+ engineers)"
  selected: null  # Document your choice

dependency_strategy:
  question: "How will packages depend on each other?"
  options:
    - loose: "Any package can depend on any other"
    - layered: "apps → features → shared → core (no reverse)"
    - domain: "Packages grouped by domain, cross-domain via APIs"
  selected: null

versioning_model:
  question: "How will you version packages?"
  options:
    - fixed: "All packages share one version (simpler)"
    - independent: "Each package has own version (flexible)"
    - hybrid: "Core packages fixed, apps independent"
  selected: null

ci_strategy:
  question: "How will CI handle the monorepo?"
  options:
    - full: "Always test everything (small repos only)"
    - affected: "Only test what changed + dependents"
    - distributed: "Parallelize across many machines"
  selected: null
```

### 2.2 Directory Structure Patterns

#### Pattern A: Flat (Startups, < 10 packages)

```
monorepo/
├── apps/
│   ├── web/
│   ├── mobile/
│   └── api/
├── packages/
│   ├── ui/
│   ├── utils/
│   └── types/
├── package.json
├── pnpm-workspace.yaml
└── turbo.json
```

#### Pattern B: Domain-Bounded (Growth, 10-50 packages)

```
monorepo/
├── domains/
│   ├── auth/
│   │   ├── apps/
│   │   │   └── sso-server/
│   │   ├── packages/
│   │   │   ├── auth-client/
│   │   │   └── auth-types/
│   │   └── services/
│   │       └── auth-api/
│   │
│   ├── content/
│   │   ├── apps/
│   │   │   └── docs/
│   │   └── packages/
│   │       └── mdx-components/
│   │
│   └── ai/
│       └── services/
│           └── mcp-server/
│
├── platform/                    # Shared across all domains
│   ├── packages/
│   │   ├── shared-ui/
│   │   ├── shared-config/
│   │   └── shared-types/
│   └── tools/
│       └── scripts/
│
├── .claude/                     # AI intelligence layer
│   ├── skills/
│   ├── agents/
│   └── commands/
│
└── infrastructure/
    ├── docker/
    ├── terraform/
    └── ci/
```

#### Pattern C: Federated (Enterprise, 50+ packages)

```
# Multiple related monorepos with shared tooling
org-repos/
├── platform-monorepo/          # Core platform team
│   ├── packages/
│   └── services/
│
├── product-a-monorepo/         # Product A team
│   ├── apps/
│   └── packages/
│
├── product-b-monorepo/         # Product B team
│   ├── apps/
│   └── packages/
│
└── shared-tooling/             # Shared across all monorepos
    ├── eslint-config/
    ├── tsconfig/
    └── ci-templates/
```

### 2.3 Initial Setup Script (Nx)

```bash
#!/bin/bash
# setup-nx-monorepo.sh

set -e

echo "Setting up Nx monorepo..."

# 1. Create Nx workspace with pnpm
npx create-nx-workspace@latest my-monorepo \
  --preset=apps \
  --packageManager=pnpm \
  --nxCloud=skip

cd my-monorepo

# 2. Create directory structure
mkdir -p .claude/{skills,agents,commands}

# 3. Create pnpm-workspace.yaml
cat > pnpm-workspace.yaml << 'EOF'
packages:
  - 'apps/*'
  - 'libs/*'
  - 'services/*'
EOF

# 4. Configure nx.json for caching
cat > nx.json << 'EOF'
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "cache": true
    },
    "test": {
      "cache": true
    },
    "lint": {
      "cache": true
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*"],
    "production": ["default", "!{projectRoot}/**/*.spec.ts"]
  },
  "defaultBase": "main"
}
EOF

# 5. Create CODEOWNERS
mkdir -p .github
cat > .github/CODEOWNERS << 'EOF'
# Default owner
* @default-team

# Domain-specific ownership (customize)
# /apps/          @apps-team
# /libs/          @platform-team
# /services/      @services-team
EOF

# 6. Create .gitignore additions
cat >> .gitignore << 'EOF'

# Nx
.nx/cache
.nx/workspace-data

# Claude Code
.claude/memory/
EOF

# 7. Add MCP configuration
cat > .mcp.json << 'EOF'
{
  "mcpServers": {
    "nx-mcp": {
      "command": "npx",
      "args": ["nx-mcp@latest"]
    }
  }
}
EOF

# 8. Commit
git add .
git commit -m "chore: initialize Nx monorepo"

echo "Nx monorepo initialized!"
echo ""
echo "Next steps:"
echo "1. Run: pnpm install"
echo "2. Run: nx graph (view project graph)"
echo "3. Add apps: nx g @nx/next:app my-app"
echo "4. Add libs: nx g @nx/js:lib shared-utils"
echo "5. Connect Nx Cloud: npx nx connect"
```

### 2.4 Multi-Language Setup (JS + Python)

For projects with both JavaScript/TypeScript and Python:

```yaml
# pnpm-workspace.yaml - JS packages only
packages:
  - 'apps/*'
  - 'packages/*'
  - 'domains/*/apps/*'
  - 'domains/*/packages/*'
  # Note: Python services managed separately
```

```toml
# pyproject.toml (root) - Python workspace
[tool.uv.workspace]
members = ["services/*", "domains/*/services/*"]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0",
    "ruff>=0.1.0",
]
```

```json
// turbo.json - Orchestrate both languages
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"]
    },
    "build:python": {
      "cache": true,
      "inputs": ["services/**/*.py", "pyproject.toml"],
      "outputs": ["services/**/dist/**"]
    },
    "test:python": {
      "dependsOn": ["build:python"],
      "inputs": ["services/**/*.py", "services/**/tests/**"]
    }
  }
}
```

---

## Part 3: Dependency Management

### 3.1 The Dependency Graph

```
                    ┌─────────────┐
                    │   apps/     │  ← Consumer layer (no deps on each other)
                    │  sso, docs  │
                    └──────┬──────┘
                           │ depends on
                    ┌──────▼──────┐
                    │  features/  │  ← Feature layer (can depend on each other)
                    │ auth, posts │
                    └──────┬──────┘
                           │ depends on
                    ┌──────▼──────┐
                    │  packages/  │  ← Shared layer (no feature deps)
                    │  ui, utils  │
                    └──────┬──────┘
                           │ depends on
                    ┌──────▼──────┐
                    │    core/    │  ← Core layer (no internal deps)
                    │types, config│
                    └─────────────┘
```

### 3.2 Enforcing Boundaries

Using Nx module boundary rules:

```json
// .eslintrc.json
{
  "rules": {
    "@nx/enforce-module-boundaries": [
      "error",
      {
        "depConstraints": [
          {
            "sourceTag": "type:app",
            "onlyDependOnLibsWithTags": ["type:feature", "type:shared", "type:core"]
          },
          {
            "sourceTag": "type:feature",
            "onlyDependOnLibsWithTags": ["type:feature", "type:shared", "type:core"]
          },
          {
            "sourceTag": "type:shared",
            "onlyDependOnLibsWithTags": ["type:shared", "type:core"]
          },
          {
            "sourceTag": "type:core",
            "onlyDependOnLibsWithTags": ["type:core"]
          }
        ]
      }
    ]
  }
}
```

### 3.3 Circular Dependency Prevention

```bash
# Detect circular dependencies
npx madge --circular --extensions ts,tsx apps/ packages/

# In CI - fail if cycles detected
- name: Check for circular dependencies
  run: |
    npx madge --circular --extensions ts,tsx . && echo "No cycles found" || exit 1
```

---

## Part 4: Team Management & Ownership

### 4.1 CODEOWNERS Configuration

```
# .github/CODEOWNERS

# ═══════════════════════════════════════════════════════
# OWNERSHIP RULES
# ═══════════════════════════════════════════════════════

# 1. DOMAIN OWNERSHIP (Primary)
/domains/auth/                    @team-auth
/domains/content/                 @team-content
/domains/ai/                      @team-ai

# 2. PLATFORM OWNERSHIP (Cross-cutting)
/platform/packages/shared-ui/     @team-platform @team-design
/platform/packages/shared-types/  @team-platform
/platform/tools/                  @team-devex

# 3. CRITICAL PATHS (Require senior review)
/platform/packages/shared-auth/   @team-auth @security-leads
*.lock                            @team-platform
/infrastructure/                  @team-sre @security-leads

# 4. DOCUMENTATION (Relaxed ownership)
*.md                              @team-docs
/docs/                            @team-docs

# 5. CI/CD (DevEx + SRE)
/.github/                         @team-devex @team-sre
/turbo.json                       @team-devex
/nx.json                          @team-devex

# 6. AI INTELLIGENCE LAYER
/.claude/                         @team-ai @team-devex
/.claude/skills/                  @team-ai
/.claude/agents/                  @team-ai
```

### 4.2 Team Topology

```
┌─────────────────────────────────────────────────────────────┐
│                    PLATFORM TEAM                            │
│  Owns: /platform/, CI/CD, tooling, shared infrastructure   │
│  Enables: All other teams                                   │
└─────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   AUTH TEAM     │  │  CONTENT TEAM   │  │    AI TEAM      │
│                 │  │                 │  │                 │
│ /domains/auth/  │  │ /domains/content│  │ /domains/ai/    │
│   - SSO server  │  │   - Docs site   │  │   - MCP server  │
│   - Auth SDK    │  │   - MDX utils   │  │   - Agents      │
│   - Auth API    │  │   - Search      │  │   - RAG         │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### 4.3 Cross-Team Coordination Protocols

#### Breaking Change Protocol

```markdown
## Breaking Change Proposal

**Package:** @myorg/shared-auth
**Proposed Change:** Remove `legacyLogin()` function

### Impact Assessment

| Team | Impacted | Files |
|------|----------|-------|
| Auth | Yes | 3 files |
| Content | No | - |
| AI | Yes | 1 file |

### Migration Guide

```typescript
// Before
import { legacyLogin } from '@myorg/shared-auth'

// After
import { login } from '@myorg/shared-auth'
```

### Timeline

- [ ] Announcement: Day 0
- [ ] Deprecation warning added: Day 5
- [ ] Teams migrate: Day 5-15
- [ ] Removal: Day 15

### Approvals Required

- [ ] @team-auth (owner)
- [ ] @team-ai (impacted)
```

#### Shared Package Modification Protocol

```yaml
# When modifying /platform/packages/*

steps:
  1. Create RFC issue:
     - Problem statement
     - Proposed solution
     - Impact on dependent packages

  2. Tag all dependent team leads for review

  3. If approved:
     - Implement with feature flag if risky
     - Add deprecation warnings before removal
     - Update all internal usages in same PR

  4. If rejected:
     - Document decision in ADR
     - Propose alternative or fork for your domain
```

### 4.4 Onboarding Protocol

```markdown
# ONBOARDING.md

## Day 1: Environment Setup

### 1. Clone and Install
```bash
git clone git@github.com:org/monorepo.git
cd monorepo
pnpm install
```

### 2. Verify Setup
```bash
pnpm build        # Should complete in < 5 min (cached)
pnpm test         # Should pass
pnpm dev          # Should start all dev servers
```

### 3. Understand Your Domain
```bash
# If you're on Auth team:
ls -la domains/auth/

# Read the domain README
cat domains/auth/README.md

# Run domain-specific dev
pnpm dev --filter="./domains/auth/**"
```

## Day 2-3: First Contribution

### 4. Make a Small Change
- Find a "good first issue" labeled for your domain
- Create branch: `git checkout -b feat/your-change`
- Make change in YOUR domain only (no cross-domain first week)

### 5. Submit PR
```bash
# Run affected tests
pnpm test --filter=...[origin/main]

# Push and create PR
git push -u origin feat/your-change
gh pr create --fill
```
```

---

## Part 5: Working on Tasks

### 5.1 Task Categories and Workflows

| Task Type | Scope | Workflow | Review |
|-----------|-------|----------|--------|
| **Bug Fix** | Single package | Branch → Fix → PR | Domain owner |
| **Feature** | Single domain | Stack PRs → Review → Merge | Domain team |
| **Cross-Domain** | Multiple domains | RFC → Coordinated PRs → All owners | All impacted |
| **Platform** | Shared packages | RFC → Migration plan → Staged rollout | Platform + all |
| **Refactor** | Any | Codemod → Verify → PR | AI-assisted review |

### 5.2 Single-Domain Task Workflow

```bash
# 1. Start from latest main
git checkout main && git pull

# 2. Create feature branch
git checkout -b feat/auth-oauth-support

# 3. Work in your domain only
code domains/auth/packages/auth-client/src/oauth.ts

# 4. Run affected tests frequently
pnpm test --filter=@myorg/auth-client...

# 5. Commit small, often
git add -A && git commit -m "feat(auth): add OAuth provider interface"

# 6. Push and create PR
git push -u origin feat/auth-oauth-support
gh pr create --title "feat(auth): add OAuth support" --body "..."
```

### 5.3 Cross-Domain Task Workflow (PR Stacking)

```bash
# 1. Create tracking issue first
gh issue create --title "Add OAuth across all apps" --label "cross-domain"

# 2. Break into stacked PRs (using Graphite)
gt create -m "feat(auth): OAuth provider interface"   # PR #1
gt create -m "feat(auth): OAuth implementation"       # PR #2
gt create -m "feat(sso): integrate OAuth"             # PR #3
gt create -m "feat(docs): OAuth documentation"        # PR #4

# 3. Each PR reviewed by respective domain owner
# 4. Merge as stack (atomic)
gt submit --stack
```

### 5.4 Trunk-Based Development Rules

```yaml
branch_lifetime:
  max_hours: 24
  exception: "Complex features use stacked PRs, not long branches"

commit_size:
  max_files: 20
  max_lines: 400
  exception: "Automated refactors/codemods can be larger"

merge_requirements:
  - all_ci_green: true
  - codeowner_approval: true
  - no_wip_commits: true

feature_flags:
  required_when:
    - "Change affects production users"
    - "Change is not fully complete"
    - "Change needs gradual rollout"

revert_policy:
  threshold: "If fix takes > 10 min, revert first"
  command: "git revert HEAD && git push"
```

---

## Part 6: CI/CD

### 6.1 Nx CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for affected detection

      - uses: pnpm/action-setup@v2

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      # Affected-only builds (recommended)
      - name: Build and test affected
        run: npx nx affected -t lint build test --base=origin/main

  # Alternative: Build everything (for main branch)
  build-all:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: npx nx run-many -t lint build test
```

### 6.2 Remote Caching Setup (Nx Cloud)

```bash
# Connect to Nx Cloud (free tier available)
npx nx connect

# Or configure manually in nx.json
```

```json
// nx.json
{
  "nxCloudAccessToken": "your-token-here"
}
```

**Cache Options**:
| Provider | Cost | Setup | Features |
|----------|------|-------|----------|
| **Nx Cloud** | Free tier | Low | Cache + insights + CI optimization |
| **Self-hosted** | Server cost | High | Full control |

```bash
# Verify caching works
nx build my-app
# Second run should show "cache hit"
nx build my-app
```

### 6.3 Merge Queue Configuration

```yaml
# Branch protection rules
protection_rules:
  main:
    required_status_checks:
      strict: true
      contexts:
        - "js-ci"
        - "python-ci"

    merge_queue:
      enabled: true
      method: "squash"
      batch_size: 5              # Merge up to 5 PRs together
      wait_time_minutes: 5       # Wait for more PRs to batch

    required_reviews: 1
    codeowner_review: true
```

---

## Part 7: Delegating to AI Agents

### 7.1 AI Agent Roles in Monorepo

> "AI and monorepos elevate each other: monorepos provide unified context for powerful agentic workflows, while AI helps navigate and automate monorepo complexity."

| Agent Type | Task | Human Role |
|------------|------|------------|
| **Code Generation** | Implement feature from spec | Review, refine, approve |
| **Refactoring** | Apply codemod across packages | Define scope, verify results |
| **CI Management** | Fix flaky tests, update deps | Approve changes |
| **Review Assistant** | Pre-review PRs, catch issues | Final approval |
| **Migration** | Update API usage across codebase | Define migration, spot-check |

### 7.2 Human-AI Task Delegation Matrix

```
┌────────────────────────────────────────────────────────────────┐
│                    TASK DELEGATION MATRIX                      │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  HUMAN ONLY                    │  AI-ASSISTED                  │
│  ────────────────────────────  │  ────────────────────────────│
│  • Architecture decisions      │  • Code generation from spec  │
│  • Cross-domain coordination   │  • Test writing               │
│  • Breaking change approval    │  • Documentation              │
│  • Production deployment       │  • Refactoring                │
│  • Security-critical changes   │  • Dependency updates         │
│  • Team conflicts              │  • Code review (first pass)   │
│                                │  • Bug investigation          │
│                                │                               │
│  AI AUTONOMOUS                 │  HUMAN REVIEW REQUIRED        │
│  ────────────────────────────  │  ────────────────────────────│
│  • Lint fixes                  │  • New features               │
│  • Type error fixes            │  • API changes                │
│  • Test fixes (deterministic)  │  • Database migrations        │
│  • Import organization         │  • Auth/security changes      │
│  • Formatting                  │  • Cross-domain changes       │
│  • README updates              │  • Performance changes        │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 7.3 Agent Skill for Monorepo Tasks

```markdown
<!-- .claude/skills/monorepo-task/SKILL.md -->
---
name: "monorepo-task"
description: "Execute tasks within monorepo boundaries. Use when user asks to modify, build, or test packages."
version: "1.0.0"
---

# Monorepo Task Skill

## Before ANY Modification

1. **Identify affected domain**
   ```bash
   # What domain does this file belong to?
   # /domains/auth/packages/... → auth domain
   # /platform/packages/... → platform (cross-cutting)
   ```

2. **Check ownership**
   ```bash
   # Who owns this code?
   cat .github/CODEOWNERS | grep <path>
   ```

3. **Understand dependencies**
   ```bash
   # What depends on this package?
   pnpm turbo build --filter=@myorg/package... --dry-run
   ```

## During Modification

4. **Stay within domain boundaries**
   - If task requires cross-domain changes, STOP and ask human
   - Single-domain changes can proceed autonomously

5. **Run affected tests continuously**
   ```bash
   pnpm turbo test --filter=...[HEAD~1]
   ```

## After Modification

6. **Verify no unintended changes**
   ```bash
   git diff --stat
   # Should only show files in intended scope
   ```

7. **Create atomic commit**
   ```bash
   git commit -m "feat(<domain>): <description>"
   ```
```

### 7.4 Background Agent Pattern

For long-running tasks that don't need real-time interaction:

```yaml
# .claude/agents/background-worker.yaml
name: background-worker
description: "Long-running tasks executed asynchronously"

suitable_tasks:
  - Large-scale refactoring
  - Test generation for existing code
  - Documentation generation
  - Dependency updates
  - Code migration

workflow:
  1. Human: Creates task spec
  2. Agent: Works in background (can take hours)
  3. Agent: Creates draft PR when done
  4. Human: Reviews PR next morning

constraints:
  - No production deployments
  - No breaking changes without explicit approval
  - Must run all affected tests
  - Must create detailed PR description
```

### 7.5 Cross-Project Refactor Workflow

```markdown
## Scenario: Rename function across monorepo

### Step 1: Human Creates Specification
```yaml
refactor:
  type: rename
  from: getUserId
  to: getCurrentUserId
  scope:
    - domains/auth/**
    - domains/content/**
  exclude:
    - "*.test.ts"

validation:
  - all_tests_pass: true
  - no_type_errors: true
  - no_runtime_changes: true
```

### Step 2: AI Agent Executes
```bash
# Discover all usages
grep -r "getUserId" domains/ --include="*.ts" | wc -l
# Found: 47 usages across 12 files

# Apply codemod
jscodeshift -t transforms/rename-function.ts domains/

# Run verification
pnpm turbo typecheck test --filter="./domains/**"

# Create PR
gh pr create --title "refactor: rename getUserId to getCurrentUserId"
```

### Step 3: Human Reviews
- Verify semantic correctness
- Check edge cases (dynamic calls, string references)
- Approve or request changes
```

---

## Part 8: Edge Cases & Pitfalls

### 8.1 The Scaling Wall

**Detection Signals:**

```yaml
warning_signs:
  - git_status_time: "> 2 seconds"
  - clone_time: "> 10 minutes"
  - ide_indexing: "> 5 minutes"
  - ci_full_build: "> 30 minutes"
```

**Solutions:**

| Problem | Solution |
|---------|----------|
| Git slow | Sparse checkout, VFS for Git |
| Clone slow | Shallow clone (`--depth 1`), partial clone |
| Build slow | Remote caching, distributed execution |
| IDE slow | Project-specific workspaces, reduce indexing |

### 8.2 The Dependency Diamond

```
        ┌──────┐
        │ App  │
        └──┬───┘
       ┌───┴───┐
       ▼       ▼
   ┌──────┐ ┌──────┐
   │Pkg A │ │Pkg B │
   └──┬───┘ └───┬──┘
      │         │
      │    ┌────┘
      ▼    ▼
    ┌────────┐
    │ Core   │  ← Pkg A wants v1.0, Pkg B wants v2.0
    └────────┘
```

**Solutions:**

```yaml
# 1. Fixed versioning (recommended)
all_packages_same_version: true

# 2. Workspace protocol (pnpm)
dependencies:
  "@myorg/core": "workspace:*"  # Always use local version

# 3. Peer dependencies for shared deps
peerDependencies:
  "@myorg/core": "^2.0.0"
```

### 8.3 The "Everything Depends on Everything" Trap

**Detection:**

```bash
# Count dependencies per package
for pkg in packages/*; do
  echo "$pkg: $(grep -c '"@myorg/' $pkg/package.json 2>/dev/null || echo 0)"
done | sort -t: -k2 -rn

# If a package has 10+ internal deps, it's a code smell
```

**Prevention:**

```json
// Max internal dependencies rule
{
  "rules": {
    "max-internal-deps": ["error", {
      "max": 5,
      "exclude": ["apps/*"]
    }]
  }
}
```

### 8.4 Abandoned Packages

**Detection Script:**

```bash
#!/bin/bash
# find-abandoned.sh

echo "Packages with no commits in 6 months:"

for pkg in packages/* domains/*/packages/*; do
  last_commit=$(git log -1 --format="%ar" -- "$pkg" 2>/dev/null)
  if [[ "$last_commit" == *"months"* ]] || [[ "$last_commit" == *"year"* ]]; then
    echo "  $pkg: $last_commit"
  fi
done
```

**Archival Process:**

```yaml
archival_criteria:
  - no_commits_days: 180
  - no_dependents: true
  - not_in_production: true

archival_process:
  1. Create deprecation issue
  2. Add @deprecated JSDoc to exports
  3. Wait 30 days for objections
  4. Move to /archived/ directory
  5. Remove from workspace
```

### 8.5 Secret/Credential Sprawl

```yaml
# Pre-commit hook for secret scanning
- name: Scan for secrets
  uses: trufflesecurity/trufflehog@main
  with:
    path: ./
    extra_args: --only-verified
```

```gitignore
# .gitignore - Never commit these
.env
.env.*
*.pem
*.key
credentials.json
secrets.yaml
```

### 8.6 Polyglot Complexity

For JS + Python monorepos:

**Challenges:**
- Different package managers (pnpm vs uv)
- Different test frameworks (vitest vs pytest)
- Different linters (eslint vs ruff)
- Different type systems

**Solutions:**

```yaml
# Unified task runner (turbo.json)
tasks:
  build:
    dependsOn: ["^build"]

  "services/mcp-server#build":
    inputs: ["services/mcp-server/**/*.py"]
    outputs: ["services/mcp-server/dist/**"]
    command: "cd services/mcp-server && uv build"

# Shared types via code generation
types_workflow:
  1. Define types in TypeScript (source of truth)
  2. Generate Python types with datamodel-codegen
  3. Import generated types in Python services
```

---

## Part 9: Tooling Decision Matrix

### 9.1 Choose Your Stack

| Scenario | Package Manager | Build Tool | CI Optimization |
|----------|-----------------|------------|-----------------|
| **Small (< 10 pkgs)** | pnpm | Turborepo | GitHub Actions |
| **Medium (10-50 pkgs)** | pnpm | Nx | Nx Cloud |
| **Large (50+ pkgs)** | pnpm/yarn | Nx | Nx Cloud + distributed |
| **Enterprise (100+)** | Custom | Bazel | Custom infra |
| **Polyglot** | pnpm + uv | moon / Nx | Platform-specific |

### 9.2 Migration Decision Tree

```
START: Do you have multiple repos?
  │
  ├── YES: Are they tightly coupled?
  │         ├── YES: Migrate to monorepo ✅
  │         └── NO: Keep separate (with shared tooling)
  │
  └── NO (already monorepo): Is it working?
            ├── YES: Don't change it ✅
            └── NO: What's the problem?
                    ├── Too slow → Add caching, affected-only
                    ├── Ownership unclear → Add CODEOWNERS
                    ├── Breaking changes → Add boundaries
                    └── Teams fighting → Consider splitting
```

---

## Part 10: Checklists

### 10.1 Pre-Migration Checklist

```markdown
## Before Starting Monorepo Migration

### Technical Readiness
- [ ] All repos use same major version of Node.js
- [ ] All repos use compatible package manager
- [ ] CI/CD can be unified
- [ ] No conflicting dependencies between repos

### Organizational Readiness
- [ ] Team leads agree on ownership model
- [ ] CODEOWNERS structure defined
- [ ] Breaking change process documented
- [ ] On-call rotation covers shared packages

### Tooling Readiness
- [ ] Build tool selected (Turborepo/Nx/Bazel)
- [ ] Remote caching available
- [ ] IDE configured for monorepo
- [ ] Git hosting supports large repos
```

### 10.2 Daily Development Checklist

```markdown
## Before Starting Work
- [ ] `git pull --rebase` (stay current)
- [ ] `pnpm install` (deps might have changed)
- [ ] Check if your domain's tests pass

## During Development
- [ ] Stay within domain boundaries
- [ ] Run affected tests: `pnpm turbo test --filter=...[HEAD~1]`
- [ ] Commit small, often

## Before Creating PR
- [ ] All affected tests pass
- [ ] No type errors: `pnpm turbo typecheck`
- [ ] Lint clean: `pnpm turbo lint`
- [ ] PR title follows convention
- [ ] PR description explains WHY

## After PR Merged
- [ ] Delete local branch
- [ ] Monitor CI on main
- [ ] Verify deployment (if applicable)
```

### 10.3 AI Agent Task Checklist

```markdown
## Before Delegating to AI Agent

### Task Suitability
- [ ] Task is well-defined with clear success criteria
- [ ] Task scope is limited (single domain preferred)
- [ ] Task doesn't require production access
- [ ] Task doesn't involve security-critical code

### Context Provided
- [ ] Specification document exists
- [ ] Affected packages identified
- [ ] Test requirements specified
- [ ] Boundaries explicitly stated

### Human Checkpoints Defined
- [ ] Review point after each major step
- [ ] Approval required for cross-domain changes
- [ ] Final human review before merge

## After AI Completes Task
- [ ] Verify changes are within expected scope
- [ ] Run full affected test suite
- [ ] Check for subtle semantic errors
- [ ] Approve or send back with feedback
```

---

## Part 11: AI Skills for Monorepo Work

Claude Code has **3 principal-level (L4/E5) skills** for Nx monorepo operations, plus access to the `nx-mcp` server with 2 tools.

### MCP Integration

The `nx-mcp` server provides AI agents with:

| Tool | Purpose | Use When |
|------|---------|----------|
| `nx_docs` | Query Nx documentation | "How do I configure caching?", "What is affected?" |
| `nx_available_plugins` | List official @nx/* plugins | "What plugins can I add?", "Does Nx support Vue?" |

### Available Skills

| Skill | Purpose | Invoke When |
|-------|---------|-------------|
| **nx-monorepo** | Project graph, affected detection, generators, caching | Analyzing deps, running affected, code generation |
| **monorepo-workflow** | Trunk-based dev, PR stacking, breaking changes | Managing PRs, code review (tool-agnostic) |
| **monorepo-team-lead** | CODEOWNERS, human-AI routing, onboarding | Team coordination (tool-agnostic) |

### Skill Routing Guide

```
Task Type                         → Action
─────────────────────────────────────────────────
"What depends on X?"              → nx graph --focus=X (nx-monorepo skill)
"Why isn't cache working?"        → Check nx.json, nx reset (nx-monorepo skill)
"Add TypeScript library"          → nx g @nx/js:lib name (nx-monorepo skill)
"Set up GitHub Actions"           → nx affected CI pattern (nx-monorepo skill)
"Create a stacked PR"             → monorepo-workflow (tool-agnostic)
"Who owns this code?"             → monorepo-team-lead (CODEOWNERS)
"How do I configure X?"           → nx_docs MCP tool
"What plugins are available?"     → nx_available_plugins MCP tool
```

### Multi-Skill Workflows

Complex tasks may require multiple skills:

```
Example: "Add a new TypeScript library"

1. nx-monorepo      → nx g @nx/js:lib shared-utils
2. nx-monorepo      → nx graph --focus=shared-utils (verify in graph)
3. nx-monorepo      → nx build shared-utils (test build)
```

```
Example: "Optimize CI for affected-only"

1. nx-monorepo      → Update CI workflow with nx affected
2. nx-monorepo      → Connect to Nx Cloud (npx nx connect)
3. monorepo-workflow → PR template with affected list
```

### Key Nx Commands (Quick Reference)

```bash
# Build & Test
nx run-many -t build             # Build all projects
nx run-many -t test              # Test all projects
nx serve my-app                  # Serve an app

# Project Graph
nx graph                         # Interactive graph
nx graph --focus=my-app          # Focus on one project
nx show projects --affected      # List affected projects

# Affected Detection
nx affected -t build             # Build affected only
nx affected -t test --base=main  # Test affected since main

# Code Generation
nx g @nx/next:app my-app         # Generate Next.js app
nx g @nx/js:lib shared-utils     # Generate JS library
nx g @nx/react:lib ui            # Generate React library

# Caching
nx reset                         # Clear cache
npx nx connect                   # Connect to Nx Cloud
```

---

## References

### Microsoft & Windows
- [How Microsoft's Git Fork Scales for Massive Monorepos](https://www.infoworld.com/article/2337202/how-microsofts-git-fork-scales-for-massive-monorepos.html)
- [Working with a Monorepo - Microsoft ISE Blog](https://devblogs.microsoft.com/ise/working-with-a-monorepo/)

### Google & Facebook
- [How Google Does Monorepo](https://qeunit.com/blog/how-google-does-monorepo/)
- [Trunk Based Development](https://trunkbaseddevelopment.com/)

### Pitfalls & Edge Cases
- [5 Mistakes to Avoid with a Monorepo](https://blog.bitsrc.io/5-mistakes-that-you-should-avoid-with-a-monorepo-956e8fe3633e)
- [Common Pitfalls When Adopting a Monorepo](https://graphite.com/guides/monorepo-pitfalls-guide)

### AI & Automation
- [Monorepos & AI](https://monorepo.tools/ai)
- [AI Coding Assistants for Large Codebases](https://www.augmentcode.com/guides/ai-coding-assistants-for-large-codebases-a-complete-guide)

### Team Productivity
- [How Shopify Scaled with Stacking](https://graphite.dev/customer/shopify)
- [Git Monorepo Best Practices](https://graphite.dev/guides/git-monorepo-best-practices-for-scalability)

---

## Discussion Points

> **This document is a living reference. Key decisions made:**

1. **Build Tool**: Nx (with MCP integration) - See ADR-0020
2. **Ownership Model**: CODEOWNERS with domain boundaries
3. **AI Delegation**: 3 skills (nx-monorepo, workflow, team-lead) + nx-mcp server
4. **Cross-Domain Protocol**: RFC process via monorepo-team-lead skill
5. **Python Integration**: Nx plugins for Python when needed
