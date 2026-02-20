# Monorepo Engineering Skills Matrix
## Competency Framework from Setup to Mastery

**Version**: 1.0.0
**Status**: Draft - Starting Point for Discussion
**Last Updated**: 2025-12-15
**Related**: [Monorepo Architecture Guide](./monorepo-architecture-guide.md)

---

## Table of Contents

1. [Overview](#overview)
2. [Skill Categories](#skill-categories)
3. [Competency Levels](#competency-levels)
4. [Complete Skills Matrix](#complete-skills-matrix)
5. [Role-Based Requirements](#role-based-requirements)
6. [AI Agent Requirements](#ai-agent-requirements)
7. [Human Manager Requirements](#human-manager-requirements)
8. [Human-AI Collaboration Model](#human-ai-collaboration-model)
9. [Onboarding Progression](#onboarding-progression)
10. [Assessment Rubrics](#assessment-rubrics)
11. [Learning Paths](#learning-paths)

---

## Overview

### Purpose

This matrix defines the skills required for engineers to effectively work in a monorepo environment. It serves as:

- **Hiring guide**: What to assess in candidates
- **Onboarding checklist**: What new joiners must learn
- **Growth framework**: How engineers level up
- **Gap analysis**: What training investments to make

### Proficiency Scale

| Level | Code | Description |
|-------|------|-------------|
| **Awareness** | L0 | Knows it exists, can recognize it |
| **Beginner** | L1 | Can do with guidance, follows documentation |
| **Competent** | L2 | Can do independently, handles common cases |
| **Proficient** | L3 | Can handle edge cases, teaches others |
| **Expert** | L4 | Designs systems, defines best practices |

---

## Skill Categories

### Category Map

```
┌─────────────────────────────────────────────────────────────────┐
│                    MONOREPO ENGINEERING SKILLS                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   CORE      │  │   BUILD     │  │    CI/CD    │             │
│  │   (C)       │  │   (B)       │  │    (P)      │             │
│  │             │  │             │  │             │             │
│  │ Git         │  │ Turborepo   │  │ GitHub      │             │
│  │ Workspaces  │  │ Nx          │  │ Actions     │             │
│  │ Dependencies│  │ Caching     │  │ Pipelines   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  WORKFLOW   │  │   TEAM      │  │     AI      │             │
│  │   (W)       │  │   (T)       │  │    (A)      │             │
│  │             │  │             │  │             │             │
│  │ Trunk-based │  │ Ownership   │  │ Agents      │             │
│  │ PR Stacking │  │ Code Review │  │ Delegation  │             │
│  │ Branching   │  │ Onboarding  │  │ Prompting   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐                              │
│  │  PLATFORM   │  │   DOMAIN    │                              │
│  │   (X)       │  │   (D)       │                              │
│  │             │  │             │                              │
│  │ DevEx       │  │ TypeScript  │                              │
│  │ Tooling     │  │ Python      │                              │
│  │ Automation  │  │ Framework   │                              │
│  └─────────────┘  └─────────────┘                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Competency Levels

### Engineer Levels

| Level | Title | Years* | Primary Focus |
|-------|-------|--------|---------------|
| **E1** | Junior Engineer | 0-2 | Execute tasks within domain |
| **E2** | Engineer | 2-4 | Independent domain work |
| **E3** | Senior Engineer | 4-7 | Cross-domain, mentoring |
| **E4** | Staff Engineer | 7-10 | Architecture, standards |
| **E5** | Principal Engineer | 10+ | Strategy, organization-wide |

*Years are indicative, not strict requirements

---

## Complete Skills Matrix

### C: Core Monorepo Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **C.1** | **Git Fundamentals** |
| C.1.1 | Clone, pull, push | Know commands exist | Execute basic commands | Handle conflicts | Rebase complex histories | Design branching strategies |
| C.1.2 | Branch management | Know branches exist | Create/switch branches | Manage feature branches | Clean up stale branches | Enforce branch policies |
| C.1.3 | Merge vs Rebase | Know difference | Use merge | Choose appropriately | Resolve complex rebases | Define team standards |
| C.1.4 | Git hooks | Know they exist | Use pre-configured | Configure hooks | Create custom hooks | Design hook systems |
| **C.2** | **Monorepo Git** |
| C.2.1 | Sparse checkout | Know concept | Enable for project | Configure patterns | Optimize for large repos | Design sparse strategies |
| C.2.2 | Partial clone | Know concept | Use shallow clone | Choose depth strategy | Optimize CI clones | Scale clone strategies |
| C.2.3 | Git LFS | Know purpose | Track files | Configure .gitattributes | Migrate existing files | Design LFS policies |
| C.2.4 | Monorepo-specific commands | Know they're different | Use basic commands | Use `--filter` flags | Optimize performance | Contribute to tooling |
| **C.3** | **Package Management** |
| C.3.1 | Workspace concept | Know what it is | Navigate workspaces | Configure workspace | Design workspace structure | Optimize workspace perf |
| C.3.2 | pnpm/npm/yarn | Know differences | Use one tool | Configure for monorepo | Migrate between tools | Evaluate tooling |
| C.3.3 | Dependency resolution | Know deps exist | Add dependencies | Resolve conflicts | Debug resolution issues | Design dep strategies |
| C.3.4 | Workspace protocol | Know `workspace:*` | Use in package.json | Configure properly | Debug linking issues | Design version strategies |
| **C.4** | **Dependency Graph** |
| C.4.1 | Understand dep graph | Know concept | Read visualizations | Trace dependencies | Optimize graph | Design graph architecture |
| C.4.2 | Circular deps | Know they're bad | Identify cycles | Break cycles | Prevent cycles | Enforce via tooling |
| C.4.3 | Boundary enforcement | Know boundaries exist | Respect boundaries | Configure rules | Fix violations | Design boundary systems |
| C.4.4 | Affected analysis | Know concept | Run affected commands | Interpret results | Optimize detection | Build affected tools |

### B: Build & Task Orchestration Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **B.1** | **Build Tools** |
| B.1.1 | Turborepo basics | Know it exists | Run turbo commands | Configure turbo.json | Optimize pipelines | Design build systems |
| B.1.2 | Nx basics | Know it exists | Run nx commands | Configure nx.json | Use generators | Extend Nx plugins |
| B.1.3 | Task dependencies | Know ^build syntax | Configure deps | Debug dep issues | Optimize DAG | Design task graphs |
| B.1.4 | Task inputs/outputs | Know concept | Configure basic | Fine-tune caching | Debug cache misses | Design cache strategies |
| **B.2** | **Caching** |
| B.2.1 | Local caching | Know it exists | Benefit from cache | Debug cache issues | Optimize hit rate | Design cache architecture |
| B.2.2 | Remote caching | Know concept | Connect to remote | Configure team cache | Debug remote issues | Manage cache infra |
| B.2.3 | Cache invalidation | Know it's hard | Clear cache manually | Configure inputs | Debug stale cache | Design invalidation |
| B.2.4 | Cache keys | Know concept | Use defaults | Customize keys | Debug key collisions | Optimize key strategy |
| **B.3** | **Build Performance** |
| B.3.1 | Parallel execution | Know concept | Use parallelism | Configure concurrency | Profile bottlenecks | Optimize parallelism |
| B.3.2 | Incremental builds | Know benefit | Use incremental | Configure properly | Debug issues | Design incremental |
| B.3.3 | Build profiling | Know to profile | Run with --profile | Interpret results | Identify bottlenecks | Optimize build times |
| B.3.4 | Distributed execution | Know concept | Use if available | Configure distribution | Debug distribution | Architect distribution |

### P: CI/CD Pipeline Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **P.1** | **CI Fundamentals** |
| P.1.1 | GitHub Actions | Know it exists | Read workflows | Write simple workflows | Complex workflows | Design CI architecture |
| P.1.2 | CI triggers | Know triggers exist | Use push/PR | Configure conditions | Optimize triggers | Design trigger strategy |
| P.1.3 | Job parallelism | Know concept | Use matrix | Configure properly | Optimize parallelism | Design job strategy |
| P.1.4 | Secrets management | Know to use secrets | Use existing secrets | Configure secrets | Rotate secrets | Design secrets strategy |
| **P.2** | **Monorepo CI** |
| P.2.1 | Affected-only CI | Know concept | Use affected filter | Configure detection | Optimize detection | Design affected system |
| P.2.2 | Path filtering | Know concept | Use paths-filter | Configure patterns | Debug filter issues | Design filter strategy |
| P.2.3 | CI caching | Know concept | Use cache actions | Configure cache keys | Debug cache issues | Optimize CI cache |
| P.2.4 | Monorepo matrix | Know concept | Use basic matrix | Dynamic matrix | Debug matrix issues | Design matrix strategy |
| **P.3** | **CD & Deployment** |
| P.3.1 | Deployment workflows | Know concept | Trigger deployments | Configure per-app | Coordinate deploys | Design deploy strategy |
| P.3.2 | Environment promotion | Know concept | Use staging/prod | Configure environments | Debug env issues | Design env strategy |
| P.3.3 | Rollback procedures | Know concept | Execute rollback | Configure rollback | Test rollbacks | Design rollback strategy |
| P.3.4 | Feature flags | Know concept | Use existing flags | Create new flags | Debug flag issues | Design flag system |
| **P.4** | **Advanced CI** |
| P.4.1 | Merge queues | Know concept | Use merge queue | Configure queue | Debug queue issues | Design queue strategy |
| P.4.2 | Self-healing CI | Know concept | Use if available | Configure self-heal | Debug healing | Design self-heal |
| P.4.3 | CI observability | Know concept | Read dashboards | Configure metrics | Debug performance | Design CI observability |
| P.4.4 | Cost optimization | Know CI costs | Track costs | Optimize costs | Reduce significantly | Design cost strategy |

### W: Workflow & Collaboration Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **W.1** | **Trunk-Based Development** |
| W.1.1 | TBD principles | Know concept | Follow TBD | Practice consistently | Advocate TBD | Define TBD standards |
| W.1.2 | Short-lived branches | Know goal | Keep < 1 day | Consistently short | Help others shorten | Enforce via policy |
| W.1.3 | Feature flags | Know purpose | Use existing | Create flags | Complex flag logic | Design flag strategy |
| W.1.4 | Continuous integration | Know concept | Commit frequently | CI mindset | Coach others | Design CI culture |
| **W.2** | **PR Stacking** |
| W.2.1 | Stacking concept | Know what it is | Read stacked PRs | Create simple stacks | Complex stacks | Design stack workflow |
| W.2.2 | Graphite/similar tools | Know they exist | Use basic commands | Full workflow | Debug issues | Evaluate tools |
| W.2.3 | Stack management | Know challenges | Keep stacks small | Manage rebases | Help others | Design stack policies |
| W.2.4 | Stack review | Know it's different | Review stacked PRs | Efficient review | Coach reviewers | Design review process |
| **W.3** | **Code Review** |
| W.3.1 | PR creation | Know process | Create basic PRs | Good descriptions | Exemplary PRs | Define PR standards |
| W.3.2 | Review giving | Know to review | Review basics | Thorough reviews | Mentoring reviews | Design review process |
| W.3.3 | Review receiving | Know to respond | Respond to feedback | Graceful iteration | Coach receivers | Define response norms |
| W.3.4 | Cross-domain review | Know it's harder | Review own domain | Review adjacent | Review any domain | Design cross-review |
| **W.4** | **Change Management** |
| W.4.1 | Breaking changes | Know danger | Avoid breaking | Manage carefully | Plan migrations | Design BC strategy |
| W.4.2 | Deprecation | Know concept | Use @deprecated | Add warnings | Migration guides | Design deprecation |
| W.4.3 | Versioning | Know semver | Apply correctly | Independent versions | Version strategy | Design version policy |
| W.4.4 | Changelog | Know purpose | Update changelog | Comprehensive logs | Automated logs | Design log strategy |

### T: Team & Organization Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **T.1** | **Code Ownership** |
| T.1.1 | CODEOWNERS | Know it exists | Find owners | Update ownership | Design ownership | Define ownership policy |
| T.1.2 | Domain boundaries | Know they exist | Respect boundaries | Clarify boundaries | Enforce boundaries | Design domains |
| T.1.3 | Cross-team collab | Know it's needed | Collaborate | Facilitate collab | Lead cross-team | Design collab patterns |
| T.1.4 | Escalation paths | Know they exist | Follow paths | Navigate paths | Define paths | Design escalation |
| **T.2** | **Documentation** |
| T.2.1 | README standards | Know to write | Write basic | Comprehensive READMEs | Exemplary docs | Define doc standards |
| T.2.2 | Architecture docs | Know purpose | Read ADRs | Write ADRs | Complex ADRs | Design ADR process |
| T.2.3 | Runbooks | Know purpose | Follow runbooks | Write runbooks | Maintain runbooks | Design runbook system |
| T.2.4 | API documentation | Know importance | Document APIs | Comprehensive API docs | Auto-gen docs | Design API doc system |
| **T.3** | **Onboarding** |
| T.3.1 | Self-onboarding | Know to onboard | Follow docs | Onboard quickly | Improve docs | Design onboarding |
| T.3.2 | Buddy system | Know it helps | Be a good buddy | Effective mentoring | Train buddies | Design buddy program |
| T.3.3 | First PR experience | Know importance | Smooth first PR | Guide first PRs | Coach guides | Design first PR |
| T.3.4 | Knowledge transfer | Know importance | Transfer basics | Effective transfer | Systematic transfer | Design KT process |
| **T.4** | **Communication** |
| T.4.1 | Async communication | Know importance | Use effectively | Optimize async | Coach others | Design async culture |
| T.4.2 | RFC process | Know what RFC is | Read RFCs | Write RFCs | Review RFCs | Design RFC process |
| T.4.3 | Incident response | Know process | Participate | Lead incidents | Improve process | Design incident mgmt |
| T.4.4 | Retrospectives | Know purpose | Participate | Lead retros | Action items | Design retro process |

### A: AI Collaboration Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **A.1** | **AI Code Assistants** |
| A.1.1 | Copilot/Claude Code | Know they exist | Basic usage | Effective prompting | Complex workflows | Evaluate AI tools |
| A.1.2 | Context management | Know context matters | Provide context | Optimize context | Design context | Build context systems |
| A.1.3 | Output validation | Know to validate | Check outputs | Systematic validation | Teach validation | Design validation |
| A.1.4 | AI limitations | Know limitations | Work around | Anticipate limits | Coach others | Design for limits |
| **A.2** | **AI Agents** |
| A.2.1 | Agent concepts | Know what agents are | Use basic agents | Configure agents | Design agents | Architect agent systems |
| A.2.2 | Task delegation | Know to delegate | Delegate simple tasks | Complex delegation | Optimize delegation | Design delegation |
| A.2.3 | Agent skills | Know skills exist | Use existing skills | Create simple skills | Complex skills | Design skill systems |
| A.2.4 | Human-AI handoffs | Know handoffs | Execute handoffs | Smooth handoffs | Coach handoffs | Design handoff process |
| **A.3** | **AI-Assisted Workflows** |
| A.3.1 | AI code review | Know concept | Use AI review | Configure review | Evaluate effectiveness | Design AI review |
| A.3.2 | AI refactoring | Know concept | Use AI refactor | Large refactors | Coach usage | Design refactor workflow |
| A.3.3 | AI documentation | Know concept | Generate docs | Edit AI docs | Coach usage | Design doc workflow |
| A.3.4 | AI testing | Know concept | Generate tests | Validate AI tests | Coach usage | Design test workflow |
| **A.4** | **Prompt Engineering** |
| A.4.1 | Prompt basics | Know prompts matter | Write basic prompts | Effective prompts | Complex prompts | Design prompt systems |
| A.4.2 | Structured prompts | Know concept | Use templates | Create templates | Design templates | Build prompt libraries |
| A.4.3 | Few-shot prompting | Know concept | Use examples | Effective examples | Design examples | Build example libraries |
| A.4.4 | Chain prompting | Know concept | Simple chains | Complex chains | Debug chains | Design chain systems |

### X: Platform Engineering Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **X.1** | **Developer Experience** |
| X.1.1 | DevEx mindset | Know concept | Appreciate DevEx | Improve DevEx | Champion DevEx | Design DevEx |
| X.1.2 | Self-service tools | Know they help | Use tools | Request improvements | Build tools | Design tool platform |
| X.1.3 | Golden paths | Know concept | Follow paths | Document paths | Create paths | Design path strategy |
| X.1.4 | Cognitive load | Know it matters | Reduce own load | Reduce team load | Measure load | Design for low load |
| **X.2** | **Tooling** |
| X.2.1 | CLI tools | Know they exist | Use CLIs | Configure CLIs | Build simple CLIs | Design CLI architecture |
| X.2.2 | IDE integration | Know integrations | Use effectively | Configure workspace | Share configs | Design IDE strategy |
| X.2.3 | Linting/formatting | Know purpose | Use configured | Configure rules | Design rulesets | Manage lint systems |
| X.2.4 | TypeScript config | Know tsconfig | Use project config | Configure correctly | Debug complex | Design TS strategy |
| **X.3** | **Automation** |
| X.3.1 | Scripting | Know value | Run scripts | Write scripts | Maintain scripts | Design script systems |
| X.3.2 | Generators | Know concept | Use generators | Configure generators | Create generators | Design generator system |
| X.3.3 | Codemods | Know concept | Run codemods | Write simple codemods | Complex codemods | Design codemod system |
| X.3.4 | Bot automation | Know bots exist | Interact with bots | Configure bots | Create bots | Design bot ecosystem |
| **X.4** | **Observability** |
| X.4.1 | Build metrics | Know metrics exist | Read dashboards | Interpret metrics | Create dashboards | Design metrics system |
| X.4.2 | DX metrics | Know metrics exist | Track own DX | Contribute data | Analyze DX | Design DX measurement |
| X.4.3 | Cost tracking | Know costs matter | Awareness | Track team costs | Optimize costs | Design cost visibility |
| X.4.4 | Incident detection | Know to detect | Notice issues | Report effectively | Debug platform | Design detection |

### D: Domain-Specific Skills

| Skill ID | Skill | L0 | L1 | L2 | L3 | L4 |
|----------|-------|----|----|----|----|-----|
| **D.1** | **TypeScript/JavaScript** |
| D.1.1 | TypeScript | Know basics | Write TS | Advanced TS | Type system expert | Design type strategy |
| D.1.2 | Node.js | Know basics | Write Node | Advanced Node | Performance expert | Architect Node apps |
| D.1.3 | Package publishing | Know npm | Use packages | Publish packages | Manage releases | Design publish system |
| D.1.4 | Framework (Next.js, etc.) | Know framework | Build apps | Advanced patterns | Framework expert | Architect framework |
| **D.2** | **Python** |
| D.2.1 | Python basics | Know basics | Write Python | Advanced Python | Python expert | Architect Python |
| D.2.2 | uv/Poetry | Know they exist | Use package mgr | Configure properly | Debug issues | Design Python deps |
| D.2.3 | Testing (pytest) | Know to test | Write tests | Advanced testing | Test architecture | Design test strategy |
| D.2.4 | Type hints | Know they exist | Use hints | Comprehensive hints | Strict typing | Design type strategy |
| **D.3** | **Polyglot** |
| D.3.1 | Cross-language types | Know challenge | Use generated | Configure generation | Debug generation | Design type sharing |
| D.3.2 | Multi-runtime CI | Know challenge | Use existing CI | Configure multi | Debug issues | Design multi-runtime |
| D.3.3 | Shared tooling | Know benefits | Use shared tools | Configure for lang | Adapt tooling | Design polyglot tools |
| D.3.4 | Language boundaries | Know boundaries | Respect boundaries | Define boundaries | Enforce boundaries | Design lang strategy |

---

## Role-Based Requirements

### Minimum Skill Requirements by Level

#### E1: Junior Engineer

| Category | Required Skills at L1+ | Required Skills at L2+ |
|----------|------------------------|------------------------|
| **Core (C)** | C.1.1, C.1.2, C.3.1, C.3.2 | None |
| **Build (B)** | B.1.1 or B.1.2 | None |
| **Pipeline (P)** | P.1.1 | None |
| **Workflow (W)** | W.1.1, W.3.1, W.3.2, W.3.3 | None |
| **Team (T)** | T.2.1, T.3.1 | None |
| **AI (A)** | A.1.1, A.1.3 | None |
| **Platform (X)** | X.2.1, X.2.2 | None |
| **Domain (D)** | D.1.1 or D.2.1 | None |

**Summary**: Can clone, build, make changes in their domain, submit PRs, use AI assistants.

---

#### E2: Engineer

| Category | Required Skills at L1+ | Required Skills at L2+ |
|----------|------------------------|------------------------|
| **Core (C)** | All C.1.x, C.2.1, All C.3.x | C.1.1, C.1.2, C.3.1, C.3.3 |
| **Build (B)** | All B.1.x, B.2.1, B.2.2 | B.1.1, B.1.3 |
| **Pipeline (P)** | All P.1.x, P.2.1, P.2.2 | P.1.1, P.1.2 |
| **Workflow (W)** | All W.1.x, All W.3.x, W.4.1 | W.1.1, W.3.1, W.3.2 |
| **Team (T)** | All T.1.x, T.2.1, T.2.2, T.3.1, T.3.2 | T.1.1, T.2.1 |
| **AI (A)** | All A.1.x, A.2.1, A.2.2 | A.1.1, A.1.2 |
| **Platform (X)** | All X.2.x, X.3.1 | X.2.1, X.2.2 |
| **Domain (D)** | All D.1.x or All D.2.x | D.1.1-D.1.3 or D.2.1-D.2.3 |

**Summary**: Independent contributor, understands monorepo concepts, effective AI collaboration, owns domain work.

---

#### E3: Senior Engineer

| Category | Required Skills at L2+ | Required Skills at L3+ |
|----------|------------------------|------------------------|
| **Core (C)** | All C.x.x | C.1.3, C.3.3, C.4.1, C.4.2 |
| **Build (B)** | All B.1.x, All B.2.x | B.1.1, B.2.1, B.2.3 |
| **Pipeline (P)** | All P.1.x, All P.2.x | P.1.1, P.2.1 |
| **Workflow (W)** | All W.x.x | W.1.1, W.2.1, W.3.2, W.4.1, W.4.2 |
| **Team (T)** | All T.x.x | T.1.1, T.1.2, T.2.2, T.3.2, T.4.2 |
| **AI (A)** | All A.1.x, All A.2.x, A.3.1, A.3.2 | A.1.1, A.2.2, A.2.3 |
| **Platform (X)** | All X.1.x, All X.2.x, X.3.1, X.3.2 | X.1.1, X.1.4, X.3.1 |
| **Domain (D)** | All primary language | Primary language L3 |

**Summary**: Cross-domain work, mentors juniors, designs AI agent skills, leads RFCs, handles breaking changes.

---

#### E4: Staff Engineer

| Category | Required Skills at L3+ | Required Skills at L4+ |
|----------|------------------------|------------------------|
| **Core (C)** | All C.x.x | C.3.4, C.4.3 |
| **Build (B)** | All B.x.x | B.1.4, B.2.4 |
| **Pipeline (P)** | All P.x.x | P.2.1, P.4.1 |
| **Workflow (W)** | All W.x.x | W.1.4, W.2.4, W.4.4 |
| **Team (T)** | All T.x.x | T.1.4, T.2.4, T.4.4 |
| **AI (A)** | All A.x.x | A.2.4, A.4.4 |
| **Platform (X)** | All X.x.x | X.1.4, X.3.4 |
| **Domain (D)** | All D.x.x | Primary language L4 |

**Summary**: Defines standards, architects systems, designs AI agent architecture, leads org-wide initiatives.

---

#### E5: Principal Engineer

| Category | Requirements |
|----------|--------------|
| **All Categories** | L3+ across all, L4+ in majority |
| **Special** | Defines organizational strategy, industry recognition |

**Summary**: Organization-wide impact, defines monorepo strategy, builds next-gen tooling.

---

## AI Agent Requirements

### The Implication

Every AI coding agent (Claude Code, Codex CLI, Cursor, Copilot Workspace, Devin, etc.) that operates in a monorepo environment **must effectively be a master of ALL these skills** to be truly useful.

This is a fundamental insight: AI agents are not junior developers who can learn on the job. They either have the skills or they don't. An AI agent operating at L1-L2 across these skills will produce problematic code that humans must constantly fix.

### AI Agent Skill Requirements

| Category | Minimum Level | Rationale |
|----------|---------------|-----------|
| **C: Core Monorepo** | L3-L4 | Must understand dependency graphs, workspace protocols, affected analysis without human guidance |
| **B: Build & Tasks** | L3-L4 | Must configure builds correctly, understand caching, optimize task pipelines |
| **P: CI/CD** | L3 | Must understand affected-only CI, write correct workflow files, debug failures |
| **W: Workflow** | L2-L3 | Must follow trunk-based development, create proper PRs, handle breaking changes |
| **T: Team** | L2 | Must understand ownership, write documentation, follow team protocols |
| **A: AI Collaboration** | N/A | This IS the AI agent |
| **X: Platform** | L3-L4 | Must understand and improve DevEx, write automation, create tooling |
| **D: Domain** | L3-L4 | Must be expert in languages used (TypeScript, Python, etc.) |

### AI Agent Capability Matrix

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    AI AGENT CAPABILITY REQUIREMENTS                        │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  MUST BE AUTONOMOUS (No human guidance needed)                             │
│  ─────────────────────────────────────────────                             │
│  • Navigate monorepo structure                                             │
│  • Identify affected packages from changes                                 │
│  • Run correct build/test commands                                         │
│  • Resolve dependency conflicts                                            │
│  • Write correct CI configurations                                         │
│  • Generate proper commit messages                                         │
│  • Create well-structured PRs                                              │
│  • Understand and respect CODEOWNERS                                       │
│  • Handle cross-package refactoring                                        │
│  • Debug build failures                                                    │
│  • Optimize caching strategies                                             │
│                                                                            │
│  MUST ASK HUMANS (Cannot be autonomous)                                    │
│  ─────────────────────────────────────────                                 │
│  • Architecture decisions                                                  │
│  • Breaking change approval                                                │
│  • Cross-domain coordination                                               │
│  • Production deployment decisions                                         │
│  • Security-critical changes                                               │
│  • Team/organizational decisions                                           │
│  • New dependency additions                                                │
│  • API design choices                                                      │
│                                                                            │
│  SHOULD PROACTIVELY DO (Without being asked)                               │
│  ───────────────────────────────────────────────                           │
│  • Run affected tests before committing                                    │
│  • Check for circular dependencies                                         │
│  • Validate against CODEOWNERS                                             │
│  • Update documentation when changing code                                 │
│  • Add deprecation warnings for breaking changes                           │
│  • Suggest PR stacking for large changes                                   │
│  • Warn about cache invalidation impact                                    │
│  • Flag potential security issues                                          │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

### AI Agent Evaluation Criteria

When evaluating an AI coding agent for monorepo work, test these scenarios:

| Test Scenario | Expected Behavior | Failure Mode |
|---------------|-------------------|--------------|
| "Add a function to shared package" | Identifies dependents, runs affected tests | Changes only the file, breaks dependents |
| "Rename this function across repo" | Uses codemod/refactor, updates all usages | Misses usages, creates broken references |
| "Fix this failing CI" | Reads workflow, identifies root cause | Tries random fixes, doesn't understand CI |
| "Create a new package" | Follows workspace conventions, updates configs | Creates incompatible structure |
| "This change needs to go to 3 packages" | Suggests atomic commit or stacked PRs | Creates 3 separate PRs that can break |
| "Debug why cache isn't working" | Checks inputs/outputs, cache keys | Has no understanding of caching |
| "Update this deprecated dependency" | Checks affected packages, runs tests | Updates one place, breaks others |

### AI Agent Skill Gaps (Common Problems)

```yaml
common_ai_agent_failures:

  dependency_blindness:
    symptom: "Changes package without checking dependents"
    required_skill: "C.4.1 Understand dep graph (L3+)"
    fix: "AI must query dependency graph before any package change"

  ci_ignorance:
    symptom: "Doesn't know how to run or interpret CI"
    required_skill: "P.2.1 Affected-only CI (L3)"
    fix: "AI must understand workflow files and affected detection"

  workspace_confusion:
    symptom: "Creates files in wrong locations, breaks workspace"
    required_skill: "C.3.1 Workspace concept (L3)"
    fix: "AI must understand workspace structure before writing files"

  cache_unawareness:
    symptom: "Changes break caching, slow builds"
    required_skill: "B.2.x Caching skills (L3)"
    fix: "AI must understand input/output declarations"

  ownership_violation:
    symptom: "Modifies code outside assigned domain"
    required_skill: "T.1.1-T.1.2 Ownership (L2)"
    fix: "AI must check CODEOWNERS before modifying files"

  breaking_change_blindness:
    symptom: "Makes breaking changes without migration"
    required_skill: "W.4.1-W.4.2 Breaking changes (L3)"
    fix: "AI must detect API changes and suggest migration path"
```

---

## Human Manager Requirements

### The Manager's Role in AI-Augmented Monorepo

Human managers overseeing monorepo work (whether done by humans, AI agents, or both) need a **different but overlapping skill set**. They must:

1. **Understand** all technical skills (to evaluate work)
2. **Not necessarily execute** all skills (AI/engineers do that)
3. **Make judgment calls** AI cannot make
4. **Design systems** for human-AI collaboration

### Manager Skill Requirements

| Category | Required Level | Focus Area |
|----------|----------------|------------|
| **C: Core Monorepo** | L2-L3 | Understand concepts, evaluate decisions |
| **B: Build & Tasks** | L2 | Understand performance, approve investments |
| **P: CI/CD** | L2-L3 | Evaluate pipeline health, approve changes |
| **W: Workflow** | L3-L4 | Define standards, resolve conflicts |
| **T: Team** | L4 | Design ownership, lead cross-team work |
| **A: AI Collaboration** | L3-L4 | Design AI delegation, evaluate AI work |
| **X: Platform** | L2-L3 | Prioritize DevEx investments |
| **D: Domain** | L2 | Enough to evaluate, not necessarily execute |

### Manager-Specific Competencies

| Skill ID | Skill | Description | Level Required |
|----------|-------|-------------|----------------|
| **M.1** | **AI Work Evaluation** |
| M.1.1 | Evaluate AI output quality | Recognize when AI code is subtly wrong | L3 |
| M.1.2 | AI task scoping | Know which tasks to delegate to AI | L3 |
| M.1.3 | AI failure detection | Identify when AI is stuck/looping | L3 |
| M.1.4 | AI capability assessment | Evaluate which AI tools to adopt | L4 |
| **M.2** | **Human-AI Orchestration** |
| M.2.1 | Task routing | Decide human vs AI for each task | L3 |
| M.2.2 | Hybrid workflows | Design workflows mixing human + AI | L4 |
| M.2.3 | Escalation design | Define when AI should ask human | L4 |
| M.2.4 | Quality gates | Define review requirements for AI work | L4 |
| **M.3** | **Monorepo Governance** |
| M.3.1 | Ownership design | Define and evolve CODEOWNERS | L4 |
| M.3.2 | Standards definition | Define coding/workflow standards | L4 |
| M.3.3 | Breaking change policy | Design BC process | L4 |
| M.3.4 | Tooling decisions | Choose build tools, CI systems | L4 |
| **M.4** | **Team Development** |
| M.4.1 | Skill gap analysis | Identify team skill gaps | L4 |
| M.4.2 | Training investment | Prioritize learning initiatives | L4 |
| M.4.3 | AI skill building | Help team use AI effectively | L4 |
| M.4.4 | Career pathing | Guide engineers through levels | L4 |

### Manager Decision Framework

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    MANAGER DECISION AUTHORITY                              │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  MANAGER MUST DECIDE (Cannot delegate to AI or junior engineers)          │
│  ───────────────────────────────────────────────────────────────           │
│  • Architecture and system design                                          │
│  • Breaking change approval                                                │
│  • New technology adoption                                                 │
│  • Cross-team coordination                                                 │
│  • Production incident response                                            │
│  • Security vulnerability response                                         │
│  • Team structure and ownership                                            │
│  • Performance and promotion decisions                                     │
│  • Vendor and tool selection                                               │
│  • Budget allocation                                                       │
│                                                                            │
│  MANAGER SHOULD DELEGATE (But must review)                                 │
│  ─────────────────────────────────────────────                             │
│  • Feature implementation (to engineers/AI)                                │
│  • Code review (to senior engineers/AI)                                    │
│  • Documentation (to AI with review)                                       │
│  • Refactoring (to AI with review)                                         │
│  • Test writing (to AI with review)                                        │
│  • CI/CD improvements (to platform engineers)                              │
│  • Onboarding (to senior engineers)                                        │
│                                                                            │
│  MANAGER SHOULD AUTOMATE (Via AI/tooling)                                  │
│  ─────────────────────────────────────────────                             │
│  • Dependency updates                                                      │
│  • Security scanning                                                       │
│  • Code formatting                                                         │
│  • Lint fixes                                                              │
│  • Simple bug fixes                                                        │
│  • Documentation updates                                                   │
│  • PR descriptions                                                         │
│  • Release notes                                                           │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Human-AI Collaboration Model

### The Three Actors

In a modern monorepo environment, work is distributed among three actors:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         THE THREE ACTORS                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│   │  HUMAN MANAGER  │    │ HUMAN ENGINEER  │    │    AI AGENT     │        │
│   │                 │    │                 │    │                 │        │
│   │  • Strategy     │    │  • Judgment     │    │  • Execution    │        │
│   │  • Governance   │    │  • Creativity   │    │  • Scale        │        │
│   │  • Decisions    │    │  • Context      │    │  • Speed        │        │
│   │  • Oversight    │    │  • Review       │    │  • Consistency  │        │
│   │                 │    │                 │    │                 │        │
│   │  Skills: M.*    │    │  Skills: All    │    │  Skills: All    │        │
│   │  Level: L3-L4   │    │  Level: E1-E5   │    │  Level: L3-L4   │        │
│   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘        │
│            │                      │                      │                 │
│            └──────────────────────┼──────────────────────┘                 │
│                                   │                                        │
│                          COLLABORATION                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Skill Distribution by Actor

| Skill Category | Human Manager | Human Engineer | AI Agent |
|----------------|---------------|----------------|----------|
| **C: Core** | L2-L3 (understand) | L2-L4 (execute) | L3-L4 (master) |
| **B: Build** | L2 (evaluate) | L2-L4 (configure) | L3-L4 (optimize) |
| **P: CI/CD** | L2-L3 (approve) | L2-L4 (implement) | L3 (execute) |
| **W: Workflow** | L3-L4 (define) | L2-L4 (follow) | L2-L3 (follow) |
| **T: Team** | L4 (lead) | L2-L4 (participate) | L2 (respect) |
| **A: AI** | L3-L4 (orchestrate) | L2-L4 (collaborate) | N/A |
| **X: Platform** | L2-L3 (prioritize) | L2-L4 (build) | L3-L4 (use) |
| **D: Domain** | L2 (evaluate) | L3-L4 (master) | L3-L4 (master) |
| **M: Manager** | L4 (own) | L1-L2 (aware) | L0 (N/A) |

### Task Routing Decision Tree

```
START: New task arrives
    │
    ├── Is this a STRATEGIC decision?
    │   (architecture, breaking change, team structure, security)
    │       │
    │       └── YES → HUMAN MANAGER decides
    │
    ├── Does this require JUDGMENT or CREATIVITY?
    │   (novel solution, ambiguous requirements, user research)
    │       │
    │       └── YES → HUMAN ENGINEER executes
    │                 (AI may assist)
    │
    ├── Is this WELL-DEFINED and REPEATABLE?
    │   (refactoring, test writing, dep updates, formatting)
    │       │
    │       └── YES → AI AGENT executes
    │                 (Human reviews)
    │
    ├── Does this require CROSS-DOMAIN coordination?
    │       │
    │       ├── YES → HUMAN MANAGER coordinates
    │       │         HUMAN ENGINEERS + AI execute
    │       │
    │       └── NO → Continue below
    │
    └── DEFAULT:
        │
        ├── Simple, single-domain → AI AGENT (with review)
        ├── Complex, single-domain → HUMAN ENGINEER (AI assists)
        └── Any production change → HUMAN ENGINEER (required)
```

### Collaboration Patterns

#### Pattern 1: AI Executes, Human Reviews

```
Task: "Add validation to user form"

1. Human Manager: Approves task, assigns to domain
2. AI Agent:
   - Analyzes existing form code
   - Identifies affected packages
   - Implements validation
   - Writes tests
   - Creates PR
3. Human Engineer:
   - Reviews PR
   - Checks edge cases AI might miss
   - Approves or requests changes
4. AI Agent:
   - Addresses feedback
   - Updates PR
5. Human Engineer:
   - Final approval
   - Merges
```

#### Pattern 2: Human Designs, AI Implements

```
Task: "Refactor auth system to support OAuth"

1. Human Manager:
   - Approves initiative
   - Assigns senior engineer
2. Human Engineer:
   - Designs architecture
   - Writes RFC
   - Defines interfaces
3. Human Manager:
   - Reviews RFC
   - Approves approach
4. AI Agent:
   - Implements each component
   - Writes tests
   - Creates stacked PRs
5. Human Engineer:
   - Reviews each PR
   - Handles edge cases
   - Coordinates merging
```

#### Pattern 3: AI Scouts, Human Decides

```
Task: "Investigate why builds are slow"

1. Human Manager:
   - Assigns investigation
2. AI Agent:
   - Profiles build times
   - Analyzes dependency graph
   - Identifies bottlenecks
   - Generates report with options
3. Human Engineer:
   - Reviews findings
   - Validates conclusions
4. Human Manager:
   - Decides which optimizations to pursue
   - Allocates resources
5. AI Agent + Human Engineer:
   - Implement chosen optimizations
```

### Quality Gates by Actor

| Gate | AI Agent | Human Engineer | Human Manager |
|------|----------|----------------|---------------|
| **Code compiles** | Must pass | Must pass | N/A |
| **Tests pass** | Must pass | Must pass | Review metrics |
| **Lint clean** | Must pass | Must pass | N/A |
| **Type safe** | Must pass | Must pass | N/A |
| **Affected tests run** | Must run | Must verify | N/A |
| **CODEOWNERS respected** | Must check | Must verify | Define rules |
| **PR description quality** | Generate | Review | Define standards |
| **Breaking change detected** | Must flag | Must review | Must approve |
| **Security scan** | Must pass | Must verify | Must approve exceptions |
| **Cross-domain impact** | Must flag | Must coordinate | Must approve |
| **Documentation updated** | Should update | Must verify | Define requirements |

### AI Agent Supervision Levels

| Task Type | Supervision Level | Human Involvement |
|-----------|-------------------|-------------------|
| **Lint/format fixes** | Autonomous | None (auto-merge OK) |
| **Test generation** | Light review | Skim tests, spot check |
| **Documentation** | Light review | Check accuracy |
| **Bug fixes (clear cause)** | Standard review | Normal PR review |
| **Feature implementation** | Standard review | Normal PR review |
| **Refactoring** | Careful review | Verify behavior preservation |
| **API changes** | Heavy review | Senior engineer required |
| **Cross-domain changes** | Heavy review | Multiple reviewers |
| **Security-related** | Heavy review | Security team required |
| **Database migrations** | Human executes | AI may draft |
| **Production deployments** | Human executes | AI prepares |

---

## Onboarding Progression

### Week 1: Foundation

```markdown
## Day 1-2: Environment Setup

### Goals
- [ ] Clone repository successfully
- [ ] Run build and tests
- [ ] Understand directory structure

### Skills Practiced
- C.1.1: Git clone, pull, push (L1)
- C.3.1: Workspace concept (L1)
- B.1.1: Turborepo basics (L1)

### Verification
- [ ] `pnpm install` completes without errors
- [ ] `pnpm build` completes (cached OK)
- [ ] `pnpm test` passes
- [ ] Can explain what a "workspace" is
```

```markdown
## Day 3-4: First Change

### Goals
- [ ] Make a small change in assigned domain
- [ ] Create and submit first PR
- [ ] Respond to review feedback

### Skills Practiced
- C.1.2: Branch management (L1)
- W.3.1: PR creation (L1)
- W.3.3: Review receiving (L1)
- A.1.1: AI assistants (L1)

### Verification
- [ ] Branch created from main
- [ ] Change committed with good message
- [ ] PR created with description
- [ ] Feedback addressed
- [ ] PR merged
```

```markdown
## Day 5: Understand the System

### Goals
- [ ] Read CODEOWNERS and understand ownership
- [ ] Understand CI pipeline
- [ ] Know who to ask for help

### Skills Practiced
- T.1.1: CODEOWNERS (L1)
- P.1.1: GitHub Actions (L1)
- T.3.1: Self-onboarding (L1)

### Verification
- [ ] Can identify owner of any file
- [ ] Can explain what CI checks run
- [ ] Knows domain team members
```

---

### Week 2-4: Independent Work

```markdown
## Goals
- [ ] Complete 3+ PRs independently
- [ ] Use affected-only commands
- [ ] Effectively use AI assistants

### Skills to Develop
- C.3.3: Dependency resolution (L2)
- B.1.3: Task dependencies (L2)
- P.2.1: Affected-only CI (L1)
- A.1.2: Context management (L2)

### Milestones
- [ ] PR without guidance from buddy
- [ ] Debug a build failure independently
- [ ] Use AI to generate tests
- [ ] Review someone else's PR
```

---

### Month 2-3: Domain Ownership

```markdown
## Goals
- [ ] Own a feature end-to-end
- [ ] Understand cross-domain dependencies
- [ ] Contribute to documentation

### Skills to Develop
- C.4.1: Understand dep graph (L2)
- W.4.1: Breaking changes (L2)
- T.2.1: README standards (L2)
- A.2.2: Task delegation (L2)

### Milestones
- [ ] Ship a feature from spec to production
- [ ] Update documentation for your domain
- [ ] Use AI for significant refactoring
- [ ] Mentor a newer team member
```

---

### Month 4-6: Cross-Domain Work

```markdown
## Goals
- [ ] Work on cross-domain feature
- [ ] Create or improve shared package
- [ ] Write an RFC

### Skills to Develop
- T.1.3: Cross-team collaboration (L2)
- T.4.2: RFC process (L2)
- W.2.1: PR Stacking (L2)
- A.2.3: Agent skills (L2)

### Milestones
- [ ] Cross-domain PR with multiple approvers
- [ ] RFC approved and implemented
- [ ] Created a reusable AI skill
- [ ] Improved build times measurably
```

---

## Assessment Rubrics

### Self-Assessment Template

```markdown
# Skill Self-Assessment

**Name**: _______________
**Current Level**: E___
**Date**: _______________

## Instructions
Rate yourself 0-4 for each skill. Be honest - this helps identify growth areas.

## Core Skills (C)
| Skill | Self-Rating | Evidence |
|-------|-------------|----------|
| C.1.1 Git Fundamentals | __ | ___ |
| C.1.2 Branch Management | __ | ___ |
| ... | ... | ... |

## Growth Plan
Based on my assessment, I want to focus on:
1. _______________
2. _______________
3. _______________
```

### Manager Assessment Criteria

```markdown
# Skill Assessment - Manager Review

**Engineer**: _______________
**Reviewer**: _______________
**Period**: _______________

## Assessment Evidence Types

### L1 (Beginner) Evidence
- Completed onboarding checklist
- Follows documentation
- Asks appropriate questions

### L2 (Competent) Evidence
- PRs merged without significant rework
- Handles common cases without help
- Helps others at L1

### L3 (Proficient) Evidence
- Handles edge cases and complex situations
- Mentors L1-L2 engineers
- Improves documentation/processes

### L4 (Expert) Evidence
- Designs systems used by others
- Defines best practices
- Recognized as go-to expert
```

---

## Learning Paths

### Path A: New Graduate → E2 (6-12 months)

```
Month 1-2: Foundation
├── Git fundamentals (C.1.x)
├── Workspace basics (C.3.1-3.2)
├── Basic build commands (B.1.1)
└── PR workflow (W.3.x)

Month 3-4: Independence
├── Dependency management (C.3.3-3.4)
├── Task orchestration (B.1.2-1.4)
├── AI assistants (A.1.x)
└── Code review (W.3.2)

Month 5-6: Ownership
├── Affected analysis (C.4.x)
├── CI configuration (P.1-2.x)
├── Documentation (T.2.x)
└── AI delegation (A.2.1-2.2)
```

### Path B: Experienced (non-monorepo) → E2 (2-4 months)

```
Week 1-2: Unlearn & Relearn
├── Monorepo Git specifics (C.2.x)
├── Workspace protocol (C.3.4)
├── Build tool comparison (B.1.x)
└── TBD principles (W.1.x)

Week 3-4: Apply Experience
├── Map existing skills to monorepo
├── CI/CD adaptation (P.x.x)
├── AI tool integration (A.1.x)
└── Cross-domain awareness (T.1.x)

Month 2: Full Speed
├── Advanced caching (B.2.x)
├── PR stacking (W.2.x)
├── Platform tooling (X.x.x)
└── AI agent usage (A.2.x)
```

### Path C: E2 → E3 (12-24 months)

```
Quarter 1: Depth
├── Master build system (B.x.x L3)
├── CI optimization (P.x.x L3)
├── Complex dependency issues (C.4.x L3)
└── AI skill creation (A.2.3 L3)

Quarter 2: Breadth
├── Cross-domain work (T.1.3 L3)
├── RFC writing (T.4.2 L3)
├── Breaking change management (W.4.x L3)
└── Platform improvement (X.x.x L3)

Quarter 3-4: Leadership
├── Mentor juniors (T.3.2-3.4 L3)
├── Define standards (W.x.x L3)
├── Design AI workflows (A.3.x L3)
└── Improve DevEx (X.1.x L3)
```

### Path D: E3 → E4 (24-36 months)

```
Year 1: Architecture
├── Design build systems (B.x.x L4)
├── Architect CI/CD (P.x.x L4)
├── Define dep strategies (C.x.x L4)
└── Build AI agent systems (A.x.x L4)

Year 2: Organization
├── Lead cross-team initiatives
├── Define org standards
├── Build platform tooling (X.x.x L4)
├── Shape engineering culture
```

---

## References

- [Software Engineer Competency Matrix 2024](https://www.qulix.com/about/blog/software-engineer-competency-matrix/)
- [Engineering Competency Matrix Guide](https://fullscale.io/blog/engineering-competency-matrix/)
- [Open Competency Matrix - GitHub](https://github.com/stride-so/matrix)
- [DevEx Platform Engineering](https://platformengineering.org/blog/what-does-a-devex-platform-engineer-do)
- [Monorepo Tools](https://monorepo.tools/)
- [Technical Skill Matrix for Developers](https://maddevs.io/blog/technical-skill-matrix-for-developers/)

---

## Discussion Points

> **This matrix is a starting point. Key decisions needed:**

1. **Skill Weighting**: Which categories matter most for our context?
2. **Level Calibration**: Are L1-L4 definitions appropriate?
3. **AI Skills Priority**: How much emphasis on AI collaboration skills?
4. **Assessment Frequency**: How often should skills be assessed?
5. **Gap Analysis**: What skills are most lacking in current team?
6. **Training Investment**: Which learning paths need resources?
