# Teacher Perspective Evaluation Rubric

Detailed criteria for evaluating educational content from an instructional design perspective.

## Learning Objectives Quality

### SMART Objectives Checklist

- **S**pecific: Clearly states what learner will do
- **M**easurable: Can verify if achieved
- **A**chievable: Realistic for proficiency level
- **R**elevant: Connected to chapter goals
- **T**ime-bound: Achievable within lesson duration

### Bloom's Taxonomy Alignment

| Level | Verbs | Example Objective |
|-------|-------|-------------------|
| Remember | List, Define, Identify | "Identify the three components of a skill" |
| Understand | Explain, Describe, Compare | "Explain when to use MCP vs skills" |
| Apply | Use, Implement, Execute | "Create a working SKILL.md file" |
| Analyze | Differentiate, Examine, Debug | "Debug why a skill isn't activating" |
| Evaluate | Judge, Assess, Recommend | "Evaluate which skills to compile vs use directly" |
| Create | Design, Build, Compose | "Design a multi-skill workflow for your domain" |

### Objective-Content Alignment Check

For each objective in frontmatter:
1. Is there content teaching this objective?
2. Is there practice/assessment for this objective?
3. Is the Bloom's level appropriate for proficiency?

### Objective Red Flags

| Problem | Example | Fix |
|---------|---------|-----|
| Vague verb | "Understand skills" | "Explain when skills activate" |
| Unmeasurable | "Appreciate the value of X" | "List 3 benefits of X" |
| Too ambitious | "Master async Python" (in one lesson) | "Write basic async/await code" |
| No assessment method | "Learn about MCP" | Add: "Assessment: Configure one MCP server" |

## Cognitive Load Management

### Concept Counting Rules

Count as "new concept":
- New terminology introduced
- New procedure/workflow
- New tool/command
- New decision framework
- New mental model

Do NOT count:
- Reinforcement of earlier concept
- Minor variation of known concept
- Simple fact (not requiring understanding)

### Load by Proficiency Level

| Level | Max New Concepts | Signs of Overload |
|-------|------------------|-------------------|
| A1 | 3-4 | More than 2 new terms per section |
| A2 | 4-5 | No practice between concepts |
| B1 | 5-7 | 3+ concepts in single paragraph |
| B2 | 6-8 | New concept every 100 words |
| C1 | 7-10 | Integration without foundation |
| C2 | 8-12 | Novel synthesis without examples |

### Cognitive Load Reducers

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| Chunking | Group related items | 3+ related concepts |
| Worked examples | Show complete solution | New procedures |
| Scaffolding | Provide structure to fill | Complex tasks |
| Analogy | Connect to known concept | Abstract ideas |
| Visual representation | Diagram/table | Relationships |

### Cognitive Overload Indicators

- Multiple new terms in single sentence
- No "pause" between concepts (practice, summary)
- Prerequisites introduced mid-lesson
- Information dump before action
- No repetition of key points

## Scaffolding Quality

### Scaffolding Checklist

- [ ] Prerequisites accurately listed
- [ ] Prior knowledge activated at start
- [ ] New builds on known
- [ ] Support provided, then faded
- [ ] Complexity increases gradually

### Scaffolding Patterns

**Good**: Gradual Release
1. Instructor demonstrates (I do)
2. Guided practice (We do)
3. Independent practice (You do)

**Good**: Incremental Complexity
1. Simplest case first
2. Add one variable
3. Add edge cases
4. Full complexity

**Bad**: Sink or Swim
1. Show complex example
2. "Now you try"
3. No intermediate steps

### Gap Detection

| Gap Type | Indicator | Impact |
|----------|-----------|--------|
| Knowledge gap | Uses term not defined in chapter | Confusion |
| Skill gap | Assumes action not taught | Failure |
| Conceptual gap | References framework not introduced | Misunderstanding |
| Tool gap | Uses command not explained | Blocked |

## Pedagogical Layer Assessment

### Layer Characteristics

#### Layer 1: Foundation (Manual-First)

**Expected**:
- Concept explanation before AI usage
- Manual process taught first
- Understanding "why" before "how"
- No AI shortcuts for learning

**Red Flags**:
- "Just ask AI to do it"
- Automation before understanding
- AI generates without learner comprehension

#### Layer 2: Collaboration (AI Partnership)

**Expected**:
- Three Roles pattern (invisible)
  - AI teaches student (suggests what student doesn't know)
  - Student teaches AI (corrects/refines output)
  - Convergence (iterate toward better solution)
- Learning through AI interaction
- Reflective prompts

**Red Flags**:
- Passive AI usage (copy-paste only)
- No iteration/refinement
- AI as oracle not collaborator
- Exposed framework labels ("AI as Teacher")

#### Layer 3: Intelligence (Pattern Recognition)

**Expected**:
- Recognizing repeated patterns
- Creating reusable components (skills, subagents)
- Encoding expertise for automation
- Meta-learning about AI capabilities

**Red Flags**:
- Creating skills without understanding them
- Automation without prior manual experience
- No reflection on what was automated

#### Layer 4: Orchestration (Capstone)

**Expected**:
- Combining multiple components
- Spec-driven development
- System-level thinking
- Real-world project completion

**Red Flags**:
- Isolated exercises (not integrated)
- No connection to earlier lessons
- Theoretical without hands-on
- Missing specifications

### Layer Progression Check

Typical chapter progression:
- L01-L02: Layer 1 (Foundation)
- L03-L05: Layer 2 (Collaboration)
- L06-L08: Layer 3 (Intelligence)
- L09+: Layer 4 (Orchestration/Capstone)

## Try With AI Effectiveness

### Prompt Quality Criteria

| Criteria | Good | Bad |
|----------|------|-----|
| Specificity | "Extend the internal-comms skill to handle..." | "Help me with skills" |
| Connection | References lesson content directly | Generic prompt |
| Learning target | States what student practices | Just gets answer |
| Progressive | Builds on previous prompt | Disconnected |
| Explanation | Includes "What you're learning" | Prompt only |

### Prompt Quantity Guidelines

| Lesson Type | Recommended | Too Few | Too Many |
|-------------|-------------|---------|----------|
| Conceptual | 2 | 1 | 4+ |
| Hands-on | 2-3 | 1 | 5+ |
| Capstone | 2-3 | 1 | 4+ |

### Effective Prompt Patterns

**Extension Pattern**: "Take what you built and add..."
**Debug Pattern**: "Something's wrong with X, diagnose..."
**Variation Pattern**: "Create a similar skill for..."
**Explanation Pattern**: "Explain why X worked/didn't work..."
**Application Pattern**: "Apply this to your own domain..."

## Assessment/Verification Quality

### Verification Types

| Type | Example | When to Use |
|------|---------|-------------|
| Command output | "You should see: `v1.2.3`" | After terminal commands |
| Visual confirmation | "The green checkmark appears" | GUI operations |
| File check | "Verify file exists with `ls`" | File creation |
| Behavior test | "Try X and confirm Y happens" | Feature verification |
| Self-assessment | "Can you explain why this works?" | Conceptual understanding |

### Verification Coverage

Aim for verification after:
- Every installation command
- Every file creation
- Every configuration change
- Every hands-on exercise
- Each major section (checkpoint)

### Missing Verification Indicators

- Commands without expected output
- "You're done!" without confirmation criteria
- Multi-step process with no intermediate checks
- Exercises with no success criteria
- "It should work" without how to verify
