# Student Perspective Evaluation Rubric

Detailed criteria for evaluating educational content from a beginner student's perspective.

## Engagement Assessment

### Hook Quality Checklist

- [ ] First paragraph contains a relatable problem or scenario
- [ ] Reader can see themselves in the opening
- [ ] "Why should I care?" answered in first 100 words
- [ ] No jargon in opening paragraph
- [ ] Creates curiosity or tension to resolve

### Engagement Red Flags

| Red Flag | Example | Impact |
|----------|---------|--------|
| Abstract opening | "In this lesson, we will learn about X" | Immediate disengagement |
| Definition-first | "X is defined as..." | Feels like dictionary, not teaching |
| No stakes | Technical explanation without "why it matters" | Low motivation |
| Wall of text | 300+ words without visual break | Cognitive fatigue |
| Passive voice throughout | "It should be noted that..." | Boring, bureaucratic |

### Engagement Enhancers

| Enhancer | Example | Effect |
|----------|---------|--------|
| Problem-first hook | "You're debugging at 2am. The error makes no sense..." | Immediate relevance |
| Concrete scenario | "Imagine you're building a todo app..." | Mental anchor |
| Before/after contrast | "Without X, you spend 3 hours. With X, 10 minutes." | Clear value |
| Question hook | "What if your AI could remember your preferences?" | Creates curiosity |
| Story snippet | "Last week, a developer at Stripe discovered..." | Human interest |

## Length Assessment Details

### Word Count by Lesson Type

| Type | Minimum | Ideal | Maximum | Signs of Problems |
|------|---------|-------|---------|-------------------|
| Conceptual intro | 900 | 1,200 | 1,400 | Under 900 = thin; Over 1,400 = verbose |
| Hands-on practical | 1,100 | 1,400 | 1,600 | Under 1,100 = incomplete steps; Over 1,600 = over-explained |
| Installation/setup | 600 | 900 | 1,200 | Under 600 = missing troubleshooting; Over 1,200 = decision paralysis |
| Capstone | 1,300 | 1,600 | 1,800 | Under 1,300 = rushed; Over 1,800 = scope creep |
| Theory deep-dive | 1,200 | 1,500 | 1,800 | Under 1,200 = superficial; Over 1,800 = academic |

### "Too Short" Indicators

- Concept mentioned but not explained
- Single example where 2-3 needed
- No "what if X goes wrong?" coverage
- Abrupt ending ("That's it!")
- Missing "Why This Matters" context
- No troubleshooting for hands-on steps

### "Too Long" Indicators

- Same concept explained 2+ different ways
- Excessive analogies (more than 1 per concept)
- Try With AI has 4+ prompts
- Tables that could be sentences
- "Furthermore" and "Additionally" padding
- Tangential "interesting facts"

## Clarity Assessment Details

### Clarity Checklist

- [ ] Every new term defined before first use
- [ ] Paragraphs under 100 words
- [ ] Transitions between sections explicit
- [ ] Code examples have explanatory comments
- [ ] Complex concepts have diagrams/tables
- [ ] Assumptions stated explicitly

### Jargon Management

| Approach | When to Use | Example |
|----------|-------------|---------|
| Define inline | First occurrence | "Skills (reusable instruction sets) encode..." |
| Glossary link | Reference term | "See Glossary: MCP" |
| Avoid entirely | Unnecessary jargon | "Use" not "leverage" |
| Table of terms | Many related terms | Quick reference at section start |

### Clarity Killers

| Problem | Example | Fix |
|---------|---------|-----|
| Assumed knowledge | "As you know, JWT tokens..." | "JWT tokens (used for authentication)..." |
| Passive voice | "The file is read by Claude" | "Claude reads the file" |
| Nested conditions | "If X, then if Y, unless Z..." | Break into separate cases |
| Abstract nouns | "The implementation of the functionality" | "How it works" |
| Acronym soup | "Use the MCP SDK to configure the CLI" | Expand on first use |

## Hands-On Effectiveness Details

### Step Quality Checklist

- [ ] Each step has clear action verb ("Run", "Create", "Open")
- [ ] Expected result stated after each command
- [ ] Error states acknowledged with solutions
- [ ] Screenshots for GUI steps
- [ ] Copy-pasteable code blocks
- [ ] Checkpoint after multi-step sequences

### Step Writing Formula

```
[Action] + [What] + [Where/How]

"Run `npm install` in your project root."
"Create a file named `SKILL.md` in `.claude/skills/my-skill/`."
"Click the green 'Code' button, then select 'Download ZIP'."
```

### Missing Step Indicators

- "And then..." without specifying what
- Result shown but not how to get there
- Assumed file locations
- Missing error recovery paths
- No verification of success

## Progression Assessment Details

### Connection Patterns

| Pattern | Example | Effectiveness |
|---------|---------|---------------|
| Explicit backward | "In Lesson 3, you installed Claude Code. Now..." | High |
| Skill building | "You created a skill. Now learn to share it." | High |
| Implicit | "Skills are important. MCP is also important." | Low |
| None | New topic with no reference to prior | Very low |

### Running Example Continuity

**Strong**: Same project/example evolves through chapter
- L01: Create `internal-comms` skill
- L02: Test `internal-comms` in different scenarios
- L03: Enhance `internal-comms` with MCP
- L04: Share `internal-comms` with team

**Weak**: Different disconnected examples
- L01: LinkedIn posting skill
- L02: Code review skill
- L03: Meeting notes skill
- L04: Generic skill

### Progression Red Flags

- Lesson references concept not yet taught
- Difficulty doesn't increase
- No callback to earlier lessons
- "We'll cover this later" with no follow-through

## Confidence Assessment Details

### Confidence Building Elements

| Element | Description | Impact |
|---------|-------------|--------|
| Verification checkpoints | "You should see X" | High |
| Practice before theory | Do, then understand | High |
| Incremental complexity | Build up gradually | Medium |
| Error recovery shown | "If you see error Y, do Z" | High |
| Real-world applicability | "You'd use this when..." | Medium |

### Confidence Destroyers

| Problem | Effect | Fix |
|---------|--------|-----|
| No verification | "Did I do it right?" anxiety | Add expected output |
| Too much too fast | Overwhelm | Chunk into smaller steps |
| Magic commands | "Why did that work?" confusion | Explain each part |
| No practice opportunity | "I haven't done this myself" | Add Try It Yourself |
| Only happy path | First error = stuck | Add troubleshooting |
