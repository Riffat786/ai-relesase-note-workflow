# Release Data Extraction Report — Release Version 14.1

## Release Information

- **Release Version:** 14.1
- **Project:** KAN (Release Notes Automation)
- **Product:** Business Loan (KAN-1, KAN-2); KAN-7 Product not set in Jira
- **Modules:** Customer Details, Loan Processing, Reports
- **Total Jira Issues:** 3 (KAN-1, KAN-2, KAN-7)
- **Total Implementation Notes matched:** 3
- **Extraction Date:** 2026-07-05
- **Sources:** Atlassian MCP Server (Jira business data); project repository `sample-data/implementation-notes/` (technical data)

---

## Consolidated Release Dataset

Records correlated by Jira Issue Key from `sample-data/jira-data.md` (Jira fields) and `sample-data/implementation-data.md` (implementation fields).

---

## KAN-1

#### Business Information

- **Issue Key:** KAN-1
- **Summary:** Bulk Customer Import
- **Description:** Added CSV-based bulk customer import to simplify customer onboarding and reduce manual effort.
- **Status:** Done
- **Assignee:** bhargavi chary
- **Product:** Business Loan
- **Module:** Customer Details
- **Release Version:** 14.1

#### Technical Information

- **Technical Implementation Summary:** Enable operations users to upload multiple customer records using a CSV file, reducing manual data entry and onboarding time.
- **Files Modified:** Not specified
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
- **Developer Notes:** Work Type — Feature.

---

## KAN-2

#### Business Information

- **Issue Key:** KAN-2
- **Summary:** Duplicate Transaction Validation
- **Description:** Fixed duplicate transaction processing by validating transaction references before payment submission.
- **Status:** Done
- **Assignee:** bhargavi chary
- **Product:** Business Loan
- **Module:** Loan Processing
- **Release Version:** 14.1

#### Technical Information

- **Technical Implementation Summary:** Prevent duplicate loan transactions from being processed.
- **Files Modified:** Not specified
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
- **Developer Notes:** Work Type — Bug.

---

## KAN-7

#### Business Information

- **Issue Key:** KAN-7
- **Summary:** Update Regulatory Report Template
- **Description:** Updated regulatory report templates to comply with the latest reporting standards.
- **Status:** Done
- **Assignee:** bhargavi chary
- **Product:** Not set in Jira
- **Module:** Reports
- **Release Version:** 14.1

#### Technical Information

- **Technical Implementation Summary:** Update regulatory reports to meet revised compliance requirements.
- **Files Modified:** Not specified
- **Technical Changes:**
  - Updated report layout.
  - Added new compliance fields.
  - Improved export performance.
- **Configuration Changes:** Report template deployment required.
- **API Changes:** `GET /reports/regulatory`
- **Database Changes:** Added `ComplianceCategory` column.
- **Testing Notes:** Completed. Validation covers mandatory compliance fields.
- **Known Limitations:** Not specified
- **Developer Notes:** Work Type — Enhancement.

---

## Validation Report

### Missing Implementation Notes
- None. All three Jira issues (KAN-1, KAN-2, KAN-7) have matching implementation notes.

### Missing Jira Issues
- None. Every matched implementation note has a corresponding Jira issue in Release 14.1.

### Duplicate Records
- None detected. Each Jira Issue Key maps to exactly one implementation note.

### Missing Metadata
- **KAN-7 — Missing Product:** Product field (customfield_10074) is not set in Jira.

### Data Discrepancies
- **KAN-7 — Release Version / Product mismatch:** Jira records **Release Version 14.1** with **Product unset**, while the implementation note (`KAN-7 – Update Regulatory Report Template.md`) records **Release Version 14.2 / Product Mortgage Loan**. Per skill constraints, Jira is treated as the source of release-scope fields, so this issue is included in Release 14.1. **Reconcile before publishing release notes.**

### Unmatched Markdown Files
The `sample-data/implementation-notes/` folder contains additional notes not part of Release 14.1 (they belong to other release versions and were not returned by the Jira 14.1 filter):
- `KAN-3 – Loan Eligibility Rule Engine.md`
- `KAN-4 – Session Timeout Issue.md`
- `KAN-5 – Email Notification Template.md`
- `KAN-6 – Advanced Customer Search Filter.md`
- `KAN-8 – Custom Dashboard Widgets.md`

---

*This consolidated dataset is the input for the Release Notes Generator skill.*
