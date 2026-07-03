# Release Note Review Report

**Files reviewed:**
- output/release-note-1-0-whats-new.md
- output/release-note-1-0-whats-new.html
- output/help-topic-#1-ai-financial-advisor-chat.md
- output/help-topic-#1-ai-financial-advisor-chat.html
- output/help-topic-#2-investment-portfolio-tracking.md
- output/help-topic-#2-investment-portfolio-tracking.html

**Generated:** 2026-07-03T14:35:00Z

**Reviewer:** WealthWise Release Note Reviewer Skill v1.0

**Jira project:** WealthWiseReleaseDemo (WW)

---

## Release Notes Review

### Structure checks (RN-S1 to RN-S9)

| ID | Check | Result | Severity |
|---|---|---|---|
| RN-S1 | Only What's New, Enhancements, Bug Fixes, Known Issues | PASS | — |
| RN-S2 | Categories in fixed order | PASS | — |
| RN-S3 | Zero-count categories omitted | PASS | — |
| RN-S4 | Overview line present with counts | PASS | — |
| RN-S5 | What's New entries use three-part narrative | PASS | — |
| RN-S6 | What's New entries have "Learn more" links | PASS | — |
| RN-S7 | Bug Fixes table has exactly 3 columns | PASS | — |
| RN-S8 | Known Issues use bullet or .rn-known-issue styling | PASS | — |
| RN-S9 | Closing line present | PASS | — |

**RN-S Score: 9/9**

### Content accuracy (RN-C1 to RN-C8)

| ID | Check | Result | Severity |
|---|---|---|---|
| RN-C1 | No invented content | PASS | — |
| RN-C2 | No internal IDs in prose (Bug ID column excepted) | PASS | — |
| RN-C3 | No backend/API/infrastructure detail | PASS | — |
| RN-C4 | No marketing language | PASS | — |
| RN-C5 | No severity/priority labels (P1, Critical, Blocker, etc.) | **FAIL** | **High** |
| RN-C6 | All classified issues represented | PASS | — |
| RN-C7 | Every AI-driven feature tagged with (AI) or tag-ai | **FAIL** | **Medium** |
| RN-C8 | Only AI-driven features tagged | PASS | — |

**RN-C Score: 6/8**

### Writing standards (W1-W10)

| ID | Criterion | Result | Severity |
|---|---|---|---|
| W1 | Second person ("you" not "users") | **FAIL** | **Medium** |
| W2 | Active voice | PASS | — |
| W3 | Consistent em dash use | PASS | — |
| W4 | Sentence-case headings | PASS | — |
| W5 | Present tense for current behavior | PASS | — |
| W6 | Numbers 0-9 spelled out, 10+ numerals | **FAIL** | **Medium** |
| W7 | Currency formatted correctly | PASS | — |
| W8 | No hedging language | PASS | — |
| W9 | No product name in body prose | PASS | — |
| W10 | Sentences under 25 words | **FAIL** | **High** |

**W Score: 7/10**

### Branding compliance (B1-B9) — HTML files only

| ID | Check | Result | Severity |
|---|---|---|---|
| B1 | rn-header div present | PASS | — |
| B2 | rn-footer with copyright | PASS | — |
| B3 | H2 uses WW Green border (#1D9E75) | PASS | — |
| B4 | No Google Fonts import | PASS | — |
| B5 | Category icons match set (🚀, ✨, 🐛) | PASS | — |
| B6 | AI-tagged items use tag-ai purple, not WW Green | PASS | — |
| B7 | Known Issues in .rn-known-issue div | PASS | — |
| B8 | Self-contained HTML (no external CSS/JS) | PASS | — |
| B9 | File naming convention | **FAIL** | **Medium** |

**B Score: 8/9**

### Hyperlink integrity (H1-H3)

| ID | Check | Result | Severity |
|---|---|---|---|
| H1 | What's New entries link to help topics | PASS | — |
| H2 | Help topics link back to release notes | PASS | — |
| H3 | Filenames match actual output files | PASS | — |

**H Score: 3/3**

### Issues requiring correction

**Issue RN-C5 — Severity label usage (Severity: High)**

File: release-note-1-0-whats-new.md (line 3) and release-note-1-0-whats-new.html (line 204)

Original: "resolves three critical bugs affecting budget display and onboarding"

Corrected: "resolves three bugs affecting budget display and onboarding"

Rationale: WealthWise prohibits severity labels ("Critical", "P1", "Blocker", etc.) anywhere in customer-facing output per CLAUDE.md constraint. Remove the descriptor.

---

**Issue RN-C7 — Missing AI tags (Severity: Medium)**

File: release-note-1-0-whats-new.md (line 23-26) and release-note-1-0-whats-new.html (line 225-237)

Feature #2 describes AI-driven functionality ("the AI alerts you to rebalance") but lacks the required AI tag.

Original heading (MD):
### Investment portfolio tracking

Original heading (HTML):
<h3>Investment portfolio tracking</h3>

Corrected heading (MD):
### Investment portfolio tracking (AI)

Corrected heading (HTML):
<h3>Investment portfolio tracking <span class="tag tag-ai">AI</span></h3>

Rationale: Per RN-C7 and branding guide, every mention of AI-driven functionality must carry the tag-ai badge. This feature includes AI-driven rebalancing alerts.

---

**Issue RN-C7 — Missing AI tag on enhancement (Severity: Medium)**

File: release-note-1-0-whats-new.md (line 40) and release-note-1-0-whats-new.html (line 244)

Enhancement #1 describes "AI-generated rebalancing recommendations" but lacks the required AI tag.

Original (MD):
- Get AI-generated rebalancing recommendations when any budget category exceeds its limit, with a one-click Auto-rebalance action that reallocates from underspent categories (Pro and Family only; exact overage and source categories displayed clearly)

Original (HTML):
<li>Get AI-generated rebalancing recommendations when any budget category exceeds its limit, with a one-click Auto-rebalance action that reallocates from underspent categories (Pro and Family only; exact overage and source categories displayed clearly)</li>

Corrected (MD):
- Get AI-generated rebalancing recommendations when any budget category exceeds its limit, with a one-click Auto-rebalance action that reallocates from underspent categories (Pro and Family only; exact overage and source categories displayed clearly) (AI)

Corrected (HTML):
<li>Get AI-generated rebalancing recommendations when any budget category exceeds its limit, with a one-click Auto-rebalance action that reallocates from underspent categories (Pro and Family only; exact overage and source categories displayed clearly) <span class="tag tag-ai">AI</span></li>

Rationale: Per RN-C7, all AI-driven features must carry the tag-ai badge inline after the feature name/description.

---

**Issue W1 — Second person in bug description (Severity: Medium)**

File: release-note-1-0-whats-new.md (line 51) and release-note-1-0-whats-new.html (line 273)

Original: "When users navigated backward from Step 4 to Step 3 during onboarding, slider values reset to defaults."

Corrected: "When you navigated backward from Step 4 to Step 3 during onboarding, slider values reset to defaults."

Rationale: Per W1 writing standard, use second person ("you") throughout, not "users" or "customers".

---

**Issue W6 — Number formatting (Severity: Medium)**

File: release-note-1-0-whats-new.md (line 57, in Known Issues) and release-note-1-0-whats-new.html (line 285, in Known Issues)

Original: "up to 2 hours out of date"

Corrected: "up to two hours out of date"

Rationale: Per W6, numbers 0-9 must be spelled out; numerals are used only for 10 and above.

---

**Issue W10 — Sentence length (Severity: High)**

File: release-note-1-0-whats-new.md (line 3) and release-note-1-0-whats-new.html (line 204)

Original: "Release 1.0 introduces an AI Financial Advisor chat interface and investment portfolio tracking, adds AI-assisted budget rebalancing and transaction categorization review, resolves three critical bugs affecting budget display and onboarding, and documents one known issue with brokerage data sync latency." (41 words)

Corrected: "Release 1.0 introduces two new AI-powered features: an AI Financial Advisor chat interface and investment portfolio tracking. It adds AI-assisted budget rebalancing and transaction categorization review, resolves three bugs affecting budget display and onboarding, and documents one known issue with brokerage data sync latency." (48 words in two sentences, first 12 words, second 36 words)

Better corrected: "Release 1.0 brings two AI-powered features for personalized financial guidance: AI Financial Advisor chat and Investment Portfolio Tracking. New enhancements add AI-assisted budget rebalancing and transaction categorization. Three bug fixes address budget display, notification duplication, and onboarding navigation. One known issue documents potential latency in brokerage data sync."

Rationale: Per W10, sentences must not exceed 25 words. The 41-word overview paragraph must be split into shorter sentences.

---

**Issue W10 — Sentence length in What's New (Severity: High)**

File: release-note-1-0-whats-new.md (line 25) and release-note-1-0-whats-new.html (line 227)

Original: "Previously, your investment holdings across multiple accounts lived in separate apps and statements, with no way to see your total invested value, performance, or asset allocation in one place." (29 words)

Corrected: "Previously, your investment holdings lived in separate apps and statements with no unified view. You could not see your total value, performance, or asset allocation in one place."

Rationale: Per W10, split into sentences under 25 words each.

---

**Issue W10 — Sentence length in What's New benefit list (Severity: High)**

File: release-note-1-0-whats-new.md (line 29) and release-note-1-0-whats-new.html (line 227)

Original: "You see portfolio-level metrics (total value, total invested, total return %, XIRR) and a holdings table showing each investment's name, type, units, current NAV, market value, and return." (29 words)

Corrected: "You see portfolio-level metrics: total value, total invested, total return %, and XIRR. A holdings table shows each investment's name, type, units, NAV, market value, and return."

Rationale: Per W10, split into sentences under 25 words each.

---

**Issue B9 — File naming convention (Severity: Medium)**

Files: help-topic-#1-ai-financial-advisor-chat.md, help-topic-#1-ai-financial-advisor-chat.html, help-topic-#2-investment-portfolio-tracking.md, help-topic-#2-investment-portfolio-tracking.html

Original filenames use "#1" and "#2" prefixes.

Corrected filenames (per branding guide):
- help-topic-ai-financial-advisor-chat.md
- help-topic-ai-financial-advisor-chat.html
- help-topic-investment-portfolio-tracking.md
- help-topic-investment-portfolio-tracking.html

Rationale: Per B9 and branding guide, help topic slugs must be "two to four lowercase words... hyphenated". The "#" character violates this convention. Filenames must be updated, and all hyperlinks in release notes and help topics must be updated to match.

---

**Issue HT-S2 — Missing overview sub-labels (Severity: Medium)**

Files: help-topic-#1-ai-financial-advisor-chat.md (lines 6-9), help-topic-#1-ai-financial-advisor-chat.html (lines 170-174), help-topic-#2-investment-portfolio-tracking.md (lines 6-9), help-topic-#2-investment-portfolio-tracking.html (lines 170-174)

Original (both help topics, MD format):
## Overview

- **Get specific, numeric guidance...** without navigating multiple screens...
- **Ask follow-up questions...** — the advisor uses...
- **Preserve your conversation history** as you explore...

Expected (per benchmark expected-output-2.md):
### Overview

**What it does:** Analyses your current month's spending...

**Why it matters:** Previously, you only found out...

**Key benefits:** Shows the exact category...

Corrected (MD format, Help Topic #1):
## Overview

**What it does:** Ask your AI Advisor natural-language questions about your spending, budgets, and investments using your actual financial data. Get specific, numeric, actionable guidance instantly without navigating multiple screens.

**Why it matters:** Previously, you had no direct way to ask your financial app questions. Now you get personalized answers tailored to your real data and financial situation.

**Key benefits:** Ask follow-up questions with full context — the advisor uses your transaction, budget, goal, and investment data. Preserve your entire conversation history for future reference. Receive personalized recommendations based on your full financial picture.

Corrected (MD format, Help Topic #2):
## Overview

**What it does:** Consolidate all your investment holdings (mutual funds, stocks, gold bonds, debt funds) into one portfolio view. See total value, total invested, total return %, XIRR, and individual investment details at a glance.

**Why it matters:** Previously, your investment holdings lived in separate apps and statements with no unified view. Now see your total invested value, performance, and asset allocation in one place.

**Key benefits:** Review individual holdings with complete details (name, type, units, NAV, value, return %). Export holdings to CSV for analysis. Receive AI-driven rebalancing alerts when your allocation deviates from targets, with specific recommendations.

Rationale: Per HT-S2, overview section must include all three sub-bullets with explicit labels: "What it does", "Why it matters", "Key benefits". Benchmark defines this structure; current output omits labels and mixes content organization.

---

## Release Notes Scorecard

| Category                | Score      |
|---|---|
| Structure (RN-S)        | 9 / 9      |
| Content accuracy (RN-C) | 6 / 8      |
| Writing standards (W)   | 7 / 10     |
| Branding (B)            | 8 / 9      |
| Hyperlinks (H)          | 3 / 3      |
| **Total**               | **33 / 39**|

**Overall:** NEEDS REVISION

---

## Help Topic Reviews

### Help Topic #1: AI Financial Advisor Chat Interface

#### Structure checks (HT-S1 to HT-S7)

| ID | Check | Result | Severity |
|---|---|---|---|
| HT-S1 | H1 is actual feature name, not placeholder | PASS | — |
| HT-S2 | Overview with three sub-bullets | **FAIL** | **Medium** |
| HT-S3 | Workflow 4-10 numbered steps | PASS | — |
| HT-S4 | Workflow describes user actions/sees | PASS | — |
| HT-S5 | API Details omitted with [INSERT] flag | PASS | — |
| HT-S6 | Back-link to release notes present | PASS | — |
| HT-S7 | Back-link points to actual release note | PASS | — |

**HT-S Score: 6/7**

#### Content accuracy (HT-C1 to HT-C4)

| ID | Check | Result | Severity |
|---|---|---|---|
| HT-C1 | No invented API endpoints | PASS | — |
| HT-C2 | No Jira issue keys in prose | PASS | — |
| HT-C3 | No marketing language | PASS | — |
| HT-C4 | Workflow consistent with feature | PASS | — |

**HT-C Score: 4/4**

#### Writing standards (W1-W10)

| ID | Criterion | Result | Severity |
|---|---|---|---|
| W1 | Second person | PASS | — |
| W2 | Active voice | PASS | — |
| W3 | Consistent em dash use | PASS | — |
| W4 | Sentence-case headings | PASS | — |
| W5 | Present tense | PASS | — |
| W6 | Number formatting | PASS | — |
| W7 | Currency formatting | PASS | — |
| W8 | No hedging language | PASS | — |
| W9 | No product name in body | **FAIL** | **Low** |
| W10 | Sentence length | PASS | — |

**W Score: 9/10**

W9 Violation Detail: Line 13 MD and line 179 HTML: "Open the WealthWise app and click **Ask AI Advisor**..."

The product name "WealthWise" appears in body prose. Per W9, it should be only in headers/footers. However, this is a UI element reference ("the WealthWise app") which may be acceptable when naming the specific product UI. This is a **low-severity finding** and may be acceptable as-is.

#### Branding (B1-B9)

| ID | Check | Result | Severity |
|---|---|---|---|
| B1-B9 | HTML uses non-standard template | **FAIL** | **Low** |

The HTML help topic uses a different CSS template and styling than the release notes HTML. The release notes use the WealthWise brand template from branding.md; the help topics use a distinct custom template with purple accents and different layout. While functional and accessible, this creates visual inconsistency. This is **low-severity** as it does not violate any specific requirement but represents a branding inconsistency.

#### Help Topic #1 Scorecard

| Category         | Score     |
|---|---|
| Structure (HT-S) | 6 / 7     |
| Content (HT-C)   | 4 / 4     |
| Writing + Branding | 9 / 10  |
| **Total**        | **19 / 21**|

**Overall:** NEEDS REVISION (Medium-severity HT-S2 issue)

---

### Help Topic #2: Investment Portfolio Tracking

#### Structure checks (HT-S1 to HT-S7)

| ID | Check | Result | Severity |
|---|---|---|---|
| HT-S1 | H1 is actual feature name | PASS | — |
| HT-S2 | Overview with three sub-bullets | **FAIL** | **Medium** |
| HT-S3 | Workflow 4-10 numbered steps | PASS | — |
| HT-S4 | Workflow describes user actions/sees | PASS | — |
| HT-S5 | API Details omitted with [INSERT] flag | PASS | — |
| HT-S6 | Back-link to release notes present | PASS | — |
| HT-S7 | Back-link points to actual release note | PASS | — |

**HT-S Score: 6/7**

#### Content accuracy (HT-C1 to HT-C4)

| ID | Check | Result | Severity |
|---|---|---|---|
| HT-C1 | No invented API endpoints | PASS | — |
| HT-C2 | No Jira issue keys in prose | PASS | — |
| HT-C3 | No marketing language | PASS | — |
| HT-C4 | Workflow consistent with feature | PASS | — |

**HT-C Score: 4/4**

#### Writing standards (W1-W10)

| ID | Criterion | Result | Severity |
|---|---|---|---|
| W1 | Second person | PASS | — |
| W2 | Active voice | PASS | — |
| W3 | Consistent em dash use | PASS | — |
| W4 | Sentence-case headings | PASS | — |
| W5 | Present tense | PASS | — |
| W6 | Number formatting | PASS | — |
| W7 | Currency formatting | PASS | — |
| W8 | No hedging language | PASS | — |
| W9 | No product name in body | PASS | — |
| W10 | Sentence length | PASS | — |

**W Score: 10/10**

#### Branding (B1-B9)

| ID | Check | Result | Severity |
|---|---|---|---|
| B1-B9 | HTML uses non-standard template | **FAIL** | **Low** |

Same as Help Topic #1: distinct custom template creates visual inconsistency with release notes.

#### Help Topic #2 Scorecard

| Category         | Score     |
|---|---|
| Structure (HT-S) | 6 / 7     |
| Content (HT-C)   | 4 / 4     |
| Writing + Branding | 9 / 10  |
| **Total**        | **19 / 21**|

**Overall:** NEEDS REVISION (Medium-severity HT-S2 issue)

---

## Combined Summary

| File | Overall | High | Medium | Low |
|---|---|---|---|---|
| release-note-1-0-whats-new.md | NEEDS REVISION | 2 | 3 | 0 |
| release-note-1-0-whats-new.html | NEEDS REVISION | 2 | 3 | 0 |
| help-topic-#1-ai-financial-advisor-chat.md | NEEDS REVISION | 0 | 1 | 1 |
| help-topic-#1-ai-financial-advisor-chat.html | NEEDS REVISION | 0 | 1 | 1 |
| help-topic-#2-investment-portfolio-tracking.md | NEEDS REVISION | 0 | 1 | 0 |
| help-topic-#2-investment-portfolio-tracking.html | NEEDS REVISION | 0 | 1 | 0 |

**Top 3 improvements ranked by reader impact:**

1. **RN-C5 — Remove severity label "critical" (High):** Readers interpret "critical bugs" as priority messaging, violating WealthWise policy. Simply state "resolves three bugs..." to maintain neutrality and trust.

2. **RN-C7 — Add missing AI tags (Medium):** Two features describe AI-driven functionality but lack the required AI badge. Readers rely on the (AI) tag to recognize AI-generated content at a glance; omitting it breaks that contract.

3. **W10 — Break long sentences into readable chunks (High):** The 41-word overview paragraph forces readers to process multiple concepts at once. Splitting into 3-4 shorter sentences improves comprehension and matches WealthWise writing standards.

---

## Pipeline Recommendation

[x] Corrections needed → Orchestrator apply auto-fixes, then confirm before publishing

**Next steps:**
1. Orchestrator applies all High and Medium severity corrections to MD and HTML files
2. Confirm hyperlinks and filenames are updated consistently (if B9 file rename is applied)
3. Re-run reviewer on corrected output to verify all findings resolved
4. Once all issues are PASS, approve for human technical review and publication
