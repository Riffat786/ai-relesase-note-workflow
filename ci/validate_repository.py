#!/usr/bin/env python3

"""
Repository Validator
Version: 1.0

Checks that the required project folders exist before
running the AI Release Note Pipeline.
"""

from pathlib import Path
import sys

print("=" * 55)
print(" AI Release Note Pipeline")
print(" Repository Validation")
print("=" * 55)
print()

ROOT = Path(__file__).resolve().parent.parent

required_folders = [
    ".claude",
    ".claude/commands",
    ".claude/prompts",
    ".claude/skills",
    "agents",
    "automation",
    "data",
    "docs",
    "mcp",
    "output",
]

errors = 0

for folder in required_folders:

    path = ROOT / folder

    if path.exists() and path.is_dir():
        print(f"✅ PASS   {folder}")
    else:
        print(f"❌ FAIL   {folder}")
        errors += 1

print()
print("=" * 55)

if errors == 0:
    print(" Repository Status: READY")
    print(" All required folders exist.")
else:
    print(f" Repository Status: FAILED ({errors} issue(s))")

print("=" * 55)

sys.exit(errors)