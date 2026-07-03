# Publish Release Notes

## Purpose

Invoke the **Release Note Publisher** skill to transform reviewed release notes into publication-ready documentation suitable for customer distribution.

---

## Arguments

$ARGUMENTS

---

## Prerequisites

Ensure the following workflow has completed successfully:

1. Release Data Extractor
2. Release Note Generator
3. Release Note Reviewer

---

## Instructions

1. Read the generated release notes from:

   `sample-data/release-notes.md`

2. Read the review report from:

   `sample-data/release-note-review-report.md`

3. Use the review report only as a quality validation reference.

4. Apply only the accepted review recommendations that improve the quality and readability of the release notes.

5. Exclude all review artifacts from the final published document, including:

   - Review Summary
   - Quality Score
   - Findings
   - Recommendations
   - Reviewer Comments
   - Validation Messages
   - AI Explanations
   - Internal References
   - Jira IDs
   - Implementation Notes

6. Invoke the **Release Note Publisher** skill located at:

   `skills/release-note-publisher-skill.md`

7. Apply the defined document structure, documentation standards, and formatting guidelines.

8. Generate the final customer-facing publication-ready release notes.

9. Generate publication-ready release notes that are suitable for export to:

   - Microsoft Word (.docx)
   - HTML (.html)

10. Save the publication-ready output to the specified output location.

---

## Expected Output

Generate publication-ready release notes that:

- Preserve the approved customer-facing content.
- Apply the defined document structure.
- Apply consistent formatting and heading hierarchy.
- Exclude all review artifacts and internal information.
- Are suitable for direct customer publication with minimal manual editing.
- Are ready for export to Microsoft Word (.docx) and HTML (.html).