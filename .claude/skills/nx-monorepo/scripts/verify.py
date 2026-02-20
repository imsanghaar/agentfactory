#!/usr/bin/env python3
"""Verify nx-monorepo skill is ready."""

import subprocess
import sys
from pathlib import Path

def check_scripts():
    """Check that required scripts exist and are executable."""
    script_dir = Path(__file__).parent

    required = ["nx-docs.sh", "nx-plugins.sh", "mcp-client.py"]

    for script in required:
        path = script_dir / script
        if not path.exists():
            print(f"✗ Missing: {script}")
            return False

    print("✓ nx-monorepo skill ready")
    return True

def check_npx():
    """Check npx is available."""
    try:
        subprocess.run(["npx", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ npx not found (required for nx-mcp)")
        return False

if __name__ == "__main__":
    success = check_scripts() and check_npx()
    sys.exit(0 if success else 1)
