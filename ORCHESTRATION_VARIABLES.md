# Variable Resolution Map — Pipeline Run 2026-07-01

**Source:** Jira Mock Data (project: KAN, 3 issues fetched)  
**Pipeline Step:** 3 — Runtime Variable Resolution  
**Status:** COMPLETE

---

## Global Variables

| Variable | Source | Value | Type |
|----------|--------|-------|------|
| product_name | Constant (branding-style-guide.md) | GlobalMail Pro | string |
| release_version | issue.fixVersions[0].name | 1.1 | string |
| version_slug | release_version with dots→hyphens | 1-1 | string |
| release_date | Today at pipeline runtime | 2026-07-01 | date |
| release_month_year | Today formatted as "Month YYYY" | July 2026 | string |
| total_issues_fetched | Count from Jira response | 3 | number |

---

## Issue Variables — KAN-101 (New Feature)

| Variable | Source | Value |
|----------|--------|-------|
| [Feature Name] | KAN-101.summary (sentence case) | AI-powered address validation with real-time correction and confidence scoring |
| [slug] | kan-101 + hyphenated(summary, max 40) | kan-101-address-validation-real-time |
| Feature Description | KAN-101.description (first paragraph) | Addresses submitted for delivery were validated after the fact — errors only surfaced once a shipment failed or required manual re-submission. |
| New Capability | KAN-101.description (second paragraph) | The Address Validator now checks each address in real time as you enter it. |
| User Action Required | Synthesised from description | No configuration changes are required. |
| Benefit 1 | Synthesised from capability | Identify and correct address errors at the point of entry, before a shipment is dispatched |
| Benefit 2 | Synthesised from capability | Review confidence scores for every correction to prioritise manual review only where it is needed |
| Benefit 3 | Synthesised from capability | Access a full audit trail of validation results in Validation History, including status, confidence percentage, and timestamp |
| Benefit 4 | Synthesised from capability | Validate addresses across 157 countries using USPS, Royal Mail, and UPU postal authority data |

---

## Issue Variables — KAN-102 (Bug Fix)

| Variable | Source | Value |
|----------|--------|-------|
| [Bug ID] | KAN-102.key | KAN-102 |
| [Bug Summary] | KAN-102.summary (sentence case) | Dashboard metrics not updating in real time |
| [Severity] | Map KAN-102.priority.name (High) | High |
| [Affected Area] | KAN-102.components[0].name | Dashboard |
| [Bug Description] | KAN-102.description (first paragraph) | Three KPI metrics on the dashboard were not updating consistently. Addresses Validated showed counts lagging by up to 24 hours. Compliance Passes displayed incorrect percentages because EU shipment data was excluded from the calculation. Delivery Success Rate was miscalculated because corrected addresses were not included in the figures. |
| [Steps to Reproduce] | KAN-102.customfield_steps_to_reproduce | 1. Log in to GlobalMail Pro Dashboard 2. Change the date range filter 3. Observe that the three KPI metrics do not reflect the selected range 4. Refresh the page 5. Metrics show slightly different values |
| [Fix Applied] | KAN-102.resolution_description | All three metrics now refresh on every page load and update in the background every 15 minutes. EU shipment data is included in Compliance Pass calculations. Corrected addresses are now included in Delivery Success Rate calculations. |
| [User Impact] | Synthesised from description + fix | Users see accurate KPI values on every Dashboard load, enabling real-time decision-making. |
| [Workaround] | KAN-102.customfield_workaround | Manually refresh the browser tab to force a metrics update. |
| [Confluence Reference] | KAN-102.remotelinks (empty) | N/A |

---

## Issue Variables — KAN-103 (Bug Fix)

| Variable | Source | Value |
|----------|--------|-------|
| [Bug ID] | KAN-103.key | KAN-103 |
| [Bug Summary] | KAN-103.summary (sentence case) | Compliance report excluding EU shipments |
| [Severity] | Map KAN-103.priority.name (Medium) | Medium |
| [Affected Area] | KAN-103.components[0].name | Compliance |
| [Bug Description] | KAN-103.description | The Compliance Passes metric excluded all shipments destined for EU countries, causing the reported compliance percentage to be higher than the actual rate. |
| [Steps to Reproduce] | KAN-103.customfield_steps_to_reproduce | 1. Open Compliance screen 2. Select any date range with EU shipments 3. EU destination rows are missing from the results |
| [Fix Applied] | KAN-103.resolution_description | EU shipment records are now included in all compliance calculations and exports. |
| [User Impact] | Synthesised from description + fix | Compliance reports accurately reflect all shipment destinations. |
| [Workaround] | KAN-103.customfield_workaround | Export the Validation History table and filter by country manually. |
| [Confluence Reference] | KAN-103.remotelinks (empty) | N/A |

---

## Help Topic Map (Generated from New Features)

```json
{
  "KAN-101": {
    "slug": "kan-101-address-validation-real-time",
    "filename": "help-topic-kan-101-address-validation-real-time.html",
    "feature_name": "AI-powered address validation with real-time correction and confidence scoring"
  }
}
```

---

## Classification Summary

**Total Issues:** 3  
**New Features:** 1 (KAN-101)  
**Enhancements:** 0  
**Bug Fixes:** 2 (KAN-102, KAN-103)  
**Known Issues:** 0  

---

**Resolved at:** 2026-07-01 23:30:00 UTC  
**All variables ready for sub-agent delegation**
