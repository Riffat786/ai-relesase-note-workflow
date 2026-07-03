# File: `docs/demo-script.md`

# Demo Script

## Goal

Demonstrate an end-to-end AI workflow that automatically generates customer-facing release notes.

AI prepares a structured darft in Document360 using the organization's release note template. Technica Writers and SME's review, refine and approve the content before it is published. 

---

## Step 1 — Introduce the Problem

Explain that release notes are often created manually using information from multiple systems.

Highlight the challenges:

* Time-consuming
* Inconsistent
* Scattered information

---

## Step 2 — Show the Architecture

Present the high-level workflow.

```text
Collector
    ↓
Analyzer
    ↓
Writer
    ↓
Reviewer
    ↓
Draft generator
```

Explain that each agent has a single responsibility.

---

## Step 3 — Show the Mock Data

Open:

`data/release-2025.8.json`
`data/service-now-2025.8.json`

Explain that this simulates Azure DevOps and ServiceNow data.

---

## Step 4 — Show the Analyzer Output

Open:

`output/artifacts/analyzed-release.json`

Explain how the AI classifies and filters customer-facing changes.

---

## Step 5 — Show the Generated Release Notes

Open:

`output/artifacts/release-notes.md`

Highlight the customer-friendly language and consistent structure.

---

## Step 6 — Show the Review Report

Open:

`output/artifacts/review-report.md`

Explain that AI performs a quality review before publication.

---

## Step 7 — Explain Future Enhancements

Describe how mock data can be replaced with:

* Azure DevOps MCP
* ServiceNow MCP
* Document360 MCP

without changing the overall architecture.

---

## Key Takeaways

* Modular AI architecture
* Reusable prompts and skills
* Clear agent responsibilities
* Traceable workflow
* Ready for enterprise integration
