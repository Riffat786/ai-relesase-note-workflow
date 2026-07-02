# File: `.claude/commands/generate-release-notes.md`

# /generate-release-notes

## Purpose

Generate a complete set of release note artifacts for a specified software release using the AI workflow.

The workflow should execute each stage in sequence, saving the output from one stage before continuing to the next.

The workflow ends when a Document360 draft and publication checklist have been created.

---

## Input

Release Version

Example

```text
/generate-release-notes 2025.8
```

---

# Workflow

Execute the following steps **in order**.

Do not skip any step.

Stop immediately if a required input cannot be found.

---

# Step 1 — Load Release Data

Read:

```text
data/release-{{releaseVersion}}.json
```

Validate that the file exists.

If it does not exist:

* Stop the workflow.
* Return an error describing the missing file.

Save a copy of the collected release data as:

```text
output/collected-release-data-{{releaseVersion}}.json
```

---

# Step 2 — Analyze the Release

Use:

```text
.claude/prompts/analyze-release.md
```

Apply the following skills:

```text
.claude/skills/classify-release-items/SKILL.md
```

Generate:

```text
output/artifacts/ai/analyzed-release.json
```

The analysis must:

* Classify Features
* Classify Enhancements
* Classify Bug Fixes
* Exclude internal technical work
* Produce valid JSON

---

# Step 3 — Generate Release Notes

Use:

```text
.claude/prompts/write-release-notes.md
```

Apply the following skills:

```text
.claude/skills/customer-friendly-language/SKILL.md

.claude/skills/release-note-template/SKILL.md
```

Input:

```text
output/artifacts/ai/analyzed-release.json
```

Generate:

```text
output/artifacts/ai/release-notes.md
```

Requirements:

* Customer-friendly language
* Professional tone
* Markdown formatting
* Add internal IDs
* Follow the release note template

---

# Step 4 — Review Release Notes

Use:

```text
.claude/prompts/review-release-notes.md
```

Apply the following skills:

```text
.claude/skills/customer-friendly-language/SKILL.md

.claude/skills/quality-review-checklist/SKILL.md
```

Input:

```text
output/artifacts/ai/release-notes.md
```

Generate:

```text
output/artifacts/ai/review-report.md
```

The review report should include:

* AI Quality Check
* Summary
* Recommendations
* Next Step

The final status should be:

```text
AI Quality Check: Passed

Next Step:
Technical Writer Review
```

unless issues are found.

---

# Step 5 — Create Document360 Draft

Use:

```text
.claude/prompts/create-document360-draft.md
```

Apply the following skills:

```text
.claude/skills/release-note-template/SKILL.md

.claude/skills/release-note-metadata/SKILL.md
```

Inputs:

```text
output/artifacts/ai/release-notes.md

output/artifacts/ai/review-report.md
```

Generate:

```text
output/artifacts/publishing/document360-draft.md
```

The draft must:

* Apply the standard release note template.
* Populate metadata.
* Set article status to Draft.
* Be ready for Technical Writer review.
* Never publish automatically.

---

# Step 6 — Create Publication Checklist

Generate:

```text
output/artifacts/publishing/publication-checklist.md
```

The checklist should include:

* AI review completed
* Technical Writer review pending
* SME review pending
* Metadata verified
* Category verified
* Tags verified
* Draft ready for review

---

# Workflow Summary

After completing all steps, display the following summary.

```text
Release Notes Generation Complete

Artifacts Created

AI

✓ analyzed-release.json

✓ release-notes.md

✓ review-report.md

Publishing

✓ document360-draft.md

✓ publication-checklist.md

Next Step

Technical Writer Review
```

---

# Error Handling

Stop the workflow if:

* Release data cannot be found.
* JSON is invalid.
* A required prompt is missing.
* A required skill is missing.
* Output cannot be generated.

Return a clear error message explaining the problem.

---

# Success Criteria

The workflow is complete only when the following artifacts exist:

```text
output/

artifacts/

    ai/

        analyzed-release.json

        release-notes.md

        review-report.md

    publishing/

        document360-draft.md

        publication-checklist.md
```

The workflow should not continue to human review or publication.

Publication remains the responsibility of the Technical Writer and Subject Matter Expert.

