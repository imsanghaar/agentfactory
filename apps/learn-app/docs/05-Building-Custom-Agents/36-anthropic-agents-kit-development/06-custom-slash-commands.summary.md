### Core Concept
Slash commands are workflow shortcuts in `.claude/commands/` that encapsulate intent, required tools, and instructions. Unlike skills (general expertise), commands are task-specific—`/review` runs a specific workflow with specific tool restrictions.

### Key Mental Models
- **Commands vs Skills**: Commands = specific workflows with tool constraints; Skills = general expertise applied across multiple commands
- **Deny by default**: Only grant tools the command actually needs
- **File-to-command mapping**: `.claude/commands/code-review.md` → invoked as `/code-review`

### Critical Patterns
- Command structure: YAML frontmatter (allowed-tools, description) + markdown instructions
- Read-only command: `allowed-tools: Read, Glob, Grep` (no Write/Edit/Bash)
- Refactoring command: `allowed-tools: Read, Edit, Bash` (Edit for changes, Bash for tests)
- Arguments: `/code-review src/auth.py --severity=critical` passes file + filter

### AI Collaboration Keys
- Build command libraries for your organization (review-pr, security-audit, generate-test)
- Each command carries its own tool restrictions for safety
- Commands should be focused—if workflow spans 3+ different concerns, split it

### Common Mistakes
- Over-privileging commands with tools they don't need
- Creating commands when skills would be more reusable
- Not testing command arguments in edge cases

### Connections
- **Builds on**: Agent Skills in Code (Lesson 5)
- **Leads to**: Session Management (Lesson 7)
