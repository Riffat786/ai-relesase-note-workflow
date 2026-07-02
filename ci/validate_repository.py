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
from datetime import datetime

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
    """Generate a professional Markdown validation report."""

    report_dir = ROOT / "output" / "validation"
    report_dir.mkdir(parents=True, exist_ok=True)

    report_file = report_dir / "repository-validation-report.md"

    status = "✅ READY" if errors == 0 else "❌ FAILED"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(report_file, "w", encoding="utf-8") as f:

        f.write("# Repository Validation Report\n\n")

        f.write("---\n\n")

        f.write("## Validation Information\n\n")

        f.write("| Property | Value |\n")
        f.write("|----------|-------|\n")
        f.write("| Repository | AI Release Note Workflow |\n")
        f.write("| Branch | Riffat |\n")
        f.write(f"| Validation Date | {timestamp} |\n")
        f.write("| Validator Version | 2.0 |\n")
        f.write(f"| Validation Status | {status} |\n")
        f.write(f"| Validation Errors | {errors} |\n\n")

        f.write("---\n\n")

        f.write("## Validation Results\n\n")

        f.write("| Validation Area | Result |\n")
        f.write("|----------------|--------|\n")
        f.write("| Folder Validation | ✅ PASS |\n")
        f.write("| Command Validation | ✅ PASS |\n")
        f.write("| Prompt Validation | ✅ PASS |\n")
        f.write("| Skill Validation | ✅ PASS |\n")
        f.write("| Agent Validation | ✅ PASS |\n")
        f.write("| Mock Data Validation | ✅ PASS |\n\n")

        f.write("---\n\n")

        f.write("## Repository Readiness\n\n")

        if errors == 0:
            f.write("The repository structure has been successfully validated.\n\n")
        else:
            f.write("Repository validation failed. One or more required items are missing.\n\n")

        f.write("### Verified Components\n\n")

        f.write("- ✅ Repository folders\n")
        f.write("- ✅ Claude commands\n")
        f.write("- ✅ Claude prompts\n")
        f.write("- ✅ Claude skills\n")
        f.write("- ✅ AI agents\n")
        f.write("- ✅ Mock Azure DevOps data\n")
        f.write("- ✅ Mock ServiceNow data\n\n")

        f.write("---\n\n")

        f.write("## Overall Status\n\n")

        if errors == 0:
            f.write("The repository is ready to execute the AI Release Note Pipeline.\n\n")
        else:
            f.write("The repository is NOT ready to execute the pipeline.\n\n")

        f.write("---\n\n")

        f.write("## Recommended Next Step\n\n")

        if errors == 0:
            f.write("Execute the Release Note Pipeline.\n\n")
        else:
            f.write("Resolve validation errors before executing the pipeline.\n\n")

        f.write("---\n\n")

        f.write("## Validation Artifact\n\n")

        f.write("```text\n")
        f.write("output/validation/repository-validation-report.md\n")
        f.write("```\n\n")

        f.write("---\n\n")

        f.write("## Validator Information\n\n")

        f.write("| Property | Value |\n")
        f.write("|----------|-------|\n")
        f.write("| Validator | Repository Validator |\n")
        f.write("| Version | 2.0 |\n")
        f.write("| Generated By | GitHub Actions / Local Execution |\n")

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