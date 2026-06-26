## What's New

### AI-powered address validation with real-time correction and confidence scoring

Addresses submitted for delivery were validated after the fact — errors only surfaced once a shipment failed or required manual re-submission. Operations teams had no visibility into why a record failed or how confident the system was in any given correction.

The Address Validator now checks each address in real time as you enter it. The system parses the address, enriches it with postal authority data, and surfaces ranked correction suggestions inline before you submit. Each suggestion carries a confidence score so you can see exactly how certain the correction is. Accepted suggestions are applied to the form automatically. Once submitted, the Validation History table records the result with a status of Valid, Corrected, or Needs Review, a confidence percentage, and a timestamp — giving your team a searchable audit trail for every record.

**What you need to do**

No configuration changes are required. Real-time validation, confidence scoring, and validation history are available automatically in the Address Validator. If your account includes enterprise SSO, sign in using your existing credentials. Role-based access is configured by your account administrator.

**Benefits**

- Identify and correct address errors at the point of entry, before a shipment is dispatched
- Review confidence scores for every correction to prioritise manual review only where it is needed
- Access a full audit trail of validation results in Validation History, including status, confidence percentage, and timestamp
- Validate addresses across 157 countries using USPS, Royal Mail, and UPU postal authority data

---

## Bug Fix

### Dashboard metrics not updating in real time

Three KPI metrics on the dashboard were not updating consistently. Addresses Validated showed counts lagging by up to 24 hours. Compliance Passes displayed incorrect percentages because EU shipment data was excluded from the calculation. Delivery Success Rate was miscalculated because corrected addresses were not included in the figures. Operations teams saw stale values that did not reflect their actual shipment activity, reducing confidence in the dashboard as a tool for decision-making.

This issue is now resolved. Addresses Validated, Compliance Passes, and Delivery Success Rate refresh every 15 minutes and reflect current data on every page load. Compliance calculations now include EU shipment data, and the Delivery Success Rate formula correctly accounts for corrected addresses. All three metrics are consistent with the values shown on the Transactions and Compliance screens.

---

1.1
