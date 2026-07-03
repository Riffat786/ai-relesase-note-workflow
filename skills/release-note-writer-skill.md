---
name: jira-release-notes
description: 'Generate professional release notes from JIRA project stories. Queries a JIRA project for all completed stories (status = Done), synthesizes their business value from descriptions and acceptance criteria, and creates formatted markdown release notes with version tables, introductory paragraphs, and business-focused enhancement descriptions in Microsoft Manual of Style. Use this skill whenever you need to produce release notes, documentation, feature summaries, or changelog documentation from JIRA data — even if the user does not explicitly ask for a skill or does not mention JIRA by name. Triggers include: generate release notes, create release documentation, extract features from JIRA, build release documentation, document completed features, prepare release announcement, or any request for professional documentation of completed JIRA stories.'
compatibility:
  - 'Requires MCP: Atlassian (JIRA) with active authentication'
  - Requires Claude to synthesize business value from technical requirements
---

## Overview

This skill automates professional release notes generation by querying JIRA and transforming raw story data into polished, business-focused documentation. The skill asks you for the **JIRA project key**, queries the project for all Done stories, extracts the business value from each story's description and acceptance criteria, and generates a formatted markdown document ready for distribution.

## What the skill does

1. **Asks for project key and version** — You provide the JIRA project key (e.g., KAN, SAN) and the release version (e.g., 26.2, v1.0)
2. **Queries JIRA** via MCP for all Done stories in that project using JQL: `project = [KEY] AND status = Done AND type = Story`
3. **Extracts key data** from each story: summary, description, acceptance criteria, components, priority, labels
4. **Synthesizes business value** — Reads the description and acceptance criteria, then writes clear, benefit-focused 1–3 sentence summaries using Microsoft Manual of Style (clear, concise, action-oriented)
5. **Formats as markdown** — Creates a professional release notes document with:
   - Title: `# Release Notes: [Project Name] [Version]`
   - Version information table (SaaS/On Premises availability)
   - Introductory paragraph
   - Enhancements section grouped by business value
6. **Outputs to markdown file** — Auto-names based on project key and version (e.g., `release-notes-KAN-26.2.md`)

## How to use it

**Trigger scenarios:**
- "Generate release notes for the KAN project version 26.2"
- "Create release notes from completed JIRA stories in SAN"
- "Extract enhancements from our JIRA project and build a release notes document"
- "Build release documentation for project XYZ"
- "Create professional release notes from JIRA"

**What you provide when the skill asks:**
- **Project key** (required): The JIRA project identifier (e.g., KAN, SAN, BHII)
- **Version** (required): The release version for the notes (e.g., 26.2, v2.1, Q3-2026)

**What you'll receive:**
- A markdown file with professional release notes including:
  - Title with project name and version
  - Version information table (SaaS/On Premises availability)
  - Introductory paragraph explaining what's new
  - Enhancements section with business-focused 1–3 sentence descriptions
  - File saved with naming convention: `release-notes-[PROJECT_KEY]-[VERSION].md`

## The JIRA query

The skill uses a dynamic JQL query based on the project key you provide:

```jql
project = [PROJECT_KEY] AND status = Done AND type = Story
```

**Example:** If you provide project key "KAN", the query becomes:
```jql
project = KAN AND status = Done AND type = Story
```

Only Done stories are included. Incomplete work, bugs, and tasks are excluded.

## Writing approach: Business value, not technical criteria

The skill transforms technical acceptance criteria into user-facing benefit statements.

### What NOT to include:
- Acceptance criteria verbatim ("CR1: Must support X, CR2: Must handle Y")
- Technical implementation details ("Uses API endpoint /v3/items")
- Internal process descriptions ("Requires 3 rounds of code review")

### What TO include:
- **User benefit** — What does the user gain?
- **Problem solved** — What pain point does this address?
- **Context** — Who benefits and why?
- **Clear, accessible language** — Readable by both technical and non-technical stakeholders

### Example transformation:

**Raw JIRA story:**
```
Summary: Add export-to-CSV feature in dashboard
Description: Users requested ability to export metrics data for external analysis
Acceptance Criteria:
  - CSV file includes all visible columns
  - File downloads with timestamp in name
  - Works for data sets up to 100k rows
  - Includes headers and proper escaping
```

**Generated release note:**
```markdown
### Export metrics to CSV
Export dashboard metrics directly to CSV format for use in external tools and analysis. Files include all visible columns with a timestamp in the filename, supporting datasets up to 100k rows and streamlining data sharing across teams.
```

Notice: The description captures **what users can now do** and **why it matters**, not the checklist of requirements.

## Release notes document structure

Follow the structure as present in the [release-notes-template.md](release-notes-template.md) file present at the root of this folder. Don't drift away from the structure.

## Document format and style

**Key formatting rules:**
- **Title:** `# Release Notes: [Project Name] [Version]`
- **Intro paragraph:** "Review the [Project Name] [Version] enhancements and improvements. The following enhancements provide new capabilities and improve the user experience."
- **Version table:** Indicates SaaS and On Premises availability (use ✓ and -)
- **Enhancements section:** `## Enhancements`
- **Each enhancement:** `### [Enhancement Title]` (H3 heading)
- **Description length:** 1–3 sentences, benefit-focused
- **Tone:** Professional, benefit-driven, Microsoft Manual of Style
- **File naming:** `release-notes-[PROJECT_KEY]-[VERSION].md`

## Process workflow

1. **Accept project key and version** from user
2. **Query JIRA** for all Done stories in the project using JQL
3. **Parse story data** — Extract summary, description, acceptance criteria, components, labels
4. **Synthesize business value** for each story (1–3 sentences, business-focused)
5. **Group enhancements** by logical business categories if applicable
6. **Create markdown document** following the format above
7. **Save to file** with auto-generated name
8. **Display file path** and preview so user can review and download

## Notes

- The skill requires active Atlassian MCP authentication. If your JIRA instance is not connected, you'll be prompted to authenticate.
- Empty acceptance criteria fields will be handled gracefully — the skill uses the summary and description alone.
- If a story has no description, the skill uses a concise synthesis of the summary and acceptance criteria.
- Version information (SaaS/On Premises) defaults to "SaaS: ✓, On Premises: -" unless specifically marked in JIRA labels or description.
