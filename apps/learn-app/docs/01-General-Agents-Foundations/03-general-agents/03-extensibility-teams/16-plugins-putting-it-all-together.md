---
slug: /General-Agents-Foundations/general-agents/plugins-putting-it-all-together
title: "Plugins: Discover and Install"
sidebar_position: 16
chapter: 3
lesson: 16
duration_minutes: 12

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "N/A"
layer_2_collaboration: "AI helps discover appropriate plugins for workflow needs, student evaluates plugin fit"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Discovering and Installing Claude Code Plugins"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can browse the plugin marketplace, install plugins, and use installed plugin commands"
  - name: "Packaging Claude Code Plugins"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can package existing skills into a plugin with valid manifest"

learning_objectives:
  - objective: "Browse the official plugin marketplace using /plugin"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful navigation of Discover tab and plugin details"
  - objective: "Install a plugin from the official marketplace"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful installation of commit-commands or another plugin"
  - objective: "Use an installed plugin's commands"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Execution of plugin command like /commit-commands:commit"
  - objective: "Understand what plugins bundle (skills, agents, hooks, MCP)"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of plugin components"
  - objective: "Package existing skills, hooks, and agents into a distributable plugin"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful creation of plugin.json and plugin structure"
  - objective: "Create a plugin marketplace and share with others"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful marketplace creation and distribution"

# Cognitive load tracking
cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (plugin marketplace, Discover tab, installation scopes, plugin commands, plugin structure, marketplace distribution) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Add third-party marketplaces; explore plugin manifest structure"
  remedial_for_struggling: "Focus on installing and using one plugin before exploring categories"

# Generation metadata
generated_by: "content-implementer v1.0.0"
source_spec: "specs/029-chapter-5-refinement/spec.md"
created: "2025-01-17"
last_modified: "2026-01-19"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "3.0.0"

teaching_guide:
  lesson_type: "core"
  session_group: 5
  session_title: "Settings, Hooks, and Plugin Synthesis"
  key_points:
    - "A plugin bundles skills, commands, agents, hooks, and MCP servers into one installable package — students must understand it is a packaging format, not a new concept"
    - "The official Anthropic marketplace is pre-configured; students can browse with /plugin immediately without any setup"
    - "Installation scope matters: User scope follows you everywhere, Project scope shares with team, Local scope is just you on this repo"
    - "Students create their own plugin by adding a .claude-plugin/plugin.json manifest (4 required fields) and a marketplace.json for distribution"
  misconceptions:
    - "Students think plugins are a separate system from skills and hooks — actually plugins just bundle the same components they already know into distributable packages"
    - "Students confuse plugin (a folder with capabilities) with marketplace (a catalog listing multiple plugins) — the app vs app-store distinction"
    - "Students assume creating a plugin requires coding — the minimum plugin.json has only 4 fields: name, description, version, author"
    - "Students expect all marketplace plugins to work out of the box — LSP plugins require language server binaries installed on the system"
  discussion_prompts:
    - "You have skills, hooks, and an MCP config that work well together in your project. What would change if you packaged them as a plugin versus keeping them as loose files?"
    - "When should you install an existing plugin versus building a custom skill? What is your decision threshold?"
  teaching_tips:
    - "Have students run /plugin before any explanation — seeing the marketplace UI first makes the concept concrete before the theory"
    - "Use the commit-commands install exercise as the demonstration: it takes under 2 minutes and shows the full install-use cycle"
    - "Walk through the plugin directory structure diagram carefully — students need to know that components go at root level, not inside .claude-plugin/"
    - "Connect the three installation scopes back to Lesson 14's settings hierarchy — same user/project/local pattern, reinforcing the mental model"
  assessment_quick_check:
    - "What are the 4 required fields in a plugin.json manifest?"
    - "What is the difference between User scope and Project scope when installing a plugin?"
    - "If an LSP plugin says 'Executable not found' after installation, what is the most likely cause?"

# Legacy compatibility
prerequisites:
  - "Lessons 01-15: Claude Code features including skills, subagents, hooks, settings"
---

# Plugins: Discover and Install

You've learned to create skills, configure hooks, and use subagents. But what if someone has already built exactly what you need?

---

## What Are Plugins?

A **plugin** bundles multiple Claude Code components into one installable package:

| Component       | What It Does                                        |
| --------------- | --------------------------------------------------- |
| **Skills**      | Autonomous capabilities Claude discovers and uses   |
| **Commands**    | Slash commands like `/commit-commands:commit`       |
| **Agents**      | Specialized subagents for focused tasks             |
| **Hooks**       | Event automation (format on save, validate on edit) |
| **MCP servers** | External integrations (GitHub, Slack, etc.)         |

**Think of plugins as**: Complete capability packages. Instead of manually setting up skills, hooks, agents, and MCP servers separately, you install one plugin and everything works together.

---

## Why Use Plugins?

**Without plugins**, adding GitHub integration means:

1. Find an MCP server for GitHub
2. Configure it in your settings
3. Maybe create skills to use it well
4. Maybe add hooks for automation
5. Test everything works together

**With plugins**, you run:

```
/plugin install github@claude-plugins-official
```

Done. GitHub integration works—including MCP config, any bundled skills, and automation hooks.

**The principle**: Check what exists before building from scratch.

---

## You Already Have a Plugin Marketplace

Run this command in Claude Code right now:

```
/plugin
```

**What you'll see**:

```
│ Plugin Manager                                                                       │
│                                                                                      │
│   Discover   │   Installed   │   Marketplaces   │   Errors                          │
│                                                                                      │
│   Code intelligence                                                                  │
│   ❯ typescript-lsp - TypeScript/JavaScript language server                          │
│     python-lsp - Python language server (Pyright)                                   │
│     rust-analyzer-lsp - Rust language server                                        │
│     gopls-lsp - Go language server                                                  │
│                                                                                      │
│   External integrations                                                              │
│     github - GitHub integration                                                      │
│     slack - Slack integration                                                        │
│     linear - Linear project management                                               │
│                                                                                      │
│   Development workflows                                                              │
│     commit-commands - Git commit workflows                                           │
│     pr-review-toolkit - Pull request review agents                                   │
```

The **official Anthropic marketplace** is automatically available. No setup needed.

Use **Tab** to switch between tabs:

- **Discover**: Browse available plugins
- **Installed**: See what you've installed
- **Marketplaces**: Manage plugin sources
- **Errors**: Debug plugin issues

---

## Try It Now: Install Your First Plugin

Let's install **commit-commands**—a plugin that helps with git workflows.

### Option 1: Use the UI

1. Run `/plugin`
2. Go to the **Discover** tab
3. Find **commit-commands** under "Development workflows"
4. Press **Enter** to see details
5. Choose **User scope** (available in all projects)

### Option 2: Install Directly

```
/plugin install commit-commands@claude-plugins-official
```

**What happens**:

- Plugin downloads and installs
- New commands become available immediately
- Plugin appears in your **Installed** tab

---

## Try It Now: Use Your New Plugin

After installing **commit-commands**, make a small change to any file, then run:

```
/commit-commands:commit
```

**What happens**:

1. Plugin stages your changes
2. Generates a commit message based on the diff
3. Creates the commit

**That's it!** You just extended Claude Code with one command.

---

## What's in the Official Marketplace?

| Category                  | Plugins                                                          | What They Do                                          |
| ------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| **Code intelligence**     | `typescript-lsp`, `python-lsp`, `rust-analyzer-lsp`, `gopls-lsp` | Jump to definitions, find references, see type errors |
| **External integrations** | `github`, `gitlab`, `slack`, `linear`, `notion`, `figma`         | Connect to external services                          |
| **Development workflows** | `commit-commands`, `pr-review-toolkit`, `plugin-dev`             | Git workflows, PR reviews, plugin creation            |
| **Output styles**         | `explanatory-output-style`, `learning-output-style`              | Customize how Claude responds                         |

### Code Intelligence Plugins

These use the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP)—the same technology that powers VS Code's code intelligence.

**After installing** (e.g., `typescript-lsp`), Claude can:

- Jump to function definitions
- Find all references to a variable
- See type errors immediately after edits

**Note**: LSP plugins require the language server binary installed on your system. If you see "Executable not found," install the required binary:

| Plugin              | Binary Required              |
| ------------------- | ---------------------------- |
| `typescript-lsp`    | `typescript-language-server` |
| `python-lsp`        | `pyright-langserver`         |
| `rust-analyzer-lsp` | `rust-analyzer`              |
| `gopls-lsp`         | `gopls`                      |

### External Integration Plugins

Connect Claude to services you already use:

```
/plugin install github@claude-plugins-official
```

Now Claude can interact with GitHub issues, PRs, and repositories directly.

---

## Installation Scopes

When you install a plugin, choose where it applies:

| Scope       | Who Uses It              | Where It's Stored       |
| ----------- | ------------------------ | ----------------------- |
| **User**    | Just you, all projects   | `~/.claude/`            |
| **Project** | Everyone on this repo    | `.claude/settings.json` |
| **Local**   | Just you, this repo only | Local settings          |

**Recommendation**: Start with **User scope** for personal tools, **Project scope** for team standards.

---

## Managing Plugins

### See What's Installed

```
/plugin
```

Go to the **Installed** tab.

### Disable Without Uninstalling

```
/plugin disable plugin-name@marketplace-name
```

### Re-enable

```
/plugin enable plugin-name@marketplace-name
```

### Completely Remove

```
/plugin uninstall plugin-name@marketplace-name
```

---

## Adding More Marketplaces

The official marketplace is just the start. You can add others:

**GitHub repositories**:

```
/plugin marketplace add owner/repo
```

**GitLab or other git hosts**:

```
/plugin marketplace add https://gitlab.com/company/plugins.git
```

**Local development**:

```
/plugin marketplace add ./my-marketplace
```

### The Official Plugins Repository

Anthropic maintains the [official plugins repository](https://github.com/anthropics/claude-plugins-official) with verified plugins:

```
/plugin marketplace add anthropics/claude-plugins-official
```

This gives you access to all officially maintained plugins including Ralph Wiggum (Lesson 17).

---

## When to Use Plugins vs. Build Custom

| Situation                          | Recommendation                             |
| ---------------------------------- | ------------------------------------------ |
| Standard task (git, GitHub, Slack) | Install existing plugin                    |
| Team-specific workflow             | Check marketplace first, then build custom |
| Learning how plugins work          | Install examples, study their structure    |
| No matching plugin exists          | Create custom (see below)                  |

**Rule of thumb**: Check the marketplace before building from scratch.

---

## Package and Distribute Your Own Plugin

You've installed plugins. Now let's create one from the skills and components you've already built.

Throughout this chapter, you created skills (Lesson 9), configured subagents (Lesson 11), connected MCP servers (Lesson 12), and set up hooks (Lesson 15). Packaging these as a plugin lets you share them with teammates or use them across all your projects.

### Plugin Directory Structure

A plugin is a folder with a specific layout:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required manifest
├── skills/                   # Your SKILL.md files
├── agents/                   # Your subagent definitions
├── hooks/
│   └── hooks.json           # Your hook configurations
├── .mcp.json                # Your MCP server configs
└── README.md
```

**Critical**: Components go at the **root level**, not inside `.claude-plugin/`. The `.claude-plugin/` folder only contains the manifest.

### The Plugin Manifest

Every plugin needs a `plugin.json` file inside `.claude-plugin/`:

```json
{
  "name": "my-skills",
  "description": "My Claude Code skills collection",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

That's the minimum. Four fields. Your plugin is ready to use.

### Try It: Package Skills Lab as a Plugin

If you downloaded the Skills Lab in Lesson 7, let's turn it into a plugin:

**Step 1**: Navigate to your Skills Lab folder:

```bash
cd claude-code-skills-lab
```

**Step 2**: Create the manifest folder and file:

```bash
mkdir .claude-plugin
```

**Step 3**: Create `plugin.json`:

```json
{
  "name": "skills-lab",
  "description": "Practice skills from imsanghaar tutorials",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

**Step 4**: Test your plugin locally:

```
claude --plugin-dir ./claude-code-skills-lab
```

**Step 5**: Verify skills appear with namespace:

```
/skills-lab:internal-comms
```

Your Skills Lab is now a plugin.

### Plugin vs. Marketplace: What's the Difference?

| Concept         | What It Is                                       | Analogy      |
| --------------- | ------------------------------------------------ | ------------ |
| **Plugin**      | A folder with skills, agents, hooks, MCP configs | An app       |
| **Marketplace** | A catalog listing multiple plugins               | An app store |

**Why have marketplaces at all?**

You _could_ share plugins without a marketplace—just tell someone to clone your repo and use `--plugin-dir`. But marketplaces provide:

- **Discovery**: Browse what's available instead of knowing exact repo URLs
- **Organization**: Group related plugins (your team's tools, a company's integrations)
- **Updates**: Marketplaces can version plugins and notify users of updates

**Can you list your plugin on someone else's marketplace?**

Yes. Options include:

1. **Official Anthropic marketplace**: Submit a PR to get your plugin listed for everyone
2. **Team/company marketplaces**: Ask the maintainer to add your plugin to their `marketplace.json`
3. **Your own marketplace**: List your plugin plus others you find useful

Most developers create their own marketplace for personal/team use, then submit polished plugins to the official marketplace for broader distribution.

### Create Your Own Marketplace

To share your plugin with others, create a marketplace:

**Step 1**: Create a `marketplace.json` in your `.claude-plugin/` folder:

```json
{
  "name": "my-plugins",
  "owner": {
    "name": "Your Name"
  },
  "plugins": [
    {
      "name": "skills-lab",
      "source": "./skills-lab",
      "description": "Practice skills collection"
    }
  ]
}
```

**Step 2**: Push to GitHub (or GitLab, or any git host)

**Step 3**: Others can now add your marketplace:

```
/plugin marketplace add your-username/your-repo
```

### Distribution Options

| Method       | Command                               | Best For           |
| ------------ | ------------------------------------- | ------------------ |
| GitHub       | `/plugin marketplace add owner/repo`  | Teams, open source |
| GitLab/Other | `/plugin marketplace add https://...` | Enterprise         |
| Local        | `/plugin marketplace add ./path`      | Testing            |

---

### What's Next

You can now discover, install, and **create** plugins—the complete lifecycle. Lesson 17 introduces the **Ralph Wiggum Loop**—an autonomous iteration pattern where Claude validates and refines its own work. You'll see how to combine everything you've learned (skills, subagents, hooks, and your own plugins) into self-correcting workflows.

---

## Try With AI

**🔍 Explore the Marketplace:**

> "Run /plugin and show me what's in the Discover tab. What categories of plugins are available? Which ones would be useful for [your work: web development / Python / data analysis]?"

**What you're learning:** Plugin discovery—understanding what capability extensions exist before building from scratch. The ecosystem often has what you need.

**📦 Install and Test:**

> "Help me install the commit-commands plugin. After it's installed, walk me through using /commit-commands:commit to commit a change. What other commands does this plugin provide?"

**What you're learning:** The full plugin workflow—from installation through verification. Knowing the complete cycle builds confidence with new plugins.

**🔌 Code Intelligence:**

> "I write [TypeScript / Python / Rust / Go]. Help me install the LSP plugin for my language. What do I need to install on my system first? After installation, show me how Claude can now jump to definitions and find references."

**What you're learning:** How plugins add capabilities Claude doesn't have natively—in this case, language-server-level code understanding.

**🔗 External Integration:**

> "I want to connect Claude to [GitHub / Slack / Linear]. Help me install the appropriate plugin. What capabilities does it add? Show me an example of using it."

**What you're learning:** Platform integration through plugins—extending Claude's reach to external services without writing custom MCP servers.

**⚖️ Plugin Decision:**

> "I need Claude to help with [describe your task]. Should I: (a) install an existing plugin, (b) create a custom skill, (c) just ask Claude directly? Help me decide based on what's available in the marketplace."

**What you're learning:** The build vs. buy decision for AI capabilities—when to use existing solutions vs. creating custom ones.

**📦 Package Your Skills:**

> "Help me package my Skills Lab directory as a plugin. Create the plugin.json manifest, organize my skills into the correct directory structure, and test it with --plugin-dir."

**What you're learning:** Plugin creation workflow—turning your existing Claude Code components into shareable, installable packages.

**🌐 Create Your Marketplace:**

> "I have a plugin ready. Help me create a marketplace.json file, push it to GitHub, and show me how others can install my plugin."

**What you're learning:** Plugin distribution—sharing your work with teammates or the broader community through marketplace catalogs.
