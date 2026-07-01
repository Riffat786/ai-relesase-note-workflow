# AI-powered address validation with real-time correction and confidence scoring

---

## Overview

**What it does:** Validates each address in real time as you enter it, enriches it with postal authority data, and surfaces ranked correction suggestions with a confidence score before you submit.

**Why it matters:** Address errors previously surfaced only after a shipment failed, requiring manual re-submission and causing delivery delays. Real-time validation catches errors at the point of entry.

**Key benefits:** Reduces failed delivery rates by catching address errors before dispatch, provides a full audit trail of every validation decision in Validation History, and supports addresses across 157 countries using USPS, Royal Mail, and UPU postal authority data.

---

## Workflow

1. User logs in to GlobalMail Pro and opens the Address Validator.
2. User enters or pastes an address into the address entry form.
3. The system validates the address in real time against postal authority data.
4. Ranked correction suggestions appear inline, each with a confidence score.
5. User reviews the suggestions and selects the correct address.
6. The accepted address is applied to the form automatically.
7. On submission, the result is recorded in Validation History with status, confidence percentage, and timestamp.

---

## API Details

**Endpoint:** `/api/v1/address/validate`

**Method:** `POST`

**Parameters**

| Parameter       | Type   | Required | Description                                                   |
|-----------------|--------|----------|---------------------------------------------------------------|
| address_line_1  | string | Yes      | First line of the address to validate.                        |
| address_line_2  | string | No       | Second address line, if applicable.                           |
| city            | string | Yes      | City or locality.                                             |
| postal_code     | string | Yes      | Postal or ZIP code.                                           |
| country_code    | string | Yes      | ISO 3166-1 alpha-2 country code, for example US, GB, or DE.   |

**Example Request**

```json
{
  "address_line_1": "123 Main St",
  "address_line_2": "Suite 100",
  "city": "New York",
  "postal_code": "10001",
  "country_code": "US"
}
```

**Example Response**

```json
{
  "success": true,
  "result": {
    "original_address": "123 Mian St, Nwe York, NY 10001, US",
    "corrected_address": "123 Main St, New York, NY 10001, US",
    "confidence_score": 0.97,
    "status": "Corrected",
    "suggestions": [
      { "address": "123 Main St, New York, NY 10001, US", "confidence": 0.97 }
    ],
    "validation_id": "val-558821",
    "timestamp": "2026-07-01T10:30:00Z"
  }
}
```

---

For help with release 1.1, see [GlobalMail Pro Release 1.1](release-notes-1-1.html).
