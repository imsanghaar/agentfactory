### Core Concept
Links (`[text](url)`), images (`![alt](url)`), and text emphasis (`**bold**`, `*italic*`) complete your markdown toolkit for writing specifications, READMEs, and documentation that AI agents can parse effectively.

### Key Mental Models
- **Links as context anchors**: Link text tells AI what a resource provides without following the link—`[Python documentation](...)` gives context; `[click here](...)` gives none
- **Images need alt text**: Modern AI is multimodal and CAN see images, but when reading markdown as text, it only sees alt text—so descriptive alt text helps in both scenarios
- **Emphasis signals priority**: Bold (`**must**`) indicates hard requirements; italic (`*recommended*`) indicates optional items—AI uses this to distinguish priorities
- **Quick Rule for syntax**: `[text](url)` = "take me there" (link); `![text](url)` = "show it here" (image)—the `!` means display inline

### Critical Patterns
- **Link syntax**: `[descriptive text](url)` — link text should describe the destination, not "click here"
- **Image syntax**: `![alt text describing what image shows](image-url)` — note leading `!`
- **Emphasis syntax**: `**bold**` for critical, `*italic*` for optional, `***both***` for absolute requirements
- **Relative paths**: `./images/diagram.png` for local images (common when AI generates diagrams)
- **URL hygiene**: No spaces in URLs; use clean paths or %20 encoding

### AI Collaboration Keys
- **Link text provides context**: AI uses link text to understand resources without following links (which it often can't do)
- **Alt text provides fallback context**: Descriptive alt text like "Task list showing 3 pending items" helps when AI reads markdown as text (not rendered)
- **Emphasis affects priority**: AI interprets `**must**` as non-negotiable and `*recommended*` as optional
- **Reference-style links**: For many links, definitions at bottom keep text clean: `[python]: https://docs.python.org/`

### Common Mistakes
- Vague link text (`[click here]` or `[link]` instead of descriptive text)
- Forgetting `!` for images (creates link instead of embedded image)
- Using italic for placeholders (use `<placeholder>` in inline code instead)
- Overusing bold (if everything is bold, nothing stands out)
- Non-descriptive alt text ("screenshot" instead of "menu showing 5 options")
- Broken relative paths (image doesn't exist at specified location)

### Connections
- **Builds on**: Lessons 1-4 (markdown structure: headings, lists, code blocks)
- **Completes**: Task Tracker App specification exercise across all lessons
- **Enables**: Writing complete READMEs and project documentation with resources, visuals, and priority signals
