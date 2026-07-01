# Release Note Orchestration Log — 2026-07-01

## Pipeline Status

**Current Phase:** Step 2 - Jira Data Fetch (IN PROGRESS)
**Started:** 2026-07-01 23:15:00 UTC
**Status:** Two agents fetching issue data from KAN project

---

## Step 1: Skills and Benchmarks — COMPLETE

All required files have been loaded:
- [x] skills/release-note-writer-skill.md — MSTP writing rules, output formats
- [x] skills/branding-style-guide.md — HTML/CSS template, colour palette, typography
- [x] skills/release-note-reviewer-skill.md — QA checklist (22-point), 7-criterion style audit
- [x] sample-data/expected-output-1.md — Release notes structure benchmark
- [x] sample-data/expected-output-2.md — Help topic structure benchmark

**Key Rules in Memory:**
- MSTP standards: Active voice, second person, no em dashes, serial commas, sentence-case headings
- Brand colours: GMP Navy #1B2A4A, GMP Green #2ECC71, GMP Dark Green #27AE60
- Typography: Inter font (weights 400, 600, 700)
- Release notes structure: Overview, New Features (with help topic links), Enhancements, Bug Fixes (table), Known Issues, Technical Notes
- Help topic structure: Overview (What it does, Why it matters, Key benefits), Workflow, API Details, Back-link to release notes
- QA: 22-point content checklist, 7-criterion style audit, hyperlink integrity, JSON validity, branding compliance

---

## Step 2: Jira Data Fetch — IN PROGRESS

**Status:** Two agents working in parallel
- Agent 1 (afb0ff29d6f6eb714): Initial fetch request
- Agent 2 (aba60eac2b979b71c): Resume/retrieve request

**JQL Query:**
```
project = KAN ORDER BY cf[10019] ASC
```

**Target Fields per Issue:**
- key, summary, description, issuetype.name, status.name, labels
- fixVersions, priority.name, components, assignee.displayName
- resolution.name, resolution.description, created, updated
- comments (all), customfield_steps_to_reproduce, customfield_workaround
- remoteLinks (Confluence pages)

**Expected Output:**
- Total issue count
- All issue objects in JSON format

---

## Step 3: Variable Resolution — PENDING

Will resolve when Jira data arrives:

| Variable | Source | Status |
|----------|--------|--------|
| product_name | Constant: "GlobalMail Pro" | READY |
| release_version | issue.fixVersions[0].name or fallback to YYYY.MM | PENDING |
| version_slug | release_version with dots→hyphens | PENDING |
| release_date | Today: 2026-07-01 | READY |
| release_month_year | Today: July 2026 | READY |
| [Feature Name] | issue.summary (sentence case) | PENDING |
| [slug] | lowercase(key)-hyphenated(summary) | PENDING |
| [Bug ID] | issue.key | PENDING |
| [Bug Summary] | issue.summary | PENDING |
| [Severity] | Map priority → High/Medium/Low | PENDING |
| [Affected Area] | components[0] or first label | PENDING |
| [Bug Description] | First paragraph of description | PENDING |
| [Steps to Reproduce] | customfield_steps_to_reproduce or extract from description | PENDING |
| [Fix Applied] | resolution.description or first comment starting with "Fix:" | PENDING |
| [User Impact] | Synthesised from description + fix | PENDING |
| [Workaround] | customfield_workaround or comment starting with "Workaround:" | PENDING |
| [Confluence Reference] | remoteLinks with atlassian.net/wiki or /confluence | PENDING |
| [API endpoint] | Parsed from description/comments | PENDING |
| [HTTP method] | GET/POST/PUT/DELETE from description/comments | PENDING |
| [Parameters] | Table from description or Confluence | PENDING |
| [Example Response] | JSON from description or Confluence, or inferred | PENDING |

---

## Step 4: Issue Classification — PENDING

Will classify when Jira data arrives using:
- New Features: Story, Feature, New Feature issue types
- Enhancements: Task, Enhancement, Improvement, Sub-task
- Bug Fixes: Bug
- Known Issues: Any type with label "known-issue"

Expected Arrays:
- new_features[] — 0+ issues
- enhancements[] — 0+ issues
- bug_fixes[] — 0+ issues
- known_issues[] — 0+ issues

---

## Step 5: Help Topic Slug Generation — PENDING

Will generate slugs for each new feature:
```
slug = lowercase(key) + "-" + lowercase_hyphenated(summary, max 40 chars)
Example: KAN-42 "Smart route optimisation engine" → "kan-42-smart-route-optimisation-engine"
```

**help_topic_map:**
```json
{
  "KAN-X": { "slug": "kan-x-...", "filename": "help-topic-kan-x-....html" },
  ...
}
```

---

## Step 6: Writer Agent Delegation — PENDING

Will invoke agents/release-note-writer-agent.md with:
- new_features[], enhancements[], bug_fixes[], known_issues[] (classified)
- release_version, release_date, release_month_year
- All resolved variables from Variable Resolution Map
- help_topic_map for link generation
- Skills: writer-skill, branding-style-guide
- Benchmark: expected-output-1.md

**Expected Outputs:**
- output/release-notes-[version_slug].html
- output/release-notes-[version_slug].md
- output/release-notes-[version_slug].json

---

## Step 7: Help Topic Writer Delegation — PENDING

For each issue in new_features[]:
- Invoke agents/help-topic-writer-agent.md
- Pass: feature issue object, slug, filename
- Skills: writer-skill, branding-style-guide
- Benchmark: expected-output-2.md

**Expected Outputs per Feature:**
- output/help-topic-[slug].html
- output/help-topic-[slug].md

---

## Step 8: Reviewer Agent Delegation — PENDING

Invoke agents/release-note-reviewer-agent.md with:
- All release notes files (MD, HTML, JSON)
- All help topic files (MD, HTML)
- All Jira issue objects
- Skills: reviewer-skill, branding-style-guide
- Benchmarks: expected-output-1.md, expected-output-2.md

**Expected Output:**
- output/release-note-review-report.md (with findings ranked by severity)

---

## Step 9: Auto-fix Application — PENDING

Will read review report and apply corrections:
- For every High severity finding: apply corrected text
- For every Medium severity finding: apply corrected text
- Log each fix: `FIXED [ID] in [filename] — [description]`
- Write corrected versions back to output files

---

## Step 10: Pipeline Summary — PENDING

Will generate final PIPELINE COMPLETE summary with:
- Release version, date, issue counts
- All output files listed
- Review result (PASS / REVISED)
- Number of high/medium/low fixes applied

---

## Notes

- All content must trace to Jira issues — no invented content
- Jira IDs appear only in Bug Fixes table, nowhere else
- OUTPUT_DIRECTORY: C:\Users\LENOVO\Documents\GitHub\ai-relesase-note-workflow\output\
- All relative links use help-topic-[slug].html format
- JSON must be valid, no trailing commas, no comments

---
