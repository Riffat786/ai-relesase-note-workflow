# WealthWise Branding System — Comprehensive Dependency Map

**Generated:** 2026-07-03  
**Branding Guide Source:** `skills/wealthwise-branding.md`  
**Scope:** All .md files in the WealthWise release note system

---

## Executive Summary

The WealthWise branding system is a **centralized, multi-layered specification** embedded across 12 files. Changes to the branding guide (`skills/wealthwise-branding.md`) require updates across multiple agent instructions, skill definitions, sample benchmarks, workflow documentation, and configuration files.

**Total files with branding dependencies:** 12  
**Total branding elements tracked:** 6 categories  
**Critical impact files:** 6 (agents + skills that generate output)

---

## 1. COLOR DEPENDENCIES

### Primary Colors — WW Green (#1D9E75, #0F6E56)

**Hardcoded references (must be updated if primary color changes):**

| File | Line | Type | Reference | Usage |
|------|------|------|-----------|-------|
| `skills/wealthwise-branding.md` | 65 | Definition | #1D9E75 | WW Green primary action colour |
| `skills/wealthwise-branding.md` | 67 | Definition | #0F6E56 | WW Dark Green hover state |
| `skills/wealthwise-branding.md` | 99 | Definition | #0F6E56 | WW Navy Text H1/H2 headings |
| `skills/wealthwise-branding.md` | 101 | Definition | #1D9E75 | WW Slate H3 headings |
| `skills/wealthwise-branding.md` | 113 | Definition | #1D9E75 | Success Green status colour |
| `skills/wealthwise-branding.md` | 227 | CSS rule | h1 color: #0F6E56 | H1 heading colour in HTML template |
| `skills/wealthwise-branding.md` | 241 | CSS rule | h2 color: #1D9E75 | H2 heading colour in HTML template |
| `skills/wealthwise-branding.md` | 243 | CSS rule | h2 border-bottom: #1D9E75 | H2 bottom border in HTML template |
| `skills/wealthwise-branding.md` | 321 | CSS rule | ul li::before background: #1D9E75 | Bullet point colour in HTML |
| `skills/release-note-writer-skill.md` | 83 | Reference | #1D9E75 | Writer role context on brand colours |
| `agents/help-topic-writer-agent.md` | 309 | CSS rule spec | border 4px solid #1D9E75 | .overview-box border in help topics |
| `agents/help-topic-writer-agent.md` | 327 | CSS rule spec | color #1D9E75 | .back-link a colour in help topics |
| `skills/release-note-reviewer-skill.md` | 209 | Validation rule | #1D9E75 | B3 check: H2 border-bottom accent |

**Impact Level:** CRITICAL - Primary action colour appears in 13 locations across generation rules and templates

---

### AI Accent Colors — WW Purple (#534AB7, #3C3489, #EEEDFE)

**Hardcoded references (must be updated if AI color changes):**

| File | Line | Type | Reference | Usage |
|------|------|------|-----------|-------|
| `skills/wealthwise-branding.md` | 81 | Definition | #534AB7 | WW Purple reserved for AI content |
| `skills/wealthwise-branding.md` | 83 | Definition | #3C3489 | WW Dark Purple AI text on purple backgrounds |
| `skills/wealthwise-branding.md` | 85 | Definition | #EEEDFE | WW Purple Tint AI background |
| `skills/wealthwise-branding.md` | 119 | Definition | #534AB7 | AI Purple status colour |
| `skills/wealthwise-branding.md` | 369 | CSS rule | .tag-ai background: #EEEDFE | AI tag background |
| `skills/wealthwise-branding.md` | 371 | CSS rule | .tag-ai color: #3C3489 | AI tag text colour |
| `skills/wealthwise-branding.md` | 561 | Rule | #534AB7, #EEEDFE | Diagram rules for AI elements |
| `skills/release-note-writer-skill.md` | 85 | Reference | #534AB7 | Writer role context on AI-reserved purple |
| `agents/release-note-writer-agent.md` | 301 | HTML spec | tag-ai class usage | AI tag application in release notes |
| `agents/help-topic-writer-agent.md` | 337 | HTML spec | tag-ai class usage | AI tag application in help topics |

**Impact Level:** CRITICAL - AI colour scheme reserved exclusively for AI features; misuse violates branding rule

---

### Supporting Colors — Neutrals, Status

**Hardcoded references:**

| File | Line | Type | Reference | Usage |
|------|------|------|-----------|-------|
| `skills/wealthwise-branding.md` | 69 | Definition | #E1F5EE | WW Green Tint success/active backgrounds |
| `skills/wealthwise-branding.md` | 71 | Definition | #FFFFFF | White page backgrounds |
| `skills/wealthwise-branding.md` | 103 | Definition | #E1F5EE | WW Page Tint backgrounds |
| `skills/wealthwise-branding.md` | 115 | Definition | #BA7517 | Caution Amber status colour |
| `skills/wealthwise-branding.md` | 117 | Definition | #A32D2D | Error Red status colour |
| `skills/wealthwise-branding.md` | 121 | Definition | #0C447C | Info Blue status colour |
| `skills/wealthwise-branding.md` | 131 | Definition | #1A1A1A | Text Dark body text |
| `skills/wealthwise-branding.md` | 133 | Definition | #5A6475 | Gray 1 muted text |
| `skills/wealthwise-branding.md` | 135 | Definition | #9AA3AF | Gray 2 placeholder text |
| `skills/wealthwise-branding.md` | 209 | CSS rule | body color: #1A1A1A | Body text colour |
| `skills/wealthwise-branding.md` | 211 | CSS rule | body background: #FFFFFF | Body background |
| `skills/wealthwise-branding.md` | 263 | CSS rule | h3 color: #5A6475 | H3 heading colour |
| `skills/wealthwise-branding.md` | 273 | CSS rule | p color: #1A1A1A | Paragraph text colour |
| `skills/wealthwise-branding.md` | 301 | CSS rule | ul li color: #1A1A1A | List item text colour |
| `skills/wealthwise-branding.md` | 329 | CSS rule | hr border: rgba(0,0,0,0.09) | Divider colour |
| `skills/wealthwise-branding.md` | 339 | CSS rule | .version color: #9AA3AF | Version text colour |
| `skills/wealthwise-branding.md` | 377 | CSS rule | .tag-security background: #FCEBEB | Security tag background |
| `skills/wealthwise-branding.md` | 379 | CSS rule | .tag-security color: #A32D2D | Security tag text colour |
| `skills/wealthwise-branding.md` | 385 | CSS rule | .tag-deprecated background: #FAEEDA | Deprecated tag background |
| `skills/wealthwise-branding.md` | 387 | CSS rule | .tag-deprecated color: #BA7517 | Deprecated tag text colour |
| `agents/help-topic-writer-agent.md` | 307 | CSS rule spec | color #9AA3AF | .meta-line colour |
| `agents/help-topic-writer-agent.md` | 325 | CSS rule spec | color #9AA3AF | .back-link colour |

**Impact Level:** HIGH - Supporting colours referenced across multiple CSS rules; changes affect visual hierarchy

---

## 2. FONT STACK DEPENDENCIES

### System Font Stack

**Central definition:**

| File | Lines | Type | Reference |
|------|-------|------|-----------|
| `skills/wealthwise-branding.md` | 180-182 | Definition + CSS | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` |

**References (no external fonts permitted):**

| File | Line | Type | Usage |
|------|------|------|-------|
| `skills/wealthwise-branding.md` | 173 | Rule | "WealthWise uses native OS font stack, no Google Fonts import required" |
| `skills/wealthwise-branding.md` | 203 | CSS rule | font-family in body rule |
| `skills/wealthwise-branding.md` | 211 | Rule context | "system font stack only" |
| `skills/release-note-writer-skill.md` | 87 | Reference | "system font stack" context |
| `agents/release-note-writer-agent.md` | 279 | Instruction | "system font stack only, per skills/wealthwise-branding.md" |
| `agents/help-topic-writer-agent.md` | 291 | Instruction | "system font stack only" |
| `agents/help-topic-writer-agent.md` | 315 | CSS rule spec | code font-family monospace |
| `skills/release-note-reviewer-skill.md` | 211 | Validation rule | B4 check: "No Google Fonts import" |
| `workflow/workflow.md` | 304 | Reference | System sans-serif stack example |
| `workflow/workflow.md` | 323 | CSS example | `-apple-system, Segoe UI, sans-serif` |
| `workflow/future-ai-workflow.md` | 124 | Reference | "Colour palette (#2D5A8C primary blue)" |
| `validation/validation-notes.md` | 144 | Validation rule | Font stack check |

**Impact Level:** MEDIUM - System font stack is fundamental; changes affect all generated HTML

---

### Typography Specifications

**Font weight and size rules:**

| File | Line | Type | Rule | Usage |
|------|------|------|------|-------|
| `skills/wealthwise-branding.md` | 161 | Spec | H1: 800 weight | Heading specification |
| `skills/wealthwise-branding.md` | 163 | Spec | H2: 700 weight | Heading specification |
| `skills/wealthwise-branding.md` | 165 | Spec | H3: 600 weight | Heading specification |
| `skills/wealthwise-branding.md` | 224 | CSS rule | h1: font-weight 800, font-size 1.6rem | H1 styling |
| `skills/wealthwise-branding.md` | 238 | CSS rule | h2: font-weight 700, font-size 1.3rem | H2 styling |
| `skills/wealthwise-branding.md` | 258 | CSS rule | h3: font-weight 600, font-size 1.02rem | H3 styling |

**Impact Level:** MEDIUM - Typography rules determine HTML heading output and readability

---

## 3. CSS TEMPLATE DEPENDENCIES

### HTML Release Note CSS Template

**Complete CSS specification embedded in:**
- `skills/wealthwise-branding.md` lines 199–459

**Referenced by (must embed entire template):**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `agents/release-note-writer-agent.md` | 283 | Instruction | "All CSS from skills/wealthwise-branding.md's HTML Release Note CSS Template, inline in a single style block. Do not modify or extend it" |
| `agents/help-topic-writer-agent.md` | 293 | Instruction | "All CSS from skills/wealthwise-branding.md inline in a single style block" |
| `skills/release-note-reviewer-skill.md` | 211 | Validation rule | B4: "No Google Fonts import" |
| `workflow/workflow.md` | 323 | Example | CSS example showing style block |

**CSS Classes defined in template:**

| Class | Definition Lines | Purpose |
|-------|------------------|---------|
| `body` | 201–219 | Page layout, font, colours |
| `h1` | 221–232 | H1 heading styling |
| `h2` | 235–255 | H2 heading styling with border-bottom |
| `h3` | 257–267 | H3 heading styling |
| `p` | 269–275 | Paragraph styling |
| `strong` | 277–283 | Bold text styling |
| `ul` | 285–293 | Unordered list styling |
| `ul li` | 295–303 | List item styling with bullet |
| `ul li::before` | 305–323 | Bullet point rendering (#1D9E75) |
| `hr` | 325–332 | Horizontal rule styling |
| `.version` | 335–343 | Version text styling |
| `.tag` | 345–365 | Base tag styling |
| `.tag-ai` | 367–372 | AI tag styling (#EEEDFE bg, #3C3489 text) |
| `.tag-security` | 375–380 | Security tag styling (#FCEBEB bg, #A32D2D text) |
| `.tag-deprecated` | 383–388 | Deprecated tag styling (#FAEEDA bg, #BA7517 text) |
| `.rn-header` | 391–409 | Release note header styling |
| `.rn-known-issue` | 429–441 | Known issues block styling |
| `.rn-footer` | 443–457 | Footer styling |

**Impact Level:** CRITICAL - Entire HTML template is fixed; any CSS changes break output consistency

---

### Help Topic CSS Extensions

**Additional CSS for help topics (defined in agent, not in branding file):**

| File | Lines | Class | Purpose |
|------|-------|-------|---------|
| `agents/help-topic-writer-agent.md` | 305–328 | `.ht-title` | H1 styling for help topics |
| `agents/help-topic-writer-agent.md` | 305–328 | `.meta-line` | Release metadata styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `.overview-box` | Overview section styling with left border |
| `agents/help-topic-writer-agent.md` | 305–328 | `ol li` | Ordered list item padding |
| `agents/help-topic-writer-agent.md` | 305–328 | `pre` | Code block styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `code` | Inline code styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `table` | Table styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `th` | Table header styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `td` | Table data cell styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `tr:nth-child(even) td` | Table row alternating |
| `agents/help-topic-writer-agent.md` | 305–328 | `.back-link` | Back link styling |
| `agents/help-topic-writer-agent.md` | 305–328 | `.back-link a` | Back link anchor styling |

**Impact Level:** MEDIUM - Help topic CSS builds on base template but includes topic-specific extensions

---

## 4. CATEGORY ICONS DEPENDENCIES

### Fixed Icon & Emoji Rules

**Definition:**

| File | Line | Category | Icon | Order |
|------|------|----------|------|-------|
| `skills/wealthwise-branding.md` | 523 | What's New | 🚀 | 1 |
| `skills/wealthwise-branding.md` | 525 | Enhancements | ✨ | 2 |
| `skills/wealthwise-branding.md` | 531 | Bug Fixes | 🐛 | 3 |
| `skills/wealthwise-branding.md` | 533 | Known Issues | — | 6 (footer, no emoji) |

**References (must use exact icons in this order):**

| File | Line | Usage |
|------|------|-------|
| `skills/release-note-writer-skill.md` | 252 | "## 🚀 What's New" in output format |
| `skills/release-note-writer-skill.md` | 313 | "## ✨ Enhancements" in output format |
| `skills/release-note-writer-skill.md` | 341 | "## 🐛 Bug Fixes" in output format |
| `agents/release-note-writer-agent.md` | 238 | "h2 (with the 🚀 icon)" instruction |
| `agents/release-note-writer-agent.md` | 305 | "h2 (with the ✨ icon)" instruction |
| `agents/release-note-writer-agent.md` | 309 | "h2 (with the 🐛 icon)" instruction |
| `agents/release-note-writer-agent.md` | 312 | "Known Issues as `h2` (no icon)" instruction |
| `skills/release-note-reviewer-skill.md` | 213 | B5 check: "Category icons match fixed set and order" |
| `workflow/workflow.md` | 212 | "## 🚀 What's New" in manual process |
| `workflow/workflow.md` | 218 | "## ✨ Enhancements" in manual process |
| `workflow/workflow.md` | 224 | "## 🐛 Bug Fixes" in manual process |
| `workflow/workflow.md` | 230 | "## ⚠️ Known Issues" reference (note: different emoji) |
| `workflow/workflow.md` | 304 | Category icons table |
| `workflow/future-ai-workflow.md` | 260 | "Four sections in order: 🚀 ✨ 🐛 ⚠️" reference |
| `validation/validation-notes.md` | 143 | Validation rule for icons |

**Note:** There is an **inconsistency**: `workflow/workflow.md` uses ⚠️ for Known Issues, but `skills/wealthwise-branding.md` specifies no emoji for Known Issues. Known Issues section should not have emoji per branding guide.

**Impact Level:** HIGH - Icons appear in every release note output; consistency is visual brand identifier

---

## 5. TAG/BADGE RULES DEPENDENCIES

### .tag-ai Badge (AI Content Only)

**Definition and rules:**

| File | Lines | Type | Specification |
|------|-------|------|---|
| `skills/wealthwise-branding.md` | 537 | Rule | "Any list item describing AI-driven functionality must include inline `<span class="tag tag-ai">AI</span>`" |
| `skills/wealthwise-branding.md` | 367–372 | CSS | `.tag-ai { background: #EEEDFE; color: #3C3489; }` |
| `skills/wealthwise-branding.md` | 89 | Rule | "If a release note item does not describe AI-driven functionality, it must NEVER use the purple family" |

**References requiring tag-ai implementation:**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `skills/release-note-writer-skill.md` | 227 | HTML instruction | Append `<span class="tag tag-ai">AI</span>` after feature name |
| `skills/release-note-writer-skill.md` | 228 | Markdown instruction | Append `(AI)` after bolded feature name |
| `agents/release-note-writer-agent.md` | 301 | Implementation | Use `<span class="tag tag-ai">AI</span>` in HTML output |
| `agents/release-note-writer-agent.md` | 167 | Implementation | Append `(AI)` to HTML for AI-driven enhancements |
| `agents/help-topic-writer-agent.md` | 337 | Implementation | `<span class="tag tag-ai">AI</span>` appended if is_ai_feature |
| `sample-data/expected-output-1.md` | 61 | Example | Shows `<span class="tag tag-ai">AI</span>` in use |
| `sample-data/expected-output-2.md` | 31 | Example | Shows AI tag in help topic |
| `skills/release-note-reviewer-skill.md` | 111 | Validation rule | RN-C7: "Every AI-driven feature mention carries the `tag-ai` badge" |
| `skills/release-note-reviewer-skill.md` | 215 | Validation rule | B6: "AI-tagged items use `tag-ai` styling (WW Purple family), never WW Green" |
| `skills/github-issue-classifier.md` | 128 | Classification rule | "If label contains `component: ai-advisor` or `ai-*` → Apply `tag-ai` badge" |
| `workflow/workflow.md` | 141 | Example | Shows `<span class="tag tag-ai">AI</span>` syntax |
| `workflow/workflow.md` | 346 | Example | HTML rendering example with tag-ai |
| `workflow/future-ai-workflow.md` | 240 | Example | Shows tag in output example |
| `CLAUDE.md` | 123 | Reference | "if item needs security/deprecated emphasis, flag inline with `tag-security` or `tag-deprecated` badge" |
| `CLAUDE.md` | 247 | Reference | "`tag-ai` applied to every AI-driven feature mention" |
| `validation/validation-notes.md` | 82 | Validation rule | "Every AI-driven feature has `<span class="tag tag-ai">AI</span>` badge" |
| `validation/validation-notes.md` | 147 | Validation rule | "AI tag: `.tag.tag-ai` with light background, blue text" |

**Impact Level:** CRITICAL - AI tag is visual signal to users that content is AI-generated; missing tags break trust

---

### .tag-security & .tag-deprecated Badges (Optional)

**Definition:**

| File | Lines | Type | Specification |
|------|-------|------|---|
| `skills/wealthwise-branding.md` | 375–380 | CSS | `.tag-security { background: #FCEBEB; color: #A32D2D; }` |
| `skills/wealthwise-branding.md` | 383–388 | CSS | `.tag-deprecated { background: #FAEEDA; color: #BA7517; }` |

**References:**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `CLAUDE.md` | 121–124 | Rule | "No separate Security or Deprecated sections; if item needs that emphasis, flag inline with `tag-security` or `tag-deprecated` badge" |

**Impact Level:** MEDIUM - Optional badges for security/deprecated features; less frequently used

---

## 6. HTML STRUCTURE DEPENDENCIES

### Required Page Header

**Definition:**

```html
<div class="rn-header">
  <span class="product-name">WealthWise</span>
  <span class="header-rule">|</span>
  <span class="header-rule">Help Centre</span>
</div>
```

**Location in branding:** `skills/wealthwise-branding.md` lines 467–485

**References (all output HTML must include this header):**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `skills/wealthwise-branding.md` | 471 | Requirement | "Every HTML release note must begin with this header" |
| `agents/release-note-writer-agent.md` | 289 | Instruction | "Required header block at top of body, exactly as specified" |
| `agents/help-topic-writer-agent.md` | 331 | Instruction | "Required header block at top of body" |
| `skills/release-note-reviewer-skill.md` | 205 | Validation rule | B1: "`rn-header` div present with product name and Help Centre label" |

**Impact Level:** CRITICAL - Header is required on every HTML output

---

### Required Copyright Footer

**Definition:**

```html
<footer class="rn-footer">
  &copy; 2026 WealthWise. All rights reserved.
</footer>
```

**Location in branding:** `skills/wealthwise-branding.md` lines 497–507

**References (all output HTML must include this footer):**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `skills/wealthwise-branding.md` | 497 | Requirement | "Every HTML release note must end with" this footer |
| `skills/release-note-writer-skill.md` | 419 | Product name rule | "The WealthWise product name inside body prose (it appears in the page header and footer)" |
| `agents/release-note-writer-agent.md` | 319 | Instruction | "Required footer exactly as specified" |
| `agents/help-topic-writer-agent.md` | 357 | Instruction | "Required footer exactly as specified" |
| `skills/release-note-reviewer-skill.md` | 207 | Validation rule | B2: "`rn-footer` div present with exact copyright line" |
| `workflow/workflow.md` | 389 | Reference | "Footer with copyright present" |
| `validation/validation-notes.md` | 146 | Validation rule | "Required: © 2026 WealthWise. All rights reserved." |

**Impact Level:** CRITICAL - Footer is required on every HTML output; copyright year (2026) is embedded

---

### Page Title Format

**Rule:** `[Section heading] — WealthWise Help Centre`

**References:**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `skills/wealthwise-branding.md` | 651 | Specification | "`<title>` set to: `[Section heading] — WealthWise Help Centre`" |
| `agents/release-note-writer-agent.md` | 277 | Title rule | "Title element: `Release [release_version] — WealthWise Help Centre`" |
| `agents/help-topic-writer-agent.md` | 289 | Title rule | "Title element: `[feature_name] — WealthWise Help Centre`" |

**Impact Level:** MEDIUM - Page titles affect browser tab and SEO

---

### Known Issues Container

**Rule:** Known Issues must be wrapped in `.rn-known-issue` div, not plain bullets

**Definition:**

| File | Lines | Type | Specification |
|------|-------|------|---|
| `skills/wealthwise-branding.md` | 429–441 | CSS | `.rn-known-issue { background: #FAEEDA; border: 1px solid #BA7517; border-radius: 12px; padding: 1rem 1.25rem; margin: 1rem 0; }` |
| `skills/wealthwise-branding.md` | 539 | Rule | "Known Issues must be wrapped in a `<div class="rn-known-issue">` block rather than a plain bullet" |

**References:**

| File | Line | Type | Reference |
|------|------|------|-----------|
| `agents/release-note-writer-agent.md` | 313 | Instruction | "Known Issues as `h2` (no icon), each entry wrapped in `div.rn-known-issue` block" |
| `skills/release-note-reviewer-skill.md` | 217 | Validation rule | B7: "Known Issues wrapped in `.rn-known-issue`, not a plain bullet" |
| `sample-data/expected-output-1.md` | 85 | Example | Shows structure without the styling applied (markdown) |

**Impact Level:** MEDIUM - Affects visual distinction of known issues

---

## 7. STRUCTURAL RULES & CONSTRAINTS

### Section Order (Fixed)

**Rule:** Four sections in fixed order; omit any section with zero entries

**Definition:**
- `skills/release-note-writer-skill.md` line 511

**References:**

| File | Line | Reference |
|------|------|-----------|
| `skills/release-note-writer-skill.md` | 511 | "Generate categories in the fixed order: What's New, Enhancements, Bug Fixes, Known Issues. Omit any category with zero entries." |
| `agents/release-note-writer-agent.md` | 260 | "Sections as `##` headings with the fixed emoji" |
| `skills/release-note-reviewer-skill.md` | 72 | RN-S2: "Categories appear in the fixed order" |
| `workflow/workflow.md` | 235 | Shows fixed section order |
| `validation/validation-notes.md` | 74 | Validation rule for section order |

**Impact Level:** HIGH - Section order is standardized across all output

---

### Bug Fixes Table (Exactly Three Columns)

**Rule:** Bug ID | Description | Fix / Solution (no additional columns)

**Definition:**
- `skills/release-note-writer-skill.md` lines 335–365

**References:**

| File | Line | Reference |
|------|------|-----------|
| `agents/release-note-writer-agent.md` | 309 | "HTML `table` with exactly three columns: Bug ID, Description, Fix / Solution" |
| `skills/release-note-reviewer-skill.md` | 83 | RN-S7: "Bug Fixes rendered as table with exactly three columns" |
| `skills/release-note-reviewer-skill.md` | 483 | "A Bug Fixes table with more than three columns is a High severity RN-S7 failure" |
| `CLAUDE.md` | 188 | "WealthWise standard is exactly Bug ID, Description, Fix / Solution" |
| `workflow/workflow.md` | 169 | Shows exact three-column format |
| `validation/validation-notes.md` | 79 | Validation rule for table structure |

**Impact Level:** HIGH - Strict column count enforced during review

---

### File Naming Convention

**Rule:** `release-note-[version]-[short-slug].html` and `.md`

**Definition:**
- `skills/wealthwise-branding.md` lines 572–640

**Examples from branding:**
- `release-note-1-0-ai-advisor-launch.html`
- `release-note-1-0-investment-tracking.html`
- `release-note-1-1-budget-rounding-fix.html`

**References:**

| File | Line | Reference |
|------|------|-----------|
| `agents/release-note-writer-agent.md` | 227 | "File: `output/release-note-[version_slug]-whats-new.md`" |
| `agents/release-note-writer-agent.md` | 265 | "File: `output/release-note-[version_slug]-whats-new.html`" |
| `agents/help-topic-writer-agent.md` | 79 | "output_html: help-topic-[slug].html" |
| `agents/help-topic-writer-agent.md` | 81 | "output_md: help-topic-[slug].md" |
| `skills/release-note-reviewer-skill.md` | 221 | B9: "File naming matches the convention" |
| `workflow/workflow.md` | 429 | Shows file naming format |
| `validation/validation-notes.md` | 200 | Validation rule for naming |

**Impact Level:** MEDIUM - File naming is standardized for version control and publication

---

## 8. CROSS-FILE CONSISTENCY CHECKS

### Files That Must Stay in Sync

**Critical sync points:**

| Change Scenario | Files Affected | Impact |
|---|---|---|
| Add new color to palette | `skills/wealthwise-branding.md` → `agents/help-topic-writer-agent.md`, `agents/release-note-writer-agent.md` | New CSS rules must be implemented in agents |
| Change primary color (#1D9E75) | `skills/wealthwise-branding.md` → 13 locations across agents, skills, workflow, validation | Entire visual identity changes; regenerate all samples |
| Modify CSS template | `skills/wealthwise-branding.md` → `agents/release-note-writer-agent.md`, `agents/help-topic-writer-agent.md` | HTML output appearance changes; regenerate benchmarks |
| Add new category icon | `skills/wealthwise-branding.md` → `skills/release-note-writer-skill.md`, `agents/release-note-writer-agent.md`, `skills/release-note-reviewer-skill.md` | New section type added; update classification rules |
| Change AI tag styling | `skills/wealthwise-branding.md` → `agents/release-note-writer-agent.md`, `agents/help-topic-writer-agent.md` | AI badge appearance changes; all AI features re-rendered |
| Modify font stack | `skills/wealthwise-branding.md` → `agents/release-note-writer-agent.md`, `agents/help-topic-writer-agent.md` | All typography regenerated; affect readability |
| Update copyright year (2026) | `skills/wealthwise-branding.md` → Footer CSS, sample outputs | Current year must update in all generated files |

---

### Sample Benchmark Updates

**Files that embed branding output examples (must be regenerated if branding changes):**

| File | Lines | Type | Content |
|------|-------|------|---------|
| `sample-data/expected-output-1.md` | 57–121 | HTML/Markdown | Release note structure benchmark with full branding applied |
| `sample-data/expected-output-2.md` | 1–146 | HTML/Markdown | Help topic structure benchmark with full branding applied |

**When to update:**
- Any color change in `skills/wealthwise-branding.md`
- Any CSS rule modification
- Any section icon change
- Any tag styling change

---

## 9. VALIDATION CHECKLIST FOR BRANDING CHANGES

### Before updating any branding element:

**Step 1: Identify all files that reference the element**
- Use `grep` to search codebase for color hex, CSS class name, emoji, or rule text
- Check this dependency map for all references

**Step 2: Update the primary definition**
- Update `skills/wealthwise-branding.md` first
- Update the definition table (color palette, typography, icons, etc.)
- Update corresponding CSS rule(s)

**Step 3: Update all agent instructions**
- `agents/release-note-writer-agent.md`
- `agents/help-topic-writer-agent.md`
- `agents/release-note-orchestrator.md`

**Step 4: Update skill references**
- `skills/release-note-writer-skill.md`
- `skills/release-note-reviewer-skill.md`

**Step 5: Update workflow documentation**
- `workflow/workflow.md`
- `workflow/future-ai-workflow.md`

**Step 6: Update validation rules**
- `validation/validation-notes.md`
- `CLAUDE.md`

**Step 7: Update sample benchmarks**
- `sample-data/expected-output-1.md`
- `sample-data/expected-output-2.md`

**Step 8: Test end-to-end**
- Generate sample release note
- Verify all outputs use new branding
- Check HTML rendering in browser
- Confirm no hardcoded values remain

---

## 10. BRANDING ELEMENT IMPACT MATRIX

| Element | Criticality | # Files | Hardcoded? | Test Required? |
|---------|-------------|---------|-----------|---|
| Primary Green (#1D9E75) | CRITICAL | 13 | Yes | Yes |
| AI Purple (#534AB7) | CRITICAL | 10 | Yes | Yes |
| Font Stack | HIGH | 12 | No | Yes |
| Category Icons (🚀✨🐛) | HIGH | 14 | Yes | Yes |
| HTML Header Block | CRITICAL | 4 | Yes | Yes |
| Copyright Footer | CRITICAL | 5 | Yes | Yes |
| CSS Template | CRITICAL | Embedded | Yes | Yes |
| .tag-ai Class | CRITICAL | 15 | Yes | Yes |
| Section Order | HIGH | 5 | No | Yes |
| Bug Fixes Table Format | HIGH | 5 | No | Yes |
| Typography (weights/sizes) | MEDIUM | 6 | No | No |
| Supporting Colors | MEDIUM | 22 | Yes | No |
| .tag-security/.tag-deprecated | MEDIUM | 3 | Yes | No |
| File Naming Convention | MEDIUM | 6 | No | No |

---

## Summary & Recommendations

### Current State
- Branding system is **highly interconnected** across 12 files
- **13 hardcoded color references** (especially #1D9E75) require synchronization
- **CSS template is embedded** in multiple agent instructions, creating duplication
- **Sample benchmarks must be manually updated** when branding changes

### Risk Areas
1. **Color inconsistency** — Primary green used in 13 places; single typo breaks all outputs
2. **Icon emoji in workflow docs** — `workflow/workflow.md` uses ⚠️ for Known Issues; branding guide specifies no emoji
3. **CSS duplication** — Help topic CSS rules live in agent, not centralized in branding file
4. **Sample benchmark staleness** — If branding changes, benchmarks become outdated and validators fail

### Recommendations
1. **Create a branding constants file** — Extract all hex colors, emoji, and class names to single source of truth
2. **Centralize CSS templates** — Move all help topic CSS rules into `skills/wealthwise-branding.md` and reference from agents
3. **Fix icon inconsistency** — Update `workflow/workflow.md` to remove ⚠️ and match branding guide (no emoji for Known Issues)
4. **Add automated validation** — Create a script to verify all branding references match the primary definition
5. **Document sync points** — Add comments in all files that embed branding rules, linking back to `skills/wealthwise-branding.md`

---

**Document Generated:** 2026-07-03  
**Status:** Complete  
**Next Review:** Upon any branding guide update
