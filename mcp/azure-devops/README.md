# File: `mcp/azure-devops/README.md`

# Azure DevOps MCP Server

## Overview

The Azure DevOps MCP Server provides a standardized interface between AI agents and Azure DevOps.

Its primary responsibility is to retrieve release-related information required to automate the generation of customer-facing release notes.

For the current Proof of Concept (POC), the MCP server is represented conceptually and returns data from local mock JSON files.

In a production implementation, the server will communicate directly with Azure DevOps using the Azure DevOps REST APIs.

---

# Purpose

The Azure DevOps MCP Server abstracts the complexity of Azure DevOps from AI agents.

Instead of querying Azure DevOps directly, agents interact with a small set of business-oriented MCP tools.

This approach provides:

* Loose coupling
* Improved maintainability
* Easier testing
* Reusable integrations
* Future scalability

---

# Architecture

```text
Claude Code
      │
      ▼
Collector Agent
      │
      ▼
Azure DevOps MCP Server
      │
      ▼
Azure DevOps REST API
```

Current POC

```text
Collector Agent
      │
      ▼
Azure DevOps MCP
      │
      ▼
data/release-2025.8.json
```

---

# Responsibilities

The Azure DevOps MCP Server is responsible for:

* Retrieving completed work items
* Retrieving completed features
* Retrieving completed bugs
* Retrieving user stories
* Retrieving release metadata
* Returning structured JSON

The MCP server does **not**:

* Generate release notes
* Classify work items
* Apply writing standards
* Perform quality reviews

Those responsibilities belong to the AI agents.

---

# AI Agents Using This MCP

Collector Agent

Future:

* Analyzer Agent
* Metrics Agent

---

# Workflows Using This MCP

* Generate Release Notes
* Generate Release Package
* Release Metrics (Future)

---

# Current POC Implementation

Current data source:

```text
data/
└── release-2025.8.json
```

Future data source:

```text
Azure DevOps
REST API
```

---

# Future Enhancements

* Authentication using Personal Access Tokens (PAT)
* Azure Entra ID authentication
* Incremental synchronization
* Multiple project support
* Sprint filtering
* Release filtering
* Work Item relationships
* Automatic pagination
* Error handling and retries

---

# Related Documents

* tools.md
* Collector Agent
* Generate Release Notes Workflow
* Architecture
* Design Decisions
