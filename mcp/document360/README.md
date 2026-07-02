# File: `mcp/document360/README.md`

# Document360 MCP Server

## Overview

The Document360 MCP Server provides a standardized interface between AI agents and Document360.

Its primary responsibility is to prepare and create structured draft articles using approved release note templates and metadata.

The MCP server does **not** publish documentation. Publication remains a human-controlled activity performed after Technical Writer and SME review.

---

# Purpose

The Document360 MCP Server abstracts Document360 functionality from the AI workflow.

Instead of interacting directly with Document360, AI agents use a small set of business-oriented tools that:

* Retrieve release note templates
* Create draft articles
* Populate draft content
* Apply metadata
* Save draft articles

This approach keeps AI responsibilities separate from documentation governance.

---

# Architecture

## Production Architecture

```text
Writer Agent
      │
      ▼
Reviewer Agent
      │
      ▼
Draft Generator Agent
      │
      ▼
Document360 MCP Server
      │
      ▼
Document360 API
      │
      ▼
Draft Article
      │
      ▼
Technical Writer
      │
      ▼
SME Review
      │
      ▼
Approve
      │
      ▼
Publish
```

---

## POC Architecture

```text
Draft Generator Agent
      │
      ▼
Document360 MCP
      │
      ▼
output/artifacts/document360-draft.md
```

---

# Responsibilities

The Document360 MCP Server is responsible for:

* Retrieving release note templates.
* Creating draft articles.
* Applying release note templates.
* Populating article content.
* Applying metadata.
* Saving draft articles.
* Returning draft information to the AI workflow.

The MCP server is **not** responsible for:

* Writing release notes.
* Reviewing release notes.
* Approving documentation.
* Publishing documentation.
* Managing documentation governance.

These responsibilities remain with the AI workflow and the human review process.

---

# AI Agents Using This MCP

* Draft Generator Agent

Future

* Knowledge Base Agent
* Documentation Migration Agent
* Article Update Agent

---

# Workflows Using This MCP

* Create Release Draft
* Update Existing Release Notes (Future)
* Documentation Migration (Future)

---

# Human Documentation Workflow

Once a draft has been created, responsibility transfers to the documentation team.

```text
Document360 Draft

        │

        ▼

Technical Writer Review

        │

        ▼

SME Validation

        │

        ▼

Documentation Approval

        │

        ▼

Publish
```

---

# Current POC Implementation

Current output

```text
output/artifacts/document360-draft.md
```

Future output

```text
Document360 Draft Article
```

---

# Future Enhancements

* Retrieve existing release note templates.
* Automatically select categories.
* Automatically assign tags.
* Support article versioning.
* Support multilingual drafts.
* Workflow status synchronization.
* Draft notifications.
* Review assignments.

---

# Related Documents

* tools.md
* Draft Generator Agent
* Create Release Draft Workflow
* Architecture
* Design Decisions
