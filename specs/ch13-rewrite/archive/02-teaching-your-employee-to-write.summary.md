# Lesson 1 Summary: Project Setup & Email Drafter Skill

## Key Concepts

1. **Skills Architecture**: Skills are reusable expertise packages stored in `.claude/skills/[name]/SKILL.md` that Claude Code loads when invoked with `/skill-name`

2. **SKILL.md Format**: Required YAML frontmatter with `name` and `description` fields, followed by markdown instructions that guide AI behavior

3. **Directory Structure**:
   ```
   .claude/skills/email-drafter/
   ├── SKILL.md
   └── references/
       └── tone-guidelines.md
   ```

4. **Tone Specification**: Reference files define consistent communication voice (formality, warmth, length, structure)

5. **Skill Invocation**: Use `/email-drafter` syntax to activate skill with context loading

## Deliverables

- Complete project directory structure with `.claude/skills/` and `.claude/agents/` folders
- Working `/email-drafter` skill with proper YAML frontmatter
- `references/tone-guidelines.md` with voice specification

## Key Code Snippets

### SKILL.md Structure
```yaml
---
name: email-drafter
description: Draft professional emails with consistent tone and structure
---

# Email Drafter

## Your Role
You are an email composition assistant...

## Workflow
1. Gather context (recipient, purpose, tone)
2. Apply tone guidelines from references/
3. Draft email following structure
4. Offer refinement options
```

### Tone Guidelines Structure
```markdown
# Tone Guidelines

## Formality Level
- Default: Professional but warm
- Adjustments: Formal for executives, casual for peers

## Voice Characteristics
- Active voice preferred
- Concise sentences
- Clear calls to action
```

## Try With AI Prompts

1. `/email-drafter` → Create cold outreach to Sarah Chen about AI consulting
2. Test tone consistency by drafting the same email with different recipients
3. Refine voice by teaching AI your specific preferences

## Skills Practiced

| Skill | Proficiency | Assessment |
|-------|-------------|------------|
| Skill Directory Structure | A2 | Create proper structure |
| SKILL.md Format | A2 | Write valid SKILL.md |
| Tone Specification | A2 | Define voice guidelines |
| Skill Invocation | A2 | Use `/skill-name` syntax |

## Duration
30 minutes

## Next Lesson
[Lesson 2: Email Templates Skill](./02-email-templates-skill.md) - Build template library with variable substitution
