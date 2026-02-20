### Core Concept
Context has a lifecycle with actionable zones: Green (0-50%, work freely), Yellow (50-70%, monitor), Orange (70-85%, compact NOW), Red (85-95%, emergency), Black (95%+, reset required). The `/clear` vs `/compact` decision depends on whether the task is complete and whether context is poisoned.

### Key Mental Models
- **Zone-Based Action**: Quality holds steady until ~70%, then degrades. Monitor in Yellow, take action in Orange—waiting until Black means compaction overhead might push you over.
- **Clear vs Compact Decision**: Clear when task is complete, context is poisoned, or switching to unrelated work. Compact when same task continues and you need to preserve decisions but free up space.
- **The 3-Day Rule**: Conversations become "un-resumable" after 3-4 days—too many tangents, too much drift. Start fresh instead of resuming stale sessions.

### Critical Patterns
- Check `/context` regularly—every 10 messages when in Yellow zone
- Use custom compaction instructions: `/compact Preserve: [decisions, file list]. Discard: [tangents, rejected options].`
- Save checkpoints before compacting or clearing—externalize progress so it survives context operations
- Use `--continue` to resume recent sessions, `--resume` to pick from session list

### Common Mistakes
- Compacting poisoned context: if context contains outdated decisions or wrong directions, compaction preserves the poison. Clear instead.
- Not saving checkpoints: if compaction loses something important, you have no recovery point
- Waiting too long: compacting at 85%+ is emergency territory; aim for 70% proactive intervention

### Connections
- **Builds on**: Tacit knowledge and memory systems (Lesson 5)
- **Leads to**: Progress files for long-horizon work (Lesson 7)
