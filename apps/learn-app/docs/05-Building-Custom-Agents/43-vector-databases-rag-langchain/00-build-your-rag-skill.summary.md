### Core Concept
Before learning RAG, create a RAG skill using Context7 to fetch official LangChain and Qdrant documentation. Skill-first learning means owning the asset before studying details. One prompt creates a complete skill grounded in official docs.

### Key Mental Models
- **Skill-first learning**: Own the asset before studying details; improve throughout chapter
- **Documentation-grounded**: Context7 fetches official LangChain/Qdrant docs—no hallucinated patterns
- **Clarifying questions**: AI asks about chunking strategies, embedding models, retrieval modes
- **RAG = Retrieval + Generation**: Find relevant context, then generate grounded answers

### Critical Patterns
- Clone skills-lab fresh (no state assumptions from prior chapters)
- Single prompt creates complete skill with references, templates, starter code
- Skill location: `.claude/skills/rag-deployment/`

### AI Collaboration Keys
- Use skill creator skill with Context7 for documentation fetching
- Let AI ask about vector store preferences, embedding models, chunking strategies
- Test skill against each lesson's concepts as you learn

### Common Mistakes
- Using AI memory instead of official docs (leads to outdated patterns)
- Skipping clarifying questions (produces generic skill)
- Not testing skill throughout chapter (skill quality stagnates)

### Connections
- **Builds on**: FastAPI for Agents (Chapter 40)
- **Leads to**: Why Agents Need External Knowledge (Lesson 1)
