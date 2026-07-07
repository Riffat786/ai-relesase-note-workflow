---
name: generate-release-notes
description: Generate customer-facing release notes from source information
argument-hint: Release version, audience, and source information (see examples in sample-data/)
---

# Generate Release Notes

You are assisting with generating customer-facing release notes from provided source information.

Load and follow the **Documentation Style Guide** skill and the **Release Note Specialist** skill.

Analyze the provided source information in `$ARGUMENTS` and create review-ready release notes.

## Requirements

1. Use only information provided in the source.
2. Do not invent missing details, benefits, or features.
3. Use customer-focused language.
4. Follow MSTP principles and documentation standards.
5. Classify content appropriately (New Features, Enhancements, Resolved Issues, Security Updates, etc.).
6. Identify missing information explicitly rather than inferring it.
7. Exclude implementation details unless specifically requested.

## Output Structure

```
# Release Overview

## New Features

## Enhancements

## Resolved Issues

## Security Updates

## Known Limitations

## Missing Information
```

Generate each section only if there is content to report. Include a "Missing Information" section listing any gaps preventing complete customer-facing description of the release.

This is a draft. Your output is intended for review by the Documentation Reviewer agent before final approval.
