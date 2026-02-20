### Core Concept
Four permission modes (default, acceptEdits, bypassPermissions, plan) set baseline trust. `canUseTool` callback enables dynamic, context-aware security decisions—protect paths, enforce time-based rules, implement RBAC.

### Key Mental Models
- **Permission modes**: default (prompts all), acceptEdits (auto files), bypassPermissions (full auto), plan (no execution)
- **canUseTool return values**: allow, deny, updatedInput (modify request)
- **Defense in depth**: Combine restricted tools + permission mode + canUseTool

### Critical Patterns
- Protect config: `if "/config/" in file_path: return {"behavior": "deny"}`
- Time-based: Block edits during production hours
- Sanitize Bash: Wrap commands with timeout, block dangerous patterns
- RBAC: viewer/editor/admin with different tool access
- Audit logging: Log all tool usage for compliance

### AI Collaboration Keys
- Permission modes set baseline; canUseTool provides surgical precision
- Well-designed agents adapt when tools are unavailable

### Common Mistakes
- Using bypassPermissions without canUseTool guardrails
- Not protecting infrastructure files (package.json, terraform/)
- Missing audit trail for compliance

### Connections
- **Builds on**: Built-in Tools (Lesson 3)
- **Leads to**: Agent Skills (Lesson 5)
