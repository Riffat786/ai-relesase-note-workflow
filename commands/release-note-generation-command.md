---
description: Generate a clean, MSTP-compliant release note from a changelog, ticket, or list of changes. Read the source material at $ARGUMENTS and produce a formatted draft grouped under the correct release note structure (What's New or Bug Fix).
---

# Release Note Generation Command

## What This Command Does

This command takes a path to a source file as its argument — a feature
requirement, bug report, changelog, or git log — and produces a
formatted GlobalMail Pro release note draft ready for review.

It applies the Release Note Writer Skill automatically. You provide only
the path. The command does the rest.

---

## Usage

```
/generate-release-note sample-data/sample-1-input.md
/generate-release-note sample-data/sample-2-input.md
/generate-release-note path/to/your-ticket.md
```

`$ARGUMENTS` is the path to your source file.

---

## Command Prompt

Paste this entire block into Claude. Replace `$ARGUMENTS` with the path
to your source file, or paste the file content directly after the label.

```
description: Generate a clean, MSTP-compliant release note from the
source material provided.

You are applying the Release Note Writer Skill below. Read the source
material at $ARGUMENTS and generate a release note.

--- WRITER SKILL START ---

[FULL CONTENT OF skills/release-note-writer-skill.md]

--- WRITER SKILL END ---

Rules
- Classify the input as: Added (new feature), Fixed (bug fix), or
  Changed (enhancement). Map to the correct output format:
    Added   → ## What's New
    Fixed   → ## Bug Fix
    Changed → ## What's New (with enhancement framing)
- Group entries under: Added, Changed, Fixed (omit empty groups).
- Write each entry as one user-facing sentence in present tense,
  starting with a verb.
- Exclude internal-only details: merge commits, lint fixes, version
  bumps, database schema changes, cache TTL values, API endpoint names,
  infrastructure notes, and bug IDs.
- Lead with the most impactful change in each group.
- Do not start any paragraph with "Previously."
- No em dashes. Serial comma in all lists of three or more items.

Output
Output ONLY the release note in markdown. No preamble, no commentary,
no explanations. Begin with the section heading (## What's New or
## Bug Fix), then the structured content. End with the version number
after a horizontal rule.

After the release note, append exactly three lines:
Classification: [Added / Fixed / Changed]
Source: [file name or ticket ID from $ARGUMENTS]
Missing: [any [INSERT:] placeholders used, or "None"]

SOURCE FILE: $ARGUMENTS
[paste file content here if not using a path reference]
```

---

## Sample Invocations

### Feature release (sample-data/sample-1-input.md)

```
/generate-release-note sample-data/sample-1-input.md
```

Expected output format matches: `sample-data/expected-output-1.md`

### Bug fix (sample-data/sample-2-input.md)

```
/generate-release-note sample-data/sample-2-input.md
```

Expected output format matches: `sample-data/expected-output-2.md`

### Real ticket

```
/generate-release-note path/to/gm-feat-302-confidence-scoring.md
```

---

## What Good Output Looks Like

For a feature input, the agent returns:

```markdown
## What's New

### [Feature name in sentence case]

[One to two sentences: what the previous approach was, then what
is new. Past tense for before, present tense for after.]

**What you need to do**

[Action required, or: No configuration changes are required.]

**Benefits**

- [Verb-first benefit — user value only]
- [Verb-first benefit]
- [Two to four bullets maximum]

---

1.1
```

For a bug fix input, the agent returns:

```markdown
## Bug Fix

### [Issue title in sentence case]

[Paragraph 1: what the user saw before. Past tense. No bug ID.]

[Paragraph 2: what is resolved. Present tense. No backend details.]

---

1.1
```

---

## What the Command Excludes

The agent will not include in its output:
- Bug IDs, ticket numbers, or severity labels
- Database changes, cache values, or infrastructure notes
- Performance tables with before/after percentages
- Installation instructions or dependency lists
- Known issues sections
- The product name "GlobalMail Pro" in body prose

If the source file contains these, the agent silently drops them and
uses only the user-facing behaviour change.

---

## Next Step

Pass the draft to the review command:
`commands/release-note-review-command.md`

Or run the full agent end-to-end:
`run/run.sh sample1` or `run/run.sh sample2`
