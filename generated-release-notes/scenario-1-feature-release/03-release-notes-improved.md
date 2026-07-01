# Release 5.4 - Improved Release Notes

Based on review findings and recommendations from `02-review-results.md`

---

# Release Overview

Release 5.4 emphasizes security enhancements and operational efficiency, introducing new authentication capabilities and reporting improvements alongside critical issue resolutions.

---

## New Features

### Multi-Factor Authentication

Users can now enable multi-factor authentication using authenticator applications for enhanced account security. Recommended for organizations with security-sensitive users and compliance requirements.

---

## Enhancements

### Dashboard Export to Excel

Users can now export dashboard data directly to Microsoft Excel format, enabling easier data sharing, analysis, and integration with business intelligence workflows.

---

## Resolved Issues

### Report Export Reliability

Resolved an issue that could prevent large reports from exporting successfully, ensuring users can reliably download complete datasets.

---

## Known Limitations

- Multi-factor authentication currently supports authenticator applications only. SMS and email-based authentication methods are planned for future releases.
- Excel export is optimized for reports up to 100,000 records. Larger datasets may require manual optimization.

---

## Security Considerations

This release introduces multi-factor authentication as a recommended security control. Organizations should plan rollout and user communication accordingly.
