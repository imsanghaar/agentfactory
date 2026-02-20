# Research Findings: Claude Code Installation & Authentication

**Source**: https://code.claude.com/docs/en/setup
**Fetched**: 2025-12-06
**Purpose**: Extract exact commands and requirements for Chapter 5 Lesson 2 update

---

## System Requirements

**Operating Systems**:
- macOS 10.15 (Catalina) or later
- Ubuntu 20.04+ / Debian 10+
- Windows 10 or later
- WSL 2 (with Ubuntu/Debian)

**Hardware**:
- 4GB+ RAM

**Optional Dependencies**:
- Node.js 18+ (only required for npm installation method)
- Git (recommended for developer workflows)

**Location Restrictions**:
- Must be in Anthropic-supported countries (location check during authentication)

---

## T002: Windows Installation Commands

### Method 1: PowerShell (RECOMMENDED)

```powershell
irm https://claude.ai/install.ps1 | iex
```

**What this does**: Downloads and runs the official installer script using PowerShell's Invoke-RestMethod.

**Requirements**: PowerShell 5.1+ (included in Windows 10+)

### Method 2: Git Bash (curl/bash)

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**What this does**: Downloads and executes the installation script using curl and bash.

**Requirements**: Git Bash installed (comes with Git for Windows)

**Special Configuration** (if Git Bash not in PATH):
```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
```

### Method 3: CMD (Command Prompt)

```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**What this does**: Downloads installer batch file, runs it, then deletes it.

**Requirements**: Windows 10+ (curl included by default)

### Method 4: npm (if Node.js installed)

```bash
npm install -g @anthropic-ai/claude-code
```

**Requirements**: Node.js 18+

---

## T003: macOS Installation Commands

### Method 1: Homebrew (RECOMMENDED)

```bash
brew install --cask claude-code
```

**What this does**: Installs Claude Code using Homebrew package manager (installs to `/Applications`).

**Requirements**: Homebrew installed (`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)

### Method 2: curl/bash

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**What this does**: Downloads and runs the official installer script.

**Requirements**: curl (pre-installed on macOS)

### Method 3: npm (if Node.js installed)

```bash
npm install -g @anthropic-ai/claude-code
```

**Requirements**: Node.js 18+

---

## T004: Linux/WSL Installation Commands

### Method 1: curl/bash (RECOMMENDED)

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**What this does**: Downloads and executes the installation script.

**Requirements**: curl, bash (pre-installed on most distributions)

**Special Case - Alpine Linux**:
```bash
apk add libgcc libstdc++ ripgrep
export USE_BUILTIN_RIPGREP=0
```

**What this does**: Installs required C++ libraries and ripgrep, then configures Claude Code to use system ripgrep.

### Method 2: npm (if Node.js installed)

```bash
npm install -g @anthropic-ai/claude-code
```

**Requirements**: Node.js 18+

---

## T005: npm Installation (Cross-Platform)

### Global Installation

```bash
npm install -g @anthropic-ai/claude-code
```

**What this does**: Installs Claude Code globally via npm package manager.

**Requirements**:
- Node.js 18 or later
- npm (included with Node.js)

**When to Use**:
- Already have Node.js installed
- Prefer npm-based workflows
- Need specific version control via package.json

**Platform Support**: Windows, macOS, Linux, WSL

---

## T006: Authentication Flows

### Authentication Method 1: Claude Console (Console API)

**Who This Is For**: Developers using Claude Code for the first time, no existing Claude subscription

**Steps**:
1. Launch Claude Code: `claude`
2. Opens browser to https://console.anthropic.com
3. Sign in with Google or email
4. Create a workspace
5. Authorize Claude Code access (OAuth)
6. Returns to terminal with authentication complete

**Access Level**: Console API (separate from Claude.ai)

### Authentication Method 2: Claude App (Unified Access)

**Who This Is For**: Users with Claude Pro or Claude Max subscriptions

**Steps**:
1. Launch Claude Code: `claude`
2. Opens browser to Claude.ai
3. Sign in with existing Claude account
4. Authorize Claude Code access
5. Returns to terminal with authentication complete

**Benefits**: Unified access across Claude web app and Claude Code

### Authentication Method 3: Enterprise (Advanced)

**Who This Is For**: Enterprise customers using Bedrock, Vertex AI, or Foundry

**Methods**:
- Amazon Bedrock integration
- Google Vertex AI integration
- Anthropic Foundry (dedicated capacity)

**Note**: Requires enterprise account setup and specific configuration

---

## T007: System Requirements Summary

| Requirement | Details |
|-------------|---------|
| **macOS** | 10.15 (Catalina) or later |
| **Ubuntu** | 20.04 or later |
| **Debian** | 10 or later |
| **Windows** | 10 or later |
| **WSL** | WSL 2 with Ubuntu/Debian |
| **RAM** | 4GB minimum |
| **Node.js** | 18+ (only for npm installation) |
| **Location** | Anthropic-supported countries |

---

## T008: Edge Cases & Special Configurations

### Alpine Linux Support

**Issue**: Missing C++ standard libraries

**Solution**:
```bash
apk add libgcc libstdc++ ripgrep
export USE_BUILTIN_RIPGREP=0
```

### Disable Auto-Update

**Use Case**: Corporate environments, testing, version pinning

**Configuration**:
```bash
export DISABLE_AUTOUPDATER=1
```

Add to shell profile (`.bashrc`, `.zshrc`, PowerShell profile) to persist.

### Git Bash Path (Windows)

**Issue**: Git Bash not in PATH

**Solution**:
```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
```

Add to PowerShell profile to persist.

### Geographic Restrictions

**Issue**: Claude Code authentication requires location in Anthropic-supported countries

**Impact**: Installation succeeds, but authentication will fail in unsupported regions

**Workaround**: None documented (requires location access)

---

## T009: Verification Commands

### Check Installation

```bash
claude --version
```

**Expected Output**: Version number (e.g., `Claude Code v1.2.3`)

### Diagnostic Tool

```bash
claude doctor
```

**What this does**: Runs system diagnostics to verify:
- Installation integrity
- Authentication status
- System compatibility
- Network connectivity

### Manual Update Check

```bash
claude update
```

**What this does**: Checks for and installs available updates (unless `DISABLE_AUTOUPDATER=1`)

### Launch Claude Code

```bash
claude
```

**What this does**: Starts Claude Code CLI. If not authenticated, triggers authentication flow.

---

## Platform-Specific Recommendations

Based on official documentation analysis:

| Platform | Primary Method | Rationale | Alternative |
|----------|---------------|-----------|-------------|
| **Windows** | PowerShell | Native to Windows, no dependencies | Git Bash (if Git installed) |
| **macOS** | Homebrew | Standard macOS package manager | curl/bash (if Homebrew not installed) |
| **Linux** | curl/bash | Universal, minimal dependencies | npm (if Node.js available) |
| **WSL** | curl/bash | Native to WSL environment | npm (if Node.js available) |

**npm as universal fallback**: Works on all platforms if Node.js 18+ is installed

---

## Validation Checklist

- [x] All commands extracted verbatim from official docs
- [x] System requirements documented
- [x] 3 authentication methods confirmed
- [x] Edge cases identified and documented
- [x] Verification commands extracted
- [x] Platform-specific recommendations defined
- [x] Source URL preserved for future reference

**Status**: Phase 1 research complete. Ready for Phase 2 (Foundational Updates).

---

**Document Version**: 1.0
**Last Updated**: 2025-12-06
**Next Phase Gate**: User approval to proceed to Phase 2
