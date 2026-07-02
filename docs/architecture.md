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

