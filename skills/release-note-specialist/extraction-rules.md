# Information Extraction Rules

## Purpose

Extract release-note-relevant information from source material.

---

# Required Information

Identify whenever available:

- Change type
- Feature name
- Description
- Customer impact
- User benefit
- Audience
- Known limitations

---

# Extraction Questions

For every change ask:

1. What changed?
2. Who is affected?
3. Why was it changed?
4. What benefit does the user receive?
5. Is the change customer-facing?

---

# Non-Customer-Facing Work

Identify internal-only changes such as:

- Refactoring
- Technical debt
- Build changes
- Test automation updates

Flag these for review rather than automatically including them.

---

# Missing Information

If critical information is missing:

Flag it explicitly.

Do not infer or create missing details.
