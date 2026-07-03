# Code Updates Completed

**Date:** July 3, 2026  
**Status:** ✅ COMPLETE - Ready for pipeline rerun

---

## Summary of Changes

All project files have been updated to enforce the following requirements:

1. ✅ Version number must appear at top of release notes only
2. ✅ Help topic links must be created from release notes and clickable
3. ✅ "Help Center" text corrected to "Help Centre" (British English)
4. ✅ Bug Fixes table structure corrected to 4 columns ONLY

---

## Files Updated

### 1. `sample-data/expected-output-1.md` (Release Notes Benchmark)

**Changes:**
- ✅ Added version number format at top: `**Version:** [version]`
- ✅ Added NOTE explaining help topic link requirements:
  - Link format: `[Learn more →](help-topic-[slug].html)`
  - Links must open help topics from release notes
  - Links must use correct file names
- ✅ Changed footer text from "Help Center" → "Help Centre"

**Section Updated:**
```markdown
## GlobalMail Pro – Release 1.1 (July 2026)

**Version:** 1.1

---

### New Features

**NOTE:** Each new feature MUST link to its corresponding help topic. 
Link format: `[Learn more →](help-topic-[slug].html)`. 
The help topic link MUST be created from this release notes page 
and should open the help topic in the Help Centre.
```

---

### 2. `skills/release-note-writer-skill.md` (Writing Standards)

**Changes:**
- ✅ Added new "Output Format — Release Notes Header" section specifying:
  - Title: `# GlobalMail Pro – Release [Version]`
  - Version: `**Version:** [Version number, e.g. 1.1]`
  - Placement: At the top, immediately after title
  
- ✅ Updated "Output Format — New Feature" section with:
  - **IMPORTANT note** about help topic links
  - Link format: `[Learn more →](help-topic-[slug].html)`
  - Link placement: After feature description
  - Link must be clickable relative URL (not absolute)

**New Template Section:**
```markdown
## Output Format — Release Notes Header

IMPORTANT: Every release notes document MUST include version number 
at the top, immediately after the main title.

# GlobalMail Pro – Release [Version]

**Version:** [Version number, e.g. 1.1]

[Release date, e.g. July 2026]

---

## Overview

[Summary paragraph...]
```

---

### 3. `agents/release-note-orchestrator.md` (Pipeline Instructions)

**Changes:**
- ✅ Enhanced "Step 6 — Delegate to the Writer Agent" with explicit instructions:

**IMPORTANT INSTRUCTIONS ADDED:**
```
1. Place version number at the top of release notes immediately after the title:
   `# GlobalMail Pro – Release [version]`
   `**Version:** [version]`
   
2. For each new feature, create a clickable help topic link using the help_topic_map:
   `[Learn more →](help-topic-[slug].html)`
   The link MUST:
   - Point to the correct help topic filename
   - Be placed after the feature description
   - Use the exact text "[Learn more →]"
   - Be a working relative link (no absolute URLs)

3. Use "Help Centre" (British English) in footer: "visit the **Help Centre**"
```

- ✅ Updated output file descriptions to include version number and help topic links

---

### 4. `agents/release-note-reviewer-agent.md` (QA Checklist)

**Changes:**
- ✅ Completely updated the Structure Compliance Checklist (RN-S1 through RN-S12):

**Updated Checklist:**

| ID    | Check                                                        |
|-------|--------------------------------------------------------------|
| RN-S1 | Version number present at top: `**Version:** [version]` |
| RN-S2 | Title is product name + version (e.g. "GlobalMail Pro – Release 1.1") |
| RN-S3 | Overview section present and non-empty                       |
| RN-S4 | New Features section present (if new_features non-empty)     |
| RN-S5 | Every New Feature entry has a clickable help topic hyperlink in format: `[Learn more →](help-topic-[slug].html)` |
| RN-S6 | Help topic links point to correct file names and exist       |
| RN-S7 | Enhancements section present (if enhancements non-empty)     |
| RN-S8 | Bug Fixes section present as a table (if bug_fixes non-empty)|
| RN-S9 | Bug Fixes table has EXACTLY 4 columns ONLY: Bug ID, Area of Impact, Issue, Fix |
| RN-S10| Known Issues section present with workarounds               |
| RN-S11| Technical Notes section NOT present (should be removed)      |
| RN-S12| Closing footer line present with "Help Centre" (British English) |

---

## Key Requirements Enforced

### Version Number Format
```
# GlobalMail Pro – Release 1.1

**Version:** 1.1

July 2026

---
```

### Help Topic Link Format
```markdown
[Learn more →](help-topic-kan-42-ai-powered-address-validation-real-time-correction.html)
```

**Link Properties:**
- ✓ Uses exact text: "[Learn more →]"
- ✓ Relative path (no absolute URL)
- ✓ Correct help topic filename
- ✓ Clickable from release notes page
- ✓ Opens Help Centre help topic

### Bug Fixes Table Format
```markdown
| Bug ID | Area of Impact | Issue | Fix |
|--------|---|---|---|
| KAN-23 | Dashboard | [Description] | [Description] |
```

**Table Properties:**
- ✓ EXACTLY 4 columns (no more, no less)
- ✓ Top-aligned headers
- ✓ No severity, summary, or other columns
- ✓ Clean, readable format

### Footer Text
```markdown
For help with any feature, contact support or visit the **Help Centre**.
```

**Text Properties:**
- ✓ Uses "Help Centre" (British English, not American "Center")
- ✓ Consistent with GlobalMail Pro Help Centre branding

---

## Pre-Pipeline Checklist

Before running the end-to-end pipeline, verify:

- ✅ Version number template added to skills and agents
- ✅ Help topic link requirements in all files
- ✅ Bug Fixes table reduced to 4 columns in checklist
- ✅ "Help Centre" (British English) in footer text
- ✅ Reviewer agent checklist updated
- ✅ Orchestrator instructions updated
- ✅ Expected output benchmark updated

---

## Next Steps

When ready to rerun the pipeline:

1. **Delete all output files:**
   ```bash
   rm -rf output/*.html output/*.md output/*.json output/*.txt
   ```

2. **Run the complete end-to-end pipeline:**
   ```
   /project:generate-release-notes
   ```
   Or paste the orchestrator command

3. **Verify output files:**
   - Check version number at top of release notes
   - Verify help topic links are present and correct
   - Confirm "Help Centre" appears in footer
   - Validate Bug Fixes table has 4 columns only
   - Run QA review report for any findings

4. **Expected Output Files:**
   ```
   ✓ release-notes-1.1.html (with version number, help topic links)
   ✓ release-notes-1.1.md (with version number, help topic links)
   ✓ release-notes-1.1.json (with version and helpTopic fields)
   ✓ help-topic-kan-42-*.html
   ✓ help-topic-kan-42-*.md
   ✓ release-note-review-report.md (with updated checklist)
   ```

---

## Files Modified Summary

| File | Changes |
|------|---------|
| `sample-data/expected-output-1.md` | Version number format, help topic link note, footer text |
| `skills/release-note-writer-skill.md` | Added Release Notes Header format, help topic link instructions |
| `agents/release-note-orchestrator.md` | Added detailed writer agent instructions for version & links |
| `agents/release-note-reviewer-agent.md` | Updated checklist with 12 new verification items |

**Total Files Modified:** 4  
**Total Sections Updated:** 8  
**Total Requirement Changes:** 3 major (version number, help links, footer text)

---

**Status:** ✅ All code updates completed  
**Ready for:** Pipeline rerun  
**Instructions:** Delete output files and execute the pipeline

---

**Last Updated:** July 3, 2026  
**Updated By:** Claude Code Release Notes Pipeline  
**Change Version:** 2.0 (Major - Structure & Format Requirements)
