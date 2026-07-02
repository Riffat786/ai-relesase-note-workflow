# File: `agents/draft-generator-agent.md`

# Draft Generator Agent

## Purpose

Prepare AI-reviewed release notes for Document360 by creating a structured draft article using the organization's release note template.

The Draft Generator Agent does **not** publish content. Its responsibility ends when the draft has been successfully created and saved.

---

## Responsibilities

- Retrieve AI-reviewed release notes.
- Retrieve the Document360 release note template.
- Apply the release note template.
- Populate the template with AI-generated content.
- Attach release metadata.
- Create a draft article.
- Save the draft.
- Notify that the draft is ready for Technical Writer review.

---

## Input

```text
output/artifacts/release-notes.md

output/artifacts/review-report.md
```

---

## Skills Used

- release-note-metadata.md
- release-note-template.md

---

## Prompt Used

```text
.claude/prompts/create-document360-draft.md
```

---

## Output

```text
Document360 Draft Article
```

POC Output

```text
output/artifacts/document360-draft.md
```

Future Output

```text
Document360 Draft
```

---

## Success Criteria

- Release note template applied.
- Metadata completed.
- Draft created successfully.
- Draft saved.
- Ready for Technical Writer review.

---

## Future MCP Tools

- get_release_template()
- create_draft_article()
- populate_article_content()
- attach_metadata()
- save_draft()

---

## Human Handoff

After draft creation:

```text
Technical Writer
        │
        ▼
SME Review
        │
        ▼
Approve
        │
        ▼
Publish
```

The Draft Generator Agent has no responsibility beyond creating the draft.