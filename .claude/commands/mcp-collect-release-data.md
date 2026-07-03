# File: `.claude/commands/mcp-collect-release-data.md`

# /mcp-collect-release-data

## Purpose

Build a consolidated release dataset by retrieving release information from enterprise systems through Model Context Protocol (MCP) servers.

This command simulates an enterprise AI workflow by retrieving release information from:

- Azure DevOps MCP
- ServiceNow MCP

The retrieved information is merged into a single release dataset that becomes the input for downstream AI agents.

For this Proof of Concept (POC), MCP responses are simulated using local mock JSON files.

This command does **not**:

- Analyze release information
- Generate release notes
- Perform AI quality review
- Create Document360 drafts

---

# Usage

```text
/mcp-collect-release-data 2025.8
```

---

# Enterprise Workflow

```text
                Collector Agent
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
 Azure DevOps MCP            ServiceNow MCP
 get_release()               get_cases()
 get_work_items()
          │                         │
          └────────────┬────────────┘
                       ▼
        Merge Release Information
                       │
                       ▼
 output/artifacts/ai/collected-release-data.json
```

---

# MCP Servers

This command communicates with the following MCP servers.

## Azure DevOps MCP

Purpose:

Retrieve release metadata and Work Item information.

Current POC Response:

```text
mcp/azure-devops/responses/work-items.json
```

---

## ServiceNow MCP

Purpose:

Retrieve customer case information.

Current POC Response:

```text
mcp/servicenow/responses/resolved-incidents.json
```

---

# Instructions

## Stage 1 — Connect to Azure DevOps MCP

Connect to the Azure DevOps MCP server.

Execute:

```text
get_release()
```

Retrieve:

- Release Version
- Release Tag
- Build Number

---

Execute:

```text
get_work_items()
```

Retrieve:

- Work Item IDs
- Titles
- Descriptions
- Work Item Type
- Area
- State
- Acceptance Criteria
- Tags
- Linked ServiceNow Case Numbers

Current POC response:

```text
mcp/azure-devops/responses/work-items.json
```

---

## Stage 2 — Connect to ServiceNow MCP

Connect to the ServiceNow MCP server.

Execute:

```text
get_cases()
```

Retrieve:

- Case Numbers
- Customer Issues
- Resolution Summaries
- Customer Impact
- Root Cause

Current POC response:

```text
mcp/servicenow/responses/resolved-incidents.json
```

---

## Stage 3 — Validate Retrieved Information

Verify that:

- Azure DevOps response exists.
- ServiceNow response exists.
- JSON responses are valid.
- Every linked ServiceNow Case exists.
- Required release metadata is available.

Stop the workflow if validation fails.

---

## Stage 4 — Merge Enterprise Data

Create a consolidated release dataset.

Merge:

Azure DevOps

- Release metadata
- Work Items
- Acceptance Criteria
- Tags

with

ServiceNow

- Customer Issues
- Resolution Summaries
- Customer Impact
- Root Cause

Maintain traceability between:

- Work Item IDs
- ServiceNow Case Numbers

Do not modify the source responses.

---

## Stage 5 — Generate Release Dataset

Create:

```text
output/artifacts/ai/collected-release-data.json
```

This dataset becomes the single source of truth for all downstream AI agents.

---

## Stage 6 — Display Collection Summary

Display:

- Release Version
- Release Tag
- Build Number
- Total Work Items Retrieved
- Total Customer Cases Retrieved
- Collection Status

Do not perform analysis.

Do not generate release notes.

---

# Output

Generate:

```text
output/artifacts/ai/collected-release-data.json
```

---

# Expected Console Output

```text
=========================================
MCP Release Data Collection
=========================================

Connecting to Azure DevOps MCP...
✓ Connected

Retrieving Release Metadata...
✓ Complete

Retrieving Work Items...
✓ 5 Work Items Retrieved

Connecting to ServiceNow MCP...
✓ Connected

Retrieving Customer Cases...
✓ 4 Cases Retrieved

Validating Enterprise Data...
✓ Validation Successful

Merging Release Dataset...
✓ Complete

Artifact Created:

output/artifacts/ai/collected-release-data.json

Collection Status:

SUCCESS
=========================================
```

---

# Success Criteria

The command is successful when:

- Azure DevOps MCP has returned release information.
- ServiceNow MCP has returned customer case information.
- All JSON responses have been validated.
- Work Items and Customer Cases have been linked.
- Traceability has been preserved.
- A consolidated release dataset has been generated.
- The dataset has been saved to:

```text
output/artifacts/ai/collected-release-data.json
```

No analysis should be performed.

No release notes should be generated.

---

# Current POC

Current implementation uses mock MCP responses located in:

```text
mcp/
├── azure-devops/
│   └── responses/
│       └── work-items.json
│
└── servicenow/
    └── responses/
        └── resolved-incidents.json
```

---

# Future Production Implementation

The mock responses will be replaced with real MCP servers connected to:

- Azure DevOps
- ServiceNow

No changes will be required to downstream AI agents because they consume the consolidated release dataset rather than directly interacting with enterprise systems.

---

# Next Step

After successful collection, execute:

```text
/mcp-analyze-release 2025.8
```