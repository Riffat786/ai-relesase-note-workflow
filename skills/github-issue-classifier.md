# GitHub Issue Classification Helper

## Purpose

Maps GitHub labels and issue data to WealthWise release note categories:
- **What's New** — Features, new capabilities
- **Enhancements** — Improvements to existing features
- **Bug Fixes** — Bug resolutions
- **Known Issues** — Disclosed known limitations

## Data Source

GitHub repository: `ShubhKN/WealthWise`
Milestone: `v1.0`

## Classification Rules

### What's New
**Source GitHub labels:** `type: feature`
**Conditions:**
- Issue type (via label): `type: feature`
- Status: Open, Closed, or merged (closed with resolution indicates completion)
- Must have a summary and description

**Output fields per issue:**
- Feature name (from issue title, first ~50 chars)
- Description (from issue body, up to 2 sentences)
- Help topic slug (derived from title: lowercase, hyphens)
- AI flag (if label `component: ai-advisor` or mention of AI in description)

---

### Enhancements
**Source GitHub labels:** `type: enhancement`
**Conditions:**
- Issue type: `type: enhancement`
- Status: Open or Closed (completed enhancements)

**Output fields:**
- Enhancement name (from title)
- Description (from body, 1-2 sentences, starting with "Improved" or "Added")
- Before/after narrative (extracted from body or constructed from summary)

---

### Bug Fixes
**Source GitHub labels:** `type: bug` (but NOT `status: known-issue`)
**Conditions:**
- Label: `type: bug`
- Does NOT have label: `status: known-issue`
- Status: Closed (must be resolved)
- Must have resolution or fix description in body

**Output fields:**
- Bug ID: GitHub issue number (e.g., #5)
- Description: Issue title + short summary from body
- Fix/Solution: Extracted from issue body (look for "Fix:", "Solution:", "Resolution:")

---

### Known Issues
**Source GitHub labels:** `type: bug` + `status: known-issue`
**Conditions:**
- Both labels present: `type: bug` AND `status: known-issue`
- Status: Any (typically Open — not yet fixed)
- Has planned resolution or disclosure text

**Output fields:**
- Issue title
- Impact description (from body)
- Planned resolution / workaround (from body, if any)
- Targetted fix version (milestone, if different from current release)

---

## Fetch Query

GitHub GraphQL or REST API call:

```
Repository: ShubhKN/WealthWise
Milestone: v1.0
Query:
  - All issues with milestone v1.0
  - Include labels, title, body, number, state (open/closed)
  - Order by creation date ascending
```

**Filter chain:**

```
For each issue in milestone v1.0:
  1. Extract all labels
  2. Check label: `type: feature` → What's New category
  3. Check label: `type: enhancement` → Enhancements category
  4. Check label: `type: bug`:
     a. If also has `status: known-issue` → Known Issues
     b. Else if state = "closed" → Bug Fixes
     c. Else → Skip (open unresolved bugs not released)
  5. Assign to category, extract fields, apply branding rules
```

---

## Field Extraction Rules

### Issue Title
- Trim "[Feature]", "[Enhancement]", "[Bug]", "[Known Issue]" prefixes
- Use the clean title for all outputs
- Example: `[Feature] AI Financial Advisor Chat Interface` → `AI Financial Advisor Chat Interface`

### Issue Body / Description
- Extract first non-empty paragraph as summary
- For What's New: use first 1-2 sentences describing the feature
- For Enhancements: use 1-2 sentences describing the improvement
- For Bug Fixes: use body text after "## Fix" or "## Solution" section
- Strip HTML, Markdown formatting; plain text only for extraction

### Help Topic Slug (What's New only)
- Convert title to URL-safe slug:
  - Lowercase
  - Replace spaces with hyphens
  - Remove special characters except hyphens
  - Max 50 chars
- Example: `AI Financial Advisor Chat Interface` → `ai-financial-advisor-chat`

### AI Flag / Tag
- If any label contains `component: ai-advisor` or `ai-*` → Apply `tag-ai` badge in output
- If description mentions "AI", "machine learning", "auto*" → Flag for review (ask writer to confirm AI tag)

### Bug Fix Table Fields
Required fields for bug fixes (exactly three columns):
1. **Bug ID**: GitHub issue number (#5)
2. **Description**: Issue title + 1-line summary
3. **Fix / Solution**: Extracted from issue body

---

## Acceptance Criteria for Classification

- [ ] All issues in milestone v1.0 fetched successfully
- [ ] No issues mis-classified (manual spot-check on 3 issues from each category)
- [ ] All required fields extracted per category
- [ ] Help topic slugs are valid, unique, URL-safe
- [ ] AI tags applied only to AI-driven features
- [ ] Bug fixes have non-empty "Fix" field
- [ ] Known issues have "Impact" and optional "Workaround" text
- [ ] No issues duplicated across categories
