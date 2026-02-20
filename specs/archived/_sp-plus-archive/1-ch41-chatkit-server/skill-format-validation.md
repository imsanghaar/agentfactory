# Canonical Skill Format Validation

**Canonical Source**: `.claude/skills/building-chat-interfaces/SKILL.md`
**Also Reference**: Chapter 5 Lesson 7 (skill format teaching), `.claude/skills/creating-skills/SKILL.md`
**Validation Date**: 2025-12-31
**Purpose**: Document required skill format for L00, L04, L05, L06

## Required Directory Structure

**CORRECT**:
```
.claude/skills/chatkit-server/
├── SKILL.md              # Main skill file
├── references/           # Supporting documentation
│   └── patterns.md
└── scripts/              # Automation scripts (optional)
    └── verify.py
```

**WRONG** (flat file):
```
.claude/skills/chatkit-server-skill.md  # ❌ NOT a directory
```

## YAML Frontmatter Format

**Canonical Template**:
```yaml
---
name: skill-name-kebab-case
description: This skill should be used when [trigger condition]. Use when [use case 1], [use case 2], or [use case 3]. Covers [key technologies/patterns].
---
```

**Quality Markers**:
- ✅ name: kebab-case (NOT snake_case or camelCase)
- ✅ description: Starts with "This skill should be used when..."
- ✅ description: Lists specific triggers ("Use when...")
- ✅ description: Lists key technologies ("Covers...")
- ✅ Single-line description (NOT multi-line YAML with `|`)

**Example from building-chat-interfaces**:
```yaml
---
name: building-chat-interfaces
description: Build AI chat interfaces with custom backends, authentication, and context injection. Use when integrating chat UI with AI agents, adding auth, or injecting user/page context. Covers ChatKitServer, useChatKit, and MCP auth patterns.
---
```

## Required Sections

### 1. Title and Brief Description

```markdown
# Building Chat Interfaces

Build production-grade AI chat interfaces with custom backend integration.
```

**Quality Markers**:
- ✅ H1 title matches skill name (formatted for readability)
- ✅ One-line tagline (NOT multi-paragraph intro)

### 2. Quick Start

```markdown
## Quick Start

```bash
# Backend (Python)
uv add chatkit-sdk agents httpx

# Frontend (React)
npm install @openai/chatkit-react
```
```

**Quality Markers**:
- ✅ Installation commands (language-specific)
- ✅ Code blocks with language tags
- ✅ Comments for context

### 3. Core Architecture (Optional but Recommended)

```markdown
## Core Architecture

```
Frontend (React)                    Backend (Python)
┌─────────────────┐                ┌─────────────────┐
│  useChatKit()   │───HTTP/SSE───>│  ChatKitServer  │
│  - custom fetch │                │  - respond()    │
│  - auth headers │                │  - store        │
│  - page context │                │  - agent        │
└─────────────────┘                └─────────────────┘
```
```

**Quality Markers**:
- ✅ ASCII diagram (NOT image reference)
- ✅ Shows system boundaries
- ✅ Key components labeled

### 4. Patterns/Workflow

```markdown
## Backend Patterns

### 1. ChatKit Server with Custom Agent

```python
from chatkit.server import ChatKitServer
...
```

### 2. Database Persistence

```python
...
```
```

**Quality Markers**:
- ✅ Numbered pattern sections
- ✅ Code examples (NOT pseudo-code)
- ✅ Comments in code explaining key points
- ✅ Complete working examples (can be copied)

### 5. Common Pitfalls (Optional but Recommended)

```markdown
## Common Pitfalls

| Issue | Symptom | Fix |
|-------|---------|-----|
| History not in prompt | Agent doesn't remember conversation | Include history as string in system prompt |
| Context not transmitted | Agent missing user/page info | Add to request metadata, extract in backend |
```

**Quality Markers**:
- ✅ Table format (Issue | Symptom | Fix)
- ✅ Specific problems (NOT vague)
- ✅ Actionable fixes

### 6. Verification

```markdown
## Verification

Run: `python3 scripts/verify.py`

Expected: `✓ building-chat-interfaces skill ready`

## If Verification Fails

1. Check: references/ folder has chatkit-integration-patterns.md
2. **Stop and report** if still failing
```

**Quality Markers**:
- ✅ Clear command to run
- ✅ Expected output specified
- ✅ Failure remediation steps
- ✅ "Stop and report" for blocking issues

### 7. References

```markdown
## References

- [references/chatkit-integration-patterns.md](references/chatkit-integration-patterns.md) - Complete patterns with evidence
- [references/nextjs-httponly-proxy.md](references/nextjs-httponly-proxy.md) - Next.js cookie proxy patterns
```

**Quality Markers**:
- ✅ Relative links to references/ directory
- ✅ Brief description after link
- ✅ Hyphen bullet format

## Section Order (Canonical)

1. YAML frontmatter
2. # Title + tagline
3. ## Quick Start
4. ## Core Architecture (optional)
5. ## Patterns/Backend Patterns/Frontend Patterns (main content)
6. ## Common Pitfalls (optional)
7. ## Verification
8. ## References

**Quality Markers**:
- ✅ Quick Start early (immediate value)
- ✅ Patterns are bulk of content
- ✅ Verification near end (testing)
- ✅ References last (deep dive links)

## What NOT to Include

**Anti-Patterns**:
- ❌ Version numbers in description ("v2.0", "2024 edition")
- ❌ Constitution alignment sections (that's for lesson design, not skills)
- ❌ Category labels ("Tier 2", "Advanced")
- ❌ Dependencies section (show in Quick Start instead)
- ❌ Changelog or history
- ❌ Author attribution
- ❌ License information in skill body (use LICENSE.txt file)

## Validation Checklist

Before committing skill, verify:
- [ ] Directory structure (NOT flat file)
- [ ] YAML frontmatter (name + description starting with "This skill should be used when...")
- [ ] Quick Start section with installation commands
- [ ] Main patterns section with working code examples
- [ ] Verification section with clear command
- [ ] References section with links to references/ folder
- [ ] No version numbers, constitution sections, or changelog

## Verification Script

**Location**: `.claude/skills/creating-skills/scripts/verify.py`

**Usage**:
```bash
cd .claude/skills/chatkit-server/
python3 ../creating-skills/scripts/verify.py
```

**Expected Output**:
```
✓ SKILL.md exists
✓ YAML frontmatter valid
✓ Required sections present
✓ chatkit-server skill ready
```

## Notes for L00 Lesson

**Teaching Approach**:
1. Show canonical source: `.claude/skills/building-chat-interfaces/SKILL.md`
2. Highlight format requirements (directory, YAML, sections)
3. Explain "This skill should be used when..." trigger pattern
4. Demonstrate verification script usage
5. Guide students to create chatkit-server skill matching format

**Anti-Pattern Warning**:
"In Chapter 14, students invented their own skill formats because they didn't reference canonical sources. This caused format drift. ALWAYS use building-chat-interfaces as your template."

## Skills to Create in Chapter 41

### L04: conversation-history

**Description Template**:
```yaml
description: This skill should be used when implementing conversation history management for AI chat interfaces. Use when loading thread items from store, building history context for agents, or implementing pagination for conversation history. Covers ChatKit store methods, history serialization patterns, and context window management.
```

### L05: session-lifecycle

**Description Template**:
```yaml
description: This skill should be used when managing ChatKit session lifecycle. Use when implementing session creation, resumption, timeout handling, or cleanup. Covers RequestContext patterns, session state management, and multi-tenant isolation.
```

### L06: chatkit-auth-security

**Description Template**:
```yaml
description: This skill should be used when implementing authentication and security for ChatKit servers. Use when validating RequestContext, enforcing thread access controls, or implementing JWT/JWKS authentication. Covers multi-tenant security patterns, metadata validation, and user isolation.
```

## Canonical Format Summary

**Core Rule**: Skills are directory-based with YAML frontmatter, Quick Start, Patterns, Verification, and References sections. Description MUST start with "This skill should be used when..." and list specific triggers. Reference `.claude/skills/building-chat-interfaces/SKILL.md` as the canonical template to prevent format drift.
