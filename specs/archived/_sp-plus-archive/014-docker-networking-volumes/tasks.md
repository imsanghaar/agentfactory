# Tasks: Docker Chapter 49 Expansion

**Feature**: `014-docker-networking-volumes`
**Created**: 2025-12-23
**Total Tasks**: 12
**Parallel Opportunities**: 4 (new lesson creation)

## Phase 1: Setup (Sequential)

- [ ] T001 Verify current Docker chapter structure with `ls /Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/`

## Phase 2: File Renaming (Sequential - MUST complete before Phase 3)

Rename existing lessons 6-10 to 10-14 to make room for new content.

- [ ] T002 Rename `06-docker-compose-development.md` to `10-docker-compose-development.md` and update sidebar_position to 10
- [ ] T003 Rename `07-security-best-practices.md` to `11-security-best-practices.md` and update sidebar_position to 11
- [ ] T004 Rename `08-ai-assisted-docker-gordon.md` to `12-ai-assisted-docker-gordon.md` and update sidebar_position to 12
- [ ] T005 Rename `09-capstone-production-ready-agent.md` to `13-capstone-production-ready-agent.md` and update sidebar_position to 13
- [ ] T006 Rename `10-building-production-dockerfile-skill.md` to `14-building-production-dockerfile-skill.md` and update sidebar_position to 14

## Phase 3: New Content Creation (Parallel)

Create 4 new L1 lessons. All can run in parallel.

- [ ] T007 [P] Create Lesson 6: Docker Networking Fundamentals at `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/06-docker-networking-fundamentals.md`
- [ ] T008 [P] Create Lesson 7: Container-to-Container Communication at `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/07-container-to-container-communication.md`
- [ ] T009 [P] Create Lesson 8: Volumes and Persistent Data at `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/08-volumes-persistent-data.md`
- [ ] T010 [P] Create Lesson 9: Docker Engine Architecture at `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/09-docker-engine-architecture.md`

## Phase 4: README Update

- [ ] T011 Update Docker chapter README.md with 14-lesson structure

## Phase 5: Validation

- [ ] T012 Run constitutional validation checks on all 4 new lessons (framework invisibility, evidence presence, proper endings)

---

## Execution Notes

### Parallel Content Creation (T007-T010)

**Pre-launch checklist**:
- [ ] Each prompt specifies exact absolute output path
- [ ] Each prompt includes "Execute autonomously without waiting for confirmation"
- [ ] Each prompt includes "DO NOT create new directories"
- [ ] Target directory verified with `ls`

### File Renaming Strategy (T002-T006)

Use `git mv` to preserve history:
```bash
git mv old-name.md new-name.md
```

Then update `sidebar_position` in frontmatter.

### Validation Commands (T012)

```bash
# Check for exposed framework labels (must be 0 matches)
grep -rE "Part [0-9]:|AI as Teacher|AI as Student|Your Role:|What you learned:" *.md

# Check proper endings (must show "Try With AI")
for f in 0[6-9]-*.md; do tail -30 "$f" | grep -E "^## " | tail -1; done

# Check code has output
for f in 0[6-9]-*.md; do echo "$f:"; grep -c '```' "$f"; grep -c '\*\*Output:\*\*' "$f"; done
```
