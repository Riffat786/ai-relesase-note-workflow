\# Release Notes Validation \& Quality Assurance



\## Overview



This document describes the automated validation and quality assurance process for GlobalMail Pro release notes. Every release notes package goes through a comprehensive 22-point checklist, 7-criterion style audit, branding compliance check, and hyperlink integrity verification before publication.



\---



\## Quality Review Agent (`agents/release-note-reviewer-agent.md`)



The Reviewer Agent applies three levels of validation:



\### Level 1: Structure Compliance (8 points)



Verifies that all required sections are present and properly formatted:



1\. \*\*Overview section\*\*

&#x20;  - ✓ Present and meaningful

&#x20;  - ✗ Flag if missing or empty



2\. \*\*New Features section\*\*

&#x20;  - ✓ Present if new features exist

&#x20;  - ✓ Each feature has: title, description, benefits, help topic link

&#x20;  - ✗ Flag if feature lacks any required element



3\. \*\*Enhancements section\*\*

&#x20;  - ✓ Present if enhancements exist

&#x20;  - ✓ Bullet point format with title and description

&#x20;  - ✗ Flag if missing or improperly formatted



4\. \*\*Bug Fixes section\*\*

&#x20;  - ✓ Present if bugs exist

&#x20;  - ✓ Table format with 4 columns: Bug ID, Area of Impact, Issue, Fix

&#x20;  - ✓ Each bug ID is valid (KAN-X format)

&#x20;  - ✗ Flag if missing, wrong format, or invalid IDs



5\. \*\*Known Issues section\*\*

&#x20;  - ✓ Present if known issues exist

&#x20;  - ✓ Tile/card format (HTML) or formatted text (Markdown)

&#x20;  - ✓ Each issue has title, description, workaround

&#x20;  - ✗ Flag if missing workaround



6\. \*\*Technical Notes section\*\*

&#x20;  - ✓ REMOVED (not in current output format)

&#x20;  - ✗ Flag if present



7\. \*\*Footer\*\*

&#x20;  - ✓ Present on all HTML files

&#x20;  - ✓ Contains copyright statement

&#x20;  - ✗ Flag if missing



8\. \*\*Related links\*\*

&#x20;  - ✓ Help topic links present for all new features

&#x20;  - ✓ Links use correct relative paths

&#x20;  - ✗ Flag if link is broken or missing



\---



\### Level 2: Content Quality (14 points)



Applies MSTP writing standards and GlobalMail Pro voice guidelines:



\#### Voice \& Tone



1\. \*\*Active voice\*\*

&#x20;  - ✓ "The validator checks each address"

&#x20;  - ✗ "Each address is checked by the validator"

&#x20;  - \*\*Auto-fix:\*\* Rewrite in active voice



2\. \*\*Present tense for current behaviour\*\*

&#x20;  - ✓ "The system now supports exports"

&#x20;  - ✗ "The system will now support exports"

&#x20;  - \*\*Auto-fix:\*\* Convert to present tense



3\. \*\*No marketing language\*\*

&#x20;  - ✗ "Powerful", "seamless", "revolutionary", "cutting-edge", "robust", "best-in-class"

&#x20;  - \*\*Auto-fix:\*\* Remove or replace with technical language



4\. \*\*Second person (where applicable)\*\*

&#x20;  - ✓ "You see ranked suggestions"

&#x20;  - ✗ "Users see ranked suggestions" (use "you" in user-facing content)

&#x20;  - \*\*Auto-fix:\*\* Convert to second person



\#### Grammar \& Punctuation



5\. \*\*No em dashes (—)\*\*

&#x20;  - ✗ "The system validates — taking 30 minutes"

&#x20;  - ✓ "The system validates, taking up to 30 minutes"

&#x20;  - \*\*Auto-fix:\*\* Replace with comma or colon



6\. \*\*Serial (Oxford) comma\*\*

&#x20;  - ✓ "City, postal code, and country"

&#x20;  - ✗ "City, postal code and country"

&#x20;  - \*\*Auto-fix:\*\* Add Oxford comma to all lists



7\. \*\*Numbers 0–9 spelled out\*\*

&#x20;  - ✓ "One new feature, three enhancements, two bug fixes"

&#x20;  - ✗ "1 new feature, 3 enhancements, 2 bug fixes"

&#x20;  - \*\*Auto-fix:\*\* Spell out numbers



8\. \*\*Periods \& spacing\*\*

&#x20;  - ✓ "One space after periods. Proper formatting."

&#x20;  - ✗ "Two  spaces  after  periods."

&#x20;  - \*\*Auto-fix:\*\* Normalize spacing



\#### Structure \& Format



9\. \*\*Sentence case on headings\*\*

&#x20;  - ✓ "AI-powered address validation with real-time correction"

&#x20;  - ✗ "AI-Powered Address Validation With Real-Time Correction"

&#x20;  - \*\*Auto-fix:\*\* Convert to sentence case



10\. \*\*No internal IDs in prose\*\*

&#x20;   - ✓ Bug ID appears in table only: | KAN-23 |

&#x20;   - ✗ "KAN-23 fixed dashboard metrics"

&#x20;   - \*\*Auto-fix:\*\* Move ID to proper table cell



11\. \*\*No engineering details\*\*

&#x20;   - ✗ "Cache values updated every 15 minutes", "Database schema changed"

&#x20;   - ✓ "Metrics update in the background every 15 minutes"

&#x20;   - \*\*Auto-fix:\*\* Remove technical implementation details



12\. \*\*Bug severity mapping\*\*

&#x20;   - ✓ Highest/High → "High", Medium → "Medium", Low/Lowest → "Low"

&#x20;   - ✗ "Critical", "Priority 1", "P1"

&#x20;   - \*\*Auto-fix:\*\* Map to standard severity levels



\#### Content Accuracy



13\. \*\*No invented content\*\*

&#x20;   - ✓ Every claim traces to Jira issue field

&#x20;   - ✗ "Users love the new validator" (not in Jira)

&#x20;   - \*\*Auto-fix:\*\* Flag with \[INSERT: data from Jira] placeholder



14\. \*\*Duplicate content check\*\*

&#x20;   - ✓ Each feature/bug/enhancement mentioned once

&#x20;   - ✗ Same feature appears in two sections

&#x20;   - \*\*Auto-fix:\*\* Remove duplicate, keep one instance



\---



\### Level 3: Technical Validation (Branding, Links, JSON)



\#### Branding Compliance



15\. \*\*Colour palette applied (HTML)\*\*

&#x20;   - ✓ H1/H2: Navy #1B2A4A

&#x20;   - ✓ Accents: Green #2ECC71

&#x20;   - ✓ Known Issue tiles: Amber #FFF9E6 with #F39C12 border

&#x20;   - ✓ Bug severity badges: High (Red), Medium (Amber), Low (Gray)

&#x20;   - \*\*Auto-fix:\*\* Apply CSS styles if missing



16\. \*\*Typography correct (HTML)\*\*

&#x20;   - ✓ Font: Inter (400, 600, 700)

&#x20;   - ✓ H1: Bold 700, 2rem

&#x20;   - ✓ H2: Bold 700, 1.35rem

&#x20;   - ✓ H3: SemiBold 600, 1.05rem

&#x20;   - ✓ Body: Regular 400, 16px

&#x20;   - \*\*Auto-fix:\*\* Add font-weight, font-size, font-family CSS



17\. \*\*Header \& footer present (HTML)\*\*

&#x20;   - ✓ Header: Navy background with "GlobalMail Pro | Help Centre"

&#x20;   - ✓ Footer: Copyright line, gray text

&#x20;   - \*\*Auto-fix:\*\* Add if missing



\#### Hyperlink Integrity



18\. \*\*Help topic links present\*\*

&#x20;   - ✓ All new features have link to help topic

&#x20;   - ✓ Link text: "\[Learn more →]"

&#x20;   - ✓ File exists: `help-topic-\[slug].html`

&#x20;   - \*\*Auto-fix:\*\* Add link or create placeholder



19\. \*\*Link format correct\*\*

&#x20;   - ✓ Relative paths: `help-topic-kan-42-....html`

&#x20;   - ✓ No absolute URLs

&#x20;   - ✓ No broken anchors

&#x20;   - \*\*Auto-fix:\*\* Correct path or remove invalid link



20\. \*\*Bidirectional links\*\*

&#x20;   - ✓ Help topic → Release Notes: `\[Release Notes](release-notes-1.1.html)`

&#x20;   - ✓ Both directions working

&#x20;   - \*\*Auto-fix:\*\* Add reverse link if missing



\#### Markdown Quality



21\. \*\*No HTML tags in Markdown\*\*

&#x20;   - ✓ Clean markdown: `\*\*bold\*\*`, `\_italic\_`, `\[link](url)`

&#x20;   - ✗ `<strong>bold</strong>`, `<em>italic</em>`

&#x20;   - \*\*Auto-fix:\*\* Convert HTML to markdown syntax



\#### JSON Validation



22\. \*\*Valid JSON structure\*\*

&#x20;   - ✓ Valid JSON (no syntax errors)

&#x20;   - ✓ All required fields present

&#x20;   - ✓ No unescaped quotes or newlines

&#x20;   - ✓ No Jira IDs in prose fields (only in `id` field)

&#x20;   - \*\*Auto-fix:\*\* Validate and repair syntax



\---



\## 7-Criterion Style Audit



Independent verification of writing quality:



\### Criterion 1: Active Voice



\*\*Requirement:\*\* All sentences in active voice (subject performs action)



\*\*Audit:\*\*

\- ✓ "The validator checks" (active)

\- ✗ "Is checked by the validator" (passive)



\*\*Finding:\*\* Count passive constructions, flag each



\### Criterion 2: Present Tense



\*\*Requirement:\*\* Present tense for current system behaviour



\*\*Audit:\*\*

\- ✓ "The system now supports"

\- ✗ "The system will support" (future)

\- ✗ "The system supported" (past)



\*\*Finding:\*\* Flag tense inconsistencies



\### Criterion 3: Second Person



\*\*Requirement:\*\* Use "you" in user-facing content where appropriate



\*\*Audit:\*\*

\- ✓ "You see ranked suggestions"

\- ✓ "Enter as much detail as you have"

\- ✗ "Users see ranked suggestions" (avoid "users")



\*\*Finding:\*\* Flag instances of "users" that should be "you"



\### Criterion 4: Sentence Length



\*\*Requirement:\*\* Aim for 12–20 words per sentence (max 25)



\*\*Audit:\*\*

\- ✓ "Ranked correction suggestions appear inline." (6 words — acceptable)

\- ✓ "Each suggestion includes a confidence percentage from zero to one hundred percent." (12 words)

\- ✗ "The Address Validator now checks each address as you enter it, surfaces ranked correction suggestions with confidence scores, and records every result in Validation History with status, confidence percentage, and timestamp." (33 words — split into 2–3 sentences)



\*\*Finding:\*\* Flag sentences over 25 words



\### Criterion 5: Heading Case (Sentence Case)



\*\*Requirement:\*\* Sentence case on all headings (capitalize first word + proper nouns only)



\*\*Audit:\*\*

\- ✓ "AI-powered address validation with real-time correction"

\- ✓ "Batch address validation now supports up to 10,000 records"

\- ✗ "AI-Powered Address Validation With Real-Time Correction"



\*\*Finding:\*\* Flag heading capitalization errors



\### Criterion 6: Code Formatting



\*\*Requirement:\*\* Monospace for field names, API endpoints, code examples



\*\*Audit:\*\*

\- ✓ Endpoint: `/api/v1/address/validate`

\- ✓ Field: `address\_line\_1`

\- ✗ "Endpoint /api/v1/address/validate" (not monospace)



\*\*Finding:\*\* Flag missing code formatting



\### Criterion 7: Jargon \& Acronyms



\*\*Requirement:\*\* No unexplained jargon; define or simplify acronyms



\*\*Audit:\*\*

\- ✓ "USPS (United States Postal Service)"

\- ✗ "UPU standards" (undefined)

\- ✗ "CSV export" (not defined, but common enough—may be acceptable)



\*\*Finding:\*\* Flag undefined terms



\---



\## Severity Levels \& Auto-fix Rules



\### High Severity

\*\*Definition:\*\* Breaks compliance, brand, or structure



\*\*Examples:\*\*

\- Missing required section

\- Invalid JSON

\- Broken hyperlinks

\- Marketing language in main content

\- Missing brand colours



\*\*Action:\*\* Auto-fix applied, reported in log



\### Medium Severity

\*\*Definition:\*\* Inconsistency in tone or format



\*\*Examples:\*\*

\- Passive voice in bug descriptions

\- Inconsistent tense

\- Poorly formatted table

\- Missing workaround in known issue



\*\*Action:\*\* Auto-fix applied, reported in log



\### Low Severity

\*\*Definition:\*\* Style preference or minor grammar



\*\*Examples:\*\*

\- Serial comma missing (acceptable if consistent)

\- Sentence over 20 words (not over 25)

\- Heading capitalization inconsistency



\*\*Action:\*\* Logged in report, not auto-fixed



\---



\## Review Report (`release-note-review-report.md`)



Sample output:



```markdown

\# Release Notes Review Report

Release 1.1 (July 2026)



\## Summary

\- \*\*Status:\*\* PASS (3 High findings auto-fixed)

\- \*\*Files reviewed:\*\* 5

\- \*\*Issues found:\*\* 8

\- \*\*Auto-fixed:\*\* 6 (3 High, 3 Medium)

\- \*\*Remaining:\*\* 2 Low



\## Findings



\### \[RN-S1] Missing Help Topic Link — HIGH

\*\*File:\*\* release-notes-1.1.html, line 45  

\*\*Section:\*\* New Features — KAN-42  

\*\*Finding:\*\* Feature "AI-powered address validation" lacks link to help topic  

\*\*Severity:\*\* High  

\*\*Fix Applied:\*\* Added link `\[Learn more →](help-topic-kan-42-ai-powered-address-validation-real-time-correction.html)`



\### \[RN-W2] Passive Voice — MEDIUM

\*\*File:\*\* release-notes-1.1.md, line 89  

\*\*Section:\*\* Bug Fixes  

\*\*Finding:\*\* "The Compliance Passes metric was excluded..." (passive voice)  

\*\*Severity:\*\* Medium  

\*\*Fix Applied:\*\* Rewritten to "EU shipments were excluded from..." (still passive but more direct) → "The system excluded EU shipments..."



\[... additional findings ...]



\## Verification Checklist

\- ✓ All sections present

\- ✓ No broken hyperlinks

\- ✓ Valid JSON

\- ✓ Brand colours applied

\- ✓ MSTP standards met

\- ✓ Help topics linked correctly



\## Sign-off

✓ Approved for publication

```



\---



\## Testing \& Verification



\### Pre-Publication Checklist



```

□ All output files present (HTML, MD, JSON, help topics)

□ Links verified (click-tested in browser if possible)

□ Branding visually correct

□ Grammar and spelling reviewed by human

□ Jira issue data matches expected content

□ Version number correct throughout

□ Release date accurate

□ No customer-facing URLs are broken

□ JSON can be parsed without errors

□ Help topics match release notes

```



\### Automated Tests



Run before committing:

```bash

\# Validate JSON

jq . output/release-notes-1.1.json



\# Check for broken links (relative paths)

grep -r "help-topic-" output/release-notes-\*.html | grep -oP "help-topic-\[^\\"]\*" | sort -u | while read link; do

&#x20; \[ -f "output/$link" ] || echo "BROKEN: $link"

done



\# Check for API tokens or secrets

grep -r "token\\|secret\\|password\\|api\_key" output/ \&\& echo "WARNING: Found potential secrets"



\# Validate markup (if available)

\# tidy -e output/release-notes-1.1.html

```



\---



\## Common Issues \& Fixes



| Issue | Root Cause | Fix |

|-------|-----------|-----|

| "No API or schema changes" text appears | Template not updated | Remove Technical Notes section entirely |

| Validation History link broken | Invalid help topic file | Remove link if help topic doesn't exist |

| Markdown has HTML tags | Conversion error | Convert `<b>` → `\*\*`, `<em>` → `\_`, etc. |

| JSON parse error | Unescaped quotes in description | Escape quotes: `\\"` |

| Help topic missing API Details | Writer agent skipped API section | Re-read expected-output-2.md and regenerate |

| Known issue without workaround | Data missing in Jira | Flag with \[INSERT: workaround needed] |

| Table alignment wrong | CSS missing | Apply `vertical-align: top` to table headers/cells |



\---



\## Next Steps After Validation



1\. \*\*Review Report:\*\* Read `release-note-review-report.md`

2\. \*\*Spot Check:\*\* Open HTML file in browser, verify appearance

3\. \*\*Link Test:\*\* Click help topic links in HTML

4\. \*\*Jira Verification:\*\* Cross-reference 3–5 issues with their Jira tickets

5\. \*\*Commit:\*\* Add all files to git

6\. \*\*Publish:\*\* Deploy to GlobalMail Pro Help Centre

7\. \*\*Monitor:\*\* Watch for user questions about new features (indicates content clarity)



\---



\*\*Last Updated:\*\* 2026-07-03  

\*\*Validation Version:\*\* 1.1  

\*\*MSTP Standards:\*\* Microsoft Writing Style Guide (https://learn.microsoft.com/en-us/style-guide/)



