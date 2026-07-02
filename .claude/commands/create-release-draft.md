# File: `.claude/commands/create-release-draft.md`

# /create-release-draft

## Purpose

Create a Document360-ready draft from the reviewed release notes.

The purpose of this command is to prepare a release note article that follows the organization's Document360 release note template and is ready for Technical Writer review.

This command does **not** publish documentation.

---

## Input

Reviewed release note artifacts.

```text
output/artifacts/ai/release-notes.md

output/artifacts/ai/review-report.md
```

---

## Instructions

### Step 1 — Read the Release Notes

Read:

```text
output/artifacts/ai/release-notes.md
```

---

### Step 2 — Read the Review Report

Read:

```text
output/artifacts/ai/review-report.md
```

Verify that the AI Quality Check has passed before creating the draft.

---

### Step 3 — Use the Prompt

Use:

```text
.claude/prompts/create-document360-draft.md
```

---

### Step 4 — Apply Skills

Apply the following skills:

```text
.claude/skills/release-note-template/SKILL.md

.claude/skills/release-note-metadata/SKILL.md
```

---

### Step 5 — Create the Document360 Draft

Generate a draft article using the approved release note template.

The draft should:

* Apply the release note template.
* Populate article metadata.
* Include release information.
* Preserve internal work item IDs.
* Include the AI review status.
* Set the article status to **Draft**.
* Never publish automatically.

---

## Draft Requirements

The generated Document360 draft must include:

### Article Metadata

Include:

* Article Title
* Release Version
* Release Date
* Category
* Tags
* Audience
* Document Status (Draft)

---

### Article Content

Include:

* Overview
* New Features
* Enhancements
* Bug Fixes
* Recommended Actions (if applicable)
* Known Limitations (if applicable)

---

### Review Information

Include:

* AI Quality Check Status
* Technical Writer Review Status
* SME Review Status
* Documentation Approval Status

---

### Publishing Information

Include:

* Document360 Status: Draft
* Ready for Technical Writer Review
* Publication: Manual Approval Required

---

## Output

Create:

```text
output/artifacts/publishing/document360-draft.md
```

---

## Expected Summary

Display:

```text
Document360 Draft Created Successfully

AI Quality Check: PASSED

Draft Status: Ready for Technical Writer Review

Artifact:

output/artifacts/publishing/document360-draft.md
```

---

## Success Criteria

The command is successful when:

* The release notes have been transformed into a Document360-ready draft.
* The release note template has been applied.
* Metadata has been populated.
* The AI Quality Check has been included.
* The document status has been set to Draft.
* The draft has been saved to:

```text
output/artifacts/publishing/document360-draft.md
```

No publication should be performed by this command.

Publication remains the responsibility of the Technical Writer and SME.
