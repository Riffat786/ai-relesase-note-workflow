---
description: Review a release note draft against the GlobalMail Pro style guide and the 22-point reviewer checklist. Report violations in a scored table. Read the draft at $ARGUMENTS.
---

# Release Note Review Command

## What This Command Does

This command takes a path to a draft release note as its argument and
reviews it against the GlobalMail Pro style guide and the 22-point
Reviewer Skill checklist. It reports violations in a scored table
and provides a summary with the top improvements ranked by reader impact.

It does not edit the document. It reports findings only.

---

## Usage

```
/review-release-note output/release-note-1-1-whats-new.html
/review-release-note output/release-note-1-1-dashboard-metrics-fix.html
/review-release-note path/to/your-draft.md
```

`$ARGUMENTS` is the path to the draft to review.

To review against the source input for accuracy, provide both paths
separated by a space:

```
/review-release-note output/draft.md sample-data/sample-1-input.md
```

---

## Command Prompt

Paste this entire block into Claude. Replace `$ARGUMENTS` with the path
to the draft (and optionally the source input path).

```
---
description: Review a document against the GlobalMail Pro style guide
and the reviewer checklist. Report violations in a scored table.
---

You are a technical editor enforcing the GlobalMail Pro style guide.
You are applying the Release Note Reviewer Skill below.

--- REVIEWER SKILL START ---

[FULL CONTENT OF skills/release-note-reviewer-skill.md]

--- REVIEWER SKILL END ---

Review: $ARGUMENTS

## Checklist

Run every check below. Mark each as ✅ PASS, ⚠️ NEEDS WORK, or ❌ FAIL.

Style guide checks (7):
1. Active voice — the subject performs the action
2. Present tense — describe what the software does now
3. Second person — address the reader as "you"
4. Sentence length — under 25 words per sentence
5. Sentence-case headings — capitalise only the first word and proper nouns
6. Code formatting — backticks on parameter names, file paths, status codes,
   and product feature names where applicable
7. Jargon — defined on first use or avoided entirely

Release note format checks (from Reviewer Skill):
Run all 22 checks from the Reviewer Skill above (F1–F7, S1–S10,
C1–C5, CL1–CL2, B1). Report each in the results table.

## Constraints

- Do NOT edit the document.
- Report findings only. Do not rewrite.
- Flag every violation, regardless of severity.
- If a source input path is provided as the second argument, check
  factual accuracy against it (check C3).

## Output

First, the style guide score table:

| # | Criterion | Status | Finding | Action |
|---|-----------|--------|---------|--------|
| 1 | Active voice | ✅ / ⚠️ / ❌ | [specific finding] | [specific action] |
| 2 | Present tense | | | |
| 3 | Second person | | | |
| 4 | Sentence length | | | |
| 5 | Sentence-case headings | | | |
| 6 | Code formatting | | | |
| 7 | Jargon | | | |

Status options: ✅ PASS  |  ⚠️ NEEDS WORK  |  ❌ FAIL

Then, the 22-check reviewer skill table:

| ID | Check | Result | Severity |
|----|-------|--------|----------|
| F1 | Correct header | PASS/FAIL/N/A | — |
[all 22 rows — do not skip any]

## Summary

- Style guide score: X of 7 criteria met
- Reviewer skill score: X of 22 checks passed (X High, X Medium, X Low failures)
- Top 3 improvements ranked by impact on the reader:
  1. [highest impact — specific finding and suggested fix]
  2. [second — specific finding and suggested fix]
  3. [third — specific finding and suggested fix]
- Overall recommendation: PASS / NEEDS REVISION / RETURN TO WRITER

DRAFT TO REVIEW: $ARGUMENTS
[paste draft content here if not using a path reference]
```

---

## Sample Invocations

### Review a generated feature release note

```
/review-release-note output/release-note-1-1-whats-new.html
                     sample-data/sample-1-input.md
```

The second argument gives the reviewer the source input for factual
accuracy checking (check C3).

Expected benchmark: `sample-data/expected-output-1.md`

### Review a generated bug fix

```
/review-release-note output/release-note-1-1-dashboard-metrics-fix.html
                     sample-data/sample-2-input.md
```

Expected benchmark: `sample-data/expected-output-2.md`

### Review any markdown draft

```
/review-release-note path/to/my-draft.md
```

---

## What the Review Report Contains

**Style guide table (7 rows)**
One row per style criterion. Status, specific finding, and a concrete
action for every ⚠️ NEEDS WORK or ❌ FAIL.

**Reviewer skill table (22 rows)**
One row per check ID (F1–F7, S1–S10, C1–C5, CL1–CL2, B1). No rows
skipped. Every failure includes the violating text.

**Summary**
- Style guide score out of 7
- Reviewer skill score out of 22, with High/Medium/Low breakdown
- Top 3 improvements ranked by reader impact — specific, actionable,
  not generic
- Overall recommendation: PASS, NEEDS REVISION, or RETURN TO WRITER

---

## After the Review

| Result | Action |
|--------|--------|
| PASS — 0 High, 0 Medium | Send to human technical reviewer (workflow step 6) |
| NEEDS REVISION — Medium or Low only | Apply fixes, commit to GitLab |
| RETURN TO WRITER — any High | Re-run generation command with corrected source input |

---

## Running Generation and Review Together

The full agent (`run/run.sh`) runs generation, review, auto-fix, and
HTML rendering in one command. Use the individual commands when you
want a manual checkpoint between generating and reviewing.

```bash
# Full automated run (both generation and review)
./run/run.sh sample1

# Manual: generate first, then review separately
/generate-release-note sample-data/sample-1-input.md
# → review the draft output
/review-release-note output/release-note-1-1-whats-new.html \
                     sample-data/sample-1-input.md
```
