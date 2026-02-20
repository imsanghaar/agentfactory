#!/usr/bin/env bash
# Guardrail: Verify infrastructure context before dangerous commands
# Triggered by: PreToolUse on Bash
# Shows current context as warning, doesn't block

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

COMMAND=$(parse_json "$INPUT" "tool_input.command" 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

[ -z "$COMMAND" ] && exit 0

# Check if this is an infrastructure command
if ! is_infra_command "$COMMAND"; then
    exit 0
fi

# Build context info
CONTEXT_INFO=""

# Kubernetes context
if echo "$COMMAND" | grep -qw "kubectl\|helm" 2>/dev/null; then
    K8S_CONTEXT=$(verify_k8s_context)
    CONTEXT_INFO="${CONTEXT_INFO}K8s context: $K8S_CONTEXT\n"

    # Warn if pointing to production
    if echo "$K8S_CONTEXT" | grep -qiE "prod|production|live" 2>/dev/null; then
        CONTEXT_INFO="${CONTEXT_INFO}WARNING: Production cluster detected!\n"
        audit_log "infra_warning" "$SESSION_ID" "$K8S_CONTEXT" "production_access" "kubectl/helm command targeting production"
    fi
fi

# Docker context
if echo "$COMMAND" | grep -qw "docker" 2>/dev/null; then
    DOCKER_CONTEXT=$(verify_docker_context)
    CONTEXT_INFO="${CONTEXT_INFO}Docker context: $DOCKER_CONTEXT\n"
fi

# AWS/Cloud context
if echo "$COMMAND" | grep -qw "aws" 2>/dev/null; then
    AWS_PROFILE="${AWS_PROFILE:-default}"
    AWS_REGION="${AWS_DEFAULT_REGION:-us-east-1}"
    CONTEXT_INFO="${CONTEXT_INFO}AWS: profile=$AWS_PROFILE region=$AWS_REGION\n"
fi

# Output context info (shown to user, not blocking)
if [ -n "$CONTEXT_INFO" ]; then
    echo -e "Infrastructure Context:\n$CONTEXT_INFO"
fi

exit 0
