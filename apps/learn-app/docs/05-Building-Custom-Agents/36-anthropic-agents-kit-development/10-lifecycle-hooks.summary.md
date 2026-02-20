### Core Concept
Hooks are async functions that intercept execution at lifecycle moments (PreToolUse, PostToolUse, UserPromptSubmit, Stop). They enforce security boundaries, log for auditing, implement permission workflows, and protect production systems.

### Key Mental Models
- **Hook lifecycle**: UserPromptSubmit → PreToolUse → [Tool executes] → PostToolUse → Stop
- **Decision returns**: permissionDecision (allow/deny), permissionDecisionReason, updatedInput
- **HookMatcher**: Target hooks to specific tools (matcher='Bash' or matcher='Read|Edit')

### Critical Patterns
- Block dangerous Bash: `if "rm -rf" in command: return {"permissionDecision": "deny"}`
- Audit logging: PostToolUse captures all tool invocations with timestamps
- Context-aware permissions: Check user_tier, enforce rate limits, implement RBAC
- Input modification: Sandbox file paths by rewriting in updatedInput

### AI Collaboration Keys
- Hooks are enforcement layer—system prompts are suggestions, hooks guarantee
- Deny-by-default safer but needs more config; allow-by-default simpler but riskier
- Combine security hooks + audit hooks for complete production coverage

### Common Mistakes
- Using hooks only for security (also useful for logging, monitoring, validation)
- Missing HookMatcher targeting (hook runs on all tools instead of specific ones)
- Not logging permissionDecisionReason (loses audit trail)

### Connections
- **Builds on**: Subagents for Parallel Work (Lesson 9)
- **Leads to**: Custom MCP Tools (Lesson 11)
