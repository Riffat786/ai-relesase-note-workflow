---
name: quality-review-checklist
description: Reviews generated release notes against documentation quality standards before publication.
version: 1.0.0
---

# Quality Review Checklist

## Purpose

Validate release notes before they proceed to the draft generation stage.

Ensure release notes meet documentation quality standards before publication.
---

## Review Areas

- Customer-friendly language
- Grammar and spelling
- Markdown formatting
- Consistency
- Technical accuracy
- Completeness
- Internal work item traceability
- Release note template compliance

## Output

Generate recommendations without modifying the release notes.

## Review Checklist

### Accuracy

* Information matches the analyzed release data.
* No unsupported claims are introduced.

---

### Customer Language

* Customer-friendly terminology is used.
* Benefits are clearly described.
* Technical jargon is avoided.

---

### Formatting

* Markdown is valid.
* Heading hierarchy is correct.
* Sections follow the release note template.

---

### Consistency

* Tone is professional.
* Terminology is consistent.
* Verb tense is consistent.

---

### Content Quality

* No duplicate information.
* No Azure DevOps references.
* No ServiceNow references.
* No implementation details.

---

### Completeness

Verify that all relevant:

* Features
* Enhancements
* Bug fixes

have been included.

---

## Approval Decision

Return one of the following:

### Approved

The release notes meet all quality standards.

### Needs Revision

Provide:

* Summary of issues
* Recommended changes
* Sections requiring revision

---

## Success Criteria

The final release notes are ready for publication with minimal or no manual editing.

---

## Related Skills

* customer-friendly-language/SKILL.md
* release-note-template/SKILL.md
* classify-release-items/SKILL.md
