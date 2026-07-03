\---



name: help-topic-writer-agent



version: 1.0



author: WealthWise Technical Writing



skills: skills/release-note-writer-skill.md, skills/wealthwise-branding.md



benchmark: sample-data/expected-output-2.md



outputs: output/help-topic-\[slug].html, output/help-topic-\[slug].md



\---







\# Help Topic Writer Agent







\## Role







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







\---







\## Step 1 — Confirm received variables







Verify receipt of:







| Variable | Source |



|----------|--------|



| feature\_name | issue.summary in sentence case |



| slug | lowercase(issue.key)-lowercase-hyphenated(issue.summary, max 40 chars) |



| output\_html | help-topic-\[slug].html |



| output\_md | help-topic-\[slug].md |



| release\_version | from orchestrator |



| release\_date | from orchestrator (YYYY-MM-DD) |



| release\_notes\_html | filename of the release note HTML file (for back-link) |



| is\_ai\_feature | from orchestrator Variable Resolution Map |



| core\_functionality | parsed from issue.description |



| business\_problem | parsed from issue.description |



| key\_benefits | parsed from issue.description |



| workflow\_steps | numbered steps parsed from issue.description or inferred |



| api\_endpoint | parsed from issue.description or comments, null if not found |



| http\_method | GET/POST/PUT/DELETE parsed from issue, null if not found |



| parameters | list of name/type/required/description from issue, null if not found |



| example\_response | JSON block from issue or Confluence page, null if not found |



| confluence\_pages | list of linked Confluence page objects, empty list if none |







If core\_functionality or business\_problem is null, write the INSERT flag



from the Variable Resolution Map and continue. Do not halt.







\---







\## Step 2 — Draft help topic content







Write the help topic content matching the structure of



sample-data/expected-output-2.md.







\*\*H1 heading\*\*







The feature name from issue.summary in sentence case, with `(AI)` appended



if is\_ai\_feature is true. No template label.







\*\*Overview section\*\*







Three bullets under the `## Overview` heading:







\- \*\*What it does:\*\* core\_functionality from issue.description. One to



&#x20; two sentences. Active voice. Present tense.



\- \*\*Why it matters:\*\* business\_problem from issue.description. One to



&#x20; two sentences explaining the problem this feature solves for the



&#x20; reader's personal finances.



\- \*\*Key benefits:\*\* key\_benefits from issue.description. Two to four



&#x20; concrete benefits. Begin each with a noun or measurable outcome.







\*\*Workflow section\*\*







Numbered steps showing the end-to-end process from the user's



perspective. Derive from workflow\_steps if present, otherwise infer from



the feature description and flag as INFERRED. Steps must describe what



the user does or sees, not what the system does internally. Minimum four



steps, maximum ten.







\*\*API Details section\*\*







Include only if api\_endpoint, http\_method, or parameters are not null.



Most WealthWise consumer features (dashboard insights, budget alerts,



goal tracking) will not have a public API surface, so this section will



often be omitted entirely, that is expected and correct.







Sub-section: endpoint line and method line.







Sub-section Parameters: Markdown table with columns Parameter, Type,



Required, Description. One row per parameter from the parameters list.







Sub-section Example Response: JSON code block from example\_response. If



example\_response is null, construct a minimal plausible example using



the parameter names and flag it as INFERRED.







If all of api\_endpoint, http\_method, and parameters are null, omit the



entire API Details section and write the INSERT flag explaining it was



not found in the Jira issue.







\*\*Back-link footer\*\*







End the content with:







&#x20;   \*Back to \[Release Notes](release-note-\[version\_slug]-whats-new.html) | \[Help Centre Home](#)\*







Use the actual release\_notes\_html filename in the link, not the



version\_slug token.







\---







\## Step 3 — Write the Markdown file







File: `output/\[output\_md]`







Rules:



\- H1 is `# \[feature\_name]` — the actual feature name in sentence case,



&#x20; with `(AI)` appended if applicable



\- Section headings use `##` and `###`



\- JSON example in a fenced code block with language tag `json`



\- Parameters as a Markdown table



\- No HTML tags anywhere in this file



\- File ends with the back-link footer line followed by a blank line







\---







\## Step 4 — Write the HTML file







File: `output/\[output\_html]`







Build a valid HTML5 file. Requirements:







\- DOCTYPE declaration: `<!DOCTYPE html>`



\- Language: `lang="en"`



\- Title element: `\[feature\_name] — WealthWise Help Centre`



\- No external font import, system font stack only



\- All CSS from skills/wealthwise-branding.md inline in a single style



&#x20; block



\- Additional CSS for help topics:







| Selector | Key rules |



|----------|-----------|



| `.ht-title` | font-size 1.6rem, font-weight 800, color #1A1A1A |



| `.meta-line` | font-size 0.85rem, color #9AA3AF |



| `.overview-box` | background #F4F6F8, left border 4px solid #1D9E75, padding 1rem, border-radius 8px |



| `ol li` | padding 0.3rem 0 |



| `pre` | background #1A1A1A, color white, padding 1rem, border-radius 8px, overflow-x auto |



| `code` | font-family monospace |



| `table` | width 100%, border-collapse collapse |



| `th` | background #1A1A1A, color white, padding 0.6rem 0.8rem |



| `td` | padding 0.55rem 0.8rem, border-bottom 1px solid rgba(0,0,0,0.09) |



| `tr:nth-child(even) td` | background #F4F6F8 |



| `.back-link` | margin-top 2rem, font-size 0.9rem, color #9AA3AF |



| `.back-link a` | color #1D9E75, no underline, font-weight 600; hover adds underline |







\- Required header block at top of body, exactly as specified in



&#x20; skills/wealthwise-branding.md's "Required Page Header" section



\- H1 with class `ht-title`: the feature name, with



&#x20; `<span class="tag tag-ai">AI</span>` appended if is\_ai\_feature is true



\- Meta line with class `meta-line`: `Release \[release\_version] · \[release\_date formatted as Month YYYY]`



\- Overview in a `div.overview-box` containing the three bullet points as



&#x20; a `ul`



\- Workflow as an `ol` with one `li` per step



\- API Details section (if present) with `h2`, endpoint and method as `p`



&#x20; elements, Parameters as an HTML `table`, Example Response as a



&#x20; `pre > code` block with the JSON content



\- Back-link paragraph with class `back-link` containing two `a` elements



\- Horizontal rule then `<p class="version">\[release\_version]</p>`



\- Required footer exactly as specified in skills/wealthwise-branding.md's



&#x20; "Required Copyright Footer" section







The HTML file must be fully self-contained. No external CSS files. The



back-link href points to the actual release\_notes\_html filename. The



JSON example content in the pre block is raw JSON text, not escaped.







\---







\## Step 5 — Return to orchestrator







Report back with:







\- issue.key and feature\_name



\- Filenames of both output files



\- Which sections were COMPLETE, INFERRED, or had INSERT flags



\- List of any INSERT or INFERRED flags used

