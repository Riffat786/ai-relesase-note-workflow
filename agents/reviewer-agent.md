# File: `agents/reviewer-agent.md`

# Reviewer Agent

## Purpose

Review generated release notes to ensure they meet documentation quality standards before publication.

The Reviewer Agent acts as the quality assurance step in the release note generation pipeline.

---

## Responsibilities

* Review generated release notes.
* Check grammar and readability.
* Verify customer-friendly language.
* Validate Markdown formatting.
* Identify missing or duplicate information.
* Recommend improvements.
* Approve or reject the release notes.

---

## Input

```text
output/release-notes.md
```

---

## Skills Used

* customer-friendly-language.md
* quality-review-checklist.md
* release-note-template.md

---

## Prompt Used

```text
.claude/prompts/review-release-notes.md
```

---

## Output

```text
output/review-report.md
```

Example:

```text
Status: Approved

No issues found.
```

or

```text
Status: Needs Revision

Recommendations:

- Simplify technical language.
- Remove duplicate enhancement.
- Improve feature summary.
```

---

## Success Criteria

* Grammar is correct.
* Tone is consistent.
* Customer-friendly language is used.
* No internal IDs are present.
* Markdown is valid.
* Release notes are ready for publication.

---

## Future MCP Tools

Document360 MCP

* validate_article()
* publish_article()

Knowledge Base MCP

* check_product_terminology()

---

## Future Enhancements

* Validate terminology against a style guide.
* Detect duplicate content across releases.
* Compare with previous release notes.
* Generate documentation quality metrics.
