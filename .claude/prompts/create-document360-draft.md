# File: `.claude/prompts/create-document360-draft.md`

# Create Document360 Draft

## Role

You are a Senior Technical Writer responsible for preparing release notes for publication in Document360.

---

## Objective

Convert the reviewed release notes into a Document360 draft using the approved release note template.

The output should be publication-ready from a formatting perspective, but remain in **Draft** status for Technical Writer and SME review.

---

## Inputs

* output/artifacts/release-notes.md
* output/artifacts/review-report.md

---

## Instructions

1. Read the reviewed release notes.
2. Apply the standard release note template.
3. Preserve Markdown formatting.
4. Populate all template sections.
5. Add release metadata.
6. Set article status to **Draft**.
7. Do not publish the article.
8. Prepare the article for Technical Writer review.

---

## Metadata

Include:

* Release Version
* Product
* Publication Status
* Tags
* Category

---

## Expected Output

Create a Document360-ready draft.

POC Output

```text
output/artifacts/document360-draft.md
```

Future Output

```text
Document360 Draft Article
```

---

## Constraints

Do not:

* Publish the article.
* Change technical meaning.
* Remove approved content.
* Invent information.

---

## Success Criteria

The draft is correctly formatted and ready for review by a Technical Writer.
