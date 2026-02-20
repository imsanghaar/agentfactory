---
sidebar_position: 10
title: "Chapter 5: Spec-Driven Development Quiz"
---

# Chapter 5 Quiz

Test your understanding of Spec-Driven Development with Claude Code. This quiz covers all concepts from the chapter including vibe coding failure modes, the three SDD levels, the four-phase workflow, and the decision framework.

<Quiz
title="Spec-Driven Development Assessment"
questions={[
{
question: "A developer asks Claude to 'add authentication' and receives JWT code. They then ask for 'OAuth support' and Claude replaces the JWT implementation entirely. Which failure mode is this?",
options: [
"Context loss from iterative discovery",
"Pattern violations from architectural misalignment",
"Assumption drift from implicit decisions",
"Specification gap from missing constraints"
],
correctOption: 0,
explanation: "This is context loss—each iteration loses discoveries from previous turns. The JWT implementation decisions were lost when focus shifted to OAuth. Context loss occurs when newer requests override earlier work because previous decisions fade from attention. Pattern violations would involve architectural conflicts; assumption drift involves reasonable but wrong guesses; specification gap isn't a defined failure mode.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "Claude creates a new database table for notifications when your project already uses a unified user_preferences table. Which failure mode does this represent?",
options: [
"Context loss from conversation history",
"Assumption drift from reasonable defaults",
"Pattern violations from unknown architecture",
"Specification ambiguity from vague requirements"
],
correctOption: 2,
explanation: "This is pattern violations—generated code ignores existing project architecture. Without knowledge of your specific patterns (all user data in user_preferences), Claude applies general best practices that conflict with your design. Context loss involves losing previous decisions; assumption drift involves wrong guesses about requirements; specification ambiguity isn't a defined failure mode.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "You asked for 'notification support' and Claude assumed you needed push notifications, email integration, and SMS fallback. You only needed simple in-app toasts. Which failure mode occurred?",
options: [
"Pattern violations from codebase conflicts",
"Context loss from session limitations",
"Architecture mismatch from documentation gaps",
"Assumption drift from implicit defaults"
],
correctOption: 3,
explanation: "This is assumption drift—Claude made reasonable but wrong guesses about your requirements. Without explicit constraints, Claude fills gaps with sensible defaults that may not match your actual needs. Pattern violations involve architectural conflicts; context loss involves losing previous decisions; architecture mismatch isn't a defined failure mode.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "Which statement best describes why specifications prevent the three vibe coding failure modes?",
options: [
"Specs replace conversation with documentation",
"Specs provide complete context upfront",
"Specs eliminate the need for iteration",
"Specs automate the implementation process"
],
correctOption: 1,
explanation: "Specifications prevent failure modes by providing the complete picture upfront—what exists, what to build, what NOT to build, and success criteria. This addresses context loss (requirements persist), assumption drift (explicit constraints), and pattern violations (architecture documented). Specs don't eliminate iteration; they front-load the important decisions.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "A team writes specifications to guide implementation but discards them after the feature ships. They create new specs for future changes. Which SDD level is this?",
options: [
"Spec-Anchored with living documentation",
"Spec-as-Source with code regeneration",
"Spec-Lite with minimal overhead",
"Spec-First with throwaway artifacts"
],
correctOption: 3,
explanation: "This is Spec-First—the most common level where specs guide implementation but are discarded afterward. The benefit is zero maintenance overhead; the cost is no specification exists for future reference. Spec-Anchored maintains both; Spec-as-Source regenerates code; Spec-Lite isn't a defined level.",
source: "Lesson 2: The Three Levels of SDD"
},
{
question: "A company commits specifications alongside code and requires spec updates before any code changes. Code reviewers verify spec alignment. Which SDD level is this?",
options: [
"Spec-Anchored with maintenance discipline",
"Spec-First with review requirements",
"Spec-as-Source with verification steps",
"Spec-Driven with compliance checks"
],
correctOption: 0,
explanation: "This is Spec-Anchored—both specification and code are maintained artifacts. The discipline requires spec changes before code changes and reviewer verification. This provides onboarding documentation and architectural records but doubles maintenance burden. Spec-First discards specs; Spec-as-Source regenerates code; Spec-Driven isn't a defined level.",
source: "Lesson 2: The Three Levels of SDD"
},
{
question: "A framework marks generated code files with '// GENERATED FROM SPEC - DO NOT EDIT' and regenerates implementation when specs change. Which SDD level is this?",
options: [
"Spec-Anchored with generation markers",
"Spec-First with automation tools",
"Spec-as-Source with code regeneration",
"Spec-Strict with edit protection"
],
correctOption: 2,
explanation: "This is Spec-as-Source—the most radical approach where specifications are the primary artifact and code is regenerated on demand. This experimental level (explored by Tessl) faces determinism challenges: identical specs don't produce identical code. Spec-Anchored maintains both; Spec-First is throwaway; Spec-Strict isn't defined.",
source: "Lesson 2: The Three Levels of SDD"
},
{
question: "Why does Spec-as-Source face determinism challenges that limit its practical adoption?",
options: [
"AI models cannot understand specifications",
"Specifications require manual code review",
"Identical specs produce different code each time",
"Code generation tools are unreliable"
],
correctOption: 2,
explanation: "Spec-as-Source struggles because identical specifications do not produce identical code. Variable names differ, control flow varies, comments appear or disappear. This makes git diffs meaningless, debugging harder, and performance unpredictable. AI can understand specs; review is still needed; tools work but non-deterministically.",
source: "Lesson 2: The Three Levels of SDD"
},
{
question: "A solo developer building a weekend project should typically use which SDD level?",
options: [
"Spec-as-Source for rapid iteration",
"Spec-Anchored for documentation benefits",
"No specification for maximum speed",
"Spec-First with throwaway artifacts"
],
correctOption: 3,
explanation: "Spec-First is appropriate for personal projects without team coordination. The spec prevents vibe coding failures, ensures complete context, and results in working code—then gets discarded. No maintenance burden, but also no documentation for later. Spec-Anchored's overhead isn't justified; Spec-as-Source is experimental; no specs risks vibe coding failures.",
source: "Lesson 2: The Three Levels of SDD"
},
{
question: "A team skips the Refinement phase and goes straight from Specification to Implementation. Which failure is most likely to occur?",
options: [
"Specification, Research, Implementation, Refinement",
"Research, Specification, Refinement, Implementation",
"Ambiguities surface mid-implementation causing costly pivots",
"Refinement, Research, Specification, Implementation"
],
correctOption: 1,
explanation: "Skipping Refinement means ambiguities in the spec are never surfaced before coding begins. These unresolved questions emerge during implementation—when changes are expensive rather than cheap. The correct sequence (Research, Specification, Refinement, Implementation) front-loads ambiguity resolution precisely to avoid mid-implementation pivots.",
source: "Lesson 3: The Four-Phase Workflow"
},
{
question: "A developer finishes writing the specification but immediately starts coding without running any investigation agents first. Which phase deliverable is missing?",
options: [
"Implementation tasks with clear dependencies listed",
"Refined specification with resolved design questions",
"Written summaries from multiple investigation agents",
"Committed code with atomic reversible changes"
],
correctOption: 2,
explanation: "The Research phase produces written summaries from multiple parallel investigation agents. Each subagent investigates a specific aspect (patterns, architecture, best practices) and returns findings. These summaries feed into specification writing. Skipping Research means the spec is based on assumptions, not evidence. Tasks come from Implementation; refined specs from Refinement; committed code from Implementation.",
source: "Lesson 3: The Four-Phase Workflow"
},
{
question: "Why does the specification become the 'source of truth' that survives session restarts?",
options: [
"Claude automatically saves specifications to disk",
"Specifications are stored in version control systems",
"The spec is encrypted for long-term persistence",
"Written specs persist as files while conversations disappear"
],
correctOption: 3,
explanation: "Specifications persist as markdown files while conversation history disappears when sessions end. Tomorrow's Claude can read today's spec and understand what was decided, why, constraints, and success criteria. This captures accumulated decisions that would otherwise be lost. Claude doesn't auto-save; VCS helps but isn't the primary reason.",
source: "Lesson 3: The Four-Phase Workflow"
},
{
question: "What distinguishes SDD's approach to review from traditional AI coding?",
options: [
"SDD reviews at phase gates, not during coding",
"SDD requires no human review at all",
"SDD automates all review processes",
"SDD delays review until deployment"
],
correctOption: 0,
explanation: "SDD separates planning from execution and reviews at phase gates (after research, after spec, after refinement) rather than constantly during coding. This reduces approval fatigue because you review plans, not every file edit. Traditional AI coding interleaves review with generation, causing constant context-switching.",
source: "Lesson 3: The Four-Phase Workflow"
},
{
question: "What happens if you skip the Research phase and go directly to specification?",
options: [
"Implementation still proceeds but pivots more often",
"Claude refuses to generate code without prior research",
"Task extraction from the spec becomes much harder",
"The specification is based on assumptions not evidence"
],
correctOption: 3,
explanation: "Skipping Research means your specification is based on assumptions rather than evidence from investigation. You might miss existing patterns, alternative approaches, or critical constraints that research would have revealed. Implementation still works but may need more pivots.",
source: "Lesson 3: The Four-Phase Workflow"
},
{
question: "What is the prompt pattern that triggers parallel research in Claude Code?",
options: [
"Research this topic thoroughly for me",
"Spin up multiple subagents for your research task",
"Investigate this using parallel processing threads",
"Start concurrent research threads for each aspect"
],
correctOption: 1,
explanation: "'Spin up multiple subagents for your research task' is the specific trigger phrase. When Claude sees this instruction with a research goal, it spawns 3-5 independent agents, each investigating a specific aspect. Other phrasings may work but this is the canonical pattern from practice.",
source: "Lesson 4: Phase 1 - Parallel Research"
},
{
question: "Why does each research subagent operate with fresh context rather than shared context?",
options: [
"To reduce computational costs of research",
"To prevent cross-contamination of findings",
"To comply with API rate limits",
"To enable faster sequential processing"
],
correctOption: 1,
explanation: "Context isolation prevents cross-contamination. When Agent 2 investigates WebSockets, it doesn't carry assumptions from Agent 1's CRDT analysis. This means findings are independent—if one agent's approach is wrong, it doesn't affect others. Each agent starts clean and reports pure findings.",
source: "Lesson 4: Phase 1 - Parallel Research"
},
{
question: "When parallel research agents report conflicting approaches for the same problem, what does this indicate?",
options: [
"A genuine design decision needs to be made",
"One agent made an error in research",
"The research should be run again",
"The specification scope is too broad"
],
correctOption: 0,
explanation: "Conflicting findings indicate a genuine design decision. Agent 1 recommending approach A while Agent 3 recommends approach B means you have real options with tradeoffs. This is valuable information—you're not making assumptions that slip through. Conflicts surface decisions that need human judgment.",
source: "Lesson 4: Phase 1 - Parallel Research"
},
{
question: "A team decomposes authentication research into: 'How does authentication work?' and 'What are authentication best practices?' What is wrong with this decomposition?",
options: [
"Both questions are too specific and narrowly scoped",
"Questions overlap and lack focused independent boundaries",
"Sequential tasks that must build on each other first",
"Broad general questions that produce flexible open results"
],
correctOption: 1,
explanation: "Effective decomposition creates independent threads where each agent can complete without information from others, each has a focused answerable question, and each knows scope boundaries. These two questions heavily overlap and are too vague—both could produce the same findings. Effective threads like 'token management', 'session handling', 'provider integration' are independent and bounded.",
source: "Lesson 4: Phase 1 - Parallel Research"
},
{
question: "Research on an authentication system should investigate token management, session handling, provider integration, and security measures. Why are these good decomposition threads?",
options: [
"They require sequential completion in order",
"They share common implementation details",
"They are independent aspects that together cover authentication",
"They focus on the same authentication patterns"
],
correctOption: 2,
explanation: "These threads work because each investigates an independent aspect of authentication. Token management can be researched without knowing session patterns; provider integration is separate from security measures. Together they cover the full authentication domain. Good decomposition is independent, focused, bounded, and complementary.",
source: "Lesson 4: Phase 1 - Parallel Research"
},
{
question: "A spec is missing the Non-Goals section entirely. What risk does this create during implementation?",
options: [
"Reference Architecture Analysis becomes harder to structure",
"Goals and Risks sections become redundant without Non-Goals",
"Introduction and Methods sections lose their framing context",
"Claude may implement reasonable features that were explicitly out of scope"
],
correctOption: 0,
explanation: "The four-part template is: Reference Architecture Analysis (what good looks like), Current Architecture Analysis (where you are), Implementation Plan (the path), Implementation Checklist (task extraction). Plus Constraints and Success Criteria sections. Without Non-Goals (part of Constraints), Claude may add caching, logging, or other reasonable features that the team explicitly decided not to build now.",
source: "Lesson 5: Phase 2 - Writing Effective Specs"
},
{
question: "Why are explicit constraints often more important than requirements in specifications?",
options: [
"Constraints are much easier to verify than requirements are",
"Constraints reduce the overall specification length significantly",
"Constraints enable faster and more predictable implementation",
"Constraints prevent Claude from making reasonable but wrong choices"
],
correctOption: 3,
explanation: "Constraints prevent reasonable-but-wrong choices. Without 'Do NOT add Redis' Claude might reasonably add it for caching. Without 'Do NOT modify database schema' Claude might optimize storage. Constraints encode your specific context that differs from general best practices Claude would otherwise apply.",
source: "Lesson 5: Phase 2 - Writing Effective Specs"
},
{
question: "A success criterion states the system should be 'fast and reliable.' What's wrong with this?",
options: [
"It should specify implementation details",
"It cannot be measured or tested",
"It doesn't include error handling",
"It focuses on positive outcomes only"
],
correctOption: 1,
explanation: "'Fast and reliable' cannot be tested. Effective criteria must be measurable: 'P95 latency < 100ms' instead of 'fast'; 'Zero data loss in conflict scenarios' instead of 'reliable.' If you can't write a test for a criterion, it's not a criterion—it's a wish.",
source: "Lesson 5: Phase 2 - Writing Effective Specs"
},
{
question: "Specification checklist items should be 'atomic' for task extraction. What does atomic mean in this context?",
options: [
"The smallest possible code change",
"Work requiring exactly one hour",
"Changes to a single file only",
"Self-contained work explainable in one sentence"
],
correctOption: 3,
explanation: "Atomic means self-contained units of work you can explain to a junior developer in one sentence. 'Create /lib/cache.ts with LRU implementation' is atomic. 'Set up the system' is not—it's too vague to delegate. Atomic isn't about size or time but about clarity and completeness.",
source: "Lesson 5: Phase 2 - Writing Effective Specs"
},
{
question: "Why is 'Use a HashMap with String keys' an anti-pattern in specifications?",
options: [
"HashMaps have poor performance characteristics",
"It prescribes HOW instead of WHAT behavior",
"Strings are not valid HashMap keys",
"It doesn't specify the value type"
],
correctOption: 1,
explanation: "Specifications should describe behavior, not implementation. 'Use HashMap' prescribes HOW; 'Returns user by ID in O(1) time' describes WHAT behavior is needed. Claude often knows better implementation patterns—by specifying behavior, you get the benefit of its knowledge.",
source: "Lesson 5: Phase 2 - Writing Effective Specs"
},
{
question: "What is the prompt pattern that triggers the interview phase for specification refinement?",
options: [
"Review my specification and flag any potential issues",
"Identify and list the gaps in this specification",
"Prepare a set of interview questions for this spec",
"Use the ask_user_question tool to surface any ambiguities before we implement"
],
correctOption: 3,
explanation: "'Use the ask_user_question tool to surface any ambiguities before we implement' triggers Claude's interview mode. This shifts Claude from implementation to investigation—it reads critically and asks questions about anything unclear, unstated, or problematic. The roles reverse: Claude asks, you answer.",
source: "Lesson 6: Phase 3 - Refinement via Interview"
},
{
question: "An ambiguity discovered during spec refinement costs 10 minutes to resolve. The same ambiguity found during production would cost 8-16 hours. What multiplier does this represent?",
options: [
"Approximately 5x more expensive",
"Approximately 10x more expensive",
"Approximately 50-100x more expensive",
"Approximately 2x more expensive"
],
correctOption: 2,
explanation: "The 10x multiplier stated in the lesson is conservative. 10 minutes during refinement versus 8-16 hours in production (480-960 minutes) represents approximately 50-100x cost difference. This demonstrates why front-loading ambiguity resolution has massive ROI.",
source: "Lesson 6: Phase 3 - Refinement via Interview"
},
{
question: "Which category of interview questions addresses 'Should we migrate existing data or start fresh?'",
options: [
"Data Decisions category",
"Conflict Resolution decisions",
"Pattern Selection choices",
"Boundary Conditions limits"
],
correctOption: 0,
explanation: "Data migration questions fall under Data Decisions—how existing information transitions to the new system. Other data questions include schema mismatch handling and transition period management. Conflict Resolution covers multi-user scenarios; Pattern Selection covers architectural choices; Boundary Conditions covers limits.",
source: "Lesson 6: Phase 3 - Refinement via Interview"
},
{
question: "The spec says 'handle conflicts optimistically.' Developer meant 'last write wins' but Claude interpreted 'prompt user to resolve.' Which interview category would have caught this?",
options: [
"Data Decisions about migration strategies",
"Failure Recovery about error handling paths",
"Conflict Resolution about disagreements between systems",
"Boundary Conditions about scale and limits"
],
correctOption: 2,
explanation: "Conflict Resolution questions address what happens when systems disagree. 'What's the conflict resolution strategy? Last write wins? User resolves? Merge automatically?' would have surfaced this ambiguity. The term 'optimistic' meant different things to developer and Claude.",
source: "Lesson 6: Phase 3 - Refinement via Interview"
},
{
question: "A developer reviews the interview transcript and notices Claude is asking variations of already-answered questions and flagging minor formatting preferences. What does this signal?",
options: [
"All five ambiguity categories have been fully addressed now",
"Questions are becoming repetitive—the interview phase should end",
"Exactly ten questions have been asked and the limit is reached",
"The specification has reached an adequate word count threshold"
],
correctOption: 1,
explanation: "Interview ends when questions become repetitive (variations of answered questions), questions are trivial (implementation details not design decisions), or the specification feels complete (you can imagine implementation without guessing). It's not about category coverage or question count. Repetition and triviality are the signals that the spec is ready.",
source: "Lesson 6: Phase 3 - Refinement via Interview"
},
{
question: "What is the core prompt pattern for task-based implementation?",
options: [
"Use the task tool, each task by subagent, commit after each",
"Break this spec into tasks and implement each one sequentially",
"Implement this entire spec using available parallel processing threads",
"Create then execute all implementation tasks directly from specification"
],
correctOption: 0,
explanation: "The canonical prompt is: 'Use the task tool and each task should only be done by a subagent so that context is clear. After each task do a commit before you continue. You are the main agent and your subagents are your devs.' This triggers task extraction, delegation, isolation, and atomic commits.",
source: "Lesson 7: Phase 4 - Task-Based Implementation"
},
{
question: "Why does each implementation subagent start with fresh context rather than inheriting the main agent's context?",
options: [
"To reduce memory usage during implementation",
"To enable faster parallel processing",
"To simplify the task management system",
"To prevent error propagation across tasks"
],
correctOption: 3,
explanation: "Fresh context prevents error propagation. If a subagent makes a wrong assumption, that assumption dies with the subagent—it doesn't contaminate other tasks. In accumulated context, a wrong assumption in minute 5 affects code in minute 45. Context isolation contains failures.",
source: "Lesson 7: Phase 4 - Task-Based Implementation"
},
{
question: "The alexop.dev implementation completed 14 tasks in 45 minutes with 71% context usage. What does 71% context usage indicate?",
options: [
"Most of the implementation failed validation",
"The orchestrator stayed efficient despite many delegations",
"Only 71% of tasks were completed successfully",
"The specification covered 71% of requirements"
],
correctOption: 1,
explanation: "71% context usage after 14 task delegations shows the main orchestrator stayed efficient. Despite spawning 14 subagents, the main agent had 29% remaining for follow-up work. This demonstrates that task delegation preserves main context because subagents handle the heavy implementation.",
source: "Lesson 7: Phase 4 - Task-Based Implementation"
},
{
question: "What is the purpose of pre-commit hooks in task-based implementation?",
options: [
"To automatically format commit messages before saving",
"To track and record which tasks have been completed",
"To synchronize and coordinate parallel task execution",
"To provide backpressure that catches errors at the source"
],
correctOption: 3,
explanation: "Pre-commit hooks provide backpressure—quality gates that slow implementation when quality drops. If typecheck fails, the commit is rejected. If tests fail, the subagent must fix issues before proceeding. This prevents broken code from entering the repository even when AI writes it.",
source: "Lesson 7: Phase 4 - Task-Based Implementation"
},
{
question: "Which Claude Code tool is used to define a new task with its description and dependencies?",
options: [
"TaskCreate for new tasks with dependencies",
"TaskGet for task definition",
"TaskUpdate for task creation",
"TaskList for defining tasks"
],
correctOption: 0,
explanation: "TaskCreate defines new tasks with description and dependencies. TaskGet retrieves details of existing tasks. TaskUpdate changes status. TaskList shows all tasks with current status. The main agent uses TaskCreate when extracting tasks from the specification.",
source: "Lesson 7: Phase 4 - Task-Based Implementation"
},
{
question: "Task 2 needs output from Task 1, and Task 3 needs output from Task 2. What execution pattern is required?",
options: [
"All three tasks run simultaneously in parallel mode",
"Tasks 1, 2, 3 run sequentially with dependencies",
"Task 1 runs first, then tasks 2 and 3 in parallel",
"Tasks run in random order with automatic dependency resolution"
],
correctOption: 1,
explanation: "When tasks have linear dependencies (2 needs 1's output, 3 needs 2's output), they must run sequentially. You cannot start Task 2 until Task 1 completes. This is why dependency analysis matters—it determines parallel versus sequential execution.",
source: "Lesson 7: Phase 4 - Task-Based Implementation"
},
{
question: "A developer evaluates a task: 'Fix the null pointer exception on line 47 of auth.ts.' Should they use SDD for this task?",
options: [
"Yes—files affected exceeds five so SDD is required here",
"No—this task is a single-file bug fix and skips SDD",
"Only for production-critical systems regardless of scope",
"Yes, when the team has more than five active members"
],
correctOption: 0,
explanation: "The heuristic states: 'IF files_affected > 5 OR requirements_unclear OR learning_new_tech: Use SDD.' This task is a single-file bug fix with a clear problem—SDD overhead (research, spec, interview, tasks) would take longer than the fix itself. The correct answer maps to the 'ELSE IF single_file AND bug_fix: Skip SDD' branch of the heuristic.",
source: "Lesson 8: The Decision Framework"
},
{
question: "According to the decision heuristic, when should you skip SDD entirely?",
options: [
"For any bug fix regardless of scope",
"When working on existing features",
"When the timeline is less than one week",
"When single_file AND bug_fix conditions are true"
],
correctOption: 3,
explanation: "The heuristic states: 'ELSE IF single_file AND bug_fix: Skip SDD.' A null pointer exception in line 47 doesn't need four phases. You know the problem, you know the fix. The overhead of research, spec, interview, and tasks would take longer than fixing directly.",
source: "Lesson 8: The Decision Framework"
},
{
question: "What should you do when a task falls into the 'judgment call' category of the decision heuristic?",
options: [
"Always default to the full SDD workflow regardless",
"Always skip SDD entirely and just implement it directly",
"Start with a lightweight spec and expand if complexity reveals itself",
"Consult with your team members before deciding anything"
],
correctOption: 2,
explanation: "For judgment calls, start with a lightweight spec (just constraints and success criteria). If writing it reveals complexity—'Wait, how DO we handle existing data?'—expand to full specification. If it feels sufficient, proceed directly. This 80/20 approach balances effort and value.",
source: "Lesson 8: The Decision Framework"
},
{
question: "What does a lightweight spec contain?",
options: [
"Only constraints and success criteria sections",
"Full four-part template with abbreviated content",
"Reference architecture and implementation plan",
"Just the implementation checklist"
],
correctOption: 0,
explanation: "A lightweight spec contains only Constraints (what NOT to do, boundaries) and Success Criteria (measurable outcomes). No reference architecture analysis, no multi-phase implementation plan. These two elements provide 80% of specification value with 20% of the overhead.",
source: "Lesson 8: The Decision Framework"
},
{
question: "The critique 'SDD is just waterfall' compares spec phases to waterfall methodology. What's the key difference that counters this critique?",
options: [
"SDD phases are much shorter than waterfall phases",
"SDD uses AI assistance while waterfall relied on humans",
"SDD tasks are atomic and reversible via git revert",
"SDD does not require any written documentation"
],
correctOption: 2,
explanation: "SDD differs from waterfall because tasks are atomic and reversible (git revert), not months-long commitments without feedback. The spec also updates during implementation when reality diverges. Waterfall phases were isolated handoffs; SDD phases have tight feedback loops.",
source: "Lesson 8: The Decision Framework"
},
{
question: "When does exploratory prototyping benefit from vibe coding over SDD?",
options: [
"When the prototype will become production code",
"When you're discovering what's possible through rapid iteration",
"When multiple developers need to collaborate",
"When the technology stack is unfamiliar"
],
correctOption: 1,
explanation: "Exploratory prototyping—'What if we visualized this differently?'—benefits from rapid iteration. You're discovering the problem, not implementing a solution. Vibe coding serves exploration. Once you discover what works, THEN write a specification for production implementation.",
source: "Lesson 8: The Decision Framework"
},
{
question: "A production incident takes down the system. Which approach should you use?",
options: [
"Full SDD with research phase",
"Lightweight spec before any changes",
"Direct fix first, SDD for follow-up prevention",
"Skip fixing and focus on documentation"
],
correctOption: 2,
explanation: "Production incidents require immediate action, not spec documents. Fix it first, document later. However, the follow-up—'Prevent this class of failure'—is exactly the unclear-requirement task where SDD excels. Incident response is direct; long-term fix benefits from specification.",
source: "Lesson 8: The Decision Framework"
},
{
question: "Why does large refactor work (15+ files) benefit particularly well from SDD?",
options: [
"Specification prevents mid-refactor pivots and scope drift",
"More files means more opportunities for parallel research",
"Large refactors are required to use formal processes",
"Version control works better with specifications"
],
correctOption: 0,
explanation: "Large refactors benefit from specifications as anchors that prevent drift. Without a spec, you might chase side effects four directories deep with no clear picture of changes. The spec defines the end state upfront—each task references it, preventing well-intentioned tangents.",
source: "Lesson 8: The Decision Framework"
},
{
question: "What characteristic do tasks that warrant SDD share?",
options: [
"They require more than one developer",
"They have regulatory compliance requirements",
"Complexity exceeds working memory capacity",
"They involve external API integrations"
],
correctOption: 2,
explanation: "Tasks warranting SDD share a characteristic: complexity exceeds working memory. You can't hold a 15-file refactor in your head. You can't remember all assumptions while exploring unfamiliar libraries. The specification becomes external memory preserving decisions across sessions and collaborators.",
source: "Lesson 8: The Decision Framework"
},
{
question: "What characteristic do tasks where SDD is overkill share?",
options: [
"The solution is either obvious or unknowable",
"They involve frontend or UI work",
"They are assigned to junior developers",
"They have tight deadlines"
],
correctOption: 0,
explanation: "Tasks where SDD is overkill share a characteristic: the solution is either obvious or unknowable. When you know exactly what to change, specifying first adds no information. When exploring to discover possibilities, specifying upfront constrains discovery.",
source: "Lesson 8: The Decision Framework"
},
{
question: "A developer is at Turn 14 in a vibe coding session and notices that Claude's latest output is formatted as a blog post instead of the research report with citations they need. Which vibe coding failure is this?",
options: [
"Context loss where previous format decisions faded from attention",
"Assumption drift where Claude filled gaps with reasonable defaults",
"Pattern violations where code ignores existing project architecture",
"Specification gap where missing constraints led to wrong output"
],
correctOption: 1,
explanation: "By Turn 14, the developer discovers Claude wrote blog-style content when they needed a research report with citations. This is assumption drift—Claude filled the gap in 'report format' with a reasonable but wrong default. Early turns seemed like progress but accumulated wrong assumptions about audience and structure. Without explicit format constraints, Claude defaulted to what 'report' typically means.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "How does context loss differ from assumption drift as a failure mode?",
options: [
"Context loss is recoverable while assumption drift is not",
"Context loss loses past decisions, assumption drift makes wrong new ones",
"Context loss affects code quality, assumption drift affects performance",
"Context loss is faster while assumption drift is slower"
],
correctOption: 1,
explanation: "Context loss means previous decisions fade from attention—features that worked stop working after unrelated changes. Assumption drift means Claude fills gaps with reasonable but wrong defaults—generated code works but doesn't match your actual needs. Both compound but in different ways.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "The compounding problem table shows context loss becomes 'Critical' at which turn range?",
options: [
"Turns 1-5",
"Turns 6-10",
"Turns 11-15",
"Turns 16+"
],
correctOption: 3,
explanation: "By Turn 16+, context loss becomes Critical, assumption drift becomes Architectural, and pattern violations Require Rewrite. The three failure modes amplify each other—by this point, you're not iterating toward your goal but managing an increasingly divergent codebase.",
source: "Lesson 1: Why Specs Beat Vibe Coding"
},
{
question: "Model-Driven Development (MDD) failed to achieve mainstream adoption for similar reasons as Spec-as-Source struggles today. What shared challenge affects both?",
options: [
"Both require expensive tooling licenses",
"Both need specialized programming languages",
"Both face abstraction leakage requiring understanding both layers",
"Both are only suitable for small projects"
],
correctOption: 2,
explanation: "Both MDD and Spec-as-Source face the same fundamental challenge: generated code needs manual patches for edge cases, models/specs can't express all implementation concerns, and the abstraction leaks—requiring developers to understand both the specification layer AND the generated code layer.",
source: "Lesson 2: The Three Levels of SDD"
},
{
question: "Traditional AI coding interleaves planning and execution in one conversation. How does SDD fundamentally change this?",
options: [
"SDD eliminates all human involvement in planning",
"SDD completes all planning phases before any code generation begins",
"SDD generates code first then documents it afterward",
"SDD runs planning and execution in parallel threads"
],
correctOption: 1,
explanation: "SDD separates planning from execution completely. All four phases (Research, Specification, Refinement) finish before Implementation begins. This front-loads decisions so implementation becomes execution of a well-understood plan, not constant course-correction during coding. Traditional vibe coding blurs these into one interleaved conversation.",
source: "Lesson 3: The Four-Phase Workflow"
}
]}
questionsPerBatch={18}
/>
