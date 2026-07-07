# Demo Storyline: AI-Powered Release Note Workflow

This document describes the step-by-step demo flow that showcases the AI-assisted release note workflow.

**Target Audience:** Workshop participants, stakeholders, product teams

**Duration:** 20–30 minutes (can be shortened or extended based on questions)

**Materials:** Repository files, Claude Code interface, sample data

---

## Setup

Before beginning the demo:

1. Ensure you have access to the repository
2. Have Claude Code open and ready to execute commands
3. Have `sample-data/scenario-1-feature-release/` and `sample-data/scenario-2-mixed-release/` visible for reference

---

## Part 1: Introduction (3 minutes)

**Objective:** Set context and establish the problem we're solving.

### Talking Points

**Problem:**
- Creating release notes is manual and repetitive
- Information comes from multiple sources (YouTrack, developer notes, product docs)
- Quality varies; terminology inconsistencies are common
- Multiple review cycles delay publication

**Guiding Principle:**
- We are not building a production-ready tool
- We are demonstrating how AI capabilities (commands, skills, agents) can automate this workflow
- Human review remains mandatory at every step

**What We'll Show:**
1. Real AI-powered commands you can invoke (not simulated)
2. Reusable skills that guide AI behavior consistently
3. Specialized agents that work together in sequence
4. How the workflow detects gaps instead of inventing details
5. How human review checkpoints are enforced

---

## Part 2: Scenario 1 — Feature Release (10 minutes)

**Objective:** Walk through a straightforward feature release using the real workflow.

### Setup

Show the audience: `sample-data/scenario-1-feature-release/input.md` — Raw source information (Multi-Factor Authentication, Dashboard Export, Report Export fixes)

### Step 1: Generate Release Notes

**Command:** `/generate-release-notes`

**Input:**
```
Release version: 5.4
Release type: Feature Release
Source: [paste content from sample-data/scenario-1-feature-release/input.md]
```

**Expected Output:**
- Structured release notes (Release Overview, New Features, Enhancements, Resolved Issues, Known Limitations)
- All content sourced from input (no invention)
- Customer-focused language ("Users can now…" not "We implemented…")

**Key Point to Highlight:**
- The command automatically loaded **Release Note Specialist** and **Documentation Style Guide** skills
- AI extracted: what changed, who benefits, why it matters
- This is a real, invokable command—not a simulation

### Step 2: Review for Quality

**Command:** `/review-release-notes`

**Input:**
```
[Paste the generated draft from Step 1]
[Optionally include the source input for validation]
```

**Expected Output:**
- Review result: "PASS" or "PASS WITH RECOMMENDATIONS"
- Findings: accuracy, clarity, customer focus, consistency, completeness
- Recommendations: actionable improvements
- Risks: issues that could prevent publication

**Key Point to Highlight:**
- The **Documentation Reviewer** skill checked for unsupported claims and hallucinations
- Reviewer does NOT rewrite—it flags issues for humans to decide
- This is the quality gate before human approval

### Step 3: Improve Based on Findings

**Command:** `/improve-release-notes`

**Input:**
```
[Original draft from Step 1]
[Review findings from Step 2]
[Original source material—critical to prevent hallucination]
```

**Expected Output:**
- Improved draft applying applicable recommendations
- Summary of changes made
- **No new details invented** (only recommendations supported by source are applied)

**Key Point to Highlight:**
- AI applies only recommendations that don't require new facts
- If a recommendation needs unsourced information, it's skipped
- This design prevents hallucination while improving quality

### Step 4: Create Executive Summary

**Command:** `/create-executive-summary`

**Input:**
```
[Approved release notes from Step 3]
```

**Expected Output:**
- High-level summary for stakeholders
- Sections: Key Highlights, Customer Benefits, Risks and Considerations, Recommendation
- Suitable for leadership and sponsors

**Key Point to Highlight:**
- Same **Documentation Style Guide** skill, applied to executive communication
- Removes technical jargon, focuses on business impact
- One-page summary enables quick stakeholder decision-making

### Outcome

Show: `generated-release-notes/scenario-1-feature-release/` containing:
- `01-generated-release-notes.md` — Original AI draft
- `02-review-results.md` — Reviewer feedback
- `03-release-notes-improved.md` — Polished draft
- `04-executive-summary.md` — Leadership summary

**Narrative:**
"In 30 minutes of workflow execution, we transformed raw source information into a complete, reviewed, improved, and summarized release package. A human approver can now make a final decision, rather than starting from scratch."

---

## Part 3: Scenario 2 — Gap Detection (10 minutes)

**Objective:** Demonstrate that the workflow detects missing information and refuses to invent details.

### Setup

Show: `sample-data/scenario-2-mixed-release/input.md`

**Challenge to Highlight:**
- Configuration Profiles feature exists in source, but key information is missing (customer impact, audience, benefit)
- A less disciplined system might invent specifics: "profiles support authentication methods, data handling preferences, and integration endpoints"
- That would be hallucination, violating our core principle: **"Do not invent information"**

**What we expect:**
- AI will flag the gap explicitly
- Reviewer will note the missing details as a risk
- The "improved" version will preserve the gap instead of fabricating details

### Step 1: Generate

**Command:** `/generate-release-notes`

**Input:**
```
Source: [paste sample-data/scenario-2-mixed-release/input.md]
```

**Output to Highlight:**
- `generated-release-notes/scenario-2-mixed-release/01-generated-release-notes.md`
- Configuration Profiles section is intentionally sparse (because source is sparse)
- "Missing Information" section explicitly lists gaps

**Narrative:**
"Notice: the Release Note Specialist did NOT invent details about what Configuration Profiles can do. It flagged the missing information. This is the 'accuracy first' principle in action."

### Step 2: Review

**Command:** `/review-release-notes`

**Input:**
```
[Paste generated draft from Step 1]
```

**Output to Highlight:**
- `generated-release-notes/scenario-2-mixed-release/02-review-results.md`
- Review result: "PASS WITH RECOMMENDATIONS"
- Findings: Configuration Profiles lack customer benefit clarity
- Recommendations: Ask for details—but don't invent them
- Risks: Users may not understand feature value

**Narrative:**
"The Reviewer identified the gap as a risk. But notice: it recommends asking questions ('What can be configured? What are the use cases?'), not inventing answers. The Reviewer is a human-assistance tool, not an automation bypass."

### Step 3: Improve (Key Constraint)

**Command:** `/improve-release-notes`

**Input:**
```
[Original draft]
[Review findings]
[Original source—NO new information provided]
```

**Output to Highlight:**
- `generated-release-notes/scenario-2-mixed-release/03-release-notes-improved.md`
- Configuration Profiles section is **still flagged under "Missing Information"**
- Password Policy and Scheduled Reports ARE improved (source supports them)
- **No new details were fabricated**

**Narrative:**
"Even though the reviewer recommended adding detail, the improved draft preserved the gap. Why? Because the source material didn't provide those details. 'AI-assisted' does NOT mean 'AI auto-completes with invented information.' The gap is preserved. A human must provide the missing information."

### Outcome: Core Principle Demonstrated

**Story Arc:**
1. Incomplete source data arrives → AI flags the gap (not inventing)
2. Reviewer identifies it as a risk → recommends asking, not guessing
3. Improvement pass preserves the gap → waiting for human input
4. Human provides missing info → gap is closed

**Key Takeaway:**
"This demonstrates our core workflow principle: **AI assists humans; humans remain in control.**"

---

## Part 4: Real Artifacts (4–5 minutes)

**Objective:** Prove these are real, invokable Claude Code artifacts—not a simulation.

### Show the `.claude/` Directory

Walk through:
- **`.claude/commands/`** — 4 real slash commands (generate-, review-, improve-release-notes, create-executive-summary)
- **`.claude/skills/`** — 3 real skills with YAML frontmatter (documentation-style-guide, release-note-specialist, documentation-reviewer)
- **`.claude/agents/`** — 5 real agent definitions (release-note-specialist-agent, documentation-reviewer-agent, executive-summary-agent, workflow-orchestrator-agent, release-intelligence-facilitator)

**Narrative:**
"These are not prose descriptions of what automation would look like. They are real Claude Code artifacts, registered with the system, invokable via slash commands and skill/agent references. A user can use this workflow immediately."

### Show Supporting Documentation

- **`README.md`, `README-project.md`, `CONTRIBUTING.md`** — Updated to reflect accurate folder structure
- **`decisions/decision-log.md`** — Documents key decisions (full conversion, hallucination fix, reorganization)
- **`charter/`, `assumptions/`, `validation/`, `demo/`** — Complete supporting artifacts

**Narrative:**
"The repository is comprehensive and self-contained. A new team member can read the README, explore the skills and agents, understand the workflow, and reproduce the demo using only the repository as a guide."

---

## Part 5: Key Takeaways (3 minutes)

### Capabilities Demonstrated

1. **Commands** — Reusable, invokable commands users can trigger
2. **Skills** — Reusable skill definitions that guide AI behavior consistently
3. **Agents** — Specialized agents handling specific workflow steps
4. **Governance** — Human-in-the-loop architecture enforcing review checkpoints
5. **Accuracy** — AI detects gaps instead of inventing details

### Real-World Implications

- Documentation workflows are prime candidates for AI assistance
- AI excels at extraction, classification, and improvement **within guardrails**
- Human review remains essential for approval and decision-making
- Proper skill design prevents hallucination and enforces consistency
- Realistic 2–3 scenarios effectively demonstrate the approach

### Recommendation

**The proof of concept successfully demonstrates:**
- AI commands, skills, and agents can automate repetitive documentation tasks
- Human oversight mechanisms enforce governance and prevent hallucination
- Realistic workflows can be implemented and demonstrated immediately
- The artifacts are real and usable—not simulated

**Next Steps (Future Work):**
- Adapt this approach to other documentation workflows (user guides, API docs, knowledge base articles, security policies)
- Integrate with actual source systems (YouTrack, Jira, GitHub)
- Extend to automated publishing and change tracking

---

## Timing Guide

| Section | Duration | Notes |
|---------|----------|-------|
| Part 1 (Intro) | 3 min | Set context and expectations |
| Part 2 (Scenario 1) | 10 min | Walk through all 4 commands sequentially |
| Part 3 (Scenario 2) | 10 min | Emphasize gap detection and no-hallucination principle |
| Part 4 (Real Artifacts) | 4 min | Show `.claude/` directory and supporting docs |
| Part 5 (Takeaways) | 3 min | Summarize learnings and implications |
| **Total** | **~30 min** | Plus 5–10 min for Q&A |

### Can Be Shortened (20 min):
- Skip detailed Step-by-Step in Scenario 2 (show outputs without running each command)

### Can Be Extended (45 min):
- Live customization demo (modify a command or skill)
- Deep dive into all skill rules and agent responsibilities
- Extended Q&A and discussion

---

## Troubleshooting

**If a command produces unexpected output:**
- Verify source input format matches expectations
- Check skill rules in `.claude/skills/*/SKILL.md`
- Review error message—usually points to missing or malformed data

**If audience asks "Can it do X?":**
- Refer to the **Guiding Principle**: We are demonstrating *release note workflow automation specifically*. Extending to other workflows is future work.

---

## Resources

All files referenced in this demo are in the repository:

- **Sample inputs:** `sample-data/scenario-1-feature-release/input.md`, `scenario-2-mixed-release/input.md`
- **Generated outputs:** `generated-release-notes/scenario-{1,2}-feature-release/`, `sample-product-5.{4,5}/`
- **Commands:** `.claude/commands/*.md`
- **Skills:** `.claude/skills/*/SKILL.md`
- **Agents:** `.claude/agents/*.md`
- **Specifications (docs):** `skills/`, `commands/`, `agent/`
- **Charter & Planning:** `charter/`, `assumptions/`
- **Validation & Decisions:** `validation/`, `decisions/decision-log.md`

For questions: see `CONTRIBUTING.md` and `decisions/decision-log.md`
