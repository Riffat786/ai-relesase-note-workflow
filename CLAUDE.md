# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This is a workshop proof-of-concept demonstrating how AI can automate and improve a release note workflow. The project uses Claude Commands, Skills, and Agents to show practical AI-assisted documentation automation.

**Key principle**: We are not building a production release note tool. We are demonstrating how AI capabilities (Commands, Skills, Agents, MCP) can transform a realistic documentation workflow.

---

## Architecture

### Directory Structure and Purpose

| Directory | Purpose |
|-----------|---------|
| `charter/` | Project scope, goals, and success criteria |
| `roster/` | Team members and role assignments |
| `workflow/` | Workflow analysis and design documentation |
| `sample-data/` | Sample inputs, expected outputs, and benchmarks for validation |
| `commands/` | Reusable Claude Code commands with prompts and instructions |
| `skills/` | Skills documentation defining roles, formats, and output standards |
| `agents/` | Agent workflow designs for multi-step automation |
| `mcp-plugin-concept/` | Integration concepts using MCP, plugins, and marketplace tools |
| `validation/` | Testing results, findings, risks, and lessons learned |
| `demo/` | Final demonstration materials and scripts |
| `meetings/` | Meeting notes, decisions, and action items |
| `assumptions/` | Project assumptions and constraints |

### Key Files

- **README.md**: Project overview and getting started
- **README-project.md**: Detailed project scope, deliverables, and success criteria
- **CONTRIBUTING.md**: Collaboration standards and guidelines
- **Github-collaboration-instructions.md**: GitHub workflow for branches, PRs, and issues

### Skills (AI Personas)

The project defines three core skills in `skills/`:

1. **release-note-writer-skill.md**: Senior technical writer role
   - Transforms structured input (features, bugs, enhancements) into customer-facing release notes
   - Enforces Microsoft Writing Style (MSTP) standards
   - Outputs both Markdown and HTML formats
   - Apply for generating draft release notes from source information

2. **release-note-reviewer-skill.md**: Quality assurance reviewer role
   - Reviews draft release notes for completeness, clarity, and compliance
   - Checks against branding guidelines and customer-facing standards
   - Provides actionable feedback for improvement
   - Apply when reviewing or improving draft release notes

3. **branding-style-guide.md**: GlobalMail Pro brand standards
   - Defines colour palette (#1B2A4A navy, #2ECC71 green)
   - Typography and visual standards
   - Pre-embedded in agent system prompts
   - Used by all HTML outputs

### Commands

Two reusable commands defined in `commands/`:

1. **release-note-generation-command.md**
   - Takes structured input from `sample-data/` 
   - Applies the writer skill
   - Produces Markdown and HTML outputs
   - Validates against benchmarks in `sample-data/expected-output-*.md`

2. **release-note-review-command.md**
   - Takes generated release notes as input
   - Applies the reviewer skill
   - Produces improvement recommendations
   - Iterative refinement workflow

### Sample Data and Benchmarks

Test the workflow with:

- `sample-data/sample-1-input.md`: Feature/enhancement scenario
- `sample-data/sample-2-input.md`: Bug fix scenario
- `sample-data/expected-output-1.md`: Benchmark for sample 1
- `sample-data/expected-output-2.md`: Benchmark for sample 2

These benchmarks define the expected quality level for generated content.

---

## Working in This Repository

### Structure Your Work

Follow **CONTRIBUTING.md** guidelines:

- **Use branches** for commands, skills, agent workflows, and major changes
  - Example: `feature/release-note-command`, `feature/reviewer-skill`, `feature/agent-workflow`
  - Submit a Pull Request when ready for review

- **Direct commits acceptable** for documentation-only updates:
  - Meeting notes → `meetings/`
  - Sample data → `sample-data/`
  - Research findings → `validation/` or `assumptions/`
  - Decisions → documented in the appropriate folder

### Core Principle

All important project work must live in this repository, not in chats, emails, or personal files.

Do:
- Commit prompts, skills, commands, and workflows
- Document decisions in appropriate folders
- Store meeting notes and action items
- Track work through GitHub Issues

Don't:
- Keep critical information only in Slack, WhatsApp, or email
- Store important work on personal machines
- Rely solely on chat for decisions or tracking

### Content Standards

When adding or updating files:
- Use clear headings and consistent formatting
- Include dates where relevant (absolute dates, not relative like "Thursday")
- Document assumptions and decisions with context ("**Why:**" and **How to apply:**" sections)
- Keep content concise and accessible
- Flag missing information with `[INSERT: field name]` instead of inventing content

---

## Testing and Validation

### Run the Workflow

Use the commands in `commands/` with Claude Code:

1. **Generate draft release notes**
   - Apply `release-note-generation-command.md`
   - Use sample input from `sample-data/sample-[1-2]-input.md`
   - Compare output to `sample-data/expected-output-[1-2].md`

2. **Review and improve drafts**
   - Apply `release-note-review-command.md`
   - Iterate on feedback
   - Validate quality against benchmarks

### Expected Quality

Generated release notes should:
- Match the structure in `skills/release-note-writer-skill.md`
- Apply every rule from the skill (no marketing language, active voice, MSTP standards)
- Use plain language without technical jargon or internal IDs
- Follow the GlobalMail Pro branding guidelines
- Include all required sections (What's New, Bug Fix, Benefits, etc.)

---

## Constraints and Out of Scope

### What This Project Is

- A demonstration of AI-assisted documentation workflow
- A proof-of-concept with realistic scenarios
- A teaching tool for Claude capabilities

### What This Project Is Not

- A production-ready tool
- Full enterprise integrations
- Complete automation (human review remains required)
- Support for all documentation types

---

## Collaboration Model

### GitHub Issues

Track work through GitHub Issues:
- One issue per major task
- Include objective, owner, expected deliverable, and status
- Use for workflow mapping, sample data, command design, skills, agent design, validation, and demo prep

### Branches and Pull Requests

Branch naming convention:
- `feature/release-note-command` (for a new command)
- `feature/reviewer-skill` (for a new skill)
- `feature/agent-workflow` (for multi-step automation)

### Commit Messages

Keep commits focused and descriptive:
- Avoid combining unrelated changes
- Reference GitHub Issues in commit messages when relevant

---

## Key Files to Read First

1. **README-project.md** - Full project scope and deliverables
2. **charter/** - Project goals and success criteria
3. **roster/team-roster.md** - Team members and assignments
4. **skills/release-note-writer-skill.md** - The core writing standards
5. **commands/release-note-generation-command.md** - How to invoke the workflow

---

## Future Work

Concepts that may be developed:

- Full MCP integrations with external systems
- Automated publish workflows
- Extended support for other documentation types
- Advanced validation and testing harnesses

See `mcp-plugin-concept/` and `workflow/` directories for design notes.

---

## Questions or Blockers

- Check GitHub Issues first
- Raise new issues if blocked or uncertain
- Document your findings in the appropriate directory (`validation/`, `assumptions/`, etc.)
- Store decisions in the repository, not in chat only

Remember: **The repository is the single source of truth.**
