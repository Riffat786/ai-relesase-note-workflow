---

description: Standalone review command for release notes and help topics already in the output/ directory. Use this to re-run QA on existing output files without regenerating them. For a full regenerate + review, use release-note-generation-command.md instead.
inputs: output/release-notes-[version].html, output/release-notes-[version].md, output/release-notes-[version].json, output/help-topic-[slug].html       (all present in output/), output/help-topic-[slug].md         (all present in output/)
outputs: output/release-note-review-report.md

---

# Release Note Review — Standalone Command

## How to Use

Run this when you want to re-review files already in `output/` without
re-fetching Jira data or re-generating content.

Paste this prompt into Claude Code:

```
Run the release note quality review on existing output files.

STEP 1 — Read agents/release-note-reviewer-agent.md in full.
STEP 2 — List all files currently in the output/ directory.
STEP 3 — Run the full reviewer agent on all release note and help topic
          files found in output/. Do not regenerate any files.
STEP 4 — Write output/release-note-review-report.md with findings.
STEP 5 — Report which High and Medium findings require manual correction
          (note: this command does not auto-apply fixes — for auto-fix,
          use the full generation command).
```

---

## Skills Applied

- `skills/release-note-reviewer-skill.md` — 22-point checklist + style audit
- `skills/branding-style-guide.md` — Branding compliance checks
- `sample-data/expected-output-1.md` — Release notes structure benchmark
- `sample-data/expected-output-2.md` — Help topic structure benchmark
