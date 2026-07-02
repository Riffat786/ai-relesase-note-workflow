---
name: classify-release-items
description: Classifies collected release items into customer-facing categories such as Features, Enhancements, and Bug Fixes while filtering internal work.
version: 1.0.0
---

# Classify Release Items

## Purpose

Classify collected release items into customer-facing categories and provide consistent rules for release note generation.

## Responsibilities

- Identify customer-facing work
- Categorize Features
- Categorize Enhancements
- Categorize Bug Fixes
- Exclude internal-only work
- Preserve work item IDs
- Preserve customer impact
- Produce structured output for the Writer Agent

## Rules

- Do not rewrite descriptions.
- Preserve traceability.
- Exclude technical implementation details that provide no customer value.

## Categories

### New Feature

A completely new capability available to customers.

Examples:

* Multi-factor authentication
* Export reports
* New dashboard

---

### Enhancement

An improvement to an existing capability.

Examples:

* Faster search
* Improved navigation
* Better accessibility

---

### Bug Fix

A customer-facing defect that has been corrected.

Examples:

* Password reset issue
* Duplicate notifications
* Display issue

---

### Known Issue

A limitation that still exists and should be communicated.

---

## Exclude from Release Notes

Do not include:

* Database migrations
* Infrastructure updates
* Refactoring
* Logging improvements
* CI/CD changes
* Deployment activities
* Code cleanup
* Test automation
* Dependency upgrades

unless they directly affect customer experience.

---

## Decision Rule

If a customer would notice the change, include it.

If only developers or system administrators would notice it, exclude it.

---

## Success Criteria

Every release item is placed into the correct category before release notes are generated.

---

## Related Skills

* customer-friendly-language/SKILL.md
* release-note-template/SKILL.md