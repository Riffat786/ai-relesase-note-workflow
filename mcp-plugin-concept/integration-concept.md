# MCP Integration Concept — Atlassian Jira + Confluence

## Overview

This document describes how the release note pipeline integrates with
Atlassian Jira and Confluence via the Atlassian Remote MCP server.

---

## MCP Server

| Property    | Value                               |
|-------------|-------------------------------------|
| Provider    | Atlassian                           |
| Type        | Remote SSE MCP server               |
| URL         | https://mcp.atlassian.com/sse       |
| Auth        | Atlassian OAuth 2.0 (browser-based) |
| Configured  | .mcp.json (project root)            |

---

## Jira Integration

### Data fetched

The pipeline queries the **GlobalMailProClaudeDemo** project using:

```
Project display name: GlobalMailProClaudeDemo
Project key: KAN
JQL: project = KAN ORDER BY cf[10019] ASC
Board URL: https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9
```

Fields extracted per issue:
- `key` — Issue ID (e.g. KAN-42)
- `summary` — Feature/bug title
- `description` — Full description (Markdown or Atlassian Document Format)
- `issuetype.name` — Story, Bug, Task, Enhancement, etc.
- `status.name` — To Do, In Progress, Done, etc.
- `labels` — Used to identify Known Issues (label: "known-issue")
- `fixVersions` — Determines the release version
- `priority.name` — High, Medium, Low
- `assignee.displayName` — For internal tracking (not in output prose)
- `comment` — Latest comments for additional context

### Issue type mapping

| Jira issuetype.name              | Release note category |
|----------------------------------|-----------------------|
| Story, Feature, New Feature      | New Features          |
| Task, Enhancement, Improvement   | Enhancements          |
| Bug                              | Bug Fixes             |
| Any type + label "known-issue"   | Known Issues          |
| Epic                             | Skipped               |

---

## Confluence Integration

If a Jira issue links to a Confluence page (via the "Confluence Pages"
field or a URL in the description), the pipeline optionally fetches that
page for additional feature context.

The Confluence MCP tools used:
- `confluence_search` — Search pages by title or space
- `confluence_get_page` — Fetch page content by ID

This is non-critical: the pipeline continues if no Confluence pages are
linked or if the Confluence fetch fails.

---

## Authentication Setup

1. Run in Claude Code:
   ```bash
   claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse
   ```

2. Claude Code opens a browser for Atlassian OAuth.

3. Sign in with the account that has access to the
   **GlobalMailProClaudeDemo** project at `https://twtaidimple.atlassian.net`.

4. OAuth tokens are stored securely by Claude Code — never in project files.

**Security requirements:**
- Do not store API keys, tokens, or passwords in `.mcp.json` or any
  project file.
- Do not log tokens in output files or commit messages.
- Use only Atlassian OAuth for authentication.

---

## Error Handling

| Condition                        | Pipeline behaviour                            |
|----------------------------------|-----------------------------------------------|
| MCP not connected                | Halt with clear error message                 |
| Jira search returns 0 issues     | Halt and report (check JQL + access)          |
| Issue description is empty       | Use summary only, flag with [INSERT:]         |
| Confluence page fetch fails      | Log, skip, continue with Jira data only       |
| Fix version not set in Jira      | Derive version from current date (YYYY.MM)    |

---

## Future Enhancements

- **Confluence publish**: After review, write the help topic as a
  new Confluence page in the GlobalMail Pro Help Center space.
- **Jira transition**: After pipeline completes, transition all
  "Done" issues to "Released" status.
- **Webhook trigger**: Trigger the pipeline automatically when a
  Jira sprint is closed or a release is created.
