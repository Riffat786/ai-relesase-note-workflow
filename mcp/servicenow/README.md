# File: `mcp/servicenow/README.md`

# ServiceNow MCP Server

## Overview

The ServiceNow MCP Server provides a standardized interface between AI agents and ServiceNow.

Its primary responsibility is to retrieve operational and release-related information that complements development work items during release note generation.

For the current Proof of Concept (POC), the MCP server is represented conceptually and returns data from local mock JSON files.

In a production implementation, the server will communicate directly with ServiceNow using the ServiceNow REST APIs.

---

# Purpose

The ServiceNow MCP Server abstracts ServiceNow implementation details from AI agents.

Instead of querying ServiceNow directly, AI agents consume business-oriented MCP tools.

This provides:

* Standardized access
* Loose coupling
* Improved maintainability
* Easier testing
* Enterprise scalability

---

# Architecture

```text
Claude Code
      │
      ▼
Collector Agent
      │
      ▼
ServiceNow MCP Server
      │
      ▼
ServiceNow REST API
```

Current POC

```text
Collector Agent
      │
      ▼
ServiceNow MCP
      │
      ▼
Mock JSON
```

---

# Responsibilities

The ServiceNow MCP Server is responsible for:

* Retrieving Change Requests
* Retrieving Incidents
* Retrieving Problems
* Retrieving Release Information
* Returning structured JSON

The MCP server does **not**:

* Generate release notes
* Review documentation
* Apply writing standards
* Publish documentation

---

# AI Agents Using This MCP

Current

* Collector Agent

Future

* Change Impact Agent
* Release Metrics Agent

---

# Workflows Using This MCP

* Generate Release Notes
* Generate Release Package
* Release Readiness Assessment (Future)

---

# Current POC Implementation

Current data source

```text
data/
└── servicenow-release.json
```

Future

```text
ServiceNow REST API
```

---

# Future Enhancements

* OAuth authentication
* Multiple ServiceNow instances
* Change approval status
* CAB information
* Deployment schedules
* Incident correlation
* Release calendar integration
* Error handling and retries

---

# Related Documents

* tools.md
* Collector Agent
* Generate Release Notes Workflow
* Architecture
* Design Decisions
