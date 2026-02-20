#!/usr/bin/env bash
# Ultimate Team Hooks: Common Utilities v4.0
# Full observability, guardrails, and team collaboration
# Cross-platform: Windows (Git Bash), macOS, Linux

# ============================================================================
# PATHS & TEAM-AWARE LOG ORGANIZATION
# ============================================================================

HOOKS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$HOOKS_DIR/../.." && pwd)"

# Team-aware log organization: logs/{user}/{branch}/{date}/
get_user() {
    # Priority: env var > git config > whoami
    if [ -n "${CLAUDE_USER:-}" ]; then
        echo "$CLAUDE_USER"
    elif command -v git &>/dev/null; then
        git config user.name 2>/dev/null | tr ' ' '_' | tr -cd '[:alnum:]_-' || whoami
    else
        whoami
    fi
}

get_branch() {
    if command -v git &>/dev/null; then
        git -C "$ROOT_DIR" branch --show-current 2>/dev/null | tr '/' '_' || echo "unknown"
    else
        echo "unknown"
    fi
}

get_date() {
    date -u +"%Y-%m-%d" 2>/dev/null || echo "unknown"
}

# Dynamic log directory: .claude/logs/{user}/{branch}/{date}/
get_log_dir() {
    local user=$(get_user)
    local branch=$(get_branch)
    local date=$(get_date)
    echo "$ROOT_DIR/.claude/logs/$user/$branch/$date"
}

# Create all required directories
init_dirs() {
    local log_dir=$(get_log_dir)
    mkdir -p "$log_dir" 2>/dev/null || true
    mkdir -p "$ROOT_DIR/.claude/context" 2>/dev/null || true
    mkdir -p "$ROOT_DIR/.claude/context/tasks" 2>/dev/null || true
    mkdir -p "$ROOT_DIR/.claude/context/subagents" 2>/dev/null || true
    mkdir -p "$ROOT_DIR/.claude/handoffs" 2>/dev/null || true
}

# Initialize on source
init_dirs

# Convenience aliases
LOGS_DIR=$(get_log_dir)
CONTEXT_DIR="$ROOT_DIR/.claude/context"

# ============================================================================
# TEAM CONFIGURATION
# ============================================================================

TEAM_WEBHOOK_URL="${CLAUDE_TEAM_WEBHOOK:-}"

PROTECTED_PATTERNS=(
    ".env" "*.pem" "*.key" "secrets/*" "credentials*"
    "package-lock.json" "pnpm-lock.yaml" "yarn.lock"
    "Dockerfile" "docker-compose*.yml"
    "*.tf" "*.tfvars" "k8s/*" "helm/*"
)

INFRA_COMMANDS=("kubectl" "helm" "docker" "terraform" "aws" "gcloud" "az")

# ============================================================================
# JSON UTILITIES
# ============================================================================

get_python_cmd() {
    if python3 --version &>/dev/null 2>&1; then
        echo "python3"
    elif python --version &>/dev/null 2>&1; then
        echo "python"
    else
        echo ""
    fi
}

parse_json() {
    local json="$1"
    local field="$2"

    if command -v jq &>/dev/null; then
        echo "$json" | jq -r ".$field // empty" 2>/dev/null
        return
    fi

    local py_cmd=$(get_python_cmd)
    if [ -n "$py_cmd" ]; then
        echo "$json" | $py_cmd -c "
import sys, json
try:
    data = json.loads(sys.stdin.read())
    keys = '$field'.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, '')
        else:
            data = ''
            break
    print(data if data is not None else '')
except:
    print('')
" 2>/dev/null
    fi
}

validate_json() {
    local json="$1"
    if command -v jq &>/dev/null; then
        echo "$json" | jq -e . >/dev/null 2>&1
        return $?
    fi
    return 0
}

get_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || echo "1970-01-01T00:00:00Z"
}

create_json() {
    local py_cmd=$(get_python_cmd)
    if [ -n "$py_cmd" ]; then
        $py_cmd -c "
import sys, json
args = sys.argv[1:]
data = {}
for i in range(0, len(args), 2):
    if i+1 < len(args):
        data[args[i]] = args[i+1]
print(json.dumps(data))
" "$@" 2>/dev/null
    else
        local result="{"
        local first=true
        while [ $# -ge 2 ]; do
            local key="$1"
            local value="$2"
            shift 2
            value=$(echo "$value" | sed 's/"/\\"/g' | tr '\n' ' ')
            if [ "$first" = true ]; then
                result="$result\"$key\": \"$value\""
                first=false
            else
                result="$result, \"$key\": \"$value\""
            fi
        done
        result="$result}"
        echo "$result"
    fi
}

write_jsonl() {
    local file="$1"
    local entry="$2"
    # Ensure directory exists
    mkdir -p "$(dirname "$file")" 2>/dev/null || true
    echo "$entry" >> "$file" 2>/dev/null
}

# ============================================================================
# CENTRALIZED LOGGING (all events go through here)
# ============================================================================

log_event() {
    local event_type="$1"    # prompts, tools, skills, tasks, subagents, errors, permissions, etc.
    local session_id="$2"
    shift 2
    # Remaining args are key-value pairs

    local log_dir=$(get_log_dir)
    local timestamp=$(get_timestamp)
    local user=$(get_user)
    local branch=$(get_branch)

    # Build JSON with common fields + passed fields
    local entry=$(create_json \
        "timestamp" "$timestamp" \
        "session_id" "$session_id" \
        "user" "$user" \
        "branch" "$branch" \
        "$@")

    write_jsonl "$log_dir/${event_type}.jsonl" "$entry"

    # Also write to unified audit log
    write_jsonl "$log_dir/audit.jsonl" "$entry"
}

# ============================================================================
# TEAM NOTIFICATIONS
# ============================================================================

notify_team() {
    local title="$1"
    local message="$2"
    local severity="${3:-info}"

    # Local notification (macOS)
    if [ "$(uname)" = "Darwin" ]; then
        local sound="default"
        case "$severity" in
            warning) sound="Basso" ;;
            critical) sound="Sosumi" ;;
        esac
        osascript -e "display notification \"$message\" with title \"$title\" sound name \"$sound\"" 2>/dev/null || true
    fi

    # Webhook notification
    if [ -n "$TEAM_WEBHOOK_URL" ]; then
        local color="good"
        case "$severity" in
            warning) color="warning" ;;
            critical) color="danger" ;;
        esac

        curl -s -X POST -H "Content-Type: application/json" \
            -d "{\"text\":\"$title\",\"attachments\":[{\"color\":\"$color\",\"text\":\"$message\"}]}" \
            "$TEAM_WEBHOOK_URL" >/dev/null 2>&1 || true
    fi
}

# ============================================================================
# FILE PROTECTION
# ============================================================================

is_protected_file() {
    local file_path="$1"
    local basename=$(basename "$file_path")

    for pattern in "${PROTECTED_PATTERNS[@]}"; do
        case "$basename" in
            $pattern) return 0 ;;
        esac
        case "$file_path" in
            *$pattern*) return 0 ;;
        esac
    done
    return 1
}

is_infra_command() {
    local command="$1"
    for cmd in "${INFRA_COMMANDS[@]}"; do
        if echo "$command" | grep -qw "$cmd" 2>/dev/null; then
            return 0
        fi
    done
    return 1
}

# ============================================================================
# SESSION CONTEXT MANAGEMENT
# ============================================================================

get_context_file() {
    local session_id="$1"
    echo "$CONTEXT_DIR/session-$session_id.json"
}

has_interview() {
    local session_id="$1"
    local context_file=$(get_context_file "$session_id")
    if [ -f "$context_file" ]; then
        local interviewed=$(parse_json "$(cat "$context_file")" "interviewed")
        [ "$interviewed" = "true" ]
    else
        return 1
    fi
}

mark_interviewed() {
    local session_id="$1"
    local context_file=$(get_context_file "$session_id")
    local py_cmd=$(get_python_cmd)

    if [ -n "$py_cmd" ]; then
        $py_cmd -c "
import json, sys
file_path = sys.argv[1]
try:
    with open(file_path, 'r') as f:
        data = json.load(f)
except:
    data = {}
data['interviewed'] = True
data['interview_time'] = '$(get_timestamp)'
with open(file_path, 'w') as f:
    json.dump(data, f)
" "$context_file" 2>/dev/null
    fi
}

requires_interview() {
    local skill_name="$1"
    case "$skill_name" in
        kubernetes|helm|docker|kafka|terraform)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

enforce_governance() {
    local skill_name="$1"
    local session_id="$2"

    if requires_interview "$skill_name"; then
        if ! has_interview "$session_id"; then
            echo "BLOCKED: $skill_name requires /interview first to gather context."
            return 1
        fi
    fi
    return 0
}

# ============================================================================
# SUBAGENT PROMPT TRACKING (Full prompt capture)
# ============================================================================

store_subagent_prompt() {
    local agent_id="$1"
    local prompt="$2"
    local subagent_type="$3"

    local prompt_file="$CONTEXT_DIR/subagents/$agent_id.prompt"
    mkdir -p "$CONTEXT_DIR/subagents" 2>/dev/null || true

    # Store full prompt (not truncated)
    echo "$prompt" > "$prompt_file"

    # Store metadata
    echo "{\"type\":\"$subagent_type\",\"started\":\"$(get_timestamp)\"}" > "$CONTEXT_DIR/subagents/$agent_id.meta"
}

get_subagent_prompt() {
    local agent_id="$1"
    local prompt_file="$CONTEXT_DIR/subagents/$agent_id.prompt"

    if [ -f "$prompt_file" ]; then
        cat "$prompt_file"
    else
        echo ""
    fi
}

cleanup_subagent_files() {
    local agent_id="$1"
    rm -f "$CONTEXT_DIR/subagents/$agent_id.prompt" 2>/dev/null || true
    rm -f "$CONTEXT_DIR/subagents/$agent_id.meta" 2>/dev/null || true
}

# ============================================================================
# INFRASTRUCTURE CONTEXT
# ============================================================================

verify_k8s_context() {
    if ! command -v kubectl &>/dev/null; then
        echo "not-installed"
        return 1
    fi
    kubectl config current-context 2>/dev/null || echo "no-context"
}

verify_docker_context() {
    if ! command -v docker &>/dev/null; then
        echo "not-installed"
        return 1
    fi
    docker context show 2>/dev/null || echo "default"
}

verify_aws_context() {
    echo "profile=${AWS_PROFILE:-default} region=${AWS_DEFAULT_REGION:-us-east-1}"
}
