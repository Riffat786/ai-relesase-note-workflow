---



description: Single-command trigger for the full WealthWise release note automation pipeline. Paste or run this command in Claude Code to generate release notes and help topics from Jira without any further user input.

data_source: Atlassian Jira — project WealthWiseReleaseDemo (key - WW)

jira_board_url: "https://wealthwise-release-demo.atlassian.net/jira/software/projects/WW/list?jql=project+%3D+WW+ORDER+BY+cf%5B10019%5D+ASC"

mcp_required: atlassian (configured in .mcp.json)

outputs: output/release-note-[version]-whats-new.html, output/release-note-[version]-whats-new.md, output/help-topic-[slug].html       (one per What's New feature), output/help-topic-[slug].md         (one per What's New feature), output/release-note-review-report.md



---



# Release Note Generation — Single Trigger Command



## How to Use



In Claude Code, run this command:



```

/project:generate-release-notes

```



Or paste the prompt below directly into Claude Code. No further input

is required. The pipeline runs to completion automatically.



---



## Trigger Prompt



```

Run the WealthWise release note automation pipeline from start to

finish. Do not pause for input at any point.



Prerequisites (verify before starting):

1. The Atlassian MCP server is connected (.mcp.json is present and

   the Atlassian MCP at https://mcp.atlassian.com/sse is authenticated).

2. The output/ directory exists and is writable.



Execute these steps in order:



STEP 1 — Read agents/release-note-orchestrator.md in full.

STEP 2 — Follow every instruction in that file exactly as written.

STEP 3 — Do not skip any step. Do not ask the user for clarification.

STEP 4 — If a non-critical step fails, log it and continue.

         If the Jira MCP fetch fails, halt and show the error.



When complete, display the pipeline summary block from the orchestrator

(the PIPELINE COMPLETE section) and list all output files created.

```



---



## What This Command Does



1. **Connects to Atlassian Jira** via MCP and fetches all issues in the

   **WealthWiseReleaseDemo** project (key: `WW`) using JQL:

   `project = WW ORDER BY cf[10019] ASC`

   Replace the placeholder board URL in `agents/release-note-orchestrator.md`

   with your team's real Jira instance before running against production data.



2. **Classifies issues** into: What's New, Enhancements, Bug Fixes,

   Known Issues — the fixed four-category set defined in

   `skills/wealthwise-branding.md`.



3. **Generates the consolidated release note** (HTML + Markdown) covering

   all classified issues, with hyperlinks from What's New entries to

   their help topics.



4. **Generates a help topic** (HTML + Markdown) for each What's New

   feature, following the template in `sample-data/expected-output-2.md`.



5. **Runs quality review** applying:

   - Writing-standards checklist (`skills/release-note-reviewer-skill.md`)

   - Structure benchmark compliance (`sample-data/expected-output-1.md`,

     `sample-data/expected-output-2.md`)

   - WealthWise branding rules (`skills/wealthwise-branding.md`)

   - Hyperlink integrity checks

   - Bug Fixes table column-count check (must be exactly three columns)



6. **Auto-fixes** all High and Medium severity findings.



7. **Writes output files** to `output/` directory.



---



## Setup (First-Time Only)



Before running this command for the first time:



### 1. Connect the Atlassian MCP server



In Claude Code, add the Atlassian MCP:



```bash

# Option A — Claude Code CLI

claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse



# Option B — Verify .mcp.json is present (already in this repo)

cat .mcp.json

```



When Claude Code first connects, it will open an Atlassian OAuth

browser window. Sign in with your Atlassian account (the account that

has access to your team's Jira instance). Do not paste your API token

into any configuration file.



### 2. Verify Jira access



After connecting, confirm access to the WealthWiseReleaseDemo project

(or your team's real project, once the placeholder URL is replaced):



```

Check that the Atlassian MCP can search issues in the WealthWiseReleaseDemo

project (WW).



Test JQL: project = WW ORDER BY cf[10019] ASC

```



### 3. Create the output directory (if it does not exist)



```bash

mkdir -p output

```



---



## Output Files Reference



| File                                          | Format   | Contents                          |

|-------------------------------------------------|----------|------------------------------------|

| output/release-note-[version]-whats-new.html      | HTML     | Full branded release note          |

| output/release-note-[version]-whats-new.md        | Markdown | Version-controlled release note    |

| output/help-topic-[slug].html                     | HTML     | Branded help topic per What's New feature |

| output/help-topic-[slug].md                       | Markdown | Help topic per What's New feature   |

| output/release-note-review-report.md              | Markdown | QA review findings and auto-fix log|



WealthWise release notes do not include a JSON output file — see

`skills/wealthwise-branding.md`, Dual Output Rule.



---



## Troubleshooting



| Symptom                          | Likely cause                  | Fix                                       |

|-----------------------------------|--------------------------------|---------------------------------------------|

| "Atlassian MCP not connected"      | MCP not added or authenticated | Run `claude mcp add atlassian ...` above  |

| Empty issue lists                  | JQL returns no results         | Check WealthWiseReleaseDemo project has issues in Jira |

| Help topic link broken             | Slug mismatch                  | Re-run pipeline (auto-fixed after review) |

| Bug Fixes table has extra columns  | Writer agent error             | Check review report for RN-S7 finding      |

| No output files created            | output/ directory missing      | Run `mkdir -p output`                      |
