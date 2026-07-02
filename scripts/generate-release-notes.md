# File: `scripts/generate-release-notes.md`

# Generate Release Notes Execution Script

## Purpose

This script orchestrates the complete AI workflow for generating customer-facing release notes.

Execute each step sequentially and save the output before continuing to the next step.

Do not skip any steps.

---

# Workflow

```text
Collector
    ↓
Analyzer
    ↓
Writer
    ↓
Reviewer
    ↓
Draft Generator
```

---

# Input

Release Version

Example

```text
2025.8
```

---

# Step 1 — Collect Release Data

## Agent

Collector Agent

## Input

```text
data/release-<release-version>.json
```

Example

```text
data/release-2025.8.json
```

## Action

Load the release data.

Validate that the file exists.

If the file cannot be found, stop the workflow.

Save a copy of the collected data.

## Output

```text
output/collected-release-data-<release-version>.json
```

---

# Step 2 — Analyze Release Data

## Agent

Analyzer Agent

## Prompt

```text
.claude/prompts/analyze-release.md
```

## Skills

* classify-release-items.md

## Action

Analyze the collected release data.

Classify work items into:

* Features
* Enhancements
* Bug Fixes

Ignore technical implementation work.

## Output

```text
output/artifacts/ai/analyzed-release.json
```

---

# Step 3 — Generate Release Notes

## Agent

Writer Agent

## Prompt

```text
.claude/prompts/write-release-notes.md
```

## Skills

* customer-friendly-language.md
* release-note-template.md

## Action

Generate customer-facing release notes.

Apply the standard release note template.

Do not include internal IDs.

## Output

```text
output/artifacts/ai/release-notes.md
```

---

# Step 4 — Review Release Notes

## Agent

Reviewer Agent

## Prompt

```text
.claude/prompts/review-release-notes.md
```

## Skills

* customer-friendly-language.md
* quality-review-checklist.md

## Action

Review the generated release notes.

Validate:

* Grammar
* Customer language
* Markdown
* Consistency
* Internal IDs
* Technical terminology

Generate a review report.

## Output

```text
output/artifacts/ai/review-report.md
```

---

# Step 5 — Create Document360 Draft

## Agent

Draft Generator Agent

## Prompt

```text
.claude/prompts/create-document360-draft.md
```

## Skills

* release-note-template.md
* release-note-metadata.md

## Action

Read:

* release-notes.md
* review-report.md

Apply:

* Release Note Template
* Metadata
* Draft Status

Prepare the article exactly as it should appear in Document360.

Do **not** publish the article.

## Output

```text
output/artifacts/publishing/document360-draft.md
```

---

# Step 6 — Generate Publication Checklist

## Action

Generate a publication checklist for the Technical Writer.

The checklist should confirm:

* AI review completed
* Technical Writer review pending
* SME review pending
* Metadata completed
* Draft created
* Ready for human review

## Output

```text
output/artifacts/publishing/publication-checklist.md
```

---

# Workflow Complete

When all steps have completed successfully, display the following summary.

```text
Release Notes Generation Complete

Artifacts Created

✓ analyzed-release.json

✓ release-notes.md

✓ review-report.md

✓ document360-draft.md

✓ publication-checklist.md

Next Step

Technical Writer Review
```

---

# Error Handling

Stop the workflow if:

* Release data is missing.
* JSON is invalid.
* A required prompt cannot be found.
* A required skill cannot be found.

Return a clear error message describing the issue.

---

# Success Criteria

The workflow is complete when:

* All AI artifacts have been generated.
* The Document360 draft has been created.
* The publication checklist has been generated.
* The draft is ready for Technical Writer review.
