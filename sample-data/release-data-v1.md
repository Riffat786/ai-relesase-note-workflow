# Release Data v1

Consolidated release dataset correlating Jira business information (Atlassian MCP) with technical implementation details (GitHub MCP).

## Dataset Metadata

| Field | Value |
| --- | --- |
| Version | v1 |
| Generated | 2026-07-02 |
| Jira Project | KAN |
| Total Issues | 8 |
| Release Versions | 14.1, 14.2 |
| Jira Source | Atlassian MCP (`https://mcp.atlassian.com/v1/sse`) |
| GitHub Source | GitHub MCP (`Riffat786/ai-relesase-note-workflow`) |
| Implementation Notes Path | `sample-data/implementation-notes/` |

## Correlation Summary

| Jira Key | Summary | Release | Implementation Note | Match Status |
| --- | --- | --- | --- | --- |
| KAN-1 | Bulk Customer Import | 14.1 | `KAN-1 – Bulk Customer Import.md` | Matched |
| KAN-2 | Duplicate Transaction Validation | 14.1 | `KAN-2 – Duplicate Transaction Validation.md` | Matched |
| KAN-3 | Loan Eligibility Rule Engine | 14.1 | `KAN-3 – Loan Eligibility Rule Engine.md` | Matched |
| KAN-4 | Session Timeout Issue | 14.1 | `KAN-4 – Session Timeout Issue.md` | Matched |
| KAN-5 | Email Notification Template | 14.2 | `KAN-5 – Email Notification Template.md` | Matched |
| KAN-6 | Advanced customer Search Filter | 14.2 | `KAN-6 – Advanced Customer Search Filter.md` | Matched |
| KAN-7 | Update Regulatory Report Template | 14.2 | `KAN-7 – Update Regulatory Report Template.md` | Matched |
| KAN-8 | Custom Dashboard Widgets | 14.2 | `KAN-8 – Custom Dashboard Widgets.md` | Matched |

## Release 14.1

---

### KAN-1 — Bulk Customer Import

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-1 |
| Summary | Bulk Customer Import |
| Description | Added CSV-based bulk customer import to simplify customer onboarding and reduce manual effort. |
| Issue Type | Task |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T14:43:34.007+0530 |
| Updated | 2026-07-01T17:46:42.566+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-1 – Bulk Customer Import.md` |
| Release Version | 14.1 |
| Product | Business Loan |
| Module | Customer Details |
| Work Type | Feature |
| Business Objective | Enable operations users to upload multiple customer records using a CSV file, reducing manual data entry and onboarding time. |

**Technical Implementation**

- Developed CSV parsing service.
- Added customer validation framework.
- Implemented duplicate customer detection.
- Integrated Customer Service API.
- Added upload progress tracking and audit logging.

**API Changes:** `POST /customers/import`

**Database Changes:** Added BulkUploadId and UploadStatus columns to CustomerUpload table.

**Validation:** Mandatory fields validation; duplicate customer validation; invalid CSV format validation.

**Testing:** Unit, integration, and regression testing completed.

**Deployment Notes:** No manual configuration required.

#### Correlation Notes

- Jira issue type is **Task**; implementation note classifies work type as **Feature**.
- Jira description aligns with the implementation note business objective.

---

### KAN-2 — Duplicate Transaction Validation

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-2 |
| Summary | Duplicate Transaction Validation |
| Description | Fixed duplicate transaction processing by validating transaction references before payment submission. |
| Issue Type | Bug |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T14:45:40.348+0530 |
| Updated | 2026-07-01T17:46:46.481+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-2 – Duplicate Transaction Validation.md` |
| Release Version | 14.1 |
| Product | Business Loan |
| Module | Loan Processing |
| Work Type | Bug |
| Business Objective | Prevent duplicate loan transactions from being processed. |

**Technical Implementation**

- Added duplicate transaction validation.
- Compared Transaction ID before processing.
- Implemented duplicate transaction logging.
- Displayed user-friendly validation message.

**API Changes:** None

**Database Changes:** Added TransactionHash index.

**Validation:** Duplicate Transaction ID; duplicate request payload; duplicate reference number.

**Testing:** Unit, integration, and regression completed.

**Deployment Notes:** Database index required.

#### Correlation Notes

- Issue type and summary align across Jira and GitHub sources.

---

### KAN-3 — Loan Eligibility Rule Engine

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-3 |
| Summary | Loan Eligibility Rule Engine |
| Description | Introduced a configurable loan eligibility rule engine to support business-driven rule management. |
| Issue Type | Feature |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T14:51:18.344+0530 |
| Updated | 2026-07-01T17:46:50.325+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-3 – Loan Eligibility Rule Engine.md` |
| Release Version | 14.1 |
| Product | Business Loan |
| Module | Loan Processing |
| Work Type | Enhancement |
| Business Objective | Improve loan eligibility calculation using configurable business rules. |

**Technical Implementation**

- Introduced rule engine.
- Externalized eligibility rules.
- Added rule priority support.
- Improved processing performance.

**API Changes:** `GET /loan/eligibility`

**Database Changes:** Created EligibilityRules table.

**Validation:** Income, age, credit score, and existing loan checks.

**Testing:** Completed successfully.

**Deployment Notes:** Rule configuration required.

#### Correlation Notes

- Jira issue type is **Feature**; implementation note classifies work type as **Enhancement**.
- Both sources describe the same configurable rule engine capability.

---

### KAN-4 — Session Timeout Issue

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-4 |
| Summary | Session Timeout Issue |
| Description | Fixed unexpected user session timeouts by improving session management logic. |
| Issue Type | Bug |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T14:53:34.642+0530 |
| Updated | 2026-07-01T17:46:55.782+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-4 – Session Timeout Issue.md` |
| Release Version | 14.1 |
| Product | Personal Loan |
| Module | Dashboard |
| Work Type | Bug |
| Business Objective | Prevent unexpected user logout during active sessions. |

**Technical Implementation**

- Fixed session timeout logic.
- Implemented activity heartbeat.
- Improved token refresh mechanism.

**API Changes:** None

**Database Changes:** None

**Validation:** Active session validation.

**Testing:** Completed.

**Deployment Notes:** Clear browser cache after deployment.

#### Correlation Notes

- Issue type and summary align across Jira and GitHub sources.

---

## Release 14.2

---

### KAN-5 — Email Notification Template

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-5 |
| Summary | Email Notification Template |
| Description | Updating email notification templates to support the latest branding and communication standards. |
| Issue Type | Feature |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T14:55:47.338+0530 |
| Updated | 2026-07-01T17:47:12.161+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-5 – Email Notification Template.md` |
| Release Version | 14.2 |
| Product | Business Loan |
| Module | Taskboard |
| Work Type | Feature |
| Business Objective | Provide standardized email notifications for loan processing events. |

**Technical Implementation**

- Added HTML email templates.
- Introduced placeholder engine.
- Configurable notification settings.

**API Changes:** `POST /notifications/email`

**Database Changes:** Created EmailTemplate table.

**Validation:** Template validation and placeholder validation.

**Testing:** Completed.

**Deployment Notes:** SMTP configuration required.

#### Correlation Notes

- Jira description emphasizes branding; implementation note emphasizes loan processing event notifications.

---

### KAN-6 — Advanced Customer Search Filter

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-6 |
| Summary | Advanced customer Search Filter |
| Description | Enhanced customer search with additional filters for faster and more accurate customer lookup. |
| Issue Type | Enhancement |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T17:01:54.199+0530 |
| Updated | 2026-07-01T17:47:16.435+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-6 – Advanced Customer Search Filter.md` |
| Release Version | 14.2 |
| Product | Personal Loan |
| Module | Customer Details |
| Work Type | Enhancement |
| Business Objective | Allow users to search customers using multiple filter criteria. |

**Technical Implementation**

- Added advanced search filters.
- Optimized database queries.
- Added pagination.

**API Changes:** `GET /customers/search`

**Database Changes:** Added composite indexes.

**Validation:** Filter validation.

**Testing:** Completed.

**Deployment Notes:** None.

#### Correlation Notes

- Issue type and summary align across Jira and GitHub sources.

---

### KAN-7 — Update Regulatory Report Template

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-7 |
| Summary | Update Regulatory Report Template |
| Description | Updated regulatory report templates to comply with the latest reporting standards. |
| Issue Type | Enhancement |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T17:07:50.081+0530 |
| Updated | 2026-07-01T17:47:20.779+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-7 – Update Regulatory Report Template.md` |
| Release Version | 14.2 |
| Product | Mortgage Loan |
| Module | Reports |
| Work Type | Enhancement |
| Business Objective | Update regulatory reports to meet revised compliance requirements. |

**Technical Implementation**

- Updated report layout.
- Added new compliance fields.
- Improved export performance.

**API Changes:** `GET /reports/regulatory`

**Database Changes:** Added ComplianceCategory column.

**Validation:** Mandatory compliance fields.

**Testing:** Completed.

**Deployment Notes:** Report template deployment required.

#### Correlation Notes

- Jira and implementation note both reference regulatory/compliance reporting updates.

---

### KAN-8 — Custom Dashboard Widgets

#### Jira (Business)

| Field | Value |
| --- | --- |
| Key | KAN-8 |
| Summary | Custom Dashboard Widgets |
| Description | Added configurable dashboard widgets to improve user productivity and personalization. |
| Issue Type | Feature |
| Status | Done |
| Priority | Medium |
| Assignee | bhargavi chary |
| Reporter | bhargavi chary |
| Created | 2026-07-01T17:38:13.007+0530 |
| Updated | 2026-07-01T17:47:25.751+0530 |

#### GitHub Implementation Note (Technical)

| Field | Value |
| --- | --- |
| File | `sample-data/implementation-notes/KAN-8 – Custom Dashboard Widgets.md` |
| Release Version | 14.2 |
| Product | Business Loan |
| Module | Dashboard |
| Work Type | Feature |
| Business Objective | Allow users to personalize dashboard widgets based on preferences. |

**Technical Implementation**

- Added widget configuration framework.
- Developed drag-and-drop layout.
- Saved user preferences.

**API Changes:** `GET /dashboard/widgets`

**Database Changes:** Created UserDashboardPreference table.

**Validation:** Widget configuration validation.

**Testing:** Completed.

**Deployment Notes:** No additional deployment activities.

#### Correlation Notes

- Issue type and summary align across Jira and GitHub sources.

---

## Release Summary by Version

### Release 14.1 (4 items)

| Key | Summary | Work Type (GitHub) | Product | Module |
| --- | --- | --- | --- | --- |
| KAN-1 | Bulk Customer Import | Feature | Business Loan | Customer Details |
| KAN-2 | Duplicate Transaction Validation | Bug | Business Loan | Loan Processing |
| KAN-3 | Loan Eligibility Rule Engine | Enhancement | Business Loan | Loan Processing |
| KAN-4 | Session Timeout Issue | Bug | Personal Loan | Dashboard |

### Release 14.2 (4 items)

| Key | Summary | Work Type (GitHub) | Product | Module |
| --- | --- | --- | --- | --- |
| KAN-5 | Email Notification Template | Feature | Business Loan | Taskboard |
| KAN-6 | Advanced Customer Search Filter | Enhancement | Personal Loan | Customer Details |
| KAN-7 | Update Regulatory Report Template | Enhancement | Mortgage Loan | Reports |
| KAN-8 | Custom Dashboard Widgets | Feature | Business Loan | Dashboard |

## Data Quality Notes

- All 8 Jira issues in project KAN have a matching implementation note in GitHub.
- Jira fix versions were not populated; release version grouping comes from GitHub implementation notes.
- Minor classification differences exist between Jira issue types and GitHub work types for KAN-1 (Task vs Feature) and KAN-3 (Feature vs Enhancement).
- Jira descriptions are concise business summaries; GitHub implementation notes contain full technical detail including API, database, validation, testing, and deployment information.
