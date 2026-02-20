### Core Concept
Skills are active intelligence encoded as SKILL.md files that agents discover and apply autonomously. Configure `setting_sources=["project"]` to load from `.claude/skills/`, and grant `allowed_tools=["Skill"]` to enable skill activation.

### Key Mental Models
- **Skills vs system prompts**: Skills are independent files (easy to update, contextually activate); system prompts are monolithic (expensive, brittle)
- **settingSources precedence**: "user" = global (~/.claude/skills/), "project" = local (./.claude/skills/); project overrides user
- **Skill activation**: Agent recognizes applicable context and loads relevant skills automatically

### Critical Patterns
- Basic setup: `setting_sources=["project"], allowed_tools=["Skill", "Read"]`
- SKILL.md structure: YAML frontmatter (name, description, proficiency_level, use_when) + markdown content
- Create skill directories: `.claude/skills/security-review/SKILL.md`
- Skills compose: one skill can reference patterns from another

### AI Collaboration Keys
- Skills encode organizational expertise that compounds over time
- Create skill when pattern recurs 3+ times across different workflows
- Skills make agents specialized experts rather than general-purpose tools

### Common Mistakes
- Putting all knowledge in system prompt instead of modular skills
- Forgetting to grant Skill tool access
- Creating generic skills ("write good code") instead of specific actionable ones

### Connections
- **Builds on**: Permission Modes and Security (Lesson 4)
- **Leads to**: Custom Slash Commands (Lesson 6)
