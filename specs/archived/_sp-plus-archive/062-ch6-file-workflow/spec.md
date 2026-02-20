# Feature Specification: Chapter 6 Redesign - File Organization Workflow

**Feature Branch**: `062-ch6-file-workflow`
**Created**: 2025-01-27
**Status**: Draft
**Input**: Redesign Chapter 6 from teaching-only to proper workflow chapter where students BUILD real, reusable outputs

---

## Executive Summary

This specification defines the complete redesign of Chapter 6 from a passive "observe and learn" chapter to an active "build and own" workflow chapter. Students will transform their own cluttered Downloads folder (or any project files) into an organized system using a reusable bash script they create and own.

**Core Design Decisions**:

- **Workflow-First**: Students BUILD real outputs (scripts, organized folders, logs) they keep forever
- **Own Files Domain**: No paid subscriptions - students work on their OWN files
- **Primary Principles**: P1 (Bash), P3 (Verification), P6 (Safety) - applied through execution, not lecture
- **State Persistence**: Later lessons build on earlier work (file-organizer/ accumulates)
- **Error Recovery**: Deliberate mistakes → safe undo via backup (P6 in action)

**Why This Redesign Matters**:
The current Chapter 6 teaches file operations conceptually through dialogue examples. Students READ about `ls` and `mv` but never BUILD automation they can reuse. This violates Part 2's purpose: "Agent Workflow Primitives" means students CREATE workflow tools, not study them.

**Model Chapter**: Chapter 10 (Version Control) is the quality standard - students BUILD Git repos, GitHub backups, and merged PRs they actually use.

---

## Assumed Knowledge

### What Students Know BEFORE This Chapter

| Concept                       | Source               | Level |
| ----------------------------- | -------------------- | ----- |
| General Agent paradigm        | Part 1, Chapters 1-3 | A1-A2 |
| Seven Principles (conceptual) | Chapter 4            | A2    |
| Claude Code interface basics  | Chapter 5            | A2    |
| Basic prompting               | Chapter 5            | A2    |

**Students DO NOT yet know**:

- Bash scripting beyond basic commands
- File organization patterns
- How to persist workflow state across sessions
- How to create reusable automation

### What Students Learn IN This Chapter

| Skill                                                   | Lesson         | Level After |
| ------------------------------------------------------- | -------------- | ----------- |
| File system navigation (`ls`, `find`, `du`)             | L01            | B1          |
| Safe backup patterns (`cp -r`, timestamped directories) | L02            | B1          |
| Categorization rules (file types, naming patterns)      | L03            | B1          |
| Bash scripting (conditionals, loops, variables)         | L04            | B1          |
| Verification workflows (before/after comparison)        | L05            | B1          |
| End-to-end automation                                   | L06 (Capstone) | B1-B2       |

---

## User Scenarios & Testing

### User Story 1 - Survey Digital Chaos (Priority: P1)

**Scenario**: Domain expert (accountant, designer, consultant) opens Claude Code to tackle their cluttered Downloads folder. They have 500+ unorganized files accumulated over months. They don't know where to start.

**Journey**:

1. Student opens Claude Code in their Downloads folder (or chosen project directory)
2. Runs `ls -la` to see current state (immediate reality check)
3. Uses `find . -type f | wc -l` to count total files
4. Uses `du -sh *` to see space consumption by item
5. Creates `file-organizer/` directory as workspace
6. Generates `FILE-INVENTORY.md` report documenting current chaos
7. Identifies top file types using `find . -name "*.pdf" | wc -l` pattern

**Why this priority**: P1 because students cannot organize what they haven't surveyed. This establishes the "current state" baseline for all subsequent work. Without this, students don't know what problem they're solving.

**Independent Test**: Can be tested by verifying `file-organizer/FILE-INVENTORY.md` exists with accurate file counts matching reality.

**Acceptance Scenarios**:

1. **Given** student has cluttered Downloads folder, **When** student runs `ls -la`, **Then** student sees real files with permissions, sizes, dates
2. **Given** student wants file count, **When** student runs `find . -type f | wc -l`, **Then** student gets accurate total (verifiable by manual count of subset)
3. **Given** student completes survey, **When** student creates FILE-INVENTORY.md, **Then** report contains: total count, breakdown by type, largest files, date range

---

### User Story 2 - Safety First Backup (Priority: P1)

**Scenario**: Before moving any files, student creates safety backup. This is P6 (Constraints and Safety) in action - establishing the safety net before any destructive operations.

**Journey**:

1. Student creates timestamped backup directory: `backup/downloads-backup-2025-01-27/`
2. Student identifies "important" files (recent, large, or by type)
3. Student copies important files: `cp -r important-stuff/* backup/`
4. Student verifies backup completeness: `ls backup/ | wc -l` matches expectations
5. Student documents backup in `ORGANIZER-LOG.md`: what, when, why

**Why this priority**: P1 because all subsequent operations (move, rename, delete) are only safe with backup. This lesson MUST complete before any file movement.

**Independent Test**: Can be tested by verifying backup directory exists, contains expected files, and log documents the backup action.

**Acceptance Scenarios**:

1. **Given** student has surveyed files, **When** student creates backup directory with timestamp, **Then** directory name includes ISO date (2025-01-27 format)
2. **Given** student selects important files, **When** student copies to backup, **Then** `diff` between source and backup shows identical content
3. **Given** backup is complete, **When** student updates ORGANIZER-LOG.md, **Then** log contains: backup location, file count, timestamp, reason

---

### User Story 3 - Categorize with Rules (Priority: P2)

**Scenario**: Student defines categorization rules and tests them on one file before batch processing. This teaches P4 (Small, Reversible Decomposition) - test on small scale before scaling up.

**Journey**:

1. Student creates `rules.md` defining categorization logic:
   - `.pdf`, `.doc`, `.docx` → `documents/`
   - `.jpg`, `.png`, `.gif` → `images/`
   - `.py`, `.js`, `.sh` → `code/`
   - Everything else → `misc/`
2. Student creates target directories in `organized/`
3. Student tests with ONE file: `mv test.pdf organized/documents/`
4. Student verifies move succeeded: `ls organized/documents/`
5. Student documents rule testing in log

**Why this priority**: P2 because rules must be explicit before automation. Students learn to WRITE rules (P5 - State) before EXECUTING rules.

**Independent Test**: Can be tested by verifying `rules.md` contains complete categorization logic and one file successfully moved to correct category.

**Acceptance Scenarios**:

1. **Given** student has backup, **When** student writes rules.md, **Then** document covers: file extensions mapping, directory targets, edge cases (unknown types)
2. **Given** rules exist, **When** student creates organized/ subdirectories, **Then** directories match rule categories (documents, images, code, misc)
3. **Given** directories exist, **When** student moves ONE test file, **Then** file appears in correct category AND disappears from source

---

### User Story 4 - Build Organizer Script (Priority: P2)

**Scenario**: Student transforms manual rules into automated bash script. This is P2 (Code as Universal Interface) in action - code solves the problem systematically.

**Journey**:

1. Student creates `organize.sh` with shebang and comments
2. Script implements categorization logic from rules.md
3. Script includes verification after each operation (P3)
4. Script logs every action to ORGANIZER-LOG.md (P7)
5. Student makes script executable: `chmod +x organize.sh`
6. Student tests script on small subset (3-5 files)

**Why this priority**: P2 because script creation is the core deliverable. This transforms one-time manual work into reusable automation.

**Independent Test**: Can be tested by running script on test files and verifying correct categorization + log entries.

**Acceptance Scenarios**:

1. **Given** rules.md exists, **When** student creates organize.sh, **Then** script contains: shebang, categorization conditionals, move operations
2. **Given** script exists, **When** student runs `chmod +x organize.sh`, **Then** `ls -la organize.sh` shows execute permission
3. **Given** script is executable, **When** student runs `./organize.sh` on test files, **Then** files move to correct directories AND log is updated

---

### User Story 5 - Run with Verification (Priority: P3)

**Scenario**: Student runs full script on all files, verifies results, handles edge cases. This applies P3 (Verification) at scale.

**Journey**:

1. Student runs script on full Downloads folder
2. Student verifies results: compare expected vs actual counts
3. Student identifies edge cases: files that didn't match any rule
4. Student handles edge cases: update rules or manually categorize
5. Student creates before/after comparison in log
6. Student confirms backup still intact (safety check)

**Why this priority**: P3 because verification is what separates reliable automation from risky scripts. Students learn to NOT trust automation blindly.

**Independent Test**: Can be tested by comparing file counts before/after and verifying all files accounted for.

**Acceptance Scenarios**:

1. **Given** script tested on subset, **When** student runs on full folder, **Then** total files organized = total files surveyed (minus backup)
2. **Given** script completes, **When** student runs verification commands, **Then** each category has expected file count
3. **Given** edge cases exist, **When** student identifies unmatched files, **Then** student either updates rules.md OR manually categorizes with log entry

---

### User Story 6 - Capstone: Clean Machine (Priority: P3)

**Scenario**: Student completes full organization workflow, creates documentation, reflects on principles applied. This is the "portfolio piece" they keep.

**Journey**:

1. Student runs final organization pass
2. Student creates before/after screenshot comparison
3. Student updates ORGANIZER-LOG.md with full history
4. Student updates rules.md with lessons learned
5. Student tests script reusability: run on different folder
6. Student documents which principles were applied where

**Why this priority**: P3 because capstone demonstrates mastery through integration. Students prove they can apply ALL principles in a real workflow.

**Independent Test**: Can be tested by verifying complete file-organizer/ directory with all artifacts present and script runs successfully on new folder.

**Acceptance Scenarios**:

1. **Given** all lessons complete, **When** student finalizes file-organizer/, **Then** directory contains: organize.sh, rules.md, ORGANIZER-LOG.md, backup/, organized/
2. **Given** directory complete, **When** student runs script on different folder, **Then** script organizes new folder correctly (reusability proven)
3. **Given** capstone complete, **When** student reviews ORGANIZER-LOG.md, **Then** log shows full history from survey to completion

---

### Edge Cases

- **Empty Downloads folder**: Student has already organized → provide sample chaos folder for practice
- **Permission denied errors**: `chmod` or `sudo` needed → teach permission concepts (P6)
- **Files with spaces in names**: Requires quotes in bash → teach quoting patterns
- **Hidden files (.files)**: Not shown by default `ls` → teach `ls -la` pattern
- **Symbolic links**: May behave unexpectedly → teach `-L` flag for find
- **Read-only files**: Cannot move without permission change → verify before move
- **Duplicate filenames**: Category collision → teach timestamped renaming
- **Very large files**: Slow copy operations → teach progress indicators
- **Cross-filesystem moves**: `mv` fails, need `cp` + `rm` → teach detection and handling

---

## Requirements

### Functional Requirements

#### L01: Survey Your Chaos

- **FR-001**: Student MUST run `ls -la` to see current file state with permissions and timestamps
- **FR-002**: Student MUST run `find . -type f | wc -l` to count total files
- **FR-003**: Student MUST run `du -sh *` to see space consumption
- **FR-004**: Student MUST create `file-organizer/` workspace directory
- **FR-005**: Student MUST generate `FILE-INVENTORY.md` with file counts by type
- **FR-006**: Student MUST identify top 5 file types present

#### L02: Safety First Backup

- **FR-007**: Student MUST create timestamped backup directory (ISO date format)
- **FR-008**: Student MUST copy important files to backup using `cp -r`
- **FR-009**: Student MUST verify backup completeness (file count comparison)
- **FR-010**: Student MUST initialize `ORGANIZER-LOG.md` with backup entry
- **FR-011**: Student MUST NOT proceed to moving files without completed backup

#### L03: Categorize with Rules

- **FR-012**: Student MUST create `rules.md` documenting categorization logic
- **FR-013**: Student MUST define at least 4 categories (documents, images, code, misc)
- **FR-014**: Student MUST create corresponding directories in `organized/`
- **FR-015**: Student MUST test categorization on ONE file before batch
- **FR-016**: Student MUST verify test file moved to correct location
- **FR-017**: Student MUST log rule testing results

#### L04: Build Your Organizer Script

- **FR-018**: Student MUST create `organize.sh` with proper shebang (`#!/bin/bash`)
- **FR-019**: Script MUST implement categorization from rules.md
- **FR-020**: Script MUST include comments explaining logic
- **FR-021**: Script MUST log every file move operation
- **FR-022**: Script MUST verify each move succeeded before proceeding
- **FR-023**: Student MUST make script executable with `chmod +x`
- **FR-024**: Student MUST test script on 3-5 files before full run

#### L05: Run with Verification

- **FR-025**: Student MUST run script on full file set
- **FR-026**: Student MUST compare expected vs actual file counts
- **FR-027**: Student MUST identify and handle edge cases (unmatched files)
- **FR-028**: Student MUST create before/after comparison in log
- **FR-029**: Student MUST verify backup remains intact after operations

#### L06: Capstone Clean Machine

- **FR-030**: Student MUST complete full organization workflow
- **FR-031**: Student MUST create before/after visual documentation
- **FR-032**: Student MUST finalize ORGANIZER-LOG.md with complete history
- **FR-033**: Student MUST test script reusability on different folder
- **FR-034**: Student MUST document which Seven Principles were applied and where

### Key Entities

- **File Organizer Workspace** (`file-organizer/`): Root directory containing all workflow artifacts; persists across lessons; students keep forever
- **Organizer Log** (`ORGANIZER-LOG.md`): Chronological record of all actions; implements P7 (Observability); timestamps, actions, outcomes
- **Categorization Rules** (`rules.md`): Persistent state documenting categorization logic; implements P5 (Persisting State); file extension → directory mappings
- **Organizer Script** (`organize.sh`): Reusable bash automation; implements P1 (Bash) and P2 (Code); executable, tested, documented
- **Backup Directory** (`backup/`): Safety net for recovery; implements P6 (Constraints and Safety); timestamped copies of important files
- **Organized Output** (`organized/`): Result directory with categorized files; documents/, images/, code/, misc/ subdirectories
- **File Inventory** (`FILE-INVENTORY.md`): Initial survey documenting chaos state; baseline for measuring success

---

## Success Criteria

### Measurable Outcomes

**Learning Objectives Met:**

- **SC-001**: 90%+ of students successfully create working `organize.sh` script that correctly categorizes files by type
- **SC-002**: 95%+ of students complete backup before any file move operations (P6 compliance)
- **SC-003**: 85%+ of students can explain WHY backup-first matters (conceptual understanding, not just compliance)
- **SC-004**: 80%+ of students successfully run script on a DIFFERENT folder than practice folder (reusability proven)

**Workflow Competence:**

- **SC-005**: Students complete survey lesson (L01) within 20 minutes, producing FILE-INVENTORY.md with accurate counts
- **SC-006**: Students complete backup lesson (L02) within 15 minutes, producing timestamped backup directory
- **SC-007**: Students complete rules lesson (L03) within 25 minutes, producing rules.md with 4+ categories
- **SC-008**: Students complete script lesson (L04) within 45 minutes, producing working organize.sh
- **SC-009**: Students complete capstone (L06) within 30 minutes, producing complete file-organizer/ directory

**Principle Application:**

- **SC-010**: 100% of students apply P6 (Safety) by creating backup before destructive operations
- **SC-011**: 90%+ of students apply P3 (Verification) by checking results after each operation
- **SC-012**: 85%+ of students apply P7 (Observability) by maintaining ORGANIZER-LOG.md throughout
- **SC-013**: 80%+ of students apply P5 (State) by persisting rules in rules.md

**Reusability & Retention:**

- **SC-014**: 70%+ of students report using organize.sh script again within 30 days (post-course survey)
- **SC-015**: 80%+ of students keep file-organizer/ directory after course completion
- **SC-016**: 75%+ of students can modify script for different categorization rules independently

**Connection to Chapter 11:**

- **SC-017**: 85%+ of students recognize how file organization capabilities enable AI Employee's file management (explicit connection made)
- **SC-018**: Students can articulate how organize.sh patterns apply to AI Employee's file watcher workflow

---

## Constraints

### Pedagogical Constraints

- **C-001**: Students MUST work on their OWN files (Downloads, projects) - no synthetic datasets requiring download
- **C-002**: Zero paid subscriptions required - students need only Claude Code and terminal
- **C-003**: State MUST persist across lessons - L02 builds on L01, L03 on L02, etc.
- **C-004**: Error recovery MUST be practiced - students make deliberate mistakes and safely undo via backup
- **C-005**: Principles applied through EXECUTION, not lecture - students DO, then understand why it matters

### Technical Constraints

- **C-006**: All commands MUST be cross-platform (Windows Git Bash, macOS Terminal, Linux shell) OR provide platform-specific alternatives
- **C-007**: Bash script MUST use POSIX-compatible syntax for maximum portability
- **C-008**: No Python or advanced scripting - this is Part 2, students don't know Python yet
- **C-009**: All file operations MUST be reversible via backup (no permanent deletion in core lessons)

### Scope Constraints

- **C-010**: Chapter focuses on file ORGANIZATION, not file PROCESSING (no content extraction, parsing)
- **C-011**: No database or external storage - files stay on local filesystem
- **C-012**: No network operations - no cloud sync, no remote backup (that's cloud-native in Part 6)
- **C-013**: No GUI tools - this chapter teaches terminal-first approach (P1)

### Interface Constraints

- **C-014**: Primary interface is Claude Code (terminal) - all lessons execute in terminal
- **C-015**: Secondary interface is Claude Cowork for PLANNING complex organization strategies only
- **C-016**: Students MUST see command output - no hidden operations

---

## Non-Goals

### Out of Scope for This Chapter

**File Content Processing:**

- Opening files to read/parse content
- OCR on images or PDFs
- Text extraction from documents
- Content-based categorization (beyond filename/extension)

**Advanced Automation:**

- Cron job scheduling (that's Chapter 10 automation)
- File watchers for automatic organization (that's Chapter 11 AI Employee)
- Event-driven file processing
- Background daemon processes

**Cloud and Network:**

- Cloud backup (Dropbox, Google Drive, S3)
- Network file shares
- Remote filesystem operations
- Sync services

**Advanced Scripting:**

- Python scripts (Part 4 content)
- Complex regex patterns
- Database storage of file metadata
- GUI applications for organization

**Why Excluded**: These topics exceed Part 2's scope (Applied Workflows for domain experts), require prerequisites from later parts (Python, Cloud Native), or distract from core objective (teaching Seven Principles through practical file organization).

**Where to Find These Topics**: File watchers → Chapter 11 (AI Employee), Cloud backup → Part 6 (Cloud Native), Python scripting → Part 4 (Coding), Content processing → Part 5 (Building Agents).

---

## Assumptions

### Student Prerequisites

- **A-001**: Students completed Part 1 (Chapters 1-5) and understand General Agent paradigm
- **A-002**: Students have Claude Code installed and can open terminal sessions
- **A-003**: Students have file system with files to organize (Downloads folder assumed, alternative provided)
- **A-004**: Students understand basic file concepts (files, folders, extensions)

### Technical Environment

- **A-005**: Students have terminal access (Git Bash on Windows, Terminal on macOS/Linux)
- **A-006**: Students have write permissions in their chosen practice directory
- **A-007**: Students have at least 1GB free disk space for backup operations
- **A-008**: Students' terminals support basic bash commands (ls, mv, cp, find)

### Pedagogical Assumptions

- **A-009**: Working on OWN files creates immediate value and motivation
- **A-010**: Creating reusable tools (scripts) is more valuable than one-time organization
- **A-011**: Error recovery practice builds confidence for autonomous AI operations
- **A-012**: Explicit principle mapping helps students transfer patterns to new contexts

### Reasonable Defaults

- **A-013**: Default practice directory is Downloads folder (most universally cluttered)
- **A-014**: Default categories are: documents, images, code, misc (covers 90%+ of typical files)
- **A-015**: Default backup naming uses ISO date format (2025-01-27)
- **A-016**: Default log format is Markdown for readability

---

## Dependencies

### Prerequisite Chapters

- **Part 1, Chapter 4**: Seven Principles introduced conceptually (this chapter applies them practically)
- **Part 1, Chapter 5**: Claude Code interface basics (students can open terminal, run commands)

### Prerequisite Skills

- Basic typing and terminal navigation (open terminal, type commands)
- Understanding of files and folders conceptually
- Ability to read command output

### Downstream Dependencies (Knowledge Transfer Mapping)

**Chapter 7 (Research Synthesis)**:

- **Transfer**: File organization patterns for research outputs
- **Composition**: Research materials organized using L01-L06 patterns
- **Reinforcement**: rules.md concept extends to research categorization rules

**Chapter 8 (Data Analysis)**:

- **Transfer**: data/ folder organization mirrors organized/ structure
- **Composition**: Analysis outputs organized using categorization rules
- **Reinforcement**: Verification patterns (P3) apply to data quality checks

**Chapter 10 (Version Control)**:

- **Transfer**: file-organizer/ becomes first Git repository
- **Composition**: organize.sh script tracked in version control
- **Reinforcement**: Backup concepts (P6) replaced/enhanced by Git history

**Chapter 11 (AI Employee)**:

- **Transfer**: organize.sh patterns inform File Watcher behavior
- **Composition**: AI Employee uses file organization for vault management
- **Gap Closure**: Manual script → Automatic file watcher
- **Reinforcement**: Chapter 6 teaches WHAT to organize; Chapter 11 teaches WHEN to trigger

---

## Lesson Flow Detail

### L01: Survey Your Chaos (25 min)

**Core Question**: "What do I actually have?"

**Students DO**:

```bash
# Navigate to Downloads (or chosen folder)
cd ~/Downloads

# See what's there
ls -la

# Count total files
find . -type f | wc -l

# See space usage
du -sh *

# Count by type
find . -name "*.pdf" | wc -l
find . -name "*.jpg" -o -name "*.png" | wc -l

# Create workspace
mkdir file-organizer
cd file-organizer
```

**Output**: `file-organizer/FILE-INVENTORY.md` with accurate counts

**Principle Focus**: P1 (Bash is the Key), P7 (Observability)

---

### L02: Safety First Backup (20 min)

**Core Question**: "How do I protect myself before making changes?"

**Students DO**:

```bash
# Create timestamped backup
mkdir -p backup/downloads-backup-$(date +%Y-%m-%d)

# Copy important files
cp -r ~/Downloads/*.pdf backup/downloads-backup-*/

# Verify backup
ls backup/downloads-backup-*/ | wc -l

# Initialize log
echo "# Organization Log" > ORGANIZER-LOG.md
echo "## $(date)" >> ORGANIZER-LOG.md
echo "- Created backup: $(ls backup/)" >> ORGANIZER-LOG.md
```

**Output**: `backup/downloads-backup-YYYY-MM-DD/` with files, `ORGANIZER-LOG.md` initialized

**Principle Focus**: P6 (Constraints and Safety), P3 (Verification)

---

### L03: Categorize with Rules (25 min)

**Core Question**: "What rules should govern where files go?"

**Students DO**:

```bash
# Create rules document
cat > rules.md << 'EOF'
# File Organization Rules

## Categories

| Extension | Destination |
|-----------|-------------|
| .pdf, .doc, .docx, .txt | documents/ |
| .jpg, .png, .gif, .svg | images/ |
| .py, .js, .sh, .html, .css | code/ |
| everything else | misc/ |

## Edge Cases
- Unknown extension → misc/
- No extension → misc/
- Duplicate filename → append timestamp
EOF

# Create directories
mkdir -p organized/{documents,images,code,misc}

# Test with ONE file
mv ~/Downloads/test.pdf organized/documents/

# Verify
ls organized/documents/
```

**Output**: `rules.md` documented, `organized/` directories created, one file moved

**Principle Focus**: P1 (Bash), P5 (Persisting State)

---

### L04: Build Your Organizer Script (45 min)

**Core Question**: "How do I automate these rules?"

**Students DO**:

```bash
# Create script
cat > organize.sh << 'EOF'
#!/bin/bash
# File Organizer Script
# Applies rules from rules.md

SOURCE_DIR="${1:-~/Downloads}"
DEST_DIR="./organized"
LOG_FILE="./ORGANIZER-LOG.md"

echo "## Organization Run: $(date)" >> "$LOG_FILE"

# Process each file
for file in "$SOURCE_DIR"/*; do
    [ -f "$file" ] || continue

    filename=$(basename "$file")
    ext="${filename##*.}"

    case "$ext" in
        pdf|doc|docx|txt)
            dest="$DEST_DIR/documents"
            ;;
        jpg|png|gif|svg)
            dest="$DEST_DIR/images"
            ;;
        py|js|sh|html|css)
            dest="$DEST_DIR/code"
            ;;
        *)
            dest="$DEST_DIR/misc"
            ;;
    esac

    mv "$file" "$dest/"
    echo "- Moved: $filename → $dest/" >> "$LOG_FILE"
done

echo "Organization complete. Check $LOG_FILE for details."
EOF

# Make executable
chmod +x organize.sh

# Test on small set
./organize.sh ~/Downloads
```

**Output**: `organize.sh` executable, tested on subset

**Principle Focus**: P1 (Bash), P2 (Code as Universal Interface)

---

### L05: Run with Verification (30 min)

**Core Question**: "Did it work? How do I know?"

**Students DO**:

```bash
# Run full organization
./organize.sh ~/Downloads

# Verify counts
echo "Files in documents: $(ls organized/documents | wc -l)"
echo "Files in images: $(ls organized/images | wc -l)"
echo "Files in code: $(ls organized/code | wc -l)"
echo "Files in misc: $(ls organized/misc | wc -l)"

# Check for stragglers
echo "Files remaining in Downloads: $(ls ~/Downloads | wc -l)"

# Verify backup still intact
ls backup/

# Update log with verification
echo "## Verification: $(date)" >> ORGANIZER-LOG.md
echo "- Total organized: $(find organized -type f | wc -l)" >> ORGANIZER-LOG.md
```

**Output**: Organized folder complete, verification logged, edge cases handled

**Principle Focus**: P3 (Verification), P7 (Observability)

---

### L06: Capstone Clean Machine (30 min)

**Core Question**: "Can I use this again? What did I learn?"

**Students DO**:

```bash
# Final organization pass
./organize.sh ~/Desktop  # Test on different folder

# Document before/after
echo "## Final State: $(date)" >> ORGANIZER-LOG.md
echo "### Before: $(cat FILE-INVENTORY.md | head -10)" >> ORGANIZER-LOG.md
echo "### After:" >> ORGANIZER-LOG.md
find organized -type f | wc -l >> ORGANIZER-LOG.md

# Update rules with lessons learned
echo "## Lessons Learned" >> rules.md
echo "- [Your observations here]" >> rules.md

# Document principles applied
echo "## Principles Applied" >> ORGANIZER-LOG.md
echo "- P1 (Bash): All operations via terminal" >> ORGANIZER-LOG.md
echo "- P3 (Verification): Checked results after each step" >> ORGANIZER-LOG.md
echo "- P5 (State): Rules persisted in rules.md" >> ORGANIZER-LOG.md
echo "- P6 (Safety): Backup created before any moves" >> ORGANIZER-LOG.md
echo "- P7 (Observability): All actions logged" >> ORGANIZER-LOG.md
```

**Output**: Complete `file-organizer/` directory, script proven reusable, principles documented

**Principle Focus**: All Seven Principles integrated

---

## Final Deliverable Structure

```
file-organizer/
├── FILE-INVENTORY.md      # L01 output: Initial chaos survey
├── ORGANIZER-LOG.md       # L01-L06 output: Complete activity history (P7)
├── rules.md               # L03 output: Categorization rules (P5)
├── organize.sh            # L04 output: Reusable script (P1, P2)
├── backup/                # L02 output: Safety backup (P6)
│   └── downloads-backup-2025-01-27/
│       └── [backed up files]
└── organized/             # L05-L06 output: Categorized files
    ├── documents/
    ├── images/
    ├── code/
    └── misc/
```

**Students keep this directory forever. It's their first reusable AI-assisted automation tool.**

---

## Success Indicators (How We Know We're Done)

### Specification Complete When:

- [x] All user scenarios prioritized and testable independently (P1-P3 defined)
- [x] Functional requirements mapped to lessons (FR-001 through FR-034)
- [x] Success criteria measurable and technology-agnostic (SC-001 through SC-018)
- [x] Constraints and non-goals explicit (pedagogical, technical, scope)
- [x] Edge cases identified (9 common failure scenarios with guidance)
- [x] Dependencies mapped (prerequisites, downstream chapters)
- [x] Lesson flow detailed with actual bash commands

### Planning Ready When:

- [ ] Specification approved by human reviewer
- [ ] spec-architect validation passed
- [ ] Lesson structure validated against cognitive load limits (A2-B1)

### Implementation Ready When:

- [ ] Plan approved with lesson-by-lesson breakdown
- [ ] All bash commands tested on Windows Git Bash, macOS, Linux
- [ ] Reference implementation of organize.sh validated

### Validation Ready When:

- [ ] All lessons implemented with workflow-first approach
- [ ] All commands execute successfully on three platforms
- [ ] State persistence verified (later lessons access earlier outputs)
- [ ] Student can complete full workflow independently

### Publication Ready When:

- [ ] validation-auditor passes pedagogical review
- [ ] factual-verifier confirms all commands accurate
- [ ] Students report keeping file-organizer/ after course (survey)
- [ ] Connection to Chapter 11 explicit and valuable

---

**Status**: Specification Complete. Ready for review.
