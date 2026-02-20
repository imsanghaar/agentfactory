# ADR 0020: Nx as Monorepo Standard (Superseding Bazel)

**Status**: Accepted
**Date**: 2025-12-15
**Deciders**: MJS, Claude Code
**Supersedes**: ADR-0019 (Bazel as Monorepo Standard)
**Context**: Build orchestrator selection for AI-native education platform

---

## Context

### Problem Statement

ADR-0019 selected Bazel as the monorepo standard based on technical criteria (hermetic builds, polyglot support, distributed execution). However, after deeper research, we identified a critical gap: **AI agent integration**.

This platform is an **AI-native education platform teaching Claude Code development**. The primary users are:
- Students learning AI-assisted development
- Authors creating AI-powered educational content
- AI agents (Claude Code) assisting with development

The monorepo tool must excel at **enabling AI agents to understand and navigate the codebase**, not just build it.

### Options Reconsidered

| Tool | MCP Status | AI Understanding | JS/TS Fit | Learning Curve |
|------|-----------|------------------|-----------|----------------|
| **Nx** | Official server | Deep (graph, CI, generation) | Native | 5 minutes |
| **Bazel** | Community only | Basic (query) | Fights npm | 3-6 months |
| **moon** | Official server | Medium (7 tools) | Native | Low-Medium |
| **Turborepo** | None (requested) | None | Native | Very Low |

### Critical Discovery: MCP Integration

The Model Context Protocol (MCP) is the standard for AI agent integration. Research revealed:

**Nx MCP Server** (Official - `nx-mcp@latest`):
- Workspace analysis with project relationships
- Live terminal integration
- CI/CD visibility (build failures, test results)
- Code generation with contextual defaults
- Cross-project impact analysis
- Graph visualization

**Bazel MCP Servers** (Community - nacgarg, aaomidi):
- Basic build/test/query operations
- No workspace analysis
- No CI integration
- No code generation

---

## Decision

**Adopt Nx as the standard build orchestrator, superseding the Bazel decision in ADR-0019.**

### Rationale

1. **AI-Native Integration**: Nx has an official MCP server with deep workspace understanding. Bazel has only community servers with basic capabilities.

2. **Project Fit**: This platform is TypeScript/Next.js-first. Nx is built for this ecosystem. Bazel's `rules_js` fights against npm conventions.

3. **Teaching Friendly**: Students can set up Nx in 5 minutes. Bazel requires 3-6 months to master BUILD files and Starlark.

4. **Claude Code Alignment**: Nx automatically generates `CLAUDE.md` and `AGENTS.md` files for AI assistants. Bazel has no equivalent.

5. **Ecosystem Momentum**: Nx MCP is production-ready and officially maintained. Bazel MCP is experimental community work.

### What Bazel Does Better (And Why It Doesn't Matter Here)

| Bazel Strength | Why Not Critical |
|----------------|------------------|
| Hermetic builds | Not needed for education platform |
| Distributed execution | Scale not required |
| Polyglot native | Platform is 90% TypeScript |
| File-level precision | Nx package-level is sufficient |

### MCP Capability Comparison

| Capability | Nx MCP | Bazel MCP |
|------------|--------|-----------|
| Workspace analysis | ✅ Deep | ❌ None |
| Project graph | ✅ Visual | ⚠️ Query only |
| CI integration | ✅ Full | ❌ None |
| Code generation | ✅ Scaffolding | ❌ None |
| Impact analysis | ✅ Cross-project | ⚠️ Manual |
| Live terminal | ✅ Real-time | ❌ None |

---

## Consequences

### Positive

1. **AI Agent Effectiveness**: Claude Code gains deep understanding of monorepo structure
2. **Fast Adoption**: 5-minute setup vs 3-6 month learning curve
3. **Ecosystem Alignment**: Native pnpm, TypeScript, Next.js support
4. **Teaching Value**: Students learn industry-standard tool with AI integration
5. **Maintenance**: Official MCP server with Nx team support

### Negative

1. **No Hermetic Builds**: Builds depend on host environment (acceptable for education)
2. **No Distributed Execution**: Cannot scale to Google-level builds (not needed)
3. **Polyglot Limitation**: Python/Go support via plugins, not native (acceptable)
4. **ADR-0019 Artifacts**: Must clean up Bazel skills, docs, configs created earlier

### Mitigations

- **Polyglot future**: Nx plugins for Python/Go if truly needed later
- **Clean migration**: Delete Bazel skills, update docs, create Nx skills
- **Document trade-off**: This ADR explains why AI integration trumps technical purity

---

## Implementation Impact

### Files to Update

| File | Change |
|------|--------|
| `CLAUDE.md` | Replace Bazel with Nx in Section V |
| `monorepo-orchestrator/SKILL.md` | Route to Nx skills instead of Bazel |
| `monorepo-architecture-guide.md` | Nx as primary standard |

### Skills to Delete (Bazel)

| Skill | Status |
|-------|--------|
| `bazel-navigator` | Delete |
| `bazel-builder` | Delete |
| `bazel-rules` | Delete |
| `bazel-ci` | Delete |

### Skills to Create (Nx)

| Skill | Purpose |
|-------|---------|
| `nx-navigator` | Project graph, affected detection, workspace analysis |
| `nx-builder` | nx.json, project.json, generators, executors |
| `nx-mcp` | MCP server setup, AI agent configuration |
| `nx-ci` | Nx Cloud, GitHub Actions, affected CI |

### Skills Retained (Tool-Agnostic)

| Skill | Reason |
|-------|--------|
| `monorepo-workflow` | PR stacking, trunk-based dev |
| `monorepo-team-lead` | CODEOWNERS, coordination |

---

## Alternatives Considered

### Alternative 1: Keep Bazel, Add MCP Later

**Rejected because**: Community MCP servers are experimental. Official support unlikely given Bazel's enterprise focus on hermetic builds, not AI integration.

### Alternative 2: Use moon Instead

**Rejected because**: moon has official MCP but only 7 tools. Nx provides deeper workspace understanding. moon is also newer with smaller ecosystem.

### Alternative 3: Use Turborepo

**Rejected because**: No MCP support at all (only a feature request). Simpler than Nx but lacks AI integration entirely.

### Alternative 4: No Orchestrator (pnpm Only)

**Rejected because**: Loses affected detection, caching, task orchestration. Too primitive for monorepo at scale.

---

## Quick Reference

### Nx vs Bazel Commands

| Task | Bazel | Nx |
|------|-------|-----|
| Build all | `bazel build //...` | `nx run-many -t build` |
| Test all | `bazel test //...` | `nx run-many -t test` |
| Affected | `bazel query rdeps(...)` | `nx affected -t test` |
| Graph | `bazel query deps(...)` | `nx graph` |
| Cache | `.bazelrc` | `nx.json` |

### Setup for Claude Code

```bash
# Add Nx MCP server
claude mcp add nx-mcp npx nx-mcp@latest

# Or auto-configure
npx nx configure-ai-agents
```

---

## References

- [Nx AI Setup](https://nx.dev/docs/getting-started/ai-setup)
- [Nx Enhance AI Features](https://nx.dev/docs/features/enhance-ai)
- [Bazel MCP Server (Community)](https://github.com/nacgarg/bazel-mcp-server)
- [Turborepo MCP Request](https://github.com/vercel/turborepo/discussions/10130)
- [moonrepo MCP Guide](https://moonrepo.dev/docs/guides/mcp)
- [monorepo.tools](https://monorepo.tools/)
- ADR-0019: Bazel as Monorepo Standard (superseded)
