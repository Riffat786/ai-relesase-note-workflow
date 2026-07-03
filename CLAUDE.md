# CLAUDE.md



This file provides guidance to Claude Code (claude.ai/code) when working

with code in this repository.



---



## Project Overview



This is an AI-automated release note and help topic generation system

for **WealthWise**, an AI-powered personal finance platform. The pipeline

connects to Atlassian Jira (https://twtaishubh.atlassian.net) via MCP,

fetches all issues from the KAN project, and produces publication-ready

release notes (HTML, Markdown) and help topics (HTML, Markdown) with full

quality review and auto-fix, all triggered by a single command.



**Key principle**: Data comes from Jira, not from local sample files.

The pipeline runs automatically from start to finish without user input.

Local files in `sample-data/` are structure and quality **benchmarks**

only — they are never treated as live release content.



This plugin is branded per `skills/wealthwise-branding.md`. It follows

the same orchestrator → sub-agents → quality-review architecture used by

the reference GlobalMail Pro release note workflow, adapted to

WealthWise's own voice, category set, and dual-output (HTML + Markdown,

no JSON) convention.



---



## Quick Start



### Prerequisite: Connect the Atlassian MCP



Before first use, connect the Atlassian MCP server:



```bash

claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse

```



Sign in with your Atlassian account that has access to the

**KAN** project at **https://twtaishubh.atlassian.net**.

Do not store credentials in any project file. OAuth is handled automatically.



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

Atlassian Jira — KAN (https://twtaishubh.atlassian.net)

         │

         │  Atlassian MCP

         │  JQL: project = KAN ORDER BY cf[10019] ASC

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



### Issue Type Mapping



| Jira issue type                           | Release note category |

|-------------------------------------------|------------------------|

| Story, Feature, New Feature                | What's New             |

| Task, Enhancement, Improvement, Sub-task   | Enhancements           |

| Bug                                        | Bug Fixes              |

| Any type with label "known-issue"          | Known Issues           |

| Epic                                       | Skipped                |



WealthWise release notes use exactly four categories — **What's New,

Enhancements, Bug Fixes, Known Issues** — per the fixed order defined in

`skills/wealthwise-branding.md`. There are no separate Security or

Deprecated sections; if an item needs that emphasis, it is flagged

inline with the `tag-security` or `tag-deprecated` badge inside its

normal category instead.



---



## Directory Structure



| Directory / File         | Purpose                                               |

|--------------------------|--------------------------------------------------------|

| `.mcp.json`               | Atlassian MCP server configuration                    |

| `commands/`               | Trigger commands — generate and review                |

| `agents/`                 | Orchestrator + three sub-agents                       |

| `skills/`                 | Writing rules, reviewer checklist, branding guide      |

| `sample-data/`            | Structure benchmarks (expected-output-1, -2) + local sample inputs |

| `output/`                 | All generated files (HTML, MD, review report)         |

| `mcp-plugin-concept/`     | Integration documentation and architecture            |

| `charter/`                | Project scope and success criteria                    |

| `roster/`                 | Team members and role assignments                     |

| `assumptions/`            | Project assumptions and constraints                   |



---



## Key Files



### Entry Point

- **`commands/release-note-generation-command.md`** — Single-command trigger for the full pipeline

- **`mcp-plugin-concept/integration-concept.md`** — Architecture and integration details with Jira



### Agents

- **`agents/release-note-orchestrator.md`** — Coordinates the full

  pipeline. Fetches Jira data, delegates to sub-agents, manages quality.

- **`agents/release-note-writer-agent.md`** — Generates the consolidated

  release note in HTML and Markdown from classified Jira issues.

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



### Benchmarks

- **`sample-data/expected-output-1.md`** — Consolidated release note

  structure template and quality benchmark, built from

  `sample-data/sample-1-input.md` (feature) and `sample-data/sample-2-input.md`

  (bug fix).

- **`sample-data/expected-output-2.md`** — Help topic structure template

  and quality benchmark for a What's New feature.



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

- Jira: read access to **KAN** project at **https://twtaishubh.atlassian.net**

- Confluence: read access (optional — used if features link to Confluence pages)



---



## Output Files



Every pipeline run produces these files in `output/`:



| File                                        | Description                              |

|----------------------------------------------|------------------------------------------|

| `release-note-[version]-whats-new.html`       | Branded HTML — links to help topics      |

| `release-note-[version]-whats-new.md`         | Markdown — version control source        |

| `help-topic-[slug].html`                      | Branded help topic per What's New feature |

| `help-topic-[slug].md`                        | Markdown help topic per What's New feature |

| `release-note-review-report.md`               | QA findings + auto-fix log               |



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

- Do not store Atlassian credentials, API tokens, or secrets in any

  project file. Use Atlassian OAuth via the MCP connection.

- Do not log or print access tokens in any output file.



### Content

- Do not invent content. Every claim must trace to a Jira issue field.

- Do not expose internal Jira IDs in prose (Bug ID in the Bug Fixes

  table only).

- Do not include engineering or infrastructure details in customer-facing

  output.

- Do not include severity ratings or priority labels (P1, Critical,

  Blocker, etc.) anywhere in customer-facing output — this is a

  WealthWise-specific rule, stricter than many reference workflows.



### Scope

- All source data comes from Jira (WealthWiseReleaseDemo project) via

  the Atlassian MCP. No local sample input files are used as live data.



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

|---------------------------------|-------------------------------------------------------|

| Atlassian MCP not connecting    | Run `claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse` and authenticate |

| No issues fetched from Jira     | Verify KAN project at https://twtaishubh.atlassian.net has issues + Atlassian OAuth is active |

| Output files not created        | Run `mkdir -p output` in project root                |

| Help topic links broken         | Check `help_topic_map` in orchestrator Step 5         |

| Bug Fixes table has extra columns | Reject — WealthWise standard is exactly Bug ID, Description, Fix / Solution |



---



## Questions or Blockers



- Check GitHub Issues first

- The repository is the single source of truth — all decisions documented here

- Raise a GitHub Issue if blocked or uncertain
