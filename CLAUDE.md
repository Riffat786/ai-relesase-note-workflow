# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

---

## Project Overview

This is a proof-of-concept demonstrating AI-automated release note and
help topic generation. The pipeline connects to Atlassian Jira via MCP,
fetches all issues from the KAN project, and produces publication-ready
release notes (HTML, Markdown, JSON) and help topics (HTML, Markdown)
with full quality review and auto-fix — triggered by a single command.

**Key principle**: Data comes from Jira, not from local sample files.
The pipeline runs automatically from start to finish without user input.

---

## Quick Start

### Prerequisite: Connect the Atlassian MCP

Before first use, connect the Atlassian MCP server:

```bash
claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse
```

Sign in with the Atlassian account that has access to the
**GlobalMailProClaudeDemo** project at `https://twtaidimple.atlassian.net`.
Do not store credentials in any project file.

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
Atlassian Jira — GlobalMailProClaudeDemo (KAN)
https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9
         │
         │  Atlassian MCP
         │  JQL: project = KAN ORDER BY cf[10019] ASC
         ▼
release-note-orchestrator.md
         │
         ├──▶ release-note-writer-agent.md
         │         │ Produces:
         │         ├── output/release-notes-[version].html
         │         ├── output/release-notes-[version].md
         │         └── output/release-notes-[version].json
         │
         ├──▶ help-topic-writer-agent.md  (once per New Feature)
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

### Issue Type Mapping

| Jira issue type                           | Release note section |
|-------------------------------------------|----------------------|
| Story, Feature, New Feature               | New Features         |
| Task, Enhancement, Improvement, Sub-task  | Enhancements         |
| Bug                                       | Bug Fixes            |
| Any type with label "known-issue"         | Known Issues         |
| Epic                                      | Skipped              |

---

## Directory Structure

| Directory / File         | Purpose                                               |
|--------------------------|-------------------------------------------------------|
| `.mcp.json`              | Atlassian MCP server configuration                    |
| `commands/`              | Single trigger command                                |
| `agents/`                | Orchestrator + three sub-agents                       |
| `skills/`                | Writing rules, reviewer checklist, branding guide     |
| `sample-data/`           | Structure benchmarks (expected-output-1, -2)          |
| `output/`                | All generated files (HTML, MD, JSON, review report)   |
| `charter/`               | Project scope and success criteria                    |
| `roster/`                | Team members and role assignments                     |
| `assumptions/`           | Project assumptions and constraints                   |

---

## Key Files

### Entry Point
- **`commands/release-note-generation-command.md`** — Run this to start
  the pipeline. Contains the trigger prompt and setup instructions.

### Agents
- **`agents/release-note-orchestrator.md`** — Coordinates the full
  pipeline. Fetches Jira data, delegates to sub-agents, manages quality.
- **`agents/release-note-writer-agent.md`** — Generates release notes
  in HTML, Markdown, and JSON from classified Jira issues.
- **`agents/help-topic-writer-agent.md`** — Generates a branded HTML +
  Markdown help topic for each New Feature issue.
- **`agents/release-note-reviewer-agent.md`** — Runs 22-point QA
  checklist, 7-criterion style audit, hyperlink checks, JSON validation,
  and branding compliance across all output files.

### Skills (AI personas and standards)
- **`skills/release-note-writer-skill.md`** — Senior technical writer role.
  MSTP writing rules, output formats, content rules.
- **`skills/release-note-reviewer-skill.md`** — QA reviewer role.
  22-point checklist, severity definitions, style audit.
- **`skills/branding-style-guide.md`** — GlobalMail Pro brand standards.
  Colour palette, typography, HTML/CSS template.

### Benchmarks
- **`sample-data/expected-output-1.md`** — Release notes structure
  template and quality benchmark. Defines all required sections.
- **`sample-data/expected-output-2.md`** — Help topic structure template
  and quality benchmark. Defines Overview, Workflow, API Details.

---

## MCP Configuration

The `.mcp.json` file at the project root configures the Atlassian MCP:

```json
{
  "mcpServers": {
    "atlassian": {
      "type": "sse",
      "url": "https://mcp.atlassian.com/sse"
    }
  }
}
```

**Authentication:** Atlassian OAuth (handled by Claude Code on first connect).
Do not store API keys or tokens in any project file.

**Access required:**
- Jira: read access to **GlobalMailProClaudeDemo** (key: KAN) at
  https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9
- Confluence: read access (optional — used if features link to Confluence pages)

---

## Output Files

Every pipeline run produces these files in `output/`:

| File                                   | Description                              |
|----------------------------------------|------------------------------------------|
| `release-notes-[version].html`         | Branded HTML — links to help topics      |
| `release-notes-[version].md`           | Markdown — version control source        |
| `release-notes-[version].json`         | Structured JSON — for downstream use     |
| `help-topic-[slug].html`               | Branded help topic per New Feature       |
| `help-topic-[slug].md`                 | Markdown help topic per New Feature      |
| `release-note-review-report.md`        | QA findings + auto-fix log               |

---

## Quality Pipeline

Every run applies these quality checks automatically:

1. **Structure compliance** — All sections match expected-output-1 and
   expected-output-2 benchmarks
2. **MSTP writing standards** — 22-point checklist (voice, tense, punctuation,
   headings, marketing language, internal IDs)
3. **7-criterion style audit** — Active voice, present tense, second person,
   sentence length, heading case, code formatting, jargon
4. **Hyperlink integrity** — Every New Feature links to its help topic;
   every help topic links back to release notes
5. **JSON validity** — Valid JSON, correct schema, no internal IDs in prose
6. **Branding compliance** — GMP colour palette, Inter typography, required
   header and footer in all HTML files
7. **Auto-fix** — Orchestrator applies corrected text for all High and
   Medium severity findings

---

## Constraints

### Security
- Do not store Atlassian credentials, API tokens, or secrets in any
  project file. Use Atlassian OAuth via the MCP connection.
- Do not log or print access tokens in any output file.

### Content
- Do not invent content. Every claim must trace to a Jira issue field.
- Do not expose internal Jira IDs in prose (Bug ID in Bug Fixes table only).
- Do not include engineering or infrastructure details in customer-facing output.

### Scope
- All source data comes from Jira (GlobalMailProClaudeDemo project) via
  the Atlassian MCP. No local sample input files are used.

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
feat(agents): update orchestrator for Jira MCP integration
fix(writer): correct bug fix table column order
docs(commands): add troubleshooting section to trigger command
```

---

## Troubleshooting

| Issue                          | Resolution                                           |
|--------------------------------|------------------------------------------------------|
| Atlassian MCP not connecting   | Run `claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse` |
| No issues fetched from Jira    | Verify GlobalMailProClaudeDemo project has issues + Atlassian OAuth is active |
| Output files not created       | Run `mkdir -p output` in project root               |
| Help topic links broken        | Check `help_topic_map` in orchestrator Step 4        |
| JSON invalid in output         | Check review report for RN-J1 finding                |

---

## Questions or Blockers

- Check GitHub Issues first
- The repository is the single source of truth — all decisions documented here
- Raise a GitHub Issue if blocked or uncertain
