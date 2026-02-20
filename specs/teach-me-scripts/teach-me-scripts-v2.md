# Teach Me Scripts v2 - Complete Specification

> **Purpose**: Define input/output contracts for Teach Me agent behavior
> **Created**: 2024-02-13
> **Status**: Ready for implementation

---

## GLOBAL RULES

```
CONTEXT MANAGEMENT:
- Only use CURRENT chunk content for responses
- Ignore conversation history for topic context
- Thread history is ONLY for tracking Q&A flow, not content

MAX ATTEMPTS:
- Maximum 3 attempts per chunk
- After 3 wrong answers → reveal answer and move on

HISTORY TRUNCATION:
- LLM should focus on current chunk_title only
- Previous chunk topics are IRRELEVANT

CHUNK QUALITY GATE:
- Minimum 100 chars of meaningful content required
- If chunk is header/transition only → auto-skip to next

MANDATORY MARKER:
- Every question MUST end with <!--CORRECT:A--> or <!--CORRECT:B-->
- If marker is missing, system will break
```

---

## Script 1: START_TEACHING

```
TRIGGER: is_first_message=true

INPUT:
- chunk_content: string (lesson section)
- chunk_title: string
- chunk_index: number
- total_chunks: number
- user_name: string (optional)

QUALITY GATE:
IF chunk_content < 100 chars OR is_header_only(chunk):
  → Skip to next chunk with: "Let's start with {next_chunk_title}..."

OUTPUT FORMAT:
1. Greeting (if user_name): "Hi {user_name}!"
2. Topic intro: "Today we'll explore {chunk_title}."
3. Explanation: 2-3 sentences summarizing KEY concept
4. Question: Tests understanding (not recognition)
5. Options: A) and B) - both plausible
6. Prompt: "Type A or B to answer"
7. Hidden: <!--CORRECT:X-->

QUESTION CRITERIA:
✅ Asks "why", "how", or "what enables/causes"
✅ Wrong option = believable misconception
✅ Both options use similar language complexity
✅ Answer requires reading content (not guessable)

❌ FORBIDDEN:
- "Is X related or unrelated?"
- "Does X exist or not?"
- Options with "not", "never", "unrelated"
- Yes/No reformulations

EXAMPLE:
Good: "What role do agents play in AI employees?"
  A) Agents power AI employees as core execution components
  B) Agents handle only the user interface layer

Bad: "Are agents part of AI employees?"
  A) Yes, they are core components
  B) No, they are unrelated
```

---

## Script 2: CORRECT_ANSWER

```
TRIGGER: verification_result="correct"

INPUT:
- current_chunk: already advanced to next chunk
- chunk_index: current position
- total_chunks: total count

BRANCH A - More chunks remaining (chunk_index < total_chunks - 1):
OUTPUT FORMAT:
1. "Correct!" + brief praise (1 sentence max)
2. Transition: "Now let's learn about {chunk_title}:"
3. Explanation: 2-3 sentences on NEW concept
4. New question following Script 1 QUESTION CRITERIA
5. "Type A or B to answer"
6. <!--CORRECT:X-->

BRANCH B - Last chunk completed (chunk_index == total_chunks - 1):
OUTPUT FORMAT:
1. "Correct!"
2. "You've completed this lesson!"
3. Summary: 2-3 bullet points of key concepts learned
4. "Continue to the next lesson when ready."
5. NO question, NO marker

❌ FORBIDDEN:
- Re-explaining previous concept
- Asking about previous chunk topic
- More than 1 sentence of praise
```

---

## Script 3: INCORRECT_ANSWER

```
TRIGGER: verification_result="incorrect"

INPUT:
- chunk_content: SAME chunk (not advanced)
- chunk_title: current topic
- attempt_count: number of tries

BRANCH A - Attempts < 3:
OUTPUT FORMAT:
1. "Not quite."
2. Explain why wrong: Reference ONLY {chunk_title} topic
3. Simpler question:
   - Use more direct language
   - Make correct answer slightly more obvious
   - Still require understanding (not trivial)
4. New A/B options
5. "Type A or B to answer"
6. <!--CORRECT:X-->

SIMPLIFICATION RULES:
Attempt 1 → Original difficulty
Attempt 2 → Add context hint in question
Attempt 3 → Make question more direct

BRANCH B - Attempts >= 3:
OUTPUT FORMAT:
1. "Let's move on."
2. "The answer was {correct_option} because {brief explanation}."
3. Transition to next chunk (follow Script 2 BRANCH A)

CONTEXT RULE:
⚠️ CRITICAL: Your explanation must ONLY reference {chunk_title}.
   The conversation may contain other topics - IGNORE THEM.
   If you mention any topic other than {chunk_title}, you have FAILED.

❌ FORBIDDEN:
- Referencing topics from earlier chunks
- Saying "as we discussed earlier"
- Using examples from previous questions
```

---

## Script 4: OFF_TOPIC_RESPONSE (Complete)

```
TRIGGER: verification_result="unknown" OR normalize_answer=None

INPUT:
- user_message: string
- current_chunk: object
- has_pending_question: boolean

STEP 1 - EMPTY CHECK:
IF message.strip() == "":
  → "I didn't receive your answer. Please type A or B."
  → Repeat question
  → EXIT

STEP 2 - PARTIAL ANSWER EXTRACTION:
IF message contains standalone "A" or "B" (word boundary):
  → Extract first A/B match
  → Process as normal answer (Script 2 or 3)
  → EXIT

STEP 3 - LONG MESSAGE CHECK:
IF len(message) > 200:
  → "Thanks for sharing! For this exercise, just type A or B."
  → "Use 'Ask Me' for detailed discussions."
  → Repeat question
  → EXIT

STEP 4 - SPECIAL REQUESTS:
IF message contains ["hint", "help", "confused", "don't understand", "explain"]:
  → Go to Script 6 (HINT)
  → EXIT

IF message contains ["skip", "next", "move on", "pass"]:
  → Go to Script 7 (SKIP)
  → EXIT

IF message contains ["both wrong", "neither", "none of these"]:
  → Go to Script 6A (OPTION_CONFUSION)
  → EXIT

STEP 5 - DEFAULT OFF-TOPIC:
  → "Please answer with A or B."
  → "If you have other questions, use the 'Ask Me' option."
  → Repeat question
  → Same <!--CORRECT:X-->
```

---

## Script 5: QUESTION_QUALITY (Validation Criteria)

```
EVERY generated question MUST pass:

STRUCTURE CHECK:
□ Question ends with "?"
□ Two options labeled A) and B)
□ Ends with "Type A or B to answer"
□ Contains <!--CORRECT:A--> or <!--CORRECT:B-->

PLAUSIBILITY CHECK:
□ Both options are grammatically similar length (±20%)
□ Both options use domain vocabulary
□ Neither option contains negative qualifiers ("not", "never", "unrelated")
□ A random guesser would have ~50% chance

UNDERSTANDING CHECK:
□ Question contains "why", "how", "what enables", "what role", or "which"
□ Correct answer requires specific knowledge from chunk
□ Wrong answer represents common misconception OR adjacent concept

ANTI-PATTERN CHECK:
□ NOT a yes/no question rephrased
□ NOT asking if something "exists" or "is part of"
□ NOT using "all of the above" / "none of the above"
□ Options are NOT opposites (X vs not-X)

SCORING (internal validation):
- Passes all checks: ✅ Use question
- Fails 1+ checks: 🔄 Regenerate with stricter prompt
```

---

## Script 6: HINT_REQUEST

```
TRIGGER: message contains "hint", "help", "confused", "don't understand"

OUTPUT FORMAT:
1. "Here's a hint:"
2. Provide contextual clue WITHOUT revealing answer
3. Rephrase the concept differently
4. "Now try again - A or B?"
5. Same <!--CORRECT:X--> as before

HINT RULES:
✅ Relate hint to chunk_title topic only
✅ Use different words than original explanation
✅ Point toward correct answer indirectly
❌ Don't say "The answer is A/B"
❌ Don't eliminate one option explicitly
```

---

## Script 6A: OPTION_CONFUSION

```
TRIGGER: message contains "both wrong", "neither", "none of these", "don't agree"

OUTPUT:
1. "I understand the options might seem tricky."
2. "Here's a hint: {contextual clue from chunk}"
3. "One of these options does match the lesson content."
4. "Try again - A or B?"
5. Same <!--CORRECT:X-->

RULES:
✅ Validate question quality (maybe question IS bad)
✅ Provide helpful hint
❌ Don't admit options are wrong
❌ Don't generate new question
```

---

## Script 7: SKIP_REQUEST

```
TRIGGER: message contains "skip", "next", "move on", "pass"

OUTPUT FORMAT:
1. "No problem, let's move forward."
2. "The answer was {correct_option}: {brief explanation}"
3. Advance to next chunk
4. Continue with Script 2 BRANCH A (or B if last chunk)

RULES:
✅ Always reveal correct answer when skipping
✅ Count as completed (don't revisit)
✅ No judgment or negative feedback
```

---

## Script 8: LESSON_COMPLETE

```
TRIGGER: All chunks completed (chunk_index >= total_chunks)

OUTPUT FORMAT:
1. "Congratulations, {user_name}!"
2. "You've completed: {lesson_title}"
3. "Key takeaways:"
   - Bullet 1: Main concept
   - Bullet 2: Supporting concept
   - Bullet 3: Practical application
4. "Ready for the next lesson? Check the sidebar to continue."

RULES:
✅ Summarize from ALL chunks taught
✅ Keep bullets concise (1 line each)
❌ No new questions
❌ No <!--CORRECT:X--> marker
```

---

## Script 9: SESSION_RESUME

```
TRIGGER: User returns to lesson with existing session_state

BACKEND CHECK:
IF session_state exists for (user, lesson):
  → Resume from last chunk_index
  → Use status: "teaching" (not "awaiting_answer")
  → Generate fresh question for current chunk

OUTPUT:
1. "Welcome back! Let's continue where you left off."
2. "We were learning about {chunk_title}..."
3. Fresh question (don't assume they remember old one)
4. Standard A/B format with <!--CORRECT:X-->
```

---

## Script 10: COMPLETED_LESSON_RETURN

```
TRIGGER: User clicks "Teach Me" on already-completed lesson

BACKEND CHECK:
IF all chunks completed for (user, lesson):

OPTION A - Allow Re-learn:
  → Reset progress
  → Start from chunk 0
  → "Let's review this lesson again!"
  → Continue with Script 1

OPTION B - Show Summary Only (Default):
  → Don't reset
  → Show completion summary
  → "You've already completed this lesson. Here's a recap:"
  → Show Script 8 output
```

---

## Backend Validation Rules

### Marker Validation (chatkit_server.py)
```python
# After receiving LLM response:
IF response has question format BUT no <!--CORRECT:X--> marker:
  → Log warning
  → Append <!--CORRECT:A--> as default
  → Flag for review

IF multiple markers found:
  → Use FIRST marker only
  → Log warning

IF marker is not A or B:
  → Default to A
  → Log error
```

### Answer Parsing Enhancement (answer_verification.py)
```python
# Enhanced normalize_answer():
def normalize_answer(text: str) -> str | None:
    clean = text.strip().upper()

    # Exact match
    if clean in ("A", "B", "A)", "B)"):
        return clean[0]

    # Word boundary match for partial answers
    # "I think A because..." → "A"
    import re
    match = re.search(r'\b([AB])\b', clean)
    if match:
        return match.group(1)

    # Option patterns
    if re.match(r'^OPTION\s*([AB])$', clean):
        return match.group(1)

    # Ordinal patterns
    if re.match(r'^(1ST|FIRST)\s*(OPTION|ONE)?$', clean):
        return "A"
    if re.match(r'^(2ND|SECOND)\s*(OPTION|ONE)?$', clean):
        return "B"

    return None
```

---

## State Machine

```
┌─────────────────────────────────────────────────────────────┐
│                      TEACH ME FLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  START ──► Script 1 (START_TEACHING)                        │
│                │                                            │
│                ▼                                            │
│  ┌─────── AWAITING_ANSWER ◄──────────────────────┐         │
│  │             │                                  │         │
│  │    ┌────────┼────────┬──────────┬─────────┐   │         │
│  │    ▼        ▼        ▼          ▼         ▼   │         │
│  │  "A/B"   off-topic  "hint"    "skip"   empty  │         │
│  │    │        │        │          │         │   │         │
│  │    ▼        ▼        ▼          ▼         ▼   │         │
│  │ VERIFY   Script 4  Script 6  Script 7  Script4│         │
│  │    │        │        │          │         │   │         │
│  │ ┌──┴──┐     │        │          │         │   │         │
│  │ ▼     ▼     │        │          ▼         │   │         │
│  │ ✓     ✗     │        │     NEXT_CHUNK     │   │         │
│  │ │     │     │        │          │         │   │         │
│  │ ▼     ▼     └────────┴──────────┤         │   │         │
│  │ S2    S3 ◄──────────────────────┘         │   │         │
│  │ │     │                                   │   │         │
│  │ │  attempts<3? ──yes──► same chunk ───────┴───┘         │
│  │ │     │                                                 │
│  │ │     no                                                │
│  │ │     ▼                                                 │
│  │ └──► NEXT_CHUNK                                         │
│  │         │                                               │
│  │    more chunks? ──yes──► Script 2A ───────────┐        │
│  │         │                      │              │        │
│  │         no                     └──────────────┘        │
│  │         ▼                                               │
│  │    Script 8 (COMPLETE)                                  │
│  │         │                                               │
│  │         ▼                                               │
│  └────── END                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Coverage Summary

| Category | Scenarios | Status |
|----------|-----------|--------|
| **Happy Path** | Start, Correct, Complete | ✅ |
| **Wrong Answers** | Incorrect 1/2/3, Move on | ✅ |
| **User Input Variations** | a/b, A/B, option A, first | ✅ |
| **Off-Topic** | Random text, questions, long | ✅ |
| **Help Requests** | Hint, confused, skip | ✅ |
| **Edge Cases** | Empty, partial answer, both wrong | ✅ |
| **LLM Failures** | Missing marker, bad marker | ✅ |
| **Session** | Resume, completed return | ✅ |
| **Content Types** | Short chunk, code, tables | ✅ |

---

## Implementation Checklist

- [ ] Update `triage.py` - Convert scripts to prompt templates
- [ ] Update `chatkit_server.py` - Add marker validation, session handling
- [ ] Update `answer_verification.py` - Enhanced parsing with word boundaries
- [ ] Update `session_state.py` - Add attempt tracking, completion detection
- [ ] Add tests for each script scenario
- [ ] Manual testing with edge cases
