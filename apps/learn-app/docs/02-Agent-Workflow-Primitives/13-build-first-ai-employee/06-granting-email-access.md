---
sidebar_position: 6
title: "Granting Email Access"
sidebar_label: "L06: Granting Email Access"
description: "Connect Claude Code to your Gmail inbox using the Gmail MCP server. Configure SMTP App Password (2 min) or OAuth (10 min) and apply essential safety protocols."
series: "email"
series_position: 6
keywords:
  - Gmail MCP
  - Claude Code email
  - MCP authentication
  - OAuth Gmail
  - SMTP App Password
  - email automation
  - Gmail API
  - AI email assistant
chapter: 10
lesson: 6
duration_minutes: 30

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "MCP protocol concepts from Chapter 3, Gmail authentication basics"
layer_2_collaboration: "Co-configuring Gmail MCP with AI assistance, testing tools iteratively, establishing safety protocols through collaborative refinement"
layer_3_intelligence: "N/A (lesson teaches configuration, not creating new MCP servers)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Gmail MCP Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can configure Gmail MCP with either SMTP or OAuth authentication and verify connection works"
  - name: "Google App Password Creation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can generate Google App Password and use it for SMTP authentication"
  - name: "OAuth Credential Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can create Google Cloud project, enable Gmail API, and configure OAuth credentials"
  - name: "Gmail MCP Tool Usage"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can invoke Gmail MCP tools (search, draft, send, labels) and interpret results"
  - name: "Email Safety Protocols"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can apply draft-first workflow and identify sensitive data that should not be included in AI prompts"

learning_objectives:
  - objective: "Understand Gmail MCP Server architecture and its 19 available tools"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain the categories of Gmail MCP tools and when each would be used"
  - objective: "Configure Gmail MCP with SMTP and App Password authentication (2-minute path)"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully connect Gmail MCP using App Password and verify with list_email_labels"
  - objective: "Configure Gmail MCP with OAuth authentication (10-minute path)"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully connect Gmail MCP using OAuth credentials from Google Cloud Console"
  - objective: "Test Gmail MCP tools including search, draft, send, and label operations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Execute at least 3 different Gmail MCP tools and verify expected results"
  - objective: "Apply safety protocols including draft-first workflow and sensitive data handling"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Identify which operations require draft review and list data categories to exclude from AI context"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (Gmail MCP architecture, SMTP auth, OAuth auth, Gmail tools, safety protocols, skill integration) - within B1 limit of 7-10 concepts"

differentiation:
  extension_for_advanced: "Configure OAuth with multiple scopes, create custom filters programmatically, integrate Gmail MCP with email-assistant orchestrator skill"
  remedial_for_struggling: "Focus on SMTP App Password method only (simpler), test with list_email_labels before attempting send operations"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 2
  session_title: "Gmail MCP Integration"
  key_points:
    - "Gmail MCP is the Action Layer from L00's architecture — it bridges the gap between 'Claude can draft emails' and 'Claude can actually read/send emails'"
    - "Two auth paths serve different needs: SMTP App Password (2 min, basic) for testing vs OAuth (10 min, full API) for production — students should start with SMTP"
    - "The draft-first rule is the most important safety protocol — important emails go through draft_email, not send_email, so humans review before sending"
    - "The integration diagram showing Skills + MCP + Subagents working together is the first complete view of how all Bronze tier components connect"
  misconceptions:
    - "Students think they are giving Claude their Gmail password — App Passwords and OAuth tokens are limited-access credentials, not the account password"
    - "Students assume SMTP and OAuth are interchangeable — SMTP only supports send/receive, while OAuth unlocks all 19 tools including labels and filters"
    - "Students skip the safety protocols section thinking it is just warnings — the draft-first workflow and sensitive data handling rules are essential for real use"
    - "Students expect Gmail MCP to work offline — it requires active internet and valid authentication; the lesson covers what happens when it is unavailable"
  discussion_prompts:
    - "The draft-first rule table categorizes which emails to draft vs send directly. Where would YOU draw the line for your own email categories?"
    - "Why does the lesson recommend starting with SMTP for testing even though OAuth is more powerful? What does this teach about integration strategy?"
    - "The sensitive data handling section says to 'reference information by description, not value.' What other categories of data should never appear in AI prompts?"
  teaching_tips:
    - "Do the SMTP App Password setup as a live walkthrough — most students hit 2FA issues or cannot find the App Passwords page"
    - "Test with list_email_labels FIRST (read-only, harmless) before attempting any write operations — this builds confidence and catches auth errors early"
    - "The troubleshooting section covers the 4 most common errors — review these BEFORE students start setup to set expectations"
    - "Skip OAuth in class unless students specifically need label/filter management — the 10-minute path often takes 20+ minutes with Google Cloud Console navigation"
  assessment_quick_check:
    - "What is the difference between SMTP App Password and OAuth authentication? When would you choose each?"
    - "Name three Gmail MCP tools and explain when each would be used"
    - "What is the draft-first rule and why is it important for email automation safety?"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-01-01"
version: "1.0.0"
---

# Granting Email Access

You've built skills that draft professional emails. You've created subagents that triage inbox priorities and suggest responses. But there's a gap: your Email Assistant can't actually read or send emails. It's like having a brilliant assistant who can write perfect letters but has no mailbox.

The Gmail MCP server bridges this gap. It gives Claude Code direct, authenticated access to your Gmail inbox — not simulated emails, but your actual messages. Search for emails from your boss. Draft responses that appear in your Gmail Drafts folder. Send messages when you're confident they're ready. With 19 specialized tools, Gmail MCP transforms your Email Assistant from a writing helper into a complete communication system.

This lesson walks you through two authentication paths: the quick SMTP method (2 minutes with an App Password) and the comprehensive OAuth method (10 minutes with full API access). You'll test the connection, explore the available tools, and establish safety protocols that protect you from automation mistakes.

---

## Gmail MCP Architecture

The Gmail MCP server acts as a secure bridge between Claude Code and your Gmail account. Here's how the components connect:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Claude Code   │────▶│   Gmail MCP     │────▶│   Gmail API     │
│   (Your Agent)  │     │   (Bridge)      │     │   (Your Inbox)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
   "Search for                  │                 Authenticated
   emails from                  │                 API requests
   boss@company.com"      19 specialized
                          tools available
```

**The key insight**: You're not giving Claude Code your Gmail password. Instead, Gmail MCP uses either an App Password (limited access token) or OAuth credentials (Google's official authorization system) to make authenticated requests on your behalf.

---

## The 19 Gmail MCP Tools

Gmail MCP provides a comprehensive toolkit organized into four categories:

### Email Operations (Core)

| Tool                  | Purpose                   | Example Use                           |
| --------------------- | ------------------------- | ------------------------------------- |
| `send_email`          | Send email immediately    | Routine messages after review         |
| `draft_email`         | Create draft for review   | Important messages requiring approval |
| `read_email`          | Get full email content    | Understanding thread context          |
| `search_emails`       | Find emails by query      | "Emails from boss this week"          |
| `modify_email`        | Change labels/read status | Mark as read, archive                 |
| `delete_email`        | Remove email permanently  | Cleanup old messages                  |
| `batch_modify_emails` | Bulk label operations     | Archive all newsletters               |
| `batch_delete_emails` | Bulk deletion             | Clear spam folder                     |
| `download_attachment` | Save file from email      | Extract report attachments            |

### Label Management

| Tool                        | Purpose                 | Example Use           |
| --------------------------- | ----------------------- | --------------------- |
| `list_email_labels`         | Show all labels         | See inbox structure   |
| `create_gmail_label`        | Create new label        | Organize by project   |
| `update_gmail_label`        | Modify label properties | Change label color    |
| `delete_gmail_label`        | Remove label            | Cleanup unused labels |
| `get_or_create_gmail_label` | Ensure label exists     | Idempotent setup      |

### Filter Management

| Tool                          | Purpose               | Example Use              |
| ----------------------------- | --------------------- | ------------------------ |
| `create_gmail_filter`         | Set up auto-rules     | Auto-archive newsletters |
| `list_gmail_filters`          | Show existing filters | Audit current automation |
| `get_gmail_filter`            | View filter details   | Debug filter behavior    |
| `delete_gmail_filter`         | Remove filter         | Disable auto-processing  |
| `create_filter_from_template` | Quick filter setup    | Common patterns          |

---

## Authentication: Two Paths

Gmail MCP supports two authentication methods. Choose based on your needs:

| Method                  | Setup Time  | Access Level       | Best For                         |
| ----------------------- | ----------- | ------------------ | -------------------------------- |
| **SMTP + App Password** | ~2 minutes  | Basic send/receive | Quick testing, simple automation |
| **OAuth**               | ~10 minutes | Full API access    | Production use, all 19 tools     |

**Recommendation**: Start with SMTP for this lesson. Move to OAuth if you need label management, filters, or batch operations.

---

## Path A: SMTP Authentication (2 Minutes)

This method uses Google's App Passwords — special 16-character passwords that grant limited access without exposing your main account credentials.

### Step 1: Generate an App Password

**Requirements**: Your Google account must have 2-Factor Authentication enabled.

1. Open [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Sign in if prompted
3. Under "App name", type: `Gmail MCP`
4. Click **Create**
5. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)

**Important**: Save this password immediately — Google only shows it once. Store it in a password manager, not a plain text file.

### Step 2: Add Gmail MCP to Claude Code

Choose your scope:

| Scope                           | Flag              | Use When                       |
| ------------------------------- | ----------------- | ------------------------------ |
| 🌍 **User Scope** (Recommended) | `--scope user`    | Available in all your projects |
| 📁 **Project Scope**            | `--scope project` | Only in current project        |

**Project scope** (current project only):

```bash
claude mcp add gmail --transport http \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Email: your-email@gmail.com" \
  --header "X-Gmail-Password: xxxx-xxxx-xxxx-xxxx"
```

**User scope** (available in all projects - recommended):

```bash
claude mcp add gmail --transport http --scope user \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Email: your-email@gmail.com" \
  --header "X-Gmail-Password: xxxx-xxxx-xxxx-xxxx"
```

**Replace these values:**

- `your-email@gmail.com` → Your actual Gmail address
- `xxxx-xxxx-xxxx-xxxx` → The 16-character App Password you generated

**Output:**

```
Added gmail to user settings
```

:::warning .mcp.json Conflict
If you have a `.mcp.json` file in your project with a `gmail` server configured, it may override your `claude mcp add` config. Either:

- Delete the conflicting entry from `.mcp.json`, or
- Use a different server name (e.g., `gmail-smtp`)
  :::

### Step 3: Verify Connection

Test that Gmail MCP is working:

```bash
claude mcp list
```

**Output:**

```
gmail: connected
  Transport: HTTP (remote)
  Endpoint: https://deep-red-marten.fastmcp.app/mcp
  Tools: 19
```

If you see `Tools: 19`, your connection is working.

---

## Path B: OAuth Authentication (10 Minutes)

OAuth provides full API access and is required for label management, filters, and some advanced operations. This method is more complex but more powerful.

### Step 1: Create Google Cloud Project

1. Open [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown (top left, near the Google Cloud logo)
3. Click **New Project**
4. Enter project name: `gmail-mcp-integration`
5. Click **Create**
6. Wait for project creation (30-60 seconds)

### Step 2: Enable Gmail API

1. In your new project, go to **APIs & Services** > **Library**
2. Search for "Gmail API"
3. Click **Gmail API** in results
4. Click **Enable**

**Output confirmation**: You'll see "Gmail API" appear in your Enabled APIs list.

### Step 3: Configure OAuth Consent Screen

1. Go to [Google Auth Platform](https://console.cloud.google.com/auth/overview) (or **APIs & Services** > **OAuth consent screen**)
2. If prompted, click **Get Started** or **Configure Consent Screen**
3. Select **External** → Click **Create**

**Configure Branding** (left sidebar):

1. App name: `Gmail MCP`
2. User support email: Your email
3. Developer contact: Your email
4. Click **Save**

**Configure Data Access** (left sidebar):

1. Click **Add or Remove Scopes**
2. In the filter, search for `gmail`
3. Select these scopes:
   - `https://www.googleapis.com/auth/gmail.modify`
   - `https://www.googleapis.com/auth/gmail.settings.basic`
4. Click **Update** → **Save**

**Configure Audience** (left sidebar):

1. Click **Add Users**
2. Add your Gmail address
3. Click **Save**

**Publish Your App** (Summary in left sidebar):

1. Click **Publish App** to move from "Testing" to "In Production"
2. This allows your app to request full permissions needed for all Gmail MCP tools

:::tip Why Publish?
While in "Testing" mode, tokens expire after 7 days. Publishing removes this limitation for your own use.
:::

### Step 4: Create OAuth Credentials

1. Go to **Clients** (left sidebar) or **APIs & Services** > **Credentials**
2. Click **Create Client** or **Create Credentials** > **OAuth client ID**
3. Application type: **Web application**
4. Name: `Gmail MCP`
5. Under **Authorized redirect URIs**, click **Add URI** and enter:
   ```
   https://developers.google.com/oauthplayground
   ```
6. Click **Create**
7. Copy your **Client ID** and **Client Secret** (save them securely!)

### Step 5: Get Refresh Token (OAuth Playground)

1. Go to [Google OAuth Playground](https://developers.google.com/oauthplayground)
2. Click ⚙️ **Settings** (gear icon, top right)
3. Check ✅ **Use your own OAuth credentials**
4. Enter your **Client ID** and **Client Secret**
5. Close settings
6. In left panel, find **Gmail API v1** and select:
   - `https://www.googleapis.com/auth/gmail.modify`
   - `https://www.googleapis.com/auth/gmail.settings.basic`
7. Click **Authorize APIs**
8. Sign in with your Google account and click **Allow**
9. Click **Exchange authorization code for tokens**
10. Copy the **Refresh Token** from the response

### Step 6: Add Gmail MCP with OAuth

Choose your scope:

| Scope                           | Flag           | Use When                       |
| ------------------------------- | -------------- | ------------------------------ |
| 🌍 **User Scope** (Recommended) | `--scope user` | Available in all your projects |
| 📁 **Project Scope**            | (default)      | Only in current project        |

**Project scope** (current project only):

```bash
claude mcp add gmail --transport http \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Client-Id: YOUR_CLIENT_ID" \
  --header "X-Gmail-Client-Secret: YOUR_CLIENT_SECRET" \
  --header "X-Gmail-Refresh-Token: YOUR_REFRESH_TOKEN"
```

**User scope** (available in all projects - recommended):

```bash
claude mcp add gmail --transport http --scope user \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Client-Id: YOUR_CLIENT_ID" \
  --header "X-Gmail-Client-Secret: YOUR_CLIENT_SECRET" \
  --header "X-Gmail-Refresh-Token: YOUR_REFRESH_TOKEN"
```

**Replace the placeholder values with your actual credentials.**

**Output:**

```
Added gmail to user settings
```

:::warning .mcp.json Conflict
If you have a `.mcp.json` file in your project with a `gmail` server configured for SMTP, it may override your OAuth config. Either:

- Update `.mcp.json` to use OAuth headers, or
- Delete the `gmail` entry from `.mcp.json`, or
- Use a different server name (e.g., `gmail-oauth`)
  :::

**Available Tools with OAuth:**

| Category              | Tools                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------ |
| **Email Operations**  | `send_email`, `draft_email`, `read_email`, `search_emails`, `modify_email`, `delete_email` |
| **Label Management**  | `list_email_labels`, `create_gmail_label`, `delete_gmail_label`                            |
| **Filter Management** | `create_gmail_filter`, `list_gmail_filters`, `delete_gmail_filter`                         |

---

## Testing Your Connection

Once authenticated (either method), test that Gmail MCP works correctly.

### Test 1: List Labels

Open Claude Code and ask:

```
List my Gmail labels
```

**Expected output:**

```
You: List my Gmail labels
Claude: [Uses list_email_labels tool]
Found 12 labels:
- INBOX (42 unread)
- SENT
- DRAFTS (3)
- STARRED
- IMPORTANT
- TRASH
- SPAM
- Category/Primary
- Category/Social
- Category/Updates
- Projects/Q4-Planning
- Clients/Acme-Corp
```

If you see your labels, the connection works.

### Test 2: Search Emails

```
Search for emails from my boss in the last week
```

Claude interprets this and constructs the Gmail search query:

```
You: Search for emails from my boss in the last week
Claude: [Uses search_emails tool with query "from:boss@company.com after:2025/12/25"]
Found 3 emails:
1. "Q4 Review Meeting" - Dec 30
   From: boss@company.com
   Preview: "Following up on our discussion about..."

2. "Budget Approval Needed" - Dec 28
   From: boss@company.com
   Preview: "Please review the attached budget..."

3. "Team Update" - Dec 27
   From: boss@company.com
   Preview: "Great work on the project milestone..."
```

### Test 3: Create a Draft

```
Draft an email to john@example.com about rescheduling our meeting to next Tuesday at 3pm
```

**Expected output:**

```
You: Draft an email to john@example.com about rescheduling our meeting
Claude: [Uses draft_email tool]
Draft created successfully!

To: john@example.com
Subject: Rescheduling Our Meeting

Hi John,

I hope this message finds you well. I need to reschedule our meeting
to next Tuesday at 3pm. Would that time work for you?

Please let me know if you need to adjust the time.

Best regards

---
Draft saved to Gmail. View in Gmail: [link to Drafts folder]
```

The draft appears in your actual Gmail Drafts folder. You can review and edit it in Gmail before sending.

---

## Safety Protocols

Email automation is powerful but risky. A typo in a recipient address or an AI-generated phrase that doesn't match your intent can cause real problems. These protocols protect you.

### The Draft-First Rule

**For important emails, always use `draft_email` before `send_email`.**

| Message Type               | Recommended Approach                      |
| -------------------------- | ----------------------------------------- |
| Cold outreach to clients   | Draft → Review in Gmail → Send manually   |
| Follow-ups with colleagues | Draft → Quick review → Send via Claude    |
| Internal team updates      | Send directly (lower risk)                |
| Anything with attachments  | Draft → Verify attachment → Send manually |
| Emails to executives       | Draft → Review tone → Send manually       |

**Implementation**: Tell Claude your preference:

```
Always create drafts for emails to external recipients.
Only use send_email for internal team messages after I confirm.
```

### Sensitive Data Handling

**Never include in your prompts:**

| Data Category               | Why It's Risky              |
| --------------------------- | --------------------------- |
| Passwords                   | Could be logged or cached   |
| Financial account numbers   | PII exposure                |
| Personal health information | Privacy regulations (HIPAA) |
| Social Security Numbers     | Identity theft risk         |
| API keys or tokens          | Security breach potential   |

**Safe alternative**: Reference information by description, not value:

```
# WRONG - exposes sensitive data
"Send payment confirmation with account number 1234-5678-9012"

# CORRECT - references without exposing
"Send payment confirmation referencing the account on file"
```

### Email Safety Checklist

Before any automated send operation:

- [ ] **Verify recipient address** — Is this the right person?
- [ ] **Review subject line** — Does it accurately describe the content?
- [ ] **Check for AI-generated errors** — Names spelled correctly? Dates accurate?
- [ ] **Confirm attachments** — Are the right files attached?
- [ ] **Test with yourself first** — Send to your own address before external recipients

### Recovery Procedures

**If you send an email in error:**

1. **Within 30 seconds**: Use Gmail's "Undo Send" feature (if enabled)
2. **After 30 seconds**: Send a follow-up correction email immediately
3. **For serious errors**: Contact recipient directly (phone if necessary)

**Enable Undo Send**: Gmail Settings > General > "Undo Send" > Set to 30 seconds

---

## Integrating Gmail MCP with Your Skills

Gmail MCP becomes most powerful when combined with the skills you've already built.

### Connection Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    Email Assistant System                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Skills (Expertise)          MCP (Access)                  │
│   ┌───────────────────┐      ┌───────────────────┐         │
│   │ /email-drafter    │──────▶│ draft_email      │         │
│   │ Tone guidelines   │      │ send_email       │         │
│   └───────────────────┘      └───────────────────┘         │
│                                                             │
│   ┌───────────────────┐      ┌───────────────────┐         │
│   │ /email-summarizer │◀─────│ read_email       │         │
│   │ Thread parsing    │      │ search_emails    │         │
│   └───────────────────┘      └───────────────────┘         │
│                                                             │
│   Subagents (Reasoning)                                     │
│   ┌───────────────────┐      ┌───────────────────┐         │
│   │ inbox-triager     │◀────▶│ list_email_labels │         │
│   │ Priority rules    │      │ modify_email     │         │
│   └───────────────────┘      └───────────────────┘         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Example: Complete Workflow

Here's how the components work together:

```
You: Triage my inbox and draft responses to urgent emails

Claude:
1. [Uses search_emails] Scanning inbox...
   Found 23 unread messages

2. [Uses inbox-triager subagent] Prioritizing...
   - 3 urgent (client emails awaiting response)
   - 8 important (team updates)
   - 12 routine (newsletters, notifications)

3. [Uses read_email] Reading urgent emails...
   Email 1: Client asking for project status
   Email 2: Vendor invoice question
   Email 3: Partner meeting request

4. [Uses /email-drafter skill] Drafting responses...

   Draft 1: Project status update to client
   Draft 2: Invoice clarification to vendor
   Draft 3: Meeting confirmation to partner

5. [Uses draft_email] Creating drafts in Gmail...
   All 3 drafts saved. Ready for your review.
```

---

## Troubleshooting Common Issues

### "Authentication Failed" Error

**Symptoms**: Gmail MCP can't connect after setup.

**Solutions**:

1. **App Password method**: Regenerate the App Password and try again
2. **OAuth method**: Check that refresh token hasn't expired; re-authorize if needed
3. **Both methods**: Verify 2FA is enabled on your Google account

### "Insufficient Permission" Error

**Symptoms**: Some tools work but others fail.

**Solution**: This usually means OAuth scopes are incomplete. Re-run the OAuth Playground step and ensure you select all required scopes.

### "Rate Limited" Error

**Symptoms**: Tools work initially but fail after many operations.

**Solution**: Gmail API has rate limits. Wait 60 seconds and try again. For production use, implement exponential backoff.

### Drafts Not Appearing

**Symptoms**: `draft_email` returns success but you don't see the draft.

**Solutions**:

1. Check the Gmail Drafts folder (not Inbox)
2. Refresh your Gmail page
3. Check if drafts are synced across devices (may take 30-60 seconds)

---

## Try With AI

**Setup:** Open Claude Code with Gmail MCP configured (either SMTP or OAuth method).

**Prompt 1: Explore Your Inbox**

```
Use Gmail MCP to give me an overview of my inbox. Show me:
1. How many unread emails I have
2. My top 3 most active labels
3. Any emails from the last 24 hours that might need urgent attention

After showing results, suggest which email I should respond to first and why.
```

**What you're learning:** This tests the search and analysis capabilities of Gmail MCP. You're seeing how Claude interprets "urgent" based on sender, subject, and timing. Notice whether the AI's prioritization matches your own judgment — this reveals where you might want to add custom priority rules to your skills.

**Prompt 2: Draft with Safety**

```
Draft a follow-up email to a client about our project status. The client is
Maria Santos at Acme Corp. The project is on track for the January 15 deadline.

Before creating the draft:
1. Search for any recent emails from Maria to understand our latest context
2. Apply my email-drafter tone guidelines
3. Create the draft for my review (don't send)

Show me the draft and explain what context you used from previous emails.
```

**What you're learning:** This demonstrates the integration between Gmail MCP (search, draft) and your skills (tone guidelines). The search-before-draft pattern ensures your response builds on existing conversation context rather than starting fresh. Evaluate: Did Claude find relevant context? Did the tone match your guidelines?

**Prompt 3: Establish Your Safety Workflow**

```
Help me set up a safe email automation workflow. Based on my actual inbox:
1. Identify which senders I email most frequently
2. Categorize them as "safe for auto-send" vs "always draft-first"
3. Create a simple rule document I can reference

Show me the category list and ask for my feedback before finalizing.
```

**What you're learning:** This builds your personal safety protocol based on real data from your inbox. The collaborative aspect — Claude proposes, you refine — ensures the final rules match your actual risk tolerance. This becomes a reusable reference for future automation.

**Safety Note:** When testing Gmail MCP, start with read-only operations (search, list labels) before attempting write operations (draft, send). Always verify drafts in Gmail before sending. For your first send test, use your own email address as the recipient.
