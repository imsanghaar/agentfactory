# Monorepo Skills Architecture
## Nx-Based AI Engineering Skills

**Version**: 2.0.0
**Status**: Implemented
**Last Updated**: 2025-12-15
**Goal**: Enable Claude Code as AI Coder, AI Engineer, and AI Manager for Nx monorepos

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MONOREPO SKILLS ECOSYSTEM (Nx-Based)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                         MCP LAYER                                    │  │
│   │  nx-mcp server provides: nx_docs, nx_available_plugins              │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                    │                                        │
│                                    ▼                                        │
│      ┌──────────────────────────────────────────────────────────────┐      │
│      │                     NX-MONOREPO SKILL                         │      │
│      │  • Project graph analysis      • Affected detection           │      │
│      │  • Code generation            • Caching & Nx Cloud            │      │
│      │  • CI pipeline design         • Nx CLI expertise              │      │
│      └──────────────────────────────────────────────────────────────┘      │
│                                    │                                        │
│           ┌────────────────────────┴────────────────────────┐              │
│           ▼                                                  ▼              │
│   ┌───────────────────────┐                  ┌───────────────────────┐     │
│   │   MONOREPO-WORKFLOW   │                  │  MONOREPO-TEAM-LEAD   │     │
│   │   (Tool-Agnostic)     │                  │   (Tool-Agnostic)     │     │
│   ├───────────────────────┤                  ├───────────────────────┤     │
│   │ • Trunk-based dev     │                  │ • CODEOWNERS          │     │
│   │ • PR stacking         │                  │ • Human-AI routing    │     │
│   │ • Code review         │                  │ • RFC process         │     │
│   │ • Breaking changes    │                  │ • Team coordination   │     │
│   └───────────────────────┘                  └───────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Design Rationale

### Why 3 Skills Instead of 7?

**Previous Architecture (v1.0)**: 7 Bazel-focused skills
- navigator, builder, ci-architect, workflow, team-lead, platform, orchestrator

**Current Architecture (v2.0)**: 3 skills with MCP integration
- `nx-monorepo` (Nx-specific)
- `monorepo-workflow` (tool-agnostic)
- `monorepo-team-lead` (tool-agnostic)

**Rationale** (ADR-0020):
1. **Nx MCP Server** provides deep workspace understanding via tools
2. **CLI-first approach** - Nx CLI handles operations, MCP handles docs
3. **Tool-agnostic separation** - Workflow and team-lead work with any build tool
4. **No duplication** - MCP provides capabilities, skills provide guidance

---

## Skill Details

### Skill 1: nx-monorepo

**Location**: `.claude/skills/engineering/monorepo/nx-monorepo/SKILL.md`
**Level**: L4 (Expert)
**Roles**: AI Coder, AI Engineer

**MCP Tools Used**:
| Tool | Purpose |
|------|---------|
| `nx_docs` | Query Nx documentation |
| `nx_available_plugins` | List official Nx plugins |

**CLI Commands Covered**:
| Command | Purpose |
|---------|---------|
| `nx graph` | Project graph visualization |
| `nx affected -t <target>` | Affected detection |
| `nx run-many -t <target>` | Parallel task execution |
| `nx g @nx/<plugin>:<generator>` | Code generation |
| `nx show projects` | List projects |
| `nx reset` | Clear cache |

**Capabilities**:
- Project graph analysis and dependency tracking
- Affected detection for CI optimization
- Code generation with Nx generators
- Local and remote caching (Nx Cloud)
- CI/CD pipeline design for monorepos

---

### Skill 2: monorepo-workflow

**Location**: `.claude/skills/engineering/monorepo/monorepo-workflow/SKILL.md`
**Level**: L3-L4 (Proficient-Expert)
**Roles**: AI Coder

**Tool-Agnostic**: Works with Nx, Bazel, Turborepo, or any monorepo tool.

**Capabilities**:
- Trunk-based development principles
- PR stacking workflows (Graphite, manual)
- Code review best practices
- Breaking change management
- Commit conventions

**Key Patterns**:
- Short-lived branches (max 24 hours)
- Feature flags for incomplete work
- Stacked PRs for large changes
- Deprecation protocols

---

### Skill 3: monorepo-team-lead

**Location**: `.claude/skills/engineering/monorepo/monorepo-team-lead/SKILL.md`
**Level**: L4 (Expert)
**Roles**: AI Manager

**Tool-Agnostic**: Organizational patterns independent of build tool.

**Capabilities**:
- CODEOWNERS design and maintenance
- Human-AI task routing decisions
- RFC process management
- Cross-team coordination
- Onboarding protocols

**Decision Matrix** (Human vs AI):
| Task Type | Executor |
|-----------|----------|
| Architecture decisions | Human |
| Breaking changes | Human approval |
| Feature implementation | AI-assisted |
| Lint/format fixes | AI autonomous |
| Documentation | AI-assisted |

---

## MCP Integration

### Available Tools

The `nx-mcp` server provides two tools:

```
nx_docs(userQuery: string)
  - Queries Nx documentation
  - Returns relevant docs sections
  - Use for: "How do I configure caching?", "What generators are available?"

nx_available_plugins()
  - Lists official @nx/* plugins
  - Shows descriptions and capabilities
  - Use for: "What plugins can I add?", "Does Nx support Vue?"
```

### CLI vs MCP

| Task | Use |
|------|-----|
| Documentation lookup | `nx_docs` MCP tool |
| Plugin discovery | `nx_available_plugins` MCP tool |
| Build operations | `nx build`, `nx test` CLI |
| Graph analysis | `nx graph`, `nx affected` CLI |
| Code generation | `nx g @nx/...` CLI |
| Cache operations | `nx reset`, `--skip-nx-cache` CLI |

---

## Skill Coverage Matrix

| Capability | nx-monorepo | workflow | team-lead |
|------------|-------------|----------|-----------|
| Project graph | ✅ | | |
| Affected detection | ✅ | | |
| Code generation | ✅ | | |
| Caching | ✅ | | |
| CI/CD | ✅ | | |
| Trunk-based dev | | ✅ | |
| PR stacking | | ✅ | |
| Code review | | ✅ | |
| Breaking changes | | ✅ | |
| CODEOWNERS | | | ✅ |
| Task routing | | | ✅ |
| RFC process | | | ✅ |
| Onboarding | | | ✅ |

---

## Success Criteria

Claude Code with these skills should:

### As AI Coder
- [x] Navigate any Nx monorepo structure
- [x] Run affected-only commands correctly
- [x] Create PRs with proper descriptions
- [x] Respect dependency boundaries

### As AI Engineer
- [x] Generate new apps/libs with Nx generators
- [x] Configure caching for optimal performance
- [x] Design CI pipelines with affected detection
- [x] Debug cache misses

### As AI Manager
- [x] Route tasks to human vs AI correctly
- [x] Design CODEOWNERS for team structure
- [x] Identify escalation triggers
- [x] Coordinate cross-domain work

---

## Migration from v1.0

| Old Skill (Bazel) | New Skill (Nx) |
|-------------------|----------------|
| bazel-navigator | nx-monorepo |
| bazel-builder | nx-monorepo |
| bazel-rules | nx-monorepo |
| bazel-ci | nx-monorepo |
| monorepo-orchestrator | Removed (MCP handles routing) |
| monorepo-workflow | monorepo-workflow (unchanged) |
| monorepo-team-lead | monorepo-team-lead (unchanged) |

**Why orchestrator removed**: The nx-mcp server provides workspace understanding. No meta-skill needed to route between specialized skills when there's one comprehensive skill plus MCP.

---

## References

- [ADR-0020: Nx as Monorepo Standard](../history/adr/0020-nx-as-monorepo-standard-superseding-bazel.md)
- [Nx AI Setup](https://nx.dev/docs/getting-started/ai-setup)
- [Nx MCP Integration](https://nx.dev/docs/features/enhance-ai)
