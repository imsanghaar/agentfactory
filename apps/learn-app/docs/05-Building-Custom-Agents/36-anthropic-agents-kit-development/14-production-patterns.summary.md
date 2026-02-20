### Core Concept
Three hosting patterns: Ephemeral (spin up, complete, terminate), Long-Running (persistent session across days), Hybrid (ephemeral tasks + long-running synthesis). Configure sandbox security and context compaction for sustainable 24/7 operation.

### Key Mental Models
- **Hosting decision tree**: Needs memory? No=ephemeral. Runs 24/7? Yes=long-running. Parallel tasks? Yes=hybrid
- **Sandbox isolation**: enabled=true for development freedom; enabled=false for production control
- **Context compaction**: PreCompact hook archives key knowledge before context window fills

### Critical Patterns
- Ephemeral: No resume, max_turns bounded, fresh session each request
- Long-running: `resume=session_id`, persistent state, context compaction at 80% threshold
- Hybrid: Cheap ephemeral analysis (Haiku) + expensive synthesis (Opus)
- PreCompact: Archive customers, patterns, open tickets; keep recent messages

### AI Collaboration Keys
- Match hosting pattern to economics: ephemeral = per-request pricing; long-running = subscription
- Sandbox development differently than production (auto=true vs auto=false)
- Design compaction strategy before deploying 24/7 agents

### Common Mistakes
- Using long-running for one-off tasks (wasted persistence overhead)
- Deploying without compaction strategy (context fills, agent fails)
- Sandbox autoAllowBash in production (dangerous)

### Connections
- **Builds on**: Cost Tracking and Billing (Lesson 13)
- **Leads to**: TaskManager Capstone (Lesson 15)
