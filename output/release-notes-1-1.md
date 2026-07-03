# GlobalMail Pro – Release 1.1

**Version:** 1.1

July 2026

---

## Overview

Release 1.1 introduces AI-powered real-time address validation, enhanced export capabilities for compliance and audit records, increased batch processing capacity, and resolves critical issues affecting dashboard reliability and compliance reporting accuracy.

---

## New Features

- **AI-powered address validation with real-time correction** The Address Validator now checks each address as you enter it, surfaces ranked correction suggestions with confidence scores, and records every result in Validation History with status, confidence percentage, and timestamp. [Learn more →](help-topic-kan-42-ai-powered-address-validation.html)

---

## Enhancements

- **Export compliance results as CSV or PDF** Adds an Export Results button to the Compliance screen. Users can download compliance check results in CSV or PDF format, including shipment ID, destination country, contents, data type, and compliance status. Helps Ops Managers share compliance reports with auditors and regulators.
- **Validation History table now supports CSV export** Operations teams can share audit records without requiring application login.
- **Batch validation now supports up to 10,000 records per job** Increased batch size limit from 5,000 to 10,000 records per validation job. Reduces turnaround time for large datasets from hours to minutes.

---

## Bug Fixes

| Bug ID | Summary | Severity | Affected Area | Description | Fix Applied |
|--------|---------|----------|---------------|-------------|----|
| KAN-23 | Dashboard metrics not updating in real time | High | Dashboard | Three KPI metrics showed values up to 24 hours old regardless of the selected date range. Addresses Validated, Compliance Passes, and Delivery Success Rate were all affected. | All three metrics now refresh on every page load and update in the background every 15 minutes. EU shipment data is included in Compliance Pass calculations. |
| KAN-31 | Compliance report excluding EU shipments | Medium | Compliance | The Compliance Passes metric excluded all shipments destined for EU countries, causing the reported compliance percentage to be higher than the actual rate. | EU shipment records are now included in all compliance calculations and exports. |

---

## Known Issues

**KAN-88: Bulk validation timeout on files over 50,000 rows**

Jobs containing more than 50,000 address records may time out after 30 minutes without completing.

**Workaround:** Split large files into multiple jobs of 40,000 records or fewer to avoid timeout errors.

---

**KAN-89: Incomplete compliance checks for China shipments**

Compliance checks for shipments to China sometimes return incomplete results because certain technology-related rules are not fully mapped in the system. Users may see a "Limited" status for China shipments, and manual review is required until full regulatory mapping is implemented.

**Workaround:** Manually review China shipment compliance results using external customs documentation for sensitive product categories.

---

For help with any feature, visit the **Help Centre** or contact our technical support team.

---

&copy; 2026 GlobalMail Pro. All rights reserved.
