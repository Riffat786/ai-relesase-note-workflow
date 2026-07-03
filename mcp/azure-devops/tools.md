# Azure DevOps MCP Tools

---

## Tool
```text
get_release()
```
### Purpose

Retrieve release metadata.

### Input

Release Version

### Example

2025.8

## Returns

- Release Version
- Release Tag
- Build Number
- Work Item IDs

---

## Tool
```text
get_work_items()
```

### Purpose

Retrieve detailed information for all Work Items included in a release.

### Input

List of Work Item IDs

### Returns

- Title
- Description
- Work Item Type
- Area
- State
- Acceptance Criteria
- Tags

---

## Tool
```text
get_work_item()
```

### Purpose

Retrieve one Work Item.

### Input

Work Item ID

### Returns

Complete Work Item information.

---

## Tool
```text
get_comments()
```

### Purpose

Retrieve discussion comments.

---

## Tool
```text
get_acceptance_criteria()
```

### Purpose

Retrieve Acceptance Criteria.