# Expected Output — Sample 2 (Bug Fix)
# Release: GlobalMail Pro 1.1
#
# CONTENT BENCHMARK ONLY.
# This file defines what the prose should say and how it should be structured.
# Company name, page header, copyright footer, and HTML styling are applied
# by the Branding Skill at HTML render time.
# See: skills/branding-style-guide.md
#
# WHAT THE AGENT ADDS AT HTML RENDER TIME:
#   Page title:  Bug Fix — GlobalMail Pro Help Centre
#   HTML header: GlobalMail Pro | Help Centre  (navy bar)
#   HTML footer: © 2026 GlobalMail Pro. All rights reserved.
#   File name:   release-note-1-1-dashboard-metrics-fix.html
#
# NOTE ON SCOPE: The source document (Release 1.1) lists four bug fixes
# (GM-DASH-101, GM-ADDR-201, GM-COMP-305, GM-SEC-410). This expected output
# covers GM-DASH-101 (dashboard metrics) as the primary sample scenario.
# Each bug fix should be its own release note file. See note at the bottom.

---

## Bug Fix

### Dashboard metrics not updating in real time

Three KPI metrics on the dashboard were not updating consistently.
Addresses Validated showed counts lagging by up to 24 hours. Compliance
Passes displayed incorrect percentages because EU shipment data was
excluded from the calculation. Delivery Success Rate was miscalculated
because corrected addresses were not included in the figures. Operations
teams saw stale values that did not reflect their actual shipment activity,
reducing confidence in the dashboard as a tool for decision-making.

This issue is now resolved. Addresses Validated, Compliance Passes, and
Delivery Success Rate refresh every 15 minutes and reflect current data
on every page load. Compliance calculations now include EU shipment data,
and the Delivery Success Rate formula correctly accounts for corrected
addresses. All three metrics are consistent with the values shown on
the Transactions and Compliance screens.

---

1.1

---
