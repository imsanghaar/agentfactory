# Tasks: Chapter 6 - File Organization Workflow

**Input**: Design documents from `/specs/062-ch6-file-workflow/`
**Prerequisites**: plan.md, spec.md

**Tests**: No automated tests - educational content validated through subagent workflow

**Organization**: Tasks organized by lesson to enable independent implementation of each lesson

## Format: `[ID] [P?] [L#] Description`

- **[P]**: Can run in parallel (different lessons, no dependencies)
- **[L#]**: Which lesson this task belongs to (L01-L06)
- All paths are absolute from repository root

## Path Conventions

**Chapter Location**: `apps/learn-app/docs/02-Applied-General-Agent-Workflows/06-file-processing/`

**Quality Reference**: `apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/01-your-first-git-repository.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Chapter initialization and configuration

- [x] T001 Verify chapter directory exists at `apps/learn-app/docs/02-Applied-General-Agent-Workflows/06-file-processing/`
- [x] T002 Read quality reference lesson at `apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/01-your-first-git-repository.md` to understand workflow-first teaching standard
- [x] T003 [P] Read Seven Principles chapter at `seven_principles_chapter.md` to ensure principle alignment
- [x] T004 [P] Read spec.md (`specs/062-ch6-file-workflow/spec.md`) for user stories and success criteria
- [x] T005 [P] Read plan.md (`specs/062-ch6-file-workflow/plan.md`) for lesson-by-lesson breakdown

**Checkpoint**: Setup complete - ready to implement lessons with full context

---

## Phase 2: Lesson 1 - Survey Your Chaos (25 min) [L01]

**Goal**: Students execute bash commands to inventory file system, create baseline documentation

**Learning Objectives**:

- LO-L01-001: Execute `ls -la`, `find`, and `du` commands to inventory file system contents
- LO-L01-002: Interpret command output to identify file types, counts, and space consumption
- LO-L01-003: Create FILE-INVENTORY.md documenting current file system state

**Principle Applications**: P1 (Bash), P7 (Observability)

**Independent Test**: Can student run commands on their Downloads folder and produce accurate inventory?

### Implementation for Lesson 1

- [x] T006 [L01] Invoke `learning-objectives` skill to generate measurable outcomes for L01 (Bloom's: Apply, Analyze, Create; CEFR: A2)
- [x] T007 [L01] **SUBAGENT**: content-implementer
  - Output path: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\06-file-processing\01-survey-your-chaos.md`
  - Stage: Layer 1 (Manual Foundation) - students execute commands, observe results, understand patterns
  - Teaching Modality: Hands-on Discovery (vary from Chapter 5 direct teaching)
  - Cognitive Load: 4 concepts (file system visibility, file discovery, space analysis, workspace setup) - WITHIN A2 LIMIT
  - Bash commands to include:
    - `ls -la` for permissions, sizes, dates
    - `find . -type f | wc -l` for file count
    - `du -sh *` for space consumption
    - `find . -name "*.pdf" | wc -l` for type-based counting
    - `mkdir file-organizer` for workspace setup
  - Outputs: `file-organizer/` directory, `FILE-INVENTORY.md` with counts by type, space usage, largest files
  - Three "Try With AI" prompts (active collaboration format, no meta-commentary):
    1. File Discovery Patterns: "Show me commands to count different file types in my folder"
    2. Space Consumption Investigation: "Show me commands to identify largest files consuming space"
    3. Inventory Report Creation: "Help me design FILE-INVENTORY.md template with totals, breakdown by type, largest files"
  - Execute autonomously without confirmation
  - Include quality reference: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\10-version-control\01-your-first-git-repository.md`
  - Returns confirmation only (~50 lines), NOT full content
- [x] T008 [L01] **VALIDATION**: educational-validator reads `apps/learn-app/docs/02-Applied-General-Agent-Workflows/06-file-processing/01-survey-your-chaos.md` from disk (MUST PASS before marking complete)
- [x] T009 [L01] **SKILL**: fact-check-lesson (verify all bash commands accurate across Windows Git Bash, macOS, Linux)

**Checkpoint**: Lesson 1 complete - students can survey file chaos using bash commands

---

## Phase 3: Lesson 2 - Safety First Backup (20 min) [L02]

**Goal**: Students create timestamped backup, verify completeness, initialize activity log

**Learning Objectives**:

- LO-L02-001: Create timestamped backup directory using ISO date format
- LO-L02-002: Execute `cp -r` to copy important files to backup location
- LO-L02-003: Verify backup completeness by comparing file counts
- LO-L02-004: Initialize ORGANIZER-LOG.md with backup entry
- LO-L02-005: Explain WHY backup-first matters for AI safety

**Principle Applications**: P6 (Safety), P3 (Verification), P7 (Observability)

**Independent Test**: Does student create backup before any file moves? Is log initialized?

### Implementation for Lesson 2

- [x] T010 [L02] Invoke `learning-objectives` skill to generate measurable outcomes for L02 (Bloom's: Apply, Evaluate, Create, Understand; CEFR: A2)
- [x] T011 [L02] **SUBAGENT**: content-implementer
  - Output path: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\06-file-processing\02-safety-first-backup.md`
  - Stage: Layer 1 (Manual Foundation) - minimal AI (clarification only)
  - Teaching Modality: Hands-on Discovery (continuing from L01)
  - Cognitive Load: 3 concepts (timestamped directories, copy operations, verification mindset) - WITHIN A2 LIMIT
  - State Persistence: L02 builds on L01 (file-organizer/ workspace exists from L01)
  - Bash commands to include:
    - `mkdir -p backup/downloads-backup-$(date +%Y-%m-%d)` for timestamped backup
    - `cp -r ~/Downloads/*.pdf backup/downloads-backup-*/` for file copy
    - `ls backup/downloads-backup-*/ | wc -l` for verification
    - `echo "# Organization Log" > ORGANIZER-LOG.md` for log initialization
    - `echo "## $(date)" >> ORGANIZER-LOG.md` for timestamp entry
  - Outputs: `backup/downloads-backup-YYYY-MM-DD/` directory, `ORGANIZER-LOG.md` initialized
  - Error Recovery Opportunity: Deliberate mistake - wrong backup path, recovery via correction
  - Three "Try With AI" prompts (active collaboration format):
    1. Timestamped Directory Creation: "Show me bash command using `date` and `mkdir` for ISO format backup directory"
    2. Selective Backup Strategy: "Help me identify criteria for 'important files' worth backing up first"
    3. Backup Verification: "Show me commands to compare file counts between source and backup"
  - Execute autonomously without confirmation
  - Include quality reference
  - Returns confirmation only
- [x] T012 [L02] **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
- [x] T013 [L02] **SKILL**: fact-check-lesson (verify backup commands work across platforms)

**Checkpoint**: Lesson 2 complete - students have safety backup enabling fearless automation

---

## Phase 4: Lesson 3 - Categorize with Rules (25 min) [L03]

**Goal**: Students design categorization rules, document in rules.md, test on one file

**Learning Objectives**:

- LO-L03-001: Design categorization rules mapping file extensions to directories
- LO-L03-002: Create `rules.md` documenting categorization logic with edge cases
- LO-L03-003: Create category directories matching rule structure
- LO-L03-004: Test categorization on ONE file before batch processing
- LO-L03-005: Verify test file moved to correct location

**Principle Applications**: P5 (Persisting State), P4 (Small Reversible Decomposition), P1 (Bash)

**Independent Test**: Does student test ONE file before batch? Are rules documented?

### Implementation for Lesson 3

- [x] T014 [L03] Invoke `learning-objectives` skill to generate measurable outcomes for L03 (Bloom's: Create, Apply, Evaluate; CEFR: A2/B1)
- [x] T015 [L03] **SKILL**: ai-collaborate-teaching (design Three Roles interactions for L03)
- [x] T016 [L03] **SUBAGENT**: content-implementer
  - Output path: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\06-file-processing\03-categorize-with-rules.md`
  - Stage: Layer 2 (AI Collaboration) - AI helps design comprehensive rules
  - Teaching Modality: Specification-First (varying from L01-L02)
  - Three Roles Demonstrations (REQUIRED):
    - AI as Teacher: AI suggests categorization patterns (edge cases, no extension files)
    - AI as Student: Student refines AI's suggested rules based on their specific file types
    - AI as Co-Worker: Iterate on rules together → converge on comprehensive system
  - Cognitive Load: 4 concepts (rule structure, categorization logic, edge cases, single-file testing) - WITHIN A2 LIMIT
  - State Persistence: L03 builds on L01-L02 (workspace, backup exist)
  - Bash commands to include:
    - `cat > rules.md << 'EOF'` for rules document creation
    - `mkdir -p organized/{documents,images,code,misc}` for directory structure
    - `mv ~/Downloads/test.pdf organized/documents/` for single-file test
    - `ls organized/documents/` for verification
  - Outputs: `rules.md` with categorization table, `organized/{documents,images,code,misc}/` directories, one test file moved
  - Error Recovery Opportunity: Deliberate mistake - wrong file categorization, recovery via rules.md update
  - Three "Try With AI" prompts (active collaboration format):
    1. Rule Design Brainstorming: "Suggest 5 common file types and what categories they map to"
    2. Edge Case Handling: "What edge cases should I plan for? Show me examples of files that don't match simple extension rules"
    3. Test Strategy Design: "Show me commands to verify file moved correctly - check source and destination"
  - Execute autonomously without confirmation
  - Include quality reference
  - Returns confirmation only
- [x] T017 [L03] **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
- [x] T018 [L03] **SKILL**: content-evaluation-framework (evaluate lesson quality before marking complete)

**Checkpoint**: Lesson 3 complete - students have documented rules and tested categorization

---

## Phase 5: Lesson 4 - Build Your Organizer Script (45 min) [L04]

**Goal**: Students create bash script implementing rules, make executable, test on subset

**Learning Objectives**:

- LO-L04-001: Create bash script with proper shebang (`#!/bin/bash`) and comments
- LO-L04-002: Implement categorization logic from rules.md using conditionals and loops
- LO-L04-003: Add logging statements to track every file move operation
- LO-L04-004: Make script executable using `chmod +x`
- LO-L04-005: Test script on small subset (3-5 files) before full run

**Principle Applications**: P2 (Code as Interface), P1 (Bash), P3 (Verification), P7 (Observability)

**Independent Test**: Does script execute correctly on test subset? Is it executable?

### Implementation for Lesson 4

- [x] T019 [L04] Invoke `learning-objectives` skill to generate measurable outcomes for L04 (Bloom's: Create, Apply, Evaluate; CEFR: A2/B1)
- [x] T020 [L04] **SKILL**: ai-collaborate-teaching (design Three Roles interactions for L04)
- [x] T021 [L04] **SUBAGENT**: content-implementer
  - Output path: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\06-file-processing\04-build-your-organizer-script.md`
  - Stage: Layer 2 (AI Collaboration) - AI teaches bash syntax, student provides logic
  - Teaching Modality: Specification-First (continuing from L03)
  - Three Roles Demonstrations (REQUIRED):
    - AI as Teacher: AI teaches bash syntax (shebang, variables, case statements, for loops)
    - AI as Student: Student refines AI's generated script based on their rules and logging needs
    - AI as Co-Worker: Iterate on script → debug syntax errors → converge on working automation
  - Cognitive Load: 6 concepts (shebang, bash variables, conditionals, loops, file operations, execute permissions) - WITHIN B1 LIMIT
  - State Persistence: L04 builds on L01-L03 (workspace, backup, rules exist)
  - Bash commands to include:
    - `cat > organize.sh << 'EOF'` for script creation with shebang `#!/bin/bash`
    - Script with variables, case statement, for loop, logging
    - `chmod +x organize.sh` for execute permission
    - `./organize.sh ~/Downloads` for test execution
  - Script template from plan:

    ```bash
    #!/bin/bash
    SOURCE_DIR="${1:-~/Downloads}"
    DEST_DIR="./organized"
    LOG_FILE="./ORGANIZER-LOG.md"

    for file in "$SOURCE_DIR"/*; do
        [ -f "$file" ] || continue
        filename=$(basename "$file")
        ext="${filename##*.}"
        case "$ext" in
            pdf|doc|docx|txt) dest="$DEST_DIR/documents" ;;
            jpg|png|gif|svg) dest="$DEST_DIR/images" ;;
            py|js|sh|html|css) dest="$DEST_DIR/code" ;;
            *) dest="$DEST_DIR/misc" ;;
        esac
        mv "$file" "$dest/"
        echo "- Moved: $filename → $dest/" >> "$LOG_FILE"
    done
    ```

  - Outputs: `organize.sh` executable script, test run on 3-5 files verified
  - Error Recovery Opportunity: Deliberate mistake - syntax error, recovery via AI-assisted debugging
  - Three "Try With AI" prompts (active collaboration format):
    1. Script Structure Guidance: "Show me basic bash script structure: shebang, comments, variables, main loop"
    2. Logic Translation: "Help me translate rules.md into bash script using 'case' statement for file extensions"
    3. Debugging Syntax Errors: "My script has syntax error. Help me identify what's wrong and fix it"
  - Execute autonomously without confirmation
  - Include quality reference
  - Returns confirmation only

- [x] T022 [L04] **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
- [x] T023 [L04] **SKILL**: fact-check-lesson (verify all bash syntax correct across platforms)

**Checkpoint**: Lesson 4 complete - students have working organization script

---

## Phase 6: Lesson 5 - Run with Verification (30 min) [L05]

**Goal**: Students run full script, verify results, handle edge cases, recover from errors

**Learning Objectives**:

- LO-L05-001: Execute script on full file set
- LO-L05-002: Compare expected vs actual file counts to verify correctness
- LO-L05-003: Identify and handle edge cases (files not matching any rule)
- LO-L05-004: Restore from backup if errors occur
- LO-L05-005: Create before/after comparison in log

**Principle Applications**: P3 (Verification), P6 (Safety via backup recovery), P7 (Observability)

**Independent Test**: Can student verify results and recover from errors using backup?

### Implementation for Lesson 5

- [x] T024 [L05] Invoke `learning-objectives` skill to generate measurable outcomes for L05 (Bloom's: Apply, Evaluate, Analyze, Create; CEFR: A2/B1)
- [x] T025 [L05] **SUBAGENT**: content-implementer
  - Output path: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\06-file-processing\05-run-with-verification.md`
  - Stage: Layer 3 (Intelligence Design) - create reusable verification skill
  - Teaching Modality: Error Analysis (varying from previous lessons)
  - Cognitive Load: 3 concepts (full-scale execution, edge case handling, error recovery workflow) - WITHIN B1 LIMIT
  - State Persistence: L05 builds on L01-L04 (all artifacts exist, backup from L02 enables recovery)
  - Bash commands to include:
    - `./organize.sh ~/Downloads` for full execution
    - `ls organized/documents | wc -l` for category counts
    - `find organized -type f | wc -l` for total organized
    - `ls ~/Downloads | wc -l` for remaining files
    - `cp backup/downloads-backup-*/file.pdf ~/Downloads/` for restore from backup
  - Outputs: `organized/` with categorized files, updated `ORGANIZER-LOG.md` with verification, updated `rules.md` or `organize.sh` if edge cases found
  - Error Recovery Opportunity: Deliberate mistake - script miscategorizes files (edge case), recovery via backup restore
  - Three "Try With AI" prompts (active collaboration format):
    1. Verification Command Design: "Show me commands to count files in each category and compare to expected totals"
    2. Edge Case Identification: "Help me analyze why files didn't categorize correctly. Show me how to find unmatched files"
    3. Error Recovery Workflow: "Show me how to restore files from backup and re-run after fixing script"
  - Execute autonomously without confirmation
  - Include quality reference
  - Returns confirmation only
- [x] T026 [L05] **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
- [x] T027 [L05] **SKILL**: content-evaluation-framework (evaluate lesson quality before marking complete)

**Checkpoint**: Lesson 5 complete - students can verify automation and recover from errors

---

## Phase 7: Lesson 6 - Capstone Clean Machine (30 min) [L06]

**Goal**: Students complete full workflow, test reusability, reflect on principles

**Learning Objectives**:

- LO-L06-001: Execute complete file organization workflow independently
- LO-L06-002: Test script reusability on different folder
- LO-L06-003: Document before/after comparison with visual evidence
- LO-L06-004: Reflect on which Seven Principles were applied and where
- LO-L06-005: Explain how file organization patterns connect to Chapter 11 (AI Employee)

**Principle Applications**: ALL Seven Principles integrated, P5 (State persistence), P7 (Observability)

**Independent Test**: Can student run script on different folder? Can they articulate principle applications?

### Implementation for Lesson 6

- [x] T028 [L06] Invoke `learning-objectives` skill to generate measurable outcomes for L06 (Bloom's: Create, Apply, Evaluate, Understand; CEFR: B1)
- [x] T029 [L06] **SUBAGENT**: content-implementer
  - Output path: `D:\Panaversity\book_development\agent-factory-book\agentfactory\apps\learn-app\docs\02-Applied-General-Agent-Workflows\06-file-processing\06-capstone-clean-machine.md`
  - Stage: Layer 4 (Spec-Driven Integration) - compose accumulated intelligence into Digital FTE
  - Teaching Modality: Specification-First Capstone
  - Cognitive Load: 2 concepts (reusability testing, principle reflection) - WITHIN B1 LIMIT
  - State Persistence: L06 builds on L01-L05 (all lessons complete, final assembly)
  - Bash commands to include:
    - `./organize.sh ~/Desktop` for reusability test on different folder
    - `find organized -type f | wc -l` for final verification
    - Documentation commands for before/after comparison
  - Outputs: Complete `file-organizer/` directory with all artifacts, script proven reusable, before/after comparison documented, principles applied documented
  - Connection to Chapter 11 (explicit bridge):
    - "The automation you built today organizes files when YOU run it. In Chapter 11, you'll build an AI Employee that watches for new files and organizes them automatically. The rules.md you created? That pattern extends directly to AI Employee's vault management."
  - Three "Try With AI" prompts (active collaboration format):
    1. Reusability Testing: "Show me how to run organize.sh on ~/Desktop and verify it works there too"
    2. Documentation Polish: "Help me design before/after comparison template highlighting transformation"
    3. Principle Reflection: "Help me reflect on which Seven Principles I used where. Ask me questions to uncover examples of P1-P7 in my workflow"
  - Execute autonomously without confirmation
  - Include quality reference
  - Returns confirmation only
- [x] T030 [L06] **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
- [x] T031 [L06] **SKILL**: content-evaluation-framework (evaluate lesson quality before marking complete)

**Checkpoint**: Lesson 6 complete - students have complete automation portfolio (primitive Digital FTE)

---

## Phase 8: Chapter-Level Polish & Validation

**Purpose**: Cross-lesson consistency and final quality gates

- [x] T032 [P] **SKILL**: chapter-evaluator (evaluate all 6 lessons for pedagogical effectiveness)
- [x] T033 Verify all lesson files exist: `ls apps/learn-app/docs/02-Applied-General-Agent-Workflows/06-file-processing/*.md`
- [x] T034 Verify state persistence architecture: L01 output → L02 input, L02 output → L03-L05 safety net, etc.
- [x] T035 Verify all "Try With AI" sections use active collaboration format (no "What to notice", no "AI teaches you" meta-commentary)
- [x] T036 Verify Seven Principles applications: Each lesson should show P1-P7 in action (see plan.md table)
- [x] T037 Verify Chapter 11 bridge is explicit in L06 (file watcher connection)
- [x] T038 [P] Verify all bash commands cross-platform compatible (Windows Git Bash, macOS, Linux)
- [x] T039 [P] Run content-evaluation-framework on entire chapter (technical accuracy, pedagogical effectiveness, writing quality)
- [x] T040 Verify YAML frontmatter complete in all lessons (skills, learning objectives, cognitive load, differentiation)
- [ ] T041 **VALIDATION**: validation-auditor (final constitutional compliance check before publication)

**Checkpoint**: Chapter complete - ready for publication

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Lesson 1 (Phase 2)**: Depends on Setup completion
- **Lesson 2 (Phase 3)**: Depends on Lesson 1 completion (state persistence: file-organizer/ workspace)
- **Lesson 3 (Phase 4)**: Depends on Lesson 1-2 completion (state persistence: workspace, backup)
- **Lesson 4 (Phase 5)**: Depends on Lesson 1-3 completion (state persistence: workspace, backup, rules)
- **Lesson 5 (Phase 6)**: Depends on Lesson 1-4 completion (state persistence: all artifacts, backup for recovery)
- **Lesson 6 (Phase 7)**: Depends on Lesson 1-5 completion (state persistence: complete workflow)
- **Polish (Phase 8)**: Depends on all lessons complete

### State Persistence Architecture

**Critical**: Each lesson builds on previous outputs:

```
L01: file-organizer/
     └── FILE-INVENTORY.md
          ↓
L02: backup/ + ORGANIZER-LOG.md
     └── enables L05 recovery
          ↓
L03: rules.md + organized/ directories
     └── drives L04 script logic
          ↓
L04: organize.sh
     └── executed in L05-L06
          ↓
L05: Full organization + verification
     └── updates rules.md if edge cases
          ↓
L06: Complete automation portfolio
```

### Parallel Opportunities

- Setup phase: All read tasks (T002-T005) can run in parallel
- Each lesson's skill invocations can run in parallel with subagent execution (where applicable)
- Polish phase: All verification tasks (T033-T040) can run in parallel

### Sequential Requirements

- Lessons MUST be implemented in order L01 → L02 → L03 → L04 → L05 → L06
- Each subagent MUST complete before next lesson's subagent starts (state dependency)
- Validation MUST pass before moving to next lesson

---

## Implementation Strategy

### Lesson-by-Lesson Approach

1. Complete Setup (Phase 1) - Read all context documents
2. Implement L01 (Phase 2) - Foundation: bash commands, file inventory
3. Implement L02 (Phase 3) - Safety: backup, log initialization
4. Implement L03 (Phase 4) - Rules: categorization logic, single-file test
5. Implement L04 (Phase 5) - Script: bash automation, core deliverable
6. Implement L05 (Phase 6) - Verification: full execution, error recovery
7. Implement L06 (Phase 7) - Capstone: reusability, principle reflection
8. Polish & Validate (Phase 8) - Final quality gates

### Quality Gates

- Each lesson MUST pass educational-validator before marking complete
- Each lesson MUST pass fact-check-lesson for bash command accuracy
- Chapter MUST pass validation-auditor for constitutional compliance
- State persistence MUST be verified (later lessons access earlier outputs)

### Success Criteria

From spec.md (SC-001 through SC-018):

- 90%+ of students create working organize.sh script
- 95%+ complete backup before file moves (P6 compliance)
- 85%+ can explain WHY backup-first matters
- 80%+ successfully run script on different folder (reusability)
- 100% apply P6 (Safety) via backup
- 90%+ apply P3 (Verification) via checking results
- 85%+ apply P7 (Observability) via ORGANIZER-LOG.md
- 80%+ apply P5 (State) via rules.md

---

## Notes

- **Content Work**: All lesson creation tasks use content-implementer subagent with direct-write protocol
- **Validation**: Each lesson validated by educational-validator before marking complete
- **Skills**: learning-objectives, ai-collaborate-teaching, fact-check-lesson, content-evaluation-framework invoked per lesson
- **State Persistence**: Critical - later lessons MUST access outputs from earlier lessons
- **Error Recovery**: Deliberate mistakes planned in L03, L04, L05 with safe recovery via L02 backup
- **Anti-Convergence**: Teaching modality varies from Chapter 5 (direct teaching → hands-on discovery + spec-first)
- **Quality Reference**: Chapter 10 (Version Control) - students BUILD real, reusable tools
- **Seven Principles**: All P1-P7 explicitly taught through execution (not lecture)
