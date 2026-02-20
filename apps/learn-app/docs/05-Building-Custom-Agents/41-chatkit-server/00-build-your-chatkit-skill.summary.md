### Core Concept
Before learning ChatKit Server, create a ChatKit skill using Context7 to fetch official documentation. One prompt creates a complete skill grounded in official docs. Agents are conversational, not request/response—ChatKit bridges this gap.

### Key Mental Models
- **Skill-first learning**: Own the asset before studying details; improve throughout chapter
- **Conversational vs REST**: REST APIs are request/response; agents need conversation semantics
- **Documentation-grounded**: Context7 fetches official ChatKit docs—no hallucinated patterns
- **Clarifying questions**: AI asks about session management, streaming, auth patterns before building

### Critical Patterns
- Clone skills-lab fresh (no state assumptions from prior chapters)
- Single prompt creates complete skill with references, templates, starter code
- Skill location: `.claude/skills/chatkit-server/`

### AI Collaboration Keys
- Use skill creator skill with Context7 for documentation fetching
- Let AI ask clarifying questions about session management and streaming
- Test skill against each lesson's concepts as you learn

### Common Mistakes
- Using AI memory instead of official docs (leads to outdated patterns)
- Skipping clarifying questions (produces generic skill)
- Not testing skill throughout chapter (skill quality stagnates)

### Connections
- **Builds on**: FastAPI for Agents (Chapter 40)
- **Leads to**: ChatKit Architecture (Lesson 1)
