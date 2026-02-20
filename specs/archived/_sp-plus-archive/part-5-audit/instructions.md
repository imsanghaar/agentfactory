# Part 5 Audit: Todo Running Example Integration

## Context

You are auditing Part 5 (Python Fundamentals, Chapters 15-32) to integrate the "One Running Example + Auxiliary Examples" framing established in Issue #406.

**Related Issues:**
- #406: Parent issue - Book Framing: One Running Example + Auxiliary Examples
- #407: Part 5 specification - Todo Console App incremental build
- #411: Audit guidelines with per-chapter template

## The Core Idea

**Running Example (Todo):** Students build a Todo console app incrementally across all lessons. Each Python concept directly contributes to the Todo app.

**Auxiliary Examples:** Each lesson also shows 2-3 domain examples (legal, finance, healthcare, marketing) demonstrating the same pattern applies universally.

**Why This Matters:** By Part 6, students build a TaskManager Agent. The Todo app from Part 5 provides the domain logic. Without consistent Todo framing in Part 5, Part 6 loses its foundation.

## Your Mission

Audit all 18 chapters (Ch 15-32) and categorize each lesson:

| Category | Description | Action |
|----------|-------------|--------|
| **A** | Already uses Todo-like examples | No changes needed |
| **B** | Minor reframe | Change variable names, add 1 sentence connecting to Todo |
| **C** | Add auxiliary examples | Has Todo but lacks domain examples |
| **D** | Add running example | Uses unrelated examples, needs Todo as primary |

## Audit Process

### Phase 1: Inventory (Do First)

For each chapter (15-32):
1. List all lessons in the chapter
2. Read each lesson's main examples
3. Categorize as A/B/C/D
4. Note specific changes needed

**Output Format:**
```markdown
### Chapter XX: [Title]

| Lesson | Current Example | Category | Changes Needed |
|--------|-----------------|----------|----------------|
| 01-xxx | Uses `items` list | B | Rename to `tasks` |
| 02-xxx | Uses Todo dict | A | None |
| 03-xxx | Generic calculator | D | Add Todo example |
```

### Phase 2: Change Specification

For each lesson needing changes, specify:

1. **What to change** (exact sections/code blocks)
2. **How to change** (specific edits)
3. **Auxiliary examples to add** (which domains)

**Example:**
```markdown
#### Lesson 17-02: Working with Dictionaries

**Current:** Uses `person = {"name": "Alice", "age": 30}`

**Change to:**
```python
# Running Example: Todo task as dictionary
task = {"title": "Review contract", "done": False, "priority": "high"}
```

**Add Auxiliary Examples:**
- Legal: `case = {"case_id": "2024-001", "status": "open", "client": "Acme Corp"}`
- Finance: `invoice = {"invoice_no": "INV-001", "amount": 1500.00, "paid": False}`
```

### Phase 3: Connection Points

Identify where lessons should reference previous Todo progress:

- Ch 17 (Data Types): "This task dict becomes the foundation for our Todo app"
- Ch 23 (Functions): "Now we wrap our task operations in reusable functions"
- Ch 27 (OOP): "Let's transform our dict-based tasks into a proper Task class"

## Todo Component Mapping

Use this as your guide for what each chapter contributes:

| Chapter | Concept | Todo Component |
|---------|---------|----------------|
| Ch 15 | UV/Setup | Project structure for Todo app |
| Ch 16 | Intro | Print task titles, hello world → "Todo: Review contract" |
| Ch 17 | Data Types | Task as dict `{"title": "...", "done": False}` |
| Ch 18 | Operators | Task ID generation, boolean done toggle |
| Ch 19 | Strings | Task title formatting, search/filter |
| Ch 20 | Control Flow | Menu loop, if/else for commands |
| Ch 21 | Lists/Dicts | Task storage in list, lookup by ID |
| Ch 22 | Sets | Tags/categories for tasks |
| Ch 23 | Functions | `add_task()`, `complete_task()`, `list_tasks()` |
| Ch 24 | Exceptions | Handle invalid input, missing tasks |
| Ch 25 | File I/O | Save/load tasks from JSON file |
| Ch 26 | Datetime | Due dates, reminders, overdue detection |
| Ch 27-28 | OOP | `Task` class, `TaskManager` class |
| Ch 29 | Dataclasses | `@dataclass` Task with auto-generated methods |
| Ch 30 | Pydantic | Validated Task model with constraints |
| Ch 31 | Asyncio | Async task operations (prep for Part 6) |
| Ch 32 | CPython/GIL | Performance understanding for batch ops |

## Auxiliary Domain Examples

Use these consistently across lessons:

| Domain | Entity | Example Operations |
|--------|--------|-------------------|
| **Legal** | Case/Contract | `add_case()`, case status, filing deadlines |
| **Finance** | Invoice/Transaction | `create_invoice()`, payment status, amounts |
| **Healthcare** | Appointment/Patient | `schedule_appointment()`, visit notes |
| **Marketing** | Campaign/Lead | `create_campaign()`, lead scoring |

## Quality Standards

### Do NOT:
- Rewrite entire lessons (too disruptive)
- Change Python explanations (they're correct)
- Remove good existing examples entirely
- Add marketing language or promises

### DO:
- Add Todo as primary example where missing
- Keep existing examples as auxiliary
- Add brief connecting sentences
- Maintain consistent naming (`task`, `tasks`, `TaskManager`)

## Output Deliverables

Create a single audit report with:

1. **Executive Summary**
   - Total lessons audited
   - Breakdown by category (A/B/C/D)
   - Estimated effort (hours)

2. **Per-Chapter Breakdown**
   - Table of lessons with categories
   - Specific changes needed

3. **Cross-Cutting Issues**
   - Inconsistent naming to fix
   - Missing connection points
   - Opportunities for improvement

4. **Implementation Priority**
   - Phase 1: Quick wins (Category B - minor reframes)
   - Phase 2: Add auxiliary examples (Category C)
   - Phase 3: Add running examples (Category D)

## File Paths

All content is at:
```
/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/apps/learn-app/docs/05-Python-Fundamentals/
```

Chapters:
- `15-python-uv-package-manager/`
- `16-introduction-to-python/`
- `17-data-types/`
- `18-operators-keywords-variables/`
- `19-strings-type-casting/`
- `20-control-flow-loops/`
- `21-lists-tuples-dictionary/`
- `22-set-frozenset-gc/`
- `23-module-functions/`
- `24-exception-handling/`
- `25-io-file-handling/`
- `26-math-datetime-calendar/`
- `27-oop-part-1/`
- `28-oop-part-2/`
- `29-metaclasses-dataclasses/`
- `30-pydantic-generics/`
- `31-asyncio/`
- `32-cpython-gil/`

## Success Criteria

The audit is complete when:
- [ ] All 18 chapters inventoried
- [ ] All lessons categorized (A/B/C/D)
- [ ] Specific changes documented for B/C/D lessons
- [ ] Auxiliary examples specified for each lesson
- [ ] Connection points identified
- [ ] Implementation priority established
- [ ] Effort estimate provided

## Notes

- This is an AUDIT, not implementation
- Focus on documenting what changes are needed
- Implementation will follow in a separate phase
- Err on the side of minimal changes (Category A/B preferred over C/D)
