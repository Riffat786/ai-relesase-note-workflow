# AI-powered address validation with real-time correction

Learn how to use GlobalMail Pro's real-time address validation to improve data quality and reduce delivery errors.

---

## Overview

GlobalMail Pro 1.1 introduces AI-powered address validation that validates each address in real time as you enter it. The system enriches addresses with postal authority data and surfaces ranked correction suggestions with confidence scores before submission.

This feature supports addresses across 157 countries using data from USPS, Royal Mail, and UPU postal authority sources.

**Benefits:**
- Reduce undeliverable shipments by validating addresses before submission
- See correction suggestions ranked by confidence score
- Ensure data consistency across your entire address database
- Support international shipping to 157 countries

---

## How to use address validation

### Validate a single address

1. Open a form or entry screen that includes address fields
2. Enter the primary address line in the Address Line 1 field
3. Add optional secondary address information in Address Line 2 (if applicable)
4. Enter the city or municipality
5. Enter the postal code
6. Select the country code (ISO 3166-1 alpha-2 format)
7. The system automatically validates each field as you enter data
8. If the system detects a potential correction, a suggestion appears below the field showing the corrected address and a confidence score
9. Review the suggested correction and accept or edit as needed
10. Submit the form to save the validated address

### Interpret confidence scores

The system returns a confidence score between 0 and 1 for each validation:

- **0.95 to 1.0** — Highly confident correction. Accept this suggestion unless you have specific knowledge that contradicts it
- **0.85 to 0.94** — Confident correction. Review and accept most suggestions at this level
- **0.75 to 0.84** — Moderately confident. Compare the suggestion to your records before accepting
- **Below 0.75** — Lower confidence. Manually verify the address or consult postal authority records

### Address validation status

After validation, each address receives one of three status values:

| Status | Meaning | Action |
|--------|---------|--------|
| Valid | The address matches postal authority records with high confidence | Proceed to next step |
| Corrected | The system modified the address to match postal records | Accept or edit before submitting |
| Manual Review | The system needs more information or cannot validate with certainty | Research the address manually or contact the recipient |

---

## Batch validation

You can validate large address datasets using the batch validation feature. Batch validation supports up to 10,000 records per job.

**To validate a batch:**

1. Navigate to the Batch Validation screen
2. Upload your CSV or Excel file containing address records
3. Map each column in your file to the required address fields:
   - Address Line 1 (required)
   - Address Line 2 (optional)
   - City (required)
   - Postal Code (required)
   - Country Code (required)
4. Click Validate to begin processing
5. The system processes all records and returns a results file with validation status and corrected addresses
6. Download the results file to review corrections

**File size limits:** Batch jobs accept up to 10,000 records. To process larger datasets, split them into multiple jobs.

### Batch validation best practices

- **Test with a small sample first** — Upload 50–100 records first to verify column mapping
- **Keep records current** — Use the most recent address database available
- **Review international addresses carefully** — Some countries use different address formats
- **Export results for archiving** — Keep a copy of validation results for audit purposes

---

## API Details

The address validation service provides an API endpoint for developers who want to integrate real-time validation into custom applications.

### Endpoint

```
POST /api/v1/address/validate
```

### Parameters

All parameters should be sent as JSON in the request body.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| address_line_1 | String | Yes | Primary address line (street number and name) |
| address_line_2 | String | No | Secondary address line (apartment, suite, building) |
| city | String | Yes | City or municipality name |
| postal_code | String | Yes | Postal code or ZIP code |
| country_code | String | Yes | ISO 3166-1 alpha-2 country code (e.g., GB, US, DE, FR) |

### Example request

```json
{
  "address_line_1": "123 Main Street",
  "address_line_2": "Suite 400",
  "city": "London",
  "postal_code": "SW1A 1AA",
  "country_code": "GB"
}
```

### Response

The API returns a JSON object containing the validation results.

| Field | Type | Description |
|-------|------|-------------|
| corrected_address | Object | Contains corrected address fields (address_line_1, address_line_2, city, postal_code, country_code) |
| confidence_score | Number | Numeric value between 0 and 1 indicating validation confidence |
| status | String | One of: Valid, Corrected, or Manual Review |
| validation_id | String | Unique identifier for this validation request (use for troubleshooting) |
| timestamp | String | ISO 8601 timestamp indicating when the validation was performed |

### Example response

```json
{
  "corrected_address": {
    "address_line_1": "123 Main Street",
    "address_line_2": "Suite 400",
    "city": "London",
    "postal_code": "SW1A 1AA",
    "country_code": "GB"
  },
  "confidence_score": 0.98,
  "status": "Valid",
  "validation_id": "val_2026_07_001234",
  "timestamp": "2026-07-03T14:25:30Z"
}
```

### Error responses

If validation fails, the API returns an error response with a status code and error message.

| Status Code | Meaning |
|-------------|---------|
| 400 | Bad Request — Missing required parameter or invalid format |
| 401 | Unauthorized — Invalid API credentials |
| 404 | Not Found — Address not found in postal authority database |
| 429 | Too Many Requests — Rate limit exceeded |
| 500 | Internal Server Error — Contact support if this persists |

### Rate limits

The address validation API enforces the following rate limits:

- **Free tier:** 100 validations per day per API key
- **Pro tier:** 10,000 validations per day per API key
- **Enterprise tier:** Custom limits — contact sales

---

## Troubleshooting

### Common issues

**Issue:** The system shows "Manual Review" for a valid address

**Solution:** Some countries use address formats that differ from international standards. Try reformatting the address to match the country's postal convention, or use an alternative format (e.g., province instead of region).

**Issue:** Batch validation job times out

**Solution:** Jobs containing more than 50,000 records may time out. Split your file into multiple batches of 40,000 records or fewer.

**Issue:** Confidence score is lower than expected

**Solution:** Confidence scores reflect how closely the address matches postal authority records. Lower scores may indicate incomplete or non-standard address data. Verify the address directly with the recipient if the confidence score is below 0.85.

---

## Related topics

- [Validation History](help-centre)
- [Export validation results](help-centre)
- [Batch validation guide](help-centre)

---

&copy; 2026 GlobalMail Pro. All rights reserved.
