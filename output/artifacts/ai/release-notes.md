# Release 2025.8

## Overview
Release 2025.8 brings enhanced security capabilities and improved reporting functionality to our platform. This release focuses on protecting user accounts with multi-factor authentication, enabling customers to export their critical business data, and improving overall system performance. We've also addressed important issues to ensure a more reliable experience across the portal.

## New Features

| ID | Title | Description |
|---|---|---|
| US-1001 | Multi-Factor Authentication | Users can now secure their accounts with multi-factor authentication using email verification. This additional security layer helps protect against unauthorized access. |
| US-1002 | Export Dashboard Reports | Users can now export their dashboard reports directly to PDF format. This makes it easy to share reports, archive data, and integrate insights into presentations and documentation. |

## Enhancements

| ID | Title | Description |
|---|---|---|
| US-1003 | Improved Search Performance | Search response times have been significantly reduced across the portal. Users will experience faster query results and improved productivity when searching for information. |

## Bug Fixes

| ID | Title | Description |
|---|---|---|
| BUG-2001 | Password Reset Email Failure | Resolved an issue where password reset emails were not being delivered to some users. Account recovery now works reliably for all users. |
| BUG-2002 | Duplicate Notifications | Fixed an issue causing duplicate notifications to appear in user accounts. Users will now receive notifications exactly once as intended. |

## Known Limitations

- **Large PDF exports may take longer than expected** (Low severity): When exporting large datasets to PDF format, the export process may require additional time to complete. We recommend waiting until the export finishes before navigating away from the page.
