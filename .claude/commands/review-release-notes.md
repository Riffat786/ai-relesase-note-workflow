# File: `.claude/commands/review-release-notes.md`

# /review-release-notes

## Purpose

Review the generated release notes and produce an AI quality review report.

The purpose of this command is to validate the release notes before they are prepared as a Document360 draft.

This command does **not** rewrite the release notes or publish documentation.

---

## Input

Generated release notes.

```text
output/artifacts/ai/release-notes.md
```

---

## Instructions

1. Read:

```text
output/artifacts/ai/release-notes.md
```

2. Use the prompt:

```text
.claude/prompts/review-release-notes.md
```

3. Apply the following skills:

```text
.claude/skills/customer-friendly-language/SKILL.md

.claude/skills/quality-review-checklist/SKILL.md
```

4. Review the release notes for:

* Customer-friendly language
* Grammar and spelling
* Markdown formatting
* Consistency
* Completeness
* Professional tone
* Internal work item IDs
* Technical accuracy

5. Identify any issues.

6. Recommend improvements where necessary.

7. Generate a review report.

Do **not** modify the release notes.

---
### Review Report Requirements

Generate a structured **AI Quality Review Report**.

The report must include the following sections.

#### Release Information

Include:

* Release Version
* Review Date
* Reviewer
* Review Status

---

#### Overall Quality Score

Calculate an overall quality score based on the review findings.

Include:

* Overall Quality Score
* Pass / Fail Status

---

#### Score Breakdown

Provide a score breakdown for each review category.

Example categories include:

* Customer Language
* Technical Accuracy
* Markdown Formatting
* Completeness
* Consistency

The scores should reflect the actual review findings and should not be hardcoded.

---

#### Quality Assessment

Assess the release notes against the review criteria.

Include:

* Customer-Friendly Language
* Grammar & Spelling
* Markdown Formatting
* Internal Work Item IDs
* Technical Accuracy
* Consistency
* Completeness
* Professional Tone
* Release Note Template Compliance

Each assessment should include:

* Result (Pass / Warning / Fail)
* Notes
* Recommendations (if applicable)

---

#### Detailed Review

Provide a detailed explanation of the review findings.

Highlight:

* Strengths
* Weaknesses
* Potential Risks
* Suggested Improvements

---

#### Strengths Summary

Summarize the strongest aspects of the release notes.

---

#### Recommendations

Provide recommendations for the Technical Writer.

Recommendations should be categorized as:

* Critical
* Recommended
* Optional

---

#### AI Review Metadata

Include:

* Reviewer Agent Version
* Prompt Version
* Review Timestamp
* Input Artifact
* Output Artifact

Generate the timestamp during execution.

---

#### AI Quality Check

Provide the overall review result.

Possible values include:

* PASSED
* PASSED WITH RECOMMENDATIONS
* FAILED

---

#### Recommended Next Step

Based on the review outcome, recommend one of the following:

* Create Document360 Draft
* Return to Writer Agent
* Manual Technical Writer Review Required

---

#### Review Checklist Summary

Generate a checklist summarizing the review outcome.

Include the review status for each completed quality check.

---

#### Sign-Off

Include the workflow status for:

* AI Quality Review
* Technical Writer Review
* SME Review
* Documentation Approval

## Output

Create:

```text
output/artifacts/ai/review-report.md
```

---

## Review Report

The report should include:

* Release Version
* Overall Quality Score
* Customer Language
* Grammar
* Markdown Formatting
* Internal IDs
* Technical Accuracy
* Consistency
* Completeness
* Recommendations
* AI Quality Check
* Next Step

---

## Expected Summary

Display:

```text
Release Notes Review Complete

Quality Score: 95/100

AI Quality Check: PASSED

Artifact:

output/artifacts/ai/review-report.md

Next Step:

Create Document360 Draft
```

---

## Success Criteria

The command is successful when:

* The release notes have been reviewed.
* A quality report has been generated.
* Recommendations have been documented.
* The review report has been saved.

No changes should be made to the release notes.
