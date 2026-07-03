# GitHub Migration Summary

## Overview

The WealthWise release note automation workflow has been successfully updated to work with **GitHub issues** instead of **Jira**. This document summarizes all changes made to enable end-to-end automatic release notes generation from GitHub milestone v1.0.

**Date:** 2026-07-03  
**Repository:** ShubhKN/WealthWise  
**Target Milestone:** v1.0  
**Status:** Ready for testing

---

## Files Updated

### 1. `.mcp.json` — MCP Server Configuration
**Change:** Replaced Atlassian MCP with GitHub MCP

**Before:**
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

**After:**
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

**Impact:** Enables GitHub API access via MCP for fetching issues.

---

### 2. `agents/release-note-orchestrator.md` — Main Orchestrator Agent

**Changes:**
- Updated all Jira references to GitHub references
- Replaced JQL queries with GitHub milestone/label queries
- Updated variable resolution map to use GitHub issue fields (title, body, number, state)
- Changed issue classification logic from Jira issue types to GitHub labels
- Updated slug generation to use GitHub issue numbers (#1, #2, etc.)
- Modified version determination to use GitHub milestone
- Updated project structure documentation

**Key Updates:**

| Aspect | Before (Jira) | After (GitHub) |
|---|---|---|
| Issue Identifier | `issue.key` (e.g., KAN-142) | `issue.number` (e.g., #5) |
| Title Field | `issue.summary` | `issue.title` |
| Description Field | `issue.description` | `issue.body` |
| Issue Type | JQL: `issuetype.name` | Labels: `type: feature`, `type: bug`, etc. |
| Version | `issue.fixVersions[0].name` | `issue.milestone.title` (v1.0) |
| Slug Format | `ww-101-ai-advisor...` | `#1-ai-financial-advisor...` |
| Query Method | JQL (project = KAN) | GitHub API (repository + milestone) |

---

### 3. `commands/release-note-generation-command.md` — Trigger Command

**Changes:**
- Updated prerequisites to check GitHub token instead of Atlassian OAuth
- Changed data source from Jira KAN to GitHub ShubhKN/WealthWise
- Updated error messages to reference GitHub MCP instead of Atlassian
- Updated trigger prompt to mention GitHub API setup

**Key Points:**
- Users must set `$env:GITHUB_TOKEN` before running
- Token requires `repo` and `read:org` scopes
- Query targets: Repository `ShubhKN/WealthWise`, Milestone `v1.0`

---

### 4. `skills/github-issue-classifier.md` — NEW FILE

**Purpose:** Defines classification rules for mapping GitHub labels to WealthWise release note categories.

**Content Includes:**
- **Issue Classification Rules:**
  - `type: feature` → What's New
  - `type: enhancement` → Enhancements
  - `type: bug` (closed, no "status: known-issue") → Bug Fixes
  - `type: bug` + `status: known-issue` → Known Issues

- **Field Extraction Rules:**
  - Title cleanup (remove prefix tags)
  - Body parsing (extract Fix sections)
  - Help topic slug generation
  - AI tag detection (labels + content matching)

- **Data Fetch Query:**
  - Repository: ShubhKN/WealthWise
  - Milestone: v1.0
  - Include all issues (open and closed)
  - Extract required fields: number, title, body, labels, state, milestone

---

### 5. `CLAUDE.md` — Project Guidance Document

**Changes:**
- Replaced all Jira references with GitHub references
- Updated MCP configuration section with GitHub MCP setup
- Updated Quick Start with GitHub token instructions
- Updated Data Flow diagram to show GitHub → Orchestrator
- Updated Issue Type Mapping to show GitHub label mapping
- Updated Architecture documentation
- Updated Troubleshooting section for GitHub-specific issues

**Key Updates:**
- Authentication: GitHub token via `$env:GITHUB_TOKEN`
- Data source: GitHub repository ShubhKN/WealthWise
- Issue mapping: Labels instead of issue types
- Constraints: GitHub issue fields instead of Jira fields

---

## How the GitHub Workflow Works

### Step-by-Step Flow

1. **Authentication**
   - User sets `$env:GITHUB_TOKEN` with valid GitHub token
   - Token has scopes: `repo` (all), `read:org`

2. **Issue Fetching (Step 2 of Orchestrator)**
   - GitHub MCP fetches all issues in ShubhKN/WealthWise repo
   - Filters for milestone: v1.0
   - Retrieves: number, title, body, labels, state, created_at, updated_at, closed_at

3. **Issue Classification (Step 4 of Orchestrator)**
   - Checks `type: *` label on each issue
   - Applies rules from `skills/github-issue-classifier.md`
   - Categorizes into: What's New, Enhancements, Bug Fixes, Known Issues

4. **Variable Resolution (Step 3 of Orchestrator)**
   - Maps GitHub fields to output variables:
     - `release_version` = "1.0" (from milestone.title)
     - `[Feature Name]` = issue.title
     - `[Bug ID]` = "#" + issue.number
     - `[slug]` = "#" + number + "-" + title_slug

5. **Release Notes Generation**
   - release-note-writer-agent.md generates HTML + Markdown
   - help-topic-writer-agent.md generates help topics for each feature
   - Both use GitHub data, not Jira data

6. **Quality Review (Step 8 of Orchestrator)**
   - release-note-reviewer-agent.md checks all output
   - Applies WealthWise standards and branding rules
   - Generates review report with findings

7. **Auto-Fix (Step 9 of Orchestrator)**
   - Applies fixes for High and Medium severity findings
   - Writes corrected output files

---

## Testing Checklist

Before running the full pipeline, verify:

- [ ] GitHub token is set: `$env:GITHUB_TOKEN`
- [ ] Token has correct scopes: `repo`, `read:org`
- [ ] Repository exists: https://github.com/ShubhKN/WealthWise
- [ ] Milestone v1.0 exists and has issues
- [ ] All 8 issues are properly labeled:
  - FEATURE-1, FEATURE-2 have `type: feature`
  - ENH-1, ENH-2 have `type: enhancement`
  - BUG-1, BUG-2, BUG-3 have `type: bug`
  - KNOWN-1 has `type: bug` + `status: known-issue`
- [ ] output/ directory exists and is writable
- [ ] All agent files are present and readable

---

## Running the Pipeline

### Command

```
/project:generate-release-notes
```

Or run the full trigger prompt from `commands/release-note-generation-command.md`

### Expected Output

```
PIPELINE COMPLETE
=================

GitHub repository: ShubhKN/WealthWise (https://github.com/ShubhKN/WealthWise)
Release version: 1.0
Release date:    2026-07-03

Issues fetched:  8

Issues classified:
  What's New:    2 issues → [#1, #2]
  Enhancements:  2 issues → [#3, #4]
  Bug Fixes:     3 issues → [#5, #6, #7]
  Known Issues:  1 issues → [#8]

Output files:
  ✓ output/release-note-1-0-whats-new.html
  ✓ output/release-note-1-0-whats-new.md
  ✓ output/help-topic-#1-ai-financial-advisor-chat.html
  ✓ output/help-topic-#1-ai-financial-advisor-chat.md
  ✓ output/help-topic-#2-investment-portfolio-tracking.html
  ✓ output/help-topic-#2-investment-portfolio-tracking.md
  ✓ output/release-note-review-report.md

Review result:     [PASS / REVISED]
High findings:     0 fixed
Medium findings:   0 fixed
Low remaining:     0 — no auto-fix applied

Next step: Human technical review → commit to repository → publish
```

---

## Mapping Reference

### GitHub Issues Created (in Milestone v1.0)

| # | Title | Labels | Category |
|---|---|---|---|
| #1 | [Feature] AI Financial Advisor Chat Interface | `type: feature`, `component: ai-advisor`, `priority: highest`, `plan: pro`, `plan: family` | What's New |
| #2 | [Feature] Investment Portfolio Tracking | `type: feature`, `component: investments`, `priority: high`, `plan: pro`, `plan: family` | What's New |
| #3 | [Enhancement] AI-Assisted Budget Auto-Rebalancing | `type: enhancement`, `component: budget`, `priority: medium`, `plan: all` | Enhancements |
| #4 | [Enhancement] Transaction Auto-Categorization Review Flow | `type: enhancement`, `component: transactions`, `priority: medium`, `plan: all` | Enhancements |
| #5 | [Bug] Budget Totals Round Incorrectly Above ₹1,00,000 | `type: bug`, `component: budget`, `priority: high`, `severity: medium` | Bug Fixes |
| #6 | [Bug] Duplicate Recurring Bill Reminder Notifications | `type: bug`, `component: notifications`, `priority: high`, `severity: medium` | Bug Fixes |
| #7 | [Bug] Onboarding Step 3 Slider Values Reset on Back Navigation | `type: bug`, `component: onboarding`, `priority: medium`, `severity: low` | Bug Fixes |
| #8 | [Known Issue] Delayed Sync for Linked Brokerage Holdings | `type: bug`, `status: known-issue`, `component: investments`, `priority: medium` | Known Issues |

---

## Troubleshooting

### Issue: "GitHub MCP not connected"

**Solution:** Verify `.mcp.json` is present and `$env:GITHUB_TOKEN` is set with a valid token.

```bash
$env:GITHUB_TOKEN = "ghp_your_token"
```

### Issue: "No issues fetched from GitHub"

**Solutions:**
1. Verify token has `repo` scope: https://github.com/settings/tokens
2. Verify repository exists: https://github.com/ShubhKN/WealthWise
3. Verify milestone v1.0 exists and has issues
4. Check all issues have proper labels (type: feature/enhancement/bug)

### Issue: "Help topic links broken"

**Solution:** Ensure slug generation is correct. Check orchestrator Step 5:
```
slug = "#" + issue.number + "-" + lowercase_hyphenated(issue.title[0:40])
```

---

## Future Enhancements

Potential improvements for future iterations:

1. **Multiple Milestones:** Support release notes for multiple milestones
2. **Filtering:** Add support for filtering by labels (e.g., `component: budget`)
3. **Custom Templates:** Allow per-milestone branding overrides
4. **Automated Publishing:** Integrate with GitHub Releases API
5. **Changelog Generation:** Auto-generate CHANGELOG.md from issues
6. **Localization:** Support for multi-language release notes

---

## References

- **GitHub MCP Server:** @modelcontextprotocol/server-github
- **WealthWise Repository:** https://github.com/ShubhKN/WealthWise
- **Release Milestone:** https://github.com/ShubhKN/WealthWise/issues?milestone=1
- **Orchestrator:** `agents/release-note-orchestrator.md`
- **Issue Classifier:** `skills/github-issue-classifier.md`
- **Branding Guide:** `skills/wealthwise-branding.md`

---

## Sign-Off

✅ **Migration Complete**

All Jira references have been replaced with GitHub equivalents.
The workflow is ready for end-to-end testing with the ShubhKN/WealthWise repository.

**Status:** Ready for Pipeline Testing
