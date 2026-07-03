# Classic Release Note Workflow — Manual Generation

**Version:** 1.0  
**Last Updated:** 2026-07-03  
**Audience:** Technical writers and product managers generating release notes without AI agents or MCPs

---

## Overview

This document describes the **traditional, manual workflow** for generating WealthWise release notes without automated agents or MCPs. This process relies on human effort to fetch issue data, classify content, write narrative, and apply quality standards.

**Use this workflow when:**
- AI agents or MCPs are unavailable
- Quick manual updates are needed (e.g., one hot-fix release)
- You prefer human control over every step
- Integrations are not configured

**For automated generation, see:** `workflow/future-ai-workflow.md`

---

## Workflow Phases

### Phase 1: Gather Data

#### 1a. Fetch Issues from GitHub

**Manual Step:** Visit GitHub and collect all issues in the release milestone.

1. Navigate to: [ShubhKN/WealthWise Issues](https://github.com/ShubhKN/WealthWise/issues)
2. Filter by milestone: `v1.0`
3. Export or note down the following fields for each issue:
   - Issue number (e.g., #1, #5, #12)
   - Title
   - Description (full body)
   - Labels (type, component, priority, status)
   - State (open or closed)
   - Created/updated/closed dates

**Expected output:** Spreadsheet or document with 4–6 issues

**Tools:**
- GitHub web UI (no token required for public repos)
- Optional: GitHub CLI `gh issue list --milestone v1.0 --repo ShubhKN/WealthWise`

---

#### 1b. Create a Working Document

Create a local working file (e.g., `release-notes-v1.0-draft.md`) with this structure:

```markdown
# WealthWise Release Notes — v1.0 (Draft)

**Release Version:** 1.0
**Release Date:** [TODAY'S DATE, e.g., July 3, 2026]
**Status:** In Progress

## Collected Issues

### What's New
- [ ] Issue #1: [Title]
- [ ] Issue #3: [Title]

### Enhancements
- [ ] Issue #2: [Title]

### Bug Fixes
- [ ] Issue #5: [Title]
- [ ] Issue #7: [Title]

### Known Issues
- [ ] Issue #4: [Title]

## Writing Work
[Will be filled in Phase 2]

## Review Checklist
[Will be filled in Phase 3]
```

---

### Phase 2: Classify & Write

#### 2a. Classify Each Issue

For each collected issue, assign a release note category using these rules:

| GitHub Label | State | Category |
|---|---|---|
| `type: feature` | — | **What's New** |
| `type: enhancement` | — | **Enhancements** |
| `type: bug` | Closed, no `status: known-issue` | **Bug Fixes** |
| `type: bug` | — | **Known Issues** (if marked `status: known-issue`) |
| `type: bug` | Open | **Skip** (unresolved, not in release) |
| Tracking issue | — | **Skip** (not customer-facing) |

**Action:** Update your working document with the correct category for each issue.

---

#### 2b. Write "What's New" Entries

For each **What's New** issue (type: feature), write a 3-part narrative:

**Pattern:**
```
### [Feature Name] [AI tag if applicable]

Previously, [customer pain point before this feature].

Now, [what the feature does, how it solves the problem].

[Outcome/value — what the customer gains].
```

**Example from sample-data:**
```
### AI Insight banner with contextual spending alerts 🏷️ AI

Previously, you had no proactive visibility into your spending trends
until you manually opened the Transactions or Budget screens, and by the
time you noticed an overspend, you had already gone past your budget.

Now, the Dashboard shows a persistent AI Insight banner that reads your
current month's spending in real time and surfaces a contextual alert
with a specific recommendation before you exceed your budget.

You catch overspending while there is still time to change course,
instead of finding out after the fact.
```

**Writing Rules:**
- Use **second person** ("you", "your")
- Use **active voice** (avoid "is shown" → use "shows")
- **No internal GitHub IDs** in the body text
- **No severity or priority labels**
- **No marketing hype** (avoid "amazing", "revolutionary")
- If AI-driven, include the tag: `🏷️ AI` or `<span class="tag tag-ai">AI</span>` for HTML
- **Sentence case** for titles (not Title Case)

---

#### 2c. Write "Enhancements" Entries

Similar to What's New, but for non-feature improvements:

**Pattern:**
```
### [Enhancement Name]

Previously, [previous behavior].

Now, [improved behavior].

[Benefit to user].
```

**Apply same writing rules as What's New.**

---

#### 2d. Create "Bug Fixes" Table

For each **Bug Fix** issue, create a table row:

| Bug ID | Description | Fix / Solution |
|---|---|---|
| #5 | Category totals display incorrect rounding above ₹1,00,000 | Budget totals now match exact transaction sums. |
| #7 | Transaction category is not saved when switching between payment methods | Payment method switching now preserves selected category. |

**Rules:**
- **Bug ID column:** Only place GitHub issue numbers appear (format: `#[number]`)
- **Description column:** Past tense (what was broken)
- **Fix/Solution column:** Present or simple past (what was done)
- **No severity labels** (Critical, P1, etc.)
- **No internal jargon** (backend terms, database names, etc.)

---

#### 2e. List "Known Issues"

For each **Known Issue** (type: bug + status: known-issue):

```
### [Known Issue Title]

[Description in present/ongoing tense]

**Status:** [ongoing investigation, workaround available, etc.]
```

---

### Phase 3: Structure & Format

#### 3a. Create the Release Note Header

Add a title and introductory paragraph:

```markdown
# WealthWise — Release 1.0 (July 2026)

Release 1.0 delivers [number] new AI-powered capabilities,
[number] enhancements to user experience, resolves [number]
critical bugs, and documents [number] known issues.

---

## 🚀 What's New

[What's New entries from Phase 2b]

---

## ✨ Enhancements

[Enhancements entries from Phase 2c]

---

## 🐛 Bug Fixes

[Bug Fixes table from Phase 2d]

---

## Known Issues

[Known Issues from Phase 2e]
```

**Rules:**
- **Always use these four sections in this order** (only include Known Issues if there are any)
- **Section icons:** What's New: 🚀, Enhancements: ✨, Bug Fixes: 🐛, Known Issues: ⚠️
- **No extra sections** (no Security, Deprecated, Compatibility Notes, etc. — if needed, flag inline within the relevant section)
- **Release title format:** "WealthWise — Release [version] ([Month] [Year])"

---

#### 3b. Generate Help Topics (One per What's New Feature)

For each **What's New** entry, create a standalone help topic document:

**File naming:** `help-topic-[slug].md`  
**Slug format:** `#[issue-number]-[lowercase-hyphenated-title-max-40-chars]`

Example: `help-topic-#1-ai-insight-banner-spending-alerts.md`

**Template:**

```markdown
# AI Insight Banner with Contextual Spending Alerts — WealthWise Help

**Breadcrumb:** WealthWise Help > Release Notes > AI Insight Banner

## Overview

The AI Insight banner is a new dashboard widget that monitors your
spending in real time and alerts you when you're approaching your
budget limit.

## How It Works

1. **Real-time monitoring** — The banner reads your transactions as
   they post throughout the month.

2. **Budget comparison** — It compares your current spending against
   your set budget limits.

3. **Proactive alerts** — When you approach 80% of your budget, the
   banner displays a warning with a recommendation.

4. **Take action** — You can adjust your spending, increase your
   budget, or dismiss the alert.

## Related

[Back to Release Notes](release-note-1-0-whats-new.md)
```

**Rules:**
- **2–3 paragraphs** explaining the feature
- **Optional numbered steps** if the feature has a workflow
- **Link back** to main release note at the bottom
- **Same writing standards** as release note (second person, active voice)
- **Create both Markdown and HTML versions** (see Phase 4b)

---

### Phase 4: Apply Branding & Generate HTML

#### 4a. Brand Standards

Ensure your content follows **WealthWise brand guidelines** from `skills/wealthwise-branding.md`:

| Element | Standard | Example |
|---|---|---|
| Product name | Always "WealthWise" | ✓ "WealthWise Release 1.0" |
| Colours | Primary green: #1D9E75, Secondary: #0F6E56, Light: #E1F5EE, Purple: #534AB7, Dark Purple: #3C3489, Light Purple: #EEEDFE | Use in headers, accents |
| Font | System sans-serif stack | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` |
| Category icons | Specific emoji per section | 🚀 ✨ 🐛 ⚠️ |
| Copyright | Required footer | © 2026 WealthWise. All rights reserved. |
| AI tag (if applicable) | Light blue background, blue text | `<span class="tag tag-ai">AI</span>` |

---

#### 4b. Convert to HTML

Create an HTML version of your release note with:

1. **Semantic structure:**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <title>WealthWise Release Notes — Version 1.0</title>
     <style>
       /* Branding styles */
       body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
       h1 { font-weight: 800; }
       h2 { font-weight: 700; }
       h3 { font-weight: 600; }
       .header { background-color: #1D9E75; color: white; padding: 20px; }
       .section { margin: 20px 0; }
       .tag { display: inline-block; background: #E1F5EE; color: #1D9E75; padding: 2px 8px; border-radius: 3px; }
       .tag-ai { background: #E1F5EE; color: #1D9E75; }
       .tag-security { background: #FFE0E0; color: #C63447; }
       .tag-deprecated { background: #F3E5F5; color: #6A1B9A; }
     </style>
   </head>
   <body>
     <div class="header">
       <h1>WealthWise Release 1.0</h1>
       <p>July 2026</p>
     </div>
     <!-- Content sections -->
     <footer style="background-color: #f5f5f5; padding: 20px; text-align: center; margin-top: 40px; border-top: 1px solid #ddd;">
       <p>&copy; 2026 WealthWise. All rights reserved.</p>
     </footer>
   </body>
   </html>
   ```

2. **Linked help topics:**
   ```html
   <h3>
     <a href="help-topic-#1-ai-insight-banner-spending-alerts.html">
       AI Insight Banner with Contextual Spending Alerts
     </a>
     <span class="tag tag-ai">AI</span>
   </h3>
   ```

3. **Responsive layout** — Mobile-friendly, readable on all screen sizes

4. **Footer with copyright** — Required in every HTML file

---

### Phase 5: Quality Review

#### 5a. Self-Review Checklist

Before publishing, verify your release note against this checklist:

**Content:**
- [ ] All four categories (What's New, Enhancements, Bug Fixes, Known Issues) present
- [ ] Every What's New entry has three-part narrative (Previously → Now → Value)
- [ ] Second person ("you") used throughout
- [ ] Active voice used (not passive)
- [ ] No internal GitHub issue numbers in body text (only in Bug Fixes table)
- [ ] No severity/priority labels visible
- [ ] AI tag applied to AI-driven features
- [ ] No marketing hype language

**Structure:**
- [ ] Title format: "WealthWise — Release 1.0 (Month Year)"
- [ ] Intro paragraph summarizes all categories with counts
- [ ] Four sections in correct order with correct icons
- [ ] Help topic files created for each What's New feature
- [ ] Bug Fixes table has exactly 3 columns: Bug ID, Description, Fix/Solution

**Links & Navigation:**
- [ ] Every What's New entry links to its help topic
- [ ] Every help topic links back to release note
- [ ] No broken links

**Brand Compliance:**
- [ ] WealthWise logo/branding present
- [ ] Correct color palette (#1D9E75 primary, #0F6E56 secondary, #E1F5EE, #534AB7, #3C3489, #EEEDFE)
- [ ] System font stack used (includes Roboto)
- [ ] Copyright footer present
- [ ] Mobile-friendly layout (if HTML)

**Formatting:**
- [ ] Markdown or HTML is valid and renders correctly
- [ ] No syntax errors or broken formatting
- [ ] Consistent date format (e.g., July 3, 2026)

---

#### 5b. Address Issues

For any items that don't pass:

1. **Content issues** → Rewrite the affected section (Phase 2)
2. **Structure issues** → Reorganize sections (Phase 3)
3. **Link issues** → Update filenames and references
4. **Brand issues** → Re-apply branding standards (Phase 4)

Repeat the checklist until all items pass.

---

#### 5c. Get Stakeholder Approval

Circulate your draft to:
- Product manager (confirm feature descriptions)
- Design team (verify branding)
- Customer support (confirm clarity)

Incorporate feedback and repeat quality review.

---

### Phase 6: Publish

#### 6a. Finalize Filenames

Save all files with standard naming:

```
output/
  ├── release-note-1-0-whats-new.md       (Markdown version)
  ├── release-note-1-0-whats-new.html     (HTML version)
  ├── help-topic-#1-ai-insight-banner.md  (Help topic Markdown)
  ├── help-topic-#1-ai-insight-banner.html (Help topic HTML)
  ├── help-topic-#3-[name].md
  ├── help-topic-#3-[name].html
  └── ...
```

Format: `release-note-[VERSION_WITH_HYPHENS]-whats-new.[FORMAT]`

---

#### 6b. Create a Manifest

Document what was published:

```markdown
# Release 1.0 Publication Manifest

**Published:** July 3, 2026

## Files Published

- release-note-1-0-whats-new.md
- release-note-1-0-whats-new.html
- help-topic-#1-ai-insight-banner-spending-alerts.md
- help-topic-#1-ai-insight-banner-spending-alerts.html
- [... one help topic per What's New feature]

## Contents Summary

- **What's New:** 2 features
- **Enhancements:** 1 improvement
- **Bug Fixes:** 2 issues resolved
- **Known Issues:** 0 issues

## Linked Resources

- GitHub milestone: https://github.com/ShubhKN/WealthWise/milestone/1
- Source issues: #1, #2, #3, #5, #7
```

---

#### 6c. Distribute

- Email to stakeholders with links
- Post to internal wiki/knowledge base
- Share with customer support team
- Add link to GitHub releases page

---

## Estimated Time & Effort

| Phase | Time | Effort |
|---|---|---|
| 1. Gather Data | 15 minutes | Low (copy-paste from GitHub) |
| 2. Classify & Write | 1–2 hours | Medium (creative writing) |
| 3. Structure & Format | 30 minutes | Low (follow template) |
| 4. Apply Branding & HTML | 45 minutes | Medium (CSS, template) |
| 5. Quality Review | 30 minutes | Low (checklist verification) |
| 6. Publish | 15 minutes | Low (file copy, distribution) |
| **Total** | **3–4 hours** | **Medium** |

---

## Tools & Resources

| Tool | Purpose | Link |
|---|---|---|
| GitHub Issues | Fetch source data | https://github.com/ShubhKN/WealthWise/issues |
| GitHub CLI | Optional: automated fetch | `gh issue list --milestone v1.0` |
| Text Editor | Write and format | VS Code, Markdown Editor, etc. |
| Markdown Preview | Verify formatting | GitHub preview, VS Code preview |
| HTML Validator | Verify HTML syntax | https://validator.w3.org |
| Browser | Test HTML rendering | Firefox, Chrome, Safari |

---

## Common Pitfalls & Solutions

| Pitfall | Why It Happens | Solution |
|---|---|---|
| Severity labels in output (P1, Critical) | Copy-paste from Jira/GitHub | Remove before publishing — WealthWise never shows severity |
| GitHub issue numbers in prose | Forgetting the "ID column only" rule | Review: issue numbers should appear ONLY in Bug Fixes table |
| Passive voice ("is implemented") | Natural writing habit | Use active voice: "We implemented" or feature-focused: "The feature enables" |
| Missing help topics | Forgetting to create one per What's New | Create help topic immediately after writing each What's New entry |
| Broken links between release note and help topics | Typos in slugs or filenames | Double-check all slugs match between What's New links and help topic filenames |
| Inconsistent formatting | Manual copy-paste from different sources | Use the provided templates for consistency |
| Missing AI tags | Forgot feature is AI-driven | Review all feature titles and descriptions; check if "AI Advisor" is mentioned |

---

## Example: Complete Workflow Run

**Scenario:** Release v1.0 with 1 What's New feature, 1 enhancement, 2 bug fixes

**Time breakdown:**
1. **Gather Data (10 min):** Copied 4 issues from GitHub
2. **Classify & Write (90 min):**
   - What's New entry: 20 min (three-part narrative)
   - Enhancement entry: 15 min
   - Bug Fixes table: 10 min
   - Help topic: 25 min
   - Review and revise: 20 min
3. **Structure (20 min):** Assembled sections, added intro
4. **Branding & HTML (40 min):** Created HTML version with CSS, tested responsive
5. **Quality Review (20 min):** Checklist review, minor fixes
6. **Publish (10 min):** Saved files, created manifest

**Total: ~3 hours 30 minutes**

---

## Transition to Automated Workflow

Once GitHub MCP and AI agents are configured, you can automate this entire workflow using the `/project:generate-release-notes` command (see `workflow/future-ai-workflow.md`).

**Benefits of automation:**
- Reduces manual effort from 3–4 hours to ~15 minutes
- Eliminates classification and writing errors
- Ensures consistency across releases
- Allows rapid iteration on multiple releases

---

## Next Steps

1. **For manual generation:** Follow this workflow for your next release
2. **For automation:** See `workflow/future-ai-workflow.md`
3. **For questions:** Check `CLAUDE.md` troubleshooting section

---

**Document Version:** 1.0  
**Last Reviewed:** 2026-07-03  
**Status:** Active
