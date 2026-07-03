# Loan Eligibility Rule Engine

## Jira Ticket
KAN-3

## Release Version
14.1

## Product
Business Loan

## Module
Loan Processing

## Work Type
Enhancement

## Business Objective
Improve loan eligibility calculation using configurable business rules.

## Technical Implementation
- Introduced rule engine.
- Externalized eligibility rules.
- Added rule priority support.
- Improved processing performance.

## API Changes
GET /loan/eligibility

## Database Changes
Created EligibilityRules table.

## Validation
Income, Age, Credit Score and Existing Loan checks.

## Testing
Completed successfully.

## Deployment Notes
Rule configuration required.
