# File: `README.md`

# Release Notes AI

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

## Overview

AI prepares a structured darft in Document360 using the organization's release note template. Technica Writers and SME's review, refine and approve the content before it is published. 

Release Notes AI is a Proof of Concept (POC) that demonstrates how AI can automate the creation of customer-facing release notes using a modular, agent-based architecture.

The solution uses mock release data to simulate enterprise systems and demonstrates AI engineering concepts including:

- AI Agents
- Prompt Engineering
- Reusable Skills
- Workflow Automation
- Modular Architecture
- MCP-ready Design
- GitHub-based Project Structure

The POC intentionally avoids direct integration with enterprise systems such as Azure DevOps, ServiceNow, and Document360. Instead, it uses mock data to validate the workflow before introducing production integrations.

# Not included in POC

- Audience based classification: Technical (for internals) and Non-technical (for customers)
- Future MCP integrations and Enterprise Automation (Phase 2 and 3 as stated below)

---

## Objectives

- Demonstrate end-to-end release note generation.
- Showcase reusable AI engineering patterns.
- Produce publication-ready release notes.
- Build an architecture that can later connect to enterprise systems through MCP.

---

# Business Value

## Benefits

### Technical Writers

- Less repetitive work
- More focus on quality
- Faster reviews

### Product Teams

- Consistent release notes
- Faster turnaround
- Better communication

### Organization

- Standardized process
- AI-assisted documentation
- Human governance
- Ready for enterprise integrations
- Technical and non-technical release notes

## End-to-End Workflow

```text
AI Workflow
/create-release-draft
        │
        ▼
Collector
        ▼
Analyzer
        ▼
Writer
        ▼
Reviewer
        ▼
Draft Generator
        │
        ▼
Document360 Draft
        │
        ▼
══════════════════════
 Human Review Gateway
══════════════════════
        │
        ├── Technical Writer Review
        ├── SME Review
        ├── Compliance/QA Review (optional)
        └── Approval
══════════════════════
        │
        ▼
Publish
```
---

## Collector agent

```text

                 Azure DevOps JSON
                        │
                        │
ServiceNow JSON         │
        │               │
        └──────┬────────┘
               │
               ▼
        Collector Agent
               │
               ▼
 collected-release-data.json
```
---

## Current Status

- ✅ Mock data
- ✅ Analyzer Prompt
- ✅ Writer Prompt
- ✅ Reviewer Prompt
- ✅ Skills
- ✅ Agent Definitions
- ✅ Commands
- ⏳ Mock MCP
- ⏳ GitHub Workflow
- ⏳ Enterprise Integrations

## Latest Progress

The project has evolved from a local mock-data workflow into a simulated enterprise AI pipeline using Model Context Protocol (MCP).

"At this stage, the Collector is already designed to orchestrate multiple enterprise systems. Today those systems are mocked with local MCP responses. Replacing them with real Azure DevOps and ServiceNow MCP servers would not require changes to the downstream AI agents because they consume the consolidated release dataset rather than the individual source systems."

### Current Architecture

- ✅ Azure DevOps MCP (Mock)
- ✅ ServiceNow MCP (Mock)
- ✅ Collector Agent orchestrates both MCP sources
- ✅ Consolidated release dataset generation
- ⏳ Analyzer Agent (next phase)
- ⏳ Writer Agent
- ⏳ Reviewer Agent
- ⏳ Document360 MCP

### Current Workflow

```text
Azure DevOps MCP
        │
        ▼
ServiceNow MCP
        │
        ▼
Collector Agent
        │
        ▼
collected-release-data.json
        │
        ▼
Analyzer Agent
```

The current implementation uses mock MCP responses while preserving the same architecture that will be used with live enterprise integrations.

---

## Future MCP Architecture

Nothing changes inside the agents. Only the data source changes.

Azure DevOps MCP

↓

ServiceNow MCP

↓

Document360 MCP

Because the workflow is modular, replacing mock data with live systems doesn't require redesigning the solution.

## Future Roadmap

- Azure DevOps MCP
- ServiceNow MCP
- Document360 Publisher
- GitHub Actions
- Cursor Commands
- Automated Publishing

# Phase 1 (Completed)

✅ Local POC

✅ AI Agents

✅ Skills

✅ Prompts

✅ Commands

✅ Release Note Generation Pipeline

# Phase 2

- Azure DevOps MCP
- ServiceNow MCP
- Document360 MCP
- GitHub Actions

# Phase 3

Enterprise Automation

- Scheduled releases
- Automated draft creation
- Notification workflows

# Key Takeaways

- AI supports the documentation process without replacing human expertise.
- The workflow is modular, making it easy to test, maintain, and extend.
- The architecture is designed to integrate with enterprise systems through MCP.
- This proof of concept provides a foundation for future automation while preserving governance and quality.

This proof of concept demonstrates that AI can assist Technical Writers by automating repetitive documentation tasks while keeping human review and approval at the center of the publishing process. The next step isn't to redesign the workflow—it's simply to replace the mock data with live integrations to Azure DevOps, ServiceNow, and Document360.

## Repository


| Component                  | Status     |
| -------------------------- | ---------- |
| Repository                 | ✅          |
| Commands                   | ✅ 6        |
| Agents                     | ✅ 5        |
| Prompts                    | ✅ 5        |
| Skills                     | ✅ Reusable |
| Architecture documentation | ✅          |
| Workflow documentation     | ✅          |
| MCP placeholders           | ✅          |
| Output artifacts           | ✅          |
| Mock data                  | ✅          |
| End-to-end pipeline        | ✅          |
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
This repository separates orchestration, prompting, reusable knowledge, and generated artifacts. That makes the solution easier to maintain and extend.


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

