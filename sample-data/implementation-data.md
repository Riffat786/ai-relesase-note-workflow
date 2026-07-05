# Implementation Notes — KAN-1, KAN-2, KAN-7

Source: `sample-data/implementation-notes/` in the current repository.

> Note: The implementation notes do not contain explicit **Files Modified** or **Known Limitations** sections. These are marked *Not specified* where absent. **Configuration Changes** is mapped from each note's *Deployment Notes* section.

---

## KAN-1 — Bulk Customer Import

- **Files Modified:** Not specified in implementation notes.
- **Technical Changes:**
  - Developed CSV parsing service.
  - Added customer validation framework.
  - Implemented duplicate customer detection.
  - Integrated Customer Service API.
  - Added upload progress tracking and audit logging.
- **Configuration Changes:** No manual configuration required.
- **API Changes:** `POST /customers/import`
- **Database Changes:** Added `BulkUploadId` and `UploadStatus` columns to the `CustomerUpload` table.
- **Testing Notes:** Unit Testing completed; Integration Testing completed; Regression Testing passed. Validation covers mandatory fields, duplicate customers, and invalid CSV format.
- **Known Limitations:** Not specified in implementation notes.

---

## KAN-2 — Duplicate Transaction Validation

- **Files Modified:** Not specified in implementation notes.
- **Technical Changes:**
  - Added duplicate transaction validation.
  - Compared Transaction ID before processing.
  - Implemented duplicate transaction logging.
  - Displayed user-friendly validation message.
- **Configuration Changes:** Database index required (deployment step).
- **API Changes:** None.
- **Database Changes:** Added `TransactionHash` index.
- **Testing Notes:** Unit, Integration, and Regression testing completed. Validation covers duplicate Transaction ID, duplicate request payload, and duplicate reference number.
- **Known Limitations:** Not specified in implementation notes.

---

## KAN-7 — Update Regulatory Report Template

- **Files Modified:** Not specified in implementation notes.
- **Technical Changes:**
  - Updated report layout.
  - Added new compliance fields.
  - Improved export performance.
- **Configuration Changes:** Report template deployment required.
- **API Changes:** `GET /reports/regulatory`
- **Database Changes:** Added `ComplianceCategory` column.
- **Testing Notes:** Completed. Validation covers mandatory compliance fields.
- **Known Limitations:** Not specified in implementation notes.

---

> ⚠️ **Discrepancy — KAN-7:** The Jira issue lists this under **Release Version 14.1 / Product unset**, but the implementation note records **Release Version 14.2 / Product Mortgage Loan**. Worth reconciling before generating release notes.
