# ADR 0019: Bazel as Monorepo Standard Over Turborepo

**Status**: Superseded by ADR-0020
**Date**: 2025-12-15
**Deciders**: MJS, Claude Code
**Context**: Build orchestrator selection for polyglot monorepo

---

## Context

### Problem Statement

We needed to select a build orchestrator for our monorepo that supports:
- Multiple languages (JavaScript/TypeScript, Python, Go)
- Remote caching for CI performance
- Affected-only testing
- Hermetic, reproducible builds
- Enterprise-scale growth potential

### Options Considered

| Tool | Type | Multi-Language | Remote Cache | Hermetic |
|------|------|----------------|--------------|----------|
| **Turborepo** | JS-focused orchestrator | Limited (plugins) | Vercel Cloud | No |
| **Nx** | JS-focused orchestrator | Limited (plugins) | Nx Cloud | No |
| **Bazel** | Universal build system | Native | Multiple options | Yes |
| **moon** | Polyglot orchestrator | Yes | Limited | No |

### Key Comparison: Bazel vs Turborepo

| Capability | Turborepo | Bazel |
|------------|-----------|-------|
| **Language Support** | JS/TS native, others via plugins | Native JS/TS, Python, Go, Java, C++ |
| **Dependency Tracking** | Package-level | File-level (more precise) |
| **Build Hermeticity** | No (relies on host tools) | Yes (sandboxed execution) |
| **Remote Cache** | Vercel Cloud only | BuildBuddy, GCS, self-hosted |
| **Distributed Execution** | No | Yes |
| **Build Graph Query** | Limited | Powerful query language |
| **Affected Detection** | Package-level | File-level precision |
| **Learning Curve** | Low | Medium-High |

---

## Decision

**Adopt Bazel as the standard build system for polyglot monorepos.**

### Rationale

1. **True Polyglot Support**: Bazel has first-class rules for JS/TS (`rules_js`), Python (`rules_python`), and Go (`rules_go`). Turborepo requires bolting on language support.

2. **Hermetic Builds**: Bazel's sandboxed execution ensures builds are reproducible across environments. Turborepo relies on host-installed tools.

3. **Precision**: Bazel tracks dependencies at file level, not package level. This means:
   - More precise affected detection
   - Better cache hit rates
   - Smaller rebuild scope

4. **Remote Execution**: Bazel supports distributed builds across many machines, essential for large codebases. Turborepo has no equivalent.

5. **Query Language**: `bazel query` provides powerful dependency analysis:
   ```bash
   # What depends on this target?
   bazel query "rdeps(//..., //libs/shared:utils)"

   # All Python binaries
   bazel query "kind(py_binary, //...)"
   ```
   Turborepo has no equivalent capability.

6. **Enterprise Proven**: Bazel is used by Google, Meta, Stripe, Twitter. Turborepo is newer with smaller scale deployments.

### Package Managers Still Used

Bazel doesn't replace package managers—it reads their lockfiles:

| Language | Package Manager | Bazel Integration |
|----------|-----------------|-------------------|
| JS/TS | pnpm | `rules_js` reads `pnpm-lock.yaml` |
| Python | uv | `rules_python` reads `requirements_lock.txt` |
| Go | go mod | `rules_go` reads `go.mod` |

**Workflow**:
1. Use pnpm/uv/go to manage dependencies
2. Bazel reads lockfiles and orchestrates builds
3. Remote cache shared across developers and CI

---

## Consequences

### Positive

1. **Unified Build System**: One system for all languages instead of language-specific tooling
2. **Better CI Performance**: File-level caching + remote cache = faster builds
3. **Reproducibility**: Hermetic builds eliminate "works on my machine" issues
4. **Scale Ready**: Distributed execution available when needed
5. **Query Power**: Rich dependency analysis for impact assessment

### Negative

1. **Learning Curve**: BUILD files and Starlark require learning
2. **Initial Setup**: More complex than `turbo.json`
3. **Tooling Investment**: Need to learn Gazelle, understand rules
4. **Community Size**: Smaller community than Turborepo for JS-focused work

### Mitigations

- **Gazelle**: Auto-generates BUILD files from source, reducing manual work
- **Skills Architecture**: Created 4 Bazel-focused skills (`bazel-navigator`, `bazel-builder`, `bazel-rules`, `bazel-ci`) to encode expertise
- **Architecture Guide**: Updated `monorepo-architecture-guide.md` with Bazel patterns

---

## Implementation Impact

### Files Updated

| File | Change |
|------|--------|
| `CLAUDE.md` | Updated Section V with Bazel skills, toolchain |
| `monorepo-orchestrator/SKILL.md` | Routes to Bazel skills instead of Turborepo |
| `monorepo-architecture-guide.md` | Bazel as primary, Turborepo as "simple alternative" |

### New Skills Created

| Skill | Purpose |
|-------|---------|
| `bazel-navigator` | `bazel query`, dependency analysis, affected detection |
| `bazel-builder` | BUILD files, Gazelle, caching, .bazelrc |
| `bazel-rules` | MODULE.bazel, rules_js, rules_python, rules_go |
| `bazel-ci` | Remote caching, GitHub Actions, BuildBuddy |

### Skills Deprecated (To Delete)

| Skill | Reason |
|-------|--------|
| `monorepo-navigator` | Replaced by `bazel-navigator` |
| `monorepo-builder` | Replaced by `bazel-builder` |
| `monorepo-ci-architect` | Replaced by `bazel-ci` |
| `monorepo-platform` | Functionality split into Bazel skills |

### Skills Retained (Tool-Agnostic)

| Skill | Reason |
|-------|--------|
| `monorepo-workflow` | PR stacking, trunk-based dev (not build-tool specific) |
| `monorepo-team-lead` | CODEOWNERS, coordination (not build-tool specific) |

---

## Quick Reference

### Bazel vs Turborepo Commands

| Task | Turborepo | Bazel |
|------|-----------|-------|
| Build all | `turbo build` | `bazel build //...` |
| Test all | `turbo test` | `bazel test //...` |
| Affected only | `turbo build --filter=...[origin/main]` | `bazel query "rdeps(//..., set(...))"` |
| Clean | `turbo clean` | `bazel clean` |
| Cache debug | `turbo build --dry-run` | `--execution_log_json_file=/tmp/log.json` |

### When Turborepo Might Be Better

- **Simple JS-only monorepo**: < 10 packages, single language
- **Vercel ecosystem**: Already using Vercel for hosting
- **Quick start**: Need something working in hours, not days
- **Team familiarity**: Team already knows Turborepo

### When Bazel Is Better

- **Polyglot**: Multiple languages (JS + Python + Go)
- **Scale**: 50+ packages, distributed builds needed
- **Hermeticity**: Reproducible builds critical
- **Query needs**: Complex dependency analysis required
- **Enterprise**: Google/Meta-scale patterns needed

---

## References

- [Bazel Documentation](https://bazel.build/)
- [rules_js (Aspect)](https://github.com/aspect-build/rules_js)
- [rules_python](https://github.com/bazelbuild/rules_python)
- [BuildBuddy](https://www.buildbuddy.io/)
- Previous skills: `monorepo-*` (Turborepo-based)
