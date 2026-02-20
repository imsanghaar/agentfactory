# Lesson 5 Summary: Gmail MCP Integration

## Key Concepts

1. **Gmail MCP Server**: External tool server providing 19 Gmail operations to Claude Code

2. **Authentication Methods**:
   - **SMTP + App Password** (2 min): Quick setup for basic send/receive
   - **OAuth** (10 min): Full API access with granular permissions

3. **Gmail MCP Tools** (19 total):
   | Category | Tools |
   |----------|-------|
   | Reading | `read_email`, `search_emails`, `get_email_thread` |
   | Sending | `send_email`, `draft_email`, `reply_to_email` |
   | Organization | `list_email_labels`, `create_label`, `apply_label` |
   | Management | `archive_email`, `delete_email`, `mark_as_read` |

4. **Safety Protocols**:
   - Draft-first workflow: Always create drafts before sending
   - Sensitive data handling: Never include passwords/tokens in prompts
   - Confirmation gates: Require explicit approval for destructive actions

5. **MCP + Skills Integration**: Combine Gmail MCP tools with email skills for complete automation

## Deliverables

- Working Gmail MCP connection (SMTP or OAuth)
- Tested Gmail operations (list labels, search, draft)
- Documented safety protocols

## Key Code Snippets

### SMTP Setup (2 minutes)
```bash
# Add Gmail MCP with App Password
claude mcp add gmail --scope user -- npx mcp-remote \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Email: your-email@gmail.com" \
  --header "X-Gmail-Password: your-app-password"
```

### OAuth Setup (10 minutes)
```bash
# 1. Create Google Cloud project
# 2. Enable Gmail API
# 3. Create OAuth credentials
# 4. Configure consent screen
# 5. Add to Claude Code with OAuth token
```

### Test Gmail Connection
```
# In Claude Code:
"List all my Gmail labels"
→ Gmail MCP tool: list_email_labels

"Search for emails from sarah@techcorp.com this week"
→ Gmail MCP tool: search_emails
```

### Safety Protocol: Draft-First
```markdown
## Draft-First Workflow

1. User requests email send
2. Claude drafts to Gmail Drafts folder
3. User reviews draft in Gmail
4. User confirms send
5. Claude executes send_email

NEVER: Skip draft review for external recipients
```

## Try With AI Prompts

1. "List all my Gmail labels" - Test basic connection
2. "Search for emails from [person] about [topic]" - Test search
3. "Draft a response to the latest email from [person]" - Test draft creation

## Skills Practiced

| Skill | Proficiency | Assessment |
|-------|-------------|------------|
| Gmail MCP Configuration | B1 | Configure with SMTP or OAuth |
| App Password Creation | A2 | Generate Google App Password |
| OAuth Credential Setup | B1 | Create Cloud project and credentials |
| Gmail MCP Tool Usage | B1 | Invoke search, draft, send tools |
| Email Safety Protocols | B1 | Apply draft-first workflow |

## Duration
30 minutes

## Next Lesson
[Lesson 6: Orchestrating Complete System](./06-orchestrating-complete-system.md) - Combine everything into Email Digital FTE
