#!/bin/bash
# Query Nx documentation via nx-mcp (on-demand, no persistent server)
# Usage: ./nx-docs.sh "your query here"

set -euo pipefail

QUERY="${1:?Error: Query required. Usage: ./nx-docs.sh \"your query\"}"

SCRIPT_DIR="$(dirname "$0")"

# Call nx-mcp via stdio (spawns on demand, no persistent connection)
python3 "$SCRIPT_DIR/mcp-client.py" call \
  -s "npx -y nx-mcp@latest" \
  -t nx_docs \
  -p "{\"userQuery\": \"$QUERY\"}" 2>/dev/null
