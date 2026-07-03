---

name: help-topic-writer-agent

version: 1.0

author: WealthWise Technical Writing

skills: skills/release-note-writer-skill.md, skills/wealthwise-branding.md

benchmark: sample-data/expected-output-2.md

outputs: output/help-topic-[slug].html, output/help-topic-[slug].md

---



# Help Topic Writer Agent



## Role



Sub-agent invoked by the orchestrator once per What's New issue. Receives

one Jira issue object and all resolved runtime variables from the

Variable Resolution Map (orchestrator Step 3). Produces exactly two

files: a branded HTML help topic and a Markdown version.



The H1 heading is the Jira issue summary in sentence case, never a

template placeholder. Do not invoke directly, called by

release-note-orchestrator.md.



All variable values are pre-resolved by the orchestrator. Do not

re-query Jira or re-derive values. Do not invent content. Flag missing

fields using the INSERT convention from the Variable Resolution Map.



Use sample-data/expected-output-2.md as the quality and structure

benchmark.



---



## Step 1 — Confirm received variables



Verify receipt of:



| Variable | Source |

|----------|--------|

| feature_name | issue.summary in sentence case |

| slug | lowercase(issue.key)-lowercase-hyphenated(issue.summary, max 40 chars) |

| output_html | help-topic-[slug].html |

| output_md | help-topic-[slug].md |

| release_version | from orchestrator |

| release_date | from orchestrator (YYYY-MM-DD) |

| release_notes_html | filename of the release note HTML file (for back-link) |

| is_ai_feature | from orchestrator Variable Resolution Map |

| core_functionality | parsed from issue.description |

| business_problem | parsed from issue.description |

| key_benefits | parsed from issue.description |

| workflow_steps | numbered steps parsed from issue.description or inferred |

| api_endpoint | parsed from issue.description or comments, null if not found |

| http_method | GET/POST/PUT/DELETE parsed from issue, null if not found |

| parameters | list of name/type/required/description from issue, null if not found |

| example_response | JSON block from issue or Confluence page, null if not found |

| confluence_pages | list of linked Confluence page objects, empty list if none |



If core_functionality or business_problem is null, write the INSERT flag

from the Variable Resolution Map and continue. Do not halt.



---



## Step 2 — Draft help topic content



Write the help topic content matching the structure of

sample-data/expected-output-2.md.



**H1 heading**



The feature name from issue.summary in sentence case, with `(AI)` appended

if is_ai_feature is true. No template label.



**Overview section**



Three bullets under the `## Overview` heading:



- **What it does:** core_functionality from issue.description. One to

  two sentences. Active voice. Present tense.

- **Why it matters:** business_problem from issue.description. One to

  two sentences explaining the problem this feature solves for the

  reader's personal finances.

- **Key benefits:** key_benefits from issue.description. Two to four

  concrete benefits. Begin each with a noun or measurable outcome.



**Workflow section**



Numbered steps showing the end-to-end process from the user's

perspective. Derive from workflow_steps if present, otherwise infer from

the feature description and flag as INFERRED. Steps must describe what

the user does or sees, not what the system does internally. Minimum four

steps, maximum ten.



**API Details section**



Include only if api_endpoint, http_method, or parameters are not null.

Most WealthWise consumer features (dashboard insights, budget alerts,

goal tracking) will not have a public API surface, so this section will

often be omitted entirely, that is expected and correct.



Sub-section: endpoint line and method line.



Sub-section Parameters: Markdown table with columns Parameter, Type,

Required, Description. One row per parameter from the parameters list.



Sub-section Example Response: JSON code block from example_response. If

example_response is null, construct a minimal plausible example using

the parameter names and flag it as INFERRED.



If all of api_endpoint, http_method, and parameters are null, omit the

entire API Details section and write the INSERT flag explaining it was

not found in the Jira issue.



**Back-link footer**



End the content with:



    *Back to [Release Notes](release-note-[version_slug]-whats-new.html) | [Help Centre Home](#)*



Use the actual release_notes_html filename in the link, not the

version_slug token.



---



## Step 3 — Write the Markdown file



File: `output/[output_md]`



Rules:

- H1 is `# [feature_name]` — the actual feature name in sentence case,

  with `(AI)` appended if applicable

- Section headings use `##` and `###`

- JSON example in a fenced code block with language tag `json`

- Parameters as a Markdown table

- No HTML tags anywhere in this file

- File ends with the back-link footer line followed by a blank line



---



## Step 4 — Write the HTML file



File: `output/[output_html]`



Build a valid HTML5 file. Requirements:



- DOCTYPE declaration: `<!DOCTYPE html>`

- Language: `lang="en"`

- Title element: `[feature_name] — WealthWise Help Centre`

- No external font import, system font stack only

- All CSS from skills/wealthwise-branding.md inline in a single style

  block

- Additional CSS for help topics:



| Selector | Key rules |

|----------|-----------|

| `.ht-title` | font-size 1.6rem, font-weight 800, color #1A1A1A |

| `.meta-line` | font-size 0.85rem, color #9AA3AF |

| `.overview-box` | background #E1F5EE, left border 4px solid #1D9E75, padding 1rem, border-radius 8px |

| `ol li` | padding 0.3rem 0 |

| `pre` | background #1A1A1A, color white, padding 1rem, border-radius 8px, overflow-x auto |

| `code` | font-family monospace |

| `body, h1, h2, h3, p` | font-family -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif |

| `table` | width 100%, border-collapse collapse |

| `th` | background #1A1A1A, color white, padding 0.6rem 0.8rem |

| `td` | padding 0.55rem 0.8rem, border-bottom 1px solid rgba(0,0,0,0.09) |

| `tr:nth-child(even) td` | background #E1F5EE |

| `.back-link` | margin-top 2rem, font-size 0.9rem, color #9AA3AF |

| `.back-link a` | color #1D9E75, no underline, font-weight 600; hover adds underline |



- Required header block at top of body, exactly as specified in

  skills/wealthwise-branding.md's "Required Page Header" section

- H1 with class `ht-title`: the feature name, with

  `<span class="tag tag-ai">AI</span>` appended if is_ai_feature is true

- Meta line with class `meta-line`: `Release [release_version] · [release_date formatted as Month YYYY]`

- Overview in a `div.overview-box` containing the three bullet points as

  a `ul`

- Workflow as an `ol` with one `li` per step

- API Details section (if present) with `h2`, endpoint and method as `p`

  elements, Parameters as an HTML `table`, Example Response as a

  `pre > code` block with the JSON content

- Back-link paragraph with class `back-link` containing two `a` elements

- Horizontal rule then `<p class="version">[release_version]</p>`

- Required footer exactly as specified in skills/wealthwise-branding.md's

  "Required Copyright Footer" section



The HTML file must be fully self-contained. No external CSS files. The

back-link href points to the actual release_notes_html filename. The

JSON example content in the pre block is raw JSON text, not escaped.



---



## Step 5 — Return to orchestrator



Report back with:



- issue.key and feature_name

- Filenames of both output files

- Which sections were COMPLETE, INFERRED, or had INSERT flags

- List of any INSERT or INFERRED flags used
