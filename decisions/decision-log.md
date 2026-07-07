# Decision Log

This file documents significant project decisions, their rationale, and outcomes.

## Format

Each decision entry includes:
- **Date**: When the decision was made
- **Decision**: What was decided
- **Rationale**: Why this decision was made
- **Impact**: How this affects the project
- **Status**: Current status (Implemented, In Progress, Under Review, etc.)

---

## Decision Template

### [Date] - [Decision Title]

**Decision:** [What was decided]

**Rationale:** [Why this decision was made]

**Impact:** [How this affects the project]

**Status:** [Current status]

---

## Project Decisions

### [Dates] – Full Conversion to Real Claude Code Artifacts

**Decision:** Convert all commands, skills, and agents from prose documentation into real, invokable Claude Code artifacts (`.claude/commands/`, `.claude/skills/`, `.claude/agents/` with proper YAML frontmatter).

**Rationale:** The original workshop deliverables were well-written specifications but not registered with Claude Code. To demonstrate that the workflow is actually functional and invokable, not just conceptual, all artifacts were converted to real implementations that users can invoke via slash commands or automatic agent/skill triggering.

**Impact:** The project now demonstrates working AI-assisted workflow automation, not just the documentation of what such automation would look like. This significantly strengthens the workshop proof-of-concept.

**Status:** Implemented (2026-07-07)

---

### [Date] – Fix Hallucination in Scenario-2 Output

**Decision:** Correct `generated-release-notes/scenario-2-mixed-release/03-release-notes-improved.md` to remove fabricated details about Configuration Profiles that were not supported by source material.

**Rationale:** The improved output contained unsourced specifics ("authentication methods, data handling preferences, and integration endpoints") that contradicted the validation report's claim of "no feature, benefit, or metric was invented beyond the source." This undermined the scenario's purpose (demonstrating correct gap detection) and the project's credibility claim (no hallucinations).

**Impact:** The corrected output now properly preserves the missing information flag instead of inventing details, aligning behavior with claims and the project's core principles.

**Status:** Implemented (2026-07-07)

---

### [Date] – Reorganize Generated Artifacts and Clean Root

**Decision:** Move loose output files from root directory into `generated-release-notes/` (creating `sample-product-5.4/` and `sample-product-5.5/` subfolders), move demo artifacts into `demo/`, and delete superseded earlier drafts.

**Rationale:** Root clutter (14 loose `.md` files, a 32MB video, HTML exports) made the repo navigation confusing and obscured which files were canonical vs. draft. Reorganization improves discoverability and signals clear project structure.

**Impact:** Repository is cleaner, more professional, and easier to navigate. The `generated-release-notes/` folder now contains the complete set of sample outputs in a consistent structure.

**Status:** Implemented (2026-07-07)

---

### [Date] – Fix Governance Documentation

**Decision:** Update `README.md`, `README-project.md`, `CONTRIBUTING.md`, and `Github-collaboration-instructions.md` to reference correct folder names and add the missing `decisions/` folder that multiple docs required.

**Rationale:** Four governance documents all referenced non-existent folders (`agents`, `mcp-integrations`, `prompts-and-commands`, `agent-workflow`, `decisions/`), creating confusion about the actual structure and making the docs unreliable. Consistency improves clarity and usability.

**Impact:** Governance documentation now accurately reflects repository structure, reducing confusion and improving contributor onboarding.

**Status:** In Progress (2026-07-07)

---

### [Date] – Merge Agent Validation Folder

**Decision:** Fold `agent/validation/README.md` content into `validation/validation-notes.md` and remove the `agent/validation/` folder.

**Rationale:** `agent/validation/` is not an agent itself; it's validation methodology documentation that belongs in the `validation/` folder. The misplacement created confusion about the actual number of agents in the system.

**Impact:** Clearer separation of concerns: agents are defined under `.claude/agents/`, and validation methodology lives in `validation/`.

**Status:** Pending (2026-07-07)

---

## Proposed Decisions (Under Review)

[Add any pending decisions here]
