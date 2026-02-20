---
description: Sync main branch from ai-native-software-development to sso-mirror-mono
---

# SSO Sync Command

Sync the SSO codebase from `https://github.com/panaversity/ai-native-software-development` to the mirror at `https://github.com/panaversity-global/sso-mirror-mono.git`.

## Execution Steps

1. **Verify Remote Exists**

   ```bash
   git remote -v | grep sso-sync
   ```

   If `sso-sync` remote doesn't exist, add it:

   ```bash
   git remote add sso-sync https://github.com/panaversity-global/sso-mirror-mono.git
   ```

2. **Verify Current Branch**

   ```bash
   git rev-parse --abbrev-ref HEAD
   git log --oneline -3
   ```

3. **Force Push to sso-sync**

   ```bash
   git push sso-sync main --force
   ```

4. **Report Result**
   Report the sync status:
   - Commit hash pushed
   - Success/failure status
   - Any warnings

## Notes

- This command always force pushes, overwriting any divergent history on sso-sync
- Only syncs the `main` branch
- Source: `https://github.com/panaversity/ai-native-software-development`
- Destination: `https://github.com/panaversity-global/sso-mirror-mono.git`
