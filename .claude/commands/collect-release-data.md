# File: `.claude/commands/collect-release-data.md`

# /collect-release-data

## Purpose

Retrieve release data for a specified release version.

For this Proof of Concept (POC), retrieve the release data from the local `data/` folder.

The goal of this command is **only** to collect the release data. Do not analyze, summarize, or generate release notes.

---

## Input

Release version.

Example:

```text
/collect-release-data 2025.8
```

---

## Instructions

1. Read the following file:

```text
data/release-{{releaseVersion}}.json
```

2. Verify that the file exists.

3. Verify that the JSON is valid.

4. Do not modify the contents.

5. Save a copy as:

```text
output/artifacts/ai/collected-release-data.json
```

6. Return a short summary containing:

* Release version
* Number of Features
* Number of Enhancements
* Number of Bug Fixes

Do not perform any analysis.

Do not generate release notes.

---

## Expected Output

Artifact:

```text
output/artifacts/ai/collected-release-data.json
```

Example summary:

```text
Release 2025.8

Features: 2

Enhancements: 1

Bug Fixes: 2

Collection completed successfully.
```

---

## Success Criteria

The command is successful when:

* The release file has been located.
* The JSON has been validated.
* The collected data has been copied to the output folder.
* No analysis has been performed.
