### Core Concept
MCP servers are dumb tools; MCP-wrapping skills add intelligence. The skill decides WHEN to call MCP, filters results (~77% token savings), handles errors, and provides fallbacks. Intelligence layer transforms MCP from interesting to production-critical.

### Key Mental Models
- **Raw MCP vs wrapped**: 934 tokens raw → 205 tokens filtered = ~77% savings through intelligent extraction
- **Intelligence layer components**: Persona, trigger conditions, questions, MCP config, result filtering, error recovery, fallback
- **Filtering before processing**: Reduce call volume AND result volume; don't analyze full page when you need one form
- **Token efficiency is intentional**: Ask "What does user actually need?" then filter to that

### Critical Patterns
- fetching-library-docs: Extract code blocks + signatures + notes; shell pipeline filtering
- browsing-with-playwright: Snapshot page → filter to relevant elements → interact with subset
- Error recovery: Library variations, topic clarification, network retry with backoff
- Fallback strategies: Cached data, external links, alternative sources

### AI Collaboration Keys
- MCP-wrapping = decision-making about when/how/why to call external tools
- Filter based on user's actual need, not everything the tool returns
- Error recovery makes skills production-ready (95% is not enough; 100% graceful failure is)

### Common Mistakes
- Using raw MCP output without filtering (wastes context)
- No error recovery for network/timeout failures
- Over-filtering that loses critical information

### Connections
- **Builds on**: Skill Composition & Multi-Skill Workflows (Lesson 2)
- **Leads to**: Build Your MCP-Wrapping Skill (Lesson 4)
