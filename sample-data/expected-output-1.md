# Release Notes Documentation Benchmark Standard
**Document Type:** Documentation Quality Standard
**Maintained by:** Documentation Standards Team
**Applies to:** All Feature Release Notes — Enterprise SaaS Platform
**Version:** 1.0
## Purpose
This document defines the structure, style, and quality criteria for a high-quality feature Release Note. It serves as the authoritative benchmark for documentation teams producing release notes across all product areas. Every release note published externally should be measured against this standard before approval.
## Benchmark Structure
A compliant release note must include the following sections, in the order shown. Optional sections are clearly marked.
## 1. Feature Title
### Criteria
The title must be:
- **Customer-focused** — describe the capability or outcome, not the internal implementation
- **Concise** — no more than 10 words
- **Action-oriented** — lead with a verb or a clear noun phrase that signals what changed
- **Free of internal jargon** — avoid system names, ticket references, or engineering terminology
### Quality Checklist
- [ ] Title communicates the feature from the user's perspective
- [ ] Title is free of internal project names, ticket IDs, or acronyms
- [ ] Title does not start with a version number or date
### Examples
| Non-compliant | Compliant |
|---|---|
| PROJ-4821: BE Pipeline Enhancement | Automated Report Scheduling |
| v2.4 Data Layer Update | Real-Time Dashboard Filters |
| SSO Refactor (Phase 2) | Single Sign-On for Enterprise Accounts |
## 2. Introductory Summary
### Purpose
The summary is the most critical section of a release note. It must answer three questions in sequence: What was the problem? What changed? Why does it matter to the reader?
### Required Structure
The summary must follow this three-part narrative flow:
**Part 1 — The Problem (Previously)**
Open with the limitation, friction, or gap that existed before this release. This grounds the reader and creates context for the improvement. Begin with "Previously," where appropriate.
**Part 2 — The Enhancement (Now)**
Describe what has changed. Be specific about the new capability or behavior. Begin with "Now," where appropriate.
**Part 3 — Business Value**
Close with a plain-language statement of what the reader can now accomplish and why it matters to their work. Do not restate Part 2 — this should describe the downstream benefit.
### Style Criteria
- Address the reader as **"You"** — never "users," "customers," or "they"
- Use **active voice** throughout — avoid passive constructions
- Use **simple, clear language** — write for a business user, not an engineer
- Keep the summary to **4–6 lines**
- Avoid bullet points in this section — it must read as a cohesive paragraph
### Quality Checklist
- [ ] Opens with the problem or prior limitation ("Previously...")
- [ ] Introduces the enhancement clearly ("Now...")
- [ ] Closes with a business value statement
- [ ] Written in active voice
- [ ] Addresses reader as "you"
- [ ] 4–6 lines in length
- [ ] No bullet points; written as prose
### Illustrative Pattern
> Previously, [describe the limitation or pain point the user experienced]. Now, [describe the new capability or behavior]. [Business value statement — what the user can accomplish and why it matters].
## 3. Key Changes Implemented
### Purpose
This section provides a structured breakdown of the distinct components that make up the feature. Each component gets its own sub-section, giving readers and support teams a clear reference for what specifically changed.
### Structure Criteria
- Use `###` sub-section headers for each component
- Each component header should be a plain-language label, not a system or code reference
- Each component description must be **2–3 lines** — no more
- Order components logically: from the user's first point of interaction to the last
### Sub-Section Criteria
Each component sub-section must:
- Name the component clearly (what the user sees or interacts with)
- Explain what changed and what the user can now do with it
- Reference UI location, field name, or access path where helpful
- Avoid internal architecture details, database terms, or implementation notes
### Quality Checklist
- [ ] Each component has its own `###` sub-section
- [ ] Sub-section headers use plain language, not internal references
- [ ] Each description is 2–3 lines
- [ ] Components are ordered from the user's point of view
- [ ] No implementation detail or engineering language present
### Example Sub-Section Format
```
### [Component Name]
[What this component is and where the user finds it.] [What the user can now do with it.] [Any relevant constraint or note that affects use.]
```
## 4. Example Workflow *(Optional — Strongly Recommended)*
### Purpose
A numbered workflow shows the reader exactly how to use the feature from start to finish. It converts feature descriptions into actionable steps, reducing time-to-value and support volume.
### When to Include
Include an example workflow when:
- The feature involves more than one step to use
- The sequence of actions affects the outcome
- The feature introduces a new UI pattern or access path
- The target audience includes administrators or first-time users of a complex capability
### Structure Criteria
The workflow must follow this three-layer pattern for each step:
1. **Action** — what the user does (verb-led instruction)
2. **System response** — what the platform does in response (describe feedback, state change, or result)
3. **Outcome** — what the user has achieved and what is now possible
The workflow must:
- Use a **numbered list** (ordered steps, not bullets)
- Begin each step with an **imperative verb** ("Navigate," "Select," "Upload," "Confirm")
- Include **UI path references** where applicable (e.g., Settings → User Management)
- End with a clear terminal outcome — what the user has when the workflow is complete
### Quality Checklist
- [ ] Steps are numbered and in logical sequence
- [ ] Each step begins with an imperative verb
- [ ] System responses are described where meaningful
- [ ] Final step states a clear, concrete outcome
- [ ] UI paths are included and accurate
- [ ] No steps are skipped or assumed
## 5. Visuals *(Optional)*
### Purpose
Visuals reduce cognitive load for complex features and support readers who process information more effectively through diagrams than prose.
### When to Include
Include a visual when:
- The feature involves a multi-step workflow with a decision point or branch
- The feature introduces a new data structure, hierarchy, or relationship
- A before/after comparison would make the change immediately obvious
- The audience includes non-technical stakeholders who benefit from a summary view
### Visual Type Reference
| Type | Best Used For |
|---|---|
| Linear workflow diagram | Sequential processes with a clear start and end |
| Branching workflow diagram | Processes with decision points or conditional paths |
| Before/after comparison table | Changes to existing behavior or UI |
| Architecture or relationship diagram | New data structures, hierarchies, or integrations |
| Annotated screenshot | New UI elements or changes to existing screens |
### Quality Checklist
- [ ] Appropriate Visual type is used for appropriate content
- [ ] Description explains what the visual depicts
## Writing Standards — Global Criteria
These criteria apply to every section of every release note, without exception.
### Voice and Tone
| Criterion | Standard |
|---|---|
| Point of view | Second person ("you") throughout |
| Voice | Active — subject performs the action |
| Tone | Professional, direct, and confident |
| Register | Plain business English — accessible to non-technical readers |
### Language Rules
- **Do** use present tense to describe current behavior ("The system validates your file before processing")
- **Do** use past tense only in the "Previously" section
- **Do not** use passive constructions ("Files are validated by the system" → incorrect)
- **Do not** use hedging language ("may," "might," "could" — unless describing a conditional behavior)
- **Do not** use internal jargon, acronyms, or system names without definition
- **Do not** anthropomorphize the product unnecessarily ("The system wants to…" → incorrect)
### Prohibited Content
The following must never appear in a published release note:
- Internal ticket numbers, project names, or sprint references
- Engineering or infrastructure implementation details
- Unresolved TODOs, placeholders, or bracketed notes
- Comparison to competitor products by name
- Forward-looking statements about unreleased features
## Release Note Quality Scorecard
Use this scorecard during peer review and editorial sign-off.
| Section | Criteria | Pass / Fail |
|---|---|---|
| Feature Title | Customer-focused, concise, no jargon | |
| Summary | Problem → Enhancement → Value structure present | |
| Summary | Active voice, addresses "you," 4–6 lines | |
| Key Changes | Each component has a `###` sub-section | |
| Key Changes | Descriptions are 2–3 lines, plain language | |
| Workflow *(if included)* | Numbered, imperative verbs, terminal outcome stated | |
| Visual Suggestion *(if included)* | Type, content, and rationale all specified | |
| Global | Active voice throughout | |
| Global | No internal references or jargon | |
| Global | Addresses reader as "you" | |

**Sign-off threshold:** All criteria must pass before a release note is approved for publication.

*This standard is maintained by the Documentation Standards Team. Submit proposed revisions via the documentation governance process. Last reviewed: June 2026.*
