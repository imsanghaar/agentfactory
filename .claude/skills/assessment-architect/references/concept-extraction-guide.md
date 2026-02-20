# Concept Extraction Guide

How to extract testable concepts from lesson content. Used in Phase 1 to build the concept map.

---

## What Is a Concept (vs a Fact)

| Category | Example | Testable? | Why |
|----------|---------|-----------|-----|
| **Concept** | "Event-driven architecture decouples producers from consumers" | Yes | Understanding, can transfer |
| **Fact** | "MCP was released in November 2024" | No | Memorization, not understanding |
| **Principle** | "Smaller, focused services are easier to deploy independently" | Yes | Can apply to new situations |
| **Definition** | "A webhook is an HTTP callback" | No | Can be looked up |
| **Trade-off** | "Microservices add network complexity but enable team autonomy" | Yes | Requires judgment |
| **Relationship** | "CI creates demand for CD" | Yes | Tests structural understanding |

**Rule:** If testing it requires only recall, it's a fact. If testing it requires applying, analyzing, or evaluating, it's a concept.

---

## Extraction Procedure

For each lesson, read the content and extract:

### 1. Core Concepts

Named ideas, patterns, or principles that the lesson teaches.

**How to identify:**
- What would you explain if someone asked "what did you learn?"
- What ideas could apply to a different domain?
- What patterns keep recurring across lessons?

**Format:**
```
Concept: {Name}
Definition: {1-2 sentences explaining the idea}
Lessons: {L03, L07} (which lessons cover this)
```

### 2. Relationships

How concepts connect to each other.

**Relationship types:**
- `enables`: Concept A makes Concept B possible or easier
- `conflicts-with`: Concept A and B cannot both be maximized
- `extends`: Concept B builds on Concept A
- `requires`: Concept B cannot work without Concept A
- `alternative-to`: Concept A and B solve the same problem differently

**Format:**
```
{Concept A} --{relationship}--> {Concept B}
Explanation: {Why this relationship exists}
```

### 3. Trade-offs

Decisions where choosing one option sacrifices something else.

**How to identify:**
- "You can have X or Y, but not both"
- "The advantage of X comes at the cost of Y"
- "Teams choose X when they value Y over Z"

**Format:**
```
Trade-off: {Choosing X} vs {Choosing Y}
What you gain: {benefit of X}
What you sacrifice: {benefit of Y}
When to choose X: {context where X wins}
When to choose Y: {context where Y wins}
```

### 4. Transfer Domains

Domains where the concept could apply but that are NOT mentioned in the chapter.

**How to identify:**
- What is the STRUCTURAL principle? (ignore the specific technology)
- Where else does this structure appear?
- What other industries face the same pattern?

**Example:**
```
Concept: Event-driven architecture (publish/subscribe)
Structural principle: "Producers emit signals without knowing who consumes them"
Transfer domains:
- Emergency dispatch (units broadcast status)
- News publishing (reporters file stories, editors subscribe)
- Supply chain (sensors emit readings, systems react)
- Ecology (predator-prey signaling)
```

**Rule:** Transfer domains must NOT appear in the chapter. If the chapter mentions healthcare, don't use healthcare as a transfer domain.

---

## What NOT to Extract

These are facts, not concepts. Do not include them in the concept map:

- Specific version numbers ("Python 3.12")
- Release dates ("launched March 2024")
- Company names unless they represent a concept ("Netflix's chaos engineering")
- Statistics ("used by 60,000 developers")
- Tool names without the underlying principle
- Syntax examples without the pattern they demonstrate
- Historical timeline events

---

## Concept Map Output Format

Write to `assessments/{SLUG}-concepts.md`:

```markdown
# Concept Map: {Chapter/Part Name}

Source: {path to chapter/part}
Lessons analyzed: {count}
Extraction date: {today}

## Concepts ({N} total)

### 1. {Concept Name}
- **Definition:** {1-2 sentences}
- **Lessons:** {L01, L05, L12}
- **Relationships:** enables {Concept X}, conflicts-with {Concept Y}
- **Transfer domains:** {domain1, domain2, domain3}
- **Trade-offs involved:** {if any}

### 2. {Concept Name}
...

## Relationships ({N} total)

| From | Relationship | To | Evidence |
|------|-------------|-----|----------|
| Concept A | enables | Concept B | {brief explanation} |
| Concept C | conflicts-with | Concept D | {brief explanation} |
...

## Trade-offs ({N} total)

| Choice A | Choice B | Gain A | Sacrifice A | Context |
|----------|----------|--------|-------------|---------|
| Microservices | Monolith | Team autonomy | Simplicity | Large teams |
...

## Transfer Domain Bank ({N} domains)

| Domain | Applicable Concepts | Not Used In Chapter |
|--------|--------------------|--------------------|
| Healthcare | Concepts 1, 5, 8 | Confirmed not in source |
| Agriculture | Concepts 3, 7 | Confirmed not in source |
...
```

---

## Quality Checks

After extraction, verify:

1. **Concept count:** Expect 1-3 concepts per lesson. A 15-lesson chapter should yield 20-45 concepts.
2. **No facts disguised as concepts:** If removal of a specific number/date makes the entry meaningless, it's a fact.
3. **Transfer domains are novel:** grep chapter content for each domain. If found, remove it.
4. **Relationships are directional:** A enables B is different from B enables A.
5. **Trade-offs have both sides:** If you can't articulate what you sacrifice, it's not a trade-off.
