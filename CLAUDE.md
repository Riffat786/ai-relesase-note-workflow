# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

---

## Project Overview

This is an AI-automated release note and help topic generation system
for **WealthWise**, an AI-powered personal finance platform. The pipeline
connects to GitHub (https://github.com/ShubhKN/WealthWise) via MCP,
fetches all issues from the v1.0 milestone, and produces publication-ready
release notes (HTML, Markdown) and help topics (HTML, Markdown) with full
quality review and auto-fix, all triggered by a single command.

**Key principle**: Data comes from GitHub issues, not from local sample files.
The pipeline runs automatically from start to finish without user input.
Local files in `sample-data/` are structure and quality **benchmarks**
only — they are never treated as live release content.

This system is branded per `skills/wealthwise-branding.md`. It follows
the same orchestrator → sub-agents → quality-review architecture used by
the reference GlobalMail Pro release note workflow, adapted to
WealthWise's own voice, category set, and dual-output (HTML + Markdown,
no JSON) convention.

---

## Quick Start

### Prerequisite: Connect GitHub MCP & Set Token

Before first use, ensure GitHub MCP is configured:

1. **Set your GitHub token** as an environment variable:

```bash
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

2. **Verify the .mcp.json** has the GitHub MCP server configuration.

**Scope needed:** `repo` (all), `read:org`

Do not store credentials in any project file. Use environment variables only.

### Run the pipeline

```
/project:generate-release-notes
```

Or read `commands/release-note-generation-command.md` for the full
trigger prompt and setup instructions.

---

## Architecture

### Data Flow

```
GitHub Repository — ShubhKN/WealthWise (milestone v1.0)

         │

         │  GitHub MCP

         │  Query: issues in milestone v1.0

         ▼

release-note-orchestrator.md

         │

         ├──▶ release-note-writer-agent.md

         │         │ Produces:

         │         ├── output/release-note-[version]-whats-new.html

         │         └── output/release-note-[version]-whats-new.md

         │

         ├──▶ help-topic-writer-agent.md  (once per What's New issue)

         │         │ Produces per feature:

         │         ├── output/help-topic-[slug].html

         │         └── output/help-topic-[slug].md

         │

         └──▶ release-note-reviewer-agent.md

                   │ Produces:

                   └── output/release-note-review-report.md

                             │

                             └──▶ Orchestrator applies auto-fixes
```

### GitHub Label to Category Mapping

| GitHub label: `type: *` | Release note category |
|---|---|
| `type: feature` | What's New |
| `type: enhancement` | Enhancements |
| `type: bug` (state=closed, no "status: known-issue") | Bug Fixes |
| `type: bug` + `status: known-issue` | Known Issues |
| Tracking issues | Skipped |

WealthWise release notes use exactly four categories — **What's New,
Enhancements, Bug Fixes, Known Issues** — per the fixed order defined in
`skills/wealthwise-branding.md`. There are no separate Security or
Deprecated sections; if an item needs that emphasis, it is flagged
inline with the `tag-security` or `tag-deprecated` badge inside its
normal category instead.

---

## Directory Structure

| Directory / File | Purpose |
|---|---|
| `.mcp.json` | GitHub MCP server configuration |
| `commands/` | Trigger commands — generate and review |
| `agents/` | Orchestrator + three sub-agents |
| `skills/` | Writing rules, reviewer checklist, branding guide, GitHub classifier |
| `sample-data/` | Structure benchmarks (expected-output-1, -2) + local sample inputs |
| `output/` | All generated files (HTML, MD, review report) |
| `mcp-plugin-concept/` | Integration documentation and architecture |
| `charter/` | Project scope and success criteria |
| `roster/` | Team members and role assignments |
| `assumptions/` | Project assumptions and constraints |

---

## Key Files

### Entry Point

- **`commands/release-note-generation-command.md`** — Single-command trigger for the full pipeline
- **`agents/release-note-orchestrator.md`** — Coordinates the full pipeline from GitHub

### Agents

- **`agents/release-note-orchestrator.md`** — Coordinates the full
  pipeline. Fetches GitHub data, delegates to sub-agents, manages quality.
- **`agents/release-note-writer-agent.md`** — Generates the consolidated
  release note in HTML and Markdown from classified GitHub issues.
- **`agents/help-topic-writer-agent.md`** — Generates a branded HTML +
  Markdown help topic for each What's New issue.
- **`agents/release-note-reviewer-agent.md`** — Runs the WealthWise
  writing-standards checklist, structure benchmark checks, hyperlink
  checks, and branding compliance across all output files.

### Skills (AI personas and standards)

- **`skills/release-note-writer-skill.md`** — Senior technical writer
  role. WealthWise voice, output formats, content rules.
- **`skills/release-note-reviewer-skill.md`** — QA reviewer role.
  Checklist, severity definitions, style audit.
- **`skills/wealthwise-branding.md`** — WealthWise brand standards.
  Colour palette, typography, HTML/CSS template, category and tag rules.
- **`skills/github-issue-classifier.md`** — GitHub label-to-category mapping
  and field extraction rules.

### Benchmarks

- **`sample-data/expected-output-1.md`** — Consolidated release note
  structure template and quality benchmark, built from
  `sample-data/sample-1-input.md` (feature) and `sample-data/sample-2-input.md`
  (bug fix).
- **`sample-data/expected-output-2.md`** — Help topic structure template
  and quality benchmark for a What's New feature.

---

## MCP Configuration

The `.mcp.json` file at the project root configures the GitHub MCP:

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "$GITHUB_TOKEN"
      }
    }
  }
}
```

**Authentication:** GitHub token via `GITHUB_TOKEN` environment variable.
Do not store API keys or tokens in any project file.

**Access required:**

- GitHub: read access to **ShubhKN/WealthWise** repository
- Token scopes: `repo` (all), `read:org`

---

## Output Files

Every pipeline run produces these files in `output/`:

| File | Description |
|---|---|
| `release-note-[version]-whats-new.html` | Branded HTML — links to help topics |
| `release-note-[version]-whats-new.md` | Markdown — version control source |
| `help-topic-[slug].html` | Branded help topic per What's New feature |
| `help-topic-[slug].md` | Markdown help topic per What's New feature |
| `release-note-review-report.md` | QA findings + auto-fix log |

WealthWise release notes do not produce a JSON output file. The dual
output rule in `skills/wealthwise-branding.md` defines exactly two files
per release note artifact: Markdown and HTML.

---

## Quality Pipeline

Every run applies these quality checks automatically:

1. **Structure compliance** — All sections match the expected-output-1
   and expected-output-2 benchmarks
2. **Writing standards** — Second person, active voice, three-part
   narrative (Previously → Now → Value) for What's New and Enhancements,
   past-tense/present-tense bug fix table cells, no internal IDs beyond
   the Bug ID column, no severity labels, no marketing language
3. **Hyperlink integrity** — Every What's New entry links to its help
   topic; every help topic links back to the release note
4. **Branding compliance** — WealthWise colour palette, system font
   stack, required header and footer, correct category order and icons,
   `tag-ai` applied to every AI-driven feature mention
5. **Auto-fix** — Orchestrator applies corrected text for all High and
   Medium severity findings

---

## Constraints

### Security

- Do not store GitHub credentials, API tokens, or secrets in any
  project file. Use GitHub tokens via environment variables only.
- Do not log or print access tokens in any output file.

### Content

- Do not invent content. Every claim must trace to a GitHub issue field.
- Do not expose internal GitHub issue numbers in prose (GitHub issue number
  in the Bug Fixes table only as "#[number]").
- Do not include engineering or infrastructure details in customer-facing
  output.
- Do not include severity ratings or priority labels (P1, Critical,
  Blocker, etc.) anywhere in customer-facing output — this is a
  WealthWise-specific rule, stricter than many reference workflows.

### Scope

- All source data comes from GitHub (ShubhKN/WealthWise, milestone v1.0) via
  the GitHub MCP. No local sample input files are used as live data.

---

## Working in This Repository

### Direct commits acceptable for

- `output/` — Generated files from pipeline runs
- `meetings/` — Meeting notes
- `validation/` — Testing findings
- `assumptions/` — Assumption updates

### Use branches for

- Changes to agents, skills, commands, or benchmarks
- New features or structural changes

### Commit message format

```
feat(agents): update orchestrator for GitHub MCP integration
fix(writer): correct bug fix table column order
docs(commands): add troubleshooting section to trigger command
```

---

## Troubleshooting

| Issue | Resolution |
|---|---|
| GitHub MCP not connecting | Verify `$env:GITHUB_TOKEN` is set with a valid token |
| No issues fetched from GitHub | Verify ShubhKN/WealthWise repo has milestone v1.0 + token has `repo` scope |
| Output files not created | Run `mkdir -p output` in project root |
| Help topic links broken | Check `help_topic_map` in orchestrator Step 5 |
| Bug Fixes table has extra columns | Reject — WealthWise standard is exactly Bug ID, Description, Fix / Solution |

---

## Questions or Blockers

- Check GitHub Issues in the WealthWise repository first
- The repository is the single source of truth — all decisions documented here
- Raise a GitHub Issue if blocked or uncertain
