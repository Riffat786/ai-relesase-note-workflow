# File: `.claude/commands/write-release-notes.md`

# /write-release-notes

## Purpose

Generate customer-facing release notes from the analyzed release data.

This command transforms structured release information into professionally written release notes using the organization's release note template.

This command does **not** review the release notes or prepare the Document360 draft.

---

## Input

Analyzed release data.

```text
output/artifacts/ai/analyzed-release.json
```

---

## Instructions

1. Read:

```text
output/artifacts/ai/analyzed-release.json
```

2. Use the prompt:

```text
.claude/prompts/write-release-notes.md
```

3. Apply the following skills:

```text
.claude/skills/customer-friendly-language/SKILL.md

.claude/skills/release-note-template/SKILL.md
```

4. Generate customer-facing release notes.

5. Preserve the categorized structure from the analyzed release data.

6. Include:

* Release version
* Overview
* New Features
* Enhancements
* Bug Fixes

7. Include the internal work item IDs for traceability.

8. Preserve the customer impact identified by the Analyzer Agent.

9. Use clear, concise, professional language suitable for customers and administrators.

10. Generate the release notes as Markdown.

---

## Output

Create:

```text
output/artifacts/ai/release-notes.md
```

---

## Requirements

The generated release notes must:

* Use customer-friendly language.
* Maintain a professional and concise tone.
* Follow Markdown formatting.
* Follow the approved release note template.
* Include internal work item IDs.
* Preserve technical accuracy.
* Be suitable for customer publication after review.

---

## Expected Sections

```text
# Release 2025.8

## Overview

## New Features

## Enhancements

## Bug Fixes

## Known Limitations (if applicable)

## Recommended Actions (if applicable)
```

---

## Expected Summary

Display:

```text
Release Notes Generated Successfully

Release: 2025.8

Features: 2

Enhancements: 1

Bug Fixes: 2

Artifact:

output/artifacts/ai/release-notes.md
```

---

## Success Criteria

The command is successful when:

* The analyzed release data has been read.
* Release notes have been generated in Markdown.
* The release note template has been applied.
* Internal IDs have been included.
* The output has been saved to:

```text
output/artifacts/ai/release-notes.md
```

No review or publishing actions should be performed by this command.
