---
sidebar_position: 9
title: "Trust But Verify"
sidebar_label: "L09: Trust But Verify"
description: "Implement Human-in-the-Loop approval workflows that prevent your AI employee from taking sensitive actions without explicit permission."
keywords:
  - Human-in-the-Loop
  - HITL
  - approval workflow
  - permission boundaries
  - sensitive actions
  - governance
chapter: 10
lesson: 9
duration_minutes: 30
tier: "Silver"

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "Understanding permission boundaries, approval request format"
layer_2_collaboration: "Designing approval workflows with AI assistance"
layer_3_intelligence: "N/A (governance pattern, not intelligence)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Approval Request Format"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can create properly formatted approval request files"
  - name: "Permission Boundaries"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can define appropriate thresholds for auto-approve vs require-approval"
  - name: "Folder-Based Workflow"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can implement /Pending_Approval/ → /Approved/ workflow"

learning_objectives:
  - objective: "Design approval request file format with all necessary metadata"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Approval request file contains action, amount, recipient, expiry"
  - objective: "Define permission boundaries for different action categories"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Permission table covers email, payments, social, file operations"
  - objective: "Implement folder-based approval workflow"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Files move from /Pending_Approval/ to /Approved/ or /Rejected/"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (approval requests, permission boundaries, folder workflow)"

differentiation:
  extension_for_advanced: "Add expiry handling and escalation rules"
  remedial_for_struggling: "Start with single action type (emails only)"

teaching_guide:
  lesson_type: "core"
  session_group: 4
  session_title: "Human-in-the-Loop Safety"
  key_points:
    - "HITL is a safety pattern, not a limitation — it prevents the AI Employee from taking irreversible actions (payments, public posts) without explicit human sign-off"
    - "Folder-based workflow (/Pending_Approval/ → /Approved/ or /Rejected/) uses the same file-based communication pattern as watchers writing to /Needs_Action/"
    - "Permission boundaries define WHAT auto-approves vs WHAT requires human review — this is the governance layer that makes autonomous operation trustworthy"
    - "This lesson complements L08 (Watchers) — watchers make the employee proactive, HITL makes that proactivity safe"
  misconceptions:
    - "Students think HITL means the AI is not trusted — it means the AI is trusted for routine tasks but sensitive actions get human review, like any real employee"
    - "Students assume all actions need approval — the permission boundaries table explicitly defines auto-approve thresholds (e.g., emails to known contacts auto-approve)"
    - "Students confuse /Pending_Approval/ with /Needs_Action/ — Needs_Action is for incoming items detected by watchers, Pending_Approval is for outgoing actions awaiting sign-off"
    - "Students think moving files between folders is primitive — file-based workflows are visible, auditable, and work with any tool (Obsidian, CLI, scripts)"
  discussion_prompts:
    - "The L00 spec says payments under $50 to recurring payees auto-approve. Where would YOU set the threshold for your business, and why?"
    - "Why does the approval request include an expiry field? What should happen when an approval request expires?"
    - "The lesson says 'trust your employee with routine tasks.' How do you decide what is routine vs sensitive in your domain?"
  teaching_tips:
    - "Start by reviewing the permission boundaries table from L00 — students need to see the full picture before building individual approval workflows"
    - "Have students design their OWN permission boundaries for their domain before looking at the provided ones — this makes the pattern personally relevant"
    - "Demo the folder workflow physically: create a file in /Pending_Approval/, then move it to /Approved/ and show what happens next"
    - "This is a placeholder lesson — direct students to L00 spec sections on HITL Pattern and Permission Boundaries for full detail until implementation is complete"
  assessment_quick_check:
    - "What are the three folders in the approval workflow, and what does each represent?"
    - "Give two examples of actions that should auto-approve and two that should always require human review"
    - "What is the difference between /Needs_Action/ (from L08) and /Pending_Approval/ (this lesson)?"

# Generation metadata
generated_by: "placeholder - to be implemented"
created: "2026-01-07"
version: "0.1.0"
---

# Trust But Verify

:::info Silver Tier Lesson
This lesson is part of the **Silver Tier**. Complete Bronze Tier (L01-L07) first.
:::

## Coming Soon

This lesson will teach you to implement **Human-in-the-Loop (HITL)** approval workflows that prevent your AI employee from taking sensitive actions without your explicit permission.

**What You'll Build:**
- Approval request file format with metadata
- Permission boundaries table (what auto-approves vs requires human)
- Folder-based workflow: `/Pending_Approval/` → `/Approved/` or `/Rejected/`

**Key Concept:** Trust your employee with routine tasks, but require sign-off for anything with real consequences (payments, new contacts, public posts).

---

## Placeholder Content

See [L00: Complete Specification](./00-personal-ai-employee-specification.md) for the full HITL architecture.

**Reference sections:**
- "Human-in-the-Loop Pattern"
- "Permission Boundaries"
- "Approval Request Format"
