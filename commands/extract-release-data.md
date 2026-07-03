# Extract Release Data

## Purpose

Extract and consolidate release information for the specified release version.

## Input

Release Version:

$ARGUMENTS

## Instructions

Use the **Release Data Extractor** skill to:

1. Retrieve release information from Jira using the Atlassian MCP server.
2. Read the corresponding implementation notes from the project repository.
3. Correlate Jira issues with implementation notes using the Jira Issue Key.
4. Generate the following outputs:
   - sample-data/jira-data.md
   - sample-data/implementation-data.md
   - sample-data/release-data.md

## Output

A consolidated release dataset (`sample-data/release-data.md`) ready for release note generation.