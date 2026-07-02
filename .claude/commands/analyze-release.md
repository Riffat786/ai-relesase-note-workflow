# File: `.claude/commands/analyze-release.md`

# /analyze-release

## Purpose

Analyze the collected release data and prepare a structured representation for release note generation.

The purpose of this command is to identify customer-facing changes and organize them into logical categories.

This command does **not** generate release notes.

---

## Input

Collected release data.

```text
output/artifacts/ai/collected-release-data.json
```

---

## Instructions

1. Read:

```text
output/artifacts/ai/collected-release-data.json
```

2. Use the prompt:

```text
.claude/prompts/analyze-release.md
```

3. Apply the skill:

```text
.claude/skills/classify-release-items/SKILL.md
```

4. Analyze every work item.

5. Classify work items into:

* Features
* Enhancements
* Bug Fixes

6. Preserve internal IDs.

7. Preserve titles.

8. Preserve descriptions.

9. Exclude work items that are not customer-facing.

10. Generate a structured JSON file.

---

## Output

Create:

```text
output/artifacts/ai/analyzed-release.json
```

---

## Expected Summary

Display:

```text
Release 2025.8 Analysis Complete

Features: X

Enhancements: X

Bug Fixes: X

Artifact:

output/artifacts/ai/analyzed-release.json
```

---

## Success Criteria

The command is successful when:

* The collected release data has been analyzed.
* All customer-facing work items have been categorized.
* Non-customer-facing work has been excluded.
* The structured JSON has been saved.
* No release notes have been generated.
