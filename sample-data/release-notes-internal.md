# Release Notes — Internal

| Item | Value |
|------|-------|
| Release Version | 14.1 |
| Release Date | 2026-07-05 |
| Audience | Internal (Engineering, QA, Release Management, Support) |
| Project | KAN — Release Notes Automation |
| Issues in Release | KAN-1, KAN-2, KAN-7 |

## Overview

Release 14.1 delivers one new feature (bulk customer import), one defect fix (duplicate transaction prevention), and one regulatory enhancement (updated report templates). All three issues are in **Done** status. This edition is for internal distribution and includes implementation, API, database, testing, and deployment details, plus open data-quality actions.

## New Features

### KAN-1 — Bulk Customer Import
- **Product / Module:** Business Loan / Customer Details
- **Work Type:** Feature
- **Summary:** CSV-based bulk customer import to reduce manual onboarding effort.
- **Technical Changes:**
  - CSV parsing service.
  - Customer validation framework.
  - Duplicate customer detection.
  - Customer Service API integration.
  - Upload progress tracking and audit logging.
- **API Changes:** `POST /customers/import`
- **Database Changes:** Added `BulkUploadId` and `UploadStatus` columns to the `CustomerUpload` table.
- **Validation:** Mandatory fields, duplicate customers, invalid CSV format.
- **Testing:** Unit, Integration, and Regression completed/passed.
- **Deployment Notes:** No manual configuration required.

## Bug Fixes

### KAN-2 — Duplicate Transaction Validation
- **Product / Module:** Business Loan / Loan Processing
- **Work Type:** Bug
- **Summary:** Prevents the same loan transaction from being processed more than once by validating transaction references before submission.
- **Technical Changes:**
  - Duplicate transaction validation.
  - Transaction ID comparison before processing.
  - Duplicate transaction logging.
  - User-friendly validation message on detection.
- **API Changes:** None
- **Database Changes:** Added `TransactionHash` index.
- **Validation:** Duplicate Transaction ID, duplicate request payload, duplicate reference number.
- **Testing:** Unit, Integration, and Regression completed.
- **Deployment Notes:** ⚠️ Database index required — must be applied as part of deployment.

## Regulatory Updates

### KAN-7 — Update Regulatory Report Template
- **Product / Module:** Product not set in Jira / Reports
- **Work Type:** Enhancement
- **Summary:** Regulatory report templates updated to meet revised compliance requirements.
- **Technical Changes:**
  - Updated report layout.
  - Added new compliance fields.
  - Improved export performance.
- **API Changes:** `GET /reports/regulatory`
- **Database Changes:** Added `ComplianceCategory` column.
- **Validation:** Mandatory compliance fields.
- **Testing:** Completed.
- **Deployment Notes:** ⚠️ Report template deployment required.

## Known Issues

None reported for this release.

## Open Actions / Data-Quality Notes

- **KAN-7 — Missing Product in Jira:** The Product field (`customfield_10074`) is not set. Populate before the next extraction.
- **KAN-7 — Release/Product discrepancy:** Jira records **Release 14.1 / Product unset**, but the implementation note records **Release 14.2 / Product Mortgage Loan**. Reconcile before publishing customer-facing notes — if KAN-7 belongs to 14.2, remove it from this release.
- **Deployment ordering:** KAN-2 (DB index) and KAN-7 (report template deployment) both require manual deployment steps — confirm these are in the release runbook.
