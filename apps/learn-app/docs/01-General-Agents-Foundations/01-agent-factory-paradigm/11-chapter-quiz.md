---
sidebar_position: 11
title: "Chapter 1: The AI Agent Factory Paradigm Quiz"
proficiency_level: A2
layer: 1
estimated_time: "50 mins"
chapter_type: Concept
running_example_id: agent-factory-paradigm-quiz
---

# Chapter 1: The AI Agent Factory Paradigm Quiz

Test your understanding of the foundational concepts that define AI-Driven Development and the Digital FTE vision. This assessment covers all 10 lessons in Chapter 1.

<Quiz
title="Chapter 1: The AI Agent Factory Paradigm Assessment"
questionsPerBatch={30}
questions={[
{
question: "Which of the following is concrete evidence that AI coding capability reached production quality in 2024-2025?",
options: ["OpenAI achieved a perfect score solving all 12 problems at the ICPC World Finals", "ChatGPT became more popular than other AI tools", "More blog posts were written about AI development", "AI companies received more venture capital funding"],
correctOption: 0,
explanation: "The ICPC World Finals breakthrough in 2025 demonstrated that AI can solve complex algorithmic problems at the highest competitive level—concrete evidence of production-quality capability, not just popularity or funding metrics.",
source: "Lesson 1: The 2025 Inflection Point"
},
{
question: "According to the 2025 Stack Overflow Developer Survey, what percentage of professional developers use or plan to use AI coding tools?",
options: ["51%", "84%", "66%", "95%"],
correctOption: 1,
explanation: "84% of developers are using or plan to use AI tools, with 51% using them daily. This mainstream adoption indicates AI tools have crossed from experimental to standard practice.",
source: "Lesson 1: The 2025 Inflection Point"
},
{
question: "A development team has vague requirements that keep changing. They're building something novel and aren't sure what the solution should look like. According to the Agent Maturity Model, which stage is most appropriate for this situation?",
options: ["Specialist stage — deploy Custom Agents for production reliability", "Production stage — enforce constraints for consistent behavior", "Incubator stage — use General Agents for exploration and prototyping", "Governance stage — enforce compliance requirements before proceeding"],
correctOption: 2,
explanation: "The Incubator stage uses General Agents like Claude Code for exploration, discovery, and prototyping. It's optimized for flexibility and reasoning, not production scale. Custom Agents (Specialist stage) handle production workloads once requirements stabilize.",
source: "Lesson 1: The 2025 Inflection Point"
},
{
question: "When should you use General Agents according to the Agent Factory paradigm?",
options: ["When you need consistent behavior across thousands of automated runs", "When cost and latency are the primary constraints to optimize", "When you need to enforce specific governance rules at scale", "When you're not sure what the solution should look like yet"],
correctOption: 3,
explanation: "General Agents are ideal when requirements are unclear, keep changing, or you're doing something novel. Custom Agents are for when you can precisely define behavior and need reliability at scale.",
source: "Lesson 1: The 2025 Inflection Point"
},
{
question: "What is 'Premature Specialization' in the Agent Factory paradigm?",
options: ["Building custom agents before requirements stabilize through exploration", "Using custom agents without building general agents first in sequence", "Training AI models too early in the product development lifecycle", "Deploying agents directly to production without adequate testing phases"],
correctOption: 0,
explanation: "Premature Specialization means trying to build custom agents before exploring the problem space with general agents. This leads to rigid solutions that don't match actual needs.",
source: "Lesson 1: The 2025 Inflection Point"
},
{
question: "What is the core reality behind the 'illusion of memory' in LLMs?",
options: ["LLMs have perfect recall but are designed to respond as if they forget", "Memory is stored in the model weights and persists permanently after training", "LLMs retain the last 10 conversations automatically in a rolling cache", "The application stores history and re-sends it; the model reads fresh each time then forgets"],
correctOption: 3,
explanation: "The application (not the model) stores conversation history. Every API call sends the entire history, which the model reads fresh—then immediately forgets. Session continuity is an application feature, not a model capability.",
source: "Lesson 2: Three Core LLM Constraints"
},
{
question: "When a developer says 'It remembers my coding style,' what's actually happening?",
options: ["The model learned their style from training data and applies it dynamically", "The model has no past-session memory; they should use style guides in AGENTS.md", "The model stores preferences in a personalized profile database", "The model's weights were updated incrementally with their preferences"],
correctOption: 1,
explanation: "LLMs have no memory between sessions. What appears as 'remembering' is actually the application re-injecting context. To preserve style preferences, encode them in persistent files like AGENTS.md.",
source: "Lesson 2: Three Core LLM Constraints"
},
{
question: "Why is LLM output probabilistic rather than deterministic?",
options: ["Servers introduce calibrated random noise to prevent identical responses being copied", "Models are engineered to be unpredictable as a core security design principle", "Models sample from probability distributions, producing different outputs from identical inputs", "Each API call routes to a different model version with slightly different weights"],
correctOption: 2,
explanation: "LLMs sample from probability distributions. Even with temperature=0, subtle variations can occur. This means you cannot expect identical code from identical prompts—validation becomes essential.",
source: "Lesson 2: Three Core LLM Constraints"
},
{
question: "What is the practical implication of probabilistic LLM outputs for software development?",
options: ["Only use temperature=0 to eliminate all variation from LLM responses", "Always use identical prompts to maximize consistency across API calls", "Avoid using LLMs for any code that is remotely critical to the system", "Validation and testing become essential since outputs vary between runs"],
correctOption: 3,
explanation: "Because outputs vary, validation becomes essential—not optional. Specifications constrain the valid output space, and Test-Driven Development verifies invariants regardless of implementation variation.",
source: "Lesson 2: Three Core LLM Constraints"
},
{
question: "What happens when an LLM's context window fills up during a long conversation?",
options: ["Early messages get truncated and information is permanently lost from context", "The model compresses old information automatically using internal summarization", "The model requests additional memory allocation from the server infrastructure", "Conversation quality improves because the model has richer data to process"],
correctOption: 0,
explanation: "When context fills up, early messages are truncated and information is lost. This is why context engineering is a core skill—you must strategically manage what goes into the context window.",
source: "Lesson 2: Three Core LLM Constraints"
},
{
question: "Which approach helps manage the 'context is limited' constraint in LLMs?",
options: ["Use the longest possible system prompts to establish comprehensive guidelines", "Include the complete conversation history to maintain full context continuity", "Reference file paths rather than paste entire file contents into prompts", "Paste entire codebases into every prompt for maximum model awareness"],
correctOption: 2,
explanation: "Context is zero-sum—every token for history is a token not available for code or response. Reference paths rather than pasting contents, maintain PROJECT_CONTEXT.md for state, and start fresh conversations for new topics.",
source: "Lesson 2: Three Core LLM Constraints"
},
{
question: "What is the most fundamental change in the developer role in the AI era?",
options: ["Learning additional frameworks, libraries, and programming languages continuously", "Shifting from implementation (typing code) to orchestration (directing AI systems)", "Mastering cloud computing, DevOps, and infrastructure as code thoroughly", "Understanding machine learning theory to evaluate model output quality"],
correctOption: 1,
explanation: "The core shift is from typist to orchestrator. Your value is no longer in how fast you can type, but in the quality of your ideas and directions. The 10% humans contribute—problem understanding, decisions, quality judgments—becomes infinitely more valuable.",
source: "Lesson 3: From Coder to Orchestrator"
},
{
question: "What is the OODA loop?",
options: ["A method for debugging code faster than traditional step-through approaches", "A programming design pattern optimized for asynchronous concurrent operations", "An acronym representing four popular programming languages in sequence", "A reasoning framework with Observe, Orient, Decide, Act—used by AI agents to process information and take action"],
correctOption: 3,
explanation: "OODA (Observe, Orient, Decide, Act) is a reasoning framework from military strategy that describes how AI agents process information and take action. Agentic AI cycles through OODA continuously until goals are achieved.",
source: "Lesson 3: From Coder to Orchestrator"
},
{
question: "What distinguishes Generation 4 AI tools from Generation 3?",
options: ["Gen 4 agents execute autonomously with multi-turn capability; Gen 3 required step-by-step approval", "Gen 4 uses substantially larger language models trained on more comprehensive data", "Gen 4 focuses on code completion only while Gen 3 handles full feature development", "Gen 4 is exclusively available to enterprise users with premium licensing agreements"],
correctOption: 0,
explanation: "Generation 4 (Claude Code, Gemini CLI) agents work autonomously—reading code, running tests, making commits—without requiring step-by-step human approval. The bottleneck shifts from typing speed to human review speed.",
source: "Lesson 3: From Coder to Orchestrator"
},
{
question: "Your team uses AI to generate 80% of routine code. A developer must now decide whether an AI-generated authentication module matches the spec and passes security review. According to the AI-transformed SDLC, what role is this developer playing?",
options: ["Traditional coder — manually rewriting all AI output before shipping", "Debug specialist — identifying bugs introduced by the AI generator", "Validator — verifying AI-generated code against specifications and security requirements", "Documentation writer — recording how the AI-generated code functions for the team"],
correctOption: 2,
explanation: "AI generates 80-90% of routine code. The developer's role shifts to validation: Does this match the spec? Are there security issues? Would an architect approve this approach?",
source: "Lesson 3: From Coder to Orchestrator"
},
{
question: "A product manager asks what the new developer role looks like in an AI-augmented team. Which answer best describes orchestrator responsibilities?",
options: ["Writing all boilerplate configuration files and database schema migrations manually", "Specification writing, requirement gathering, and validation of AI-generated work", "Implementing database queries and API endpoints without relying on AI assistance", "Memorizing programming language syntax and framework APIs without references"],
correctOption: 1,
explanation: "Orchestrators focus on the judgment work: writing clear specifications, gathering requirements, designing architecture, and validating AI output. AI handles the mechanical implementation.",
source: "Lesson 3: From Coder to Orchestrator"
},
{
question: "What are the Five Powers that enable autonomous agents?",
options: ["Five cloud providers for deploying production-grade AI systems globally", "Five programming languages every agent developer must master completely", "Five types of machine learning models used in enterprise production stacks", "See, Hear, Reason, Act, Remember—five capabilities that combine for autonomous orchestration"],
correctOption: 3,
explanation: "The Five Powers are: See (visual understanding), Hear (audio processing), Reason (complex decision-making), Act (execute and orchestrate), Remember (maintain context and learn). Combined, they enable autonomous orchestration.",
source: "Lesson 4: Five Powers and the Modern AI Stack"
},
{
question: "In the Modern AI Stack, what role do AI-First IDEs (Layer 2) play?",
options: ["They act as context orchestrators, intelligently selecting relevant code for models", "They train the AI models on new code patterns from the active codebase", "They replace the need for frontier models by running local inference efficiently", "They only provide syntax highlighting and basic autocomplete functionality"],
correctOption: 0,
explanation: "AI-First IDEs like Cursor and Windsurf are context orchestrators. They intelligently select relevant code, host skills, and create the environment where models, tools, and files meet—solving the context management problem.",
source: "Lesson 4: Five Powers and the Modern AI Stack"
},
{
question: "What is the primary advantage of a modular, three-layer AI stack compared to monolithic tool ecosystems?",
options: ["It eliminates the need for AI frontier models in the development workflow", "It guarantees all tools are free and open-source under permissive licenses", "It prevents vendor lock-in and enables faster evolution by composing independent layers", "It requires substantially less onboarding time for developers to become productive"],
correctOption: 2,
explanation: "The modular stack (Frontier Models → AI-First IDEs → Agent Skills) prevents vendor lock-in. You can swap models via API, choose best-of-breed at each layer, and evolve your stack independently.",
source: "Lesson 4: Five Powers and the Modern AI Stack"
},
{
question: "How does MCP (Model Context Protocol) function as the 'USB cable for AI'?",
options: ["It physically connects AI hardware accelerators to host computers", "It compresses data for faster and more efficient transmission between services", "It only works with Anthropic's Claude models via proprietary protocol extensions", "It provides a standardized protocol so any MCP-compatible agent can use any MCP server"],
correctOption: 3,
explanation: "MCP standardizes agent-to-tool connections. Instead of M agents × N tools = M×N custom integrations, MCP provides one protocol for all. Any MCP-compatible agent (Claude, ChatGPT, Gemini, custom) can use any MCP server.",
source: "Lesson 4: Five Powers and the Modern AI Stack"
},
{
question: "What is the primary business benefit of AAIF (Agentic AI Foundation) for building Digital FTEs?",
options: ["It ensures your Digital FTEs are portable investments that work across platforms, not locked to a single vendor", "It provides free cloud hosting infrastructure for all deployed AI agent workloads", "It automatically generates production-ready code templates for your custom agents", "It provides access to frontier AI models at substantially discounted API prices"],
correctOption: 0,
explanation: "AAIF provides neutral governance for open standards (MCP, AGENTS.md, goose), ensuring your Digital FTEs can connect to any CRM, work with any AI platform, and adapt to any client's workflow—without custom integration per platform.",
source: "Lesson 5: AIFF Standards Foundation"
},
{
question: "In MCP's three primitives, what is the difference between Resources and Tools?",
options: ["Resources are free while Tools require subscription payment to access", "Resources provide data to read (agent's 'eyes'); Tools execute actions (agent's 'hands')", "Resources work locally in the IDE; Tools work remotely via cloud API calls", "Resources are designed for developers only; Tools are designed for end users"],
correctOption: 1,
explanation: "Resources are what your Digital FTE can see—lead data from CRM, email history, company information. Tools are what your Digital FTE can do—create records, send emails, schedule meetings. Resources read; Tools act.",
source: "Lesson 5: AIFF Standards Foundation"
},
{
question: "You're selling the same Digital FTE to 100 different enterprise clients, each with different coding conventions, build commands, and deployment pipelines. Which standard eliminates per-client customization work?",
options: ["MCP — provides connectivity so agents can talk to each client's tool stack", "Progressive Disclosure — loads skill metadata only when that client activates a feature", "goose — open-source framework that adapts workflows across diverse environments", "AGENTS.md — enables zero-config deployments where the Digital FTE reads each client's environment automatically"],
correctOption: 3,
explanation: "AGENTS.md is README for AI agents. Your Digital FTE reads each client's AGENTS.md to understand their coding conventions, build commands, and security requirements—deploying to 100 different organizations without customization.",
source: "Lesson 5: AIFF Standards Foundation"
},
{
question: "What is the key difference between MCP and Agent Skills?",
options: ["MCP is open-source while Agent Skills are proprietary and vendor-specific", "MCP works only with Claude models; Agent Skills work only with ChatGPT models", "MCP provides connectivity (how agents talk to tools); Skills provide expertise (what agents know how to do)", "MCP is for reading data; Agent Skills are exclusively for writing and modifying data"],
correctOption: 2,
explanation: "MCP and Skills are complementary, not competing. MCP connects to tools (agent's hands); Skills encode expertise (agent's training). For Stripe payments: MCP Server connects to Stripe API, while a Skill knows payment best practices.",
source: "Lesson 5: AIFF Standards Foundation"
},
{
question: "What is 'Progressive Disclosure' in the Agent Skills standard?",
options: ["Loading only skill metadata at startup (~100 tokens), full instructions when activated (<5k), resources on-demand", "Teaching skills progressively from simple beginner tasks to complex expert workflows", "Hiding advanced agent features from new users until they reach a proficiency threshold", "Gradually revealing product features to end users based on engagement and usage patterns"],
correctOption: 0,
explanation: "Progressive Disclosure reduces token usage by 80-98%. At startup, agents see only name and description (~100 tokens per skill). Full SKILL.md loads when activated (<5k tokens). Supporting resources load only when actually needed.",
source: "Lesson 5: AIFF Standards Foundation"
},
{
question: "What distinguishes goose from Claude Code?",
options: ["goose is substantially more powerful than Claude Code for production agent workloads", "goose is open-source (Apache 2.0) with visible source code; Claude Code is proprietary", "goose was created by OpenAI while Claude Code was created by Anthropic for developers", "Claude Code only works offline in air-gapped environments; goose requires internet access"],
correctOption: 1,
explanation: "goose (from Block) is open-source under Apache 2.0—you can study its architecture, adapt patterns, and understand production agent implementation. Claude Code is proprietary. Use Claude Code for productivity today; study goose for building Custom Agents tomorrow.",
source: "Lesson 5: AIFF Standards Foundation"
},
{
question: "What is a Digital FTE?",
options: ["A part-time AI coding assistant that handles repetitive development work on demand", "A chatbot that answers employee questions about software tools and documentation", "A productivity tool that accelerates developer output by roughly twenty percent", "An autonomous AI agent executing the COMPLETE output of a human employee, focused on outcomes not tasks"],
correctOption: 3,
explanation: "FTE = Full-Time Equivalent. A Digital FTE is an autonomous AI agent that executes complete human employee output. Unlike tools (which require operators), Digital FTEs replace the need for operators by focusing on OUTCOMES, not individual tasks.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "In the 'Productivity Trap vs Ownership Model' story, why did Sarah get displaced while Marcus succeeded?",
options: ["Marcus had much deeper technical programming skills across all relevant engineering domains than Sarah", "Sarah didn't adopt or use AI coding tools effectively enough to keep pace with market automation", "Sarah used AI for productivity; Marcus built a Digital FTE encoding his expertise as a product he owns", "Marcus worked in a higher-value industry vertical that was far less vulnerable to AI-driven labor disruption"],
correctOption: 2,
explanation: "Sarah positioned AI as a productivity tool—when a cheaper Digital FTE launched, it directly competed with her labor. Marcus positioned his expertise as a product that AI delivers—he owns the Digital FTE that competes with his own labor.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "What is 'The Moat' in Digital FTE positioning?",
options: ["The 10% of nuanced, experience-based insights that generic AI cannot replicate reliably", "A water feature around data centers for physical security and cooling purposes", "A legal intellectual property protection mechanism for proprietary AI agent code", "The amount of GPU compute power required to run production-grade agent workloads"],
correctOption: 0,
explanation: "The 90/10 split: 90% is commodity (structure, grammar, basic facts—AI excels at this). 10% is the moat—nuance, edge cases, political context, 'gut check' based on years of experience. Your ability to filter, correct, and elevate AI output IS the moat.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "In the 'Snakes and Ladders' framework, which layer should third-party developers avoid competing in?",
options: ["Layer 2: General Agents as Developer Tools for everyday productivity", "Layer 1: Consumer AI Backbone (OpenAI vs Google war)", "Layer 3: Custom Agents built for specific vertical industry markets", "Layer 4: Orchestrator Layer combining multiple agents into workflows"],
correctOption: 1,
explanation: "Layer 1 is a brutal two-player game where only OpenAI and Google survive (billions in data, compute, marketing). Don't compete here—avoid the snake. Instead, climb the ladder at Layer 2 (developer tools) or Layer 3 (vertical markets).",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "What is the economic advantage of Digital FTE labor over human labor for customer support?",
options: ["Digital FTEs provide superior emotional support through more empathetic responses", "Digital FTEs require zero infrastructure investment compared to human support teams", "Digital FTEs only handle simple queries but do so at roughly the same cost", "Digital FTEs cost ~$3/ticket vs ~$150/ticket for humans, with 24/7 availability"],
correctOption: 3,
explanation: "Human agent: $6k/month, 40 hrs/week, 20 tickets/day = $150/ticket. Digital FTE: $1.5k/month, 168 hrs/week, 500+ tickets/day = $3/ticket. Digital FTE is ~50x more cost-efficient with 24/7 availability.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "When would a 'Success Fee' model be better than 'Subscription' for Digital FTE pricing?",
options: ["When you want stable recurring passive income without performance accountability", "When clients want fully predictable fixed monthly operating costs for budgeting", "When outcomes are easily measurable and clients are skeptical ('prove it first')", "When clients need around-the-clock support coverage across multiple time zones"],
correctOption: 2,
explanation: "Success Fee (commission on measured outcomes) works when: outcomes are easy to measure, clients are skeptical and want proof first, and you're confident the solution works. Subscription works better for predictable costs and hands-off automation.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "A medical startup wants to validate their AI diagnostic assistant before allowing it to operate autonomously. They need the agent to run and generate outputs while physicians retain all final decision authority, logging everything for accuracy comparison. Which deployment strategy does this describe?",
options: ["Shadow Mode — agent runs and generates recommendations while humans retain all final decisions and everything is logged for comparison", "Progressive Deployment — agent operates at night when patient volume is lowest to limit risk", "Staged Rollout — agent is hidden from end users while backend teams verify accuracy metrics", "Full Autonomy — agent executes decisions immediately after recommendation generation"],
correctOption: 0,
explanation: "Shadow Mode (Weeks 1-4): Agent runs, generates recommendations, but humans make all final decisions. Log all outputs and decisions. Measure: Does agent agree with humans 80%+? This validates accuracy before any autonomous operation.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "Which scenario represents a valid use case for autonomous AI agents?",
options: ["AI sending completed legal opinions directly to clients without any attorney review", "AI recommending actions for human review and approval before any execution occurs", "AI executing financial transactions without prior human authorization or oversight", "AI screening resumes and advancing only 'qualified' candidates without human review"],
correctOption: 1,
explanation: "Agent should RECOMMEND; human should APPROVE. Legal decisions, medical recommendations, financial transactions, and hiring decisions all require human oversight due to liability, regulatory, and ethical requirements.",
source: "Lesson 6: Digital FTE Business Strategy"
},
{
question: "What defines AI-Driven Development (AIDD)?",
options: ["Using AI to generate all code without any human involvement in the process", "Using AI exclusively for testing, debugging, and quality assurance tasks only", "Replacing developers entirely with autonomous AI systems that self-manage", "A specification-first methodology transforming developers into specification engineers and architects"],
correctOption: 3,
explanation: "AIDD is a specification-first methodology where agents handle implementation while developers focus on architecture and validation. It has nine core characteristics including specification-driven, AI-augmented, quality-gated, and human-verified.",
source: "Lesson 7: Nine Pillars of AIDD"
},
{
question: "Why does 'Markdown as Programming Language' (Pillar 2) enable new development patterns?",
options: ["Markdown is substantially faster to parse than compiled programming languages", "Markdown eliminates the need for all traditional programming languages in a stack", "Markdown specs become executable 'source code' that AI agents read and implement directly", "Markdown is only useful for documentation and has no role in active development"],
correctOption: 2,
explanation: "Markdown specifications become the human-readable 'source code' that AI agents implement. This removes the massive cognitive load of translating ideas into rigid syntax—you express intent, AI handles implementation details.",
source: "Lesson 7: Nine Pillars of AIDD"
},
{
question: "What is an 'M-Shaped Developer' and why was it nearly impossible before AI?",
options: ["A developer with deep expertise in 2-4 complementary domains, enabled by AI handling cognitive load across areas", "A developer who only creates mobile applications and nothing else in their career", "A developer who manages multiple development teams across different product lines", "A developer who works exclusively on Monday through Friday with no weekend hours"],
correctOption: 0,
explanation: "M-Shaped developers have deep expertise in 2-4 complementary domains (e.g., full-stack + DevOps + ML). Before AI, mastering multiple domains required overwhelming cognitive load and hours that weren't available. The nine pillars remove these barriers.",
source: "Lesson 7: Nine Pillars of AIDD"
},
{
question: "Why is partial adoption of AIDD pillars (e.g., 6 of 9) less effective than complete adoption?",
options: ["Some pillars are inherently more important than others and must be prioritized first", "Partial adoption always costs more in tooling licenses than adopting all nine pillars", "The pillars are designed to function only as a complete integrated set, not individually", "Partial adoption creates gaps; pillars multiply effects exponentially when combined, not just add linearly"],
correctOption: 3,
explanation: "Individual tools add value linearly (10-20% gains). Nine pillars working together multiply effects exponentially. Without complete adoption, bottlenecks remain. Example: Skills (Pillar 8) depend on MCP (Pillar 3), SDD (Pillar 7), and Markdown (Pillar 2).",
source: "Lesson 7: Nine Pillars of AIDD"
},
{
question: "What is the core equation of Spec-Driven Development?",
options: ["More code written quickly equals better and more reliable software results", "Vague Idea + AI = 5+ iterations; Clear Specification + AI = 1-2 iterations", "Faster coding speed leads directly to higher quality and fewer production defects", "Documentation is equivalent to specification and can substitute for it in practice"],
correctOption: 1,
explanation: "The bottleneck has shifted to specification. With clear specs, AI implements in 1-2 refinement cycles. With vague ideas, you spend 5+ iterations on misalignment. SDD front-loads the thinking work for faster, more accurate results.",
source: "Lesson 8: Spec-Driven Development"
},
{
question: "A developer writes a spec with clear Intent, Success Criteria, and Constraints — but omits Non-Goals. What risk does this missing element create for the project?",
options: ["The AI will refuse to generate code without all four elements present in the document", "The spec cannot be shared with teammates because it fails validation requirements", "Non-Goals are optional metadata only needed for compliance documentation purposes", "Scope creep risk — without explicit boundaries, AI may implement features outside intended scope"],
correctOption: 2,
explanation: "A complete specification includes: Intent (why does this exist?), Success Criteria (what does correct look like?), Constraints (what limits exist?), and Non-Goals (what are we explicitly NOT building?). Non-Goals prevent scope creep.",
source: "Lesson 8: Spec-Driven Development"
},
{
question: "A team wants to adopt the SDD workflow. Their tech lead asks what the correct sequence of phases is. Which answer is accurate?",
options: ["Specify, Clarify, Plan, Tasks, Implement, Validate", "Plan, Code, Test, Deploy, Monitor, Maintain in that order", "Gather, Analyze, Design, Build, Review, Release as standard phases", "Discovery, Definition, Design, Development, Delivery, Deployment across six stages"],
correctOption: 0,
explanation: "The SDD workflow: Specify (define what), Clarify (remove ambiguity), Plan (design how), Tasks (break down work), Implement (AI executes), Validate (verify quality). Each phase has a quality gate before proceeding.",
source: "Lesson 8: Spec-Driven Development"
},
{
question: "When is 'Vibe Coding' appropriate vs when is SDD essential?",
options: ["Vibe coding is always the faster and superior approach for experienced senior developers working on complex problems", "SDD is only necessary for large enterprise teams with multiple developers; solo developers can always vibe code", "Both approaches produce identical quality results when the developer is sufficiently skilled and experienced", "Vibe coding works for learning and throwaway code; SDD is essential for production, security-critical, or AI-assisted work"],
correctOption: 3,
explanation: "Vibe coding works for learning experiments, throwaway prototypes, and simple scripts (<50 lines). SDD is essential when there's business impact, complexity, security/compliance requirements, multiple developers, or AI assistance.",
source: "Lesson 8: Spec-Driven Development"
},
{
question: "A developer starts using AI to generate code without writing specifications first. Their codebase grows rapidly but becomes increasingly difficult to debug and modify. Which principle explains this outcome?",
options: ["Specification-Driven Amplification — each unclear requirement compounds into multiple misaligned outputs requiring rework", "Vibe coding generates technically correct but semantically wrong code due to prompt ambiguity", "AI performance degrades — models produce worse code as context windows fill up with poor examples", "Testing gaps — without specs, AI skips edge case handling and produces incomplete implementations"],
correctOption: 1,
explanation: "AI generates code instantly but won't write specs you didn't ask for or tests you didn't request. Vibe Coding + AI = Amplified Chaos. Spec-Driven + AI = Amplified Excellence. The discipline becomes more critical, not less.",
source: "Lesson 8: Spec-Driven Development"
},
{
question: "What distinguishes a Digital FTE from a 'tool' in the AI era?",
options: ["Digital FTEs are substantially more expensive than traditional software tools and require dedicated AI ops teams", "Digital FTEs only work for large enterprise clients with dedicated AI infrastructure and compliance teams", "Tools wait for prompts; Digital FTEs monitor domains, identify needs, and execute solutions with 24/7 autonomous operation", "Tools are AI-powered products while Digital FTEs use legacy rule-based automation without machine learning components"],
correctOption: 2,
explanation: "The FTE threshold isn't just what an agent CAN do, but HOW it exists. Tools wait for prompts. Digital FTEs monitor their domain, identify needs, and execute solutions with the reliability and persistence of a human team member—24/7 autonomous operation.",
source: "Lesson 9: Synthesis - The Digital FTE Vision"
},
{
question: "What does 'AI is an amplifier' mean for the choice between Vibe Coding and SDD?",
options: ["AI amplifies good habits (SDD) AND bad habits (Vibe Coding)—discipline matters MORE with AI, not less", "AI makes both approaches produce equivalent quality with different speed tradeoffs", "AI eliminates any meaningful difference between structured and unstructured approaches", "AI only amplifies positive development outcomes regardless of underlying methodology used"],
correctOption: 0,
explanation: "AI is an amplifier—it amplifies whatever direction you're heading. Clear specifications lead to excellent results fast. Vague requirements lead to terrible results fast. This is why SDD matters MORE in the AI era, not less.",
source: "Lesson 9: Synthesis - The Digital FTE Vision"
},
{
question: "What creates the 'virtuous cycle' in the Agent Factory paradigm?",
options: ["Using more expensive frontier AI models with larger parameter counts, context windows, and training data", "Hiring more senior developers specifically to review AI output faster and more thoroughly at scale", "Focusing exclusively on one highly specialized agent type to maximize performance within that single domain", "Clear specs → precise execution → reliable agents → Digital FTEs → multiplied capacity → larger problems → even better specs"],
correctOption: 3,
explanation: "Everything compounds: clear specs lead to precise AI execution, which enables reliable Custom Agents, which become Digital FTEs, which multiply capacity for larger problems, which require even better specs. The gap widens with each AI generation.",
source: "Lesson 9: Synthesis - The Digital FTE Vision"
},
{
question: "According to Chapter 1, what is the fundamental choice developers face?",
options: ["Whether to adopt open-source or proprietary AI tools for daily development work", "Path A (treat AI as faster keyboard, vibe code) vs Path B (master Agent Factory paradigm, build Digital FTEs)", "Which programming language to prioritize learning as AI reshapes the industry landscape", "Whether to work remotely or in-office as AI changes team collaboration dynamics"],
correctOption: 1,
explanation: "Path A: Treat AI as a faster keyboard, vibe code, watch technical debt compound while competitors build systematic capabilities. Path B: Master the Agent Factory paradigm, clear specifications, build Digital FTEs, multiply capacity systematically. This book teaches Path B.",
source: "Lesson 9: Synthesis - The Digital FTE Vision"
},
{
question: "According to McKinsey's 2025 survey, what percentage of C-suite executives are already running agentic AI pilots?",
options: ["Around 50% across all industry sectors surveyed", "Approximately 65% concentrated in technology companies", "More than 80%", "Close to 95% of enterprises in the Fortune 500"],
correctOption: 2,
explanation: "McKinsey's July 2025 survey of 200 C-suite executives found that more than 80% are already running pilots on agentic AI, with some progressing to scaled deployments. This represents a massive market opportunity for Digital FTE providers.",
source: "Lesson 10: Selling Agentic AI Services"
},
{
question: "Which of the following is NOT one of the six core factors enterprises cite when choosing an agentic AI service provider?",
options: ["Ability to customize solutions for specific enterprise workflows and requirements", "Domain expertise in the specific industry vertical being automated", "Outcome-based pricing models that align vendor incentives with client results", "Lowest price guarantee ensuring the vendor will always beat any competitor quote"],
correctOption: 3,
explanation: "Enterprises prioritize: (1) customization ability, (2) partnership ecosystem and IP, (3) consultative sales, (4) domain expertise, (5) line-of-business-focused delivery, and (6) outcome-based pricing. Price alone is not a core factor—value and outcomes matter more than being cheapest.",
source: "Lesson 10: Selling Agentic AI Services"
},
{
question: "In McKinsey's four value propositions for the agentic era, which role best fits someone who builds bespoke AI solutions for specific industries?",
options: ["Custom Agent Developer — creates bespoke agentic AI solutions tailored to unique enterprise needs", "Agentic AI Enabler providing infrastructure and tooling to other AI builders", "Packaged Agent Implementer deploying pre-built solutions across many similar clients", "End-to-End Workflow Disruptor replacing entire business functions with autonomous AI"],
correctOption: 0,
explanation: "Custom Agent Developer creates bespoke agentic AI solutions tailored to unique enterprise needs. This requires domain expertise, agentic-stack development capabilities, and deep understanding of enterprise workflows—ideal for specialized industry knowledge.",
source: "Lesson 10: Selling Agentic AI Services"
},
{
question: "Why do more than 70% of enterprises prefer outcome-based pricing over traditional time-and-materials models?",
options: ["Outcome-based pricing is always cheaper than hourly billing regardless of scope", "It requires substantially less negotiation time than complex time-and-materials contracts", "It aligns provider incentives with measurable business results and reduces client risk", "It eliminates the need for project management oversight and milestone tracking"],
correctOption: 2,
explanation: "Outcome-based pricing (gain-share, subscription, fixed-price) aligns provider revenue with client value. If the AI solution delivers measurable savings or productivity gains, both parties win. This reduces client risk and builds trust—traditional hourly rates risk margin erosion without delivering proven value.",
source: "Lesson 10: Selling Agentic AI Services"
},
{
question: "The Agent Triangle classifies agentic AI into three paths. Which path describes Pre-Built AI Employees like OpenClaw, Manus, and Devin?",
options: ["Option A: Smart Consultant — session-based reasoning for novel one-off problems", "Option C: Pre-Trained New Hire — pre-packaged, always-on, onboard to your systems", "Option B: Assembly Line — custom-built with SDKs for production workflow automation", "Option D: Hybrid Agent — combines all three triangle approaches in one integrated system"],
correctOption: 1,
explanation: "Pre-Built AI Employees (Option C) arrive pre-trained with capabilities. You onboard them to your systems rather than building from scratch. They're always-on, multi-channel, and have persistent memory — like hiring a skilled employee who already knows their craft.",
source: "Preface: The AI Agent Factory"
},
{
question: "In the Agent Triangle, what distinguishes Custom-Built AI Employees (Option B) from Pre-Built AI Employees (Option C)?",
options: ["Option B uses rule-based systems while Option C uses modern AI language models", "Option B is exclusively for large enterprises while Option C serves individual developers", "Option B is completely free to deploy while Option C requires an ongoing subscription fee", "Option B requires you to architect every workflow; Option C comes pre-trained and you configure/onboard"],
correctOption: 3,
explanation: "Both B and C produce Digital FTEs. The difference is the classic Build vs. Buy decision: with B, you are the architect defining every guardrail and hand-off. With C, you are the manager onboarding a pre-trained employee to your systems.",
source: "Preface: The AI Agent Factory"
},
{
question: "Which options in the Agent Triangle are classified as Digital FTEs (AI Employees)?",
options: ["Options B and C — both are Digital FTEs, distinguished by Build vs. Buy", "Only Option A — General Agents that consult on specific session-based problems", "Only Option B — Custom-Built AI Employees built with development frameworks and SDKs", "All three options A, B, and C qualify as Digital FTEs across different deployment contexts"],
correctOption: 0,
explanation: "Options B (Custom-Built) and C (Pre-Built) are both Digital FTEs — permanent AI employees. Option A (General Agents) are 'Smart Consultants' or contractors — you bring them in for a specific problem, they deliver the result, and leave. The B vs C distinction is the classic Build vs. Buy decision.",
source: "Preface: The AI Agent Factory"
},
{
question: "A startup wants an always-on assistant that monitors their servers via Slack, manages their calendar, and proactively alerts about issues — with minimal setup time. Which Agent Triangle path is most appropriate?",
options: ["Option A: Use Claude Code interactively to build and run a custom monitoring script", "Option B: Build a custom agent from scratch using OpenAI Agents SDK with full control", "Option C: Onboard a Pre-Built AI Employee like OpenClaw for fast deployment", "Skip agents entirely and hire a dedicated human DevOps engineer for reliability"],
correctOption: 2,
explanation: "This scenario calls for Option C — always-on presence, multi-channel (Slack), persistent memory, proactive behavior, and fast time-to-value. Pre-Built AI Employees like OpenClaw are designed exactly for this: you configure and onboard rather than build from scratch.",
source: "Preface: The AI Agent Factory"
}
]}
/>
