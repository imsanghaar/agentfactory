---
slug: /General-Agents-Foundations/general-agents/free-claude-setup
title: "Free Claude Code Setup"
sidebar_position: 3
chapter: 3
lesson: 3
duration_minutes: 15

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation - Free Backend Path)"
layer_1_foundation: "API-based architecture setup, environment configuration, backend routing, model selection"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Free Claude Code Backend Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can configure Claude Code to use free AI backends (Gemini or DeepSeek) via API routing, understand the architecture of backend abstraction, and evaluate trade-offs between different free options"

learning_objectives:
  - objective: "Understand API-based architecture where frontend (Claude Code CLI) separates from backend (AI model)"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of three-layer architecture (CLI → Router → API)"
  - objective: "Evaluate and choose between free backend options (Gemini vs DeepSeek) based on use case"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Selection of appropriate backend with articulation of trade-offs"
  - objective: "Configure Claude Code Router to translate API formats between different LLM standards"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful router configuration with chosen free backend"
  - objective: "Set up environment variables for secure API key management"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "API key stored as environment variable, not hardcoded"
  - objective: "Verify free backend setup produces identical Claude Code functionality"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Completion of same verification tasks as Lesson 2 (official setup)"

# Cognitive load tracking
cognitive_load:
  new_concepts: 9
  assessment: "9 concepts (API routing, backend selection, format translation, environment variables, free tier limits, router configuration, daily workflow, architecture layers, trade-off evaluation) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Configure multiple backends in parallel, implement custom routing logic for specific use cases, monitor API usage and costs across backends"
  remedial_for_struggling: "Choose one backend (recommend Gemini for simplicity), focus on copy-paste setup first, verify it works before understanding the architecture"

# Generation metadata
generated_by: "AI-Native Software Development Curriculum Team"
source_spec: "Educational accessibility initiative - Multiple backend support"
created: "2025-11-20"
last_modified: "2026-01-16"
version: "2.1.0"

# Legacy compatibility
prerequisites:
  - "Lesson 1: Understanding Claude Code paradigm"
  - "Node.js 18+ installed"
  - "Free account with Gemini and/or DeepSeek"
  - "Terminal access"

# TEACHING GUIDE METADATA (visible to teacher role only)
teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "Getting Started with Claude Code"
  key_points:
    - "The three-layer architecture (CLI -> Router -> API) is the real lesson — students learn backend abstraction as a side effect of saving money"
    - "Free tier limits changed significantly in Dec 2025 — students must plan for rate limits and have backup backends ready"
    - "All Claude Code features (subagents, skills, MCP, hooks) work identically regardless of backend — this is the power of the abstraction"
    - "The 'ccr start' then 'ccr code' two-terminal workflow is the most common failure point for beginners"
  misconceptions:
    - "Students think free backends produce inferior Claude Code functionality — the CLI features are identical, only the underlying model intelligence differs"
    - "Students confuse the router config's $GOOGLE_API_KEY placeholder with their actual key — the warning boxes exist because students repeatedly paste real keys there"
    - "Students assume they must pick one backend permanently — they can switch by editing config.json anytime"
  discussion_prompts:
    - "What does it mean architecturally that you can swap the AI model behind Claude Code without changing how you use it?"
    - "If free tiers keep shrinking, what is your backup plan — and how does the router architecture make switching painless?"
    - "Why do you think Anthropic built Claude Code so it could work with competing models through routers?"
  teaching_tips:
    - "Demo the two-terminal workflow live — start ccr in terminal 1, then ccr code in terminal 2 — students need to see the sequence visually"
    - "Have the OpenRouter vs Gemini vs DeepSeek comparison table on screen when students choose — rushed choices here cause frustration later"
    - "The $VARIABLE_NAME placeholder confusion is so common that you should explicitly say 'do NOT replace this text' while pointing at the config"
    - "Pair students who chose different backends and have them compare responses to the same prompt — makes the abstraction layer tangible"
  assessment_quick_check:
    - "Ask students to draw the request flow: their prompt -> CLI -> router -> API -> model -> response"
    - "Have students run 'ccr version' and 'claude --version' and explain what each tool does"
    - "Ask: Why do you need two terminal windows, and what happens if you close the first one?"
---

# Free Claude Code Setup

**This lesson provides free alternatives to use Claude Code** without a subscription. You'll choose between Open Router, oGoogle Gemini or DeepSeek as your backend, learning the same Claude Code CLI interface and features covered in Lesson 2.

⚠️ **Important (January 2026)**: Google significantly reduced Gemini API free tier limits in December 2025. Daily request limits dropped 50-80% for most models. OpenRouter free models have daily request limits that vary by model. OpenRouter offers 30+ free models AI Free API but with daily request limits. Models rotate and quality varies. [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing) is not truly "free" but offers very low pricing (~$0.028-$0.42 per million tokens). Both deepseek-chat and deepseek-reasoner follow the same pricing: $0.028 per million input tokens (cache hit), $0.28 per million input tokens (cache miss), and $0.42 per million output tokens. Groq has a [Free Tier](https://community.groq.com/t/is-there-a-free-tier-and-what-are-its-limits/790) for its API via GroqCloud. Plan your usage accordingly and have backup options ready.

**All features work identically**: Subagents, skills, MCP servers, hooks, and all other capabilities covered in Lessons 05-15 function the same way with free backends. The only difference is the backend AI model and API provider.

:::tip Free Ongoing Usage
By using **Gemini's free tier** or **DeepSeek's competitive API**, you get ongoing free or low-cost consumption—no subscription required. This setup isn't just for learning; many developers use it as their daily driver. The free tiers are generous enough for real development work.
:::

---

## Choose Your Free Backend

Before setup, decide which backend suits you. All three options provide identical Claude Code functionality:

| Factor | OpenRouter | Gemini | DeepSeek |
| :--- | :--- | :--- | :--- |
| **Available Models** | 5+ free options | Gemini 2.5 Flash | DeepSeek Chat/Reasoner |
| **Free Tier** | Daily request limits per model | Daily request limits | Token-based (~$0.028-$0.42/M tokens) |
| **Speed** | Very Fast | Very Fast | Fast |
| **Setup Complexity** | Manual, most transparent | Easiest (few steps) | Slightly more involved |
| **Reasoning Models** | Available (Qwen, Llama) | Native support | Native support |

---

## OpenRouter Setup

**This section guides you through configuring Claude Code with OpenRouter's multi-model platform.**

OpenRouter aggregates multiple AI models (including Gemini, Qwen, Llama) under one API. This gives you maximum flexibility to experiment with different models without re-configuring.

### Step 1: Get Your OpenRouter API Key

1. Go to: [OpenRouter API Keys](https://openrouter.ai/keys)
2. Click **"Create Key"**
3. Name it (e.g., "Claude Code Router")
4. **Copy the key** (starts with: `sk-or-v1-...`)

---

### Step 2: Install and Configure

**Select your operating system:**

::::os-tabs

::windows

### Verify Node.js

```powershell
node --version  # Should show v18.x.x or higher
```

If missing, install from [nodejs.org](https://nodejs.org/)

---

### Install Tools

Open PowerShell and run:

```powershell
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router
```

---

### Create Config Directories

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude-code-router"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude"
```

---

### Create the Config File

1. Open **Notepad** (search "Notepad" in Windows Start menu)
2. Copy and paste this exactly:

```json
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1",
      "api_key": "$OPENROUTER_API_KEY",
      "models": [
        "qwen/qwen-coder-32b-vision",
        "google/gemini-2.0-flash-exp:free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "qwen/qwen3-14b:free",
        "xiaomi/mimo-v2-flash:free"
      ],
      "transformer": {
        "use": ["openrouter"]
      }
    }
  ],
  "Router": {
    "default": "openrouter,qwen/qwen-coder-32b-vision",
    "background": "openrouter,qwen/qwen-coder-32b-vision",
    "think": "openrouter,meta-llama/llama-3.3-70b-instruct:free",
    "longContext": "openrouter,qwen/qwen-coder-32b-vision",
    "longContextThreshold": 60000
  }
}
```

:::warning Do NOT Change $OPENROUTER_API_KEY
Leave `"api_key": "$OPENROUTER_API_KEY"` exactly as written. The router reads your key from the environment variable you'll set in the next step.
:::

3. Click **File → Save As**
4. In the "File name" field, type exactly: `%USERPROFILE%\.claude-code-router\config.json`
5. Click **Save**

---

### Set Your API Key

**Run PowerShell as Administrator:**
1. Search "PowerShell" in Windows Start menu
2. **Right-click** on "Windows PowerShell"
3. Click **"Run as administrator"**
4. Click "Yes" if prompted

Run this command (replace `YOUR_KEY_HERE` with your key from Step 1):

```powershell
[System.Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY', 'YOUR_KEY_HERE', 'User')
```

5. **Close PowerShell completely** (not just the tab—close the whole window)
6. Open a **new regular PowerShell** (not as admin)
7. Verify it worked:

```powershell
echo $env:OPENROUTER_API_KEY
```

You should see your API key displayed ✅

---

### Verify Setup

```powershell
claude --version     # Should show: Claude Code v2.x.x
ccr version          # Should show version number
echo $env:OPENROUTER_API_KEY  # Should show your key
```

✅ **Done!** Proceed to Step 3: Daily Workflow below.

::macos

### Verify Node.js

```bash
node --version  # Should show v18.x.x or higher
```

If missing, install from [nodejs.org](https://nodejs.org/)

---

### Copy-Paste Setup

Copy and paste this entire block into Terminal:

```bash
# Install tools
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

# Create config directories
mkdir -p ~/.claude-code-router ~/.claude

# Create router config
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1",
      "api_key": "$OPENROUTER_API_KEY",
      "models": [
        "qwen/qwen-coder-32b-vision",
        "google/gemini-2.0-flash-exp:free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "qwen/qwen3-14b:free",
        "xiaomi/mimo-v2-flash:free"
      ],
      "transformer": {
        "use": ["openrouter"]
      }
    }
  ],
  "Router": {
    "default": "openrouter,qwen/qwen-coder-32b-vision",
    "background": "openrouter,qwen/qwen-coder-32b-vision",
    "think": "openrouter,meta-llama/llama-3.3-70b-instruct:free",
    "longContext": "openrouter,qwen/qwen-coder-32b-vision",
    "longContextThreshold": 60000
  }
}
EOF

# Verify file was created
cat ~/.claude-code-router/config.json
```

---

### Set Your API Key

Replace `YOUR_KEY_HERE` with your actual API key:

```bash
# For zsh (default on macOS):
echo 'export OPENROUTER_API_KEY="YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

---

### Verify Setup

```bash
claude --version          # Should show: Claude Code v2.x.x
ccr version               # Should show version number
echo $OPENROUTER_API_KEY # Should show your key
```

✅ **Done!** Proceed to Step 3: Daily Workflow below.

::linux

### Verify Node.js

```bash
node --version  # Should show v18.x.x or higher
```

If missing, install via your package manager or [nodejs.org](https://nodejs.org/)

---

### Copy-Paste Setup

Copy and paste this entire block into your terminal:

```bash
# Install tools
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

# Create config directories
mkdir -p ~/.claude-code-router ~/.claude

# Create router config
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1",
      "api_key": "$OPENROUTER_API_KEY",
      "models": [
        "qwen/qwen-coder-32b-vision",
        "google/gemini-2.0-flash-exp:free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "qwen/qwen3-14b:free",
        "xiaomi/mimo-v2-flash:free"
      ],
      "transformer": {
        "use": ["openrouter"]
      }
    }
  ],
  "Router": {
    "default": "openrouter,qwen/qwen-coder-32b-vision",
    "background": "openrouter,qwen/qwen-coder-32b-vision",
    "think": "openrouter,meta-llama/llama-3.3-70b-instruct:free",
    "longContext": "openrouter,qwen/qwen-coder-32b-vision",
    "longContextThreshold": 60000
  }
}
EOF

# Verify file was created
cat ~/.claude-code-router/config.json
```

---

### Set Your API Key

Replace `YOUR_KEY_HERE` with your actual API key:

```bash
# For bash:
echo 'export OPENROUTER_API_KEY="YOUR_KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

:::tip Check Your Shell
Run `echo $SHELL` to see which shell you use. If it shows `/bin/zsh`, use `~/.zshrc` instead of `~/.bashrc`.
:::

---

### Verify Setup

```bash
claude --version          # Should show: Claude Code v2.x.x
ccr version               # Should show version number
echo $OPENROUTER_API_KEY # Should show your key
```

✅ **Done!** Proceed to Step 3: Daily Workflow below.

::::

---

### Step 3: Daily Workflow

**Every time you want to code:**

::::os-tabs

::windows

**PowerShell 1** - Start router FIRST:
```powershell
ccr start
```

Leave this window running. You'll see a warning message—that's normal!

**PowerShell 2** - Open a NEW PowerShell window and run:
```powershell
cd C:\your\project\folder
ccr code
```

:::tip First Startup Takes Time
**Wait 10-20 seconds** after running `ccr code` on first startup. The router needs time to initialize.
:::

**When done:** Press `Ctrl+C` in both windows.

::macos

**Terminal 1** - Start router FIRST:
```bash
ccr start
# Wait for: ✅ Service started successfully
```

**Terminal 2** - THEN use Claude:
```bash
cd ~/your-project
ccr code
```

**When done:** Press `Ctrl+C` in both terminals.

::linux

**Terminal 1** - Start router FIRST:
```bash
ccr start
# Wait for: ✅ Service started successfully
```

**Terminal 2** - THEN use Claude:
```bash
cd ~/your-project
ccr code
```

**When done:** Press `Ctrl+C` in both terminals.

::::

---

## Gemini Setup

**This section guides you through configuring Claude Code with Google's Gemini API.**

### Step 1: Get Your Free Google API Key

1. Go to: [Google AI Studio](https://aistudio.google.com/api-keys)
2. Click **"Get API Key"**
3. Sign in with Google
4. Click **"Create API Key"**
5. **Copy the key** (looks like: `AIzaSyAaBbCcDd...`)

---

### Step 2: Install and Configure

**Select your operating system:**

::::os-tabs

::windows

### Step 0: Install Node.js (Skip if Already Installed)

**Check if you have Node.js:**

Open **PowerShell** (search "PowerShell" in Windows Start menu) and type:

```powershell
node --version
```

- **If you see `v18.x.x` or higher** → Skip to Step 1 ✅
- **If you see an error or version lower than v18** → Follow these steps:

1. Go to: [nodejs.org](https://nodejs.org/)
2. Click the big green button that says **"Download Node.js (LTS)"**
3. Run the downloaded file (it's called something like `node-v20.x.x-x64.msi`)
4. Click **Next** → **Next** → **Next** → **Install**
5. Wait for it to finish
6. **Close ALL PowerShell windows completely**
7. Open a **new PowerShell** window
8. Type `node --version` again to confirm it works

You should now see a version number like `v20.11.0` ✅

---

### Step 1: Install Tools

Open PowerShell and run:

```powershell
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router
```

---

### Step 2: Create Config Directories

Enable running scriptson your system first:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Now create directories:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude-code-router"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude"
```

---

### Step 3: Create the Config File

1. Open **Notepad** (search "Notepad" in Windows Start menu)
2. Copy and paste this text exactly as-is:

```json
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/models/",
      "api_key": "$GOOGLE_API_KEY",
      "models": [
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash"
      ],
      "transformer": {
        "use": ["gemini"]
      }
    }
  ],
  "Router": {
    "default": "gemini,gemini-2.5-flash-lite",
    "background": "gemini,gemini-2.5-flash-lite",
    "think": "gemini,gemini-2.5-flash-lite",
    "longContext": "gemini,gemini-2.5-flash-lite",
    "longContextThreshold": 60000
  }
}
```

:::warning Do NOT Change $GOOGLE_API_KEY
Leave `"api_key": "$GOOGLE_API_KEY"` exactly as written. Do NOT replace it with your actual key here—the router will automatically read your key from the environment variable you set in Step 4.
:::

3. Click **File → Save As**
4. In the "File name" field, type exactly: `%USERPROFILE%\.claude-code-router\config.json`
5. Click **Save**

---

### Step 4: Set Your API Key

**Run PowerShell as Administrator:**
1. Search "PowerShell" in Windows Start menu
2. **Right-click** on "Windows PowerShell"
3. Click **"Run as administrator"**
4. Click "Yes" if prompted

Run this command (replace `YOUR_KEY_HERE` with your actual API key from Step 1):

```powershell
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'YOUR_KEY_HERE', 'User')
```

5. **Close PowerShell completely** (not just the tab—close the whole window)
6. Open a **new regular PowerShell** (not as admin this time)
7. Verify it worked:

```powershell
echo $env:GOOGLE_API_KEY
```

You should see your API key displayed ✅

---

### Verify Setup

```powershell
claude --version     # Should show: Claude Code v2.x.x
ccr version          # Should show version number
echo $env:GOOGLE_API_KEY  # Should show your key
```

✅ **Done!** Proceed to Step 3: Daily Workflow below.

::macos

### Verify Node.js

```bash
node --version  # Should show v18.x.x or higher
```

If missing, install from [nodejs.org](https://nodejs.org/)

---

### Copy-Paste Setup

Copy and paste this entire block into Terminal:

```bash
# Install tools
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

# Create config directories
mkdir -p ~/.claude-code-router ~/.claude

# Create router config
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/models/",
      "api_key": "$GOOGLE_API_KEY",
      "models": [
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash"
      ],
      "transformer": {
        "use": ["gemini"]
      }
    }
  ],
  "Router": {
    "default": "gemini,gemini-2.5-flash-lite",
    "background": "gemini,gemini-2.5-flash-lite",
    "think": "gemini,gemini-2.5-flash-lite",
    "longContext": "gemini,gemini-2.5-flash-lite",
    "longContextThreshold": 60000
  }
}
EOF

# Verify file was created
cat ~/.claude-code-router/config.json
```

---

### Set Your API Key

Replace `YOUR_KEY_HERE` with your actual API key:

```bash
# For zsh (default on macOS):
echo 'export GOOGLE_API_KEY="YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

---

### Verify Setup

```bash
claude --version     # Should show: Claude Code v2.x.x
ccr version          # Should show version number
echo $GOOGLE_API_KEY # Should show your key
```

✅ **Done!** Proceed to Step 3: Daily Workflow below.

::linux

### Verify Node.js

```bash
node --version  # Should show v18.x.x or higher
```

If missing, install from [nodejs.org](https://nodejs.org/) or use your package manager.

---

### Copy-Paste Setup

Copy and paste this entire block into your terminal:

```bash
# Install tools
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

# Create config directories
mkdir -p ~/.claude-code-router ~/.claude

# Create router config
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/models/",
      "api_key": "$GOOGLE_API_KEY",
      "models": [
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash"
      ],
      "transformer": {
        "use": ["gemini"]
      }
    }
  ],
  "Router": {
    "default": "gemini,gemini-2.5-flash-lite",
    "background": "gemini,gemini-2.5-flash-lite",
    "think": "gemini,gemini-2.5-flash-lite",
    "longContext": "gemini,gemini-2.5-flash-lite",
    "longContextThreshold": 60000
  }
}
EOF

# Verify file was created
cat ~/.claude-code-router/config.json
```

---

### Set Your API Key

Replace `YOUR_KEY_HERE` with your actual API key:

```bash
# For bash:
echo 'export GOOGLE_API_KEY="YOUR_KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

:::tip Check Your Shell
Run `echo $SHELL` to see your shell. If it shows `/bin/zsh`, use `~/.zshrc` instead of `~/.bashrc`.
:::

---

### Verify Setup

```bash
claude --version     # Should show: Claude Code v2.x.x
ccr version          # Should show version number
echo $GOOGLE_API_KEY # Should show your key
```

✅ **Done!** Proceed to Step 3: Daily Workflow below.

::::

---

### Step 3: Daily Workflow

**Every time you want to code:**

::::os-tabs

::windows

**PowerShell 1** - Start router FIRST:
```powershell
ccr start
```

Leave this window running. You'll see a warning message—that's normal!

**PowerShell 2** - Open a NEW PowerShell window and run:
```powershell
cd C:\your\project\folder
ccr code
```

:::tip First Startup Takes Time
**Wait 10-20 seconds** after running `ccr code` on first startup. The router needs time to initialize. If it seems stuck, just wait—it's working!
:::

**When done:** Press `Ctrl+C` in both windows.

::macos

**Terminal 1** - Start router FIRST:
```bash
ccr start
# Wait for: ✅ Service started successfully
```

**Terminal 2** - THEN use Claude:
```bash
cd ~/your-project
ccr code
```

**When done:** Press `Ctrl+C` in both terminals.

::linux

**Terminal 1** - Start router FIRST:
```bash
ccr start
# Wait for: ✅ Service started successfully
```

**Terminal 2** - THEN use Claude:
```bash
cd ~/your-project
ccr code
```

**When done:** Press `Ctrl+C` in both terminals.

::::

---

## DeepSeek Setup

**This section guides you through configuring Claude Code with DeepSeek's API.**

If you already completed the **Gemini Setup** above, you already have Node.js and the Claude Code Router installed. You only need to create the DeepSeek configuration and set your API key.

### Step 1: Get Your DeepSeek API Key

1. Go to: [DeepSeek API Platform](https://platform.deepseek.com/)
2. Sign up or log in with your account
3. Navigate to **API Keys** section
4. Click **"Create API Key"**
5. **Copy the key** (looks like: `sk-...`)

---

### Step 2: Configure DeepSeek

::::os-tabs

::windows

**Create the config file:** Open **Notepad** and paste:

```json
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/v1",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        "deepseek-chat",
        "deepseek-reasoner"
      ],
      "transformer": {
        "use": ["openai"]
      }
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "deepseek,deepseek-chat",
    "longContextThreshold": 60000
  }
}
```

:::warning Do NOT Change $DEEPSEEK_API_KEY
Leave `"api_key": "$DEEPSEEK_API_KEY"` exactly as written.
:::

Save as: `%USERPROFILE%\.claude-code-router\config.json`

**Set your API key** (Run PowerShell as Administrator):

```powershell
[System.Environment]::SetEnvironmentVariable('DEEPSEEK_API_KEY', 'YOUR_KEY_HERE', 'User')
```

Close and reopen PowerShell, then verify:

```powershell
echo $env:DEEPSEEK_API_KEY
```

::macos

**Create config and set API key:**

```bash
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/v1",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        "deepseek-chat",
        "deepseek-reasoner"
      ],
      "transformer": {
        "use": ["openai"]
      }
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "deepseek,deepseek-chat",
    "longContextThreshold": 60000
  }
}
EOF

# Set your API key
echo 'export DEEPSEEK_API_KEY="YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

::linux

**Create config and set API key:**

```bash
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/v1",
      "api_key": "$DEEPSEEK_API_KEY",
      "models": [
        "deepseek-chat",
        "deepseek-reasoner"
      ],
      "transformer": {
        "use": ["openai"]
      }
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner",
    "longContext": "deepseek,deepseek-chat",
    "longContextThreshold": 60000
  }
}
EOF

# Set your API key
echo 'export DEEPSEEK_API_KEY="YOUR_KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

::::

---

## Verification

Both Gemini and DeepSeek use the **same daily workflow** and verification process.

**Start a Claude session and say hi:**

```
hi
```

**Expected**: Claude responds with a greeting confirming it's working! ✅ Success!

---

## Troubleshooting

::::os-tabs

::windows

**"command not found" or "not recognized"**

Close and reopen PowerShell completely. If still failing, the npm global bin directory isn't in your PATH.

**"API key not found" or empty variable**

1. Make sure you ran the `SetEnvironmentVariable` command as Administrator
2. Close ALL PowerShell windows and open a fresh one
3. Check with `echo $env:GOOGLE_API_KEY`

**Stuck at "starting service"**

Wait 20-30 seconds on first run. This is normal.

**Router starts but Claude hangs**

Make sure `ccr start` is running in PowerShell 1 before running `ccr code` in PowerShell 2.

::macos

**"command not found: claude" or "command not found: ccr"**

The npm global bin directory isn't in your PATH:

```bash
npm config get prefix
echo 'export PATH="$PATH:/usr/local/bin"' >> ~/.zshrc
source ~/.zshrc
```

**"API key not found" or empty GOOGLE_API_KEY**

```bash
echo $GOOGLE_API_KEY
# If empty, re-add:
echo 'export GOOGLE_API_KEY="YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

**Router starts but Claude hangs**

Wait 2-3 seconds after `ccr start` shows "Service started" before running `ccr code`.

::linux

**"command not found: claude" or "command not found: ccr"**

The npm global bin directory isn't in your PATH:

```bash
npm config get prefix
echo 'export PATH="$PATH:/usr/local/bin"' >> ~/.bashrc
source ~/.bashrc
```

**"API key not found" or empty GOOGLE_API_KEY**

```bash
echo $GOOGLE_API_KEY
# If empty, re-add:
echo 'export GOOGLE_API_KEY="YOUR_KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

**Router starts but Claude hangs**

Wait 2-3 seconds after `ccr start` shows "Service started" before running `ccr code`.

::::

---

## Try With AI

Once your free setup is working, try these prompts to verify everything works:

**Verify Basic Functionality:**

> "Hello! Confirm you're working by telling me: (1) what model you're using, (2) can you see files in this directory? List them if so."

**Test File Operations:**

> "Create a simple test file called `hello.txt` with the text 'Free Claude Code setup works!' Then read it back to confirm."

**Understand the Architecture:**

> "Explain the architecture of my current setup: I'm using Claude Code CLI with a router pointing to a free backend. What's happening when I send you a message? Walk me through the request flow."

---

That's it. Proceed to **Lesson 05** to learn about teaching Claude your way of working.
