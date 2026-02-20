### Core Concept
Claude Agent SDK differs fundamentally from Claude API: with Client SDK you implement the tool loop yourself; with Agent SDK, Claude handles the loop autonomously. This separation enables skills ecosystem, file checkpointing, and runtime permissions—features other SDKs lack.

### Key Mental Models
- **SDK vs API**: API = you orchestrate; SDK = Claude orchestrates
- **Skills ecosystem**: Package domain expertise as reusable SKILL.md files
- **File checkpointing**: `rewindFiles()` makes failure recoverable
- **Runtime permissions**: `canUseTool` callback enables context-aware security

### Critical Patterns
- Agent SDK handles tool loop: prompt → tools execute → result
- Skills compose: `/skills/security-review.md`, `/skills/python-best-practices.md`
- Checkpoint enables bold exploration: failure is reversible
- Dynamic permissions adapt based on what agent is trying to do

### AI Collaboration Keys
- SDK removes infrastructure burden—focus on domain expertise
- Skills are versionable and shareable across team

### Common Mistakes
- Using Client SDK patterns when Agent SDK is more appropriate
- Implementing tool loop manually when SDK handles it

### Connections
- **Builds on**: Skill-first learning (Lesson 0)
- **Leads to**: First Agent with query() (Lesson 2)
