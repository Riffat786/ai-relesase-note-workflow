# Review Release Notes

## Purpose

Review the generated release notes to ensure they are accurate, customer-focused, compliant with organizational standards, and ready for publication.

## Input

Generated Release Notes:

$ARGUMENTS 

## Instructions

Use the **Release Note Reviewer** skill to:

1. Determine the target audience before starting the review.
  Ask the user:
  Who is the target audience for these release notes?
  1. Customer
  2. Internal
    If the audience is not specified, do not begin the review until the user provides a response. Pass the selected audience to the Release Note Reviewer skill and apply the corresponding review rules..
2. Review the release notes specified in `$ARGUMENTS`.
3. Verify:
  - Business accuracy
  - Customer readability
  - Documentation quality
  - Template compliance
  - Completeness
  - Consistency
  - Publication readiness
4. Identify any issues or recommendations.
5. Generate a structured review report.

## Output

Generate:

- `sample-data/release-note-review-report.md`

