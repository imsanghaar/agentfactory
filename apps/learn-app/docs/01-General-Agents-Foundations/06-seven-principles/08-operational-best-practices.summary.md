### Core Concept

Productive Claude Code sessions require workflow discipline, not AI knowledge. The four-phase workflow (Explore→Plan→Implement→Commit) transforms messy exploration into systematic progress, while course correction tools let you recover from wrong directions without losing work.

### Key Mental Models

- **Planning is Cheap, Implementation is Expensive**: Catching misunderstandings during planning costs minutes; fixing them during implementation costs hours. When unsure whether to plan, plan.
- **The Time Machine Combo**: Single `Esc` is your steering wheel (stops Claude mid-response). Double `Esc` or `/rewind` opens the checkpoint menu—your time machine to go back before you steered wrong.
- **The Rule of Two**: If Claude misses the mark twice on the same fix, STOP. Don't try a third time. `/clear` and start over with a better prompt that includes what you learned from the failures.
- **The Golden Reset**: After an interview, copy the clean specification into a fresh session. Signal-dense context beats conversation tangents.

### Critical Patterns

- Enter Plan Mode (`Shift+Tab`) for exploration before making changes—this is Principle 6 (Constraints) in action
- Use `Ctrl+G`/`Cmd+G` to edit plans before implementation
- Press `Esc` twice or `/rewind` to access checkpoint menu
- Use `--continue` or `--resume` to pick up previous sessions
- Configure `/permissions` with a standard safe list: `ls, cat, grep, find` (read), `npm test, pytest` (verify), `git status, git diff` (observe)
- Apply the interview pattern with one line: "Don't code yet. Interview me until you have a 100% clear spec."

### Common Mistakes

- **Kitchen Sink Session**: Mixing unrelated tasks pollutes context. Fix: One session, one purpose. `/clear` between unrelated work.
- **Correction Loop**: Repeated corrections add noise. Fix: Apply the Rule of Two—after two misses, fresh start beats third attempt.
- **Bloated CLAUDE.md**: 200+ lines dilutes focus. Fix: Keep under 60 lines; move domain knowledge to skills.
- **Trust-Then-Verify Gap**: Accepting plausible output without running it. Fix: "It looks right" isn't verification—running it is.
- **Infinite Exploration**: Open-ended investigation fills context. Fix: Scope narrowly or use subagents for research.

### Connections

- **Builds on**: Chapter 4's context engineering fundamentals (`/clear`, `/compact`, context window)
- **Leads to**: The Seven Principles that explain *why* these operational patterns work
- **Plan Mode = Principle 6**: Read-only constraint that prevents changes until you're ready
