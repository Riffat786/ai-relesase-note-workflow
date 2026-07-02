---
name: release-note-metadata
description: Applies metadata required for Document360 draft articles.
version: 1.0.0
---

# Release Note Metadata

## Purpose

Populate metadata required for Document360 draft creation.
Provide a consistent metadata standard for release notes created by the AI workflow.

This skill ensures that every generated draft contains the required information before entering the human review process.

---

## Metadata

Include:

- Article Title
- Release Version
- Release Date
- Product
- Category
- Tags
- Audience
- Status
- AI Quality Check
- Technical Writer Review Status
- SME Review Status
- Documentation Approval Status

## Rules

Always set:

- Status = Draft
- Publication = Manual Approval Required

Never publish automatically.
---

## Required Metadata

### Product

Example

```text
My Product
```

---

### Release Version

Example

```text
2025.8
```

---

### Publication Status

For AI-generated content

```text
Draft
```

---

### Category

Example

```text
Release Notes
```

---

### Tags

Examples

```text
Release

Release Notes

2025.8

Product Name
```

---

### Author

Example

```text
AI Draft Generator
```

---

### Reviewer

Example

```text
Technical Writer
```

---

### SME

Example

```text
Subject Matter Expert
```

---

## Metadata Rules

Always:

* Populate all required metadata.
* Set publication status to **Draft**.
* Leave publication date empty until approval.
* Do not assign Published status.

---

## Future Document360 Mapping

| Metadata        | Document360 Field |
| --------------- | ----------------- |
| Product         | Category          |
| Release Version | Version           |
| Status          | Workflow Status   |
| Tags            | Tags              |
| Author          | Article Owner     |

---

## Success Criteria

Every draft created by the Draft Generator Agent contains complete metadata and is ready for Technical Writer review before publication.
