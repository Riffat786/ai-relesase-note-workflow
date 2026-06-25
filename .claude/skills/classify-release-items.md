# File: `.claude/skills/classify-release-items.md`

# Classification Rules

## Purpose

Provide consistent rules for classifying release items before generating release notes.

---

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

* customer-friendly-language.md
* release-note-template.md