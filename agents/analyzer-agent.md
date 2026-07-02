# File: `agents/analyzer-agent.md`

# Analyzer Agent

## Purpose

Analyze release data and identify customer-facing changes that should appear in the release notes.

This agent converts raw release information into structured categories for the Writer Agent.

---

## Responsibilities

* Read release data.
* Classify release items.
* Filter out technical work.
* Organize customer-facing changes.
* Produce structured output.

---

## Input

```text
data/release-2025.8.json
```

---

## Skills Used
```text
classify-release-items.md
```
---

## Prompt Used

```text
.claude/prompts/analyze-release.md
```

---

## Output

```text
output/analyzed-release.json
```

Example output:

```json
{
  "features": [],
  "enhancements": [],
  "bugFixes": []
}
```

---

## Success Criteria

* All customer-facing items are classified correctly.
* Technical tasks are excluded.
* Features, enhancements, and bug fixes are grouped correctly.
* Output is valid JSON.

---

## Future MCP Tools

Azure DevOps MCP

* get_release_work_items()

ServiceNow MCP

* get_change_requests()

---

## Future Enhancements

* Detect duplicate work items.
* Group related features.
* Generate release statistics.
* Suggest release highlights automatically.
