# WealthWise — Release 1.0 (July 2026)

Release 1.0 brings two AI-powered features for personalized financial guidance: AI Financial Advisor chat and Investment Portfolio Tracking. New enhancements add AI-assisted budget rebalancing and transaction categorization. Three bug fixes address budget display, notification duplication, and onboarding navigation. One known issue documents potential latency in brokerage data sync.

---

## 🚀 What's New

### AI Financial Advisor chat interface (AI)

Previously, you could not ask your financial app direct questions about your spending, budgets, or investment strategy without manually analyzing your data yourself. Now, the AI Advisor answers natural-language questions about your financial life using your actual transaction, budget, goal, and investment data, returning specific, numeric, actionable guidance. You access the Advisor from the dashboard sidebar or directly from Overview, Budget, and Investments views. The chat interface shows your conversation history and suggests starter questions to get you thinking about different aspects of your finances. While the Advisor generates a response, you see a typing indicator so you know it's working.

**Key benefits**

- Ask follow-up questions and get answers tailored to your real data, not generic advice
- See your entire financial picture through the Advisor's recommendations—spending patterns, rebalancing opportunities, goal-pacing insights
- Available to Pro and Family subscription tiers

[Learn more →](help-topic-ai-financial-advisor-chat.html)

---

### Investment portfolio tracking (AI)

Previously, your investment holdings lived in separate apps and statements with no unified view. You could not see your total value, performance, or asset allocation in one place. Now, the Investments module consolidates all your holdings—mutual funds, stocks, gold bonds, debt funds—into one portfolio view. You see portfolio-level metrics: total value, total invested, total return %, and XIRR. A holdings table shows each investment's name, type, units, NAV, market value, and return. You can export your holdings as CSV and set target allocations. When your portfolio drifts from your targets, the AI alerts you to rebalance. This feature is available to Pro and Family subscription tiers.

**Key benefits**

- Track consolidated performance across all investment types at a glance
- Identify rebalancing opportunities before drift becomes significant
- Export holdings data for tax or advisory workflows
- Available to Pro and Family subscription tiers

[Learn more →](help-topic-investment-portfolio-tracking.html)

---

## ✨ Enhancements

- Get AI-generated rebalancing recommendations when any budget category exceeds its limit, with a one-click Auto-rebalance action that reallocates from underspent categories (Pro and Family only; exact overage and source categories displayed clearly) (AI)
- Surface AI auto-categorization confidence in your Transactions view, with an Insight banner showing how many transactions are auto-categorized versus flagged for manual review, and a quick link to review and correct uncategorized items (AI)

---

## 🐛 Bug Fixes

| Bug ID | Description | Fix / Solution |
|--------|--------------|-----------------|
| #5 | Category and total budget values above ₹1,00,000 displayed incorrect rounding. | Budget totals now match the exact sum of transactions to the rupee. |
| #6 | Recurring bill reminders triggered multiple times for the same bill in a single notification cycle. | Reminders now send exactly once per configured frequency without duplication. |
| #7 | When you navigated backward from Step 4 to Step 3 during onboarding, slider values reset to defaults. | Slider values now persist when navigating backward, maintaining user input. |

---

## Known Issues

- **Delayed sync for linked brokerage holdings:** Holdings synced from certain third-party brokerage connections (e.g., Zerodha) may reflect data up to two hours out of date rather than near-real-time, due to aggregator API polling intervals. This does not affect manually entered holdings or bank transaction sync. Portfolio value and XIRR may lag market-hours pricing by up to two hours. No data loss or incorrect transaction records occur—this is a display latency only. We plan to investigate webhook-based sync with the aggregator to replace polling, targeted for v1.1.

---

*Need help with a feature? Visit the WealthWise Help Centre or ask the AI Advisor.*
