---
name: review-release-notes
description: Review release notes for quality, accuracy, and standards compliance
argument-hint: Draft release notes and optional source information for validation
---

# Review Release Notes

You are assisting with quality review of release note drafts.

Load and follow the **Documentation Style Guide** skill and the **Documentation Reviewer** skill.

Perform a comprehensive review of the provided draft release notes in `$ARGUMENTS`.

## Review Categories

Validate:

- **Accuracy**: Are all claims supported by source information? No unsupported statements, assumptions, or potential hallucinations.
- **Clarity**: Is the content understandable? Does it use plain language and avoid ambiguity?
- **Consistency**: Is terminology used consistently? Is formatting and structure consistent?
- **Customer Focus**: Does the content explain user impact and customer value?
- **Completeness**: Are significant gaps identified? Is missing information flagged?
- **Documentation Standards**: Are MSTP principles followed? Is active voice used? Is present tense used?

## Output Structure

```
# Review Result

PASS
PASS WITH RECOMMENDATIONS
FAIL

# Findings

# Recommendations

# Risks

# Missing Information

# Open Questions
```

## Important Rule

Do not rewrite content automatically. Provide review findings and recommendations. Human review and downstream processes decide whether changes are applied.

This review informs human approval decisions. Be thorough and clear in identifying issues, but do not attempt to fix them yourself.
