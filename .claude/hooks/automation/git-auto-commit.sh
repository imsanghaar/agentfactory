#!/usr/bin/env bash
# Automation: Auto-commit and push changes on session end
# Triggered by: Stop (or SessionEnd)
# Cloud-native hardened version

set -uo pipefail
export GIT_TERMINAL_PROMPT=0

INPUT="$(cat || true)"
[ -z "$INPUT" ] && exit 0

command -v jq >/dev/null 2>&1 || exit 0
command -v git >/dev/null 2>&1 || exit 0

SESSION_ID="$(echo "$INPUT" | jq -r '.session_id // empty' 2>/dev/null || true)"
CWD="$(echo "$INPUT" | jq -r '.cwd // empty' 2>/dev/null || true)"

[ -z "$SESSION_ID" ] && exit 0

REPO_ROOT="${CWD:-.}"
git -C "$REPO_ROOT" rev-parse --git-dir >/dev/null 2>&1 || exit 0

GIT_DIR="$(git -C "$REPO_ROOT" rev-parse --git-dir)"
LOCKFILE="$GIT_DIR/git-auto-push.lock"
LOG_FILE="$GIT_DIR/git-auto-push.log"

exec 9>"$LOCKFILE" || exit 0
if command -v flock >/dev/null 2>&1; then
    flock -n 9 || exit 0
fi

log_msg() {
    echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ")|$*" >> "$LOG_FILE"
}

log_msg "INFO|Session ${SESSION_ID:0:8}|Starting"

# Ensure git identity
if ! git -C "$REPO_ROOT" config user.email >/dev/null 2>&1; then
    git -C "$REPO_ROOT" config user.email "claude-code@local" >/dev/null 2>&1 || true
fi
if ! git -C "$REPO_ROOT" config user.name >/dev/null 2>&1; then
    git -C "$REPO_ROOT" config user.name "Claude Code" >/dev/null 2>&1 || true
fi

CURRENT_BRANCH="$(git -C "$REPO_ROOT" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")"

# Safety: don't auto-commit on main/master
if [ "$CURRENT_BRANCH" = "main" ] || [ "$CURRENT_BRANCH" = "master" ] || [ "$CURRENT_BRANCH" = "HEAD" ]; then
    log_msg "INFO|Skipping auto-commit on $CURRENT_BRANCH"
    exit 0
fi

# Stage all changes
git -C "$REPO_ROOT" add -A >/dev/null 2>&1 || exit 0

# Check if anything staged
git -C "$REPO_ROOT" diff --cached --quiet && exit 0

# Commit
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
COMMIT_MSG="Session ${SESSION_ID:0:8} - $TIMESTAMP

Co-Authored-By: Claude <noreply@anthropic.com>"

if git -C "$REPO_ROOT" commit -m "$COMMIT_MSG" >/dev/null 2>&1; then
    log_msg "INFO|Committed session ${SESSION_ID:0:8}"
else
    log_msg "ERROR|Commit failed"
    exit 0
fi

# Push with timeout and retry
PENDING_FILE="$GIT_DIR/push-pending"
echo "$CURRENT_BRANCH" > "$PENDING_FILE" 2>/dev/null || true

for i in 1 2; do
    if timeout 6 git -C "$REPO_ROOT" push origin "$CURRENT_BRANCH" >/dev/null 2>&1; then
        log_msg "INFO|Push succeeded"
        rm -f "$PENDING_FILE" 2>/dev/null || true
        break
    fi
    [ $i -lt 2 ] && sleep 1
done

exit 0
