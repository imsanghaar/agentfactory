#!/usr/bin/env bash
# Guardrail: Block destructive commands in production environments
# Triggered by: PreToolUse on Bash
# Exit 2 = BLOCK with message to Claude

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

COMMAND=$(parse_json "$INPUT" "tool_input.command" 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

[ -z "$COMMAND" ] && exit 0

# Destructive patterns to block
DESTRUCTIVE_PATTERNS=(
    "rm -rf /"
    "rm -rf /*"
    "rm -rf ~"
    "rm -rf ."
    ":(){ :|:& };:"     # Fork bomb
    "mkfs"
    "dd if=/dev/zero"
    "> /dev/sda"
    "chmod -R 777 /"
    "DROP DATABASE"
    "DROP TABLE"
    "TRUNCATE"
    "--force --all"
    "kubectl delete namespace"
    "kubectl delete -A"
    "helm uninstall --all"
    "terraform destroy -auto-approve"
)

for pattern in "${DESTRUCTIVE_PATTERNS[@]}"; do
    if echo "$COMMAND" | grep -qiF "$pattern" 2>/dev/null; then
        audit_log "destructive_blocked" "$SESSION_ID" "$COMMAND" "blocked" "Destructive command pattern: $pattern"
        notify_team "Destructive Command Blocked" "Session $SESSION_ID attempted: $COMMAND" "critical"
        echo "BLOCKED: This command matches a destructive pattern ($pattern) and cannot be executed automatically." >&2
        exit 2
    fi
done

exit 0
