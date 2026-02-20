### Core Concept
Heading hierarchy (`#` through `######`) creates document structure that lets AI agents quickly locate sections and understand relationships between ideas—the foundation of machine-parseable specifications.

### Key Mental Models
- **Heading Levels = Folder Structure**: Level 1 (main), Level 2 (sections), Level 3 (subsections) mirror computer folder hierarchies; AI navigates documents using this structure
- **Semantic Meaning in Levels**: Each heading level communicates relationship—`## Features` followed by `### Add Tasks` tells AI "Add Tasks is a detail within Features"
- **No Skipping Levels**: Breaking hierarchy (jumping from `#` to `###`) breaks document semantics; intermediate levels anchor subsections in proper context
- **AI's Logical Map**: Wrong heading hierarchy creates a broken map—AI can't navigate to the right section if hierarchy is inconsistent

### Critical Patterns
- **Six heading levels**: `#` through `######` (but levels 5-6 are rarely needed—avoid deep nesting in specifications)
- **Correct Hierarchy**: One Level 1 title, multiple Level 2 sections, Level 3 subsections nested under their parent Level 2
- **Hash Syntax + Space**: `# Title` (not `#Title`); space is required for markdown parser to recognize heading
- **Single Level 1**: Use `#` only once for document title; subsequent sections use `##`
- **Common Sections**: Professional specs follow pattern: `# Title`, `## Problem`, `## Features`, `## Expected Output`

### AI Collaboration Keys
- **Navigation landmarks**: AI uses headings as search anchors—can locate "Features section" instantly without reading entire document
- **Structure parsing**: AI counts heading levels to understand document scope ("this spec has 4 main sections")
- **JSON tree visualization**: Ask AI to show your heading structure as a JSON tree to verify hierarchy is correct
- **Code generation mapping**: "## Features" with 5 items tells AI "generate 5 functions"; structure → implementation

### Common Mistakes
- Forgetting space after `#` symbols (`#Title` instead of `# Title`)
- Using multiple Level 1 headings (multiple `#` sections confuses document structure)
- Skipping heading levels (going from `# Title` directly to `### Subsection`)
- Using levels 5-6 in specifications (too deep—refactor into separate sections instead)
- Vague heading names ("Section A" instead of "Features" or "Installation")

### Connections
- **Builds on**: Lesson 1 understanding that structure enables AI parsing
- **Leads to**: Lesson 3 (lists under headings), Lesson 4 (code blocks after headings), Lesson 5 (complete spec)
- **Task Tracker App**: This lesson adds heading structure to your ongoing specification project
