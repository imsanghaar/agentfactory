# ADR-0005: Git Worktrees as Parallel Development Infrastructure

> **Scope**: This ADR documents the decision to use git worktrees as the technical infrastructure enabling true parallel development, rather than branch-only workflows, Docker containers, or cloud workspaces.

- **Status:** Accepted
- **Date:** 2025-11-06
- **Feature:** 002-chapter-32-redesign
- **Context:** To teach decomposition thinking through hands-on parallel development, students need infrastructure that enables 3-10 simultaneous workflows with complete isolation. The infrastructure choice impacts pedagogical effectiveness (learning curve), technical correctness (avoiding file conflicts), and transferability (patterns students can use in production). Git worktrees provide the optimal balance of simplicity, isolation, and professional relevance.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: YES - Long-term consequence for how students manage parallel development throughout Chapter 32 and in future projects
     2) Alternatives: YES - Multiple viable options considered (branches only, Docker containers, cloud workspaces, virtual environments)
     3) Scope: YES - Cross-cutting concern affecting all lessons L1-L8, foundational for all parallel workflows
-->

## Decision

Use **Git Worktrees** as the primary infrastructure for parallel development:

**Technical Implementation:**

1. **Worktree Setup**: Each feature gets isolated working directory
   ```bash
   git worktree add ../worktree-001-auth feature-001-auth
   git worktree add ../worktree-002-products feature-002-products
   git worktree add ../worktree-003-cart feature-003-cart
   ```

2. **Isolation Mechanism**: Complete file system isolation
   - Each worktree = separate directory with own file state
   - Shared git history (`.git` directory)
   - Independent branches per worktree
   - No file conflicts during parallel work

3. **Session Management**: One terminal/Claude session per worktree
   - Terminal 1 (main): Orchestration, monitoring
   - Terminal 2 (worktree-001): Feature 001 development
   - Terminal 3 (worktree-002): Feature 002 development
   - Terminal 4 (worktree-003): Feature 003 development

4. **Integration Workflow**: Merge branches sequentially after parallel work
   ```bash
   # After parallel implementations complete
   git checkout main
   git merge feature-001-auth
   git merge feature-002-products
   git merge feature-003-cart
   ```

**Pedagogical Benefits:**
- Students see isolation visually (separate directories)
- Terminal-per-worktree maps 1:1 with agent-per-feature
- Merge conflicts reveal decomposition quality immediately
- Same workflow scales from 3 to 10 worktrees

## Consequences

### Positive

1. **Complete Isolation**: No file conflicts during parallel work (students can work truly independently)
2. **Low Learning Curve**: Students already know git and directories (no new tools to learn)
3. **Visual Clarity**: Separate directories make parallel work tangible (not abstract)
4. **Production-Ready Pattern**: Git worktrees used by professional developers for parallel feature work
5. **Scales Well**: Works for 3-10 worktrees without additional infrastructure
6. **Clean Integration**: Merge workflow validates decomposition quality (conflicts = boundary problems)
7. **No External Dependencies**: Works on any machine with git 2.5+ (no cloud accounts, Docker setup)

### Negative

1. **Disk Space**: Each worktree duplicates working directory files (3 features = 3x disk usage)
2. **Manual Cleanup**: Students must remember to remove worktrees after merging (`git worktree remove`)
3. **Not Obvious**: Git worktrees are lesser-known feature (requires explicit teaching in Lesson 1)
4. **Terminal Management**: 3-10 open terminals can be overwhelming without tmux/multiplexing
5. **Path Confusion**: Students might forget which terminal corresponds to which worktree

## Alternatives Considered

### Alternative A: Branch-Only Workflow (No Worktrees)
**Approach**: Use `git checkout` to switch branches, one working directory

**Why Rejected**:
- No true parallelization (must switch branches sequentially)
- File state changes with branch switch (confusing for beginners)
- Defeats the pedagogical goal (experiencing parallel work)
- Forces synchronous workflow (exactly what we're teaching to avoid)

**When It's Better**: Solo development with sequential feature work

### Alternative B: Docker Containers per Feature
**Approach**: Spin up separate Docker containers, each with own git clone

**Why Rejected**:
- High setup complexity (Docker installation, container management)
- Introduces Docker learning curve (scope creep for Chapter 32)
- Overkill for parallel development (Docker solves environment isolation, not needed here)
- Harder to debug (container networking, volume mounts)
- Disk space worse than worktrees (each container = full OS + dependencies)

**When It's Better**: Testing environment-specific issues, production microservices

### Alternative C: Cloud Workspaces (GitHub Codespaces, Gitpod)
**Approach**: Spin up cloud-based development environments per feature

**Why Rejected**:
- Requires internet connection (breaks local development workflows)
- Cost barrier (free tiers limited, students may need paid plans)
- Introduces cloud account management (authentication, quotas)
- Slower iteration (cloud latency vs local)
- Not transferable to air-gapped or offline scenarios

**When It's Better**: Distributed teams need consistent environments, no local setup

### Alternative D: Virtual Environments Only (Python venv, Node.js nvm)
**Approach**: Use language-specific virtual environments for isolation

**Why Rejected**:
- Only isolates dependencies, not file system (students still experience file conflicts)
- Doesn't enable true parallel development (still one working directory)
- Language-specific (doesn't generalize across Python, TypeScript, etc.)
- Misses the decomposition learning objective

**When It's Better**: Managing dependency conflicts, testing with different library versions

## Why Git Worktrees Win

**Decision Rationale**:
1. **Simplicity**: Students already know git and directories (minimal new concepts)
2. **Isolation**: Complete file system separation prevents conflicts during parallel work
3. **Pedagogically Sound**: Visual separation reinforces decomposition thinking
4. **Production-Ready**: Real developers use git worktrees for parallel feature work
5. **No External Dependencies**: Works anywhere git works (universal accessibility)
6. **Transferable**: Same pattern works for 3 features or 50 features

## Worktree Best Practices (Taught in Lesson 1)

**Setup Pattern:**
```bash
# Create worktree structure
git worktree add ../worktree-001-auth feature-001-auth
git worktree add ../worktree-002-products feature-002-products

# Verify isolation
git worktree list
```

**Naming Convention:**
- `worktree-NNN-feature-name` (e.g., `worktree-001-auth`)
- Number matches feature number (001, 002, 003)
- Clear labels prevent confusion

**Terminal Setup:**
- tmux windows or iTerm2 split panes
- Label each terminal clearly
- Keep orchestration terminal separate

**Cleanup After Integration:**
```bash
git worktree remove ../worktree-001-auth
git branch -d feature-001-auth  # if fully merged
```

## References

- Feature Spec: `specs/002-chapter-32-redesign/spec.md` (FR-001, FR-002, FR-005)
- Implementation Plan: `specs/002-chapter-32-redesign/plan.md` (Lesson 1, foundational for all)
- Refactored Tasks: `specs/002-chapter-32-redesign/tasks-REFACTORED.md` (Task 2.1)
- Related ADRs:
  - ADR-0001 (Two-Climax Structure - worktrees enable both climaxes)
  - ADR-0004 (Contract-Based Coordination - worktrees provide isolation for autonomous work)
- Git Worktree Documentation: https://git-scm.com/docs/git-worktree (official reference)
- Real-World Usage: Vercel engineering uses worktrees for parallel feature development
