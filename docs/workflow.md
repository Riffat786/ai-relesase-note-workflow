# File: `docs/workflow.md`

# Workflow

## Overview

The Release Notes AI workflow automates the collection, analysis, and drafting of release notes while maintaining human ownership of the review, approval, and publication process.

The solution follows an AI-assisted documentation workflow where AI performs repetitive tasks and Technical Writers and Subject Matter Experts (SMEs) remain responsible for validating and publishing the final content.

---

# Business Workflow

```text
Release Request
      │
      ▼
Collect Release Data
      │
      ▼
Analyze Customer-Facing Changes
      │
      ▼
Generate Draft Release Notes
      │
      ▼
AI Quality Review
      │
      ▼
Create Draft in Document360
      │
      ▼
═══════════════════════════════
     Human Review Gateway
═══════════════════════════════
      │
      ├── Technical Writer Review
      │
      ├── SME Validation
      │
      ├── Content Updates
      │
      └── Final Approval
═══════════════════════════════
      │
      ▼
Publish Release Notes
```

---

# AI Workflow

## Step 1 — Collector Agent

### Purpose

Retrieve release information.

### Input

* Release Version

### Output

* Release JSON

---

## Step 2 — Analyzer Agent

### Purpose

Identify customer-facing changes and classify release items.

### Input

* Release JSON

### Output

* Categorized Release Data

---

## Step 3 — Writer Agent

### Purpose

Generate customer-friendly release notes.

### Input

* Categorized Release Data

### Output

* Draft Release Notes

---

## Step 4 — Reviewer Agent

### Purpose

Perform an AI quality review of the generated release notes.

Checks include:

* Grammar
* Customer-friendly language
* Consistency
* Markdown formatting
* Internal references
* Technical jargon

### Output

* Review Report

---

## Step 5 — Draft Generator Agent

### Purpose

Prepare a structured draft article in Document360.

Responsibilities include:

* Retrieve the Release Note template
* Populate the template with generated content
* Apply metadata
* Save the article as a Draft

### Output

* Draft Article in Document360

---

# Human Review Workflow

Once the draft has been created in Document360, ownership transitions from AI to the documentation team.

## Technical Writer

Responsibilities:

* Validate AI-generated content
* Improve readability
* Ensure consistency
* Verify links, formatting, and structure

---

## Subject Matter Expert (SME)

Responsibilities:

* Validate technical accuracy
* Confirm feature descriptions
* Identify missing information
* Approve technical content

---

## Final Approval

The approved draft is published using the organization's existing documentation governance process.

---

# Future Workflow

```text
/create-release-draft
        │
        ▼
Collector Agent
        │
        ▼
Azure DevOps MCP

ServiceNow MCP
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
Draft Generator Agent
        │
        ▼
Document360 MCP
        │
        ▼
Draft Article
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

---

# Key Principles

* AI automates repetitive documentation tasks.
* AI generates drafts, not published content.
* Human reviewers remain responsible for quality and accuracy.
* Publishing follows the organization's existing documentation governance process.
* The architecture is designed to support future enterprise integrations through MCP.
