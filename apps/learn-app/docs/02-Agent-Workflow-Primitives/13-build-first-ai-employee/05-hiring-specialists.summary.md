# Lesson 4 Summary: Creating Custom Subagents

## Key Concepts

1. **Subagent Architecture**: Autonomous agents stored in `.claude/agents/[name].md` that can reason independently and use tools

2. **Agent Definition Format**: YAML frontmatter with:
   - `name`: Agent identifier
   - `description`: **MUST be single-line** (multi-line breaks parsing)
   - `tools`: Comma-separated list (Read, Grep, Glob, Edit)

3. **Task Tool Delegation**: Invoke subagents using the Task tool with `subagent_type` parameter

4. **Skills vs Subagents Decision Framework**:
   | Use Case | Decision Points | Choose |
   |----------|-----------------|--------|
   | Content generation | 2-4 | Skill |
   | Classification/reasoning | 5+ | Subagent |
   | External integration | N/A | MCP |

5. **Three Email Subagents**:
   - `inbox-triager`: Priority classification (Urgent/Important/Normal/Low)
   - `response-suggester`: Generate 2-3 response options with tone variations
   - `follow-up-tracker`: Identify emails needing follow-up with deadlines

## Deliverables

- Three working subagents in `.claude/agents/`:
  - `inbox-triager.md`
  - `response-suggester.md`
  - `follow-up-tracker.md`

## Key Code Snippets

### Agent Definition Format
```yaml
---
name: inbox-triager
description: Classify emails into Urgent/Important/Normal/Low priorities with reasoning
tools: Read, Grep, Glob
---

# Inbox Triager Agent

## Classification Criteria

### Urgent (respond within 2 hours)
- Explicit deadline today
- Executive sender
- Customer escalation

### Important (respond within 24 hours)
- Action items assigned to you
- Time-sensitive decisions
- Team dependencies
```

### Task Tool Invocation
```python
# In Claude Code, invoke subagent:
Task(
    subagent_type="inbox-triager",
    prompt="Classify these 5 emails by priority...",
    description="Triage inbox emails"
)
```

### Skills vs Subagents Decision
```markdown
## When to Use Each

**Use SKILL when:**
- Output format is predictable
- Logic has 2-4 decision points
- Guidance needed, not reasoning

**Use SUBAGENT when:**
- Autonomous reasoning required
- 5+ decision points
- Context-dependent responses
- Need to use multiple tools
```

## Try With AI Prompts

1. Test inbox-triager with 5 sample email subjects/snippets
2. Generate response options for a client complaint email
3. Identify follow-up needs in a 2-week-old thread

## Skills Practiced

| Skill | Proficiency | Assessment |
|-------|-------------|------------|
| Subagent Architecture | B1 | Explain skill vs subagent |
| Agent Definition Format | A2 | Create valid agent files |
| Classification Logic | B1 | Design priority criteria |
| Task Tool Delegation | A2 | Invoke subagents correctly |
| Response Patterns | B1 | Generate tone variations |
| Deadline Tracking | A2 | Detect implicit deadlines |
| Decision Framework | B1 | Choose correct component |

## Duration
35 minutes

## Next Lesson
[Lesson 5: Gmail MCP Integration](./05-gmail-mcp-integration.md) - Connect to real Gmail
