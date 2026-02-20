### Core Concept
Code blocks (fenced with triple backticks and language tags) provide **specification by example**—showing exact expected output and code format so AI agents see concrete targets instead of interpretations, reducing ambiguity dramatically.

### Key Mental Models
- **Specification by Example**: Showing expected output in a code block is clearer than describing it in prose
- **Language Tags as Context**: `python`, `bash`, `text` tags tell AI which language to generate and which syntax applies
- **Exact vs Abstract**: Abstract: "show current temperature"; Exact: code block showing actual output format
- **Semantic Anchoring**: Code blocks are "anchor points"—when AI sees expected output, it has a concrete target to implement against

### Critical Patterns
- **Fenced syntax**: Triple backticks ``` at start and end; content between treated literally
- **Language tags**: `python`, `bash`, `text`, `json` go immediately after opening backticks (no space)
- **Inline code syntax**: Single backticks for short references in text (`pip install`, `app.py`)
- **Documenting code blocks**: Use quadruple backticks (``````) to show triple backticks in documentation
- **"What you type" / "What it renders as"**: Show both raw syntax and rendered output when teaching markdown

### AI Collaboration Keys
- **Output specification**: Code blocks showing expected output give AI unambiguous implementation targets
- **Language clarity**: Language tags prevent AI from mixing syntaxes (Python code vs bash commands)
- **Edge cases**: Include code blocks showing edge cases (empty lists, error states) so AI handles them
- **Mental model alignment**: Code blocks in specs become the "acceptance test"—AI knows it succeeded when output matches

### Common Mistakes
- Forgetting closing triple backticks (leaves code block unclosed)
- Missing language tag when it matters (unlabeled blocks are ambiguous)
- Showing description instead of exact output ("menu appears" vs actual menu text)
- Using escaped backticks (`\`\`\``) instead of quadruple backticks when documenting code blocks
- Not providing context about whether code block is complete spec or illustrative example

### Connections
- **Builds on**: Lessons 1-3 (structure, headings, lists provide context where code blocks appear)
- **Leads to**: Lesson 5 (integrating code blocks into complete specifications with links and images)
- **Task Tracker App**: This lesson adds expected output examples to your ongoing specification
