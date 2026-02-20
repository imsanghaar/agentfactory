### Core Concept
Context engineering is the discipline of controlling what your AI sees to produce consistent, high-quality output—finding the smallest set of high-signal tokens that maximize the likelihood of your desired outcome.

### Key Mental Models
- **Context > Prompts**: Your prompt is 0.1% of what the model processes; the other 99.9% is context. Optimizing prompts while ignoring context is "polishing the doorknob while the house is on fire."
- **Context Rot Types**: Degradation manifests as Poisoning (outdated info persists), Distraction (irrelevant content dilutes attention), Confusion (similar concepts conflate), or Clash (contradictory instructions compete).
- **Token Budget Awareness**: Everything the AI "sees" consumes limited context window capacity—context engineering is designing what goes in, where it's positioned, and when it loads.

### Critical Patterns
- Use `/context` to see what's consuming your attention budget before you work
- Diagnose which of the four rot types is affecting your session before taking action
- Recognize that autocompact handles most context management, but manual intervention is sometimes needed

### Common Mistakes
- Treating "prompt engineering" as the primary lever when context is 99.9% of the input
- Assuming AI got "dumber" when quality degrades—usually context got corrupted
- Ignoring baseline cost: much of your context is consumed before you type anything

### Connections
- **Builds on**: Chapter 1's Digital FTE concept (consistent agents require consistent context)
- **Leads to**: Signal vs Noise audit for quality control (Lesson 2)
