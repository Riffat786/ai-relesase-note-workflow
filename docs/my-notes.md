# SKILL
You must add the YAML frontmatter block at the absolute top of the markdown file. It must be the very first thing in the file, even before your main title header.

It is separated from the rest of your text by three dashes (---) at the start and three dashes (---) at the end.

## Exact Code Example
Here is exactly how your SKILL.md file should look:

```text
---
name: release-note
description: Generates standardized production release notes from git logs.
version: 1.0.0
---

# Release Note Skill

This is where your regular markdown content and instructions go. 
The AI will read the metadata above, but it won't show it to the user.

```
# Strict Rules for Frontmatter

1. Line 1 Must Be ---: Do not leave an empty line or space at the very beginning of the file.
2. Use Valid YAML Syntax: Use a colon followed by a space (e.g., name: value). Do not use equal signs or tabs.
3. No Code Blocks Above It: Do not wrap the frontmatter block inside markdown code ticks (like ```). The three dashes are all you need.

## Why Is This Needed?

AI agents and developer tools read this metadata block before processing the file. It tells the tool what the skill is named and when to trigger it without forcing the AI to read your entire markdown prompt first.

---

> Note
> Add the following in README.md when the automation phase is finished. 

#Phase 2: Enterprise Architecture

The goal is to replace the manual orchestration with an automated pipeline, while still using mock data.

## Step 1 – GitHub Actions

Right now I run the following commands manually:

```text
/collect-release-data

/analyze-release

/write-release-notes

/review-release-notes

/create-release-draft
```

Instead create:

```text 

GitHub Push

↓

GitHub Action

↓

Collector

↓

Analyzer

↓

Writer

↓

Reviewer

↓

Draft Generator

↓

Artifacts
```
This demonstrates automation without needing live enterprise systems.
---
## Step 2 – Real Automation Scripts

Currently, Claude is orchestrating the workflow interactively.

So We'll implement:

```text 

automation/

generate-release-notes.py

review-release.py

create-draft.py
```

These scripts will:

- Load files
- Invoke prompts
- Generate artifacts
- Save outputs

This makes the pipeline reproducible and prepares it for CI/CD.
---
## Step 3 – MCP Contracts

Even without live systems, we can define the interfaces.

### Azure DevOps MCP
```text
Collector Agent

↓

getRelease()

↓

returns

User Stories

Features

Bugs

Tasks

```
---
### ServiceNow MCP
```text
Collector Agent

↓

getReleaseSupportData()

↓

returns

Known Issues

Change Requests

Maintenance Window

Support Notes
```
---

### Document360 MCP
```text
Draft Generator

↓

createDraft()

↓

returns

Draft URL

Draft ID

Status
```
These contracts make it easy to swap in real integrations later.
---
## Step 4 – Plugins

Your repository already has commands and skills.

Now we can add plugins such as:

- Markdown Validator
- Release Note Template Validator
- Metadata Validator
- Quality Score Calculator

These enhance the workflow without changing the core pipeline.
---
## Step 5 – Marketplace Readiness

Structure the repository so it could be shared internally:
```text

release-note-generator/

README.md

CHANGELOG.md

LICENSE

docs/

examples/

.claude/

mcp/

automation/
```

This makes it look like a reusable internal accelerator rather than a one-off demo.

# Step 1 - Github actions
Goal

Currently, the workflow is:
```text
You
 │
 ▼
Run /collect-release-data
 │
 ▼
Run /analyze-release
 │
 ▼
Run /write-release-notes
 │
 ▼
Run /review-release-notes
 │
 ▼
Run /create-release-draft
```
We want to move towards:
```text
GitHub Push
      │
      ▼
GitHub Action
      │
      ▼
Release Note Pipeline
      │
      ▼
Artifacts Generated
```

*Notice something important:*

> GitHub Actions won't replace Claude.

> GitHub Actions simply becomes the orchestrator.

This step will teach:

- GitHub Actions
- CI/CD basics
- YAML workflows
- Automation
- Repository events
- Future MCP orchestration

This aligns perfectly with Docs-as-Code learning roadmap.