# Validation Notes

## Purpose

This document describes how the AI-assisted release note workflow is validated.

It defines the validation approach, method, criteria, and roles. The detailed outcomes of running this method against the sample scenarios are recorded in `sample-data/validation-results.md`.

---

## Validation Objective

Confirm that the workflow can:

- Transform source change information into review-ready release notes.
- Classify changes correctly.
- Identify missing information instead of inventing it.
- Apply documentation standards consistently.
- Preserve mandatory human review and approval.

The objective is to evaluate the proof of concept, not to certify a production system.

---

## What Is Being Validated

| Layer | Validated For |
| --- | --- |
| Skills | Correct application of style, classification, and review rules |
| Agents | Correct role behavior and handoffs |
| Commands | Repeatable, consistent invocation |
| Workflow | Correct end-to-end sequence and checkpoints |
| Governance | Human oversight is preserved and cannot be bypassed |

See `agent/`, `skills/`, and `commands/` for the components under test.

---

## Validation Method

The workflow is validated using **scenario-based testing**: realistic release inputs are run end to end, and the outputs are compared against expected results.

### Steps

1. **Prepare scenario input.** Use a realistic set of release issues (see `sample-data/`).
2. **Run generation.** Pass the input to the Release Note Specialist Agent.
3. **Run review.** Pass the draft to the Documentation Reviewer Agent.
4. **Run summary.** Pass approved content to the Executive Summary Agent.
5. **Compare to expected output.** Check the draft and findings against the scenario's expected files.
6. **Record results.** Capture pass/fail, findings, risks, and observations in `sample-data/validation-results.md`.

### Source of Truth

Each scenario folder contains the expected artifacts used for comparison:

- `input.md` — source issues
- `expected-release-notes.md` — expected draft
- `review-findings.md` — expected review outcome
- `executive-summary.md` — expected summary

---

## Validation Criteria

A scenario is considered successful when the output meets the following.

### Accuracy

- Every statement is supported by source information.
- No features, benefits, metrics, or security claims are invented.

### Classification

- Each change is placed in the correct section (New Feature, Enhancement, Resolved Issue, Security Update, Known Limitation).
- Non-customer-facing items (for example, technical debt) are excluded from customer notes.

### Customer Focus

- Content describes outcomes and value, not implementation detail.
- Language follows MSTP principles (active voice, present tense, plain language).

### Gap Detection

- Missing customer impact, benefit, or audience is flagged.
- Gaps are reported, never guessed.

### Standards Compliance

- Approved terminology and formatting are applied consistently.

### Human Oversight

- The workflow ends at a human approval checkpoint.
- No content is auto-approved or auto-published.

---

## Test Data Strategy

- Scenarios use **non-confidential, illustrative data** created for the workshop.
- At least one scenario uses **complete input** to validate the happy path.
- At least one scenario uses **incomplete input** to validate gap detection and fail-safe behavior.
- A simulated MCP data source is available in `mcp-plugin-concept/simulated-data/` to validate the intake stage without live system access.

---

## Roles

| Role | Responsibility |
| --- | --- |
| Validator | Runs scenarios and records results |
| Reviewer (human) | Confirms output quality and approval readiness |
| Facilitator | Confirms validation covers project success criteria |

The Release Intelligence Facilitator oversees validation coverage; see `agent/release-intelligence-facilitator/README.md`.

---

## Pass and Fail Definitions

| Outcome | Meaning |
| --- | --- |
| Pass | Output meets all criteria; only optional improvements suggested |
| Pass with recommendations | Output is acceptable; non-blocking improvements recommended |
| Fail | Output contains unsupported claims, wrong classification, or missing critical information presented as complete |

A scenario where the workflow correctly **flags** missing information is a pass, not a fail. Failing to flag missing information is a fail.

---

## Known Limitations of This Validation

- Small sample size (two scenarios) does not cover all release shapes.
- Static sample data; live YouTrack/MCP retrieval is not exercised.
- Automated review does not replace domain or business validation.
- Results depend on source input quality.

---

## Maintenance

When the workflow, skills, or agents change:

1. Re-run the existing scenarios.
2. Update expected files in `sample-data/` if intended behavior changed.
3. Record new results in `sample-data/validation-results.md`.
4. Add new scenarios for any newly discovered edge cases.

---

## Related Documents

- `sample-data/validation-results.md` — recorded results of applying this method
- `sample-data/` — scenario inputs and expected outputs
- `mcp-plugin-concept/integration-concept.md` — intake integration concept
- `charter/project-charter.md` — success criteria this validation supports
