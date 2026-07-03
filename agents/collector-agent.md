# File: `agents/collector-agent.md`

# Collector Agent

## Purpose

Build an enriched release dataset that serves as the single source of truth for all downstream AI agents.

The Collector Agent is responsible for gathering all release-related information required to generate customer-facing release notes.

For the current Proof of Concept (POC), the Collector Agent retrieves release information from local mock JSON files that simulate enterprise systems.

In the future production solution, the Collector Agent will retrieve and merge release information from Azure DevOps and ServiceNow through MCP (Model Context Protocol) servers, producing a consolidated release dataset for AI processing.

The Collector Agent does **not** analyze, summarize, or rewrite release information. Its responsibility is to collect, validate, and consolidate release data.

---

# Responsibilities

## Current POC

The Collector Agent:

- Retrieve release data for a specified release version.
- Retrieve related ServiceNow case information.
- Validate that all required mock data exists.
- Verify that all JSON files are valid.
- Merge release information into a consolidated dataset.
- Preserve relationships between Work Items and ServiceNow cases.
- Pass the collected release dataset to the Analyzer Agent.
- Log missing or invalid data.

---

## Future Production

The Collector Agent will:

- Receive the Release Package generated from Azure DevOps.
- Extract all Azure DevOps Work Item IDs.
- Extract all linked ServiceNow Case Numbers.
- Retrieve detailed Work Item information from Azure DevOps MCP.
- Retrieve detailed Customer Case information from ServiceNow MCP.
- Merge all information into an enriched release dataset.
- Preserve traceability between Work Items and Customer Cases.
- Validate retrieved information.
- Pass the enriched release dataset to downstream AI agents.

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
             │
             ▼
Analyzer Agent
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
 ┌───────┴────────┐
 ▼                ▼
Azure DevOps MCP  ServiceNow MCP
get_work_items()  get_cases()
 ▼                ▼
Retrieve WI       Retrieve Cases
         │
         └───────┬────────┘
                 ▼
 Merge & Enrich Release Data
                 │
                 ▼
collected-release-data.json
                 │
                 ▼
Analyzer Agent
```

---

# Inputs

## Current POC

The Collector Agent reads the following mock data:

```text
data/release-2025.8.json

data/service-now-2025.8.json
```

---

## Future Production

The Collector Agent will receive a Release Package containing:

- Release Version
- Release Tag
- Build Number
- Azure DevOps Work Item IDs
- Linked ServiceNow Case Numbers

---

# Skills Used

## Current POC

None

---

## Future

- Data Validation
- Data Normalization
- Duplicate Detection
- Traceability Validation

---

# Prompt Used

None.

The Collector Agent retrieves structured information and prepares it for downstream AI agents.

---

# Output

## Current POC

```text
output/artifacts/ai/collected-release-data.json
```

---

## Future Production

The generated dataset will contain:

- Release metadata
- Azure DevOps Work Item information
- ServiceNow Case information
- Customer issue summaries
- Resolution summaries
- Customer impact
- Functional area
- Work Item categorization
- Traceability between Work Items and Customer Cases

This enriched dataset becomes the single source of truth for all downstream AI agents.

---

# Success Criteria

The Collector Agent is successful when:

- All required release information has been retrieved.
- All linked ServiceNow cases have been retrieved.
- Release metadata has been preserved.
- Traceability between Work Items and Customer Cases has been maintained.
- Duplicate records have been identified.
- Missing information has been reported.
- A consolidated release dataset has been generated.
- The dataset is ready for analysis.

---

# Future MCP Integrations

## Azure DevOps MCP

Available tools:

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

Available tools:

- get_case(caseNumber)
- get_cases(caseNumbers)
- get_resolution(caseNumber)
- get_customer_impact(caseNumber)
- get_root_cause(caseNumber)

Purpose:

Retrieve customer case information linked to Azure DevOps Work Items.

---

## Document360 MCP

Available tools:

- search_existing_release_notes()
- get_article()
- get_category()

Purpose:

Support duplicate detection and future release note traceability.

---

# Future Enhancements

- Automatically retrieve the Release Package from Azure DevOps.
- Support multiple simultaneous releases.
- Merge information from additional enterprise systems.
- Detect duplicate Work Items.
- Detect missing linked customer cases.
- Validate release completeness.
- Cache previously retrieved Work Items.
- Support incremental release updates.
- Generate collection metrics and audit reports.
- Provide collection statistics for AI quality review.

---

# Version History


| Version | Description                                                                         |
| ------- | ----------------------------------------------------------------------------------- |
| 1.0     | Initial Proof of Concept using local mock data.                                     |
| 2.0     | Planned MCP integration with Azure DevOps and ServiceNow for enterprise automation. |


