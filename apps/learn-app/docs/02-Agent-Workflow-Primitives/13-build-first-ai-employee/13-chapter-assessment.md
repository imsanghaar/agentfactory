---
sidebar_position: 13
title: "Chapter Assessment"
sidebar_label: "L13: Assessment"
description: "Validate your Personal AI Employee knowledge with a comprehensive quiz covering skills, subagents, MCP, watchers, HITL, and autonomous operations."
keywords:
  - chapter quiz
  - assessment
  - Personal AI Employee
  - Digital FTE
  - skills
  - subagents
  - MCP
chapter: 10
lesson: 13
duration_minutes: 20

# Generation metadata
teaching_guide:
  lesson_type: "supplementary"
  session_group: 5
  session_title: "Chapter Assessment"
  key_points:
    - "The assessment validates understanding across all three tiers — Bronze (skills, subagents, MCP), Silver (watchers, HITL, scheduling), Gold (error recovery, audit logging)"
    - "Questions test both conceptual understanding (when to use skills vs subagents) and practical application (design an approval workflow for a scenario)"
    - "The hackathon submission requires 5 deliverables: repo, README, demo video, tier declaration, and security disclosure"
  misconceptions:
    - "Students think they must complete Gold Tier to pass the assessment — Bronze questions (1-10) are the foundation; Silver and Gold are extensions"
    - "Students confuse the assessment with the hackathon submission — the quiz tests knowledge, the submission demonstrates working implementation"
    - "Students assume the demo video must be polished — a 5-10 minute screen recording walking through key features is sufficient"
  discussion_prompts:
    - "Which tier did you target and why? What would change your decision if you could start over?"
    - "What was the most surprising concept in this chapter — something you did not expect when you started?"
  teaching_tips:
    - "Use the Bronze questions (1-10) as a review session before the quiz — they cover the most testable concepts from L01-L07"
    - "The submission guidelines double as a project checklist — have students self-evaluate against each requirement before submitting"
    - "This is a placeholder quiz — direct students to review L00 spec and each lesson's key concepts as preparation"
  assessment_quick_check:
    - "What are the 5 hackathon submission deliverables?"
    - "Which tier concepts does each question block cover? (1-10 Bronze, 11-16 Silver, 17-20 Gold)"

generated_by: "placeholder - to be implemented"
created: "2026-01-07"
version: "0.1.0"
---

# Chapter 6 Assessment

## Overview

This assessment validates your understanding of the Personal AI Employee architecture across all three tiers.

**Format:** 20 questions covering Bronze, Silver, and Gold tier concepts.

**Passing Score:** 80% (16/20 correct)

---

## Bronze Tier Questions (1-10)

Questions covering:
- Vault structure and governance (AGENTS.md, CLAUDE.md)
- Skill creation and SKILL.md format
- Subagent architecture and when to use skills vs subagents
- MCP integration and Gmail tools
- Orchestration patterns

## Silver Tier Questions (11-16)

Questions covering:
- Watcher architecture and BaseWatcher pattern
- Human-in-the-Loop approval workflows
- Permission boundaries and sensitive actions
- Process management with cron and PM2
- CEO Briefing structure

## Gold Tier Questions (17-20)

Questions covering:
- Cross-domain integration patterns
- Error recovery and graceful degradation
- Audit logging requirements
- Ethics and responsible automation

---

## Coming Soon

Full quiz with 20 questions will be added here.

---

## Submission Guidelines

If participating in the Personal AI Employee Hackathon:

1. **Repository**: Public GitHub repo (or private with judge access)
2. **README.md**: Setup instructions and architecture overview
3. **Demo Video**: 5-10 minute walkthrough of key features
4. **Tier Declaration**: State Bronze, Silver, or Gold tier
5. **Security Disclosure**: How credentials are handled

See [L00: Complete Specification](./00-personal-ai-employee-specification.md) for full submission requirements.
