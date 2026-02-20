---
sidebar_position: 12
title: "Chapter 4: Context Engineering Quiz"
description: "Diagnostic assessment testing decision-making, tradeoff reasoning, and failure detection in real-world context engineering scenarios"
keywords:
  [
    "context engineering quiz",
    "attention budget",
    "CLAUDE.md optimization",
    "context zones",
    "progress files",
    "memory injection",
    "context isolation",
    "context rot",
    "instruction drift",
    "diagnostic assessment",
  ]
chapter: 4
proficiency_level: B2
layer: 2
estimated_time: "60 mins"
chapter_type: Assessment
---

# Chapter 4 Quiz: Context Engineering

This diagnostic assessment evaluates your judgment in real-world context engineering scenarios. Each question presents a situation requiring you to reason about tradeoffs, identify failure modes, and select appropriate interventions.

**Target audience:** Practitioners who will architect long-running agent systems.

<Quiz
title="Chapter 4: Context Engineering Diagnostic Assessment"
questionsPerBatch={30}
questions={[
{
question: "Session 12 of a multi-week contract review project. The agent correctly identified a liability cap issue in Session 3 but now recommends accepting the same clause pattern it previously flagged. Progress files exist but haven't been updated since Session 8. What's the root cause?",
options: [
"Model capability failure where the agent lacks sufficient parameters to maintain cross-session consistency in legal reasoning",
"Position sensitivity issue where the liability criteria are placed in Zone 2 of CLAUDE.md instead of Zone 1",
"Context rot: Session 3's decision is buried in accumulated noise and no longer receiving attention",
"Token budget exhaustion where context utilization is too high for reliable recall of prior session decisions"
],
correctOption: 2,
explanation: "This is classic context rot from an unmaintained progress file. The Session 3 decision wasn't recorded in the progress file, so Session 12 has no access to it. The decision exists only in stale conversation history that may have been compacted or forgotten. Progress files only work when they're updated at session boundaries.",
source: "Lesson 7: Progress Files"
},
{
question: "Your CLAUDE.md contains 180 lines. After running the 4-question audit, you find: 60 lines pass Q1 (Claude would ask), 40 lines pass Q2-Q4 but fail Q1, and 80 lines fail all questions. A colleague suggests compressing the 80 'noise' lines to 20 lines. What's wrong with this approach?",
options: [
"Compressed noise is still noise—it consumes instruction budget without providing signal, just more efficiently",
"Compression is computationally slower than deletion and introduces latency for noise reduction operations",
"20 lines is still far too many tokens for Zone 2 content with its limited attention allocation",
"Compression often loses important contextual nuance that might become relevant in edge-case scenarios later"
],
correctOption: 0,
explanation: "Compressed noise is still noise. The 80 lines that fail all 4 questions shouldn't be compressed—they should be deleted or moved to external files. The instruction limit (~150-200) doesn't care about line efficiency; it cares about distinct instructions. Turning 80 lines of noise into 20 denser lines of noise still wastes ~20 instruction slots.",
source: "Lesson 2: Signal vs Noise"
},
{
question: "A research synthesis agent processes 30 papers across 5 sessions. By Session 5, it misattributes findings—citing Paper 7's methodology for Paper 19's conclusions. Context utilization is only at 45%. What's happening?",
options: [
"The agent's training data contains gaps in academic citation conventions causing systematic misattribution errors",
"The vector database is returning semantically similar but incorrect document chunks for each paper retrieval",
"The agent needs a significantly larger context window to hold all 30 papers simultaneously without confusion",
"Context isolation failure: papers with similar topics are conflating in the shared context space"
],
correctOption: 3,
explanation: "At 45% utilization, this isn't a budget problem—it's a context isolation problem. When similar papers share the same context, their details conflate. The solution isn't more context; it's structured isolation. Process papers in batches with fresh context per batch, returning only structured summaries to the orchestrator for final synthesis.",
source: "Lesson 9: Context Isolation"
},
{
question: "You're at 72% context utilization with critical architectural decisions made this session. You need to continue working. Which compaction instruction demonstrates the deepest understanding of context engineering?",
options: [
"/compact Keep everything important and discard things that are clearly not needed",
"/compact Preserve: the decision to use JWT over sessions with rationale (security + statelessness), the 3 files modified (auth.ts, middleware.ts, config.ts), current task (adding refresh tokens). Discard: the exploration of OAuth alternatives in messages 8-15, the debugging tangent about expired tokens.",
"/compact Preserve decisions and discard exploration phases",
"/compact Focus on code changes and remove all discussion threads"
],
correctOption: 1,
explanation: "Effective compaction requires specificity. 'Keep everything important' and 'preserve decisions' are too vague—Claude must guess what you mean. The third option explicitly names: (1) the specific decision with its rationale, (2) concrete file references, (3) current task state, and (4) specific content to discard with message references. This precision ensures critical context survives.",
source: "Lesson 6: Context Lifecycle"
},
{
question: "An orchestrator spawns three parallel subagents: Legal reviews contract terms, Finance analyzes pricing, Operations assesses implementation timeline. Each returns 8,000 tokens of analysis. The orchestrator's synthesis is confused and contradictory. What architectural flaw caused this?",
options: [
"The subagents lacked shared constraints, so they made incompatible assumptions about the contract's baseline terms",
"Parallel execution is inherently unstable and produces inconsistent results for complex multi-domain analysis tasks",
"8,000 tokens per subagent exceeds the safe return threshold and overwhelms the orchestrator's synthesis capacity",
"The orchestrator's context window is too small to synthesize three large analyses without significant context loss"
],
correctOption: 0,
explanation: "Parallel subagents operate in isolation—that's the point. But isolation means they can't coordinate assumptions. If Legal assumes a 3-year term, Finance assumes 5-year, and Operations assumes 1-year, their analyses are internally consistent but mutually incompatible. The fix: provide shared constraints in each delegation prompt before subagents diverge.",
source: "Lesson 9: Context Isolation"
},
{
question: "A marketing campaign agent was given brand voice guidelines in the session's first message. At turn 47, its copy sounds generic and off-brand. Context is at 55%. The guidelines are in CLAUDE.md Zone 1. What's the most likely cause?",
options: [
"Zone 1 placement only provides primacy advantage at session start and mid-session recall follows different attention patterns",
"55% context utilization is already too high for reliable brand voice retention and consistent style application",
"The guidelines need to be restated in the chat every 10 messages to maintain consistent agent attention",
"The conversation history has accumulated enough noise to dilute even Zone 1 content"
],
correctOption: 3,
explanation: "Zone 1 placement gives primacy advantage, but attention is relative to total context. At 55% with 47 turns of history, the message history now dominates the context. Even well-positioned CLAUDE.md content gets proportionally less attention. The solution: either compact to reduce history's share, or re-inject brand guidelines in the current message (recency effect).",
source: "Lesson 3: Lost in the Middle"
},
{
question: "Session 5 of a consulting engagement. The agent keeps suggesting deliverables that don't match client requirements. Progress file shows 'Decisions Made' is empty. 'Session Log' shows only dates and file lists. What's the critical missing element?",
options: [
"More detailed session timestamps with exact times to allow accurate reconstruction of the decision sequence",
"Links to all referenced external documents so future sessions can reload the source materials directly",
"Rationale for decisions—not just what was decided, but WHY and what alternatives were rejected",
"Task decomposition into smaller granular items with assigned owners and completion criteria"
],
correctOption: 2,
explanation: "A progress file that tracks WHAT without WHY enables context reconstruction but not decision continuity. When Session 5 asks 'Should we use approach A or B?', it doesn't know Session 2 already analyzed this and chose A because of constraint X. Without rationale and rejected alternatives, every session can re-debate settled questions—or worse, choose differently.",
source: "Lesson 7: Progress Files"
},
{
question: "Your PreToolUse hook extracts Claude's thinking block and queries a vector database for relevant memories. The same 3 memories keep returning for different tool calls across 20 turns. What optimization is missing?",
options: [
"Use UserPromptSubmit hook instead of PreToolUse to generate more stable and diverse query vectors",
"Deduplication layer: track (memory_id, thinking_hash) pairs with TTL to skip recently-injected memories",
"Increase the top_k parameter to return more results per query and improve result diversity",
"Add more memories to the vector database to improve retrieval diversity and reduce repetition rate"
],
correctOption: 1,
explanation: "Without deduplication, the same relevant memories get re-injected repeatedly. Each injection consumes tokens without adding new information. The fix: cache recent (memory_id, thinking_hash) pairs with a ~5 minute TTL. If the same memory was injected for similar thinking recently, skip it. This prevents redundant token consumption.",
source: "Lesson 8: Memory Injection"
},
{
question: "Agent A (research) completes its work and passes context to Agent B (analysis). Agent B produces excellent analysis but references 'the approach we rejected in exploration phase' which confuses the final output. What pattern would prevent this?",
options: [
"Clean context pattern: Agent A returns only a structured summary; Agent B receives fresh context with just the summary",
"Use a stateful handoff protocol with explicit 'ignore these sections' markers embedded throughout the transfer",
"Instruct Agent A to delete all exploration branches from its context before initiating the handoff process",
"Allocate a larger context window to accommodate both Agent A's exploration and Agent B's final analysis work"
],
correctOption: 0,
explanation: "This is the dirty slate problem. Agent A's exploration was useful for Agent A but is noise for Agent B. The clean context pattern isolates this: Agent A returns a structured summary of findings (not process), and Agent B receives fresh context containing only that summary plus the task. Agent B never sees Agent A's rejected approaches.",
source: "Lesson 9: Context Isolation"
},
{
question: "You're debugging an agent that inconsistently applies your coding standards. Investigation reveals: CLAUDE.md is 52 lines (under 60), standards are in Zone 1, context utilization is 35%. What should you check next?",
options: [
"Whether the standards are written as actionable instructions vs vague guidelines",
"Whether the model version has recently changed and introduced different behavior",
"Whether the coding standards file was modified recently and contains stale or conflicting directives",
"Whether Zone 1 needs to be expanded with more detailed code examples and sample outputs"
],
correctOption: 3,
explanation: "Position is good (Zone 1), length is good (52 lines), budget is good (35%). The remaining variable is signal quality. 'Use good coding practices' is noise—it's vague and Claude knows it already. 'Use 2-space indentation, early returns, JSDoc for all functions' is signal—specific, actionable, different from defaults. Audit the standards for specificity.",
source: "Lesson 2: Signal vs Noise"
},
{
question: "A 4-day-old session contains critical decisions about database schema. You need to continue this work. What's the correct approach?",
options: [
"Use /compact on the old session aggressively to compress history, then continue from the compacted state",
"Use claude --continue to resume the session with its full accumulated context intact",
"Start fresh session, read progress file to reconstruct state, reference old session only if specific details needed",
"Use /resume to pick from recent sessions in the session browser and select this specific one"
],
correctOption: 2,
explanation: "Sessions expire after ~3 days. A 4-day-old session has accumulated drift, implicit assumptions that no longer hold, and context pollution that compaction can't fully clean. The 3-day rule exists because resuming old sessions creates more confusion than starting fresh. Extract decisions to progress file, then use fresh context.",
source: "Lesson 6: Context Lifecycle"
},
{
question: "Your agent reviews contracts daily. You've documented 15 'red flag' patterns in CLAUDE.md Zone 1. Despite this, it catches only 8-10 patterns per review. Investigation shows Zone 1 is now 45 lines. What's the diagnosis?",
options: [
"Zone 1 should only be ~10% of CLAUDE.md; 45 lines exceeds the primacy advantage threshold",
"15 contract flag patterns is simply too many for reliable recall regardless of their position in the file",
"Each flag pattern needs more detailed explanation text to ensure Claude can recognize the pattern accurately",
"Zone 1 content needs to be migrated to a separate dedicated rules file for better attention allocation"
],
correctOption: 0,
explanation: "Zone 1's primacy advantage depends on scarcity. When Zone 1 is ~6 lines of a 60-line file (10%), each line gets premium attention. At 45 lines, Zone 1 isn't premium anymore—you've diluted the primacy effect. Move stable reference patterns to Zone 2 or external docs. Reserve Zone 1 for the 3-5 most critical constraints.",
source: "Lesson 3: Lost in the Middle"
},
{
question: "An agent working on a feature implementation drifts from 'add user authentication' to 'refactor the entire user module.' The original task was clear at turn 1. Now at turn 25, it's building unnecessary abstractions. What intervention addresses the root cause?",
options: [
"Add 'NEVER refactor without explicit permission' to CLAUDE.md Zone 1 to prevent future unauthorized scope expansion",
"Memory injection via PreToolUse hook: re-inject the original task scope when the agent's thinking diverges",
"Add '/compact Focus on authentication only' to compress the session and restore original task focus",
"Restart the entire session with a more tightly constrained and unambiguous task prompt"
],
correctOption: 1,
explanation: "This is workflow drift—the agent's current thinking has diverged from the original intent. UserPromptSubmit injection only fires once at session start; by turn 25, that context is stale. PreToolUse injection fires before each tool call, using the agent's current thinking to trigger relevant memory retrieval. When thinking mentions 'refactoring,' the hook can re-inject 'Scope: authentication only.'",
source: "Lesson 8: Memory Injection"
},
{
question: "Your CLAUDE.md contains 'For quality review process, see docs/review-checklist.md'. The agent sometimes follows the checklist, sometimes ignores it. What's the progressive disclosure failure?",
options: [
"External file references don't work reliably across sessions and lose their binding between executions",
"The checklist file is too long for the agent to process efficiently within available token budget",
"The reference should be placed in Zone 3 rather than Zone 2 for better workflow trigger association",
"The reference lacks a trigger condition—it doesn't specify WHEN to read the file"
],
correctOption: 3,
explanation: "Progressive disclosure requires trigger conditions. 'See docs/review-checklist.md' tells Claude the file exists but not when to read it. Better: 'Before finalizing any deliverable, read docs/review-checklist.md'. The trigger ('before finalizing') creates a clear moment when the agent should load the external context. Without triggers, external files are suggestions, not workflows.",
source: "Lesson 2: Signal vs Noise"
},
{
question: "Session 7 of a long project. The agent asks 'Should we use TypeScript or JavaScript?' when Session 2 already decided TypeScript with documented rationale. Your progress file has a 'Decisions Made' section. What's missing?",
options: [
"Session initialization protocol: the agent isn't reading the progress file at session start",
"More detailed rationale for the TypeScript decision including all the alternatives that were evaluated",
"Links to the Session 2 conversation transcript where the original TypeScript decision was made",
"The TypeScript decision should be recorded in CLAUDE.md instead of the progress file"
],
correctOption: 0,
explanation: "A well-structured progress file is useless if the agent doesn't read it. The session initialization protocol should be in CLAUDE.md Zone 3: 'At session start: 1. Read claude-progress.txt. 2. Confirm understanding of current state. 3. Then begin work.' Without this protocol, each session starts fresh, ignoring accumulated decisions.",
source: "Lesson 7: Progress Files"
},
{
question: "You're building a document review pipeline: Agent A reads documents, Agent B analyzes findings, Agent C writes the report. Testing shows Agent C consistently produces the best output when you manually copy-paste Agent B's summary. What does this reveal?",
options: [
"Manual curation always produces better results than automated handoffs because human judgment filters noise",
"Copy-paste operations introduce beneficial whitespace and formatting changes that improve Agent C's comprehension",
"Agent C works better with less context—the automated pipeline is passing too much raw process alongside the summary",
"Agent B's automatically generated summary is lower quality than what you manually select and paste"
],
correctOption: 2,
explanation: "When manual copy-paste beats automated handoff, the pipeline is leaking process into product. Your automated handoff likely passes Agent B's full output (including reasoning scaffolding, exploration, intermediate steps) rather than just the structured summary. Agent C receives noise that competes with signal. Fix: ensure Agent B returns only structured output, not its working process.",
source: "Lesson 9: Context Isolation"
},
{
question: "A consulting agent's recommendations vary in quality—sometimes brilliant, sometimes generic. Analysis shows quality correlates with session length: quality drops sharply after turn 35-40. Context utilization reaches ~70% at turn 40. What's the mechanism?",
options: [
"API rate limiting mechanisms activate after approximately 40 turns and throttle model performance",
"Quality degradation at 70% is the U-shaped attention curve hitting its middle trough",
"The 70% threshold triggers automatic context compaction which silently loses important background context",
"The agent degrades in longer sessions because accumulated conversation history introduces inconsistent patterns"
],
correctOption: 1,
explanation: "This is the attention budget ceiling. At 70%, the model must make attention tradeoffs—it can't give full focus to everything. Quality degradation isn't random; it follows the physics of context windows. The fix: proactive compaction at 60-65% to stay in the green zone where full attention is available. Don't wait for degradation to start.",
source: "Lesson 1: What Is Context Engineering?"
},
{
question: "Your agent maintains a 'memories/learned-preferences.md' file that grows as it discovers user preferences. After 3 months, the file is 400 lines. Quality has been declining. What's the underlying problem?",
options: [
"The preferences file should be stored in a vector database rather than markdown for semantic retrieval",
"400 lines exceeds the practical size limit that Claude can fully process within a single context read",
"The learned preferences should be consolidated directly into CLAUDE.md instead of a separate tracking file",
"Preferences change over time; older preferences may contradict newer ones"
],
correctOption: 3,
explanation: "Preference files without lifecycle management become context poisoning sources. A preference from month 1 may contradict month 3's refined understanding. Without version control, expiration, or conflict resolution, the file accumulates contradictions. Older preferences can override newer ones if they're positioned earlier. Implement preference decay or periodic consolidation.",
source: "Lesson 1: What Is Context Engineering?"
},
{
question: "Three independent reviewers analyze the same document (legal, financial, compliance perspectives). Each returns ~3,000 tokens. The orchestrator synthesizes well. You change to sequential review (legal → financial → compliance) to 'build on each other's work.' Quality drops. Why?",
options: [
"Later reviewers are influenced by earlier reviewers' framing, losing independent perspective",
"Sequential execution runs substantially slower than parallel and introduces latency-related quality degradation",
"Accumulating 3,000 tokens per sequential reviewer creates too much layered context for the orchestrator",
"The orchestrator's synthesis logic was designed for parallel input format and can't handle sequential structure"
],
correctOption: 0,
explanation: "The value of multiple perspectives comes from independence. When reviewers see each other's work, they anchor on previous framings instead of bringing fresh analysis. Legal's 'high-risk' label influences Financial to look for risks instead of opportunities. The parallel pattern preserved independence; sequential destroyed it. Choose patterns based on whether cross-influence helps or hurts.",
source: "Lesson 9: Context Isolation"
},
{
question: "You notice your agent occasionally produces output that violates conventions it followed perfectly 20 turns ago. Context is at 52%. CLAUDE.md is well-structured. What's the most likely explanation?",
options: [
"The agent needs explicit convention reminders injected into the chat approximately every 10 turns",
"Model version inconsistency causes unpredictable instruction-following behavior across different session lengths",
"The convention instruction is in the middle 80% of CLAUDE.md (Zone 2) where recall drops",
"52% context utilization is high enough to cause early attention degradation in long conversations"
],
correctOption: 2,
explanation: "Position sensitivity affects mid-session recall. Convention instructions in Zone 2 get ~30% less attention than Zone 1 or Zone 3 content. Even at comfortable utilization (52%), the U-shaped attention curve deprioritizes middle content. Move critical conventions to Zone 1 (always-apply rules) or Zone 3 (workflow triggers), not Zone 2 (reference material).",
source: "Lesson 3: Lost in the Middle"
},
{
question: "Your agent architecture uses PreToolUse hooks for memory injection. A new team member asks: 'Why not just put all relevant memories in the system prompt?' What's the fundamental limitation they're missing?",
options: [
"Memories stored in system prompts are visible to end users, which creates a significant privacy and security risk",
"System prompts can't be updated mid-session; PreToolUse enables dynamic injection based on evolving needs",
"Injecting memories into system prompts costs significantly more tokens than hook-based dynamic injection",
"System prompts have a fixed maximum size limit that would be quickly exhausted by a comprehensive memory store"
],
correctOption: 1,
explanation: "System prompts are static—they're set at session start and can't change based on what happens during the session. At turn 1, you don't know what memories will be relevant at turn 30. PreToolUse hooks solve this by injecting memories dynamically, using the agent's current thinking (what it's about to do) to query for contextually relevant information. Static prompts can't adapt to workflow drift.",
source: "Lesson 8: Memory Injection"
},
{
question: "A subagent returns a 500-token summary instead of its full 8,000-token analysis. The orchestrator's final output misses important nuances from the analysis. What's the correct fix?",
options: [
"Instruct the subagent to flag whenever it believes important nuances might be lost during compression",
"Pass the full 8,000-token analysis instead of the summary to avoid any information loss at handoff",
"Increase summary length to 2,000 tokens to provide more room for nuanced detail in the compressed output",
"Restructure summary format: 'Summary + Supporting Evidence + Caveats' to ensure nuances survive compression"
],
correctOption: 3,
explanation: "The tradeoff isn't length—it's structure. A 500-token unstructured summary loses nuance. A 500-token structured summary ('Summary: X. Evidence: Y, Z. Caveats: A, B') preserves critical details through explicit sections. The problem isn't too-aggressive compression; it's compression without structure. Nuances survive in the 'Caveats' section.",
source: "Lesson 9: Context Isolation"
},
{
question: "Your CLAUDE.md says: 'Follow best practices for security.' A security audit reveals the agent approved code with SQL injection vulnerabilities. What type of noise is this instruction?",
options: [
"Redundant noise: Claude already knows general security best practices from training data and doesn't need reminding",
"Stale noise: Security best practices have evolved significantly since Claude's training cutoff date",
"Position noise: The instruction is ineffective because it is placed in Zone 2 rather than Zone 1",
"Vague noise: 'Best practices' is unactionable; it should specify 'parameterize all queries, validate all inputs, escape all outputs'"
],
correctOption: 0,
explanation: "This is vague noise—instructions Claude can't act on. 'Follow best practices' provides no decision criteria. Does Claude know YOUR definition of best practices? Which practices take priority when they conflict? Actionable signal: 'Security requirements: parameterize all SQL queries (no string concatenation), validate input types before processing, sanitize output for XSS.' Specificity enables compliance.",
source: "Lesson 2: Signal vs Noise"
},
{
question: "You're designing an agent for long-running legal case analysis spanning weeks. The case involves multiple parties, evolving precedents, and strategic decisions. Which architecture provides the strongest foundation?",
options: [
"Fresh sessions daily with comprehensive progress files capturing all decisions and strategic reasoning",
"Single long session with aggressive compaction to manage context growth across the full duration",
"Shared memory layer (progress file + vector DB) with stateless subagents for specific analyses",
"Multiple sessions using --continue to maintain the full conversation thread and accumulated decisions"
],
correctOption: 2,
explanation: "Long-running complex work requires: (1) persistent state that survives session boundaries (progress file), (2) searchable knowledge that doesn't fit in context (vector DB), and (3) isolation for specific analyses to prevent cross-contamination (stateless subagents). Single sessions accumulate rot. --continue degrades after 3 days. This hybrid architecture scales to weeks.",
source: "Lessons 7, 8, 9: Progress Files, Memory Injection, Context Isolation"
},
{
question: "An agent correctly identified a conflict-of-interest issue in Session 2 and flagged it. Session 6 is reviewing a similar pattern but doesn't flag it. The issue: Session 2's insight was recorded as 'Flagged COI issue' without specifics. What's the failure mode?",
options: [
"Session 2's learning wasn't captured as transferable pattern—it was recorded as event, not rule",
"The progress file should include a direct link to the original Session 2 conversation for context",
"Conflict-of-interest detection requires real-time memory injection via hooks rather than progress file storage",
"The agent requires additional COI detection training to reliably identify these patterns across sessions"
],
correctOption: 1,
explanation: "Recording 'Flagged COI issue' documents WHAT happened, not WHAT TO DO NEXT TIME. A learning becomes transferable when it's captured as pattern: 'COI Pattern: When Party A has financial relationship with Party B and Party B is decision-maker on Party A's contract, flag for review.' Session 6 can apply this rule. Session 6 cannot interpret 'Flagged COI issue' as instruction.",
source: "Lesson 7: Progress Files"
},
{
question: "Your context budget breakdown shows: System prompt (8%), CLAUDE.md (12%), Tool definitions (15%), Message history (45%), Tool outputs (15%), Reserve (5%). What's the warning sign?",
options: [
"CLAUDE.md at 12% is too high and is consuming budget that should be reserved for message history",
"Tool definitions at 15% suggests too many tools are enabled simultaneously for this workflow type",
"Message history at 45% is above the safe threshold and will cause attention degradation immediately",
"Reserve at 5% is dangerously low—no buffer for unexpected file reads or complex responses"
],
correctOption: 3,
explanation: "A 5% reserve is a single large file read away from the 70% degradation threshold. With 45% message history + 15% tool outputs, you're at 60% consumption. One 15,000-token document read would push you to 67%. The reserve buffer should be 10-15% to accommodate unexpected needs. At 5%, you're operating without safety margin.",
source: "Lesson 10: The Playbook"
},
{
question: "A code review agent catches style issues early in sessions but misses them later. You discover it's running the linter and including full output (2,000+ tokens) for each file. What's the optimization?",
options: [
"Summarize linter output: 'Style issues: 3 indentation, 2 naming conventions in lines 45, 78, 92' instead of full verbose output",
"Increase the context window allocation specifically reserved for tool outputs to prevent budget exhaustion",
"Run the linter less frequently—only on changed files rather than every file in the review batch",
"Move linting to a separate pre-processing step that runs before the agent session initializes"
],
correctOption: 0,
explanation: "Tool outputs are often verbose because tools are designed for humans who want details. Agent context engineering requires summarization. '2,000 tokens of linter output' becomes '50 tokens of actionable summary.' The summary preserves decision-relevant information (what to fix, where) while freeing budget for the actual review work. Verbose tool outputs are a hidden context drain.",
source: "Lesson 10: Token Budgeting Strategies"
},
{
question: "You're troubleshooting an agent that 'forgets' important context. Investigation reveals: CLAUDE.md is lean (45 lines), context utilization is 48%, instructions are in Zone 1. But the agent still ignores critical rules. What's left to check?",
options: [
"Whether the rules are formatted as interrogative questions versus imperative commands in the instruction text",
"Whether a recent model version update changed the underlying instruction-following behavior",
"Whether the rules are truly actionable—can Claude actually follow them, or are they aspirational?",
"Whether Zone 1 needs to be expanded with more content to reinforce the critical rules through repetition"
],
correctOption: 2,
explanation: "After ruling out position, length, and budget, check signal quality. 'Ensure code quality' isn't actionable—Claude can't verify if code has 'quality.' 'All functions under 50 lines, all public methods documented, no any types' IS actionable. Aspirational rules get ignored because there's no clear compliance criteria. Convert aspirations to verifiable instructions.",
source: "Lesson 2: Signal vs Noise"
},
{
question: "Your multi-agent system has an orchestrator and 4 subagents. Quality is good, but latency is high—tasks take 3x longer than expected. Analysis shows subagents run sequentially. What architectural change addresses this?",
options: [
"Reduce the total subagent count from 4 to 2 and consolidate their responsibilities to minimize coordination overhead",
"Identify which subagent tasks are independent and run those in parallel; only sequence tasks with genuine dependencies",
"Increase the context allocation for each subagent to allow faster individual processing and reduce per-agent time",
"Implement result caching so subagent outputs can be reused across multiple orchestration cycles"
],
correctOption: 1,
explanation: "Sequential execution is only necessary when tasks have dependencies (Agent B needs Agent A's output). Many multi-agent workflows have independent tasks: Legal review, Financial analysis, and Compliance check don't depend on each other—they can run simultaneously. Map your dependencies, parallelize independents. 3x latency suggests most tasks could be parallel.",
source: "Lesson 9: Context Isolation"
},
{
question: "A marketing agent was instructed at turn 1: 'All copy must be approved by brand team before use.' At turn 38, it generates copy and marks it 'Ready for publication.' What mechanism would catch this?",
options: [
"Memory injection at turn 38 that re-injects the brand approval requirement when output generation is detected",
"Stronger and more emphatic wording in the original instruction to increase its weight in attention distribution",
"Adding the approval instruction to both Zone 1 and Zone 3 of CLAUDE.md for maximum recall redundancy",
"Workflow-level verification: a post-generation check that validates approval status before marking 'ready'"
],
correctOption: 3,
explanation: "This is an instruction that should be enforced structurally, not relied upon for recall. Position and memory injection help recall, but verification ensures compliance. A workflow that checks 'Is brand_approved = true?' before allowing 'ready' status catches violations regardless of whether the agent 'remembers' the rule. Critical constraints need verification, not just instruction.",
source: "Lesson 10: The Playbook"
},
{
question: "You've implemented all context engineering techniques: optimized CLAUDE.md, progress files, memory injection, context isolation. Quality is excellent for 2 weeks, then starts degrading. What's the maintenance failure?",
options: [
"The context engineering techniques you implemented have a natural expiration period and need systematic replacement",
"The underlying model received an update after deployment that changed behavior in ways incompatible with your setup",
"Context engineering techniques need to be manually re-applied and reconfigured periodically as a scheduled task",
"Context engineering is a continuous discipline—memories accumulate conflicts, progress files bloat, CLAUDE.md drifts from actual practice"
],
correctOption: 3,
explanation: "Context engineering isn't 'set and forget.' Memories accumulate contradictions as preferences evolve. Progress files bloat with decisions that are now obvious. CLAUDE.md drifts as actual workflows change. The 2-week degradation timeline suggests accumulated entropy. Regular audits catch drift: review progress file for staleness, audit CLAUDE.md quarterly, consolidate contradictory memories.",
source: "Chapter synthesis"
}
]}
/>
