# MCP Integration Concept — WealthWise Release Notes

## Overview

This document describes the integration of the WealthWise release note automation pipeline with the Atlassian MCP (Model Context Protocol) server, enabling automatic fetching of issues from a Jira instance and real-time generation of branded release notes and help topics.

---

## Architecture

### Data Flow

```
Jira Instance (twtaishubh.atlassian.net)
       │
       │  Atlassian MCP Server (https://mcp.atlassian.com/sse)
       │  JQL: project = KAN ORDER BY cf[10019] ASC
       │
       ▼
release-note-orchestrator.md (this workflow)
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
```

---

## Jira Integration Details

### Instance Configuration

| Parameter | Value |
|-----------|-------|
| **Jira Site URL** | `https://twtaishubh.atlassian.net` |
| **Project Key** | `KAN` |
| **Project Name** | (auto-detected from Jira) |
| **Board URL** | `https://twtaishubh.atlassian.net/jira/software/projects/KAN/list?jql=project%20%3D%20KAN%20ORDER%20BY%20cf%5B10019%5D%20ASC` |
| **JQL Query** | `project = KAN ORDER BY cf[10019] ASC` |

### Fields Retrieved Per Issue

The orchestrator retrieves the following fields for each Jira issue:

- `key` — Jira issue key (e.g., KAN-42)
- `summary` — Issue title
- `description` — Issue description
- `issuetype.name` — Type (Story, Feature, Bug, Task, Enhancement, etc.)
- `status.name` — Current status (To Do, In Progress, Done, etc.)
- `labels` — Issue labels (including "ai", "known-issue", etc.)
- `fixVersions` — Release version(s) associated with the issue
- `assignee.displayName` — Person assigned to the issue
- `resolution.name` — Resolution status (Fixed, Won't Fix, etc.)
- `resolution.description` — Resolution details
- `created` — Issue creation date
- `updated` — Last update date
- `comment` — All issue comments (checked for fix details, workarounds)
- `remotelinks` — Linked pages (e.g., Confluence documentation)

### Issue Classification

Jira issues are classified into release note categories using this mapping:

| Jira Issue Type | Release Note Category |
|-----------------|----------------------|
| Story, Feature, New Feature | What's New |
| Task, Enhancement, Improvement, Sub-task | Enhancements |
| Bug | Bug Fixes |
| Any type with label "known-issue" | Known Issues |
| Epic | Skipped (not included in output) |

---

## MCP Server Setup

### Prerequisites

1. **Atlassian Account** — Must have access to the KAN project in `https://twtaishubh.atlassian.net`
2. **Claude Code with Atlassian MCP** — The MCP server must be configured and authenticated
3. **Output Directory** — The `output/` directory must exist in the project root (created automatically if missing)

### Connecting the Atlassian MCP

```bash
# Option A — Using Claude Code CLI
claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse

# Option B — Using Claude Code Settings
# Open Claude Code settings, go to MCP Servers, add:
# - Name: atlassian
# - Type: SSE
# - URL: https://mcp.atlassian.com/sse
```

When first connecting, Claude Code will open an Atlassian OAuth authentication window. Sign in with your Atlassian account (the one with access to `twtaishubh.atlassian.net`). **Do not** store API tokens or credentials in project files — OAuth is handled automatically by Claude Code.

### Verification

After connecting, verify that the MCP can access the KAN project:

```
Test JQL: project = KAN ORDER BY cf[10019] ASC
Expected: Returns all issues in the KAN project, ordered by custom field cf[10019]
```

If no issues are returned, check that:
1. The KAN project exists in `https://twtaishubh.atlassian.net`
2. The Atlassian OAuth token is active and has read access to the KAN project
3. The project has at least one issue created

---

## Runtime Workflow

### Trigger

To generate release notes from Jira, run:

```bash
# In Claude Code
/project:generate-release-notes
```

Or paste the trigger prompt from `commands/release-note-generation-command.md` into Claude Code.

### Process

1. **Orchestrator loads skills and benchmarks** — Reads all writing rules, branding guidelines, and output structure templates
2. **MCP fetches issues from Jira** — Executes JQL query `project = KAN ORDER BY cf[10019] ASC` and retrieves all matching issues with full field data
3. **Issues are classified** — Each issue is categorized (What's New, Enhancements, Bug Fixes, Known Issues) based on type and labels
4. **Release version is resolved** — Derived from the first `fixVersions` value found, or generated as `YYYY.MM` if no versions are set
5. **Sub-agents are invoked** — Writer and help-topic-writer agents produce draft HTML and Markdown output files
6. **Quality review runs** — Reviewer agent applies checklist and benchmarks, producing a review report
7. **Auto-fixes are applied** — All High and Medium severity findings are corrected automatically
8. **Output files are written** — Final HTML, Markdown, and review report are saved to `output/`

### Output

The pipeline produces these files in the `output/` directory:

| File | Format | Content |
|------|--------|---------|
| `release-note-[version]-whats-new.html` | HTML | Branded release note with all sections and help topic links |
| `release-note-[version]-whats-new.md` | Markdown | Version-controlled release note source |
| `help-topic-[slug].html` | HTML | Branded help topic (one per What's New feature) |
| `help-topic-[slug].md` | Markdown | Help topic (one per What's New feature) |
| `release-note-review-report.md` | Markdown | QA findings, auto-fix log, and recommendations |

---

## Configuration Files

### .mcp.json

Configures the Atlassian MCP server connection:

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

The Jira site URL and project key are specified in `agents/release-note-orchestrator.md` (not in `.mcp.json`), allowing the same MCP connection to serve multiple Jira instances.

### agents/release-note-orchestrator.md

Key settings at the top of the file:

```markdown
jira_board_url: "https://twtaishubh.atlassian.net/jira/software/projects/KAN/list?jql=..."
jql: "project = KAN ORDER BY cf[10019] ASC"
```

If you need to change the Jira instance or project key in the future, update only these two lines.

---

## Security & Constraints

### Authentication

- **No tokens in files** — Atlassian OAuth is managed by Claude Code. Do not store API keys, personal access tokens, or passwords in any project file.
- **Scope control** — The authenticated OAuth token has access only to resources visible in your Atlassian account.

### Content

- **No invented content** — Every claim in release notes must trace directly to a Jira issue field.
- **No internal IDs** — Jira issue keys appear only in the Bug Fixes table (Bug ID column). All other sections use natural language only.
- **No engineering details** — Infrastructure, technical jargon, and internal processes are stripped from customer-facing output.
- **No severity labels** — WealthWise release notes never display priority/severity ratings (P1, Critical, Blocker, etc.) — this is enforced by the reviewer agent.

### Scope

- **Read-only** — The pipeline only reads from Jira. It does not create, modify, or delete issues.
- **Single project** — Only the KAN project (as specified in the JQL) is included. Issues from other projects are ignored.
- **All issues included** — The JQL `project = KAN ORDER BY cf[10019] ASC` includes all issues in the project regardless of status or assignee.

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "Atlassian MCP not connected" | MCP not added or not authenticated | Run `claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse` and sign in |
| Empty or incomplete issue lists | JQL query returns no results | Verify KAN project exists and has issues in `https://twtaishubh.atlassian.net` |
| OAuth token expired | MCP connection lost after extended time | Reconnect via Claude Code settings → MCP Servers |
| Help topic links broken | Slug derivation error | Re-run the pipeline — slugs are auto-corrected after review |
| Output files not created | `output/` directory missing or not writable | Create directory: `mkdir -p output` |
| Jira field data missing in output | Field not retrieved by orchestrator | Check `agents/release-note-orchestrator.md` Step 2 for the field list; add missing fields if needed |

---

## Next Steps

1. Verify Atlassian MCP is connected (`claude mcp add atlassian ...`)
2. Verify OAuth is authenticated for `twtaishubh.atlassian.net`
3. Run the trigger command: `/project:generate-release-notes`
4. Check `output/release-note-review-report.md` for any quality findings
5. Review and approve output files before publishing
