# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

---

# Project Overview

This repository contains a Proof of Concept (POC) for AI-assisted release note generation.

The project demonstrates how multiple AI agents can collaborate to automatically collect, analyze, write, review, and prepare release notes for publication.

The architecture has been designed to evolve from local mock data into enterprise integrations using Model Context Protocol (MCP).

---

# Project Objectives

The objectives of this POC are to demonstrate:

- AI-assisted release note generation
- Multi-agent orchestration
- Enterprise MCP integrations
- Human-in-the-loop documentation review
- Document360 draft generation
- Future-ready Docs-as-Code workflows

---
# End-to-end Architecture
```text

                 User

                   │

                   ▼

      /mcp-generate-release-notes

                   │

                   ▼

          Pipeline Orchestrator

                   │

      ┌────────────┼─────────────┐

      ▼            ▼             ▼

Azure DevOps     ServiceNow   Document360
     MCP             MCP          MCP

      │              │

      └──────┬───────┘

             ▼

      Collector Agent

             ▼

collected-release-data.json

             ▼

      Analyzer Agent

             ▼

 analyzed-release.json

             ▼

       Writer Agent

             ▼

 release-notes.md

             ▼

      Reviewer Agent

             ▼

 review-report.md

             ▼

 Document360 Draft

             ▼

document360-draft.md

             ▼

 Technical Writer

             ▼

      Manual Approval

             ▼

      Publish
```
# Current POC Phases

## Phase 1 — Local Mock Workflow

The pipeline retrieves release information from local JSON files.

Workflow:
```text

Release Data

↓

Collector

↓

Analyzer

↓

Writer

↓

Reviewer

↓

Document360 Draft
```
---

## Phase 2 — Repository Automation

Repository validation and pipeline orchestration.

Includes:

- GitHub Actions
- Repository validation
- Python orchestration
- Artifact generation

---

## Phase 3 — MCP Enterprise Workflow (Current)

The Collector Agent retrieves release information through simulated MCP servers.

Current integrations:

- Azure DevOps MCP
- ServiceNow MCP

Future:

- Document360 MCP

---

# End-to-End Workflow

```
                Azure DevOps MCP
                       │
               get_release()
               get_work_items()
                       │
                       ▼
                Collector Agent
                       │
                get_cases()
                       ▲
                       │
                ServiceNow MCP
                       │
                       ▼
      collected-release-data.json
                       │
                       ▼
                Analyzer Agent
                       │
             analyzed-release.json
                       │
                       ▼
                 Writer Agent
                       │
             release-notes.md
                       │
                       ▼
                Reviewer Agent
                       │
             review-report.md
                       │
                       ▼
             Document360 MCP
             create_draft()
                       │
                       ▼
          document360-draft.md
```

---

# AI Agents

| Stage | Agent           | Input                             | Output                      |
| ----- | --------------- | --------------------------------- | --------------------------- |
| 1     | Collector       | Azure DevOps MCP + ServiceNow MCP | collected-release-data.json |
| 2     | Analyzer        | collected-release-data.json       | analyzed-release.json       |
| 3     | Writer          | analyzed-release.json             | release-notes.md            |
| 4     | Reviewer        | release-notes.md                  | review-report.md            |
| 5     | Draft Generator | release-notes + review            | document360-draft.md        |


## Collector Agent

Purpose

Collect release information from enterprise systems.

Responsibilities

- Retrieve release metadata
- Retrieve Work Items
- Retrieve ServiceNow cases
- Merge enterprise information
- Generate collected-release-data.json

---

## Analyzer Agent

Purpose

Analyze collected release information.

Responsibilities

- Classify Work Items
- Determine customer-facing changes
- Group release items
- Prepare structured release information

Output

```
output/artifacts/ai/analyzed-release.json
```

---

## Writer Agent

Purpose

Generate release notes.

Responsibilities

- Produce customer-friendly content
- Apply release note template
- Generate Markdown

Output

```
output/artifacts/ai/release-notes.md
```

---

## Reviewer Agent

Purpose

Perform AI quality review.

Responsibilities

- Validate writing quality
- Validate metadata
- Validate completeness
- Produce review report

Output

```
output/artifacts/ai/review-report.md
```

---

## Draft Generator Agent

Purpose

Generate a Document360-ready draft.

Responsibilities

- Apply article template
- Populate metadata
- Preserve traceability
- Prepare Draft status

Output

```
output/artifacts/publishing/document360-draft.md
```

---
# Directory structure

| Directory        | Purpose               |
| ---------------- | --------------------- |
| .claude/commands | Claude commands       |
| .claude/prompts  | Prompt templates      |
| .claude/skills   | RTCCO skills          |
| agents           | Agent specifications  |
| automation       | Python orchestration  |
| ci               | Validation scripts    |
| docs             | Architecture & design |
| mcp              | Mock MCP servers      |
| output           | Generated artifacts   |
| validation       | Validation reports    |

---
# Key files
| File                      | Description                |
| ------------------------- | -------------------------- |
| ```README.md```                | Project overview           |
| ```CLAUDE.md```                 | Repository playbook        |
| ```release-note-pipeline.yml``` | GitHub workflow            |
| ```validate_repository.py```    | Repository validator       |
| ```pipeline_orchestrator.py```  | Master Python orchestrator |
| ```collector-agent.md```        | Collector definition       |
| ```analyzer-agent.md```         | Analyzer definition        |
| ```writer-agent.md```           | Writer definition          |
| ```reviewer-agent.md```         | Reviewer definition        |
| ```draft-generator-agent.md```  | Draft Generator definition |

---
# Mapping rules (Analyzer)
| Azure DevOps Type | Analyzer Category | Release Note Section |
| ----------------- | ----------------- | -------------------- |
| Feature           | Feature           | New Features         |
| Enhancement       | Enhancement       | Enhancements         |
| Bug               | Bug Fix           | Bug Fixes            |
| Technical Task    | Ignore            | Internal             |
| Infrastructure    | Ignore            | Internal             |

---

# Output files
| Artifact                    | Generated By    | Purpose                |
| --------------------------- | --------------- | ---------------------- |
| ```collected-release-data.json``` | Collector       | Enterprise dataset     |
| ```analyzed-release.json```       | Analyzer        | Structured release     |
| ```release-notes.md```            | Writer          | Customer release notes |
| ```review-report.md```            | Reviewer        | AI QA                  |
| ```document360-draft.md```        | Draft Generator | Ready for TW           |

---

# MCP Servers

## Azure DevOps MCP

Current POC

Mock responses

```
mcp/azure-devops/
```

Provides

- Release Metadata
- Work Items
- Build Information

Future

Azure DevOps REST API

---

## ServiceNow MCP

Current POC

Mock responses

```
mcp/servicenow/
```

Provides

- Customer Cases
- Resolution Details
- Customer Impact

Future

Live ServiceNow MCP

---

## Document360 MCP

Current Status

Planned

Future Responsibilities

- Create Draft
- Update Draft
- Search Articles
- Publish (Manual Approval)

---

# Claude Commands

## Phase 1 Commands

```
/collect-release-data

/analyze-release

/write-release-notes

/review-release-notes

/create-release-draft
```

---

## Phase 3 MCP Commands

```
/mcp-collect-release-data

/mcp-analyze-release

/mcp-write-release-notes

/mcp-review-release-notes

/mcp-create-release-draft
```

---

# Skills

The project uses reusable Claude Skills for:

- Release Note Template
- Metadata Generation
- Quality Review
- Customer-friendly Language
- Release Classification

---

# Repository Structure

```
.claude/
    commands/
    prompts/
    skills/

agents/

automation/

ci/

data/

docs/

mcp/
    azure-devops/
    servicenow/
    document360/

output/
    artifacts/
        ai/
        publishing/

validation/
```

---

# Generated Artifacts

Collector

```
collected-release-data.json
```

Analyzer

```
analyzed-release.json
```

Writer

```
release-notes.md
```

Reviewer

```
review-report.md
```

Draft Generator

```
document360-draft.md
```

---

# Current POC Scope

The project currently demonstrates:

✅ Multi-agent orchestration

✅ Azure DevOps MCP simulation

✅ ServiceNow MCP simulation

✅ Enterprise data consolidation

✅ AI release note generation

| Phase   | Description                                     | Status  |
| ------- | ----------------------------------------------- | ------- |
| Phase 1 | Local JSON POC                                  | ✅       |
| Phase 2 | Repository Automation (GitHub Actions + Python) | ✅       |
| Phase 3 | MCP Enterprise Integration                      | 🚧      |
| Phase 4 | Live Enterprise MCP                             | Planned |
| Phase 5 | End-to-End One-Command Automation               | Planned |


Future phases will replace the mock MCP responses with live enterprise integrations while preserving the same AI pipeline.

---

# Working Principles

- Never invent release information.
- Preserve traceability between Work Items and ServiceNow cases.
- Maintain separation between enterprise systems and AI agents.
- The Collector is responsible only for collecting and merging data.
- Analysis is performed only by the Analyzer Agent.
- Human review is always required before publication.
- Document360 drafts must never be published automatically.

---

# Future Roadmap

Phase 4

- Live Azure DevOps MCP
- Live ServiceNow MCP
- Live Document360 MCP

Phase 5

- Azure DevOps Wiki
- Automated Release Pipelines
- CI/CD Integration
- GitHub Actions orchestration
- One-command release note generation

---

# Success Criteria

The POC is successful when a single command can orchestrate:
```
Azure DevOps MCP

↓

ServiceNow MCP

↓

Collector

↓

Analyzer

↓

Writer

↓

Reviewer

↓

Document360 Draft
```
while preserving traceability, AI quality review, and human approval before publication.

---
# Troubleshooting
| Problem              | Solution                   |
| -------------------- | -------------------------- |
| Missing MCP response | Verify JSON exists         |
| Validation failed    | Run validate_repository.py |
| Pipeline stopped     | Check Collector logs       |
| Missing artifacts    | Run Collector again        |
