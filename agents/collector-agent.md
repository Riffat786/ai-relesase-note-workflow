# File: `agents/collector-agent.md`

# Collector Agent

## Purpose

Collect all release-related information required to generate release notes.

For this Proof of Concept (POC), the Collector Agent retrieves release data from local mock JSON files.

In future phases, this agent will retrieve data from Azure DevOps, ServiceNow, and other enterprise systems through MCP servers.

---

## Responsibilities

* Retrieve release data for a specified release version.
* Validate that the release data exists.
* Ensure the data is in the expected JSON format.
* Pass the collected data to the Analyzer Agent.
* Log any missing or invalid data.

---

## Input

Release identifier.

Example:

```text
Release 2025.8
+
Service-now-2025.8
```

Current data source:

```text
data/release-2025.8.json
```
```text
data/service-now-2025.8.json
```
---

## Skills Used

None (POC)

Future:

* Data Validation
* Data Normalization

---

## Prompt Used

None

The Collector Agent simply retrieves structured data.

---

## Output

```text
data/release-2025.8.json
```

---

## Success Criteria

* Release data is successfully located.
* JSON is valid.
* Data is ready for analysis.

---

## Future MCP Tools

Azure DevOps MCP

* get_release_work_items()
* get_completed_features()
* get_completed_bugs()

ServiceNow MCP

* get_change_requests()
* get_incidents()

Document360 MCP

* search_existing_release_notes()

---

## Future Enhancements

* Support multiple releases.
* Merge data from multiple systems.
* Validate duplicate work items.
* Handle missing information gracefully.
