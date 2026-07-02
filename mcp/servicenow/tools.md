# File: `mcp/servicenow/tools.md`

# ServiceNow MCP Tools

## Overview

This document defines the business-oriented tools exposed by the ServiceNow MCP Server.

These tools provide operational information used during release note generation.

---

# Tool Catalogue

## get_change_requests()

### Purpose

Retrieve approved change requests associated with a release.

---

### Used By

* Collector Agent

---

### Input

| Parameter      | Type   | Required |
| -------------- | ------ | -------- |
| releaseVersion | String | Yes      |

---

### Output

```json
{
  "release": "2025.8",
  "changes": []
}
```

Current POC

Returns mock JSON.

Future

Returns ServiceNow data.

---

## get_incidents()

### Purpose

Retrieve resolved incidents associated with a release.

---

### Used By

Collector Agent

---

## get_problems()

### Purpose

Retrieve completed problems addressed during the release.

---

### Used By

Collector Agent

---

## get_release_schedule()

### Purpose

Retrieve planned deployment information.

---

## Future Tools

* get_cab_approvals()
* get_known_errors()
* get_release_calendar()
* get_post_implementation_reviews()
* get_problem_relationships()

---

# Design Principles

Every MCP tool should:

* Return structured JSON.
* Have a single responsibility.
* Hide ServiceNow implementation details.
* Be reusable across workflows.

---

# Tool Flow

```text
Collector Agent
        │
        ▼
get_change_requests()
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
ServiceNow REST API
        │
        ▼
ServiceNow MCP Server
        │
        ▼
Collector Agent
```
