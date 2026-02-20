### Core Concept
Unordered and ordered lists communicate whether items are **independent** (features, requirements—use bullets) or **dependent** (steps, sequences—use numbering), allowing AI agents to understand dependencies and generate appropriately independent vs sequential code.

### Key Mental Models
- **Order Matters Test**: "Do these items need to happen in sequence?" YES = ordered (numbered), NO = unordered (bullets)
- **Semantic Information via List Type**: Unordered under "Features" tells AI "develop independently"; ordered under "Installation" tells AI "execute in sequence"
- **Dependency Chains**: Ordered lists communicate causal relationships (Step 2 depends on Step 1) that AI uses for workflow generation
- **Nested lists vs more headings**: Use nested lists for closely related sub-items; use new headings when topics deserve their own section

### Critical Patterns
- **Unordered syntax**: `-`, `*`, or `+` followed by space (`- item`)—all three are equivalent
- **Ordered syntax**: `1.` followed by space (`1. step`)—markdown auto-renumbers (even `1. 1. 1.` renders as `1. 2. 3.`)
- **Numbering behavior**: Starting with `11.` continues as `11, 12, 13...`—use this intentionally or start with `1.`
- **Nested lists**: Indent with 2-4 spaces to create sub-items under parent items
- **Blank line handling**: Adding blank lines between items may change rendering—be consistent

### AI Collaboration Keys
- **Feature count extraction**: AI counts items in unordered feature list to know how many functions to generate
- **Sequence understanding**: Numbered steps tell AI this is a workflow; it generates sequential scripts
- **Error prevention**: Correct list type prevents AI from running installation steps out of order or treating features as ranked priority
- **Modular code**: Unordered feature lists encourage AI to generate modular, independent functions

### Common Mistakes
- Using ordered lists for features (creates false impression of priority when items are independent)
- Using unordered lists for installation steps (AI may execute commands out of order)
- Forgetting space after dash or number (`-item` or `1.item`)
- Inconsistent bullet characters in same document (pick one: `-`, `*`, or `+`)
- Not realizing markdown auto-renumbers (typing `1. 1. 1.` still renders as `1. 2. 3.`)

### Connections
- **Builds on**: Lesson 2 (headings create context for lists)
- **Leads to**: Lesson 4 (code blocks showing implementation of listed features), Lesson 5 (complete spec)
- **Task Tracker App**: This lesson adds feature lists and menu options to your ongoing specification
