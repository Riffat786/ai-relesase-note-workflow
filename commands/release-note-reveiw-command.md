---



description: Standalone review command for release notes and help topics already in the output/ directory. Use this to re-run QA on existing output files without regenerating them. For a full regenerate + review, use release-note-generation-command.md instead.

inputs: output/release-note-[version]-whats-new.html, output/release-note-[version]-whats-new.md, output/help-topic-[slug].html       (all present in output/), output/help-topic-[slug].md         (all present in output/)

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



- `skills/release-note-reviewer-skill.md` — writing-standards checklist,

  structure checks, style audit

- `skills/wealthwise-branding.md` — branding compliance checks

- `sample-data/expected-output-1.md` — release notes structure benchmark

- `sample-data/expected-output-2.md` — help topic structure benchmark



---



## When to Use This Instead of the Full Generation Command



| Scenario | Use this command | Use the generation command |

|---|---|---|

| Content already drafted, want a fresh QA pass | ✓ | |

| A human editor hand-edited an output file and wants it re-checked | ✓ | |

| Jira has new issues not yet reflected in output/ | | ✓ |

| No files exist yet in output/ | | ✓ |



---



## Troubleshooting



| Symptom                          | Likely cause                          | Fix                                             |

|-----------------------------------|-----------------------------------------|---------------------------------------------------|

| "No files found in output/"        | Pipeline has not been run yet           | Run `commands/release-note-generation-command.md` first |

| Review report missing a file       | File in output/ does not match expected naming | Confirm filenames follow the convention in `skills/wealthwise-branding.md` |

| Findings reference a stale benchmark | expected-output-1/2.md edited after last run | Re-read the benchmark files before scoring |
