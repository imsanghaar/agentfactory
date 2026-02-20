---
title: "Summary: Connecting Google Workspace"
sidebar_label: "Summary"
sidebar_position: 7.5
---

# Summary: Connecting Google Workspace

## Key Concepts

- **gog** is a unified CLI that bridges OpenClaw and Google Workspace, supporting Gmail, Calendar, Drive, Contacts, Sheets, and Docs through a single OAuth setup
- OAuth credentials are created once in Google Cloud Console and registered with `gog auth credentials`
- Your agent accesses Google services through subcommands (`gog gmail`, `gog calendar`, `gog drive`) with JSON output for automation
- Connecting real productivity tools is what crosses the line from demo to daily-use AI Employee
- The lethal trifecta from L05 becomes concrete once your agent has OAuth access to your actual data

## Setup Quick Reference

| Step                       | Command                                                      |
| -------------------------- | ------------------------------------------------------------ |
| Install gog                | `brew install steipete/tap/gogcli`                           |
| Register OAuth credentials | `gog auth credentials ~/Downloads/client_secret_*.json`      |
| Authorize account          | `gog auth add you@gmail.com`                                 |
| Limit scope (optional)     | `gog auth add you@gmail.com --services gmail,calendar,drive` |
| Set default account        | `export GOG_ACCOUNT=you@gmail.com`                           |
| Verify connection          | `gog auth list`                                              |
| Test Gmail access          | `gog gmail labels list`                                      |

## Common Mistakes

- Granting all 6 service scopes when you only need 2-3 -- apply least privilege
- Skipping the GCP Console API enablement step, then wondering why gog commands fail
- Sharing `client_secret.json` or screenshots showing email content in shared environments
- Forgetting to add your email as a test user in the OAuth consent screen (causes auth failures)
- Not adding `export GOG_ACCOUNT=...` to your shell profile, requiring it every session

## Security Reminder

- OAuth access makes the lethal trifecta real: your agent now has private data (email), untrusted content (incoming messages from anyone), and external communication (can send email)
- Apply least privilege: grant only the services your agent actually needs
- Every security rule from L05 applies with higher stakes after connecting Google Workspace
- A malicious skill with gog access could read email, send messages from your account, or exfiltrate documents
- Consider using a dedicated test Google account rather than your primary one when learning
