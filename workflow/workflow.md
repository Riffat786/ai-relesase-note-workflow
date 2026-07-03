# Technical Writing Workflow: Release Notes & Help Topics

## Overview

This document describes the traditional technical writing workflow for creating release notes and help topics. This is the **pre-automation baseline** that the GlobalMail Pro automation pipeline replicates and enhances.

---

## Phase 1: Planning & Scope Definition

### Step 1.1: Gather Release Information

**Input:**
- Product roadmap/release plan
- Jira issues or issue tracking system
- Engineering change logs
- Product manager notes

**Activities:**
1. Review all issues planned for the release
2. Classify issues by type (features, enhancements, bugs, known issues)
3. Determine release version and date
4. Identify major themes (e.g., "Performance & Compliance Focus")

**Output:**
- Release scope document
- Issue list organized by category
- Release version and date confirmed

**Time:** 2–4 hours

### Step 1.2: Define Documentation Scope

**Activities:**
1. Determine which features require help topics (usually: new features, major enhancements)
2. Decide on release notes structure and sections
3. Identify links needed between release notes and help topics
4. Plan for API documentation (if applicable)

**Output:**
- Documentation scope checklist
- Help topic list (which features need documentation)
- Structural outline for release notes

**Time:** 1–2 hours

---

## Phase 2: Information Gathering

### Step 2.1: Extract Feature Details from Jira

**For each feature/enhancement:**

1. **Read the issue summary and description**
   - What is the feature?
   - What problem does it solve?
   - What are the user benefits?

2. **Review comments and acceptance criteria**
   - Look for design decisions
   - Note any edge cases or limitations
   - Identify future enhancements mentioned

3. **Check for linked Confluence pages**
   - Technical specifications
   - Design documents
   - API endpoint definitions

4. **Clarify with product manager/engineer if needed**
   - Request user-facing language
   - Ask about target user audience
   - Get examples or use cases

**Output per feature:**
```
Feature Title: [from Jira summary]
Description: [user-facing explanation]
Benefits: [what users gain]
User Action Required: [setup steps, if any]
Related Areas: [other features, modules affected]
API Endpoint: [if applicable]
Help Topic Needed: Yes/No
```

**Time:** 15–30 minutes per feature

### Step 2.2: Extract Bug Fix Details from Jira

**For each bug:**

1. **Read the issue title and description**
   - What was broken?
   - How did users experience the problem?
   - What was the severity/impact?

2. **Review resolution notes**
   - What was the root cause? (don't include in output)
   - What was fixed? (include in output)
   - What changed from user perspective?

3. **Check for workarounds documented**
   - Was there a temporary workaround?
   - Include in release notes for users still on old version

4. **Determine severity mapping**
   - Highest/High priority → High severity
   - Medium priority → Medium severity
   - Low/Lowest priority → Low severity

**Output per bug:**
```
Bug ID: [Jira key]
Title: [user-facing summary]
Severity: [High / Medium / Low]
Affected Area: [Dashboard, Compliance, etc.]
What Was Broken: [user impact description]
What is Now Fixed: [resolution description]
User Impact: [what users can now do]
Workaround: [if applicable, include for documentation]
```

**Time:** 10–20 minutes per bug

### Step 2.3: Extract Known Issue Details

**For each known issue:**

1. **Read the issue description**
   - What is the limitation?
   - What is the current status?
   - Is there a timeline for fix?

2. **Document the workaround**
   - What can users do to work around the issue?
   - Is it a temporary solution or permanent recommendation?

3. **Determine communication strategy**
   - Should this be prominent or de-emphasized?
   - Is it a blocker for users or minor inconvenience?

**Output per known issue:**
```
Known Issue Title: [user-facing title]
Description: [what doesn't work, why]
Workaround: [steps users can take]
Status: [when/if it will be fixed]
```

**Time:** 10–15 minutes per known issue

---

## Phase 3: Content Development

### Step 3.1: Write Release Notes (Markdown)

**Structure:**

```markdown
# [Product Name] — Release [Version]

[Release Date]

---

## Overview

[Summary paragraph: mention feature count, enhancement count, bug fix count, 
known issue count. Highlight major theme if applicable.]

---

## New Features

### [Feature Title]

[Opening paragraph: Describe what the feature does and why it matters. 
1-3 sentences. Do not start with "Previously".]

**What you need to do**

[State any setup or configuration required. If no action needed: 
"No configuration changes are required."]

**Benefits**

- [User benefit 1]
- [User benefit 2]
- [User benefit 3]

[Link to help topic if available]

---

## Enhancements

- **[Enhancement Title]:** [Brief description of improvement and user impact]
- **[Enhancement Title]:** [Brief description]

---

## Bug Fixes

| Bug ID | Area of Impact | Issue | Fix |
|--------|---|---|---|
| KAN-23 | Dashboard | [Description of what was broken] | [Description of what is fixed] |
| KAN-31 | Compliance | [Description of what was broken] | [Description of what is fixed] |

---

## Known Issues

**[Issue Title]**

[Description of the limitation or problem]

*Workaround:* [Steps users can take to work around the issue]

---

For help with any feature, contact support or visit the Help Center.
```

**Writing Standards (MSTP):**
- Active voice: "The system validates" not "is validated by the system"
- Present tense: "The feature now supports" not "will support"
- No marketing language: avoid "powerful", "seamless", "cutting-edge"
- Second person: "You can now..." where applicable
- Oxford comma: "A, B, and C" not "A, B and C"
- Spell out numbers 0–9, use numerals for 10+
- Sentence case on headings: "Smart address validation" not "Smart Address Validation"

**Time:** 4–8 hours (depending on feature count)

### Step 3.2: Create Help Topics (One per New Feature)

**Structure:**

```markdown
# [Feature Title]

[One-line description of what the feature does]

---

## Overview

**What it does:** [Detailed description of the feature]

**Why it matters:** [User problem it solves]

**Key benefits:**
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

---

## Workflow

1. [Step 1 - User action or system behavior]
2. [Step 2 - Continuation]
3. [Step 3 - Result]
...
7. [Final step]

---

## API Details (if applicable)

**Endpoint:** `/api/v1/[resource]/[action]`

**Method:** `POST` / `GET` / `PUT` / `DELETE`

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| param1 | string | Yes | Description |
| param2 | integer | No | Description |

### Example Request

\`\`\`json
{
  "param1": "value",
  "param2": 123
}
\`\`\`

### Example Response

\`\`\`json
{
  "success": true,
  "result": {
    "id": "123",
    "status": "completed"
  }
}
\`\`\`

---

## Tips for best results

- [Tip 1]
- [Tip 2]
- [Tip 3]

---

## Troubleshooting

**Problem:** [Common user issue]

[Solution or explanation]

---

[Link back to release notes]
```

**Key Sections:**
1. **Overview** — What, why, benefits (user-focused)
2. **Workflow** — Step-by-step instructions (how to use)
3. **API Details** — For developers (if applicable)
4. **Tips** — Best practices
5. **Troubleshooting** — Common issues
6. **Back link** — To release notes

**Time:** 2–4 hours per help topic

---

## Phase 4: Branding & Formatting

### Step 4.1: Apply Brand Standards

**Typography:**
- Font: Inter (Google Fonts)
- Weights: Regular (400), SemiBold (600), Bold (700)
- H1: Bold 2rem, Navy #1B2A4A
- H2: Bold 1.35rem, Navy #1B2A4A, green underline
- H3: SemiBold 1.05rem, Light Navy #2C3E6B
- Body: Regular 1rem, Text Dark #1A1A2E

**Colour Palette:**
- Primary: Navy #1B2A4A (headings, main structure)
- Accent: Green #2ECC71 (buttons, links, highlights)
- Warning/Known Issues: Amber #FFF9E6 (background), #F39C12 (border)
- Neutral: Grays for text, borders, dividers

**HTML Structure:**
```html
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700" rel="stylesheet">
  <style>
    body { font-family: Inter, -apple-system, Arial, sans-serif; }
    h1, h2 { color: #1B2A4A; }
    a { color: #2ECC71; }
    /* Additional branding CSS */
  </style>
</head>
<body>
  <div class="header">GlobalMail Pro | Help Centre</div>
  <!-- Content -->
  <footer>© 2026 GlobalMail Pro. All rights reserved.</footer>
</body>
</html>
```

**Time:** 2–4 hours (design system already defined)

### Step 4.2: Create JSON Version

**Structure:**
```json
{
  "release": {
    "version": "1.1",
    "date": "2026-07-03",
    "product": "GlobalMail Pro"
  },
  "overview": "Release summary...",
  "newFeatures": [...],
  "enhancements": [...],
  "bugFixes": [...],
  "knownIssues": [...]
}
```

**Purpose:**
- Structured data for downstream systems
- Can be imported into CMSs or analytics platforms
- Enables programmatic access to release information

**Time:** 1–2 hours

---

## Phase 5: Quality Assurance

### Step 5.1: Content Review

**Self-Review Checklist:**
- [ ] All features, enhancements, bugs are included
- [ ] No marketing language
- [ ] Active voice throughout
- [ ] Present tense for current behavior
- [ ] Sentence case on all headings
- [ ] No internal technical details
- [ ] No unexplained acronyms
- [ ] Consistent tone throughout

**Time:** 1–2 hours

### Step 5.2: Link Verification

**Check:**
- [ ] All help topic links are valid and working
- [ ] Links use correct file names
- [ ] Release notes links back from help topics
- [ ] No broken anchors

**Time:** 30 minutes

### Step 5.3: Peer Review

**Assign to:**
- Product manager (accuracy of features/benefits)
- Engineering lead (correctness of bug descriptions)
- Another technical writer (tone, clarity, consistency)

**Time:** 2–4 hours (including revisions)

### Step 5.4: Style & Grammar Check

**Tools:**
- Grammarly for spelling/grammar
- Manual review for MSTP compliance
- Check for consistency

**Time:** 1–2 hours

---

## Phase 6: Publishing & Archiving

### Step 6.1: Final Sign-off

**By:**
- Product Manager (content accuracy)
- Technical Lead (technical accuracy)
- Documentation Manager (compliance, branding)

**Approval Criteria:**
- ✓ All sections complete and accurate
- ✓ No spelling or grammar errors
- ✓ Branding standards met
- ✓ Links verified and working
- ✓ JSON valid and well-formed

**Time:** 30 minutes

### Step 6.2: Publish to Help Center

**Steps:**
1. Upload HTML and Markdown files
2. Update navigation/table of contents
3. Create/update search index
4. Test links in published environment

**Time:** 1–2 hours

### Step 6.3: Archive & Analytics

**Actions:**
1. Store JSON version in analytics system
2. Create archive of Markdown for version control
3. Log metrics: word count, section count, feature count
4. Prepare for future reference/comparison

**Time:** 30 minutes

---

## Timeline Summary

| Phase | Activity | Time |
|-------|----------|------|
| 1 | Planning & Scope | 3–6 hours |
| 2 | Information Gathering | 2–4 hours per feature |
| 3 | Content Development | 8–16 hours |
| 4 | Branding & Formatting | 3–6 hours |
| 5 | Quality Assurance | 4–8 hours |
| 6 | Publishing & Archiving | 2–4 hours |
| **TOTAL** | **All Phases** | **22–50+ hours** |

**Typical Release (5 features, 2 enhancements, 3 bugs, 1 known issue):**
- **Estimated Time:** 40–60 hours (1–1.5 weeks, full-time)
- **Team Size:** 1–2 technical writers + reviews
- **Resources:** Multiple Jira accesses, peer reviewers, publishing access

---

## Common Challenges & Solutions

| Challenge | Impact | Solution |
|-----------|--------|----------|
| Missing information in Jira | +1–2 hours per issue | Request clarification early |
| API documentation incomplete | +2–4 hours | Get from API team, test yourself |
| Scope creep during documentation | Delays publication | Establish feature freeze date |
| Consistency issues across writers | +1–2 hours in QA | Use templates, peer review |

---

## Best Practices

1. **Start Early** — Begin documentation during development, not after release
2. **Stay Close to Jira** — Use issues as single source of truth
3. **Test Everything** — Click links, test APIs, verify all instructions work
4. **Use Templates** — Consistent structure saves time and ensures quality
5. **Collaborate** — Get engineer and PM feedback early, not in final review
6. **Version Control** — Store Markdown in git for history and collaboration
7. **Plan for Accessibility** — Ensure content is readable, findable, searchable

---

## How Automation Helps

The GlobalMail Pro automation pipeline reduces this workflow from **40–60 hours** to **2–4 hours** by:

1. **Eliminating manual data extraction** — Reads Jira directly via MCP
2. **Automating classification** — Sorts issues by type automatically
3. **Generating content structure** — Creates outlines and templates
4. **Applying branding automatically** — Inserts colours, fonts, styling
5. **Creating cross-links** — Generates help topic links automatically
6. **Running QA checks** — 22-point checklist, style audit automated
7. **Auto-fixing issues** — Corrects passive voice, marketing language, formatting
8. **Generating multiple formats** — HTML, Markdown, JSON all at once

**Result:** Writers focus on **review and refinement**, not mechanical tasks.

---

**Document Version:** 1.0  
**Last Updated:** July 3, 2026  
**Audience:** Technical Writers, Documentation Managers, Product Teams
