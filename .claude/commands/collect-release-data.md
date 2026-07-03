# File: `.claude/commands/collect-release-data.md`

# /collect-release-data

## Purpose

Build a consolidated release dataset for a specified software release.

The Collector retrieves all release information required for downstream AI agents and prepares the release dataset used throughout the AI Release Note Pipeline.

For the current Proof of Concept (POC), this command retrieves release information from local mock JSON files that simulate Azure DevOps and ServiceNow.

In the future production solution, this command will retrieve release information directly from Azure DevOps MCP and ServiceNow MCP.

This command **only collects and consolidates data**.

It does **not**:

- Analyze release information
- Generate release notes
- Perform AI review
- Create Document360 drafts

---

# Usage

```text
/collect-release-data 2025.8
```

---

# Current POC Workflow

```text
Local Mock Data
      │
      ├──────────────┐
      ▼              ▼
release-2025.8.json  service-now-2025.8.json
      │              │
      └──────┬───────┘
             ▼
      Collector Agent
             │
             ▼
collected-release-data.json
```

---

# Future Production Workflow

```text
Azure DevOps
(Release Package)
         │
         ▼
Collector Agent
         │
 ┌───────┴────────────┐
 ▼                    ▼
Azure DevOps MCP   ServiceNow MCP
get_work_items()   get_cases()
 ▼                    ▼
Retrieve WI       Retrieve Cases
         │
         └───────┬────────────┘
                 ▼
 Merge & Enrich Release Data
                 │
                 ▼
collected-release-data.json
```

---

# Inputs

## Current POC

Read the following files:

```text
data/release-{{releaseVersion}}.json

data/service-now-{{releaseVersion}}.json
```

---

## Future Production

Retrieve release information using:

Azure DevOps MCP

- Release Package
- Work Item IDs
- Release metadata

ServiceNow MCP

- Linked customer cases
- Resolution information
- Customer impact

---

# Instructions

## Step 1 — Load Release Data

Read:

```text
data/release-{{releaseVersion}}.json
```

Verify that:

- The file exists.
- The JSON is valid.

---

## Step 2 — Load ServiceNow Data

Read:

```text
data/service-now-{{releaseVersion}}.json
```

Verify that:

- The file exists.
- The JSON is valid.

---

## Step 3 — Validate Input Data

Verify that:

- Release version exists.
- Required Work Items are present.
- Related ServiceNow cases are available.
- JSON structure is valid.

If validation fails, stop the workflow and report the issue.

---

## Step 4 — Merge Release Information

Create a consolidated release dataset by combining:

Azure DevOps information:

- Release metadata
- Work Item IDs
- Feature information
- Bug information
- Enhancement information

ServiceNow information:

- Case Numbers
- Customer issue summaries
- Resolution summaries
- Customer impact

Preserve traceability between Work Items and ServiceNow Cases.

Do not modify the source data.

---

## Step 5 — Generate Artifact

Create:

```text
output/artifacts/ai/collected-release-data.json
```

The generated artifact becomes the single source of truth for all downstream AI agents.

---

## Step 6 — Display Summary

Return a summary including:

- Release Version
- Number of Work Items
- Number of Features
- Number of Enhancements
- Number of Bug Fixes
- Number of ServiceNow Cases
- Collection Status

Do not perform analysis.

Do not generate release notes.

---

# Output

Create:

```text
output/artifacts/ai/collected-release-data.json
```

---

# Expected Summary

Display:

```text
Release Data Collection Complete

Release Version: 2025.8

Work Items: 5

Features: 2

Enhancements: 1

Bug Fixes: 2

ServiceNow Cases: 5

Collection Status: SUCCESS

Artifact:

output/artifacts/ai/collected-release-data.json
```

---

# Success Criteria

The command is successful when:

- Release data has been located.
- ServiceNow data has been located.
- All JSON files have been validated.
- Release metadata has been preserved.
- Work Items and ServiceNow Cases have been linked.
- A consolidated release dataset has been generated.
- The dataset has been saved to:

```text
output/artifacts/ai/collected-release-data.json
```

No analysis should be performed.

No release notes should be generated.

---

# Future MCP Integration

## Azure DevOps MCP

Future tools:

- get_release()
- get_release_manifest()
- get_work_item(workItemId)
- get_work_items(workItemIds)
- get_acceptance_criteria(workItemId)
- get_comments(workItemId)

Purpose:

Retrieve release metadata and detailed Work Item information.

---

## ServiceNow MCP

Future tools:

- get_case(caseNumber)
- get_cases(caseNumbers)
- get_resolution(caseNumber)
- get_customer_impact(caseNumber)
- get_root_cause(caseNumber)

Purpose:

Retrieve customer case information linked to Azure DevOps Work Items.

---

# Future Enhancements

- Automatically retrieve Release Packages from Azure DevOps.
- Support multiple releases.
- Detect duplicate Work Items.
- Detect missing linked customer cases.
- Validate release completeness.
- Cache previously retrieved Work Items.
- Generate collection metrics.
- Support incremental release updates.