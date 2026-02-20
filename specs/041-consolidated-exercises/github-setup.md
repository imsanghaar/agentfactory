# GitHub Setup Guide for Exercise Repos

This document captures the exact patterns used in `panaversity/claude-code-basic-exercises` and `panaversity/claude-code-skills-exercises`, providing reusable templates for creating new exercise repos.

---

## 1. Current Repo Inventory

| Repo                           | Status               | ZIP Name               | Download URL                                                                                                |
| ------------------------------ | -------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| `claude-code-basic-exercises`  | Active, public       | `basics-exercises.zip` | `https://github.com/panaversity/claude-code-basic-exercises/releases/latest/download/basics-exercises.zip`  |
| `claude-code-skills-exercises` | Active, public       | `skills-exercises.zip` | `https://github.com/panaversity/claude-code-skills-exercises/releases/latest/download/skills-exercises.zip` |
| `claude-code-exercises`        | **Archived**, public | N/A (no releases)      | N/A — monorepo with `basics/` and `skills/` subdirs, replaced by the two repos above                        |

### Observations

- Both active repos were created on 2026-02-08 and have a single release tagged `latest`.
- The archived `claude-code-exercises` repo has **no releases** and **no workflow**. It served as the original monorepo before being split.
- Both active workflows are **identical** except for the ZIP filename.
- The `softprops/action-gh-release@v2` action requires **write permissions** to contents (default for `GITHUB_TOKEN` in public repos).

---

## 2. GitHub Actions Workflow Template

Both repos use the same workflow. The only variable is the ZIP filename.

### `.github/workflows/release.yml`

```yaml
name: Release Exercise Pack
on:
  push:
    branches: [main]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Create ZIP
        run: zip -r {{ZIP_NAME}}.zip . -x '.github/*' '.git/*'
      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: latest
          files: {{ZIP_NAME}}.zip
          make_latest: true
```

**Placeholders:**

- `{{ZIP_NAME}}` — The name of the ZIP file (without `.zip` extension). Convention: `<topic>-exercises` (e.g., `basics-exercises`, `skills-exercises`).

**How it works:**

1. On every push to `main`, the workflow triggers.
2. It zips the entire repo excluding `.github/` and `.git/` directories.
3. It creates (or overwrites) a release tagged `latest` with the ZIP attached.
4. The `make_latest: true` flag ensures it shows as the "Latest" release on GitHub.

**Exclusion note:** The `-x '.github/*' '.git/*'` flags ensure students never see CI/CD files or git history in the downloaded ZIP. Add more exclusions as needed (e.g., `'.gitignore'` or `'*.md'` at root level if you want to exclude repo-level README from the ZIP).

---

## 3. `.github/` Directory Structure

Minimal — only the workflow file:

```
.github/
└── workflows/
    └── release.yml
```

No branch protection rules, no CODEOWNERS, no issue templates are used in the current repos. Keep it simple.

---

## 4. README.md Template for New Exercise Repos

````markdown
# {{REPO_TITLE}}

**By Panaversity — {{TAGLINE}}**

---

## What's Inside

{{BRIEF_DESCRIPTION_OF_EXERCISES}}

## Package Structure

\```
{{FOLDER_TREE}}
\```

---

## How to Get Started

### With Cowork (Recommended for Beginners)

1. Open Claude Desktop app on macOS
2. Switch to the Cowork tab
3. Point Cowork at the exercise folder you want to work on
4. Read the INSTRUCTIONS.md file in the exercise folder
5. Start describing your task to Claude

### With Claude Code (For Terminal Users)

1. Open your terminal
2. Navigate to the exercise folder: `cd {{EXAMPLE_PATH}}`
3. Launch Claude Code
4. Read the INSTRUCTIONS.md and start working

---

## Recommended Order

{{PROGRESSION_TABLE_OR_LIST}}

---

## Problem-Solving Framework

Use this for every exercise:

1. **Define** -- What exactly am I trying to accomplish?
2. **Gather** -- What files/data does Claude need?
3. **Specify** -- Describe the desired outcome, constraints, and format
4. **Execute** -- Run it with Claude Code or Cowork
5. **Verify** -- Does the output match what I asked for?
6. **Iterate** -- What would I change? Run it again.
7. **Reflect** -- What did I learn about specifying problems clearly?

---

_Built for Panaversity's AI-Native Development Curriculum_
````

**Placeholders:**

- `{{REPO_TITLE}}` — e.g., "Claude Code & Cowork: Practical Problem-Solving Exercises"
- `{{TAGLINE}}` — e.g., "Learn by Doing, Not by Reading"
- `{{BRIEF_DESCRIPTION_OF_EXERCISES}}` — 2-3 sentences
- `{{FOLDER_TREE}}` — ASCII tree of exercise structure
- `{{EXAMPLE_PATH}}` — Path to a first exercise folder
- `{{PROGRESSION_TABLE_OR_LIST}}` — Recommended weekly schedule

---

## 5. Step-by-Step Repo Setup Checklist

### Phase A: Create the Repo

- [ ] Go to `https://github.com/organizations/panaversity/repositories/new`
- [ ] Name: `claude-code-{{TOPIC}}-exercises` (e.g., `claude-code-testing-exercises`)
- [ ] Description: Brief one-liner about the exercise pack
- [ ] Visibility: **Public**
- [ ] Initialize with: README (will be replaced)
- [ ] Default branch: `main`
- [ ] No license file needed (exercises are educational material)

### Phase B: Add Workflow and Content

```bash
# Clone the new repo
gh repo clone panaversity/claude-code-{{TOPIC}}-exercises
cd claude-code-{{TOPIC}}-exercises

# Create workflow directory
mkdir -p .github/workflows

# Create the release workflow (copy template above, replace {{ZIP_NAME}})
# Example: ZIP_NAME = "testing-exercises"
cat > .github/workflows/release.yml << 'EOF'
name: Release Exercise Pack
on:
  push:
    branches: [main]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Create ZIP
        run: zip -r testing-exercises.zip . -x '.github/*' '.git/*'
      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: latest
          files: testing-exercises.zip
          make_latest: true
EOF

# Add README.md (use template above)
# Add exercise folders with INSTRUCTIONS.md and starter files

# Commit and push
git add -A
git commit -m "feat: initial exercise pack with CI release"
git push origin main
```

### Phase C: Verify

- [ ] Go to repo Actions tab — confirm workflow ran successfully (green check)
- [ ] Go to Releases tab — confirm `latest` release exists with ZIP attached
- [ ] Test download URL in browser:
  ```
  https://github.com/panaversity/claude-code-{{TOPIC}}-exercises/releases/latest/download/{{ZIP_NAME}}.zip
  ```
- [ ] Download the ZIP and verify:
  - Contains exercise folders with INSTRUCTIONS.md
  - Does NOT contain `.github/` or `.git/` directories
  - README.md is present at root level
- [ ] Verify the ZIP size is reasonable (basics=120KB, skills=similar)

### Phase D: Update Lesson with Download Link

- [ ] Find the lesson file that references this exercise pack
- [ ] Add download button using this exact format (from existing lessons):
  ```markdown
  **[Download {{PACK_NAME}} Exercises (ZIP)](https://github.com/panaversity/claude-code-{{TOPIC}}-exercises/releases/latest/download/{{ZIP_NAME}}.zip)**
  ```
- [ ] Verify the link works from the lesson page after deploy

---

## 6. Download Link Format

### Primary Format (used in lessons)

```
https://github.com/panaversity/{{REPO_NAME}}/releases/latest/download/{{ZIP_NAME}}.zip
```

**Examples from existing lessons:**

- `apps/learn-app/docs/01-General-Agents-Foundations/03-general-agents/06-basics-exercises.md` line 69:
  ```markdown
  **[Download Basics Exercises (ZIP)](https://github.com/panaversity/claude-code-basic-exercises/releases/latest/download/basics-exercises.zip)**
  ```
- `apps/learn-app/docs/01-General-Agents-Foundations/03-general-agents/10-skills-exercises.md` line 75:
  ```markdown
  **[Download Skills Exercises (ZIP)](https://github.com/panaversity/claude-code-skills-exercises/releases/latest/download/skills-exercises.zip)**
  ```

### Why `releases/latest/download/` Works

The `latest` tag is overwritten on every push to main via `softprops/action-gh-release@v2` with `tag_name: latest` and `make_latest: true`. This means the URL is **stable** — it always points to the most recent ZIP, no version numbers to update.

### Fallback Link (if release not yet created)

If the repo exists but the first push hasn't happened yet:

```markdown
**[Download from GitHub](https://github.com/panaversity/{{REPO_NAME}})**

_Clone or download the ZIP from the repository directly._
```

---

## 7. Deprecation Notice Template

For repos being replaced or consolidated (like `claude-code-exercises` was archived):

### README.md Addition (top of file)

```markdown
> **This repository has been archived.**
>
> The exercises have moved to dedicated repositories:
>
> - **Basics exercises**: [claude-code-basic-exercises](https://github.com/panaversity/claude-code-basic-exercises)
> - **Skills exercises**: [claude-code-skills-exercises](https://github.com/panaversity/claude-code-skills-exercises)
>
> Please use the new repositories for the latest versions.
```

### Steps to Deprecate a Repo

1. Add the deprecation notice to the top of README.md
2. Archive the repo: Settings > Danger Zone > Archive this repository
3. Update any lesson files that linked to the old repo
4. Verify old links redirect or show clear notice

**Note:** The current `claude-code-exercises` archived repo does NOT have a deprecation notice in its README. If students find it via search, the README still describes exercise content as if it's active. Consider adding the notice above.

---

## 8. Workflow Comparison: basic-exercises vs skills-exercises

| Aspect          | basic-exercises                                         | skills-exercises                                        |
| --------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| Workflow name   | `Release Exercise Pack`                                 | `Release Exercise Pack`                                 |
| Trigger         | Push to `main`                                          | Push to `main`                                          |
| Runner          | `ubuntu-latest`                                         | `ubuntu-latest`                                         |
| Checkout action | `actions/checkout@v4`                                   | `actions/checkout@v4`                                   |
| ZIP command     | `zip -r basics-exercises.zip . -x '.github/*' '.git/*'` | `zip -r skills-exercises.zip . -x '.github/*' '.git/*'` |
| Release action  | `softprops/action-gh-release@v2`                        | `softprops/action-gh-release@v2`                        |
| Tag name        | `latest`                                                | `latest`                                                |
| Make latest     | `true`                                                  | `true`                                                  |

**Verdict: Identical** except for ZIP filename. The template above captures the pattern exactly.

---

## 9. Repo Settings Checklist

Verified settings from both active repos:

- [x] Visibility: **Public**
- [x] Default branch: **main**
- [x] Archived: **false**
- [x] Issues: **enabled**
- [x] Downloads: **enabled**
- [x] Actions: **enabled**, all actions allowed
- [x] No branch protection (exercises are pushed directly to main)
- [x] No topics set (consider adding: `exercises`, `claude-code`, `panaversity`)
- [ ] No CODEOWNERS file
- [ ] No issue or PR templates

### Recommended Additional Settings (for new repos)

- Add topics: `exercises`, `claude-code`, `panaversity`, `ai-education`
- Add description on repo creation
- Consider adding a simple `.gitignore` for common OS files (`.DS_Store`, `Thumbs.db`)
