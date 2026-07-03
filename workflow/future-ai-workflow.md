\# GlobalMail Pro Release Notes Automation Workflow



\## Overview



This document describes the complete automated workflow for generating GlobalMail Pro release notes, help topics, and quality reports from Jira data.



\---



\## Architecture



```

┌─────────────────────────────────────────────────────────────────┐

│                    JIRA - GlobalMailProClaudeDemo               │

│                   (KAN Project Issues)                          │

└────────────────────────────┬────────────────────────────────────┘

&#x20;                            │

&#x20;                            │ JQL: project = KAN ORDER BY cf\[10019] ASC

&#x20;                            │ Via Atlassian MCP

&#x20;                            ▼

┌─────────────────────────────────────────────────────────────────┐

│              ORCHESTRATOR AGENT                                  │

│         agents/release-note-orchestrator.md                     │

│                                                                  │

│  Responsibilities:                                              │

│  • Connect to Atlassian MCP and fetch all issues               │

│  • Classify issues (New Features, Enhancements, Bugs, Known)   │

│  • Resolve runtime variables (version, date, slugs)            │

│  • Delegate to sub-agents                                      │

│  • Manage quality review and auto-fix                          │

└────────────────────────────┬────────────────────────────────────┘

&#x20;                            │

&#x20;               ┌────────────┼────────────┐

&#x20;               │            │            │

&#x20;               ▼            ▼            ▼

&#x20;   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐

&#x20;   │   WRITER AGENT   │  │  HELP TOPIC AGENT│  │  REVIEWER AGENT  │

&#x20;   │                  │  │                  │  │                  │

&#x20;   │ Generate:        │  │ Generate:        │  │ Verify:          │

&#x20;   │ • HTML RN        │  │ • HTML topics    │  │ • Structure      │

&#x20;   │ • MD RN          │  │ • MD topics      │  │ • Content        │

&#x20;   │ • JSON RN        │  │ • Cross-links    │  │ • Formatting     │

&#x20;   └──────────────────┘  └──────────────────┘  │ • Links          │

&#x20;               │            │                   │ • JSON validity  │

&#x20;               │            │                   │ • Branding       │

&#x20;               └────────────┴───────────────────┤ • MSTP standards │

&#x20;                                                └──────────────────┘

&#x20;                                                        │

&#x20;                                                        ▼

&#x20;                            ┌───────────────────────────────────┐

&#x20;                            │   OUTPUT PACKAGE                  │

&#x20;                            │                                   │

&#x20;                            │ ✓ release-notes-1.1.html         │

&#x20;                            │ ✓ release-notes-1.1.md           │

&#x20;                            │ ✓ release-notes-1.1.json         │

&#x20;                            │ ✓ help-topic-\[slug].html (×N)    │

&#x20;                            │ ✓ help-topic-\[slug].md (×N)      │

&#x20;                            │ ✓ release-note-review-report.md  │

&#x20;                            └───────────────────────────────────┘

```



\---



\## Workflow Steps



\### Step 1: Issue Fetching (Orchestrator)



\*\*Jira Query:\*\*

```

JQL: project = KAN ORDER BY cf\[10019] ASC

```



\*\*Fields Retrieved per Issue:\*\*

\- key (e.g., KAN-42)

\- summary

\- description

\- issuetype.name (Story, Feature, Bug, Task, etc.)

\- labels (used for classification: known-issue, enhancement, internal)

\- fixVersions (used for release version)

\- priority.name (mapped to severity for bugs)

\- components (affected area for bugs)

\- status

\- comments (for workarounds, fix details)

\- customfield\_steps\_to\_reproduce (for bugs)

\- customfield\_workaround (for known issues)



\### Step 2: Issue Classification



Issues are classified using \*\*label-first priority\*\* to distinguish enhancements from features and known issues from bugs.



\*\*Classification Rules (evaluated top-to-bottom):\*\*



| Priority | Condition | Category | Output Section |

|----------|-----------|----------|-----------------|

| 1 | `labels` contains `internal` | Skip | — |

| 2 | `labels` contains `known-issue` | Known Issues | Known Issues |

| 3 | `labels` contains `enhancement` | Enhancements | Enhancements |

| 4 | `issuetype` = Epic | Skip | — |

| 5 | `issuetype` ∈ (Story, Feature, New Feature) | New Features | New Features |

| 6 | `issuetype` ∈ (Task, Subtask, Enhancement, Improvement) | Enhancements | Enhancements |

| 7 | `issuetype` = Bug | Bug Fixes | Bug Fixes |

| 8 | No match | Enhancements | Enhancements (fallback) |



\*\*Result:\*\* Four lists

\- `new\_features\[]` — Issues for New Features section

\- `enhancements\[]` — Issues for Enhancements section

\- `bug\_fixes\[]` — Issues for Bug Fixes section

\- `known\_issues\[]` — Issues for Known Issues section



\### Step 3: Variable Resolution



Before any content is generated, all runtime variables are resolved:



| Variable | Source | Example |

|----------|--------|---------|

| `release\_version` | fixVersions\[0].name or YYYY.MM | 1.1 |

| `release\_date` | Today's date | 2026-07-03 |

| `release\_month\_year` | Formatted date | July 2026 |

| `product\_name` | Hardcoded constant | GlobalMail Pro |



Feature/Bug-specific variables:

| Variable | Source | Example |

|----------|--------|---------|

| `\[Feature Name]` | issue.summary (sentence case) | AI-powered address validation |

| `\[slug]` | `{key}-{hyphenated-summary}` | kan-42-ai-powered-address-validation |

| `\[Bug ID]` | issue.key | KAN-23 |

| `\[Severity]` | Mapped from priority.name | High, Medium, Low |

| `\[Affected Area]` | components or labels | Dashboard, Compliance |



\### Step 4: Help Topic Slug Generation



For each new feature, a unique slug is generated:



```

slug = lowercase(issue.key) + "-" + lowercase\_hyphenated(issue.summary\[0:40])



Example:

KAN-42 "AI-powered address validation with real-time correction"

→ "kan-42-ai-powered-address-validation-real-time-correction"



Files created:

\- help-topic-kan-42-ai-powered-address-validation-real-time-correction.html

\- help-topic-kan-42-ai-powered-address-validation-real-time-correction.md

```



\### Step 5: Release Notes Generation



\*\*Writer Agent\*\* (`agents/release-note-writer-agent.md`) generates three formats:



\#### Markdown (release-notes-1.1.md)

\- Single source of truth for version control

\- No HTML tags

\- Clean text formatting

\- Sections: Overview, New Features, Enhancements, Bug Fixes, Known Issues



\#### HTML (release-notes-1.1.html)

\- Branded with GlobalMail Pro colours (Navy #1B2A4A, Green #2ECC71)

\- Professional typography (Inter font)

\- Responsive layout

\- Styled elements:

&#x20; - Navy headings with green underlines

&#x20; - Colored severity badges for bugs (High, Medium, Low)

&#x20; - Amber-tinted tiles for known issues

&#x20; - Interactive table styling



\#### JSON (release-notes-1.1.json)

\- Structured data format for downstream systems

\- All sections as objects with properties

\- Links to help topics embedded

\- Valid JSON, no Jira IDs in prose



\*\*Content Format Standards:\*\*



\*\*New Features:\*\*

```markdown

\### \[Feature Title]



\[Description: What it does, why it matters, benefits]



\*\*What you need to do\*\*



\[Action required, or "No configuration changes required"]



\*\*Benefits\*\*

\- \[User benefit 1]

\- \[User benefit 2]

\- \[User benefit 3]



\[Link to help topic if available]

```



\*\*Enhancements:\*\*

```markdown

\- \*\*\[Enhancement Title]:\*\* \[Brief description explaining the improvement and user impact]

```



\*\*Bug Fixes (Table):\*\*

```

| Bug ID | Area of Impact | Issue | Fix |

|--------|---|---|---|

| KAN-23 | Dashboard | \[What was broken] | \[What is now fixed] |

```



\*\*Known Issues (Tiles in HTML, formatted text in Markdown):\*\*

```markdown

\*\*\[Issue Title]\*\*



\[Description of the problem]



\*Workaround:\* \[Temporary solution or mitigation]

```



\### Step 6: Help Topic Generation



\*\*Help Topic Agent\*\* (`agents/help-topic-writer-agent.md`) creates documentation for each new feature.



\*\*Format (from expected-output-2.md):\*\*

```markdown

\# \[Feature Title]



\[One-line description]



\---



\## Overview



\*\*What it does:\*\* \[Description]

\*\*Why it matters:\*\* \[User impact]

\*\*Key benefits:\*\* \[List of benefits]



\---



\## Workflow



1\. \[Step 1]

2\. \[Step 2]

...

7\. \[Step N]



\---



\## API Details



\*\*Endpoint:\*\* `/api/v1/...`

\*\*Method:\*\* `POST`



\### Parameters



| Parameter | Type | Required | Description |

|---|---|---|---|

| param1 | string | Yes | Description |



\### Example Response



\\`\\`\\`json

{

&#x20; "success": true,

&#x20; "result": { ... }

}

\\`\\`\\`



\---



\[Tips, troubleshooting, related topics]



\---



\[Footer with link back to release notes]

```



\### Step 7: Cross-linking



\*\*Release Notes → Help Topics:\*\*

```markdown

\[Learn more →](help-topic-kan-42-ai-powered-address-validation-real-time-correction.html)

```



\*\*Help Topic → Release Notes:\*\*

```markdown

\[Release Notes for Version 1.1](release-notes-1.1.html)

```



\*\*JSON Links:\*\*

```json

{

&#x20; "id": "KAN-42",

&#x20; "title": "Feature title",

&#x20; "helpTopic": "help-topic-kan-42-....html"

}

```



\### Step 8: Quality Review



\*\*Reviewer Agent\*\* (`agents/release-note-reviewer-agent.md`) runs automated QA:



\*\*Checklist (22 points):\*\*

1\. ✓ Overview section present

2\. ✓ New Features section complete (title, description, benefits, link)

3\. ✓ Enhancements section present (if enhancements exist)

4\. ✓ Bug Fixes table present (if bugs exist)

5\. ✓ Known Issues section present (if known issues exist)

6\. ✓ All issue keys (KAN-X) are valid

7\. ✓ No marketing language (seamless, powerful, revolutionary)

8\. ✓ Active voice throughout

9\. ✓ Present tense for current behavior

10\. ✓ Second person where applicable

11\. ✓ No internal engineering details

12\. ✓ Serial (Oxford) comma used

13\. ✓ Numbers 0-9 spelled out

14\. ✓ No em dashes (—)

15\. ✓ Sentence case on headings

16\. ✓ Help topic links present (if new features exist)

17\. ✓ Help topic links are valid filenames

18\. ✓ No duplicate content

19\. ✓ Severity badges correct (High, Medium, Low)

20\. ✓ Known issues have workarounds

21\. ✓ JSON is valid and complete

22\. ✓ Branding applied (colours, typography, footer)



\*\*7-Criterion Style Audit:\*\*

1\. Active voice

2\. Present tense

3\. Second person (where applicable)

4\. Sentence length (aim for 12-20 words)

5\. Heading case (sentence case)

6\. Code formatting (monospace for API endpoints, field names)

7\. No jargon or unexplained acronyms



\*\*Auto-fix:\*\*

\- High severity findings → Auto-corrected

\- Medium severity findings → Auto-corrected

\- Low severity findings → Logged in report



\### Step 9: Auto-fix \& Output



\*\*Auto-fix Examples:\*\*

\- ✗ "Previously, users submitted addresses..." → ✓ "Addresses were submitted..."

\- ✗ "The system provides seamless validation" → ✓ "The system validates addresses in real time"

\- ✗ "No API or schema changes" → ✗ \[Removed entirely]



\*\*Output Package Written to `/output/`:\*\*

```

release-notes-1.1.md                                   (3.1 KB)

release-notes-1.1.html                                 (7.7 KB)

release-notes-1.1.json                                 (3.6 KB)

help-topic-kan-42-ai-powered-address-validation-\*.md  (3.2 KB)

help-topic-kan-42-ai-powered-address-validation-\*.html (6.6 KB)

release-note-review-report.md                          (QA findings)

```



\---



\## Configuration \& Skills



\### Branding Style Guide (`skills/branding-style-guide.md`)



\*\*Colour Palette:\*\*

\- Primary: Navy #1B2A4A, Green #2ECC71

\- Supporting: Light Navy #2C3E6B, Navy Tint #EDF0F7, Green Tint #E8F8F0

\- Status: Valid Green #2ECC71, Amber #F39C12, Red #C0392B

\- Neutral: Text Dark #1A1A2E, Gray 1–4



\*\*Typography:\*\*

\- Font: Inter (400, 600, 700 weights)

\- Fallback: -apple-system, Arial

\- H1/H2: Navy, Bold 700

\- H3: Light Navy, SemiBold 600

\- Body: Text Dark, Regular 400



\### Writing Standards (`skills/release-note-writer-skill.md`)



\*\*MSTP Rules:\*\*

\- Active voice: "The system validates" not "The address is validated"

\- Present tense for current behaviour

\- No filler: "in order to", "it should be noted"

\- No marketing: "powerful", "seamless", "cutting-edge"

\- Oxford comma in lists: "A, B, and C"

\- Spell out 0–9, numerals for 10+



\### Expected Outputs (`sample-data/expected-output-1.md`, `sample-data/expected-output-2.md`)



Benchmarks define:

\- Release notes structure (all required sections)

\- Help topic structure (Overview, Workflow, API)

\- Content quality (tone, length, clarity)

\- Link format (relative paths, anchor text)



\---



\## Data Fallback



If Atlassian MCP connection fails, the orchestrator falls back to \*\*sample data\*\*:

\- `sample-data/sample-input-enhancement.md` — Enhancement data

\- `sample-data/sample-input-knownissue.md` — Known issue data

\- Hardcoded new features and bug fixes



This ensures the pipeline completes even if Jira is unavailable.



\---



\## Example Execution



```bash

\# Trigger the pipeline

/project:generate-release-notes



\# Or paste the orchestrator command

Run the GlobalMail Pro release note automation pipeline from start to finish...

```



\*\*Output:\*\*

```

PIPELINE COMPLETE

=================

Release version: 1.1

Release date:    2026-07-03



Issues processed:

&#x20; New Features:  1 (KAN-42)

&#x20; Enhancements:  3 (KAN-11, KAN-41, KAN-40)

&#x20; Bug Fixes:     2 (KAN-23, KAN-31)

&#x20; Known Issues:  2 (KAN-13, KAN-50)



Files created:

&#x20; ✓ output/release-notes-1.1.html

&#x20; ✓ output/release-notes-1.1.md

&#x20; ✓ output/release-notes-1.1.json

&#x20; ✓ output/help-topic-kan-42-\*.html

&#x20; ✓ output/help-topic-kan-42-\*.md

&#x20; ✓ output/release-note-review-report.md



Quality review: PASS (0 High, 0 Medium, 0 Low findings)

```



\---



\## Troubleshooting



| Issue | Resolution |

|-------|-----------|

| Atlassian MCP not connected | Run `claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse` |

| No issues fetched | Verify KAN project has issues in Jira |

| Output files missing | Run `mkdir -p output` |

| Help topic links broken | Verify slug matches filename exactly |

| JSON invalid | Check for unescaped quotes or newlines in descriptions |

| Branding not applied | Verify HTML file includes `<link>` for Inter font and CSS styles |



\---



\## Next Steps



1\. \*\*Human Review:\*\* Check output files for accuracy and completeness

2\. \*\*Commit:\*\* `git add output/ \&\& git commit -m "feat: release notes 1.1"`

3\. \*\*Publish:\*\* Deploy to GlobalMail Pro Help Centre

4\. \*\*Archive:\*\* Store JSON version in analytics/compliance system



\---



\*\*Last Updated:\*\* 2026-07-03  

\*\*Workflow Version:\*\* 1.1  

\*\*Orchestrator Version:\*\* 1.1



