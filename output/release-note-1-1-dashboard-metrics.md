## Bug Fix

### Dashboard metrics not updating in real time

Three KPI metrics on the dashboard were not updating consistently. Addresses Validated showed counts lagging by up to 24 hours. Compliance Passes displayed incorrect percentages because EU shipment data was excluded from the calculation. Delivery Success Rate was miscalculated because corrected addresses were not included in the figures. Operations teams saw stale values that did not reflect their actual shipment activity, reducing confidence in the dashboard as a tool for decision-making.

This issue is now resolved. Addresses Validated, Compliance Passes, and Delivery Success Rate refresh every 15 minutes and reflect current data on every page load. Compliance calculations now include EU shipment data, and the Delivery Success Rate formula correctly accounts for corrected addresses. All three metrics are consistent with the values shown on the Transactions and Compliance screens.

---

1.1
