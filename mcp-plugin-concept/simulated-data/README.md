# Simulated YouTrack Data

## Purpose

These files contain simulated YouTrack data shaped exactly like the result of the `list_release_issues` MCP tool described in `../integration-concept.md`.

They support the **Simulated** proof-of-concept demonstration option: driving the full agent workflow with realistic source data without requiring live YouTrack access or a running MCP server.

---

## Files

| File | Release | Type | Mirrors |
| --- | --- | --- | --- |
| `scenario-1-release-5.4.json` | 5.4 | Feature Release | `sample-data/scenario-1-feature-release/input.md` |
| `scenario-2-release-5.5.json` | 5.5 | Mixed Release | `sample-data/scenario-2-mixed-release/input.md` |

Each file is the same information already in `sample-data/`, expressed as the structured JSON the MCP server would return instead of free-form Markdown.

---

## Schema

```json
{
  "tool": "list_release_issues",
  "request": { "fixVersion": "<version>" },
  "release": {
    "version": "<version>",
    "type": "<release type>",
    "fixVersion": "<version>"
  },
  "issues": [
    {
      "id": "YT-000",
      "type": "Feature | Enhancement | Bug | Security | Technical Debt",
      "summary": "<short title>",
      "description": "<source description>",
      "customerBenefit": "<optional, when provided in source>",
      "customerImpact": "<optional, when provided in source>",
      "fixVersion": "<version>",
      "status": "Done"
    }
  ]
}
```

The `customerBenefit` and `customerImpact` fields are included only when present in the source issue. Their absence is intentional and is what the Release Note Specialist Agent should flag as missing information.

---

## How to Use in the Demo

1. Present this JSON as the output of the `list_release_issues` MCP tool (intake stage).
2. Pass the `issues` array to the **Release Note Specialist Agent** to generate draft release notes.
3. Continue through the standard workflow: review, improve, executive summary, human approval.
4. Use each issue `id` to demonstrate traceability from a release note line back to its source issue.

These files contain non-confidential, illustrative data created for the workshop proof of concept.
