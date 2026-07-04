  # Release Data Extraction Report

  ## Release Information

  - **Release Version:** 14.1
  - **Project:** KAN (twtaibhargavi.atlassian.net)
  - **Product:** Business Loan, Personal Loan
  - **Module:** Customer Details, Loan Processing, Dashboard
  - **Total Jira Issues:** 4 (KAN-1, KAN-2, KAN-3, KAN-4)
  - **Total Implementation Notes:** 4
  - **Extraction Date:** 2026-07-04

  ---

  ## Consolidated Release Dataset

  ### KAN-1

  #### Business Information
  - **Summary:** Bulk Customer Import
  - **Description:** Added CSV-based bulk customer import to simplify customer onboarding and reduce manual effort.
  - **Status:** Done
  - **Assignee:** bhargavi chary
  - **Product:** Business Loan
  - **Module:** Customer Details
  - **Release Version:** 14.1

  #### Technical Information
  - **Technical Implementation Summary:** Enable operations users to upload multiple customer records using a CSV file, reducing manual data entry and onboarding time.
  - **Files Modified:** Not specified in implementation note
  - **Technical Changes:**
    - Developed CSV parsing service.
    - Added customer validation framework.
    - Implemented duplicate customer detection.
    - Integrated Customer Service API.
    - Added upload progress tracking and audit logging.
  - **Configuration Changes:** No manual configuration required.
  - **API Changes:** POST /customers/import
  - **Database Changes:** Added BulkUploadId and UploadStatus columns to CustomerUpload table.
  - **Testing Notes:**
    - Unit Testing completed
    - Integration Testing completed
    - Regression Testing passed
    - Validation: Mandatory fields validation, Duplicate customer validation, Invalid CSV format validation
  - **Known Limitations:** None documented
  - **Developer Notes:** Work Type — Feature. No manual configuration required for deployment.

  ---

  ### KAN-2

  #### Business Information
  - **Summary:** Duplicate Transaction Validation
  - **Description:** Fixed duplicate transaction processing by validating transaction references before payment submission.
  - **Status:** Done
  - **Assignee:** bhargavi chary
  - **Product:** Business Loan
  - **Module:** Loan Processing
  - **Release Version:** 14.1

  #### Technical Information
  - **Technical Implementation Summary:** Prevent duplicate loan transactions from being processed.
  - **Files Modified:** Not specified in implementation note
  - **Technical Changes:**
    - Added duplicate transaction validation.
    - Compared Transaction ID before processing.
    - Implemented duplicate transaction logging.
    - Displayed user-friendly validation message.
  - **Configuration Changes:** Database index required.
  - **API Changes:** None
  - **Database Changes:** Added TransactionHash index.
  - **Testing Notes:**
    - Unit, Integration and Regression completed.
    - Validation: Duplicate Transaction ID, Duplicate Request Payload, Duplicate Reference Number
  - **Known Limitations:** None documented
  - **Developer Notes:** Work Type — Bug. Database index required for deployment.

  ---

  ### KAN-3

  #### Business Information
  - **Summary:** Loan Eligibility Rule Engine
  - **Description:** Introduced a configurable loan eligibility rule engine to support business-driven rule management.
  - **Status:** Done
  - **Assignee:** bhargavi chary
  - **Product:** Business Loan
  - **Module:** Loan Processing
  - **Release Version:** 14.1

  #### Technical Information
  - **Technical Implementation Summary:** Improve loan eligibility calculation using configurable business rules.
  - **Files Modified:** Not specified in implementation note
  - **Technical Changes:**
    - Introduced rule engine.
    - Externalized eligibility rules.
    - Added rule priority support.
    - Improved processing performance.
  - **Configuration Changes:** Rule configuration required.
  - **API Changes:** GET /loan/eligibility
  - **Database Changes:** Created EligibilityRules table.
  - **Testing Notes:**
    - Completed successfully.
    - Validation: Income, Age, Credit Score and Existing Loan checks.
  - **Known Limitations:** None documented
  - **Developer Notes:** Work Type — Enhancement. Rule configuration required for deployment.

  ---

  ### KAN-4

  #### Business Information
  - **Summary:** Session Timeout Issue
  - **Description:** Fixed unexpected user session timeouts by improving session management logic.
  - **Status:** Done
  - **Assignee:** bhargavi chary
  - **Product:** Personal Loan
  - **Module:** Dashboard
  - **Release Version:** 14.1

  #### Technical Information
  - **Technical Implementation Summary:** Prevent unexpected user logout during active sessions.
  - **Files Modified:** Not specified in implementation note
- **Technical Changes:**
  - Fixed session timeout logic.
  - Implemented activity heartbeat.
  - Improved token refresh mechanism.
- **Configuration Changes:** Clear browser cache after deployment.
- **API Changes:** None
- **Database Changes:** None
- **Testing Notes:**
  - Completed.
  - Validation: Active session validation.
- **Known Limitations:** None documented
- **Developer Notes:** Work Type — Bug. Clear browser cache after deployment.

---

## Validation Report

- **Missing Implementation Notes:** None. All 4 Jira issues (KAN-1, KAN-2, KAN-3, KAN-4) have a matching Markdown implementation note.
- **Missing Jira Issues:** None. All Release 14.1 implementation notes have a corresponding Jira issue.
- **Duplicate Records:** None detected.
- **Missing Metadata:**
  - **Product / Module / Release Version not populated in Jira:** For every KAN issue, the Jira `fixVersions`, `components`, and `labels` fields are empty and there are no Product/Module/Release custom fields. These three attributes were sourced from the GitHub implementation notes. Jira was not modified.
- **Data Discrepancies:** None. For KAN-1 through KAN-4 the Jira Summary/Description align with the implementation-note content.
- **Unmatched Markdown Files:** None for Release 14.1. The implementation-notes folder also contains KAN-5, KAN-6, KAN-7, and KAN-8, but their implementation notes state Release Version 14.2, so they are out of scope for Release 14.1 (each still maps to an existing Jira issue).

---

*Source systems: Jira (Atlassian MCP — project KAN, site twtaibhargavi.atlassian.net) for business information; repository implementation notes (`sample-data/implementation-notes/`) for technical information and release/product/module metadata. No Jira data or implementation notes were modified. Release membership determined by the "Release Version" field inside each implementation note, as Jira carries no version data.*
