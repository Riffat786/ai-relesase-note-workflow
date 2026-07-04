# Release Notes

## Release Version

**14.1**

## Overview

Release 14.1 focuses on faster customer onboarding, smarter loan decisioning, and a more reliable, uninterrupted user experience. This update introduces bulk customer onboarding and a configurable loan eligibility engine, while resolving issues around duplicate transactions and unexpected session timeouts. Together, these changes help teams work more efficiently and with greater confidence in day-to-day operations.

## New Features

**Bulk Customer Import**
- Onboard multiple customers at once by uploading a single file, instead of entering records one at a time. Data is validated as it is processed, potential duplicates are flagged, and upload progress is tracked throughout.
- **Customer Benefit:** Significantly reduces manual data entry and shortens onboarding time while helping ensure clean, accurate customer records.

## Enhancements

**Configurable Loan Eligibility Engine**
- Loan eligibility is now determined by configurable business rules that consider factors such as income, age, credit score, and existing loans. Rules can be prioritized and adjusted to match evolving business needs.
- **Customer Benefit:** Enables faster, more consistent loan decisions and lets the business adapt eligibility criteria without waiting on technical changes.

## Bug Fixes

**Duplicate Transaction Prevention**
- Resolved an issue that could allow the same transaction to be processed more than once. Each transaction is now verified before submission, and a clear message is shown when a potential duplicate is detected.
- **Customer Benefit:** Prevents unintended duplicate payments and improves the accuracy and reliability of transaction processing.

**Reliable Session Handling**
- Resolved an issue that caused users to be logged out unexpectedly during active sessions. Sessions now stay active during ongoing work and are maintained more reliably in the background.
- **Customer Benefit:** Reduces interruptions and prevents lost work, delivering a smoother and more dependable experience.

## Known Issues

None reported for this release.
