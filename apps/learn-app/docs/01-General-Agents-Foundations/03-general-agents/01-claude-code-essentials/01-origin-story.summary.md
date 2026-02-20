### Core Concept
Claude Code represents a paradigm shift from passive AI assistance (copy-paste from chat) to agentic AI collaboration—where AI reads your actual files, proposes specific changes to your codebase, and executes with your approval.

### Key Mental Models
- **Passive vs. Agentic**: Chat AI is a consultant giving generic advice over the phone; agentic AI is a pair programmer sitting next to you, looking at your screen
- **Product Overhang**: The capability to be a development partner already existed inside Claude—it was waiting for a product (filesystem access) to unlock it. The model didn't need to become smarter; it needed to *see* what developers were working on
- **Friction Removal > Feature Addition**: The value isn't faster coding—it's eliminating context-switching, copy-paste workflows, and manual integration so you can focus on creative problem-solving
- **Self-Building Proof**: ~90% of Claude Code was written by Claude Code itself—evidence that agentic AI can sustain complex work when given proper access

### Key Facts (as of mid-2025)
- **Timeline**: September 2024 (Boris Cherny's prototype) → November 2024 (dogfooding) → May 2025 (public launch)
- **Adoption curve**: 20% day 1 → 50% day 5 → 80%+ daily usage at GA
- **Productivity**: 5 PRs/day per engineer (vs typical 1-2)
- **Self-building**: ~90% of the codebase written by Claude Code itself
- **Revenue**: $500M+ annual run-rate from word-of-mouth adoption

### Critical Patterns
- Agentic workflow: describe task → Claude reads files → proposes specific changes → you approve → Claude executes
- Terminal integration enables: direct file system access, real-time execution and error handling, Git integration, and developer workflow alignment
- Trust through transparency: see exact diffs before approving file changes, see command outputs in real-time

### Common Mistakes
- Thinking "AI makes coding faster" (copy-paste friction often makes passive AI slower than no AI)
- Believing agentic AI replaces developers (it removes execution friction, not creative problem-solving)
- Assuming terminal-based means harder to use (terminal integration removes context-switching friction)
- Continuing to copy-paste context when context-aware tools would see your actual code

### Connections
- **Builds on**: Basic understanding of AI assistants and terminal usage
- **Leads to**: Practical Claude Code workflows, configuration with CLAUDE.md, and hands-on usage patterns
