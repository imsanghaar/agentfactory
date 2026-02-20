---
sidebar_position: 8
title: "Your Employee's Senses"
sidebar_label: "L08: Employee's Senses"
description: "Build Python Watcher scripts that monitor Gmail and filesystem for changes, creating the perception layer that makes your employee proactive instead of reactive."
keywords:
  - Python Watchers
  - Gmail Watcher
  - File Watcher
  - perception layer
  - autonomous agent
  - event-driven
chapter: 10
lesson: 8
duration_minutes: 45
tier: "Silver"

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2 to Layer 3"
layer_progression: "L2 (AI Collaboration) → L3 (Intelligence Design)"
layer_1_foundation: "Understanding daemon processes, polling patterns, file system events"
layer_2_collaboration: "Using AI to write and refine watcher scripts"
layer_3_intelligence: "Creating reusable watcher patterns for any data source"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "BaseWatcher Pattern"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can implement BaseWatcher abstract class"
  - name: "Gmail API Integration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can poll Gmail API for new messages"
  - name: "File System Monitoring"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can use watchdog library to monitor folder changes"

learning_objectives:
  - objective: "Implement BaseWatcher abstract class for consistent watcher pattern"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Working BaseWatcher with abstract methods"
  - objective: "Build Gmail Watcher that detects new important emails"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Gmail Watcher creates .md files in /Needs_Action/"
  - objective: "Build File Watcher for drop folder monitoring"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "File Watcher triggers on new files in drop folder"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (daemon processes, polling, file events, BaseWatcher, action files)"

differentiation:
  extension_for_advanced: "Add WhatsApp Watcher using Playwright"
  remedial_for_struggling: "Start with File Watcher only (simpler than Gmail API)"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Perception Layer - Watchers"
  key_points:
    - "Watchers solve the 'lazy agent' problem — without them, the AI Employee only works when you type a command; with them, it notices things on its own"
    - "BaseWatcher abstract class enforces a consistent pattern (check_for_updates, create_action_file, run) across all data sources"
    - "Watchers create .md files in /Needs_Action/ — this file-based communication is the bridge between the Perception layer and the Reasoning layer from L00's architecture"
    - "This is the first Silver tier lesson — it marks the transition from human-triggered to event-triggered AI operation"
  misconceptions:
    - "Students think watchers ARE Claude Code — watchers are lightweight Python scripts that TRIGGER Claude Code by writing files to the vault"
    - "Students expect watchers to process emails — watchers only DETECT and DEPOSIT; Claude Code reads /Needs_Action/ and does the reasoning"
    - "Students think polling is inefficient — for personal use, polling every 60 seconds is perfectly adequate and simpler than webhooks or push notifications"
    - "Students assume watchers require the vault to be open in Obsidian — watchers write directly to the filesystem; Obsidian is just a UI for viewing"
  discussion_prompts:
    - "The spec shows Gmail, WhatsApp, and File watchers. What other data sources in YOUR work would benefit from a watcher? What would the action file contain?"
    - "Why does the architecture use file-based communication (/Needs_Action/ folder) instead of direct API calls between watchers and Claude Code?"
    - "The watcher runs in an infinite loop with a sleep interval. What are the tradeoffs of a 30-second vs 5-minute polling interval?"
  teaching_tips:
    - "Start with FileWatcher (simpler, no API credentials) before attempting GmailWatcher — students gain confidence with the pattern before adding complexity"
    - "Demo the watcher creating a file in /Needs_Action/ and then show Claude Code reading it — the visual connection between perception and reasoning is powerful"
    - "Emphasize that this is a placeholder lesson — direct students to L00 spec for full watcher architecture and code patterns until implementation is complete"
    - "Connect back to L01's MCP setup — watchers running from outside the vault use Obsidian MCP to access the Memory Bank, which is why that setup was essential"
  assessment_quick_check:
    - "Name the three methods every BaseWatcher must implement and explain what each does"
    - "What file does a watcher create when it detects a new email, and where does it go?"
    - "Why do watchers need Obsidian MCP from L01? (They run from outside the vault directory)"

# Generation metadata
generated_by: "placeholder - to be implemented"
created: "2026-01-07"
version: "0.1.0"
---

# Your Employee's Senses

:::info Silver Tier Lesson
This lesson begins the **Silver Tier**. Complete Bronze Tier (L01-L07) first.
:::

## Coming Soon

This lesson will teach you to build **Python Watcher scripts** that give your Personal AI Employee the ability to perceive changes in the world — transforming it from reactive (waits for you) to proactive (notices things itself).

**What You'll Build:**

- `BaseWatcher` abstract class (consistent pattern for all watchers)
- `GmailWatcher` that polls Gmail API for urgent messages
- `FileWatcher` that monitors a drop folder for new files

**Key Concept:** Watchers create `.md` files in `/Needs_Action/` that trigger Claude Code to reason and act.

---

## Placeholder Content

See [L00: Complete Specification](./00-personal-ai-employee-specification.md) for the full Watcher architecture and code patterns.

**Reference sections:**

- "Perception (The Watchers)"
- "Watcher Architecture"
- "Core Watcher Pattern"
- "Gmail Watcher Implementation"
- "File System Watcher"
