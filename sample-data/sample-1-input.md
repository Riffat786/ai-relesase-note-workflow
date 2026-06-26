# New Feature release
## Source
Feature ID: WW-FEAT-301
Release: WealthWise — Q3 2026
## Feature Title
Dashboard Enhancement — AI Insight Banner with Contextual Spending Alerts
## Description
Users currently have no proactive visibility into spending trends until they manually navigate to the Transactions or Budget screens. By the time they notice an overspend, they have already exceeded their budget. The dashboard now includes a persistent AI Insight banner that analyses the user's current month spending in real time and surfaces a contextual alert with a specific recommendation before the budget is exceeded.
## Affected Workflow
Dashboard view → User reviews KPIs → User navigates away to find details
## Changed Behavior
Before: The dashboard showed static KPI cards (Net Worth, Monthly Savings, Total Spent, Goal Progress) with no proactive guidance. Users had to open the Budget or Transactions screens to understand whether their spending was on track. After:  A banner appears at the top of the dashboard whenever the AI detects a spending pattern that may lead to a budget overrun. The banner includes:
- The category where overspend is detected (e.g. dining)
- The percentage increase versus last month
- The projected budget overrun amount in rupees
- A specific behavioural recommendation (e.g. "Cook at home 3 more days this week")
- A direct link to Ask AI Advisor for further guidance
## Example Banner Content (from screen)
"You've spent 28% more on dining this month vs last. At this rate, you'll exceed your Rs 6,000 food budget by Rs 1,840. Consider cooking at home 3 more days this week."
## Acceptance Criteria
- Banner appears on the dashboard when spending in any category exceeds 15% above the prior month for the same period
- Banner shows category name, percentage increase, projected overrun amount, and a specific recommendation
- "Ask advisor" link navigates the user to the AI Advisor screen
- Banner is dismissible per session
- Banner does not appear if all categories are within 15% of prior month
## Affected Screens
- Dashboard (primary)
- AI Advisor (linked from banner)
## Audience
External — Individual users (dashboard primary view)
