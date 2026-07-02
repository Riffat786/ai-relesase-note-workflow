# File: `README.md`

# Release Notes AI

## Overview
AI prepares a structured darft in Document360 using the organization's release note template. Technica Writers and SME's review, refine and approve the content before it is published. 

Release Notes AI is a Proof of Concept (POC) that demonstrates how AI can automate the creation of customer-facing release notes using a modular, agent-based architecture.

The solution uses mock release data to simulate enterprise systems and demonstrates AI engineering concepts including:

* AI Agents
* Prompt Engineering
* Reusable Skills
* Workflow Automation
* Modular Architecture
* MCP-ready Design
* GitHub-based Project Structure

The POC intentionally avoids direct integration with enterprise systems such as Azure DevOps, ServiceNow, and Document360. Instead, it uses mock data to validate the workflow before introducing production integrations.

# Not included in POC
- Audience based classification: Technical (for internals) and Non-technical (for customers)
- Future MCP integrations and Enterprise Automation (Phase 2 and 3 as stated below)

---

## Objectives

* Demonstrate end-to-end release note generation.
* Showcase reusable AI engineering patterns.
* Produce publication-ready release notes.
* Build an architecture that can later connect to enterprise systems through MCP.

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
## Repository Structure

This repository separates orchestration, prompting, reusable knowledge, and generated artifacts. That makes the solution easier to maintain and extend.

Commands
↓
call
↓
Prompts
↓
use
↓
Skills
↓
produce
↓
Artifacts

```text
.claude/

commands/

prompts/

skills/

agents/

mcp/

automation/

output/

docs/
```

---

## Current Status

* ✅ Mock data
* ✅ Analyzer Prompt
* ✅ Writer Prompt
* ✅ Reviewer Prompt
* ✅ Skills
* ✅ Agent Definitions
* ✅ Commands
* ⏳ Mock MCP
* ⏳ GitHub Workflow
* ⏳ Enterprise Integrations

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

* Azure DevOps MCP
* ServiceNow MCP
* Document360 Publisher
* GitHub Actions
* Cursor Commands
* Automated Publishing

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
| Commands                   | ✅ 5        |
| Agents                     | ✅ 5        |
| Prompts                    | ✅ 5        |
| Skills                     | ✅ Reusable |
| Architecture documentation | ✅          |
| Workflow documentation     | ✅          |
| MCP placeholders           | ✅          |
| Output artifacts           | ✅          |
| Mock data                  | ✅          |
| End-to-end pipeline        | ✅          |
