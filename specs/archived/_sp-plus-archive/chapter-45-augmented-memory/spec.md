# Chapter 45: Augmented Memory for Agentic Applications

## Specification v1.0

---

## Overview

This chapter teaches how to add persistent memory to AI agents, transforming stateless LLM interactions into contextual, personalized experiences. Students will understand memory architecture patterns conceptually before implementing with Mem0 and claude-mem.

### Position in Curriculum

- **Part**: 6 - AI-Native Software Development
- **Chapter**: 45
- **Prerequisites**: Ch33 (Agent fundamentals), Ch34-36 (Agent SDKs), Ch40 (FastAPI)
- **Target Proficiency**: B1 (intermediate)
- **Total Duration**: 265 minutes (9 lessons)

### Running Example

Task API agent from Ch40, enhanced with:
- User preference memory
- Task pattern recognition
- Context-aware recommendations

---

## Learning Outcomes

By completing this chapter, students will be able to:

1. **Explain** why agents need persistent memory beyond context windows (Understand)
2. **Classify** different memory types (conversation, working, episodic, semantic) (Understand)
3. **Design** memory prioritization and forgetting strategies (Apply)
4. **Implement** retrieval strategies (recency, relevance, hybrid) (Apply)
5. **Manage** context window constraints with summarization (Apply)
6. **Build** memory-augmented agents using Mem0 (Apply)
7. **Integrate** memory patterns into existing agent systems (Apply)
8. **Configure** claude-mem for Claude Code agents (Apply)

---

## Chapter Structure

### IMPORTANT: NO L00 FOR THIS CHAPTER

User explicitly requested: Skip L00 (Skill-First) entirely.
- This chapter teaches concepts deeply before implementation
- Mem0 is simple enough that skill-building happens during implementation
- Start directly with L01

---

## Lesson Breakdown

### L01: Why Agents Need Memory (20 min)

**Layer**: L1 (Manual/Conceptual)
**Proficiency**: B1

**Learning Objectives**:
- Understand the context window problem
- Distinguish stateless vs stateful agents
- Identify types of information agents should remember
- Recognize memory as competitive advantage

**Content Outline**:
1. The Amnesia Problem (context windows as temporary buffers)
2. Stateless vs Stateful Agents (comparison table)
3. What Agents Should Remember (user identity, preferences, patterns)
4. Memory as Competitive Advantage (business value)

**Key Concepts**: context window, stateless, stateful, session, persistence

---

### L02: Memory Architecture Patterns (30 min)

**Layer**: L1 (Manual/Conceptual)
**Proficiency**: B1

**Learning Objectives**:
- Understand five types of agent memory
- Map cognitive science concepts to agent systems
- Choose appropriate memory types for different needs
- Design memory architecture for Task API

**Content Outline**:
1. Conversation Memory (Short-term) - sliding window
2. Long-term Memory - persistent facts
3. Working Memory - current task context
4. Episodic Memory - time-stamped events
5. Semantic Memory - knowledge graph/entities

**Key Concepts**: conversation memory, working memory, episodic memory, semantic memory, memory blocks (Letta reference)

**Diagram**: Memory architecture showing tiers

---

### L03: What to Remember and What to Forget (25 min)

**Layer**: L1 → L2 (Conceptual → Collaboration)
**Proficiency**: B1

**Learning Objectives**:
- Apply memory prioritization strategies
- Implement relevance scoring for memories
- Design memory consolidation approaches
- Handle active forgetting (privacy, outdated info)

**Content Outline**:
1. The Memory Prioritization Problem
2. Relevance Scoring (formula: recency + importance + access frequency)
3. Memory Consolidation (summarizing old memories)
4. Active Forgetting (GDPR, outdated info, contradictions)
5. Memory Hygiene (deduplication, contradiction resolution)

**Key Concepts**: relevance scoring, consolidation, decay, right to forget

---

### L04: Memory Retrieval Strategies (25 min)

**Layer**: L2 (Collaboration)
**Proficiency**: B1

**Learning Objectives**:
- Implement recency-based retrieval
- Implement relevance-based retrieval (vector similarity)
- Design entity-based retrieval
- Combine strategies with hybrid retrieval

**Content Outline**:
1. Recency-based Retrieval (most recent first)
2. Relevance-based Retrieval (semantic search)
3. Entity-based Retrieval (memories about specific entities)
4. Hybrid Retrieval (weighted combination)
5. The Context Window Budget (token constraints)

**Key Concepts**: semantic search, hybrid retrieval, entity extraction, token budget

**Code Examples**: Retrieval strategy pseudocode/patterns

---

### L05: Context Window Management (25 min)

**Layer**: L2 (Collaboration)
**Proficiency**: B1

**Learning Objectives**:
- Understand fixed context window constraints
- Design memory injection strategies
- Implement summarization chains
- Apply memory compression techniques

**Content Outline**:
1. The Fixed Context Window (GPT-4: 128k, Claude: 200k)
2. Memory Injection Strategies (pre-prompt, mid-prompt, dynamic)
3. Summarization Chains (hierarchical: session → week → month)
4. Memory Compression Techniques (key-value extraction, deduplication)
5. When to Retrieve vs Summarize (decision tree)

**Key Concepts**: context window, token budget, injection, summarization, compression

---

### L06: Implementing Memory with Mem0 (35 min)

**Layer**: L2 → L3 (Collaboration → Implementation)
**Proficiency**: B1

**Learning Objectives**:
- Install and configure Mem0
- Add memories from conversations
- Search memories with filters
- Integrate with Task API agent

**Content Outline**:
1. Installation and Setup (`pip install mem0ai`)
2. Basic Memory Operations (add, search)
3. Memory Categories and Metadata
4. Integrating with Task API (FastAPI example)
5. Testing Memory Across Sessions

**Code Examples**: Full working Mem0 integration with Task API

**Key Concepts**: Mem0, user_id, filters, metadata, persistence

---

### L07: Memory-Augmented Agent Patterns (30 min)

**Layer**: L3 (Implementation)
**Proficiency**: B1

**Learning Objectives**:
- Implement pre-prompt memory injection
- Design dynamic memory retrieval during conversation
- Update memories after interactions
- Test memory-augmented agents

**Content Outline**:
1. Pre-prompt Memory Injection (build_prompt pattern)
2. Dynamic Memory Retrieval (entity-based during conversation)
3. Memory Update After Interactions (store new memories)
4. Handling Memory Conflicts (timestamp resolution)
5. Testing Memory-Augmented Agents (unit + integration)

**Code Examples**: Complete memory-augmented agent implementation

**Key Concepts**: prompt injection, dynamic retrieval, conflict resolution, testing

---

### L08: Building a Memory-Augmented Agent (40 min)

**Layer**: L3 (Implementation)
**Proficiency**: B1

**Learning Objectives**:
- Build complete agent with memory tools using OpenAI Agents SDK and Mem0
- Implement memory retrieval that enhances agent responses
- Design agent instructions that leverage stored memories
- Test memory persistence across independent agent sessions

**Content Outline**:
1. Project Structure and Setup
2. Building Memory Tools (@function_tool decorators for recall, store, list, forget)
3. Creating the Task Manager Agent (memory-aware instructions)
4. Running the Agent (conversation loop with Runner)
5. Testing Memory Persistence (multi-session tests)
6. Architecture Summary

**Key Concepts**: function_tool, Agent, Runner, memory tools, session persistence

**Code Examples**: Complete working project with memory tools, agent definition, main loop, tests

---

### L09: Memory for Claude Code (35 min)

**Layer**: L3 (Application)
**Proficiency**: B1

**Learning Objectives**:
- Install and configure claude-mem plugin for Claude Code
- Configure privacy controls to prevent storage of sensitive information
- Use the web UI to inspect and manage stored memories
- Leverage MCP tools for memory search within conversations

**Content Outline**:
1. Installation from Plugin Marketplace
2. How It Works (lifecycle hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd)
3. Privacy Controls (`<private>` tags, excluded patterns)
4. Web UI (localhost:37777 - timeline, search, management)
5. MCP Tools (search, timeline, get_observations)
6. Experiencing Memory-Augmented Claude Code
7. Workflow Patterns (project onboarding, decision documentation, error patterns)

**Key Concepts**: claude-mem, lifecycle hooks, privacy tags, web UI, MCP tools

---

## Safety Notes (Emphasize Throughout)

1. **Privacy Requirements**: User memory is sensitive personal data
2. **User Consent**: Explicit consent before memory creation
3. **Right to Be Forgotten**: Implement deletion requests (GDPR/CCPA)
4. **Data Retention**: Define retention policies
5. **PII Handling**: Never store PII without explicit consent

---

## Technical Requirements

### Dependencies

```bash
pip install mem0ai
export OPENAI_API_KEY="your-key"
```

### Platform

- Python 3.11+
- Local development environment
- OpenAI API access (for Mem0 defaults)

---

## Running Example Integration

The Task API agent from Ch40 will:

1. **Remember User Preferences**
   - Preferred task times (morning/evening)
   - Priority weightings
   - Category preferences

2. **Recall Past Project Contexts**
   - "The project" resolves to most recent active project
   - Project-specific terminology

3. **Store Learned Patterns**
   - How user structures tasks
   - Completion time estimates
   - Workflow preferences

4. **Surface Relevant Memories**
   - When creating tasks, inject relevant history
   - When reviewing, show patterns

---

## Layer Progression

| Lesson | Layer | Focus |
|--------|-------|-------|
| L01 | L1 | Conceptual - Why memory matters |
| L02 | L1 | Conceptual - Architecture patterns |
| L03 | L1→L2 | Design - Prioritization strategies |
| L04 | L2 | Collaboration - Retrieval design |
| L05 | L2 | Collaboration - Context management |
| L06 | L2→L3 | Implementation - Mem0 integration |
| L07 | L3 | Implementation - Agent patterns |
| L08 | L3 | Implementation - Complete agent build (OpenAI Agents SDK + Mem0) |
| L09 | L3 | Application - Personal agent memory (claude-mem) |

---

## Content Requirements

Every lesson MUST include:

1. **Full YAML Frontmatter**
   - sidebar_position, title, description, keywords
   - skills (hidden, with proficiency_level, bloom_level)
   - learning_objectives
   - cognitive_load assessment
   - differentiation (extension/remedial)

2. **Compelling Narrative Opening**
   - Real-world scenario
   - Business/practical hook
   - 2-3 paragraphs before first section

3. **Three "Try With AI" Prompts**
   - Each targets different aspect
   - Each has "What you're learning:" explanation
   - Prompts in code blocks (copyable)
   - Final prompt connects to reader's domain

4. **Evidence Blocks**
   - All code examples have Output: blocks
   - Show expected results

5. **NO Summary Section After Try With AI**
   - Chapter ends with activities, not summaries

---

## Quality Reference

Match structure and quality of:
`apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-digital-fte-revolution.md`

---

## Expertise Skill Reference

Use patterns from:
`.claude/skills/building-with-agent-memory/SKILL.md`

This skill contains verified API patterns, architecture diagrams, and code examples from official documentation.

---

## Output Location

```
apps/learn-app/docs/06-AI-Native-Software-Development/45-augmented-memory/
├── README.md
├── 01-why-agents-need-memory.md
├── 02-memory-architecture-patterns.md
├── 03-what-to-remember-and-forget.md
├── 04-memory-retrieval-strategies.md
├── 05-context-window-management.md
├── 06-implementing-memory-with-mem0.md
├── 07-memory-augmented-agent-patterns.md
├── 08-building-a-memory-augmented-agent.md
└── 09-memory-for-claude-code.md
```

---

## Version History

- v1.1 (2025-12-30): Added L08 (OpenAI Agents SDK + Mem0 complete build) and L09 (claude-mem hands-on)
- v1.0 (2025-12-30): Initial specification
