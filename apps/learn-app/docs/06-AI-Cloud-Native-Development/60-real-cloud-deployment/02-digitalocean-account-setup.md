---
sidebar_position: 2
title: "DigitalOcean Account & doctl Setup"
description: "Create a DigitalOcean account, install doctl CLI, and authenticate using API token"
keywords: [digitalocean, doctl, kubernetes, cloud, api token, cli, doks]
chapter: 60
lesson: 2
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Cloud Provider Account Setup"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student creates a DigitalOcean account with proper billing configuration and understands free credit programs"

  - name: "API Token Management"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "4. Safety"
    measurable_at_this_level: "Student generates API tokens with appropriate scopes and understands security implications of read vs read/write permissions"

  - name: "CLI Tool Installation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student installs doctl CLI using platform-appropriate package manager (brew, snap, or binary)"

  - name: "CLI Authentication"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "5.3 Using digital tools to solve problems"
    measurable_at_this_level: "Student authenticates doctl with API token and verifies connection using doctl account get"

learning_objectives:
  - objective: "Create a DigitalOcean account with billing configured and understand the free credit program"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has active DigitalOcean account with payment method added"

  - objective: "Generate an API token with read/write scope for cluster management"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has generated token stored securely and can explain why read/write scope is required"

  - objective: "Install doctl CLI on your operating system using the appropriate package manager"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "doctl version command returns version information"

  - objective: "Authenticate doctl with your API token and verify the connection"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "doctl account get returns account information with email, status, and droplet limit"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (account creation, API tokens, doctl installation, authentication flow) well within B1 tier (7-10 concepts) - straightforward sequential setup with clear validation at each step"

differentiation:
  extension_for_advanced: "Explore DigitalOcean Spaces for container registry, configure multiple authentication contexts with doctl auth"
  remedial_for_struggling: "Focus on GUI-based token generation, use exact commands provided without modification"
---

# DigitalOcean Account & doctl Setup

Your Kubernetes knowledge from Docker Desktop and local clusters translates directly to the cloud. The only new element? Connecting to a remote cluster instead of a local one. Before you can provision DOKS (DigitalOcean Kubernetes Service), you need credentials and the CLI tools to manage them.

This lesson establishes your cloud connection: account setup, API token generation, and doctl authentication. Once complete, you'll be ready to create real Kubernetes clusters in Lesson 3.

---

## Why DigitalOcean for Learning Cloud Kubernetes?

Cloud providers offer managed Kubernetes services that handle the control plane (API server, etcd, scheduler) while you manage worker nodes. The major providers are:

| Provider | Service | Minimum Monthly Cost | Free Tier |
|----------|---------|---------------------|-----------|
| AWS | EKS | ~$73 (control plane) + nodes | None for EKS |
| Google Cloud | GKE | ~$73 (control plane) + nodes | Autopilot free tier |
| Azure | AKS | Control plane free + nodes | Control plane free |
| **DigitalOcean** | **DOKS** | **~$24** (2-node cluster) | **$200 free credit (60 days)** |
| Civo | Civo K3s | ~$5 (starter cluster) | $250 free credit |

DigitalOcean stands out for learners:

1. **Predictable pricing**: No surprise bills from hidden egress charges
2. **Simple interface**: Clean dashboard, straightforward CLI
3. **Generous free credit**: $200 for 60 days covers extensive practice
4. **Fast provisioning**: Clusters ready in 4-5 minutes (vs 10-15 for AWS/GCP)

Your kubectl and Helm skills from Chapters 50-51 work identically on DOKS. The only difference is how you connect.

---

## Step 1: Create Your DigitalOcean Account

### Navigate to Signup

1. Open [cloud.digitalocean.com/registrations/new](https://cloud.digitalocean.com/registrations/new)
2. Choose signup method:
   - **Email**: Enter email and password
   - **Google**: Sign in with Google account
   - **GitHub**: Sign in with GitHub account

GitHub signup is convenient if you already use it for development.

### Verify Email

After signup, check your email for verification link. Click it to confirm your account.

### Add Payment Method

DigitalOcean requires a payment method before provisioning resources, even with free credit. This prevents abuse of free tier.

1. Navigate to **Settings > Billing**
2. Click **Add Payment Method**
3. Enter credit card details
4. DigitalOcean authorizes $1 (refunded immediately) to verify the card

**Important**: You won't be charged until your free credit expires AND you have active resources. The payment method is required to create an account.

### Claim Free Credit

New accounts receive **$200 free credit valid for 60 days**. This appears automatically after account verification. Confirm by checking:

1. Click your profile icon (top right)
2. Select **Billing**
3. Look for "Account Credit" showing $200.00

If you see $0 credit, look for promotional emails or check if your account was created before the current promotion period.

---

## Step 2: Generate an API Token

The DigitalOcean API token lets doctl (and other tools) manage your infrastructure programmatically. Think of it as a password specifically for CLI and automation access.

### Navigate to API Settings

1. Click your profile icon (top right)
2. Select **API**
3. Click **Generate New Token**

### Configure Token Settings

| Setting | Value | Why |
|---------|-------|-----|
| **Token name** | `doctl-cli` | Descriptive name for identifying this token later |
| **Expiration** | 90 days (or No expiry for learning) | Balance security vs convenience |
| **Scopes** | **Read and Write** | Required for creating clusters, deployments, load balancers |

### Understand Token Scopes

**Read scope** allows:
- Listing resources (droplets, clusters, domains)
- Viewing account information
- Checking balances and usage

**Write scope** adds:
- Creating resources (clusters, droplets, load balancers)
- Modifying configurations
- Deleting resources

For cluster provisioning, you need **read/write scope**. Read-only tokens cannot create DOKS clusters.

### Save Your Token Securely

After clicking **Generate Token**, you'll see the token value **once**. DigitalOcean does not store it.

```
dop_v1_a1b2c3d4e5f6...  # Example format
```

**Critical**: Copy this token immediately and store it securely:

- **macOS**: Store in Keychain Access
- **Linux**: Store in password manager or encrypted file
- **All platforms**: Never commit tokens to Git repositories

If you lose this token, you must revoke it and generate a new one.

---

## Step 3: Install doctl CLI

`doctl` is DigitalOcean's official command-line interface. It's your primary tool for managing cloud resources.

::::os-tabs

::macos
**Using Homebrew (recommended):**

```bash
brew install doctl
```

**Expected output:**
```
==> Downloading https://ghcr.io/v2/homebrew/core/doctl/manifests/1.104.0
==> Installing doctl
==> Pouring doctl--1.104.0.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/doctl/1.104.0: 8 files, 32.5MB
```

**Alternative (manual download):**

If you don't use Homebrew:

1. Download from [GitHub releases](https://github.com/digitalocean/doctl/releases)
2. Extract the archive
3. Move the binary to your PATH:

```bash
sudo mv doctl /usr/local/bin/
```

::windows
**Using Scoop (recommended):**

```powershell
scoop install doctl
```

**Using Chocolatey:**

```powershell
choco install doctl
```

**Alternative (manual download):**

1. Download `doctl-X.X.X-windows-amd64.zip` from [GitHub releases](https://github.com/digitalocean/doctl/releases)
2. Extract to a folder (e.g., `C:\doctl`)
3. Add that folder to your PATH environment variable

::linux
**Ubuntu/Debian (using Snap):**

```bash
sudo snap install doctl
```

**Expected output:**
```
doctl 1.104.0 from DigitalOcean (digitalocean) installed
```

**Alternative (using wget):**

```bash
# Download latest release
wget https://github.com/digitalocean/doctl/releases/download/v1.104.0/doctl-1.104.0-linux-amd64.tar.gz

# Extract
tar xf doctl-1.104.0-linux-amd64.tar.gz

# Move to PATH
sudo mv doctl /usr/local/bin/
```

::::

### Verify Installation

Confirm doctl installed correctly:

```bash
doctl version
```

**Expected output:**
```
doctl version 1.104.0-release
Git commit hash: a1b2c3d4
```

If you see `command not found`, your installation path may not be in your shell's PATH variable. Restart your terminal or add the installation directory to PATH.

---

## Step 4: Authenticate doctl

Now connect doctl to your DigitalOcean account using the API token.

### Initialize Authentication

```bash
doctl auth init
```

When prompted, paste your API token:

```
Please authenticate doctl for use with your DigitalOcean account. You can generate a token in the control panel at https://cloud.digitalocean.com/account/api/tokens

Enter your access token: [paste your token here]
```

**Expected output:**
```
Validating token... OK
```

doctl stores the token in your system's secure credential store:
- **macOS**: Keychain Access
- **Linux**: `~/.config/doctl/config.yaml` (file permissions restricted)
- **Windows**: Credential Manager

### Verify Connection

Confirm authentication works by querying your account:

```bash
doctl account get
```

**Expected output:**
```
Email                        Droplet Limit    Email Verified    UUID                                    Status
you@example.com              25               true              xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx    active
```

| Field | Meaning |
|-------|---------|
| **Email** | Your account email |
| **Droplet Limit** | Maximum VMs you can create (increases with usage history) |
| **Email Verified** | Must be `true` to create resources |
| **UUID** | Your unique account identifier |
| **Status** | Must be `active` to create resources |

If you see `Error: Unable to authenticate`, your token may be incorrect or expired. Generate a new token and run `doctl auth init` again.

---

## Understanding doctl Command Structure

doctl follows a consistent pattern:

```
doctl [resource] [action] [flags]
```

Common resources you'll use:

| Resource | Purpose | Example |
|----------|---------|---------|
| `account` | Account information | `doctl account get` |
| `kubernetes` | DOKS clusters | `doctl kubernetes cluster list` |
| `compute` | Droplets (VMs), load balancers | `doctl compute droplet list` |
| `apps` | App Platform deployments | `doctl apps list` |

Explore available commands:

```bash
doctl --help
```

**Expected output (abbreviated):**
```
doctl is a command-line interface (CLI) for the DigitalOcean API.

Usage:
  doctl [command]

Available Commands:
  account     Display commands that retrieve account details
  apps        Display commands for working with apps
  auth        Display commands for authenticating doctl with an account
  compute     Display commands that manage infrastructure
  databases   Display commands that manage databases
  kubernetes  Display commands for managing Kubernetes clusters and configurations
  ...
```

For cluster management specifically:

```bash
doctl kubernetes --help
```

---

## Security Best Practices

### Token Rotation

API tokens should be rotated periodically:

1. Generate a new token in the DigitalOcean dashboard
2. Run `doctl auth init` with the new token
3. Revoke the old token in the dashboard

For production environments, rotate tokens every 30-90 days.

### Multiple Contexts

If you have multiple DigitalOcean accounts (personal, work), doctl supports authentication contexts:

```bash
# Add a named context
doctl auth init --context work

# Switch between contexts
doctl auth switch --context work
doctl auth switch --context default

# List contexts
doctl auth list
```

### Environment Variables

For CI/CD pipelines or scripts, use environment variables instead of interactive auth:

```bash
export DIGITALOCEAN_ACCESS_TOKEN=dop_v1_your_token_here
doctl account get  # Uses token from environment
```

**Warning**: Never commit scripts containing hardcoded tokens. Use secret management tools (GitHub Secrets, HashiCorp Vault) in production.

---

## Troubleshooting Common Issues

### Issue: "Error: Unable to authenticate"

**Cause**: Token is invalid, expired, or has insufficient scope.

**Fix**:
1. Verify token in DigitalOcean dashboard (API section)
2. Check token hasn't expired
3. Ensure token has read/write scope
4. Generate a new token and re-run `doctl auth init`

### Issue: "command not found: doctl"

**Cause**: doctl not in PATH or not installed.

**Fix**:
- **macOS**: Run `brew install doctl` or add installation directory to PATH
- **Linux**: Ensure `/snap/bin` is in PATH for snap installs, or move binary to `/usr/local/bin`
- **Windows**: Add doctl directory to PATH environment variable

### Issue: "Droplet Limit: 0" in account get

**Cause**: New accounts may have zero limit until payment method verified.

**Fix**:
1. Ensure payment method is added in Billing settings
2. Wait 24 hours for account verification
3. Contact DigitalOcean support if issue persists

### Issue: Token works in browser but not doctl

**Cause**: Token may have been copied with extra whitespace.

**Fix**:
1. Copy token again, ensuring no leading/trailing spaces
2. Run `doctl auth init` and paste cleanly

---

## What You've Accomplished

Your cloud foundation is now ready:

| Component | Status | Purpose |
|-----------|--------|---------|
| **DigitalOcean Account** | Active | Access to managed Kubernetes |
| **Payment Method** | Added | Required for resource creation |
| **Free Credit** | $200 (60 days) | Practice without cost |
| **API Token** | Generated | Programmatic access |
| **doctl CLI** | Installed | Local cluster management |
| **Authentication** | Verified | Ready for cluster provisioning |

In Lesson 3, you'll use these credentials to provision your first DOKS cluster. The `kubectl` commands you learned in Chapter 50 will work identically—the only difference is the cluster runs on DigitalOcean's infrastructure instead of your laptop.

---

## Try With AI

Now that you have doctl configured, explore DigitalOcean's capabilities with your AI partner.

### Prompt 1: Explore Available Regions

```
I just authenticated doctl for DigitalOcean. Before I create a Kubernetes
cluster, I want to understand the available regions. Help me:

1. List all DigitalOcean regions using doctl
2. Understand which regions support DOKS (Kubernetes)
3. Choose a region based on:
   - My location (I'm in [your country/region])
   - Latency considerations
   - Pricing (if there are differences)

Show me the doctl commands and explain what the output means.
```

**What you're learning**: Understanding cloud geography. Region selection affects latency, compliance requirements, and sometimes pricing. Your AI partner helps you interpret doctl output and make informed decisions.

### Prompt 2: Understand Pricing Before Provisioning

```
I have $200 free credit on DigitalOcean for 60 days. I want to practice
Kubernetes without exhausting my credit. Help me understand:

1. What does a minimal DOKS cluster cost per month?
2. What are the hidden costs I should watch for (egress, load balancers)?
3. How can I monitor my spending with doctl or the dashboard?
4. What's the safest way to teardown resources to avoid charges?

I don't want any surprises on my credit card.
```

**What you're learning**: Cloud cost awareness. Unlike local Docker, cloud resources incur real costs. Understanding pricing before provisioning prevents bill shock and teaches you to build cost-conscious habits.

### Prompt 3: Compare Authentication Methods

```
I authenticated doctl using an API token. But I've heard about other
authentication methods for cloud CLIs. Compare for me:

1. API tokens (what I'm using)
2. OAuth flows
3. Service accounts

When would I use each? What are the security tradeoffs? I want to
understand this before I use these credentials in CI/CD pipelines.
```

**What you're learning**: Authentication patterns for cloud infrastructure. Understanding the security model helps you make appropriate choices for different environments (development, CI/CD, production).

**Safety note**: API tokens are powerful credentials. Anyone with your token can create or delete resources in your account. Treat tokens like passwords: rotate regularly, never share, and use environment variables instead of hardcoding in scripts.

---

## Reflect on Your Skill

You built a `multi-cloud-deployer` skill in Lesson 0. Test and improve it based on what you learned.

### Test Your Skill

```
Using my multi-cloud-deployer skill, verify I have DigitalOcean doctl properly
configured. Does my skill include authentication verification and account
status checks?
```

### Identify Gaps

Ask yourself:
- Did my skill include doctl installation for multiple platforms?
- Did it explain API token scope requirements (read vs read/write)?
- Did it include verification commands like `doctl account get`?

### Improve Your Skill

If you found gaps:

```
My multi-cloud-deployer skill is missing doctl setup verification. Update it
to include:
1. doctl authentication flow
2. API token scope explanation (why read/write is needed for clusters)
3. Account verification with expected output format
```

Your skill should now help others set up DigitalOcean access without re-reading this lesson.
