# Expected Output — Sample 1 (What's New / Feature Release)

## Release — GlobalMail Pro 1.1

## CONTENT BENCHMARK — Release Notes

**Source:** Jira — GlobalMailProClaudeDemo project (key: KAN)  
**Board:** [KAN Project Board](https://twtaidimple.atlassian.net/jira/software/projects/KAN/list?jql=project+%3D+KAN+ORDER+BY+cf%5B10019%5D+ASC&atlOrigin=eyJpIjoiMmFmZjcxOTdlMTE4NDFlMDllYmYzN2Q3MWIyYjJmZTMiLCJwIjoiaiJ9)  
**JQL:** `project = KAN ORDER BY cf[10019] ASC`

---


This file shows the required output structure and quality standard.  
Agents use it as a benchmark — all content is replaced with real Jira data at runtime.  
No variables or placeholders appear in the actual generated output.

---

## GlobalMail Pro – Release 1.1 (July 2026)

---

### Overview
Release 1.1 delivers one new feature for real-time address validation, two enhancements to batch processing and audit reporting, resolves two bug fixes in the dashboard and compliance modules, and documents one known issue in bulk validation.

---

### New Features
- **AI-powered address validation with real-time correction:** The Address Validator now checks each address as you enter it, surfaces ranked correction suggestions with confidence scores, and records every result in Validation History with status, confidence percentage, and timestamp. [Learn more →](help-topic-link)

---

### Enhancements
- The Validation History table now supports CSV export, allowing operations teams to share audit records without requiring a login to the application.  
- Batch address validation now supports up to 10,000 records per job, reducing turnaround time for large datasets from hours to minutes.

---

### Bug Fixes

| Bug ID | Summary | Severity | Affected Area | Description | Steps to Reproduce | Fix Applied | User Impact | Workaround | Confluence Reference |
|--------|---------|----------|---------------|-------------|--------------------|-------------|-------------|------------|----------------------|
| KAN-23 | Dashboard metrics not updating in real time | High | Dashboard | Three KPI metrics showed values up to 24 hours old regardless of the selected date range. Addresses Validated, Compliance Passes, and Delivery Success Rate were all affected. | 1. Log in. 2. Open Dashboard. 3. Change the date range filter. Metrics do not reflect the selected range. | All three metrics now refresh on every page load and update in the background every 15 minutes. EU shipment data is included in Compliance Pass calculations. | Users see current KPI values on every Dashboard visit, enabling accurate real-time decisions. | Manually refresh the browser tab to force a metrics update. | N/A |
| KAN-31 | Compliance report excluding EU shipments | Medium | Compliance | The Compliance Passes metric excluded all shipments destined for EU countries, causing the reported compliance percentage to be higher than the actual rate. | 1. Open Compliance screen. 2. Select any date range with EU shipments. EU destination rows are missing from the results. | EU shipment records are now included in all compliance calculations and exports. | Compliance reports accurately reflect all shipment destinations. | Export the Validation History table and filter by country manually. | N/A |

---

### Known Issues
- **Bulk validation timeout on files over 50,000 rows:** Jobs containing more than 50,000 address records may time out after 30 minutes without completing. Split input files into batches of 25,000 rows as a temporary workaround.

---

### Technical Notes
No API or schema changes in this release.

---

For help with any feature, contact support or visit the **Help Center**.

