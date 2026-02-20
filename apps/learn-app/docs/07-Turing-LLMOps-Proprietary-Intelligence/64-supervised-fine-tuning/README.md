---
sidebar_position: 64
title: "Chapter 64: Supervised Fine-Tuning (SFT)"
description: "Build your fine-tuning skill first, then master LoRA/QLoRA training with Unsloth on Colab T4"
---

# Chapter 64: Supervised Fine-Tuning (SFT)

You build a `fine-tuning` skill first, then train models with LoRA/QLoRA (Unsloth) on Colab T4. The Task API dataset from Chapter 63 powers your first supervised run.

---

## Goals

- Prepare and load SFT datasets for instruction-style tasks
- Run LoRA/QLoRA fine-tuning with Unsloth on Colab/GPU
- Evaluate checkpoints and manage artifacts
- Capture repeatable prompts and configs in a fine-tuning skill

---

## Lesson Progression

- Build the fine-tuning skill
- Dataset formatting/validation for SFT
- LoRA/QLoRA training runs with Unsloth
- Checkpoint evaluation and export
- Capstone: trained Task API model; finalize the skill

---

## Outcome & Method

You finish with a trained SFT model for the Task API and a reusable fine-tuning skill for future datasets.

---

## Prerequisites

- Chapters 61-63 (strategy, architecture, data)
- Python/Colab access with GPU
