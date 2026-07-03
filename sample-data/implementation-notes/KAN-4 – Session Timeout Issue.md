# Session Timeout Issue

## Jira Ticket
KAN-4

## Release Version
14.1

## Product
Personal Loan

## Module
Dashboard

## Work Type
Bug

## Business Objective
Prevent unexpected user logout during active sessions.

## Technical Implementation
- Fixed session timeout logic.
- Implemented activity heartbeat.
- Improved token refresh mechanism.

## API Changes
None

## Database Changes
None

## Validation
Active session validation.

## Testing
Completed.

## Deployment Notes
Clear browser cache after deployment.