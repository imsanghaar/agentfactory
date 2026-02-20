### Core Concept
Separate what model sees from what widget sees. `structuredContent` = summary for model narration (counts, status). `_meta` via `toolResponseMetadata` = full data for widget (complete task list). Model narrates concisely; widget shows everything.

### Key Mental Models
- **Two data channels**: `structuredContent` (Model + Widget) vs `_meta` (Widget only)
- **Token efficiency**: 100 tasks in structuredContent = verbose narration; in _meta = clean summary
- **toolOutput vs toolResponseMetadata**: Different APIs for different data sources
- **Dynamic list rendering**: JavaScript reads `_meta.tasks` and generates DOM

### Critical Patterns
- Model sees: `structuredContent={"total": 3, "pending": 2, "completed": 1}`
- Widget sees: `_meta={"tasks": [...full list...], "openai.com/widget": ...}`
- Widget access: `const meta = window.openai?.toolResponseMetadata`
- Summary access: `const summary = window.openai?.toolOutput`

### AI Collaboration Keys
- Prompt 1: Handle empty state with "No tasks yet" message
- Prompt 2: Style pending vs done with visual hierarchy
- Prompt 3: Add task count to widget title dynamically

### Common Mistakes
- Putting full list in structuredContent (model tries to summarize everything)
- Confusing toolOutput and toolResponseMetadata
- Not handling empty tasks array (crashes on undefined)

### Connections
- **Builds on**: Adding a Refresh Button (Lesson 3)
- **Leads to**: Task Actions with callTool (Lesson 5)
