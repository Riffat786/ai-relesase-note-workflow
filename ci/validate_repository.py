#!/usr/bin/env python3

"""
Repository Validator
Version: 2.0

Purpose:
Validate that the AI Release Note repository contains
all required folders and files before the GitHub
Actions pipeline executes.

Exit Codes:
0 = Success
1+ = Validation Failed
"""

from pathlib import Path
import sys

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

errors = 0


# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def print_header(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def validate_folders(folders):
    global errors

    print_header("Folder Validation")

    for folder in folders:
        path = ROOT / folder

        if path.exists() and path.is_dir():
            print(f"✅ PASS   {folder}")
        else:
            print(f"❌ FAIL   {folder}")
            errors += 1


def validate_files(title, files):
    global errors

    print_header(title)

    for file in files:
        path = ROOT / file

        if path.exists():
            print(f"✅ PASS   {file}")
        else:
            print(f"❌ FAIL   {file}")
            errors += 1


# ----------------------------------------------------------
# Required Folders
# ----------------------------------------------------------

required_folders = [

    ".claude",
    ".claude/commands",
    ".claude/prompts",
    ".claude/skills",

    "agents",
    "automation",
    "ci",
    "data",
    "docs",
    "examples",
    "mcp",
    "output",
]


# ----------------------------------------------------------
# Required Command Files
# ----------------------------------------------------------

required_commands = [

    ".claude/commands/collect-release-data.md",
    ".claude/commands/analyze-release.md",
    ".claude/commands/write-release-notes.md",
    ".claude/commands/review-release-notes.md",
    ".claude/commands/create-release-draft.md",
]


# ----------------------------------------------------------
# Required Prompt Files
# ----------------------------------------------------------

required_prompts = [

    ".claude/prompts/analyze-release-notes.md",
    ".claude/prompts/write-release-notes.md",
    ".claude/prompts/review-release-notes.md",
    ".claude/prompts/create-document360-draft.md",
]


# ----------------------------------------------------------
# Required Skills
# ----------------------------------------------------------

required_skills = [

    ".claude/skills/classify-release-items/SKILL.md",
    ".claude/skills/customer-friendly-language/SKILL.md",
    ".claude/skills/quality-review-checklist/SKILL.md",
    ".claude/skills/release-note-template/SKILL.md",
    ".claude/skills/release-note-metadata/SKILL.md",
]


# ----------------------------------------------------------
# Required Agents
# ----------------------------------------------------------

required_agents = [

    "agents/collector-agent.md",
    "agents/analyzer-agent.md",
    "agents/writer-agent.md",
    "agents/reviewer-agent.md",
    "agents/draft-generator-agent.md",
]


# ----------------------------------------------------------
# Required Mock Data
# ----------------------------------------------------------

required_data = [

    "data/release-2025.8.json",
    "data/service-now-2025.8.json",
]


# ----------------------------------------------------------
# Validation Starts Here
# ----------------------------------------------------------

print("=" * 60)
print(" AI Release Note Pipeline")
print(" Repository Validation")
print("=" * 60)

validate_folders(required_folders)

validate_files("Command Validation", required_commands)

validate_files("Prompt Validation", required_prompts)

validate_files("Skill Validation", required_skills)

validate_files("Agent Validation", required_agents)

validate_files("Mock Data Validation", required_data)


# ----------------------------------------------------------
# Final Status
# ----------------------------------------------------------
def write_validation_report():
    """Generate a Markdown validation report."""

    report_dir = ROOT / "output" / "validation"
    report_dir.mkdir(parents=True, exist_ok=True)

    report_file = report_dir / "repository-validation-report.md"

    status = "✅ READY" if errors == 0 else "❌ FAILED"

    with open(report_file, "w", encoding="utf-8") as f:

        f.write("# Repository Validation Report\n\n")
        f.write("## Summary\n\n")
        f.write(f"**Status:** {status}\n\n")
        f.write(f"**Validation Errors:** {errors}\n\n")

        f.write("---\n\n")

        f.write("## Validation Scope\n\n")

        f.write("- Folder Validation\n")
        f.write("- Command Validation\n")
        f.write("- Prompt Validation\n")
        f.write("- Skill Validation\n")
        f.write("- Agent Validation\n")
        f.write("- Mock Data Validation\n\n")

        f.write("---\n\n")

        if errors == 0:
            f.write("Repository is ready for the AI Release Note Pipeline.\n")
        else:
            f.write("Repository validation failed. Review the GitHub Actions log for details.\n")

    print()
    print(f"📄 Validation report created:")
    print(report_file)

print()
print("=" * 60)

if errors == 0:
    print("✅ Repository Status: READY")
    print("All required folders and files were found.")
else:
    print(f"❌ Repository Status: FAILED")
    print(f"Missing items detected: {errors}")

print("=" * 60)

write_validation_report()

sys.exit(errors)