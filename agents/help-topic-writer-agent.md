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

| slug | Pre-resolved by orchestrator. Format: `[issue.number]-[lowercase-hyphenated-title, max 40 chars]`. Example: `1-ai-financial-advisor-chat`. NO "#" character. |

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



Build a valid HTML5 file with complete WealthWise branding compliance. Requirements:



### Document structure
- DOCTYPE declaration: `<!DOCTYPE html>`
- Language: `lang="en"`
- Title element: `[feature_name] — WealthWise Help Centre`
- Encoding: UTF-8
- Viewport meta tag for responsive scaling

### CSS — COMPLETE REQUIRED STYLE BLOCK

**CRITICAL:** Every help topic HTML file must include ALL of the following CSS rules inline in a single `<style>` block. Do not omit, abbreviate, or simplify any of these rules. This is what ensures visual consistency across all help topics.

| Selector | Required CSS rules | Purpose |
|----------|-------------------|---------|
| `body` | `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;` `font-size: 16px;` `line-height: 1.7;` `color: #1A1A1A;` `background: #FFFFFF;` `max-width: 760px;` `margin: 0 auto;` `padding: 2rem 1.5rem 4rem;` | Base typography and layout |
| `h1` | `font-size: 1.6rem;` `font-weight: 800;` `color: #0F6E56;` `letter-spacing: -0.3px;` `margin: 0 0 0.5rem;` | Feature title (WW Navy, weight 800) |
| `h2` | `font-size: 1.3rem;` `font-weight: 700;` `color: #1D9E75;` `border-bottom: 3px solid #1D9E75;` `padding-bottom: 0.4rem;` `margin: 2rem 0 1rem;` | Section headings (WW Green with underline) |
| `h3` | `font-size: 1.02rem;` `font-weight: 600;` `color: #5A6475;` `margin: 1.5rem 0 0.75rem;` | Subheadings (WW Gray) |
| `p` | `margin-bottom: 1rem;` `color: #1A1A1A;` | Paragraph spacing and color |
| `strong` | `font-weight: 700;` `color: #1A1A1A;` | Bold text |
| `ul` | `list-style: none;` `padding: 0;` `margin: 0.5rem 0 1rem;` | Unordered list reset |
| `ul li` | `padding: 0.3rem 0 0.3rem 1.25rem;` `position: relative;` `color: #1A1A1A;` | List item spacing and padding |
| `ul li::before` | `content: '';` `position: absolute;` `left: 0;` `top: 0.7rem;` `width: 7px;` `height: 7px;` `border-radius: 50%;` `background: #1D9E75;` | WW Green bullet points (custom) |
| `ol` | `margin-left: 1.5rem;` `margin-bottom: 1rem;` | Ordered list spacing |
| `ol li` | `margin-bottom: 0.75rem;` | Ordered list item spacing |
| `hr` | `border: none;` `border-top: 1px solid rgba(0,0,0,0.09);` `margin: 1.5rem 0 0.75rem;` | Horizontal rule styling |
| `.version` | `font-size: 0.85rem;` `color: #9AA3AF;` `font-weight: 600;` | Release version meta line |
| `.tag` | `display: inline-flex;` `align-items: center;` `gap: 4px;` `padding: 2px 9px;` `border-radius: 20px;` `font-size: 0.72rem;` `font-weight: 700;` `margin-left: 0.4rem;` `vertical-align: middle;` | AI tag container |
| `.tag-ai` | `background-color: #534AB7;` `color: white;` | AI purple badge (WW Purple) |
| `.tag-security` | `background: #FCEBEB;` `color: #A32D2D;` | Security badge (if needed) |
| `.tag-deprecated` | `background: #FAEEDA;` `color: #BA7517;` | Deprecated badge (if needed) |
| `.rn-header` | `background: #1D9E75;` `color: #FFFFFF;` `padding: 1rem 1.5rem;` `margin: -2rem -1.5rem 2rem;` `display: flex;` `align-items: center;` `gap: 0.75rem;` `border-radius: 0 0 12px 12px;` | WealthWise branding header (WW Green background) |
| `.rn-header .product-name` | `font-size: 1rem;` `font-weight: 700;` `color: #FFFFFF;` | Product name in header |
| `.rn-header .header-rule` | `font-size: 0.85rem;` `color: rgba(255,255,255,0.55);` | Divider in header |
| `.rn-known-issue` | `background: #FAEEDA;` `border: 1px solid #BA7517;` `border-radius: 12px;` `padding: 1rem 1.25rem;` `margin: 1rem 0;` | Known issue callout box |
| `.rn-footer` | `margin-top: 3rem;` `padding-top: 1rem;` `border-top: 1px solid rgba(0,0,0,0.09);` `font-size: 0.8rem;` `color: #9AA3AF;` `text-align: center;` | Footer styling |
| `a` | `color: #1D9E75;` `text-decoration: none;` `font-weight: 600;` | Links (WW Green) |
| `a:hover` | `text-decoration: underline;` | Link hover state |
| `pre` | `background: #1A1A1A;` `color: white;` `padding: 1rem;` `border-radius: 8px;` `overflow-x: auto;` | Code block styling (for API examples) |
| `code` | `font-family: monospace;` | Inline code font |
| `table` | `width: 100%;` `border-collapse: collapse;` | Parameter table styling |
| `th` | `background: #1A1A1A;` `color: white;` `padding: 0.6rem 0.8rem;` | Table header (dark background) |
| `td` | `padding: 0.55rem 0.8rem;` `border-bottom: 1px solid rgba(0,0,0,0.09);` | Table cell styling |
| `tr:nth-child(even) td` | `background: #E1F5EE;` | Table row striping (WW Green tint) |

### HTML body structure (in order)

1. **Required header block:**
   ```html
   <div class="rn-header">
     <span class="product-name">WealthWise</span>
     <span class="header-rule">|</span>
     <span class="header-rule">Help Centre</span>
   </div>
   ```

2. **H1 title** with optional AI tag:
   ```html
   <h1>[feature_name] <span class="tag tag-ai">AI</span></h1>
   ```
   (Include `<span class="tag tag-ai">AI</span>` only if is_ai_feature is true)

3. **Meta line** with class `version`:
   ```html
   <p class="version">Release [release_version] · [Month YYYY]</p>
   ```

4. **Horizontal rule:** `<hr>`

5. **Overview section** with three paragraphs (no special container div):
   - Each paragraph starts with `<strong>What it does:</strong>`, `<strong>Why it matters:</strong>`, or `<strong>Key benefits:</strong>`
   - If Key benefits is a bulleted list, use `<p><strong>Key benefits:</strong></p>` followed by `<ul><li>...</li>...</ul>`

6. **Horizontal rule:** `<hr>`

7. **Workflow section** with `<h3>Workflow</h3>` followed by `<ol>` with one `<li>` per step

8. **API Details section (if api_endpoint is not null):**
   - H3 heading: `<h3>API Details</h3>`
   - Endpoint: `<p><strong>Endpoint:</strong> [api_endpoint]</p>`
   - Method: `<p><strong>Method:</strong> [http_method]</p>`
   - Parameters (if present): HTML `<table>` with th: Parameter, Type, Required, Description
   - Example Response (if present): `<pre><code>[JSON content]</code></pre>`

9. **Horizontal rule:** `<hr>`

10. **Back-link paragraph:**
    ```html
    <p><a href="[release_notes_html_filename]">Back to Release Notes</a> | <a href="#">Help Centre Home</a></p>
    ```

11. **Required footer:**
    ```html
    <footer class="rn-footer">
      &copy; 2026 WealthWise. All rights reserved.
    </footer>
    ```

### Key rules

- No external CSS files. All styles must be inline in the `<style>` block.
- No external fonts. Use system font stack only.
- The back-link href must use the actual `release_notes_html_filename` passed from orchestrator, not a placeholder.
- JSON example content in `<pre><code>` blocks is raw text, not escaped.
- All colour values must match exactly: WW Green #1D9E75, WW Navy #0F6E56, WW Purple #534AB7, etc.
- Section headings use `<h3>`, not `<h2>`.
- Workflow section is numbered `<ol>`, not bullet list.



---



## Step 5 — Validate branding compliance before returning



Before reporting back to the orchestrator, verify that your HTML file meets ALL of these branding compliance checks. Do not return until all checks pass:

### Branding validation checklist

| Check | Must have |
|-------|-----------|
| Header block | `<div class="rn-header">` with WealthWise, divider, Help Centre |
| H1 color | `color: #0F6E56;` (WW Navy) |
| H1 weight | `font-weight: 800;` |
| H2 color | `color: #1D9E75;` (WW Green) |
| H2 border | `border-bottom: 3px solid #1D9E75;` |
| H2 weight | `font-weight: 700;` |
| Bullet color | `background: #1D9E75;` (WW Green dots, not generic) |
| AI tag color | `background-color: #534AB7;` (WW Purple) |
| Link color | `color: #1D9E75;` (WW Green, not #0066cc) |
| Footer | `<footer class="rn-footer">` with copyright year 2026 |
| System font stack | `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;` (no Google Fonts) |
| Max width | `max-width: 760px;` on body |
| Back-link href | Uses actual filename from release_notes_html (not placeholder) |
| CSS completeness | All selectors from Step 4 table are present in style block |

If any check fails, do not submit. Correct the HTML and re-validate.

---

## Step 6 — Return to orchestrator



Report back with:



- issue.key and feature_name

- Filenames of both output files

- Which sections were COMPLETE, INFERRED, or had INSERT flags

- List of any INSERT or INFERRED flags used

- Branding validation result: **PASS** (include this confirmation)
