# File: `docs/repository-structure.md`

# Repository Structure

## Overview

The repository is organized to separate AI assets, documentation, data, and generated artifacts.

---

## Folder Structure

### `.claude/`

Contains reusable AI assets.

#### prompts/

Task-specific prompts.

#### skills/

Reusable writing and quality standards.

---

### `agents/`

Agent specifications describing responsibilities, inputs, outputs, prompts, and skills.

---

### `data/`

Mock release data used for the POC.

Future:

* Azure DevOps exports
* ServiceNow exports

---

### `docs/`

Architecture and project documentation.

---

### `output/`

Generated content.

#### artifacts/

* analyzed-release.json
* release-notes.md
* review-report.md

#### logs/

Execution and workflow logs.

---

### `.github/`

Future GitHub Actions workflows.

---

## Guiding Principles

* Separate configuration from execution.
* Keep prompts reusable.
* Keep skills independent.
* Keep outputs traceable.
* Document architectural decisions.
