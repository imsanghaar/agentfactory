---
id: "0165"
title: "Nx Monorepo Standard ADR Creation"
stage: general
feature: null
date: 2025-12-15
model: claude-opus-4-5-20251101
tokens_in: ~15000
tokens_out: ~3000
---

# Nx Monorepo Standard ADR Creation

## Prompt

User invoked `/sp.adr` with context:

> Given above research we have standardized to "NX" for monorepo

This followed a comprehensive research session comparing monorepo orchestrators (Nx, Bazel, moon, Turborepo) with focus on AI/MCP integration capabilities.

## Response Summary

Created ADR-0020: Nx as Monorepo Standard (Superseding Bazel)

### Key Decisions Documented

1. **Primary Decision**: Adopt Nx over Bazel for AI-native education platform

2. **Rationale**:
   - Nx has official MCP server with deep workspace understanding
   - Bazel has only community MCP servers with basic capabilities
   - Platform is TypeScript/Next.js-first (Nx native ecosystem)
   - 5-minute setup vs 3-6 month Bazel learning curve
   - Nx auto-generates CLAUDE.md and AGENTS.md for AI assistants

3. **MCP Capability Gap**:
   | Capability | Nx MCP | Bazel MCP |
   |------------|--------|-----------|
   | Workspace analysis | Deep | None |
   | Project graph | Visual | Query only |
   | CI integration | Full | None |
   | Code generation | Scaffolding | None |

4. **Trade-offs Accepted**:
   - No hermetic builds (acceptable for education)
   - No distributed execution (scale not needed)
   - Polyglot via plugins not native (acceptable)

### Files Changed

- Created: `history/adr/0020-nx-as-monorepo-standard-superseding-bazel.md`
- Updated: `history/adr/0019-bazel-as-monorepo-standard-over-turborepo.md` (Status → Superseded)

### Next Steps

- Delete Bazel skills (bazel-navigator, bazel-builder, bazel-rules, bazel-ci)
- Create Nx skills (nx-navigator, nx-builder, nx-mcp, nx-ci)
- Update CLAUDE.md Section V
- Update monorepo-orchestrator routing
- Update monorepo-architecture-guide.md

## Lessons Learned

1. **AI integration trumps technical purity**: Bazel is technically superior but Nx provides better AI agent integration, which matters more for this platform.

2. **MCP is the differentiator**: Official MCP server support is a key factor for AI-native development.

3. **Research before implementation**: The initial Bazel decision was made without researching MCP integration. Fresh research revealed the critical gap.
