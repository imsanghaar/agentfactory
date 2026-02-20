# Lesson 3 Summary: Email Summarizer Skill

## Key Concepts

1. **Thread Parsing**: Identify message boundaries, sender attribution, and chronological order in email threads

2. **Extraction Targets**: Three categories to extract:
   - **Decisions**: Conclusions reached in the thread
   - **Action Items**: Tasks assigned with owners and deadlines
   - **Open Questions**: Unanswered queries requiring response

3. **Output Formatting**: Different formats for different use cases:
   - Executive Summary: Brief overview for quick decisions
   - Detailed Breakdown: Complete analysis for response planning

4. **Skill Chaining**: Connect summarizer output to drafter input for automated response generation

5. **Reference Patterns**: Create extraction patterns reference file for consistent analysis

## Deliverables

- Working `/email-summarizer` skill with SKILL.md
- `references/extraction-patterns.md` with extraction criteria
- Skill chaining demonstration with email-drafter

## Key Code Snippets

### Extraction Patterns Reference
```markdown
# Extraction Patterns

## Decision Indicators
- "We've decided to..."
- "The final approach is..."
- "Going with option X"

## Action Item Markers
- "Please [verb]..."
- "[Name] will..."
- "By [date]..."

## Open Question Signals
- "What about...?"
- "Has anyone...?"
- "Still need to determine..."
```

### Output Format: Executive Summary
```markdown
## Thread Summary: {{subject}}

**Key Decision**: {{main_decision}}

**Your Action Items**:
1. {{action_1}} (due: {{deadline_1}})
2. {{action_2}} (due: {{deadline_2}})

**Open Questions**:
- {{question_1}}
```

### Skill Chaining Pattern
```markdown
## Workflow: Summarize → Draft Response

1. Invoke /email-summarizer on thread
2. Extract action items assigned to user
3. Identify open questions requiring response
4. Pass context to /email-drafter
5. Generate response addressing all items
```

## Try With AI Prompts

1. `/email-summarizer` → Paste a long email thread for analysis
2. Test extraction accuracy with threads containing implicit deadlines
3. Chain summarizer output to drafter for response generation

## Skills Practiced

| Skill | Proficiency | Assessment |
|-------|-------------|------------|
| Thread Parsing | A2 | Identify messages and senders |
| Information Extraction | A2 | Extract decisions, actions, questions |
| Output Format Design | A2 | Create appropriate formats |
| Skill Chaining | A2 | Connect skill outputs to inputs |
| Skill Reference Files | A2 | Create extraction patterns |

## Duration
25 minutes

## Next Lesson
[Lesson 4: Creating Custom Subagents](./04-creating-custom-subagents.md) - Build specialized email processing agents
