# File: `workflows/review-release-notes.md`

# Review Release Notes Workflow

## Purpose

Review AI-generated release notes to ensure they meet documentation quality standards before publication.

---

## Trigger

User executes

```text
/review-release-notes
```

---

## Workflow

```text
User
    │
    ▼
Review Command
    │
    ▼
Reviewer Agent
    │
    ▼
Generate Review Report
    │
    ▼
Workflow Complete
```

---

## Execution Steps

### Step 1

Load generated release notes.

Input

```text
output/artifacts/release-notes.md
```

---

### Step 2

Reviewer Agent

Perform quality review.

Checks include:

* Grammar
* Tone
* Customer language
* Markdown
* Consistency
* Technical jargon
* Internal IDs

---

### Step 3

Generate review report.

Output

```text
output/artifacts/review-report.md
```

---

## Skills Used

* customer-friendly-language/SKILL.md
* quality-review-checklist/SKILL.md
* release-note-template/SKILL.md

---

## Prompt Used

* review-release-notes.md

---

## Artifacts Produced

* review-report.md

---

## Success Criteria

* Quality review completed.
* Recommendations documented.
* Overall approval status assigned.

---

## Future Enhancements

* Automatic corrections
* Readability score
* Terminology validation
* AI quality scoring
