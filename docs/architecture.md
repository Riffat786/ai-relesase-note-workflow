# File: `docs/architecture.md`

# Architecture

## Solution Overview

The solution follows a modular AI workflow where each agent has a single responsibility.

The AI solution collects release data, analyzes customer impact, generates customer-facing release notes, performs an automated quality review, and prepares a Document360 draft for Technical Writer and SME review. The AI never publishes content—publication remains a human responsibility

```text
Release Manager
        │
        ▼
Collector Agent
        │
        ▼
Analyzer Agent
        │
        ▼
Writer Agent
        │
        ▼
Reviewer Agent
        │
        ▼
Draft generator Agent
        │
        ▼
Document360 Draft
        │
        ▼
Technical Writer
        │
        ▼
SME
        │
        ▼
Approve
        │
        ▼
Publish
```

# What did I build:

```text
Mock Release Data
        │
        ▼
/collect-release-data
        │
        ▼
collected-release-data.json
        │
        ▼
/analyze-release
        │
        ▼
analyzed-release.json
        │
        ▼
/write-release-notes
        │
        ▼
release-notes.md
        │
        ▼
/review-release-notes
        │
        ▼
review-report.md
        │
        ▼
/create-release-draft
        │
        ▼
document360-draft.md
        │
        ▼
Technical Writer Review
        │
        ▼
SME Review
        │
        ▼
Publish to Document360
```

---

## Command dependency diagram

```text

User
    │
    ▼
Command
    │
    ▼
Agent
    │
    ├── Prompt
    └── Skills
    │
    ▼
Artifacts

```

---

## Layers

### Data Layer

- Mock Release JSON
- Mock ServiceNow JSON
- Future Azure DevOps
- Future ServiceNow

---

### AI Layer

Agents

- Collector
- Analyzer
- Writer
- Reviewer
- Draft generator

Prompts

- Analyze Release
- Write Release Notes
- Review Release Notes
- Create draft Document360

Skills

- Classification Rules
- Customer-Friendly Language
- Release Note Template
- Release Note Metadata
- Quality Review Checklist

---

### Output Layer

Artifacts

- analyzed-release.json
- release-notes.md
- review-report.md

Logs

- Workflow execution logs
- Future audit logs

---

## Design Principles

- Modular
- Reusable
- Maintainable
- MCP-ready
- Prompt-driven
- Agent-oriented
- Enterprise scalable

## Future MCP Architecture

```
      Azure DevOps MCP
             │
             │
  ServiceNow MCP
             │
             ▼
     Collector Agent
             │
             ▼
  collected-release-data.json
```
```text
                Azure DevOps
          (Release Package)
                     │
                     ▼
             Collector Agent
       ┌─────────────┴─────────────┐
       ▼                           ▼
 Azure DevOps MCP           ServiceNow MCP
 get_work_items()           get_cases()
       │                           │
       └─────────────┬─────────────┘
                     ▼
      collected-release-data.json
                     │
                     ▼
             Analyzer Agent
                     │
                     ▼
          analyzed-release.json
                     │
                     ▼
              Writer Agent
                     │
                     ▼
             release-notes.md
                     │
                     ▼
             Reviewer Agent
                     │
                     ▼
            review-report.md
                     │
                     ▼
             Document360 MCP
              create_draft()
                     │
                     ▼
         document360-draft.md
                     │
                     ▼
        Technical Writer Review
                     │
                     ▼
              SME Approval
                     │
                     ▼
                 Publish
```
---

# Milestone: MCP-Based Data Collection

## Overview

The Collector Agent has been enhanced to simulate enterprise integrations using Model Context Protocol (MCP).

Instead of relying solely on local mock data, the Collector now orchestrates data retrieval from multiple enterprise systems through dedicated MCP interfaces.

Current mock integrations include:

- Azure DevOps MCP
- ServiceNow MCP

The Collector retrieves release metadata, work item information, and customer case details before merging them into a single consolidated release dataset.

This dataset becomes the single source of truth for downstream AI agents.

## Current Workflow

```text
                Collector Agent
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Azure DevOps MCP              ServiceNow MCP
  get_release()                  get_cases()
  get_work_items()
        │                             │
        └──────────────┬──────────────┘
                       ▼
      collected-release-data.json
                       │
                       ▼
              Analyzer Agent
```

## Current POC Implementation

The MCP integrations are currently simulated using local mock responses.

Azure DevOps

```text
mcp/azure-devops/responses/work-items.json
```

ServiceNow

```text
mcp/servicenow/responses/resolved-incidents.json
```

The architecture has been designed so these mock responses can later be replaced with live MCP servers without changing downstream AI agents.
