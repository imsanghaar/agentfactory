# Feature Specification: Chapter 6 - Building a Complete Email Assistant

**Feature Branch**: `001-ch6-business-workflows`
**Created**: 2026-01-01
**Status**: Draft (Revised)
**Reference**: GitHub Issue #554
**Revision Note**: Complete rewrite to leverage full Claude Code potential (Skills + Subagents + MCP)

## Chapter Overview

This chapter teaches students to build a **complete Email Assistant system** from scratch using Claude Code's full capabilities. Instead of surface-level coverage of multiple platforms, we go deep on one project that demonstrates:

- **Skills**: Multiple specialized skills working together
- **Subagents**: Custom agents for specific email tasks
- **MCP Integration**: Real Gmail connectivity via Gmail MCP Server
- **Orchestration**: Combining skills + subagents + MCP into a cohesive system

**Position in Book**: Part 2 (AI Tool Landscape), Chapter 6
**Proficiency Level**: A2-B1 (Elementary to Intermediate) - Progressive skill building
**Pedagogical Layer**: L2 → L3 progression (Collaboration → Intelligence Design)

## The Vision: Email Assistant as a Digital FTE

By chapter's end, students own a complete **Email Digital FTE** (Full-Time Equivalent):

```
📧 Email Assistant System
├── Skills (Reusable Expertise)
│   ├── /email-drafter       → Professional email composition
│   ├── /email-templates     → Template library with variables
│   ├── /email-summarizer    → Thread summarization & extraction
│   └── /tone-adapter        → Voice/style customization
│
├── Subagents (Specialized Workers)
│   ├── inbox-triager        → Priority classification
│   ├── response-suggester   → Quick reply recommendations
│   └── follow-up-tracker    → Deadline & reminder management
│
├── MCP Integration (External Connectivity)
│   └── Gmail MCP Server     → Real email operations
│       ├── send_email, draft_email
│       ├── read_email, search_emails
│       ├── list_labels, create_filter
│       └── batch operations
│
└── Orchestrator (System Coordinator)
    └── /email-assistant     → Master skill combining everything
```

---

## Assumed Knowledge (From Chapter 5)

Students MUST have completed Chapter 5 and understand:

| Concept | Chapter 5 Lesson | Required Understanding |
|---------|------------------|----------------------|
| Skills Architecture | L5: Concept Behind Skills | Why skills exist, progressive loading |
| Creating Skills | L6-L7: Skill Factory | SKILL.md format, YAML frontmatter, directory structure |
| CLAUDE.md | L8: Context Files | Persistent project context |
| MCP Fundamentals | L9: MCP Integration | What MCP is, how servers connect |
| Compiling MCP to Skills | L10: MCP to Skills | Token optimization, when to compile |
| Subagents | L11: Subagents & Orchestration | Built-in subagents, Task tool, delegation |
| Settings Hierarchy | L12: Settings | User/Project/Local scope |
| Hooks | L13: Hooks & Extensibility | Event-driven automation |

**What Chapter 6 teaches from scratch**:
- Professional email communication patterns
- How to design multi-skill systems
- Creating CUSTOM subagents (not just using built-in ones)
- MCP server configuration with authentication
- Orchestrating skills + subagents + MCP together

---

## User Stories & Testing

### User Story 1: Skill-Based Email Drafting (Priority: P1)

**Scenario**: A professional needs consistent, high-quality emails. They want skills that understand their tone, apply templates, and draft messages that sound like them.

**What students build**:
- `/email-drafter` skill with tone specification
- `/email-templates` skill with variable substitution
- `/tone-adapter` skill for voice customization

**Independent Test**: Student can invoke `/email-drafter "Write a cold outreach to [name] about [topic]"` and get a professional email matching their specified tone profile.

**Acceptance Scenarios**:
1. **Given** a drafting request, **When** skill is invoked, **Then** output matches tone-guidelines.md specification
2. **Given** a template name and variables, **When** template skill is used, **Then** placeholders are correctly substituted
3. **Given** an email draft, **When** tone-adapter is applied, **Then** formality/warmth/length are adjusted as specified

---

### User Story 2: Subagent-Based Email Processing (Priority: P1)

**Scenario**: A professional receives 50+ emails daily. They need automated triage, response suggestions, and follow-up tracking that works WITHOUT manual intervention.

**What students build**:
- `inbox-triager` subagent for classification
- `response-suggester` subagent for quick replies
- `follow-up-tracker` subagent for deadline management

**Independent Test**: Student gives the inbox-triager a list of email subjects/snippets, and it returns priority classifications with reasoning.

**Acceptance Scenarios**:
1. **Given** a batch of email metadata, **When** inbox-triager runs, **Then** emails are classified as Urgent/Important/Normal/Low
2. **Given** an email requiring response, **When** response-suggester runs, **Then** it proposes 2-3 response options with tone variations
3. **Given** sent emails with implicit deadlines, **When** follow-up-tracker runs, **Then** it identifies which need follow-up and when

---

### User Story 3: Gmail MCP Integration (Priority: P1)

**Scenario**: A professional wants Claude Code to work with their REAL inbox—search emails, create drafts, send messages, manage labels—all from the terminal.

**What students build**:
- Gmail MCP server connection (SMTP or OAuth)
- Workflow combining MCP tools with skills
- Safety protocols for email operations

**Independent Test**: Student can say "Search my inbox for emails from [person] about [topic] and summarize them" and Claude performs real Gmail operations.

**Acceptance Scenarios**:
1. **Given** Gmail MCP configured, **When** user requests email search, **Then** real Gmail search executes and returns results
2. **Given** a drafted email, **When** user approves sending, **Then** email is sent via Gmail MCP (with draft-first safety)
3. **Given** need for organization, **When** user requests label creation, **Then** Gmail label is created via MCP

---

### User Story 4: Orchestrated Email System (Priority: P1)

**Scenario**: A professional wants ONE command that leverages ALL capabilities—skills for drafting, subagents for processing, MCP for execution.

**What students build**:
- `/email-assistant` master skill that orchestrates:
  - Skills for content generation
  - Subagents for classification/suggestion
  - MCP for real Gmail operations

**Independent Test**: Student says "Help me manage my inbox" and the system triages emails, suggests responses, drafts replies, and prepares them as Gmail drafts.

**Acceptance Scenarios**:
1. **Given** the orchestrator skill, **When** invoked for inbox management, **Then** it coordinates triage → suggestion → drafting → MCP operations
2. **Given** a complex email task, **When** orchestrator determines needs, **Then** it delegates to appropriate skill/subagent/MCP tool
3. **Given** the full system, **When** user completes chapter, **Then** they have a portable, reusable Email Digital FTE

---

## Requirements

### Functional Requirements

| ID | Requirement | Lesson |
|----|-------------|--------|
| FR-001 | Chapter includes README with system architecture overview | README |
| FR-002 | Students create 4+ working skills with proper SKILL.md format | L1-L3 |
| FR-003 | Students create 3+ custom subagents with agent definitions | L4 |
| FR-004 | Students configure Gmail MCP with authentication | L5 |
| FR-005 | Students build orchestrator combining skills + subagents + MCP | L6 |
| FR-006 | Each lesson includes 3+ "Try With AI" exercises | All |
| FR-007 | System handles edge cases (empty input, character limits, errors) | L6 |
| FR-008 | Chapter includes quiz validating all components | Quiz |

### Technical Requirements

| ID | Requirement | Details |
|----|-------------|---------|
| TR-001 | Skills follow `.claude/skills/[name]/SKILL.md` structure | Canonical format |
| TR-002 | Subagents follow `.claude/agents/[name].md` format | Single-line descriptions |
| TR-003 | Gmail MCP supports both SMTP and OAuth authentication | User choice |
| TR-004 | Orchestrator uses Task tool for subagent delegation | Built-in tool |
| TR-005 | All skills have references/ and templates/ directories | Full structure |
| TR-006 | System works offline (skills/subagents) and online (MCP) | Graceful degradation |

---

## Chapter Structure (7 Lessons)

### Lesson 1: Project Setup & Email Drafter Skill (30 min)

**Layer**: L2 (Collaboration) → L3 (Intelligence Design)
**Goal**: Set up project structure and create first skill

**Topics**:
1. Email Assistant project architecture overview
2. Setting up the skills-lab directory structure
3. Creating `/email-drafter` skill with SKILL.md
4. Tone specification in references/tone-guidelines.md
5. Three Roles: AI teaches email patterns, student refines voice

**Deliverable**: Working `/email-drafter` skill

**Directory Structure Created**:
```
skills-lab/
├── .claude/
│   └── skills/
│       └── email-drafter/
│           ├── SKILL.md
│           └── references/
│               └── tone-guidelines.md
└── CLAUDE.md
```

---

### Lesson 2: Email Templates Skill (25 min)

**Layer**: L3 (Intelligence Design)
**Goal**: Create reusable template system with variable substitution

**Topics**:
1. Template design principles (placeholders, structure)
2. Creating `/email-templates` skill
3. Building template library (cold-outreach, follow-up, meeting-request)
4. Variable substitution patterns
5. Template selection logic

**Deliverable**: Working `/email-templates` skill with 3+ templates

**Directory Structure Added**:
```
.claude/skills/
└── email-templates/
    ├── SKILL.md
    └── templates/
        ├── cold-outreach.md
        ├── follow-up.md
        └── meeting-request.md
```

---

### Lesson 3: Email Summarizer Skill (25 min)

**Layer**: L3 (Intelligence Design)
**Goal**: Create skill for thread summarization and action extraction

**Topics**:
1. Thread parsing patterns
2. Creating `/email-summarizer` skill
3. Extraction targets: decisions, action items, open questions
4. Output formatting for different use cases
5. Combining with drafter for response generation

**Deliverable**: Working `/email-summarizer` skill

**Directory Structure Added**:
```
.claude/skills/
└── email-summarizer/
    ├── SKILL.md
    └── references/
        └── extraction-patterns.md
```

---

### Lesson 4: Creating Custom Subagents (35 min)

**Layer**: L3 (Intelligence Design)
**Goal**: Build specialized subagents for email processing

**Topics**:
1. Subagent architecture in Claude Code
2. Creating `inbox-triager` agent definition
3. Creating `response-suggester` agent definition
4. Creating `follow-up-tracker` agent definition
5. Testing subagents with Task tool
6. When to use skills vs. subagents (decision framework)

**Deliverable**: 3 working subagents in `.claude/agents/`

**Directory Structure Added**:
```
.claude/agents/
├── inbox-triager.md
├── response-suggester.md
└── follow-up-tracker.md
```

---

### Lesson 5: Gmail MCP Integration (30 min)

**Layer**: L2 (Collaboration) + Technical Setup
**Goal**: Connect Claude Code to real Gmail

**Topics**:
1. Gmail MCP Server overview (19 tools)
2. Authentication options (SMTP vs OAuth)
3. Step-by-step SMTP setup (2 minutes)
4. Step-by-step OAuth setup (10 minutes)
5. Testing Gmail MCP tools (list labels, search, draft)
6. Safety protocols (draft-first, sensitive data handling)

**Deliverable**: Working Gmail MCP connection

**Configuration Added**:
```bash
claude mcp add gmail --scope user -- npx mcp-remote \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Email: your-email@gmail.com" \
  --header "X-Gmail-Password: your-app-password"
```

---

### Lesson 6: Orchestrating the Complete System (40 min)

**Layer**: L4 (Spec-Driven / Capstone)
**Goal**: Combine skills + subagents + MCP into unified system

**Topics**:
1. Orchestration patterns (coordinator skill)
2. Creating `/email-assistant` master skill
3. Delegation logic (when to use which component)
4. Workflow: Triage → Suggest → Draft → Send
5. Error handling and graceful degradation
6. Testing the complete system

**Deliverable**: Working `/email-assistant` orchestrator

**Final Directory Structure**:
```
skills-lab/
├── .claude/
│   ├── skills/
│   │   ├── email-drafter/
│   │   ├── email-templates/
│   │   ├── email-summarizer/
│   │   └── email-assistant/      # Orchestrator
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── orchestration-logic.md
│   └── agents/
│       ├── inbox-triager.md
│       ├── response-suggester.md
│       └── follow-up-tracker.md
├── CLAUDE.md
└── .mcp.json                      # Gmail MCP config
```

---

### Lesson 7: Chapter Quiz (15 min)

**Focus**: Validate understanding of full system

**Question Categories**:
- Skills: SKILL.md format, when to create, structure (4 questions)
- Subagents: Agent definition format, delegation, when to use (4 questions)
- MCP: Authentication, tools, safety protocols (3 questions)
- Orchestration: Combining components, workflow design (4 questions)

**Total**: 15 questions, 60% pass threshold

---

## Success Criteria

| ID | Criterion | Measurement |
|----|-----------|-------------|
| SC-001 | Students create 4+ working skills | All skills invocable via `/name` |
| SC-002 | Students create 3+ working subagents | Subagents execute via Task tool |
| SC-003 | Gmail MCP connection works | Can list labels, search emails |
| SC-004 | Orchestrator coordinates all components | End-to-end workflow executes |
| SC-005 | System handles edge cases | Graceful error handling |
| SC-006 | 90% quiz pass rate on first attempt | Quiz analytics |
| SC-007 | Students understand when to use skills vs. subagents | Can articulate decision criteria |
| SC-008 | Students can extend system for new use cases | Demonstrate adding new template |

---

## Out of Scope

- Other platforms (WhatsApp, LinkedIn, Twitter) - separate future chapter
- Multi-language email support - English focus
- Email scheduling/automation beyond MCP - future chapters
- Building custom MCP servers - Chapter 38 covers this
- Production deployment - development/learning focus

---

## Dependencies

- **Chapter 5** (REQUIRED): Claude Code fundamentals
- **Chapter 38** (FUTURE): Building custom MCP servers (references forward)
- **Gmail MCP Server**: External dependency (cloud-hosted option available)

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Gmail MCP server down | Skills/subagents work offline; MCP is one component |
| OAuth setup complexity | SMTP option takes 2 minutes as fallback |
| Student doesn't have Gmail | Can still complete L1-L4 and L6 (orchestration) without L5 |
| Subagent format breaks | Lesson includes troubleshooting for single-line description requirement |
