## Agent Teams: The Network Pattern in Practice

You just saw three subagent design patterns: Stateless, Stateful, and Shared (Network). The Stateless and Stateful patterns are well-established. But the Shared pattern raises a practical question: how do you actually coordinate multiple agents that need to communicate with each other, share state, and self-organize around a problem?

Claude Code's **agent teams** feature is a native implementation of the Network pattern. The key evolution from subagents: subagents report results back to their caller only. They cannot talk to each other. Agent teams are separate Claude Code instances that can message each other directly, share a task list, and self-coordinate without routing every communication through the orchestrator.

This changes what's possible. With subagents, the orchestrator is a bottleneck for all communication. Agent A discovers something relevant to Agent C, but must report it to the orchestrator, which must then relay it to Agent C. With agent teams, Agent A messages Agent C directly. The lead coordinates the overall mission, but teammates handle tactical communication on their own.

### Subagents vs Agent Teams

| Dimension | Subagents | Agent Teams |
| :--- | :--- | :--- |
| **Context** | Own context window; results return to caller | Own context window; fully independent |
| **Communication** | Report results back to main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost** | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |

Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.

### When Agent Teams Add Value

Agent teams shine in specific scenarios where inter-agent communication produces better results than isolated reports:

- **Research and review**: Multiple teammates investigate different aspects of a problem simultaneously, then share and challenge each other's findings. A security reviewer, a performance analyst, and a test coverage auditor working the same codebase produce richer results when they can question each other's conclusions than when they report independently to the orchestrator.

- **New modules or features**: Teammates each own a separate piece without stepping on each other. A frontend specialist, a backend specialist, and a test writer can coordinate directly about interface contracts instead of routing every question through a lead.

- **Debugging with competing hypotheses**: Teammates test different theories in parallel and converge faster. When the root cause is unclear, sequential investigation anchors on the first plausible explanation. Multiple independent investigators actively trying to disprove each other's theories surface the actual root cause more reliably.

- **Cross-layer coordination**: Changes that span frontend, backend, and tests, each owned by a different teammate, benefit from direct communication about shared interfaces and dependencies.

Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently on separate files or concerns. For sequential tasks, same-file edits, or work with many dependencies, subagents are more effective. The pattern selection table from earlier still applies -- agent teams are the practical implementation of "Shared (Network)" for cases where inter-agent dialogue matters.

### When to Use Which

The original pattern selection table covered Stateless, Stateful, and Shared. Here is how agent teams fit alongside subagents within the Stateless and Shared categories:

| Your situation | Use subagents | Use agent teams |
| :--- | :--- | :--- |
| Three independent research tasks that produce separate reports | Yes -- each reports back to orchestrator, no inter-agent dialogue needed | Overkill -- coordination overhead adds cost without benefit |
| Code review from security, performance, and testing perspectives where findings inform each other | Possible but limited -- security finding about auth can't reach test reviewer directly | Yes -- reviewers can challenge each other and cross-reference findings |
| Multi-day project with persistent shared state | No -- subagents are ephemeral, one-shot workers | Yes -- shared task list persists, teammates can be replaced as work evolves |
| Quick fact-check or file lookup | Yes -- single focused task, minimal overhead | No -- spawning a team for a quick lookup wastes tokens |
| Parallel implementation of three independent modules | Either works -- if modules have clean interfaces, subagents suffice | Better if modules share interfaces that need negotiation |

The decision comes down to one question: **do the workers need to talk to each other?** If yes, agent teams. If no, subagents.

### Practical: Starting Your First Agent Team

Agent teams are experimental and disabled by default. Enable them in your settings:

```json
// settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Then describe the team structure you want in natural language:

```
Create an agent team to review this project from different angles:
- One teammate focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

**Output:**

```
Created team "project-review" with 3 teammates:
  - security-reviewer: Reviewing for security vulnerabilities
  - performance-analyst: Checking performance impact
  - test-validator: Validating test coverage

Task list created with 3 tasks. Teammates are starting work.
```

Here is how agent teams operate in practice:

- **The lead coordinates work and synthesizes results.** The session where you create the team becomes the lead for its lifetime. The lead breaks work into tasks, assigns them, and combines findings when teammates finish.

- **Teammates work independently in their own context windows.** Each teammate loads the same project context (CLAUDE.md, MCP servers, skills) but does not inherit the lead's conversation history. Task-specific details must go in the spawn prompt -- this is why specifying clear, focused prompts for each teammate matters.

- **A shared task list coordinates who does what.** Tasks have three states: pending, in progress, and completed. Tasks can depend on other tasks -- a pending task with unresolved dependencies cannot be claimed until those dependencies complete. Teammates self-claim available work when they finish a task, and file locking prevents two teammates from claiming the same task simultaneously.

- **Teammates can message each other directly.** This is the fundamental difference from subagents. When a security reviewer discovers that the authentication module has no rate limiting, it can message the test coverage teammate directly: "Check whether rate limiting tests exist for the auth module." No routing through the lead required.

**Interacting with teammates:**

| Action | Keyboard shortcut | What it does |
| :--- | :--- | :--- |
| Select teammate | **Shift+Up/Down** | Cycle through active teammates to message one directly |
| View task list | **Ctrl+T** | Toggle the shared task list showing all pending, in-progress, and completed tasks |
| Delegate mode | **Shift+Tab** | Restrict the lead to coordination-only tools, preventing it from implementing tasks itself |
| View teammate session | **Enter** (on selected teammate) | See full output of a teammate's work in progress |
| Interrupt teammate | **Escape** (while viewing) | Stop a teammate's current turn to redirect their approach |

**Delegate mode** deserves special attention. Without it, the lead sometimes starts implementing tasks itself instead of waiting for teammates. This defeats the purpose of the team -- the lead should be coordinating, not coding. Delegate mode restricts the lead to spawning, messaging, shutting down teammates, and managing tasks. Use it when you want strict separation between orchestration and implementation.

### Context Engineering for Agent Teams

Every best practice for agent teams maps directly to context engineering principles from this chapter.

**"Give teammates enough context."** Teammates load CLAUDE.md automatically, but they do not inherit the lead's conversation history. If the lead spent ten minutes discussing the authentication architecture with you, none of that context reaches the teammate who reviews the auth module. Task-specific details must go in the spawn prompt:

```
Spawn a security reviewer teammate with the prompt: "Review the
authentication module at src/auth/ for security vulnerabilities.
Focus on token handling, session management, and input validation.
The app uses JWT tokens stored in httpOnly cookies.
Report any issues with severity ratings."
```

This is Strategy 3 (Include Critical Context in Delegation Prompt) from the context amnesia section, applied at the team level. The more specific the spawn prompt, the less time the teammate spends orienting and the more time it spends on actual analysis.

**"Size tasks appropriately."** Too small and coordination overhead exceeds benefit. Too large and teammates work too long without check-ins, increasing the risk of wasted effort. The recommendation is 5-6 tasks per teammate as a starting point. This is the Signal vs Noise principle from Lesson 2 applied to task granularity: each task should be large enough to produce meaningful signal but small enough that the lead can detect problems before they compound.

**"Avoid file conflicts."** Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files. This is context isolation applied to file system state, not just token context. The same principle that keeps Agent A's research artifacts out of Agent C's attention budget also keeps Agent A's file edits from colliding with Agent C's file edits.

These are not new principles. They are the same context engineering fundamentals you have been learning throughout this chapter, applied at a different scale. The pattern holds: clean signal in, clean signal out, regardless of whether "in" means a single agent's context window or a team of six coordinating across a codebase.

### Case Study: 16 Agents Build a C Compiler

Anthropic researcher Nicholas Carlini used 16 parallel Claude instances to build a C compiler from scratch. Over nearly 2,000 Claude Code sessions and approximately 2 billion input tokens, the agents produced a 100,000-line Rust-based compiler that can compile Linux 6.9 across x86, ARM, and RISC-V architectures. The compiler achieves a 99% pass rate on standard compiler test suites and can also compile QEMU, FFmpeg, SQLite, PostgreSQL, and Redis. Total cost: approximately $20,000.

The project was not a toy demonstration. It produced a working compiler that handles real-world software. And the engineering challenges Carlini encountered read like a chapter summary of everything you have learned about context engineering.

**Test suites as signal.** High-quality test suites directed agent behavior without human supervision. But the test harness had to be clean. As Carlini documented, the harness should avoid printing noise that obscures the actual error. Instead, it should log important information to files and keep error output on single lines for automated grep searches. This is Lesson 2 (Signal vs Noise) at compiler scale: the agents spent attention diagnosing real problems, not parsing noisy output.

**Documentation for agent onboarding.** Agents maintained extensive READMEs and progress files updated frequently with current status. When a new agent session started, these documents helped it orient quickly without human intervention. This is the context amnesia workaround (Strategy 2: Master-Clone) working at production scale: every fresh agent reads the project brief before starting its task.

**Randomized test sampling.** The harness included a fast mode that runs a 1% or 10% random sample of test cases, deterministic per-agent but random across instances. This enabled parallel debugging: each agent worked on different failure subsets simultaneously. This is decomposition for parallelism, the same principle behind the clean context pattern, applied to the test suite itself.

**Clear error messaging.** Pre-computed statistics and clear error messages reduced the computational overhead of understanding failures. Agents could immediately see what failed and why, rather than sifting through thousands of lines of output. This is context quality at the infrastructure level: the environment itself was engineered to present clean signal to the agents.

| Lesson from Compiler Project | Context Engineering Principle | Where You Learned It |
| :--- | :--- | :--- |
| Clean test harness output | Signal vs Noise | Lesson 2 |
| READMEs for agent orientation | Master-Clone architecture | This lesson (Strategy 2) |
| Randomized test sampling | Decomposition for parallelism | This lesson (Clean Context Pattern) |
| Pre-computed error statistics | Context quality | Lesson 4 (structured context) |

The takeaway: at 16-agent scale, the differentiator was not the model or the tools. It was context quality. The same model, the same tools, but disciplined context engineering produced a compiler that passes real-world test suites. Sloppy test harnesses, verbose output, or missing documentation would have turned those 2 billion tokens into noise instead of progress.

This principle scales down, too. Whether you are coordinating 16 agents building a compiler or 3 teammates reviewing a contract, the work succeeds or fails based on the quality of context each agent receives. Clean signal in, clean results out.

## Try With AI

### Prompt 4: Experience Agent Teams for Parallel Review

Enable agent teams in your settings, then try this:

```
Create an agent team to analyze [a project or codebase you're working on].

Spawn three teammates:
- A "Researcher" who investigates the project structure and documents
  key patterns
- A "Critic" who identifies potential problems, risks, and improvements
- A "Architect" who proposes structural improvements based on findings

Have them share findings with each other and debate their conclusions.
Synthesize a final assessment when they converge.
```

**What you're learning:** Agent teams demonstrate the network pattern from this lesson in action. Notice how each teammate operates with clean context (they don't inherit the lead's history), how they coordinate through the shared task list, and how inter-agent communication produces richer analysis than isolated subagents reporting back independently. The debate structure -- teammates challenging each other's findings -- is impossible with subagents, which can only report to their caller.

### References

- Anthropic. (2026). "[Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)." Claude Code Documentation.
- Anthropic. (2026). "[Building a C Compiler with Parallel Claude Agents](https://www.anthropic.com/engineering/building-c-compiler)." Anthropic Engineering Blog.
