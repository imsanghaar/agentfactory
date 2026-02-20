# Lesson 2 Summary: Email Templates Skill

## Key Concepts

1. **Template Design**: Create email templates with `{{variable_name}}` placeholders for personalization

2. **Variable Substitution**: Replace placeholders with actual values at generation time (recipient name, company, value proposition)

3. **Template Library**: Organize templates in `templates/` directory with clear naming conventions

4. **Template Selection Logic**: Define when-to-use criteria for each template type

5. **References Directory**: Store supporting files that enhance skill capabilities

## Deliverables

- Working `/email-templates` skill with proper SKILL.md
- Three template files:
  - `templates/cold-outreach.md`
  - `templates/follow-up.md`
  - `templates/meeting-request.md`

## Key Code Snippets

### Template Structure
```markdown
# Cold Outreach Template

Subject: {{subject_hook}}

Hi {{recipient_name}},

{{personalized_opener}}

I'm reaching out because {{value_proposition}}.

{{specific_ask}}

{{sign_off}}
```

### SKILL.md Workflow
```markdown
## Template Application Workflow

1. Identify template type from context
2. Read template from templates/
3. Collect variable values from user
4. Substitute all {{placeholders}}
5. Apply tone guidelines
6. Return completed email
```

### Variable Collection Pattern
```markdown
## Required Variables by Template

### Cold Outreach
- recipient_name: First name of recipient
- company: Their organization
- value_proposition: What you offer
- specific_ask: Clear next step
```

## Try With AI Prompts

1. `/email-templates cold-outreach` → Sarah Chen at TechCorp about AI consulting
2. Test variable substitution with multiple recipients
3. Create a new template for investor updates

## Skills Practiced

| Skill | Proficiency | Assessment |
|-------|-------------|------------|
| Email Template Design | A2 | Create templates with placeholders |
| Skill Creation | A2 | Write valid SKILL.md |
| Template Library Organization | A2 | Organize templates logically |
| Variable Substitution Patterns | A2 | Implement {{variable}} syntax |
| Template Selection Logic | A2 | Define when-to-use criteria |

## Duration
25 minutes

## Next Lesson
[Lesson 3: Email Summarizer Skill](./03-email-summarizer-skill.md) - Parse threads and extract action items
