# Release Note Publisher Skill

## Metadata

- **Skill Name:** Release Note Publisher
- **Version:** 1.0
- **Author:** Bhargavi
- **Status:** Active

---

## Objective

Transform AI-generated and reviewed release notes into publication-ready documentation by applying standardized formatting, document structure, metadata handling, and publication standards while preserving the approved customer-facing content.

---

## Scope

This skill is responsible for preparing reviewed release notes for customer publication.

The skill applies formatting, document structure, metadata handling, and publication standards to produce a professional release notes document.

This skill does not:

- Generate new release note content.
- Modify approved business or technical information.
- Add, remove, or reorder release items.
- Change the intent or meaning of the approved release notes.

Its responsibility is limited to preparing the final publication-ready document.

---

## Dependencies

This skill shall be executed only after the successful completion of:

1. Release Data Extractor
2. Release Note Generator
3. Release Note Reviewer

---

## Input

The skill requires the following inputs:

- Generated Release Notes (`release-notes.md`)
- Review Report (`release-note-review-report.md`)

The review report is used only as a quality validation reference.

The skill shall extract and apply only the accepted review recommendations that improve the quality of the release notes.

The following information from the review report must **never** appear in the published document:

- Review Summary
- Quality Score
- Findings
- Recommendations
- Reviewer Comments
- Validation Messages
- AI Explanations
- Internal Notes

---

## Responsibilities

The skill shall:

- Read the generated release notes.
- Read the review report.
- Apply accepted review recommendations where appropriate.
- Ignore all review metadata and review analysis.
- Remove reviewer comments.
- Remove quality scores.
- Remove review summaries.
- Remove findings and recommendations.
- Remove validation messages.
- Remove AI-generated explanations.
- Remove Jira IDs.
- Remove implementation notes.
- Remove internal comments and references.
- Apply the organization's release note template.
- Apply the required document structure.
- Apply professional formatting.
- Preserve the information hierarchy.
- Generate publication-ready Microsoft Word (.docx) and HTML (.html) documents.

---

## Document Structure

The final release notes shall contain the following sections in the specified order.

1. Release Title
2. Release Version
3. Release Date
4. Overview
5. New Features
6. Enhancements
7. Bug Fixes
8. Regulatory Updates
9. Known Issues
10. Additional Notes

### Metadata Rules

- Display **Product** in the document header only when every release item belongs to the same product.
- If multiple products are present, omit Product from the document header.
- Display **Product** beneath the corresponding feature whenever available.
- Display **Module** beneath the corresponding feature whenever available.
- Never infer or invent Product or Module information.
- Omit unavailable metadata instead of generating placeholder values.

---

## Content Structure Standards

Preserve the semantic hierarchy of the approved release notes.

Each release item shall be treated as one parent item.

For every release item, present information in the following order:

- Title
- Product (if available)
- Module (if available)
- Description
- Customer Benefit or Business Impact (if available)

Customer Benefit and Business Impact shall always belong to their corresponding release item.

Do not render Customer Benefit or Business Impact as independent release items.

Do not flatten hierarchical content during Markdown, HTML, or Microsoft Word conversion.

The publisher shall preserve the semantic relationship between content elements and shall not alter the approved structure of the generated release notes during format conversion.

---

## Formatting Standards

### Document Title (Heading 1)

- Font: Cambria
- Font Size: 20 pt
- Font Style: Bold
- Font Color: Black
- Alignment: Left

### Section Headings (Heading 2)

- Font: Cambria
- Font Size: 16 pt
- Font Style: Bold
- Font Color: Black
- Alignment: Left

### Body Text

- Font: Cambria
- Font Size: 11 pt
- Font Style: Regular
- Font Color: Black
- Alignment: Left

### Bullet Lists

- Use a solid black square (■) for all bullet lists.
- Maintain consistent indentation and spacing.

### General Formatting

- Maintain consistent spacing throughout the document.
- Use **Title Case** for all section headings.
- Maintain a consistent heading hierarchy.
- Preserve the information hierarchy across all output formats.
- Ensure correct grammar, spelling, and punctuation.
- Remove duplicate or redundant information.
- Produce a clean, professional, customer-facing document.

---

## Constraints

- Do not modify approved customer-facing content.
- Do not infer or invent missing information.
- Do not introduce new features, enhancements, or bug fixes.
- Do not remove approved customer-facing information.
- Do not publish review summaries.
- Do not publish quality scores.
- Do not publish findings.
- Do not publish recommendations.
- Do not publish reviewer comments.
- Do not publish validation messages.
- Do not publish AI-generated explanations.
- Do not publish Jira IDs.
- Do not publish implementation notes.
- Preserve the accuracy and intent of the approved release notes.

---

## Output

Generate only the final customer-facing publication-ready release notes.

The final document shall contain only information relevant to the customer.

Do not include:

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

Generate the final publication-ready document in:

- Microsoft Word (.docx)
- HTML (.html)

The generated outputs shall:

- Preserve identical customer-facing content.
- Maintain the same document structure.
- Preserve identical information hierarchy across Markdown, HTML, and Microsoft Word.
- Preserve parent-child relationships between Features and Customer Benefits.
- Preserve Product and Module associations for each feature.
- Maintain consistent heading hierarchy.
- Maintain consistent formatting and spacing.
- Preserve bullet styles and indentation.
- Be suitable for direct customer publication with minimal manual editing.

---

## Success Criteria

The skill is considered successful when:

- The generated document contains only customer-facing release note content.
- All review artifacts have been removed.
- The document follows the defined formatting standards.
- The approved content remains unchanged.
- Feature hierarchy is preserved.
- Customer Benefit and Business Impact remain associated with the correct Feature.
- Product and Module metadata are correctly displayed whenever available.
- The document is visually professional and publication-ready.
- The output is suitable for publication in Microsoft Word (.docx) and HTML (.html) formats with minimal manual effort.