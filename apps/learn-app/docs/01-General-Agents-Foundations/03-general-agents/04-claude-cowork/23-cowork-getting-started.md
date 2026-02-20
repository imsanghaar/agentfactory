---
slug: /General-Agents-Foundations/general-agents/cowork-getting-started
title: "Getting Started with Cowork"
sidebar_position: 23
chapter: 3
lesson: 23
duration_minutes: 20
chapter_type: Practical
running_example_id: cowork-setup

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on setup of Claude Cowork including subscription requirements, installation, and first task execution"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Claude Cowork Setup and Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can successfully set up Claude Cowork, grant folder access, and complete a basic file manipulation task"

learning_objectives:
  - objective: "Set up Claude Cowork including subscription requirements and Desktop app installation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful Cowork installation and first task execution"
  - objective: "Grant and manage folder access permissions safely"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Demonstration of proper folder access workflow"
  - objective: "Navigate the Cowork interface (conversation panel, execution panel, artifacts)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation of interface components"
  - objective: "Complete a first Cowork task end-to-end"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful execution of file organization or document task"

# Cognitive load tracking
cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (subscription tiers, Desktop app, folder permissions, interface panels, approval workflow, artifacts, task execution) - within A2 limit of 7 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Explore creating dedicated workspaces for different projects and setting up project-specific contexts"
  remedial_for_struggling: "Focus only on granting folder access and completing one simple file operation"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2025-01-22"
last_modified: "2025-01-22"
git_author: "Claude Code"
workflow: "manual"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Completion of Lesson 22: From Terminal to Desktop"
  - "macOS computer (Windows support coming soon)"
  - "Anthropic subscription (Pro or Max required for Cowork)"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 8
  session_title: "Cowork Desktop Environment and Browser Integration"
  key_points:
    - "Folder access is the critical security boundary -- Claude can only access explicitly approved folders, and students should start with a dedicated test folder, not their home directory"
    - "The three interface panels (conversation, execution, artifacts) serve distinct purposes: communicate, observe actions, and review results"
    - "The approval workflow table shows that reads are automatic but all writes, modifications, deletions, and moves require explicit confirmation"
    - "The first task (organizing a messy folder) demonstrates the full propose-approve-execute cycle without requiring any code"
  misconceptions:
    - "Students grant access to their entire home directory for convenience -- the best practices section specifically warns against this and recommends dedicated workspace folders"
    - "Students think Cowork mode is always on -- they need to explicitly switch from Chat mode to Cowork mode, and the folder access panel confirms which mode is active"
    - "Students expect Cowork to work on Windows -- the requirements table states macOS only with Windows support in development, which may cause frustration for some"
  discussion_prompts:
    - "The approval workflow requires confirmation for writes but not reads. Why is this asymmetry the right default? When might you want reads to require approval too?"
    - "Compare the folder access permission model to how you grant app permissions on your phone. What design principles are shared?"
  teaching_tips:
    - "Have students create the test folder with the provided bash commands before class so setup does not consume session time"
    - "Walk through the approval workflow table as a security exercise: for each operation type, ask students what could go wrong without approval"
    - "If Windows users are in the class, pair them with macOS users for live demonstrations, and use the troubleshooting section to set expectations"
    - "Use the 'Common First Tasks' table as a choose-your-own-adventure: let each student pick one task that matches their daily work and try it live"
  assessment_quick_check:
    - "Name the three panels in the Cowork interface and describe what each shows during a file organization task"
    - "Which operations require approval in Cowork and which do not? Explain the security reasoning"
    - "What is the first troubleshooting step if Cowork mode does not appear in Claude Desktop?"
---

# Getting Started with Cowork

Claude Cowork transforms how you work with documents and files. But before you can organize folders, analyze spreadsheets, or generate reports, you need to set up the environment. Let's get started.

---

## Requirements

Before you begin, ensure you have:

| Requirement        | Details                                              |
| ------------------ | ---------------------------------------------------- |
| **Subscription**   | Claude Pro or Max (free tier doesn't include Cowork) |
| **Platform**       | macOS (Windows support in development)               |
| **Claude Desktop** | Latest version from claude.ai/download               |
| **Work to do**     | Documents, files, or data you want to work with      |

**Why the subscription requirement?** Cowork's agentic capabilities—filesystem access, document processing, persistent context—require significant infrastructure. The Pro and Max tiers support this enhanced functionality.

---

## Installation Steps

### Step 1: Install Claude Desktop

1. Visit claude.ai/download
2. Download the Claude Desktop app for macOS
3. Install and launch the application
4. Sign in with your Anthropic account (Pro or Max)

The Desktop app is your gateway to Cowork. Unlike the web interface, it has direct access to your filesystem with your permission.

### Step 2: Enable Cowork Mode

In Claude Desktop, you'll see options for different interaction modes:

- **Chat mode**: Standard conversation (web-like behavior)
- **Cowork mode**: Agentic mode with filesystem access

Switch to Cowork mode when you want Claude to work with files. You'll know you're in Cowork mode when you see the folder access panel.

### Step 3: Grant Folder Access

The first time you use Cowork, Claude will ask for folder access. This is a critical security boundary—Claude can only access folders you explicitly approve.

**To grant access:**

1. Click the "Grant Access" or "Choose Folder" button
2. Navigate to the folder you want to work with
3. Confirm the access request

**Best practices for folder access:**

- Create a dedicated workspace folder for Cowork projects
- Don't grant access to sensitive system directories
- Start with a specific project folder, not your entire home directory
- Revoke access when you're done with sensitive work

---

## The Cowork Interface

When you're in Cowork mode, the interface has three main sections:

### Conversation Panel

Where you communicate with Claude. This works like standard chat, but with enhanced context awareness:

- Claude knows about files in your approved folders
- Previous conversations in the session inform context
- You can reference files by name without uploading

### Execution Panel

Shows what Claude is actually doing:

- Files being read or written
- Operations in progress
- Warnings or errors

This is your visibility into Claude's actions. You see exactly what will change before it happens.

### Artifacts Panel

Where Claude presents results:

- Generated documents
- Analysis results
- Created files

You can preview, download, or open artifacts directly from this panel.

---

## Your First Cowork Task

Let's put Cowork to work with a practical first task: organizing a messy folder.

**Setup:** Create a test folder with some disorganized files:

```bash
mkdir -p ~/test-cowork
cd ~/test-cowork
# Create some messy test files
touch "document 1.txt" "REPORT final.docx" "image.JPG" "notes (1).txt" "data (2).csv"
```

**Task:** In Claude Cowork, grant access to `~/test-cowork` and ask:

> "Organize these files by type: put all text files in a 'docs' folder, all Word documents in an 'office' folder, and all images in an 'images' folder. Use consistent naming."

**What happens:**

1. Claude reads the directory to see what files exist
2. Claude proposes an organization plan in the Execution Panel
3. You review and approve the plan
4. Claude creates folders and moves files
5. Claude confirms completion

**Why this matters:** You didn't write any code. You described what you wanted, and Claude executed it safely with your approval.

---

## Understanding the Approval Workflow

Cowork doesn't execute blindly. Every significant operation requires your approval:

| Operation Type        | Requires Approval | Example                               |
| --------------------- | ----------------- | ------------------------------------- |
| Read files            | No                | Claude reads to understand context    |
| Create new files      | Yes               | Claude shows what will be created     |
| Modify existing files | Yes               | Claude shows diff or summary          |
| Delete files          | Yes               | Claude asks for explicit confirmation |
| Move/rename files     | Yes               | Claude shows before/after paths       |

This approval workflow is your safety net. Claude proposes, you approve, then Claude acts.

---

## Working with Documents

Cowork shines when working with document formats. Try this:

**Task:** Create a simple Word document with structured content.

> "Create a Word document called 'project-plan.docx' with these sections: Overview, Timeline, Budget, and Team. Add placeholder content for each section."

Claude will:

1. Create the .docx file
2. Add the section headers
3. Generate relevant placeholder content
4. Show you the result in the Artifacts panel

You can then open the document in Word to see a properly formatted file—not just text, but actual document structure.

---

## Common First Tasks

After completing the initial setup, try these tasks to explore Cowork's capabilities:

| Task                  | Prompt                                                                                        | What You'll Learn             |
| --------------------- | --------------------------------------------------------------------------------------------- | ----------------------------- |
| **Batch rename**      | "Rename all files in this folder to use YYYY-MM-DD format based on their creation date"       | Pattern-based file operations |
| **Document summary**  | "Read all the .txt files in this folder and summarize the key points from each"               | Multi-document analysis       |
| **Format conversion** | "Convert this Word document to a plain text file while preserving the structure"              | Document format handling      |
| **File cleanup**      | "Find all duplicate files in this folder (by content) and move them to a 'duplicates' folder" | Advanced file operations      |

---

## Safety Tips

As you start using Cowork, keep these safety principles in mind:

1. **Start Small**: Begin with a test folder, not your important documents
2. **Review Carefully**: Always read the execution plan before approving
3. **Backup First**: Cowork is powerful—back up important data before major operations
4. **Revoke Access**: Remove folder permissions when you're done with a project
5. **Watch the Panel**: Keep an eye on the Execution Panel to understand what Claude is doing

---

## Troubleshooting

**Issue: Cowork mode doesn't appear**

- Ensure you're on Pro or Max subscription
- Update Claude Desktop to the latest version
- Sign out and sign back in

**Issue: Folder access denied**

- Check macOS Privacy Settings (System Settings > Privacy & Security > Files and Folders)
- Grant Claude Desktop permission to access the location
- Try granting access to a more specific folder

**Issue: Operations are slow**

- Large folders take time to scan—be patient with the initial read
- Complex operations (like analyzing hundreds of files) may take time
- Check the Execution Panel for progress information

---

## Try With AI

\*\*🔍 Explore Your Environment:"

> "I want to use Claude Cowork for [specific task]. What folder structure should I set up? What files do I need? Help me plan the workspace before I start."

**What you're learning:** Workspace design—thinking through how to organize your work for effective AI collaboration. Good workspace design makes Cowork more effective.

\*\*💡 Test the Limits:"

> "Give Claude a moderately complex task in your test folder: something that would take you 10-15 minutes manually. Compare the time, accuracy, and effort. What did Claude do well? What would you change?"

**What you're learning:** Capability assessment—understanding what Cowork excels at and where human oversight still matters. This helps you choose the right tasks for automation.

\*\*🏗️ Design Your Workflow:"

> "Based on how I work, describe a weekly routine where Claude Cowork would save me time. When would I use it? What tasks would I delegate? What would I still do manually?"

**What you're learning:** Process integration—thinking about how AI fits into your existing workflow rather than replacing it entirely. The most effective automation enhances, not replaces.

---

## What's Next

Now that you're set up, the next lessons explore practical workflows: organizing files, processing documents, integrating with browsers, and using connectors. You'll see Cowork handle real-world tasks that save hours of manual work.
