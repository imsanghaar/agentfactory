#!/bin/bash
# List available Nx plugins via nx-mcp (on-demand, no persistent server)
# Usage: ./nx-plugins.sh

set -euo pipefail

SCRIPT_DIR="$(dirname "$0")"

# Call nx-mcp via stdio (spawns on demand, no persistent connection)
python3 "$SCRIPT_DIR/mcp-client.py" call \
  -s "npx -y nx-mcp@latest" \
  -t nx_available_plugins \
  -p "{}" 2>/dev/null
