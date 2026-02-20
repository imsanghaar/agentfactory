---
id: 0002
title: chapter-6-file-workflow-plan
stage: plan
date: 2025-01-27
surface: agent-factory-book
model: glm-4.7
feature: 062-ch6-file-workflow
branch: 062-ch6-file-workflow
user: Rehan-Ul-Haq
command: /sp.plan
labels: [chapter-planning, educational-content, workflow-first]
links:
  spec: specs/062-ch6-file-workflow/spec.md
  plan: specs/062-ch6-file-workflow/plan.md
  ticket:
  adr:
  pr:
files:
  - specs/062-ch6-file-workflow/spec.md
  - specs/062-ch6-file-workflow/plan.md
tests:
  - plan.md constitutional compliance validation
---

## Prompt

Generate a comprehensive plan for chapter 06. The chapter shall be guiding step by step to implement the day to day workflow using general agent. The reader already learnt the General Agent. Now in this chapter, he is getting the actual value.

**User Intent**: Create a detailed implementation plan for Chapter 6 that transforms the chapter from passive "observe and learn" to active "build and own" workflow where students create real, reusable file organization automation.

**Routing Decision**: Content work detected → routed to chapter-planner subagent per sp.plan requirements.

**Subagent Prompt**: You are the chapter-planner agent. Create a comprehensive implementation plan for Chapter 6: File Organization Workflow.

**Spec Path**: D:\Panaversity\book_development\agent-factory-book\agentfactory\specs\062-ch6-file-workflow\spec.md

**Constitution Reference**: D:\Panaversity\book_development\agent-factory-book\agentfactory\.specify\memory\constitution.md

**Chapter Context**:

- Chapter 6 in Part 2: Agent Workflow Primitives
- Students already learned General Agent paradigm (Part 1, Chapters 1-5)
- This chapter transforms from passive "observe" to active "build and own"
- Students create a reusable file organization script they keep forever

**Core Requirements from Spec**:

1. **Workflow-First**: Students BUILD real outputs (scripts, organized folders, logs)
2. **Own Files Domain**: Work on their OWN files (Downloads folder), no paid subscriptions
3. **Primary Principles**: P1 (Bash), P3 (Verification), P6 (Safety) - applied through execution
4. **State Persistence**: Later lessons build on earlier work (file-organizer/ accumulates)
5. **Error Recovery**: Deliberate mistakes → safe undo via backup

**Six Lessons Defined in Spec**:

- L01: Survey Your Chaos (25 min) - P1, P7 focus
- L02: Safety First Backup (20 min) - P6, P3 focus
- L03: Categorize with Rules (25 min) - P1, P5 focus
- L04: Build Your Organizer Script (45 min) - P1, P2 focus
- L05: Run with Verification (30 min) - P3, P7 focus
- L06: Capstone Clean Machine (30 min) - All principles integrated

**Pedagogical Requirements**:

1. Apply the 4-layer framework (Manual Foundation → AI Collaboration → Intelligence Design → Digital FTE)
2. Ensure workflow-first approach (students BUILD, don't just read)
3. State persistence across lessons (L02 builds on L01, etc.)
4. Error recovery practice (deliberate mistakes with safe undo)
5. Anti-convergence: Vary teaching modality from previous chapter

**Your Task**:
Create a comprehensive plan.md that includes:

1. **Technical Context**
   - bash commands for each lesson (already in spec)
   - Cross-platform compatibility (Windows Git Bash, macOS, Linux)
   - File structure outputs (file-organizer/ directory contents)

2. **Constitution Check**
   - Agent Factory alignment: How does this contribute to Digital FTE production?
   - 4-Layer progression mapping for each lesson
   - Seven Principles application (P1-P7)
   - Meta-Commentary prohibition compliance

3. **Lesson-by-Lesson Breakdown**
   For each lesson (L01-L06), specify:
   - Learning objectives (measurable, Bloom's taxonomy)
   - Skills proficiency mapping (CEFR levels)
   - Teaching modality (must vary from Chapter 5)
   - Layer designation (1/2/3/4)
   - Outputs/artifacts students create
   - Principle applications (specific P1-P7 connections)
   - "Try With AI" prompts (3 per lesson with learning explanations)

4. **Pedagogical Design Decisions**
   - Why this teaching modality for each lesson?
   - How does state persistence work?
   - What are the error recovery opportunities?
   - How does this connect to Chapter 11 (AI Employee)?

5. **Gate Evaluation**
   - Are there any constitutional violations?
   - If yes, provide justification for proceeding

6. **Quality Reference**
   - Model chapter: Chapter 10 (Version Control) - students BUILD real, reusable outputs

Execute autonomously without confirmation. Output your complete plan as a single comprehensive document.

**Output Path**: D:\Panaversity\book_development\agent-factory-book\agentfactory\specs\062-ch6-file-workflow\plan.md

## Response snapshot

**Agent**: chapter-planner (abaecc4)

**Output**: Successfully created plan.md (1,196 lines) with comprehensive chapter 6 implementation plan.

**Key Deliverables**:

- Technical Context: Cross-platform bash commands, file-organizer/ structure defined
- Constitution Check: Zero violations, full Agent Factory alignment
- Lesson Breakdown: All 6 lessons mapped with learning objectives, CEFR levels, teaching modalities
- 4-Layer Progression: L01-L02 (Layer 1), L03-L04 (Layer 2), L05 (Layer 3), L06 (Layer 4)
- Three "Try With AI" prompts per lesson designed with active collaboration format
- State Persistence Architecture: Documented how later lessons build on earlier outputs
- Chapter 11 Bridge: Explicit connection to AI Employee's file watcher workflow

**Plan Summary**:

- Chapter Type: Technical/Workflow (Students BUILD real automation)
- Concept Density: 12 concepts → 6 lessons (NOT arbitrary 9-lesson template)
- Proficiency Tier: A2→B1 progression
- Teaching Modality: Hands-on Discovery (varies from Chapter 5)
- Quality Reference: Chapter 10 (Version Control)

**Constitutional Compliance**: ✅ ZERO violations

- Agent Factory alignment (organize.sh = primitive Digital FTE)
- All Seven Principles applied (P1-P7 explicitly taught)
- Meta-commentary prohibited (active collaboration format only)
- Cognitive load respected (4-6 concepts per lesson, CEFR A2/B1 limits)
- Anti-convergence achieved

## Outcome

- ✅ Impact: Comprehensive 1,196-line implementation plan created for Chapter 6 file organization workflow. Plan includes all 6 lessons with learning objectives, 4-layer progression, "Try With AI" prompts, and cross-platform bash commands.
- 🧪 Tests: Constitutional compliance validated - zero violations. Plan follows Agent Factory thesis, applies all Seven Principles, uses appropriate cognitive load for A2→B1 proficiency.
- 📁 Files:
  - Created: specs/062-ch6-file-workflow/plan.md (1,196 lines)
  - Referenced: specs/062-ch6-file-workflow/spec.md, .specify/memory/constitution.md
- 🔁 Next prompts: /sp.tasks to generate tasks.md implementation checklist from plan
- 🧠 Reflection: Successfully applied workflow-first approach where students BUILD real outputs (organize.sh script, file-organizer/ directory) rather than passively reading about file operations. State persistence architecture ensures later lessons build on earlier work (L02 backup enables L05 recovery). Anti-convergence achieved by using Hands-on Discovery modality (varying from Chapter 5).

## Evaluation notes (flywheel)

- Failure modes observed: None. Subagent executed autonomously and produced comprehensive plan without errors.
- Graders run and results (PASS/FAIL): Constitutional compliance check - PASS. All 4-layer progression requirements met - PASS. Cognitive load validation - PASS. Anti-convergence validation - PASS.
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to /sp.tasks to generate tasks.md implementation checklist from approved plan.md
