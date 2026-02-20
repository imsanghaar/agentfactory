---
description: |
  Structured spec-vs-implementation review with single-pass file reading.
  Use when reviewing code against specifications, analyzing compliance, or auditing implementations.
allowed-tools: Read, Grep, Glob
---

# Spec Review Skill

Review specifications against implementations with disciplined file access.

## Protocol

### Phase 1: Spec Mapping (5 min)
1. Read the spec file(s) ONCE
2. Extract all requirements as a checklist:
   ```
   REQUIREMENTS FROM SPEC:
   [ ] REQ-1: [requirement text]
   [ ] REQ-2: [requirement text]
   ...
   ```

### Phase 2: Implementation Discovery
1. `ls` or `glob` to identify all implementation files
2. List files to review:
   ```
   FILES TO REVIEW:
   - path/to/file1.py
   - path/to/file2.ts
   ...
   ```

### Phase 3: Single-Pass Review
For EACH file (read ONCE):
```
FILE: [path]
PURPOSE: [what this file does]
REQUIREMENTS ADDRESSED:
- REQ-1: [how it's implemented / NOT FOUND]
- REQ-3: [how it's implemented / NOT FOUND]
ISSUES FOUND:
- [issue at line X]
```

**CRITICAL: Never re-read a file. Your notes must be sufficient.**

### Phase 4: Compliance Matrix
```
| Requirement | Status | Implementation Location | Notes |
|-------------|--------|-------------------------|-------|
| REQ-1       | ✅/❌  | file.py:42             | ...   |
| REQ-2       | ✅/❌  | file.ts:87             | ...   |
```

### Phase 5: Recommendations
```
GAPS FOUND:
1. [Missing requirement with priority]

RECOMMENDATIONS:
1. [Actionable fix]

FILES REVIEWED: [count unique files]
FILES RE-READ: 0 (if >0, explain why)
```

## Output Format

Always produce:
1. Requirements checklist
2. Per-file notes (single read)
3. Compliance matrix
4. Prioritized recommendations

## Anti-Patterns to Avoid

- ❌ "Let me check that file again..."
- ❌ Reading the same file from different perspectives
- ❌ Re-reading to "confirm" something
- ✅ Taking thorough notes on first read
- ✅ Referencing notes for analysis
