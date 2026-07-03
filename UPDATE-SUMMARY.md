# Configuration Update Summary

**Date:** 2026-07-03

**Updated by:** Claude Code

---

## Overview

The WealthWise release note automation pipeline has been reconfigured to fetch issues from the actual Jira project at `https://twtaishubh.atlassian.net` (project key: `KAN`) instead of the placeholder WealthWiseReleaseDemo project.

---

## Files Updated

### 1. **mcp-plugin-concept/integration-concept.md** ✓ CREATED
   - **Status:** New file created
   - **Content:** Comprehensive integration documentation covering:
     - Data flow architecture
     - Jira instance configuration (twtaishubh.atlassian.net, KAN project)
     - MCP server setup instructions
     - Runtime workflow
     - Security and constraints
     - Troubleshooting guide
   - **Key Changes:** Documented the real Jira instance URL and KAN project key

### 2. **agents/release-note-orchestrator.md** ✓ UPDATED
   - **Status:** Updated
   - **Changes:**
     - Project key: `WW` → `KAN`
     - Jira instance: `wealthwise-release-demo.atlassian.net` → `twtaishubh.atlassian.net`
     - JQL query: `project = WW` → `project = KAN`
     - Board URL updated to match new instance
     - Removed placeholder disclaimer (now using actual instance)
     - Updated example issue IDs: `WW-42` → `KAN-42`, `WW-101` → `KAN-101`, etc.
     - Updated pipeline summary output to reference KAN project

### 3. **commands/release-note-generation-command.md** ✓ UPDATED
   - **Status:** Updated
   - **Changes:**
     - Data source: `WealthWiseReleaseDemo (WW)` → `KAN (https://twtaishubh.atlassian.net)`
     - JQL updated: `project = WW` → `project = KAN`
     - Setup instructions now reference KAN project specifically
     - Troubleshooting entries updated to reference correct Jira instance

### 4. **CLAUDE.md** ✓ UPDATED
   - **Status:** Updated
   - **Changes:**
     - Project description updated to reference actual Jira instance URL
     - MCP setup instructions now specify correct Jira instance
     - Data flow diagram updated: `WW` → `KAN`
     - Directory structure includes `mcp-plugin-concept/` folder
     - Jira access requirements updated to specify KAN project at correct URL
     - Troubleshooting section updated with correct project details

### 5. **.mcp.json** ✓ UPDATED
   - **Status:** Updated
   - **Changes:**
     - Updated description to reference KAN project at correct Jira instance
     - Clarified authentication handling (OAuth, no credentials in file)

---

## Configuration Summary

| Parameter | Old Value | New Value |
|-----------|-----------|-----------|
| **Jira Site URL** | `wealthwise-release-demo.atlassian.net` | `twtaishubh.atlassian.net` |
| **Project Key** | `WW` | `KAN` |
| **JQL Query** | `project = WW ORDER BY cf[10019] ASC` | `project = KAN ORDER BY cf[10019] ASC` |
| **Board URL** | `https://wealthwise-release-demo.atlassian.net/jira/software/projects/WW/...` | `https://twtaishubh.atlassian.net/jira/software/projects/KAN/...` |

---

## How to Use

### Prerequisites

1. **Atlassian MCP Connection**
   ```bash
   claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse
   ```
   When prompted, sign in with your Atlassian account that has access to the KAN project.

2. **Verify Access**
   - Ensure you have read access to the KAN project at https://twtaishubh.atlassian.net
   - No credentials should be stored in any project file (OAuth is handled by Claude Code)

### Running the Pipeline

```bash
# In Claude Code, run:
/project:generate-release-notes
```

Or manually trigger by reading the full prompt from `commands/release-note-generation-command.md`.

### What Happens

1. **Fetch:** Orchestrator queries `project = KAN ORDER BY cf[10019] ASC` via Atlassian MCP
2. **Classify:** Issues are categorized into What's New, Enhancements, Bug Fixes, Known Issues
3. **Generate:** Sub-agents produce branded HTML + Markdown release notes and help topics
4. **Review:** Reviewer agent applies quality checklist and benchmarks
5. **Auto-fix:** High and Medium severity findings are corrected automatically
6. **Output:** Finalized files written to `output/` directory

---

## Output Files

All files are generated in the `output/` directory:

- `release-note-[version]-whats-new.html` — Branded HTML release note
- `release-note-[version]-whats-new.md` — Markdown version
- `help-topic-[slug].html` — Branded help topic (one per What's New feature)
- `help-topic-[slug].md` — Help topic (one per What's New feature)
- `release-note-review-report.md` — QA review findings and auto-fix log

---

## Sample Data

The sample data files in `sample-data/` remain unchanged and continue to use example WW issue IDs (WW-1, WW-2, etc.). These are structure and quality benchmarks only — they are never used as live data. The pipeline always pulls data directly from Jira.

---

## Documentation References

- **Integration Details:** See `mcp-plugin-concept/integration-concept.md`
- **Orchestrator Instructions:** See `agents/release-note-orchestrator.md`
- **Trigger Command:** See `commands/release-note-generation-command.md`
- **Branding Rules:** See `skills/wealthwise-branding.md`
- **Writing Standards:** See `skills/release-note-writer-skill.md`
- **Review Checklist:** See `skills/release-note-reviewer-skill.md`

---

## Next Steps

1. ✅ Configuration files updated to point to KAN project
2. ✅ Integration documentation created
3. ⬜ **(You need to do this)** Connect Atlassian MCP and authenticate with your Jira account
4. ⬜ **(You need to do this)** Run `/project:generate-release-notes` to test the pipeline
5. ⬜ Review and approve generated release notes before publishing

---

## Notes

- All changes are backward compatible with the existing agent and skill files
- No credentials or API tokens have been added to any files
- The pipeline is ready to run against live Jira data immediately after MCP authentication
- Sample data benchmarks in `sample-data/` are unchanged and serve as quality references
