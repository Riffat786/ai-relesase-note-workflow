**GlobalMail Pro – Release 1.1 (July 2026)**

---

## Overview

Release 1.1 delivers one new feature for real-time address validation with confidence scoring, resolves two bug fixes in the dashboard and compliance modules with improved KPI accuracy.

---

## New Features

- **AI-powered address validation with real-time correction and confidence scoring:** Addresses submitted for delivery were validated after the fact, with errors surfacing only when shipments failed. The Address Validator now checks each address in real time as you enter it, surfaces ranked correction suggestions with confidence scores, and records every result in Validation History with status, confidence percentage, and timestamp. [Learn more →](help-topic-kan-101-address-validation-real-time.html)

---

## Enhancements

No enhancements in this release.

---

## Bug Fixes

| Bug ID | Summary | Severity | Affected Area | Description | Steps to Reproduce | Fix Applied | User Impact | Workaround | Confluence Reference |
|--------|---------|----------|---------------|-------------|--------------------|-------------|-------------|------------|----------------------|
| KAN-102 | Dashboard metrics not updating in real time | High | Dashboard | Three KPI metrics on the dashboard were not updating consistently. Addresses Validated showed counts lagging by up to 24 hours. Compliance Passes displayed incorrect percentages because EU shipment data was excluded from the calculation. Delivery Success Rate was miscalculated because corrected addresses were not included in the figures. Operations teams saw stale values that did not reflect their actual shipment activity. | 1. Log in to GlobalMail Pro Dashboard. 2. Change the date range filter. 3. Observe that the three KPI metrics do not reflect the selected range. 4. Refresh the page. 5. Metrics show slightly different values. | All three metrics now refresh on every page load and update in the background every 15 minutes. EU shipment data is included in Compliance Pass calculations. Corrected addresses are now included in Delivery Success Rate calculations. | Users see accurate KPI values on every Dashboard load, enabling real-time decision-making. | Manually refresh the browser tab to force a metrics update. | N/A |
| KAN-103 | Compliance report excluding EU shipments | Medium | Compliance | The Compliance Passes metric excluded all shipments destined for EU countries, causing the reported compliance percentage to be higher than the actual rate. | 1. Open Compliance screen. 2. Select any date range with EU shipments. 3. EU destination rows are missing from the results. | EU shipment records are now included in all compliance calculations and exports. | Compliance reports accurately reflect all shipment destinations. | Export the Validation History table and filter by country manually. | N/A |

---

## Known Issues

No known issues in this release.

---

## Technical Notes

No API or schema changes in this release.

---

*For help with any feature, contact support or visit the Help Center.*
