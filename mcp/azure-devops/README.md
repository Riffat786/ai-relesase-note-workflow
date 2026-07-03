# Azure DevOps MCP Server

## Purpose

Provides AI agents with secure access to Azure DevOps release information.

The Azure DevOps MCP server retrieves release metadata and detailed Work Item information required for release note generation.

For this Proof of Concept (POC), responses are simulated using local mock JSON files.

Future versions will retrieve information directly from Azure DevOps through the Azure DevOps REST API.

---

## Consumers

- Collector Agent

---

## Supported Workflow

Collector Agent

↓

Azure DevOps MCP

↓

Release Package

↓

Work Items

↓

Collector merges information with ServiceNow

↓

Collected Release Dataset

---

## Available Tools

- get_release()
- get_work_items()
- get_work_item()
- get_comments()
- get_acceptance_criteria()

---

## Current Implementation

Mock JSON

---

## Future Implementation

Azure DevOps REST API