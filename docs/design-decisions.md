# File: `docs/design-decisions.md`

# Design Decisions

## Purpose

This document records the architectural decisions made during the Proof of Concept and explains the reasoning behind them.

---

## Key Decisions

### Mock Data Instead of Enterprise Integrations

**Decision**

Use local JSON files.

**Reason**

Allows the AI workflow to be validated before integrating Azure DevOps, ServiceNow, and Document360.

---

### Five-Agent Architecture

**Decision**

Use Collector, Analyzer, Writer, Reviewer and draft generator agents.

**Reason**

Keeps responsibilities clear while avoiding unnecessary complexity.

---

### Separate Skills from Prompts

**Decision**

Store reusable standards as Skills.

**Reason**

Improves consistency and makes prompts easier to maintain.

---

### Output Artifacts

**Decision**

Store generated outputs under `output/artifacts`.

**Reason**

Provides traceability and supports future automation.

---

### MCP-Ready Design

**Decision**

Design the architecture so that mock data can later be replaced by MCP tools.

**Reason**

Minimizes future refactoring when enterprise integrations are introduced.

---

**Decision**: AI Generates Drafts Instead of Publishing

Reason:

- Maintains documentation governance.
- Ensures human validation of technical accuracy.
- Supports regulated documentation processes.
- Keeps Technical Writers and SMEs responsible for final approval.
- Aligns with existing review and publishing workflows.

---

## Future Decisions

* GitHub Actions
* Cursor Commands
* Azure DevOps MCP
* ServiceNow MCP
* Document360 Publishing
