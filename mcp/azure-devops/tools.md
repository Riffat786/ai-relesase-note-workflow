# File: `mcp/azure-devops/tools.md`

# Azure DevOps MCP Tools

## Overview

This document defines the business-oriented tools exposed by the Azure DevOps MCP Server.

These tools are consumed by AI agents rather than calling Azure DevOps APIs directly.

---

# Tool Catalogue

## get_release_work_items()

### Purpose

Retrieve all completed work items for a specified release.

---

### Used By

* Collector Agent

---

### Input

| Parameter      | Type   | Required |
| -------------- | ------ | -------- |
| releaseVersion | String | Yes      |

Example

```text
2025.8
```

---

### Output

```json
{
  "release": "2025.8",
  "items": []
}
```

---

### Current POC

Returns:

```text
data/release-2025.8.json
```

Future:

Azure DevOps REST API

---

## get_completed_features()

### Purpose

Retrieve completed customer-facing features.

---

### Used By

Collector Agent

---

### Output

Feature work items only.

---

## get_completed_bugs()

### Purpose

Retrieve completed customer-facing bug fixes.

---

### Used By

Collector Agent

---

### Output

Bug work items only.

---

## get_user_stories()

### Purpose

Retrieve completed user stories associated with a release.

---

### Used By

Collector Agent

---

## get_release_metadata()

### Purpose

Retrieve release information including:

* Version
* Sprint
* Release date
* Project

---

## Future Tools

* search_work_items()
* get_work_item_comments()
* get_linked_work_items()
* get_release_metrics()
* get_pull_requests()
* get_test_results()
* get_deployment_status()

---

# Design Principles

Each MCP tool should:

* Have a single responsibility.
* Return structured JSON.
* Be reusable.
* Be independent of AI prompts.
* Hide implementation details from AI agents.

---

# Tool Flow

```text
Collector Agent
        │
        ▼
get_release_work_items()
        │
        ▼
Structured JSON
        │
        ▼
Analyzer Agent
```

---

# Future Implementation

Current

```text
Mock JSON
```

Future

```text
Azure DevOps REST API
        │
        ▼
Azure DevOps MCP Server
        │
        ▼
Collector Agent
```
