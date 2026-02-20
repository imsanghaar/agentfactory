---
sidebar_position: 10
title: "Always On Duty"
sidebar_label: "L10: Always On Duty"
description: "Configure your AI employee to run 24/7 using cron for scheduled tasks, PM2 for process management, and watchdog patterns for error recovery."
keywords:
  - cron
  - PM2
  - process management
  - watchdog
  - daemon process
  - always-on
  - scheduled tasks
chapter: 10
lesson: 10
duration_minutes: 35
tier: "Silver"

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1 to Layer 2"
layer_progression: "L1 (Manual Foundation) → L2 (AI Collaboration)"
layer_1_foundation: "Understanding cron syntax, PM2 basics, process lifecycle"
layer_2_collaboration: "Using AI to configure schedules and troubleshoot process issues"
layer_3_intelligence: "N/A (operations, not intelligence)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Cron Scheduling"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can write cron expressions for daily/weekly tasks"
  - name: "PM2 Process Management"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can start, monitor, and persist processes with PM2"
  - name: "Watchdog Pattern"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can implement health check and auto-restart logic"

learning_objectives:
  - objective: "Configure cron jobs for scheduled Claude Code tasks"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Cron entry triggers daily briefing at 8 AM"
  - objective: "Use PM2 to keep Watcher processes running persistently"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Watchers survive terminal close and system reboot"
  - objective: "Implement watchdog for process health monitoring"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Watchdog detects crashed process and restarts it"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (cron, PM2, watchdog, persistence)"

differentiation:
  extension_for_advanced: "Add Slack/email alerts for process failures"
  remedial_for_struggling: "Start with cron only (simpler than PM2)"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 4
  session_title: "Operations - Always-On Infrastructure"
  key_points:
    - "A true Digital FTE does not stop working when you close your laptop — cron handles scheduled tasks, PM2 keeps watchers alive, watchdog monitors health"
    - "Cron is for scheduled operations (daily briefing at 8 AM), PM2 is for continuous operations (watchers that run forever) — students must understand this distinction"
    - "PM2's 'pm2 save && pm2 startup' command pair is the key to surviving system reboots — without it, processes die on restart"
    - "This lesson completes the Silver tier infrastructure: L08 (Perception) + L09 (Safety) + L10 (Persistence) enable autonomous 24/7 operation"
  misconceptions:
    - "Students think cron and PM2 do the same thing — cron runs tasks at specific times then exits, PM2 keeps long-running processes alive continuously"
    - "Students assume PM2 prevents all crashes — PM2 restarts crashed processes, but the watchdog pattern adds health checks to detect silent failures (process running but not working)"
    - "Students think always-on requires a server — for personal use, their laptop or a mini-PC running PM2 is sufficient; cloud VMs are optional"
    - "Students skip 'pm2 startup' and wonder why processes disappear after reboot — this is the most common setup error"
  discussion_prompts:
    - "The spec shows the CEO Briefing runs every Sunday night. What scheduled tasks would benefit YOUR workflow, and what cron expression would trigger them?"
    - "What is the difference between a process that crashes (PM2 restarts it) and a process that hangs (watchdog detects it)? Why do you need both?"
    - "If you had to choose between scheduled operations (cron) and continuous operations (PM2/watchers) for your first deployment, which would deliver more value?"
  teaching_tips:
    - "This is a placeholder lesson — direct students to L00 spec sections on Operations and Process Management for full patterns until implementation is complete"
    - "Cron syntax is notoriously confusing — use crontab.guru as a live reference tool during class"
    - "Demo PM2 status output to show students what a managed process looks like — 'pm2 list' output is more meaningful than abstract descriptions"
    - "Connect to L08: the GmailWatcher from L08 is the primary candidate for PM2 management — show how they integrate"
  assessment_quick_check:
    - "Write a cron expression for 'every day at 8 AM' and explain each field"
    - "What two PM2 commands make a process survive a system reboot?"
    - "What is the difference between cron (scheduled) and PM2 (continuous) operation?"

# Generation metadata
generated_by: "placeholder - to be implemented"
created: "2026-01-07"
version: "0.1.0"
---

# Always On Duty

:::info Silver Tier Lesson
This lesson is part of the **Silver Tier**. Complete Bronze Tier (L01-L07) first.
:::

## Coming Soon

This lesson will teach you to configure your AI employee to run **24/7** — surviving terminal closes, system reboots, and process crashes.

**What You'll Build:**
- Cron jobs for scheduled tasks (daily briefing at 8 AM)
- PM2 configuration for persistent Watcher processes
- Watchdog script for health monitoring and auto-restart

**Key Concept:** A true Digital FTE doesn't stop working when you close your laptop.

---

## Placeholder Content

See [L00: Complete Specification](./00-personal-ai-employee-specification.md) for operations patterns.

**Reference sections:**
- "Continuous vs Scheduled Operations"
- "Why Watchers Need Process Management"
- "Watchdog Process"
- "Error States & Recovery"
