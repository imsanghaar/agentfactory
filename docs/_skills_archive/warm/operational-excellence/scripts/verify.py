#!/usr/bin/env python3
"""Verify operational-excellence skill integrity."""
import os
import sys

def main():
    skill_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_md = os.path.join(skill_path, "SKILL.md")

    if not os.path.isfile(skill_md):
        print(f"✗ SKILL.md not found")
        sys.exit(1)

    with open(skill_md, 'r') as f:
        content = f.read()

    # Check required sections
    required = ["VPA", "OpenCost", "Velero", "Chaos Mesh", "Safety"]
    missing = [s for s in required if s not in content]

    if missing:
        print(f"✗ Missing sections: {', '.join(missing)}")
        sys.exit(1)

    print("✓ operational-excellence valid")
    sys.exit(0)

if __name__ == "__main__":
    main()
