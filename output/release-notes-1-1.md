# GlobalMail Pro 1.1 Release Notes

**Release Date:** July 2026

---

## What's new in version 1.1

GlobalMail Pro 1.1 introduces real-time address validation powered by AI, enhanced export capabilities, and critical bug fixes to improve dashboard reliability and compliance reporting accuracy.

---

## New Features

### AI-powered address validation with real-time correction

Validate each address in real time as you enter it. The system enriches it with postal authority data and surfaces ranked correction suggestions with confidence scores before submission. Supports addresses across 157 countries using USPS, Royal Mail, and UPU postal authority data.

**Component:** Address Validator

**Key capabilities:**
- Real-time validation as you type
- Confidence scoring for address corrections
- Support for 157 countries
- Postal authority data enrichment
- Ranked correction suggestions

**API Details**

The address validation endpoint processes address data and returns corrected values with confidence metrics.

**Endpoint:** `POST /api/v1/address/validate`

**Parameters:**
- `address_line_1` (required): Primary address line
- `address_line_2` (optional): Secondary address line
- `city` (required): City or municipality
- `postal_code` (required): Postal code
- `country_code` (required): ISO 3166-1 alpha-2 country code

**Response fields:**
- `corrected_address`: The validated and corrected address
- `confidence_score`: Numeric value between 0 and 1
- `status`: One of Valid, Corrected, or Manual Review
- `validation_id`: Unique identifier for this validation request
- `timestamp`: ISO 8601 timestamp of the validation

For detailed implementation guidance, see [AI-powered address validation help topic](help-topic-kan-42-ai-powered-address-validation.html).

---

## Enhancements

| Title | Description | Component |
|-------|-------------|-----------|
| Export compliance results as CSV or PDF | Adds an Export Results button to the Compliance screen. Users can download compliance check results in CSV or PDF format, including shipment ID, destination country, contents, data type, and compliance status. | Compliance |
| Validation History table now supports CSV export | The Validation History table can now be exported to CSV format. Operations teams can share audit records without requiring application login. | Validation History |
| Batch validation now supports up to 10,000 records per job | Increased batch size limit from 5,000 to 10,000 records per validation job. Reduces turnaround time for large datasets. | Batch Processing |

---

## Bug Fixes

| Bug ID | Issue | Resolution |
|--------|-------|-----------|
| KAN-23 | Dashboard metrics not updating in real time | All three metrics (Addresses Validated, Compliance Passes, Delivery Success Rate) now refresh on every page load and update in the background every 15 minutes. EU shipment data is included in Compliance Pass calculations. |
| KAN-31 | Compliance report excluding EU shipments | EU shipment records are now included in all compliance calculations and exports. |

---

## Known Issues

The following issues are present in this release and are under investigation.

| Issue | Description | Workaround | Status |
|-------|-------------|-----------|--------|
| KAN-88: Bulk validation timeout on files over 50,000 rows | Jobs containing more than 50,000 address records may time out after 30 minutes without completing. | Split large files into multiple jobs of 40,000 records or fewer. | Open |
| KAN-89: Incomplete compliance checks for China shipments | Compliance checks for shipments to China sometimes return incomplete results because certain technology-related rules are not fully mapped in the system. Users may see a Limited status for China shipments. | Review China shipment compliance results manually for sensitive product categories. | Open |

---

## Getting help

Visit our Help Centre for detailed guidance on all features in GlobalMail Pro. For urgent support, contact our technical support team.

---

&copy; 2026 GlobalMail Pro. All rights reserved.
