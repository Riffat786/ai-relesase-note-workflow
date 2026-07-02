# File: `agents/writer-agent.md`

## Writer Agent

## Purpose

Generate customer-facing release notes.

---

## Responsibilities

- Read analyzed release data.
- Produce release notes.
- Apply customer-friendly language.
- Follow release note template.
  
---

## Input
```text
output/analyzed-release.json
```
---

## Uses Skills
```text
customer-friendly-language.md

release-note-template.md
```
---

## Uses Prompt
```text
write-release-notes.md
```
---


## Output
```text
output/release-notes.md
```
---

**Success Criteria**

- Professional
- Customer-friendly
- Markdown formatted
- No internal IDs

---

**Future MCP**

Document360 Publisher