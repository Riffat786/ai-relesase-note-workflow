# Consolidated Release Records — Release Version 14.1

Records correlated by Jira Issue Key from `sample-data/jira-data.md` (Jira fields) and `sample-data/implementation-data.md` (implementation fields).

---

## KAN-1

- **Issue Key:** KAN-1
- **Summary:** Bulk Customer Import
- **Business Description:** Added CSV-based bulk customer import to simplify customer onboarding and reduce manual effort.
- **Status:** Done
- **Product:** Business Loan
- **Module:** Customer Details
- **Release Version:** 14.1
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
- **Known Limitations:** Not specified

---

## KAN-2

- **Issue Key:** KAN-2
- **Summary:** Duplicate Transaction Validation
- **Business Description:** Fixed duplicate transaction processing by validating transaction references before payment submission.
- **Status:** Done
- **Product:** Business Loan
- **Module:** Loan Processing
- **Release Version:** 14.1
- **Technical Changes:**
  - Added duplicate transaction validation.
  - Compared Transaction ID before processing.
  - Implemented duplicate transaction logging.
  - Displayed user-friendly validation message.
- **Configuration Changes:** Database index required (deployment step).
- **API Changes:** None
- **Database Changes:** Added `TransactionHash` index.
- **Testing Notes:** Unit, Integration, and Regression testing completed. Validation covers duplicate Transaction ID, duplicate request payload, and duplicate reference number.
- **Known Limitations:** Not specified

---

## KAN-7

- **Issue Key:** KAN-7
- **Summary:** Update Regulatory Report Template
- **Business Description:** Updated regulatory report templates to comply with the latest reporting standards.
- **Status:** Done
- **Product:** Not specified
- **Module:** Reports
- **Release Version:** 14.1
- **Technical Changes:**
  - Updated report layout.
  - Added new compliance fields.
  - Improved export performance.
- **Configuration Changes:** Report template deployment required.
- **API Changes:** `GET /reports/regulatory`
- **Database Changes:** Added `ComplianceCategory` column.
- **Testing Notes:** Completed. Validation covers mandatory compliance fields.
- **Known Limitations:** Not specified

> ⚠️ **Data discrepancy (KAN-7):** Jira lists this issue under **Release Version 14.1** with **Product** unset, while the implementation note records **Release Version 14.2 / Product Mortgage Loan**. Jira values are used above (Jira is the source for release-scope fields). Reconcile before publishing release notes.
