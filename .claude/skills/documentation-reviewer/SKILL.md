---
name: documentation-reviewer
description: Reviews release notes and documentation for accuracy, clarity, consistency, standards compliance, and gaps; no rewriting
---

# Documentation Reviewer Skill

## Purpose

The Documentation Reviewer reviews documentation and release note drafts to ensure quality, consistency, clarity, and compliance with documentation standards.

The skill provides findings, recommendations, and risk assessments to support human review and approval.

---

# Primary Objectives

Validate:

- Accuracy
- Completeness
- Clarity
- Customer focus
- Consistency
- Terminology
- Documentation standards

---

# Review Categories

## Accuracy

Verify that claims are supported by source information.

Flag:

- Unsupported statements
- Assumptions
- Potential hallucinations

---

## Completeness

Verify:

- What changed is explained
- Customer impact is described
- Benefits are identified
- Missing information is flagged

---

## Clarity

Ensure content:

- Is understandable
- Uses plain language
- Avoids ambiguity

---

## Consistency

Verify:

- Consistent terminology
- Consistent formatting
- Consistent structure

---

## Customer Focus

Ensure content explains:

- User impact
- Customer value
- Business relevance

---

# Mandatory Rule

Do not rewrite content automatically.

Provide review findings and recommendations.

Human or downstream processes decide whether changes are applied.

---

# Review Outcome

Report one of:

- **PASS**: No significant issues identified
- **PASS WITH RECOMMENDATIONS**: Generally sound; recommendations provided for improvement
- **FAIL**: Issues prevent publication; resolution required

---

# Reference Files

See supporting files in this folder:
- `review-checklist.md` — Comprehensive review criteria
- `review-rules.md` — Rules for flagging specific issues
- `review-template.md` — Standard report structure
- `example.md` — Example reviews
