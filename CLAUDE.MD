# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# Quick Start

**Run the entire release note pipeline locally:**

```bash
# From the project root directory
python automation/pipeline_orchestrator.py
```

This orchestrates all five stages in sequence:
1. **Collector** — consolidates mock release data from `data/`
2. **Analyzer** — classifies and structures the release information
3. **Writer** — generates customer-facing release notes
4. **Reviewer** — performs AI quality review
5. **Draft Generator** — creates a Document360-ready draft

Output artifacts are saved to `output/artifacts/ai/` and `output/artifacts/publishing/`.

**Run individual stages:**

Use the Claude commands in `.claude/commands/` (e.g., `/collect-release-data`, `/analyze-release`) for testing or debugging specific stages. These are orchestrated through AI agents and provide detailed logging.

## Python Environment

The Python scripts require **Python 3.7+** and use only the standard library (no external dependencies). Run scripts from the project root directory.

The orchestrator imports from the `automation/` package, so ensure you're in the correct directory before running.

---

# Understanding the Codebase

## Code Organization

The project separates concerns across multiple layers:

- **Commands** (`.claude/commands/`) — User-facing entry points that describe each stage; most wrap Agent calls
- **Prompts** (`.claude/prompts/`) — System prompts for Analyzer, Writer, Reviewer agents
- **Skills** (`.claude/skills/`) — Reusable capabilities: release note template, metadata, customer-friendly language
- **Agents** (`agents/`) — Agent specifications defining responsibilities and input/output contracts
- **Automation** (`automation/`) — Python orchestration: `pipeline_orchestrator.py` runs stages sequentially via `automation/stages/`
- **Mock Data** (`data/`) — JSON files simulating enterprise systems: `release-2025.8.json` and `service-now-2025.8.json`
- **Mock MCP** (`mcp/`) — Simulated MCP server structures (Azure DevOps, ServiceNow, Document360) with request/response pairs

## Code Navigation

**To understand the full pipeline:** Start with `automation/pipeline_orchestrator.py` — it's ~20 lines and shows how the five stages connect.

**To understand a specific stage:** Read `automation/stages/{stage}_stage.py` and its corresponding agent spec in `agents/{stage}-agent.md`.

**To understand what an Agent generates:** Check `.claude/prompts/{stage}*.md` — the system prompts for each agent.

**To understand the data model:** Examine `consolidated-release-dataset.json` or raw mock data in `data/release-*.json`.

## Common Development Tasks

**Modify an Agent's output:** Edit its prompt in `.claude/prompts/` and rerun the stage.

**Add or change mock data:** Edit JSON files in `data/` and rerun the Collector stage to regenerate the consolidated dataset.

**Add a new stage:** Create `automation/stages/newstage_stage.py`, add it to `pipeline_orchestrator.py`, create an agent spec in `agents/`.

**Test a single stage:** Use the Claude command in `.claude/commands/` (e.g., `/analyze-release`) rather than running the entire pipeline.

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

### Phase 1 Commands (Local Mock)
Use these to test with local JSON mock data:
- `/collect-release-data` — Collector stage with local `data/*.json`
- `/analyze-release` — Analyzer stage
- `/write-release-notes` — Writer stage
- `/review-release-notes` — Reviewer stage
- `/create-release-draft` — Draft Generator stage

### Phase 3 Commands (MCP Simulation)
Use these to test with simulated MCP servers:
- `/mcp-collect-release-data` — Collector stage with MCP simulation

All downstream stages remain the same; they consume the consolidated dataset regardless of data source.

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

All artifacts are saved to `output/artifacts/` during pipeline execution:

| Artifact                    | Generated By    | Location | Purpose                |
| --------------------------- | --------------- | -------- | ---------------------- |
| `collected-release-data.json` | Collector       | Root (or `output/artifacts/ai/`) | Enterprise dataset consolidated from all sources |
| `analyzed-release.json`       | Analyzer        | `output/artifacts/ai/` | Categorized and structured release information |
| `release-notes.md`            | Writer          | `output/artifacts/ai/` | Customer-facing release notes |
| `review-report.md`            | Reviewer        | `output/artifacts/ai/` | AI quality assurance report |
| `document360-draft.md`        | Draft Generator | `output/artifacts/publishing/` | Ready for Technical Writer review in Document360 |

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
