# Bug fix or enhancements
## Source
Bug ID: WW-DASH-101
Release: WealthWise — Q3 2026
## Bug Title
Dashboard Metrics Displaying Stale and Incorrect Values
## Bug Description
Three KPI cards on the dashboard are showing inaccurate data:
- Total Spent card shows a value that does not reflect the current month's transactions. The figure lags behind actual spend recorded in the Transactions screen by up to 24 hours.
- Monthly Savings card displays an incorrect percentage change because the prior month baseline is being read from a cached value that is not invalidated when new transactions are added.
- Goal Progress card shows a stale completion percentage. Progress updates only when the user navigates away from the dashboard and returns, rather than reflecting the current state on load.
## Observed Behavior
Users see KPI values on the dashboard that do not match what is shown on the Transactions and Budget screens. For example:
- Dashboard shows Total Spent: Rs 52,400 with "8% above budget"
- Transactions screen shows a higher actual total for the same period
- Monthly Savings shows "12% vs last month" based on outdated baseline
- Goal Progress shows 68% even after a qualifying transaction has been recorded that should move the percentage higher
## Expected Behavior
All four KPI cards on the dashboard — Net Worth, Monthly Savings, Total Spent, and Goal Progress — must reflect real-time data on every page load and after every transaction is added.
## Resolution Details
### Backend Fixes
- Total Spent now reads directly from the live transaction aggregation endpoint rather than the daily batch summary.
- Monthly Savings percentage is recalculated on each dashboard load using the current month total against the prior month actuals, not the cached baseline.
- Goal Progress is now recomputed server-side on each request, factoring in all transactions recorded up to the request timestamp.
### Cache Updates
- Dashboard KPI cache TTL reduced from 24 hours to 5 minutes.
- Cache is invalidated immediately when a new transaction is added via the Add transaction flow.
### QA Validation
- Regression tests confirmed all four KPI cards match the Transactions screen totals within the same session.
- Tested across scenarios: new transaction added, transaction edited, transaction deleted.
## User Impact
Before fix: Users see KPI values that do not match their actual financial position, reducing trust in the dashboard and leading to incorrect budget decisions.
After fix:
- Total Spent reflects all transactions recorded up to the current moment.
- Monthly Savings percentage is accurate against the true prior month total.
- Goal Progress updates immediately after qualifying transactions.
- All four KPI cards are consistent with the Transactions and Budget screens.
## Affected Screens
- Dashboard (KPI cards: Net Worth, Monthly Savings, Total Spent, Goal Progress)
## Audience
External — Individual users (dashboard primary view)" 
