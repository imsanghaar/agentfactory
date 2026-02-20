---
sidebar_position: 11
title: "Chapter 6: The Seven Principles Quiz"
proficiency_level: B1
layer: 1
estimated_time: "25 mins"
chapter_type: Concept
running_example_id: seven-principles-quiz
---

# Chapter 6: The Seven Principles of General Agent Problem Solving Quiz

Test your understanding of the seven principles that make agentic AI workflows effective: bash as universal interface, code as universal interface, verification as core step, small reversible decomposition, persisting state in files, constraints and safety, and observability.

<Quiz
title="Chapter 6: The Seven Principles Assessment"
questionsPerBatch={30}
questions={[
{
question: "A developer is choosing between ChatGPT (web interface, no terminal access) and Claude Code (terminal-based, file access). They need to debug a failing test. Why is terminal access the deciding factor for this task?",
options: [
"Terminal access allows the AI to read test files, run tests, and observe actual output",
"Terminal access provides faster response times compared to web interfaces",
"Terminal access enables access to more powerful language models than web interfaces",
"Terminal access provides code suggestions that web interfaces cannot generate"
],
correctOption: 0,
explanation: "Terminal access is the key differentiator because it enables agentic capability—the ability to observe, orient, decide, and act in a loop. For debugging a failing test, the AI needs to read the actual test file, execute the test command, observe the real error output, analyze the results, and propose fixes. ChatGPT can only suggest based on what you paste—it cannot run the test itself or see the actual error. Claude Code can execute `npm test`, read the output, identify the root cause, and iterate. Options B, C, and D describe characteristics that don't distinguish the tools or are incorrect (model access is similar, response speed isn't the primary advantage). The real difference is agency: the ability to act in your environment rather than just generate text.",
source: "Lesson 01: Bash is the Key"
},
{
question: "You're explaining to a colleague why terminal access matters for AI. They say: 'I can just copy-paste commands and output to ChatGPT.' What limitation of the copy-paste workflow does your colleague miss?",
options: [
"Copy-paste is slower than terminal-based AI for all tasks",
"Copy-paste doesn't work with complex multi-file projects",
"Copy-paste requires paid subscriptions while terminal access is free",
"Copy-paste breaks the OODA loop that enables autonomous iteration"
],
correctOption: 3,
explanation: "The copy-paste workflow fundamentally breaks the OODA loop (Observe-Orient-Decide-Act) that makes agentic AI powerful. With copy-paste, YOU become the bridge between AI and your system—you observe the error, paste it to AI, get a suggestion, paste it back, observe if it works, and repeat. This manual loop is slow and error-prone. With terminal access, the AI closes its own OODA loop: it observes by running commands, orients by analyzing output, decides on next steps, and acts by executing commands—iterating autonomously until the problem is solved. Option A is an overgeneralization—some simple tasks are similar speed. Option B is incorrect because copy-paste can work with multi-file projects, just poorly. Option C is incorrect—pricing varies by tool. The real issue is the broken feedback loop.",
source: "Lesson 01: Bash is the Key"
},
{
question: "Which command category would you always want to require human approval before allowing an AI to execute?",
options: [
"Read operations like cat, grep, find",
"Build commands like npm run build, make",
"Destructive operations like rm -rf, git reset --hard",
"Test commands like npm test, pytest"
],
correctOption: 2,
explanation: "Destructive operations (Option C) should always require human approval because they can cause irreversible damage—deleting files, discarding work, breaking systems. Read operations (cat, grep) are inherently safe—they only gather information. Build and test commands are generally low-risk and should be auto-approved for efficiency; they're verification steps that catch problems. The permission model should scale with risk: read operations are automatic, writes require review, destructive operations need explicit approval. This layered approach balances safety with autonomy—you don't want to approve every `cat` command, but you absolutely want to review `rm -rf` commands before execution.",
source: "Lesson 01: Bash is the Key"
},
{
question: "You ask an AI: 'Add input validation.' It generates basic length checks, but you wanted business rule validation (email domain must match company). What communication breakdown occurred?",
options: [
"The AI model wasn't large enough to understand complex requirements",
"Natural language ambiguity prevented precise intent transmission",
"Input validation is too complex for AI systems to handle correctly",
"The AI ignored your request intentionally to save time"
],
correctOption: 1,
explanation: "This scenario illustrates natural language ambiguity—'input validation' means different things in different contexts. The AI reasonably guessed at validation type (length, format) but couldn't know your specific business requirement (company email domain) without more context. Code resolves this ambiguity: showing an example of what you want is more precise than describing it in words. Option A is incorrect—model size isn't the issue; all models struggle with unstated requirements. Option C is wrong—AI can handle any validation type if specified clearly. Option D mischaracterizes AI behavior as intentional. The real lesson: natural language is inherently ambiguous, and code/examples serve as the precise interface that bridges the intent-implementation gap.",
source: "Lesson 02: Code as Universal Interface"
},
{
question: "A team uses a specification document written in prose to describe features. AI implementations based on this document consistently miss edge cases. What would most improve alignment between specifications and implementations?",
options: [
"Include executable test cases as part of the specification",
"Use a larger AI model with better reasoning capabilities",
"Hold meetings to verbally explain edge cases to the team",
"Rewrite the specification using more precise language"
],
correctOption: 0,
explanation: "Executable test cases provide unambiguous specifications because they define expected behavior precisely—input X should produce output Y. Unlike prose descriptions, which are open to interpretation, tests are machine-verifiable and leave no room for ambiguity about what 'correct' means. When AI implements against tests, it can verify its own work and catch edge cases before you review. Option B (larger model) doesn't solve the fundamental ambiguity problem. Option C (meetings) doesn't help AI systems, which only see the written specification. Option D (precise language) still suffers from natural language ambiguity—prose can never be as precise as executable code. The principle here is: code is the most precise specification language we have.",
source: "Lesson 02: Code as Universal Interface"
},
{
question: "You're reviewing AI-generated code and notice it doesn't match your intent. What's the most effective feedback approach?",
options: [
"Explain in natural language what's wrong and what should change",
"Paste the problematic code into ChatGPT for alternative implementation",
"Ask the AI to rewrite the entire feature from scratch",
"Provide specific code examples showing desired behavior"
],
correctOption: 3,
explanation: "Specific code examples bridge the intent-implementation gap more effectively than natural language descriptions. Instead of saying 'handle edge cases better' (vague), show `if (user === null) return error` (precise). Code examples are unambiguous—they demonstrate exactly what you want, leaving no room for interpretation. Option A (natural language) repeats the ambiguity problem that caused the initial mismatch. Option B starts over with a tool that lacks your project context. Option C is wasteful—rewriting everything when you could provide targeted correction. The most effective feedback anchors discussion in code: 'Here's what I want' (example) is clearer than 'Change X to be more Y' (description).",
source: "Lesson 02: Code as Universal Interface"
},
{
question: "An AI generates a function that looks correct but has a race condition: it checks a value, then acts on it, but the value might change between check and act. Why didn't verification catch this?",
options: [
"Verification is unnecessary for simple functions with clear logic",
"Verification only catches syntax errors and not logical errors",
"The race condition only occurs under concurrent load not captured by basic tests",
"AI systems cannot generate code that handles concurrency correctly"
],
correctOption: 2,
explanation: "This scenario illustrates that verification depth must match risk level. Basic verification (syntax check, unit tests) passes because the race condition only manifests under concurrent load—multiple operations accessing shared state simultaneously. The function works correctly in single-threaded tests but fails in production with concurrent users. This doesn't mean verification is useless (Option A)—it means you need appropriate verification for the risk level. High-risk code (concurrency, security, payments) requires deeper verification: load testing, concurrent test execution, security review. Option D is incorrect—AI can write correct concurrent code when explicitly asked. Option B is wrong—verification does catch logic errors, but only if tests cover the actual failure mode. The lesson: match verification depth to consequence of failure.",
source: "Lesson 03: Verification as Core Step"
},
{
question: "You're implementing a feature and the AI suggests a large change touching 50 files across multiple domains. What verification strategy is most appropriate?",
options: [
"Break the change into smaller pieces and verify each independently",
"Accept the change and monitor for bugs in production",
"Run the full test suite and if it passes, approve the change",
"Ask the AI to review its own changes for potential issues"
],
correctOption: 0,
explanation: "Breaking large changes into smaller, independently verifiable pieces (Principle 4: Decomposition) makes verification manageable. When you verify 50 files at once, you can't effectively review the diff, understand the changes, or identify problems. When you verify 5 files at a time across 10 iterations, each review is thorough and problems are caught early. Option B is irresponsible—production is not a testing environment. Option C is insufficient because tests pass doesn't mean changes are correct (tests might not cover new behavior, or changes might introduce subtle bugs). Option D is useful but doesn't replace human review—AI can miss context and consequences that you would catch. The principle: verify at granularity you can actually understand and review.",
source: "Lesson 03: Verification as Core Step"
},
{
question: "A team accepts AI-generated code without review because 'the tests pass.' After deployment, they discover the code has a security vulnerability. What verification principle did they violate?",
options: [
"They didn't run the tests enough times to be confident",
"They skipped manual review which catches issues tests may miss",
"They used the wrong AI model for security-sensitive code",
"They didn't document the code properly for maintainability"
],
correctOption: 1,
explanation: "Tests verify expected behavior but don't guarantee absence of issues like security vulnerabilities, performance problems, or architectural mismatches. Manual review remains essential because humans can identify concerns that tests don't capture: 'This input isn't validated' (security), 'This query will be slow at scale' (performance), 'This doesn't match our patterns' (architecture). Option A suggests running tests more, but the same tests would pass regardless—they don't test for security. Option C is incorrect—model choice doesn't change the need for review. Option D is important but separate from the immediate issue. The principle: tests are necessary but not sufficient—verification includes code review, security analysis, and architectural validation.",
source: "Lesson 03: Verification as Core Step"
},
{
question: "A developer makes one large commit with a complete feature implementation. Later, they discover a bug but can't identify which change caused it because the commit touches 20 files. What principle would have prevented this problem?",
options: [
"Persisting state in files for better context",
"Constraints and safety to prevent bugs early",
"Observability to trace the issue across files",
"Small, reversible decomposition with atomic commits"
],
correctOption: 3,
explanation: "Small, reversible decomposition (Principle 4) means breaking work into atomic commits where each commit can be independently understood, tested, and reverted. If the developer had made 20 small commits (one per logical change) instead of one large commit, they could use binary search on commit history (`git bisect`) to quickly identify which commit introduced the bug. With one monolithic commit, they can't isolate the problematic change. Options A, B, and C are valuable principles but don't directly address this isolation problem. State persistence (A) helps with context but not bug isolation. Safety constraints (B) prevent some bugs but not all. Observability (C) helps trace execution but not commit history. The specific issue here is commit granularity—atomic commits enable precise rollback and debugging.",
source: "Lesson 04: Small, Reversible Decomposition"
},
{
question: "Why is it recommended to create a feature branch for AI-assisted work rather than working directly on main?",
options: [
"Feature branches prevent AI from accessing production code",
"Feature branches are required by git for all development work",
"Feature branches enable easy rollback if AI makes mistakes",
"Feature branches make it harder for AI to read sensitive files"
],
correctOption: 2,
explanation: "Feature branches create a sandbox where AI can work without affecting the main branch. If the AI makes mistakes or you're unsatisfied with the changes, you can simply abandon the branch—main remains untouched. This is reversibility in action: branches are cheap to create and delete, making them ideal for experimentation. Option A is incorrect—AI can read any branch, including main. Option B is incorrect—direct main commits are allowed, just inadvisable. Option D is wrong—branch access doesn't affect file reading permissions. The principle: use branching to create reversible work streams where mistakes are easily discarded.",
source: "Lesson 04: Small, Reversible Decomposition"
},
{
question: "You ask AI to 'refactor the auth system' and it immediately starts making changes. What's missing from this workflow?",
options: [
"The workflow lacks decomposition into small, verifiable steps",
"The AI needs a better model to understand refactoring",
"The auth system is too complex for AI to refactor",
"The workflow needs more safety constraints enabled"
],
correctOption: 0,
explanation: "Refactoring an entire auth system is a large, complex task that should be decomposed into small steps: extract validation logic, extract token handling, update tests, etc. Without decomposition, the AI makes all changes before you see any—making review impossible and rollback difficult. A better approach: 'Plan the refactoring. Show me the steps. Execute one step at a time, waiting for my approval before continuing.' This makes each change reviewable and reversible. Option B is incorrect—model size isn't the issue. Option C is defeatist—auth systems can be refactored, just not as one monolithic change. Option D helps but doesn't solve the core problem. The principle: large tasks must be broken down for effective human-AI collaboration.",
source: "Lesson 04: Small, Reversible Decomposition"
},
{
question: "A developer starts a new AI session and has to re-explain project conventions that they explained in previous sessions. What would solve this repetition?",
options: [
"Use a different AI model with better memory of past conversations",
"Persist project context in CLAUDE.md that AI reads automatically",
"Type faster to reduce the time spent on explanations",
"Share conversation history manually with each new session"
],
correctOption: 1,
explanation: "AI systems are stateless—each session starts fresh. CLAUDE.md files persist project context (conventions, patterns, decisions) that AI reads automatically, eliminating repetitive explanations. Instead of saying 'we use TypeScript strict mode and prefix interfaces with I' in every session, you document this once in CLAUDE.md and all future sessions include this context automatically. Option A is incorrect—AI models don't maintain session memory across conversations. Option C doesn't solve the problem, just makes it less annoying. Option D is impractical and error-prone. The solution is persistent context files that serve as shared memory between you, the AI, and future collaborators.",
source: "Lesson 05: Persisting State in Files"
},
{
question: "Six months after choosing PostgreSQL over MongoDB, the team forgets why they made that decision. What document would have prevented this memory loss?",
options: [
"README.md with project overview and setup instructions",
"CLAUDE.md with coding conventions and style guides",
"Package.json with database dependencies and versions",
"Architecture Decision Record (ADR) explaining the choice"
],
correctOption: 3,
explanation: "Architecture Decision Records (ADRs) exist to capture the 'why' behind technical choices: what problem you faced, what options you considered, what you chose, and the consequences. Unlike README.md (what the project does) or CLAUDE.md (how to work on it), ADRs document the reasoning that future you (or new team members) can reference when questions resurface. Option C shows what you chose but not why. Six months later, when someone asks 'why not MongoDB?', the ADR provides the answer without requiring original decision-makers to remember. The principle: decisions have consequences, and those consequences should be documented.",
source: "Lesson 05: Persisting State in Files"
},
{
question: "A team's CLAUDE.md file says 'Use functional components' but the codebase has mostly class components. What does this mismatch indicate?",
options: [
"CLAUDE.md should document actual patterns, not aspirational ones",
"The AI is ignoring CLAUDE.md instructions intentionally",
"Class components should be immediately converted to functional",
"CLAUDE.md files don't work for React projects"
],
correctOption: 0,
explanation: "CLAUDE.md should document reality, not aspirations. If it says 'use functional components' but the codebase uses class components, AI faces conflicting signals—should it follow documented rules or existing patterns? This confusion leads to inconsistent code. Either update CLAUDE.md to match reality ('we use class components, migrating to functional over time') or update the codebase to match documentation. Option B mischaracterizes AI behavior—AI doesn't 'ignore' instructions, it reconciles conflicts imperfectly. Option C is premature—migrate first, then update documentation. Option D is incorrect—CLAUDE.md works for any project. The principle: context files should reflect actual project state, not desired state, to avoid confusion.",
source: "Lesson 05: Persisting State in Files"
},
{
question: "You grant AI terminal access on a production server. It accidentally runs `rm -rf /app/data` while trying to clean up temporary files. What safety principle was violated?",
options: [
"Observability—you didn't see the command before it executed",
"Decomposition—the operation was too large to execute safely",
"Constraints and safety—AI shouldn't have production access",
"Verification—you didn't test the command beforehand"
],
correctOption: 2,
explanation: "Granting AI direct production access violates the safety principle of environment isolation. AI should work in sandbox/staging environments, with human-controlled deployment to production. This containment limits the blast radius of mistakes—destructive commands in staging are annoying; in production, they're catastrophic. Options A, B, and D are valuable principles but the root issue here is inappropriate access. Observability (A) helps diagnose problems after they occur but doesn't prevent them. Decomposition (B) is irrelevant to this specific failure. Verification (D) might catch the issue if you reviewed the command, but the real problem is AI executing destructive commands in production at all. The principle: isolate AI work from production systems.",
source: "Lesson 06: Constraints and Safety"
},
{
question: "You're working on a critical system (payment processing). Should you use permissive, confirming, or restricted permission mode?",
options: [
"Permissive mode—efficiency is critical for payment systems",
"Confirming mode—approve all writes to maintain oversight",
"Restricted mode—AI should only read, never modify payment code",
"Any mode—AI is safe enough for payment processing"
],
correctOption: 1,
explanation: "Critical systems like payment processing warrant confirming mode (approve all writes) because the consequence of failure is high (financial loss, regulatory issues, reputation damage). You want AI assistance but need human oversight for any modifications. Permissive mode (auto-approve safe operations) might be acceptable for trusted routine work, but not for critical systems. Restricted mode (read-only) limits usefulness too much—you do want AI help, just with review. Option D is dangerous—no system is 'safe enough' to skip oversight when consequences are severe. The principle: permission mode should scale with risk—higher consequence requires more human oversight.",
source: "Lesson 06: Constraints and Safety"
},
{
question: "An AI tool offers to 'auto-approve all commands' for faster workflow. When is this appropriate?",
options: [
"Always—speed is more important than caution",
"Never—you should always review every command",
"Only when using the most expensive AI model tier",
"When working in sandbox environment on trusted codebase"
],
correctOption: 3,
explanation: "Auto-approve (permissive mode) is appropriate when the consequence of mistakes is low—sandbox environments where you can easily reset, familiar codebases where you understand patterns, routine operations where risks are known. In these cases, the efficiency benefit outweighs the small risk. It's inappropriate for production systems (consequence high), unfamiliar code (risk unknown), or destructive operations (irreversible). Options A and B are absolute rules that don't match the nuanced reality of risk-based decision making. Option C is unrelated to safety. The principle: calibrate permissions to context—more permissive when risks are low and contained, more cautious when consequences are severe.",
source: "Lesson 06: Constraints and Safety"
},
{
question: "You ask AI to fix a bug and it reports 'Done!' but doesn't show what it changed. You later discover it modified files you didn't want touched. What principle would have prevented this?",
options: [
"Observability—AI should show what it's doing as it works",
"Bash is the key—AI should use terminal more carefully",
"Code as universal interface—you should have specified changes as code",
"Decomposition—you should have broken the task into smaller steps"
],
correctOption: 0,
explanation: "Observability (Principle 7) means seeing what the AI is doing—what files it reads, what changes it makes, what commands it executes. Without visibility, you can't verify the AI is doing only what you asked. A good AI workflow shows progress: 'Reading auth.js... Found bug... Modifying auth.js (+3 lines)... Tests pass.' This transparency lets you redirect if the AI goes off-track. Options B and C are valuable but don't directly address this visibility problem. Option D helps but doesn't prevent unintended modifications if you can't see what's changing. The principle: you can't trust (or effectively direct) what you can't see.",
source: "Lesson 07: Observability"
},
{
question: "When debugging an AI session, what information is most valuable for understanding what went wrong?",
options: [
"The AI model version used during the session",
"The time of day when the session occurred",
"The activity log showing the sequence of actions taken",
"The length of the conversation in tokens"
],
correctOption: 2,
explanation: "Activity logs showing the sequence of actions (read file X, modify file Y, run command Z, observed result W) let you reconstruct what happened and identify where things went wrong. Unlike the other options (model version, time, token count), the action sequence is diagnostic—you can see 'AI read the wrong config file' or 'AI ran tests before implementing the fix.' This observability enables debugging: you can trace the failure to a specific decision point. Option A might be relevant for some issues but most problems are workflow-related, not model-specific. Options B and D are rarely relevant to understanding failures. The principle: logs are your post-mortem tool—what the AI did, in order, is the most valuable diagnostic information.",
source: "Lesson 07: Observability"
},
{
question: "You're implementing a new feature. Which principles are MOST critical for this task type?",
options: [
"Only bash access is needed since features require code execution",
"All principles are relevant for feature implementation work",
"Only verification is needed since features must work correctly",
"Only observability is needed since you need to see progress"
],
correctOption: 1,
explanation: "Feature implementation involves all principles: bash access to execute commands, code as interface to specify behavior, verification to test correctness, decomposition to break into manageable steps, state persistence to maintain context, safety to prevent mistakes, and observability to see progress. While you might prioritize certain principles based on context (safety for production systems, observability for debugging), all seven are relevant for complete feature work. Options A, C, and D incorrectly suggest single principles are sufficient—no single principle covers all aspects of feature development. The principle: real workflows integrate multiple principles, with emphasis shifting based on task context.",
source: "Lesson 09: Putting It All Together"
},
{
question: "You're debugging a production issue. Which THREE principles are most critical?",
options: [
"Bash access, state persistence, and safety constraints",
"Code as interface, decomposition, and state persistence",
"Decomposition, safety, and observability",
"Bash access, verification, and observability"
],
correctOption: 3,
explanation: "Debugging production issues requires: bash access to investigate (read logs, run commands, check system state), verification to test fixes (ensure the fix actually resolves the issue), and observability to understand what happened (trace logs, see error sequence). While other principles are valuable, these three are essential for the debugging cycle. Option A includes state persistence (useful for context but not critical for acute debugging) and safety (important but secondary to fixing the active issue). Option B misses observability which is crucial for understanding the problem. Option C misses bash access which is required for investigation. The principle: prioritize principles based on task needs—debugging emphasizes investigation, verification, and visibility.",
source: "Lesson 09: Putting It All Together"
},
{
question: "A team wants to improve their AI workflow but doesn't know where to start. What's the first step?",
options: [
"Identify which principle would provide the most value for their specific pain points",
"Implement all seven principles simultaneously for maximum benefit",
"Purchase a more expensive AI tool with better built-in safety features",
"Hire an AI workflow consultant to design a comprehensive solution"
],
correctOption: 0,
explanation: "The most effective starting point is identifying your biggest pain point and applying the principle that addresses it. If you're constantly repeating context, start with CLAUDE.md (state persistence). If you're surprised by AI changes, improve observability. If you're debugging integration issues, focus on decomposition and verification. Option B (all principles at once) is overwhelming and wasteful—you'll implement features you don't need. Option C (expensive tool) throws money at process problems. Option D (consultant) might help eventually, but start with self-assessment. The principle: targeted improvement based on actual problems beats wholesale change.",
source: "Lesson 09: Putting It All Together"
},
{
question: "An AI agent successfully implements a feature in a development environment. When moved to staging, it fails because environment variables differ. The agent had no way to know about the staging configuration. Which principle combination would have caught this earlier?",
options: [
"Code as Interface + Decomposition: specify behavior precisely and break into steps",
"Safety + Observability: restrict access and monitor activity",
"Verification + Persisting State: test in multiple environments and document differences",
"Bash access + Observability: run commands and see results"
],
correctOption: 2,
explanation: "This is an environment parity problem. Verification (Principle 3) across environments would catch configuration mismatches before staging. Persisting State (Principle 5) would document environment-specific configurations in files the agent can read—'staging uses DATABASE_URL_STAGING, not DATABASE_URL.' Together, these principles ensure the agent knows about environmental differences and tests against them. Bash access alone doesn't help if you don't know what to test. Code precision doesn't address environment configuration. Safety constraints wouldn't prevent this class of error. The lesson: verification must span environments, and environmental differences must be documented.",
source: "Lesson 03: Verification as Core Step"
},
{
question: "A developer uses AI to refactor authentication. The AI makes changes across 12 files in one operation. Tests pass, but a week later, a subtle security flaw is discovered in the token validation logic. Git history shows one massive commit. What principle failure made this bug hard to isolate?",
options: [
"Observability failure: the developer couldn't see what changed",
"Decomposition failure: atomic commits would have isolated the token validation change",
"Verification failure: tests didn't cover the security scenario",
"State persistence failure: the refactoring plan wasn't documented"
],
correctOption: 1,
explanation: "While verification (C) also failed (tests missed the flaw), the question asks about isolation difficulty. Small, reversible decomposition (Principle 4) would have created atomic commits—one for 'extract token validation,' another for 'add expiration check,' etc. With atomic commits, git bisect could pinpoint exactly which commit introduced the flaw. With one massive commit, you can't isolate which of the 12 file changes caused the problem. Observability helps during the session but not for post-hoc debugging of committed code. The lesson: decomposition enables forensic debugging.",
source: "Lesson 04: Small, Reversible Decomposition"
},
{
question: "Two developers use AI on the same codebase. Developer A's AI follows team conventions perfectly. Developer B's AI constantly violates them, using different naming patterns and import styles. Both use identical AI tools and models. What's the most likely cause of the difference?",
options: [
"Developer A has a higher-tier AI subscription with better instruction following",
"Developer A reviews code carefully and rejects bad suggestions immediately",
"Developer B's AI has degraded context from too many prior sessions",
"Developer A has conventions documented in CLAUDE.md; Developer B relies on verbal explanations each session"
],
correctOption: 3,
explanation: "This illustrates Principle 5 (Persisting State in Files). Developer A encoded conventions in CLAUDE.md—the AI reads them automatically every session. Developer B re-explains conventions each time, introducing variance, forgetting details, or omitting context. The AI doesn't 'remember' previous sessions, so verbal explanations are lost. Same tool, same model, different results because of context persistence. Subscription tiers don't affect instruction following. Context doesn't degrade between sessions (each starts fresh). Code review catches issues but doesn't prevent them. The lesson: persistent context files eliminate session-to-session variance.",
source: "Lesson 05: Persisting State in Files"
},
{
question: "An AI agent is given broad file system access and told to 'clean up the project.' It deletes node_modules (correct), .git directory (catastrophic), and build artifacts (correct). The developer had no warning before the .git deletion. Which TWO principles failed?",
options: [
"Constraints/Safety and Observability",
"Bash access and Code as Interface",
"Verification and Decomposition",
"State Persistence and Verification"
],
correctOption: 0,
explanation: "Two principles failed catastrophically: Constraints/Safety (Principle 6) should have prevented AI from touching .git—it should be on an explicit deny list or require confirmation for any git-related operations. Observability (Principle 7) should have shown the developer what files would be deleted BEFORE deletion, allowing intervention. With proper safety constraints, .git would be protected. With proper observability, the developer would see 'About to delete: node_modules/, .git/, dist/' and could say 'Stop—not .git!' The lesson: destructive operations need both protection (constraints) and preview (observability).",
source: "Lesson 06: Constraints and Safety"
},
{
question: "You ask an AI to 'make the API faster.' It refactors database queries, adds caching, and changes the response format. Users report broken integrations because the response format changed. What specification approach would have prevented the breaking change?",
options: [
"Natural language: 'Make it faster but don't change the response structure'",
"Decomposition: Break 'make faster' into smaller optimization tasks",
"Code as Interface: Provide existing API contract tests that must continue passing",
"Observability: Watch the AI work in real-time and intervene if needed"
],
correctOption: 2,
explanation: "Code as Universal Interface (Principle 2) solves this precisely. 'Don't break anything' is vague—what counts as breaking? API contract tests are unambiguous: these requests must return these exact response shapes. The AI can optimize freely as long as tests pass. If it changes response format, tests fail, and the AI knows to revert. Natural language (A) is too vague. Decomposition (B) helps but doesn't define 'breaking.' Observability (D) might let you catch it but requires constant attention. The lesson: executable specifications (tests) define constraints more precisely than prose.",
source: "Lesson 02: Code as Universal Interface"
},
{
question: "A junior developer sets AI to 'permissive mode' (auto-approve all operations) to work faster. A senior developer insists on 'confirming mode' (approve writes). The junior argues: 'I can always git reset if something goes wrong.' What does the junior's argument miss?",
options: [
"Git reset is too slow to be practical for iterative development",
"Some destructive operations (secrets leaked, external API calls, database mutations) can't be reset with git",
"Confirming mode is faster because it prevents having to fix mistakes",
"Permissive mode doesn't actually work with modern AI tools"
],
correctOption: 1,
explanation: "The junior assumes all AI actions are reversible via git. But Principle 6 (Constraints and Safety) recognizes that some operations have consequences beyond the repository: leaked API keys can't be un-leaked, external API calls (sending emails, making payments) can't be un-sent, database changes may not be tracked in git. Git reset fixes file state but not external state. The junior's mental model works for pure code changes but fails for operations with real-world effects. The lesson: reversibility has limits—some operations require approval because their effects extend beyond what git controls.",
source: "Lesson 06: Constraints and Safety"
},
{
question: "A developer notices their AI sessions are inconsistent: sometimes the AI follows project patterns perfectly, other times it seems to forget them mid-session. Context utilization varies from 20% to 85% across tasks. What's the likely root cause?",
options: [
"The AI model has inconsistent capabilities across different session types",
"The developer is using different AI models in different sessions unknowingly",
"Network latency is causing instructions to be silently dropped",
"Project patterns aren't in CLAUDE.md Zone 1, so they lose attention as context fills"
],
correctOption: 3,
explanation: "This combines Principle 5 (State Persistence) with context engineering from Chapter 4. When patterns are in Zone 2 (middle) of CLAUDE.md, they receive ~30% less attention. At 20% context utilization, there's enough attention for everything. At 85%, attention is strained, and middle-positioned content gets deprioritized. The solution: move critical patterns to Zone 1 (beginning) where primacy ensures consistent attention regardless of utilization. The AI model doesn't vary (A), and dropped instructions (C) would cause different symptoms. The lesson: position affects reliability, especially under context pressure.",
source: "Lesson 05: Persisting State in Files"
},
{
question: "A developer starts Claude Code and immediately types: 'Add a payment system with Stripe integration.' Claude begins editing files right away. After 20 minutes, the developer realizes Claude chose the wrong architecture. What operational practice would have prevented this?",
options: [
"Using the four-phase workflow: Explore and Plan in Plan Mode before implementing",
"Using a larger context window to give Claude more room to work",
"Asking Claude to work faster so mistakes are caught sooner",
"Running all tests before letting Claude start any implementation"
],
correctOption: 0,
explanation: "The four-phase workflow (Explore → Plan → Implement → Commit) prevents this exact scenario. In Plan Mode (Shift+Tab), Claude reads and plans without modifying files. The developer would see the proposed architecture before any code is written—catching the wrong approach in minutes rather than discovering it after 20 minutes of wasted implementation. Option B doesn't help because more context doesn't prevent wrong architectural choices. Option C makes things worse—faster mistakes are still mistakes. Option D is premature—there's nothing to test yet. The key insight: course correction is cheap during planning, expensive during implementation.",
source: "Lesson 08: Operational Best Practices"
},
{
question: "A developer asks Claude to fix a bug. Claude's first attempt is wrong. The developer corrects it. Claude's second attempt is also wrong, in a different way. What should the developer do next?",
options: [
"Provide a third, more detailed correction and continue in the same session",
"Switch to a different AI model that may understand better",
"Apply the Rule of Two: /clear and start a fresh session with a better prompt",
"Continue correcting until Claude eventually converges on the right answer"
],
correctOption: 2,
explanation: "The Rule of Two says: if Claude misses the mark twice on the same fix, STOP. Don't try a third time. Each correction adds noise to the context—Claude is now juggling the original request plus two failed attempts plus your frustrations. The signal-to-noise ratio collapses. Instead, /clear and start fresh with a prompt that includes what you learned from the failures. The failed attempts taught you what Claude needed to know; a fresh prompt with that information upfront beats a third round of corrections every time. Option A continues the correction loop. Option B changes the tool but not the approach. Option D is the definition of the correction loop anti-pattern.",
source: "Lesson 08: Operational Best Practices"
},
{
question: "Before implementing a complex notification system, a developer uses the prompt: 'Don't code yet. Interview me until you have a 100% clear spec.' After the interview produces a detailed specification, what is the most effective next step?",
options: [
"Continue implementing in the same session since Claude already has context",
"Start a fresh session with only the specification (the Golden Reset)",
"Delete the specification and let Claude implement from memory",
"Share the specification with a different AI tool for implementation"
],
correctOption: 1,
explanation: "The Golden Reset—starting a fresh session with only the clean specification—often produces better results than continuing in the same session. The interview session contains exploratory noise: tangents, rejected ideas, back-and-forth clarification. A fresh context with just the signal-dense specification means Claude's full attention goes to implementation rather than filtering through conversation history. Option A works but carries the noise from exploration. Option C loses the specification's value. Option D fragments context across tools. The lesson: clean spec → clean session → clean code.",
source: "Lesson 08: Operational Best Practices"
}
]}
/>

## Answer Key

| Question | Correct Answer | Principle Tested                             |
| -------- | -------------- | -------------------------------------------- |
| 1        | A              | Principle 1: Bash is the Key                 |
| 2        | D              | Principle 1: Bash is the Key                 |
| 3        | C              | Principle 1: Bash is the Key                 |
| 4        | B              | Principle 2: Code as Universal Interface     |
| 5        | A              | Principle 2: Code as Universal Interface     |
| 6        | D              | Principle 2: Code as Universal Interface     |
| 7        | C              | Principle 3: Verification as Core Step       |
| 8        | A              | Principle 3: Verification as Core Step       |
| 9        | B              | Principle 3: Verification as Core Step       |
| 10       | D              | Principle 4: Small, Reversible Decomposition |
| 11       | C              | Principle 4: Small, Reversible Decomposition |
| 12       | A              | Principle 4: Small, Reversible Decomposition |
| 13       | B              | Principle 5: Persisting State in Files       |
| 14       | D              | Principle 5: Persisting State in Files       |
| 15       | A              | Principle 5: Persisting State in Files       |
| 16       | C              | Principle 6: Constraints and Safety          |
| 17       | B              | Principle 6: Constraints and Safety          |
| 18       | D              | Principle 6: Constraints and Safety          |
| 19       | A              | Principle 7: Observability                   |
| 20       | C              | Principle 7: Observability                   |
| 21       | B              | Principle 8: Putting It All Together         |
| 22       | D              | Principle 8: Putting It All Together         |
| 23       | A              | Principle 8: Putting It All Together         |
| 24       | C              | Lesson 03: Verification as Core Step         |
| 25       | B              | Lesson 04: Small, Reversible Decomposition   |
| 26       | D              | Lesson 05: Persisting State in Files         |
| 27       | A              | Lesson 06: Constraints and Safety            |
| 28       | C              | Lesson 02: Code as Universal Interface       |
| 29       | B              | Lesson 06: Constraints and Safety            |
| 30       | D              | Lesson 05: Persisting State in Files         |
| 31       | A              | Lesson 08: Operational Best Practices        |
| 32       | C              | Lesson 08: Operational Best Practices        |
| 33       | B              | Lesson 08: Operational Best Practices        |

## Scoring Guide

| Score | Proficiency Level | Interpretation                                                      |
| ----- | ----------------- | ------------------------------------------------------------------- |
| 30-33 | B2 (Advanced)     | Strong understanding of all seven principles and how they integrate |
| 24-29 | B1 (Intermediate) | Good understanding with some gaps in integration                    |
| 18-23 | A2 (Elementary)   | Basic understanding of principles but needs more practice           |
| 0-17  | A1 (Beginner)     | Review the lessons and try the "Try With AI" exercises              |

## Next Steps

Based on your performance, focus on:

- **Principles 1-3 (Foundation)**: If you missed questions 1-9, review the fundamental lessons on bash access, code as interface, and verification
- **Principles 4-5 (Workflow)**: If you missed questions 10-15 or 24-26, focus on decomposition and state persistence patterns
- **Principles 6-7 (Safety & Observability)**: If you missed questions 16-20, 27, or 29, study safety models and observability practices
- **Operational Practices**: If you missed questions 31-33, review Lesson 8 on the four-phase workflow, failure patterns, and the interview pattern
- **Integration & Tradeoffs**: If you missed questions 21-23 or 24-30, practice applying multiple principles together and reasoning about principle interactions

Remember: The principles are most powerful when applied together. The scenario-based questions (24-33) test your ability to diagnose which principles apply to real-world situations—this judgment is what separates practitioners from beginners.
