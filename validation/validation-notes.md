# Validation Notes — WealthWise Release Note System

**Document Status:** Active Validation Framework  
**Last Updated:** 2026-07-03  
**Scope:** Quality assurance, output structure, content compliance, and system integration testing

---

## Purpose

This document records validation findings, quality checkpoints, and test results across the WealthWise release note generation system. It serves as the living record of what has been tested, what passed, what failed, and what remediation was applied.

---

## Validation Areas

### 1. GitHub MCP Integration

**Objective:** Verify that the GitHub MCP correctly fetches issues from ShubhKN/WealthWise v1.0 milestone.

| Checkpoint | Status | Notes |
|---|---|---|
| MCP server connection | ✓ Ready | GitHub MCP configured in `.mcp.json`; requires `GITHUB_TOKEN` env var |
| Issue query execution | ✓ Ready | Query format: `Repository: ShubhKN/WealthWise, Milestone: v1.0` |
| Required fields retrieved | ✓ Ready | Fetches: issue number, title, body, labels, state, milestone, timestamps |
| Field parsing accuracy | ⏳ Pending | Verify all label extraction and state classification work correctly |
| Edge case: Issues without titles | ⏳ Pending | Verify flagging: `[INSERT: feature name — GitHub issue #N has no title]` |
| Edge case: Issues without descriptions | ⏳ Pending | Verify fallback flag applied when body is empty |
| Milestone resolution | ⏳ Pending | Confirm v1.0 milestone resolves to release_version = "1.0" |

**Validation Plan:**
- Run live fetch against ShubhKN/WealthWise repository
- Inspect retrieved issues for completeness
- Confirm all label types are present and correctly formatted
- Test graceful handling of missing/malformed fields

---

### 2. Issue Classification

**Objective:** Verify that each GitHub issue is correctly mapped to a release note category.

**Classification Rules:**
- `type: feature` → What's New
- `type: enhancement` → Enhancements
- `type: bug` + closed state (no `status: known-issue`) → Bug Fixes
- `type: bug` + `status: known-issue` → Known Issues
- `type: bug` + open state → Skip (unresolved bugs)
- Tracking issues → Skip

| Checkpoint | Status | Notes |
|---|---|---|
| Feature detection | ⏳ Pending | Test: identify all `type: feature` issues correctly |
| Enhancement detection | ⏳ Pending | Test: identify all `type: enhancement` issues correctly |
| Bug fix detection | ⏳ Pending | Test: identify closed bugs without `status: known-issue` |
| Known issue detection | ⏳ Pending | Test: identify bugs marked with `status: known-issue` |
| Open bug filtering | ⏳ Pending | Test: correctly skip open (unresolved) bugs |
| AI feature tagging | ⏳ Pending | Test: detect `component: ai-advisor` label and apply `tag-ai` badge |
| Duplicate detection | ⏳ Pending | Test: no issue appears in multiple categories |

**Test Data:**
- Sample What's New feature (from sample-data/sample-1-input.md)
- Sample Bug Fix (from sample-data/sample-2-input.md)

---

### 3. Release Note Output Structure

**Objective:** Verify that generated release notes match the expected structure benchmark.

**Expected Output:** `sample-data/expected-output-1.md`

| Section | Status | Validation Rule |
|---|---|---|
| Title | ⏳ Pending | Format: "WealthWise — Release [version] ([Month] [Year])" |
| Summary paragraph | ⏳ Pending | 2–3 sentences covering all categories with counts (e.g., "delivers one new AI-powered..." |
| What's New section | ⏳ Pending | Heading: "🚀 What's New"; entries have three-part narrative (Previously → Now → Value) |
| Enhancements section | ⏳ Pending | Heading: "✨ Enhancements"; entries follow three-part narrative |
| Bug Fixes section | ⏳ Pending | Heading: "🐛 Bug Fixes"; table format with Bug ID, Description, Fix/Solution columns |
| Known Issues section | ⏳ Pending | Heading: "⚠️ Known Issues"; present only if issues exist |
| No extra sections | ⏳ Pending | Only four categories; no Security, Deprecated, or other sections |
| AI tags applied | ⏳ Pending | Every AI-driven feature has `<span class="tag tag-ai">AI</span>` badge |
| Help topic links | ⏳ Pending | Every What's New entry links to its help topic (HTML version) |

---

### 4. Help Topic Output Structure

**Objective:** Verify that generated help topics match the expected structure benchmark.

**Expected Output:** `sample-data/expected-output-2.md`

| Element | Status | Validation Rule |
|---|---|---|
| File naming | ⏳ Pending | Format: `help-topic-[slug].html` and `help-topic-[slug].md` |
| Slug generation | ⏳ Pending | Format: `#[issue-number]-[lowercase-hyphenated-title-max-40-chars]` |
| Page title | ⏳ Pending | Format: "[Feature Name] — WealthWise Help" |
| Breadcrumb | ⏳ Pending | Format: "WealthWise Help > Release Notes > [Feature Name]" |
| Help content | ⏳ Pending | 2–3 paragraphs explaining feature; past-to-present narrative |
| Step-by-step (if applicable) | ⏳ Pending | Numbered steps if feature has a workflow |
| Related links back to release note | ⏳ Pending | Link to release note with text "Back to Release Notes" |
| Branding elements | ⏳ Pending | WealthWise logo, colour palette, system font stack |
| AI tags | ⏳ Pending | Apply `tag-ai` if feature is AI-driven |

---

### 5. Writing Standards Compliance

**Objective:** Verify that all content follows WealthWise writing standards.

**Writing Rules** (from `skills/release-note-writer-skill.md`):

| Rule | Status | Validation |
|---|---|---|
| Second person ("you") | ⏳ Pending | All What's New and Enhancement entries use "you" or "your" |
| Active voice | ⏳ Pending | Avoid passive constructions; prioritize active voice |
| Three-part narrative | ⏳ Pending | What's New/Enhancements: (Previously → Now → Value) |
| Bug fixes: past/present tense | ⏳ Pending | Description in past tense; Fix/Solution in present/simple tense |
| No internal IDs | ⏳ Pending | GitHub issue numbers appear ONLY in Bug Fixes table; never in prose |
| No severity labels | ⏳ Pending | No P1, Critical, Blocker, or severity ratings anywhere |
| No marketing language | ⏳ Pending | Avoid hype (amazing, groundbreaking, revolutionary) |
| Sentence case titles | ⏳ Pending | Titles like "AI Insight banner..." not "AI Insight Banner..." |
| Currency notation | ⏳ Pending | Indian Rupee: ₹ symbol; amounts like ₹1,00,000 |
| Clarity and brevity | ⏳ Pending | No jargon; accessible to finance users |

**Test Documents:**
- `sample-data/sample-1-input.md` — What's New feature
- `sample-data/sample-2-input.md` — Bug fix

---

### 6. Branding Compliance

**Objective:** Verify that HTML output applies WealthWise brand standards.

**Brand Rules** (from `skills/wealthwise-branding.md`):

| Element | Status | Validation |
|---|---|---|
| Product name | ⏳ Pending | Every page title contains "WealthWise" |
| Logo placement | ⏳ Pending | Logo in header; version in release notes title |
| Colour palette | ⏳ Pending | Primary: #1D9E75 (WW Green), #0F6E56 (WW Dark Green); AI Accents: #534AB7 (WW Purple), #3C3489 (WW Dark Purple); Supporting: #E1F5EE (Green Tint), #EEEDFE (Purple Tint) |
| Category icons | ⏳ Pending | What's New: 🚀; Enhancements: ✨; Bug Fixes: 🐛; Known Issues: — |
| Font stack | ⏳ Pending | System fonts: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif |
| HTML structure | ⏳ Pending | Valid semantic HTML; proper heading hierarchy (h1 → h2 → h3) |
| Footer | ⏳ Pending | Required: "© 2026 WealthWise. All rights reserved." |
| Tag styling | ⏳ Pending | Tag classes: .tag-ai (background #EEEDFE, text #3C3489); .tag-security (background #FCEBEB, text #A32D2D); .tag-deprecated (background #FAEEDA, text #BA7517) |
| Typography weights | ⏳ Pending | H1: 800 weight; H2: 700 weight; H3: 600 weight (per branding guide lines 161-165) |
| Responsive layout | ⏳ Pending | Mobile-friendly; readable on phone, tablet, desktop |
| CSS embedded | ⏳ Pending | All styles in `<style>` block; no external stylesheets |

---

### 7. Hyperlink Integrity

**Objective:** Verify that all cross-references between release notes and help topics are correct.

| Check | Status | Validation |
|---|---|---|
| Help topic links present | ⏳ Pending | Every What's New entry in release note links to its help topic |
| Link target exists | ⏳ Pending | Referenced help topic file exists (HTML and Markdown versions) |
| Reverse links | ⏳ Pending | Every help topic links back to release note |
| URL format (HTML) | ⏳ Pending | Format: `help-topic-[slug].html` |
| Link text | ⏳ Pending | Descriptive (not "here" or "click here") |
| Markdown links | ⏳ Pending | Format: `[text](help-topic-[slug].md)` for Markdown version |
| No broken anchors | ⏳ Pending | Check for 404 or missing pages |

---

### 8. Auto-Fix Application

**Objective:** Verify that the orchestrator correctly identifies and fixes High and Medium severity issues.

**Review Report:** `output/release-note-review-report.md`

| Scenario | Status | Validation |
|---|---|---|
| High severity flagged | ⏳ Pending | Missing title/description/fix flags correctly recorded |
| Medium severity flagged | ⏳ Pending | Style violations, tense inconsistencies flagged |
| Auto-fix applied | ⏳ Pending | Orchestrator corrects findings and re-runs reviewer |
| Low severity logged only | ⏳ Pending | Logged in report but not auto-fixed (human review needed) |
| Recursion prevention | ⏳ Pending | Auto-fix doesn't create infinite loop; max 2 iterations |
| Report accuracy | ⏳ Pending | All findings correctly documented with before/after |

---

### 9. File Output Generation

**Objective:** Verify that all output files are created with correct naming and format.

**Expected Output Files:**

| File | Format | Status | Notes |
|---|---|---|---|
| `release-note-[version]-whats-new.html` | HTML | ⏳ Pending | Branded, linked help topics |
| `release-note-[version]-whats-new.md` | Markdown | ⏳ Pending | Version control source |
| `help-topic-[slug].html` | HTML | ⏳ Pending | One per What's New feature |
| `help-topic-[slug].md` | Markdown | ⏳ Pending | One per What's New feature |
| `release-note-review-report.md` | Markdown | ⏳ Pending | QA findings and auto-fix log |

**No JSON output** — WealthWise uses only HTML and Markdown per `skills/wealthwise-branding.md`.

| Validation | Status |
|---|---|
| All files created in `output/` | ⏳ Pending |
| File permissions readable | ⏳ Pending |
| No intermediate temp files left | ⏳ Pending |
| Naming conventions followed | ⏳ Pending |

---

### 10. End-to-End Pipeline Execution

**Objective:** Verify the entire pipeline runs without user intervention.

**Test Scenario:** Run `/project:generate-release-notes` command (from `commands/release-note-generation-command.md`)

| Step | Expected Behavior | Status |
|---|---|---|
| 1. Fetch GitHub issues | 4–6 issues retrieved from v1.0 milestone | ⏳ Pending |
| 2. Classify issues | All issues sorted into categories | ⏳ Pending |
| 3. Run writer agent | Release note and help topics generated | ⏳ Pending |
| 4. Run reviewer agent | Quality report produced | ⏳ Pending |
| 5. Apply auto-fixes | High/Medium findings corrected | ⏳ Pending |
| 6. Output to files | All files written to `output/` | ⏳ Pending |
| 7. No user prompts | Pipeline runs without requiring input | ⏳ Pending |
| 8. Completion report | Orchestrator summarizes results | ⏳ Pending |

---

## Known Issues & Blockers

| Issue | Impact | Resolution Status |
|---|---|---|
| (None recorded yet) | — | — |

---

## Test Data & Samples

**Current Test Fixtures:**
- `sample-data/sample-1-input.md` — What's New feature sample
- `sample-data/sample-2-input.md` — Bug fix sample
- `sample-data/expected-output-1.md` — Release notes structure benchmark
- `sample-data/expected-output-2.md` — Help topic structure benchmark

**Live Data:**
- Source: GitHub repository [ShubhKN/WealthWise](https://github.com/ShubhKN/WealthWise)
- Milestone: v1.0

---

## Validation Checklist (Pre-Release)

- [ ] GitHub MCP integration tested and working
- [ ] All issue classifications verified (4+ issues per category where present)
- [ ] Release note structure matches expected-output-1.md
- [ ] Help topic structure matches expected-output-2.md
- [ ] Writing standards applied consistently
- [ ] Branding compliance verified (HTML colors, fonts, layout)
- [ ] Hyperlinks verified (no broken links)
- [ ] Auto-fix correctly applied to findings
- [ ] All output files generated and readable
- [ ] End-to-end pipeline runs without user input
- [ ] Review report documents all findings clearly
- [ ] Sample output ready for stakeholder review

---

## Next Steps

1. **Execute test run** using `/project:generate-release-notes` command
2. **Record findings** in this document by updating checkpoints
3. **Resolve blockers** before full release
4. **Obtain stakeholder sign-off** on output quality and branding
5. **Archive this validation report** after release

---

**Questions or Blockers?**  
Refer to `CLAUDE.md` for troubleshooting. Raise a GitHub Issue in ShubhKN/WealthWise if blocked or uncertain.
