---

description: Single-command trigger for the full GlobalMail Pro release note automation pipeline. Paste or run this command in Claude Code to generate release notes and help topics from Jira without any further user input.
data_source: Atlassian Jira — project GlobalMailProClaudeDemo (key- KAN)
jira_board_url: "https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9"
mcp_required: atlassian (configured in .mcp.json)
outputs: output/release-notes-[version].html, output/release-notes-[version].md, output/release-notes-[version].json, output/help-topic-[slug].html       (one per new feature), output/help-topic-[slug].md         (one per new feature), output/release-note-review-report.md

---

# Release Note Generation — Single Trigger Command

## How to Use

In Claude Code, run this command:

```
/project:generate-release-notes
```

Or paste the prompt below directly into Claude Code. No further input
is required. The pipeline runs to completion automatically.

---

## Trigger Prompt

```
Run the GlobalMail Pro release note automation pipeline from start to
finish. Do not pause for input at any point.

Prerequisites (verify before starting):
1. The Atlassian MCP server is connected (.mcp.json is present and
   the Atlassian MCP at https://mcp.atlassian.com/sse is authenticated).
2. The output/ directory exists and is writable.

Execute these steps in order:

STEP 1 — Read agents/release-note-orchestrator.md in full.
STEP 2 — Follow every instruction in that file exactly as written.
STEP 3 — Do not skip any step. Do not ask the user for clarification.
STEP 4 — If a non-critical step fails, log it and continue.
         If the Jira MCP fetch fails, halt and show the error.

When complete, display the pipeline summary block from the orchestrator
(the PIPELINE COMPLETE section) and list all output files created.
```

---

## What This Command Does

1. **Connects to Atlassian Jira** via MCP and fetches all issues in the
   **GlobalMailProClaudeDemo** project (key: KAN) using JQL:
   `project = KAN ORDER BY cf[10019] ASC`
   Board: https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9

2. **Classifies issues** into: New Features, Enhancements, Bug Fixes,
   Known Issues

3. **Generates release notes** (HTML + Markdown + JSON) covering all
   classified issues, with hyperlinks from New Features to their help topics

4. **Generates a help topic** (HTML + Markdown) for each New Feature,
   following the template in `sample-data/expected-output-2.md`

5. **Runs quality review** applying:
   - 22-point MSTP checklist (`skills/release-note-reviewer-skill.md`)
   - 7-criterion style audit
   - Structure benchmark compliance (`sample-data/expected-output-1.md`,
     `sample-data/expected-output-2.md`)
   - GlobalMail Pro branding rules (`skills/branding-style-guide.md`)
   - Hyperlink integrity checks
   - JSON validity check

6. **Auto-fixes** all High and Medium severity findings

7. **Writes output files** to `output/` directory

---

## Setup (First-Time Only)

Before running this command for the first time:

### 1. Connect the Atlassian MCP server

In Claude Code, add the Atlassian MCP:

```bash
# Option A — Claude Code CLI
claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse

# Option B — Verify .mcp.json is present (already in this repo)
cat .mcp.json
```

When Claude Code first connects, it will open an Atlassian OAuth
browser window. Sign in with your Atlassian account (the account that
has access to https://twtaidimple.atlassian.net). Do not paste your
API token into any configuration file.

### 2. Verify Jira access

After connecting, confirm access to the GlobalMailProClaudeDemo project:

```
Check that the Atlassian MCP can search issues in the GlobalMailProClaudeDemo
project (KAN) at:
https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9

Test JQL: project = KAN ORDER BY cf[10019] ASC
```

### 3. Create the output directory (if it does not exist)

```bash
mkdir -p output
```

---

## Output Files Reference

| File                                  | Format   | Contents                          |
|---------------------------------------|----------|-----------------------------------|
| output/release-notes-[version].html   | HTML     | Full branded release notes         |
| output/release-notes-[version].md     | Markdown | Version-controlled release notes   |
| output/release-notes-[version].json   | JSON     | Structured data for downstream use |
| output/help-topic-[slug].html         | HTML     | Branded help topic per new feature |
| output/help-topic-[slug].md           | Markdown | Help topic per new feature          |
| output/release-note-review-report.md  | Markdown | QA review findings and auto-fix log|

---

## Troubleshooting

| Symptom                          | Likely cause                  | Fix                                       |
|----------------------------------|-------------------------------|-------------------------------------------|
| "Atlassian MCP not connected"    | MCP not added or authenticated| Run `claude mcp add atlassian ...` above  |
| Empty issue lists                | JQL returns no results        | Check GlobalMailProClaudeDemo project has issues in Jira |
| Help topic link broken           | Slug mismatch                 | Re-run pipeline (auto-fixed after review) |
| JSON parse error in output       | Writer agent error            | Check review report for RN-J1 finding     |
| No output files created          | output/ directory missing     | Run `mkdir -p output`                     |
