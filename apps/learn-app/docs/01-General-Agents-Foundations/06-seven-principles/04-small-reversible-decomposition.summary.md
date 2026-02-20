### Core Concept

Breaking complex problems into small, independently verifiable steps that can be easily rolled back is the key to managing complexity in agentic workflows. Like building with Lego bricks instead of sculpting clay—if something goes wrong, you pop off the bad brick instead of reworking the whole sculpture.

### Key Mental Models

- **Lego vs Clay**: Atomic changes (Lego) snap together and can be individually replaced. Monolithic changes (Clay) require reworking adjacent parts when something goes wrong. Always choose Lego.
- **Atomic Change**: The smallest unit of work that can be independently verified, makes sense on its own, and can be reverted without breaking other work. One logical concern per commit.
- **Debugging Mathematics**: Bug-finding cost grows exponentially with change size. Ten small tested changes beat one large change every time.
- **Revert, Don't Fix**: When something breaks, your first instinct should be `git checkout` not debugging. Reverting is faster, safer, and preserves your mental energy.
- **Step Zero**: Before any implementation, always start with a plan. "Before we start, create an implementation plan. List the files you'll change and what each change does."

### Key Facts

- **Cognitive limit**: Humans hold about 7±2 items in working memory—large changes exceed this
- **AI has context limits too**: Claude's context window means massive changes crowd out the understanding needed to complete them well
- **Small iteration timeline**: Many small verified steps complete features faster with lower stress than big-batch approaches

### Critical Patterns

- Four decomposition strategies: Vertical Slicing, Horizontal Slicing, Dependency-First, Test-First
- Good commit boundaries: one concern per commit, each leaves code working, each independently revertable
- Prompt for Step Zero: "Before we implement, create an implementation plan listing files and changes"
- The Revert-Don't-Fix prompt: "That broke something. Let's revert and try a different approach instead of debugging"

### Common Mistakes

- Micro-commits (too fine-grained—group related tiny fixes into one atomic change)
- Mixed concerns (unrelated changes in one commit—makes reverting one impossible)
- Untested middle states (commits that don't compile—intermediate states should always work)
- Skipping Step Zero (diving into implementation without a plan—leads to rework)
- Debugging instead of reverting (spending 30 minutes fixing when 30 seconds of revert would suffice)

### Connections

- **Builds on**: Principle 3 (Verification)—small changes make verification tractable
- **Leads to**: Principle 5 (State Persistence)—documenting decomposed plans in files ensures continuity
- **Synergy**: Git commits are both decomposition units AND safety mechanisms (Principle 6)
