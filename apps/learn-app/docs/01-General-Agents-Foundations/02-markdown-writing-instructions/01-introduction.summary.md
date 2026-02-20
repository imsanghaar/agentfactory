### Core Concept
Markdown is structured text that creates a bridge between human intent (what you want to build) and machine interpretation (what AI agents understand), forming the **Intent Layer of AIDD** where specifications flow down to AI reasoning and code generation.

### Key Mental Models
- **Structured vs Unstructured**: Structured text (markdown) removes ambiguity by using explicit labels (headings, lists) that AI agents can parse; unstructured paragraphs force AI to guess
- **Three-Layer AIDD**: Markdown is Layer 1 (your intent specification) → AI Reasoning (Layer 2) → Code Generation (Layer 3)
- **Intent Layer Philosophy**: You control the spec; AI implements it. Change the spec, AI rebuilds to match—this keeps you in control
- **Dual-Nature Format**: Markdown is simultaneously human-readable (no special software) and machine-parseable (structured for AI agents)

### Critical Patterns
- **Specification Quality Effect**: Same information as unstructured paragraph vs markdown structure produces dramatically different AI outputs
- **GitHub README Convention**: Professional developers use markdown for README.md files (not Word/TXT) because it's version-control friendly and renders beautifully
- **Markdown Flavors**: CommonMark is the base standard; GitHub Flavored Markdown (GFM) adds tables, task lists, and strikethrough
- **Semantic Meaning in Structure**: Headings and lists communicate semantic meaning—AI extracts this structure to understand scope, dependencies, and relationships

### AI Collaboration Keys
- **LLM Tokenization**: Structured markdown gives AI clearer token boundaries and "attention cues"—a heading like `## Features` tells the model everything below relates to features
- **Structure parsing**: AI uses markdown structure to identify scope, dependencies, and relationships between requirements
- **Specification by example**: Showing expected output in code blocks gives AI concrete targets instead of interpretations
- **Verification is critical**: AI makes mistakes—always verify AI responses against lesson rules and test specific claims

### Common Mistakes
- Treating markdown as "just formatting" rather than specification language that AI parses
- Writing unstructured paragraphs when structure (lists, headings) would clarify scope
- Mixing explicit requirements with vague descriptions in same specification
- Blindly trusting AI feedback without verification (ask AI to explain reasoning, test claims)

### Connections
- **Builds on**: GitHub README familiarity, intuitive understanding that clear writing helps communication
- **Leads to**: Lesson 2 (headings), Lesson 3 (lists), Lesson 4 (code blocks), Lesson 5 (links, images, emphasis)
- **Practical application**: Every AI prompt, GitHub documentation, and technical specification uses markdown; this is foundational to AI-native development
