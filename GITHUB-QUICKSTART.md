# GitHub Release Notes Pipeline — Quick Start

## Prerequisites

1. **GitHub Account:** You have access to https://github.com/ShubhKN/WealthWise
2. **GitHub Token:** Create a personal access token at https://github.com/settings/tokens
   - Scopes needed: `repo` (all), `read:org`
   - Copy the token (you'll need it in Step 2)
3. **Claude Code:** You're running Claude Code with access to this repository

---

## Setup (One-Time)

### Step 1: Create or verify the milestone

Go to https://github.com/ShubhKN/WealthWise/milestones and ensure:
- Milestone `v1.0` exists
- All 8 issues are assigned to v1.0:
  - #1 [Feature] AI Financial Advisor Chat Interface
  - #2 [Feature] Investment Portfolio Tracking
  - #3 [Enhancement] AI-Assisted Budget Auto-Rebalancing
  - #4 [Enhancement] Transaction Auto-Categorization Review Flow
  - #5 [Bug] Budget Totals Round Incorrectly Above ₹1,00,000
  - #6 [Bug] Duplicate Recurring Bill Reminder Notifications
  - #7 [Bug] Onboarding Step 3 Slider Values Reset on Back Navigation
  - #8 [Known Issue] Delayed Sync for Linked Brokerage Holdings

### Step 2: Set your GitHub token

Run this in your terminal/PowerShell:

```bash
$env:GITHUB_TOKEN = "ghp_your_token_here"
```

Replace `ghp_your_token_here` with your actual personal access token from Step 1.

### Step 3: Verify MCP configuration

Check that `.mcp.json` has the GitHub MCP server configuration:

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

---

## Running the Pipeline

### Option 1: Use the command

```
/project:generate-release-notes
```

### Option 2: Use the full trigger prompt

Read `commands/release-note-generation-command.md` and paste the full prompt into Claude Code.

### Option 3: Invoke the orchestrator directly

```
Read agents/release-note-orchestrator.md in full, then:

1. Load all skills: release-note-writer-skill.md, wealthwise-branding.md, 
   release-note-reviewer-skill.md, github-issue-classifier.md

2. Load benchmarks: sample-data/expected-output-1.md, expected-output-2.md

3. Follow every step in the orchestrator from Step 1 through Step 10

4. Do not pause or ask for user input at any point

5. If a non-critical step fails, log it and continue

6. If GitHub MCP fetch fails, halt and show the error
```

---

## What Happens

The pipeline automatically:

1. **Connects to GitHub** and fetches all issues in ShubhKN/WealthWise (milestone v1.0)
2. **Classifies issues** into four categories based on labels:
   - What's New (type: feature)
   - Enhancements (type: enhancement)
   - Bug Fixes (type: bug, state=closed, no status: known-issue)
   - Known Issues (type: bug + status: known-issue)
3. **Generates release notes** in HTML and Markdown
4. **Generates help topics** for each What's New feature
5. **Reviews quality** against WealthWise branding and writing standards
6. **Auto-fixes** High and Medium severity findings
7. **Outputs files** to `output/` directory

Total time: ~5-10 minutes

---

## Output Files

After the pipeline completes, you'll have:

```
output/
  ├── release-note-1-0-whats-new.html           ← Main release notes (HTML)
  ├── release-note-1-0-whats-new.md             ← Main release notes (Markdown)
  ├── help-topic-#1-ai-financial-advisor-chat.html    ← Help topic for #1
  ├── help-topic-#1-ai-financial-advisor-chat.md
  ├── help-topic-#2-investment-portfolio-tracking.html ← Help topic for #2
  ├── help-topic-#2-investment-portfolio-tracking.md
  └── release-note-review-report.md             ← QA findings + fixes
```

---

## Verify the Output

1. **Open the HTML files** in a browser to check formatting and links
2. **Check the Markdown files** in your editor for correctness
3. **Review the QA report** for any remaining findings
4. **Commit to git** if everything looks good

```bash
git add output/
git commit -m "docs(release): generate v1.0 release notes from GitHub"
```

---

## Troubleshooting

| Problem | Check |
|---|---|
| "GitHub MCP not connected" | Is `$env:GITHUB_TOKEN` set? Does it have `repo` scope? |
| "No issues fetched" | Does milestone v1.0 exist? Are all 8 issues assigned to it? |
| "Output files not created" | Does `output/` directory exist? Is it writable? |
| "Help topic links broken" | Check issue #1 and #2 are labeled `type: feature` |
| "Release notes have [INSERT: ...]" | An issue is missing description or fix details |

---

## Next Steps

1. **Review output files** in `output/` directory
2. **Check for [INSERT: ...] flags** in the markdown/HTML (indicate manual input needed)
3. **Fix any Low severity findings** listed in the review report manually
4. **Commit to repository:**
   ```bash
   git add -A output/
   git commit -m "docs: release notes v1.0 (auto-generated from GitHub)"
   ```
5. **Publish:** Copy files to your documentation site or GitHub Releases

---

## Advanced: Customizing Issue Processing

To customize how issues are processed:

1. **Edit `skills/github-issue-classifier.md`** to change classification rules
2. **Edit `agents/release-note-orchestrator.md`** Step 3 to customize variables
3. **Edit `skills/release-note-writer-skill.md`** to change writing rules
4. **Edit `skills/wealthwise-branding.md`** to change HTML/CSS templates

Then re-run the pipeline. Changes are picked up automatically.

---

## Questions?

Check these files in order:

1. **CLAUDE.md** — Full project documentation
2. **agents/release-note-orchestrator.md** — Detailed pipeline steps
3. **skills/github-issue-classifier.md** — Issue classification rules
4. GitHub Issues in ShubhKN/WealthWise — For issue-specific questions
