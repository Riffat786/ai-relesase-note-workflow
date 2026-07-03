# Future AI-Powered Workflow — Automated Release Note Generation

**Version:** 2.0  
**Last Updated:** 2026-07-03  
**Audience:** Product managers and technical writers using the fully automated AI-powered pipeline

---

## Overview

This document describes the **end-to-end, AI-automated workflow** for generating WealthWise release notes using:

- **Skills** — Reusable AI personas for writing and reviewing (senior technical writer, QA reviewer)
- **Agents** — Autonomous AI workflows that coordinate data fetching, writing, and quality review
- **MCPs (Model Context Protocol)** — Integrations that connect Claude to external systems (GitHub API)

**This workflow replaces the 3–4 hour manual process with a fully automated 15-minute pipeline.**

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER TRIGGERS COMMAND                         │
│         /project:generate-release-notes (or skill invocation)    │
└──────────────────────┬──────────────────────────────────────────┘
                       │
       ┌───────────────▼────────────────┐
       │  Release Note Orchestrator     │
       │  (agents/release-note-      │
       │   orchestrator.md)             │
       │                                │
       │  Responsibilities:             │
       │  - Read all skills & rules   │
       │  - Connect to GitHub MCP     │
       │  - Fetch issues from v1.0    │
       │  - Classify by category      │
       │  - Coordinate sub-agents     │
       │  - Manage quality review     │
       │  - Apply auto-fixes          │
       │  - Generate output files     │
       └───────────────┬────────────────┘
                       │
       ┌───────────────┴────────────────┐
       │  (Fetches issues via GitHub MCP) │
       │  Repository: ShubhKN/WealthWise │
       │  Milestone: v1.0               │
       └───────────────┬────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   ┌────▼────┐  ┌─────▼─────┐  ┌────▼─────┐
   │  Writer │  │ Help Topic│  │ Reviewer │
   │  Agent  │  │  Agent    │  │  Agent   │
   │         │  │           │  │          │
   │Produces:│  │ Produces: │  │Produces: │
   │- .html  │  │ - .html   │  │- Report  │
   │- .md    │  │ - .md     │  │- Fixes   │
   └────┬────┘  └─────┬─────┘  └────┬─────┘
        │             │             │
        └─────────────┼─────────────┘
                      │
         ┌────────────▼──────────────┐
         │  Output Files in output/  │
         │                           │
         │ - release-note-[v]-      │
         │   whats-new.html/.md     │
         │ - help-topic-[slug].     │
         │   html/.md (1 per feature)│
         │ - release-note-review-   │
         │   report.md              │
         └───────────────────────────┘
```

---

## Component Breakdown

### 1. Skills (AI Personas)

Skills are reusable AI instructions that define expertise and writing standards.

#### A. Release Note Writer Skill
**File:** `skills/release-note-writer-skill.md`

**Role:** Senior technical writer with expertise in WealthWise product, customer communication, and release note conventions.

**Responsibility:**
- Write release note entries (What's New, Enhancements)
- Create help topics for each new feature
- Follow three-part narrative (Previously → Now → Value)
- Use second person ("you"), active voice, no jargon
- Apply AI tags where applicable
- Embed WealthWise branding

**Called by:** Writer Agent and Help Topic Agent

---

#### B. Release Note Reviewer Skill
**File:** `skills/release-note-reviewer-skill.md`

**Role:** QA reviewer with expertise in quality standards, checklist verification, and finding issues.

**Responsibility:**
- Audit structure against expected benchmarks
- Check writing standards (voice, tense, terminology)
- Verify hyperlink integrity
- Confirm branding compliance
- Classify findings by severity (High, Medium, Low)
- Generate detailed review report

**Called by:** Reviewer Agent

---

#### C. WealthWise Branding Skill
**File:** `skills/wealthwise-branding.md`

**Role:** Brand authority defining visual and verbal identity.

**Contents:**
- Colour palette (#2D5A8C primary blue)
- Typography and font stack
- HTML template and CSS
- Category icons and tag styling
- Copyright and footer rules
- Logo placement guidelines

**Applied by:** Writer Agent when generating HTML

---

#### D. GitHub Issue Classifier Skill
**File:** `skills/github-issue-classifier.md`

**Role:** Expert in mapping GitHub labels to release note categories.

**Rules:**
- `type: feature` → What's New
- `type: enhancement` → Enhancements
- `type: bug` (closed, no `status: known-issue`) → Bug Fixes
- `type: bug` + `status: known-issue` → Known Issues
- Open bugs → Skip
- Tracking issues → Skip

**Applied by:** Orchestrator

---

### 2. Agents (Autonomous Workflows)

Agents are AI workflows that execute multi-step tasks without user intervention.

#### A. Release Note Orchestrator Agent
**File:** `agents/release-note-orchestrator.md`

**Entry Point:** `/project:generate-release-notes` or invoked as a skill

**Pipeline (7 steps):**

**Step 1 — Initialize**
- Read all skills and benchmarks
- Load branding rules, reviewer checklist, writer standards, classifier rules
- Store in working memory

**Step 2 — Connect to GitHub MCP & Fetch Issues**
- Authenticate via GitHub MCP with `GITHUB_TOKEN` environment variable
- Query: `Repository: ShubhKN/WealthWise, Milestone: v1.0`
- Retrieve all issues (open and closed) with fields:
  - Issue number, title, body, labels, state, milestone, timestamps
- If fetch fails, halt and report error

**Step 3 — Resolve Runtime Variables**
- Map each issue field to output variable (see table below)
- Generate slugs for help topics
- Determine release version (v1.0 → "1.0")
- Set release_date to today (e.g., 2026-07-03)
- Never invent values; use [INSERT: ...] flags for missing data

**Variable Resolution Map:**

| Variable | Source | Fallback | Example |
|---|---|---|---|
| `product_name` | Branding constant | None — always "WealthWise" | WealthWise |
| `release_version` | `issue.milestone.title` | "1.0" | 1.0 |
| `release_date` | Today's date | None — always today | 2026-07-03 |
| `[Feature Name]` | `issue.title` (sentence case) | `[INSERT: feature name — #N missing]` | AI Insight banner... |
| `[slug]` | `#[number]-[title-slug-max-40-chars]` | None — always derivable | #1-ai-insight-banner |
| `[Bug ID]` | `#[number]` (only in Bug Fixes table) | None — always present | #5 |
| `[is_ai_feature]` | Check labels or title/body mention | false | true |

**Step 4 — Classify Issues by Category**
- Apply classifier rules to each issue
- Build four lists: `whats_new[]`, `enhancements[]`, `bug_fixes[]`, `known_issues[]`
- Log any unclassified or edge-case issues
- Pass categorized issues to sub-agents

**Step 5 — Generate Help Topic Map**
- For each What's New issue, generate slug and output filename
- Build map: `{issue.number → help_topic_filename}`
- Pass map to Writer Agent so it can link help topics

**Step 6 — Delegate to Sub-Agents**
- **Writer Agent:** Generate release note (HTML + Markdown)
- **Help Topic Agent:** Generate help topic for each What's New feature
- **Reviewer Agent:** Run quality checks and produce review report
- Collect outputs from all agents

**Step 7 — Apply Auto-Fixes & Generate Final Output**
- Reviewer Agent produces report with High, Medium, Low severity findings
- Orchestrator applies auto-fixes for all High and Medium findings
- If changes were made, re-run Reviewer Agent (max 2 iterations to prevent loops)
- Write all final files to `output/` directory
- Produce summary: "Generated 2 What's New features, 1 enhancement, 2 bug fixes, 0 known issues. Review report: 3 findings auto-fixed."

---

#### B. Release Note Writer Agent
**File:** `agents/release-note-writer-agent.md`

**Inputs from Orchestrator:**
- `whats_new[]` — Array of What's New issues
- `enhancements[]` — Array of Enhancement issues
- `bug_fixes[]` — Array of Bug Fix issues
- `release_version` — e.g., "1.0"
- `release_date` — e.g., "2026-07-03"
- `help_topic_map` — `{#1 → help-topic-#1-slug.html, ...}`
- All resolved variables and branding rules

**Processing:**

1. **Generate What's New entries** using Writer Skill
   - Apply three-part narrative (Previously → Now → Value)
   - Add AI tag if `is_ai_feature = true`
   - Link to help topic using `help_topic_map`
   - Example output:
     ```markdown
     ### AI Insight banner with contextual spending alerts <span class="tag tag-ai">AI</span>
     
     Previously, you had no proactive visibility...
     Now, the Dashboard shows...
     You catch overspending while there is still time to change course.
     ```

2. **Generate Enhancements entries** using Writer Skill
   - Same three-part narrative pattern
   - Apply AI tag if applicable

3. **Generate Bug Fixes table** with three columns
   - Bug ID, Description (past tense), Fix/Solution (present tense)
   - No severity labels
   - No internal jargon

4. **Generate Known Issues section** (if any)
   - Current-tense description
   - Status (ongoing, workaround available, etc.)

5. **Assemble full release note**
   - Title: "WealthWise — Release 1.0 (July 2026)"
   - Intro paragraph with category counts
   - Four sections in order: 🚀 What's New, ✨ Enhancements, 🐛 Bug Fixes, ⚠️ Known Issues

6. **Generate HTML version**
   - Apply WealthWise branding (colors, fonts, layout)
   - Embed CSS for styling
   - Make responsive (mobile-friendly)
   - Include header with logo, footer with copyright
   - Link help topics in What's New section

7. **Output two files:**
   - `output/release-note-[version]-whats-new.md` (Markdown)
   - `output/release-note-[version]-whats-new.html` (Branded HTML)

---

#### C. Help Topic Writer Agent
**File:** `agents/help-topic-writer-agent.md`

**Inputs from Orchestrator:**
- `whats_new[]` — Array of What's New issues (one help topic per issue)
- `release_version`
- Branding rules and writing standards

**Processing per issue:**

1. **Generate help topic content** using Writer Skill
   - Page title: "[Feature Name] — WealthWise Help"
   - Breadcrumb: "WealthWise Help > Release Notes > [Feature Name]"
   - Overview paragraph explaining the feature
   - Optional: 3–5 numbered steps if workflow applies
   - Link back to main release note
   - Same writing standards as release note (second person, active voice)

2. **Generate slug** from issue title
   - Format: `#[number]-[lowercase-hyphenated-title-max-40-chars]`
   - Example: `#1-ai-insight-banner-spending-alerts`

3. **Generate HTML version**
   - Apply WealthWise branding
   - Responsive layout
   - Include header with breadcrumb

4. **Output two files per issue:**
   - `output/help-topic-[slug].md` (Markdown)
   - `output/help-topic-[slug].html` (Branded HTML)

**Example output structure:**
```
output/help-topic-#1-ai-insight-banner-spending-alerts.md
output/help-topic-#1-ai-insight-banner-spending-alerts.html
output/help-topic-#3-[next-feature-slug].md
output/help-topic-#3-[next-feature-slug].html
...
```

---

#### D. Release Note Reviewer Agent
**File:** `agents/release-note-reviewer-agent.md`

**Inputs from Orchestrator:**
- `release-note-[version]-whats-new.html` — Generated release note
- `release-note-[version]-whats-new.md` — Generated release note
- `help-topic-[slug].html` — All help topics
- All sample benchmark files
- Reviewer Skill checklist and standards

**Processing:**

1. **Run structure compliance checks**
   - Verify release note matches `sample-data/expected-output-1.md` structure
   - Verify help topic matches `sample-data/expected-output-2.md` structure
   - Check all four categories present (What's New, Enhancements, Bug Fixes, Known Issues)

2. **Run writing standards checks**
   - Second person ("you") used in What's New and Enhancements
   - Active voice (no passive constructions)
   - Three-part narrative pattern followed
   - Bug fixes in past/present tense (not hype)
   - No GitHub issue numbers in prose (only Bug Fixes table)
   - No severity or priority labels
   - No internal jargon

3. **Check hyperlink integrity**
   - Every What's New entry links to help topic (HTML)
   - Every help topic links back to release note
   - No broken links (files exist)
   - URLs well-formed

4. **Check branding compliance**
   - WealthWise logo/name present
   - Colour palette correct (#2D5A8C)
   - System font stack used
   - Category icons present (🚀 ✨ 🐛 ⚠️)
   - Copyright footer present
   - AI tags applied to AI features
   - Layout responsive

5. **Classify findings by severity**
   - **High:** Missing required content, broken links, invalid structure
   - **Medium:** Writing standard violations, branding misses
   - **Low:** Style nitpicks, tone refinements (non-blocking)

6. **Generate findings report**
   - List each finding with:
     - Section/file affected
     - Severity (High, Medium, Low)
     - Description
     - Suggested fix
   - Example:
     ```
     **Finding:** What's New entry "AI Insight banner" missing from release note
     **Severity:** High
     **File:** output/release-note-1-0-whats-new.html
     **Description:** Issue #1 classified as What's New but not in generated output
     **Suggested Fix:** Verify Writer Agent received issue and that slug generation succeeded
     ```

7. **Output review report**
   - `output/release-note-review-report.md`
   - Sections: Summary (count by severity), High findings, Medium findings, Low findings, Log of auto-fixes applied

---

### 3. GitHub MCP (Model Context Protocol)

**Purpose:** Connect Claude to GitHub API without hardcoding credentials

**Configuration:** `.mcp.json` in project root

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

**Authentication:**
- Token provided via `GITHUB_TOKEN` environment variable
- Required scopes: `repo` (all), `read:org`
- No credentials stored in project files

**Capabilities:**
- List issues in milestone
- Fetch issue details (body, labels, state)
- Create/update issues (optional)
- Query pull requests (future use)

---

## Workflow Execution

### Trigger Command

```bash
/project:generate-release-notes
```

Or via skill invocation from Claude Code:

```bash
/generate-release-notes
```

### Execution Timeline

| Step | Time | What Happens |
|---|---|---|
| 1. Initialize | 5 sec | Skills and benchmarks loaded into memory |
| 2. Fetch GitHub | 10 sec | All v1.0 issues retrieved (4–6 issues) |
| 3. Classify | 5 sec | Issues categorized into four lists |
| 4. Write (in parallel) | 60 sec | Writer, Help Topic, Reviewer agents run simultaneously |
| 5. Review | 30 sec | Quality report generated |
| 6. Auto-fix | 20 sec | High/Medium findings corrected |
| 7. Output | 5 sec | Files written to `output/` directory |
| **Total** | ~**2 minutes** | All files generated and ready |

**No user input required after trigger.**

---

## Output Files

### Generated Files

```
output/
├── release-note-1-0-whats-new.md
├── release-note-1-0-whats-new.html
├── help-topic-#1-ai-insight-banner-spending-alerts.md
├── help-topic-#1-ai-insight-banner-spending-alerts.html
├── help-topic-#3-[feature-name-slug].md
├── help-topic-#3-[feature-name-slug].html
└── release-note-review-report.md
```

### No JSON Output

WealthWise uses **only HTML and Markdown**, no JSON. This is a deliberate choice per `skills/wealthwise-branding.md`:
- HTML for web publication
- Markdown for version control and editing
- JSON not supported

---

## Quality Assurance Loop

### Iteration on Failures

If Reviewer Agent finds issues:

1. **High severity findings** (missing content, broken structure)
   - Orchestrator applies corrections to source data
   - Re-runs Writer Agent with corrected data
   - Re-runs Reviewer Agent to verify fix

2. **Medium severity findings** (writing standards, branding)
   - Orchestrator applies text corrections
   - Re-runs Reviewer Agent
   - If still failing, loop once more (max 2 iterations to prevent infinite loops)

3. **Low severity findings**
   - Logged in review report
   - Noted for human review but not auto-fixed
   - Stakeholders can choose to manually address or accept

### Auto-Fix Examples

**Before (High severity):**
```
Missing title: [INSERT: feature name — GitHub issue #1 has no title]
```

**After auto-fix:**
- Orchestrator flags issue in GitHub
- Re-fetches with corrected title
- Writer Agent regenerates with correct title

**Before (Medium severity - passive voice):**
```
The AI Insight banner is displayed on the dashboard to notify users.
```

**After auto-fix:**
```
The dashboard displays an AI Insight banner that notifies you of spending trends.
```

---

## Error Handling

### Critical Failures (Pipeline Halts)

- **GitHub MCP not connected** — Report: "GitHub MCP not available. Check token and .mcp.json configuration."
- **No issues in v1.0 milestone** — Report: "No issues found in v1.0 milestone. Nothing to release."
- **Writer Agent fails** — Report with exact error message; halt pipeline.

### Non-Critical Failures (Continue with Flag)

- **Issue missing title** → Flagged in output: `[INSERT: title — issue #N missing]`
- **Issue body empty** → Flagged: `[INSERT: description — issue #N empty]`
- **Help topic generation fails for one feature** → Log in review report; continue with other features

---

## Comparison: Manual vs. Automated

| Aspect | Manual Workflow | AI-Automated Workflow |
|---|---|---|
| **Time** | 3–4 hours | ~2 minutes |
| **User input** | 6+ manual steps | 1 trigger command |
| **Data fetching** | Copy-paste from GitHub | Automatic via MCP |
| **Classification** | Manual mapping | Automatic rule-based |
| **Writing** | Human writer (30–45 min) | AI agent (1 min) |
| **Quality review** | Checklist audit (30 min) | Auto reviewer + report (30 sec) |
| **Fixes** | Manual edits | Auto-applied (20 sec) |
| **Consistency** | Variable (human-dependent) | Always follows rules |
| **Error rate** | Moderate (typos, missed items) | Low (rule-based) |
| **Scalability** | Difficult (linear time increase) | Easy (agents handle any size) |

---

## Configuration & Setup

### Prerequisites

1. **GitHub MCP Configured**
   - `.mcp.json` present in project root
   - `GITHUB_TOKEN` environment variable set
   - Token scopes: `repo`, `read:org`

2. **All Skills & Agents Ready**
   - `skills/*.md` files present
   - `agents/*.md` files present
   - `sample-data/expected-output-*.md` benchmarks present

3. **Output Directory**
   - `output/` directory exists (or will be created)

4. **Claude Code & MCP Support**
   - Using Claude API with MCP capability
   - Or Claude Code desktop/CLI with MCP enabled

### One-Time Setup

```bash
# Set GitHub token in environment
$env:GITHUB_TOKEN = "ghp_your_token_here"

# Verify .mcp.json exists
ls .mcp.json

# Test GitHub connection (optional)
gh repo list ShubhKN --json nameWithOwner
```

### Run Command

```bash
/project:generate-release-notes
```

---

## Monitoring & Observability

### Logs & Reporting

- **Orchestrator:** Reports each step (Initialize → Fetch → Classify → Delegate → Review → Fix → Output)
- **Sub-agents:** Report completion with file counts
- **Review Report:** `output/release-note-review-report.md` documents all findings

### Success Indicators

- All files present in `output/`
- Review report shows 0 High severity findings (after auto-fix)
- Release note structure matches benchmark
- Help topics linked and valid

### Troubleshooting

| Issue | Check | Resolution |
|---|---|---|
| GitHub MCP not connecting | `$env:GITHUB_TOKEN` set? | Set token: `$env:GITHUB_TOKEN = "ghp_..."` |
| No issues fetched | Milestone exists? | Verify ShubhKN/WealthWise has v1.0 milestone with issues |
| Files not created | `output/` directory exists? | Create: `mkdir output` |
| Help topic links broken | Slug names match? | Verify `#[number]-[slug]` format in both files |
| High severity findings | Content missing? | Check GitHub issue has title and description |

---

## Future Enhancements

- **Multi-version support** — Generate release notes for multiple milestones in parallel
- **Localization** — Auto-translate release notes to multiple languages
- **Analytics** — Track which features get most help topic views
- **Integration** — Auto-publish to help centre CMS
- **Webhooks** — Trigger on milestone completion automatically

---

## Architecture Principles

1. **Data comes from GitHub** — Never from local files
2. **Agents are stateless** — Each run is independent; no persistent state
3. **Quality is automatic** — Reviewer Agent runs on every output
4. **Errors are loud** — Missing data → explicit [INSERT: ...] flags
5. **No manual steps** — User triggers once; pipeline completes autonomously
6. **Rules are explicit** — All standards in skills files; no hidden logic
7. **Output is reproducible** — Same input → same output every time

---

## Related Documentation

- **Manual Workflow:** `workflow/workflow.md` (for when automation is unavailable)
- **Validation Plan:** `validation/validation-notes.md` (testing & QA)
- **Writing Standards:** `skills/release-note-writer-skill.md`
- **Reviewer Checklist:** `skills/release-note-reviewer-skill.md`
- **Branding Guide:** `skills/wealthwise-branding.md`
- **Classifier Rules:** `skills/github-issue-classifier.md`
- **Orchestrator Details:** `agents/release-note-orchestrator.md`
- **Trigger Command:** `commands/release-note-generation-command.md`
- **Troubleshooting:** `CLAUDE.md`

---

## Success Metrics

### First Release (v1.0)

- [ ] Pipeline completes in <3 minutes
- [ ] All output files generated (release note + 2+ help topics)
- [ ] Review report shows 0 High severity findings
- [ ] Stakeholder review passes with no rewrites needed
- [ ] Help topic links verified working
- [ ] Branding compliance 100%

### Ongoing

- [ ] Each release takes <5 minutes to generate
- [ ] Quality consistency maintained (same scoring across releases)
- [ ] Team productivity increases (fewer manual edits)
- [ ] Help centre traffic increases (improved user adoption)

---

**Document Version:** 2.0  
**Status:** Active  
**Last Updated:** 2026-07-03

For questions or issues, refer to the main `CLAUDE.md` or raise a GitHub Issue in ShubhKN/WealthWise.
