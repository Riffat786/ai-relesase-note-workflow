# File: `workflows/generate-release-notes.md`

# Generate Release Notes Workflow

## Purpose

Generate customer-facing release notes for a specified software release using a modular AI workflow.

This workflow orchestrates multiple AI agents to collect release data, analyze customer-facing changes, and generate publication-ready release notes.

---

## Trigger

User executes:

```text
/generate-release-notes <release-version>
```

Example

```text
/generate-release-notes 2025.8
```

---

## Workflow

```text
Collector

↓

Analyzer

↓

Writer

↓

Reviewer

↓

Draft Generator

↓

Document360 Draft
```

---

## Execution Steps

### Step 1

Collector Agent

* Locate release data.
* Validate release version.
* Load release JSON.

Output

```text
data/release-2025.8.json
```

---

### Step 2

Analyzer Agent

* Classify release items.
* Remove technical tasks.
* Organize customer-facing changes.

Output

```text
output/artifacts/analyzed-release.json
```

---

### Step 3

Writer Agent

* Generate release notes.
* Apply writing standards.
* Follow release note template.

Output

```text
output/artifacts/release-notes.md
```

---

## Skills Used

* classify-release-items/SKILL.md
* customer-friendly-language/SKILL.md
* release-note-template/SKILL.md

---

## Prompts Used

* analyze-release.md
* write-release-notes.md

---

## Artifacts Produced

* analyzed-release.json
* release-notes.md

---

## Success Criteria

* Release data collected.
* Customer-facing changes identified.
* Publication-ready release notes generated.

---

## Future Enhancements

* Azure DevOps MCP
* ServiceNow MCP
* Automatic release highlights
* GitHub Actions integration
