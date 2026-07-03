# Bulk Customer Import

## Jira Ticket
KAN-1

## Release Version
14.1

## Product
Business Loan

## Module
Customer Details

## Work Type
Feature

## Business Objective
Enable operations users to upload multiple customer records using a CSV file, reducing manual data entry and onboarding time.

## Technical Implementation
- Developed CSV parsing service.
- Added customer validation framework.
- Implemented duplicate customer detection.
- Integrated Customer Service API.
- Added upload progress tracking and audit logging.

## API Changes
POST /customers/import

## Database Changes
Added BulkUploadId and UploadStatus columns to CustomerUpload table.

## Validation
- Mandatory fields validation
- Duplicate customer validation
- Invalid CSV format validation

## Testing
- Unit Testing completed
- Integration Testing completed
- Regression Testing passed

## Deployment Notes
No manual configuration required.