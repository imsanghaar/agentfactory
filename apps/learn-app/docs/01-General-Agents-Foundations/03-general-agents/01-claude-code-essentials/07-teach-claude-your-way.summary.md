# Lesson 7 Summary: Teach Claude Your Way of Working

## Key Concepts

### 1. AI Models Are Non-Deterministic

**Non-deterministic** means "not guaranteed to give the same result." The same input can produce different outputs each time.

```
> Write a LinkedIn post about learning AI development.
```

Run this twice. You'll get different results—different structure, tone, length. Not wrong, just different.

This is fundamental to how AI models work, not a bug.

### 2. The Double Variability Problem

Two sources of drift make outputs unpredictable:

| Source | What Happens |
|--------|--------------|
| **You** | Phrase requests differently each time |
| **AI model** | Generates differently even for identical requests |

For casual conversation, this is fine. For consistent professional output? It's a problem.

### 3. Two Problems, Two Solutions

| Problem | Impact | Solution |
|---------|--------|----------|
| Session memory loss (Lesson 5) | Claude forgets your project | `CLAUDE.md` |
| Output variability (this lesson) | Results drift from non-determinism | **Skills** |

`CLAUDE.md` = project context. Skills = personal style.

### 4. Skills Constrain Non-Determinism

A skill is a folder with a `SKILL.md` file containing your instructions—tone, structure, preferences—so Claude creates output within YOUR boundaries.

Claude's output still varies (non-determinism doesn't disappear), but it stays within your defined constraints. Every LinkedIn post has your tone, your emoji style, your engagement hooks.

### 5. Skills ≠ Saved Prompts

| Concept | What It Encodes |
|---------|-----------------|
| **Prompts** | WHAT you want ("Write a blog post") |
| **Skills** | HOW you think about a task (structure, preferences, quality criteria) |

Prompts get you *a* result. Skills get you *your* result.

### 6. Two Activation Modes

| Method | How It Works | When to Use |
|--------|--------------|-------------|
| **Automatic** | Claude recognizes when your style applies | Normal workflow—just ask naturally |
| **Explicit** | You say "Use [skill-name]..." | When you want a specific skill for sure |

Both work! Start with explicit invocation to see skills in action clearly.

---

## Mental Models

### The Constraint Model
Non-determinism = infinite possible outputs. Your skill = boundaries that keep outputs within YOUR style. The AI still varies, but only within your constraints.

### The Personal Assistant Model
- **Generic assistant**: Helps with anything, uses default approach
- **Personal assistant who knows you**: Applies YOUR preferences automatically

Skills transform Claude from generic to personal.

### The Procedure Test
If you've explained the same thing to Claude more than twice, and it's stable enough to document, it's a skill candidate.

---

## Hands-On: Skills Lab

1. Go to [github.com/imsanghaar/claude-code-skills-lab](https://github.com/imsanghaar/claude-code-skills-lab)
2. Click green **Code** button → **Download ZIP**
3. Extract and open folder in terminal
4. Run `claude`

**Test non-determinism (without skill):**
```
> Write a LinkedIn post about learning how to build software with AI Agents.
```
Run twice, compare outputs.

**Test with skill constraint:**
```
> Use internal-comms and write a LinkedIn post about learning how to build software with AI Agents.
```

**Notice**: The skill-enhanced output stays within defined boundaries—personality, strategic emojis, engagement question.

### Skills Available Now (no Python needed)
- `internal-comms` — Status reports, newsletters, LinkedIn posts
- `brand-guidelines` — Apply brand colors and typography

### Skills After Python (Chapter 16)
- `docx`, `pdf`, `pptx`, `xlsx` — Document creation and manipulation

---

## Real Example: Study Notes Assistant

A skill that transforms messy lecture notes into structured study materials:

1. Ask for lecture topic
2. Request text content (typed notes, slide text, transcript)
3. Extract key concepts and definitions
4. Create summary with main points
5. Generate practice questions
6. Create quick review section
7. Save as organized markdown file

**The payoff**: Consistent structure every time, despite non-determinism.

---

## Common Mistakes to Avoid

1. **Thinking non-determinism is a bug** — It's fundamental to AI models; skills constrain it, not eliminate it
2. **Confusing skills with saved prompts** — Skills encode reasoning patterns, not just text to paste
3. **Only considering coding tasks** — Skills work for any repeated procedure
4. **Overcomplicating** — "LinkedIn posts: friendly tone, 2-3 emojis, end with question" is enough

---

## Preparation for Next Lesson

Identify one procedure you want to encode:

1. **When do I do this?** (trigger)
2. **How do I like it?** (your style)
3. **What makes it 'me'?** (distinctive elements)
4. **What should others know?** (pro tips)

Document your answers. This becomes raw material for your first skill.

---

## Quick Reference

**Non-deterministic**: Same input → different output each time (fundamental to AI models)

**Skill**: Your personal style guide that constrains Claude's output to YOUR boundaries

**Key insight**: `CLAUDE.md` = project context. Skills = personal style.

**Two activation modes**: Automatic (Claude decides) or Explicit (you name it)

**Start now**: `internal-comms`, `brand-guidelines` (no Python needed)

**Add later**: `docx`, `pdf`, `pptx`, `xlsx` (after Chapter 16)
