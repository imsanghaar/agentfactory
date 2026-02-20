---
title: "Summary: Your Employee's Memory"
sidebar_label: "Summary"
sidebar_position: 1.5
---

# Lesson 1 Summary: Your Employee's Memory

## Key Concepts

1. **Obsidian Vault as Workspace**: The vault is your employee's persistent memory — structured folders for projects, logs, and knowledge

2. **AGENTS.md Governance**: Defines skill and agent formats, workspace structure, and governance rules that Claude Code reads on every invocation

3. **CLAUDE.md Context**: Personal preferences, current focus, and working style that shapes how your AI employee operates

4. **MCP Memory Bank**: Obsidian REST API connected via MCP gives Claude Code read/write access to vault contents

5. **Vault Security**: Never store secrets in vault files; use `.env` outside the vault, add to `.gitignore`, reference secrets by name only

## Deliverables

- Obsidian vault with proper folder structure (`/Inbox/`, `/Done/`, `/Logs/`, `/Projects/`)
- `AGENTS.md` with governance rules and skill/agent format definitions
- `CLAUDE.md` with personal context and preferences
- Working MCP connection to Obsidian REST API
- Verified Claude Code can read vault context

## Key Code Snippets

### Vault Folder Structure

```
Employee_Vault/
├── AGENTS.md
├── CLAUDE.md
├── Inbox/
├── Done/
├── Logs/
├── Projects/
└── .obsidian/
```

## Skills Practiced

| Skill                            | Proficiency | Assessment                               |
| -------------------------------- | ----------- | ---------------------------------------- |
| Obsidian Vault Setup             | A2          | Create vault with governance files       |
| AGENTS.md Configuration          | A2          | Write AGENTS.md with skill/agent formats |
| Claude Code Context Verification | A2          | Verify Claude Code reads vault context   |

## Duration

25 minutes

## Next Lesson

[Lesson 2: Teaching Your Employee to Write](./02-teaching-your-employee-to-write.md) - Build the email drafter skill
