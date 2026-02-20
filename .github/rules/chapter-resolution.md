# Chapter/Part Resolution Protocol

**Problem**: "Chapter 5" and "Part 5" are different things. Ambiguous references cause wrong paths.

| User Says              | Interpretation                | Example                    |
| ---------------------- | ----------------------------- | -------------------------- |
| `ch 11` / `chapter 11` | Chapter 11 (single chapter)   | AI-Native IDEs (in Part 3) |
| `part 4` / `p4`        | Part 4 (all chapters in part) | Coding for Problem Solving |
| `5` (bare number)      | **AMBIGUOUS**                 | Must ask user to clarify   |

## Authoritative Source: The Filesystem

**The filesystem at `apps/learn-app/docs/` is the source of truth. No hardcoded index file exists — always discover via `ls`.**

```
apps/learn-app/docs/
├── 01-General-Agents-Foundations/             ← Part 1
│   ├── 01-agent-factory-paradigm/            ← Chapter 1
│   ├── 02-general-agents/                    ← Chapter 2
│   └── 03-seven-principles/                  ← Chapter 3
├── 02-Applied-General-Agent-Workflows/        ← Part 2
│   ├── 06-build-your-first-personal-ai-employee/
│   └── ...
├── 03-SDD-RI-Fundamentals/                   ← Part 3
│   ├── 11-ai-native-ides/                    ← Chapter 11
│   └── ...
└── ...
```

**Structure**: Parts are top-level folders (`NN-*`), chapters are inside them (`NN-*/`).

## Resolution Procedure

**BEFORE any chapter/part work, run these bash commands:**

```bash
# Step 1: Parse input and discover path

# For "ch 11" / "chapter 11" → Find chapter folder:
ls -d apps/learn-app/docs/*/11-*/
# Returns: apps/learn-app/docs/03-SDD-RI-Fundamentals/11-ai-native-ides/

# For "part 4" / "p4" → Find part folder:
ls -d apps/learn-app/docs/04-*/
# Returns: apps/learn-app/docs/04-Coding-for-Problem-Solving/

# For bare "5" → AMBIGUOUS, ask user first!
```

```bash
# Step 2: Validate and count contents

# Count lessons in a chapter:
ls apps/learn-app/docs/03-SDD-RI-Fundamentals/11-ai-native-ides/*.md | wc -l

# Count chapters in a part:
ls -d apps/learn-app/docs/04-Coding-for-Problem-Solving/*/ | wc -l
```

```bash
# Step 3: Confirm with user before proceeding
```

**Example confirmation**:

```
"You said 'ch 11'. I found:
- Chapter 11: ai-native-ides
- Path: apps/learn-app/docs/03-SDD-RI-Fundamentals/11-ai-native-ides/
- Part: 03-SDD-RI-Fundamentals
- Lessons: 17 files

Is this correct?"
```

## Key Rule: Chapter Numbers Are Global

Chapter numbers are **global across the book**, not local to parts.

- `ch 11` → Chapter 11 (lives in Part 3, folder `11-*`)
- `part 4` → Part 4 (folder `04-Coding-for-Problem-Solving/`)

**`ch 4` ≠ `part 4`** — completely different locations!

## Failure Modes

- ❌ **Guessing paths without running `ls`** (Always discover via filesystem)
- ❌ **Not asking for clarification on bare numbers** ("5" is ambiguous)
- ❌ **Trusting stale documentation over filesystem** (Filesystem is source of truth)
- ❌ **Referencing hardcoded index files** (No chapter-index.md exists — use `ls -d` only)

**Always run `ls -d` to discover paths. Never guess. Never reference a hardcoded file.**
