# Expected Output — Sample 1 (Release Notes Structure Benchmark)



## Release — WealthWise 1.0



## CONTENT BENCHMARK — Release Notes



**Source:** `sample-data/sample-1-input.md` (What's New) and

`sample-data/sample-2-input.md` (Bug Fix)



This file shows the required output structure and quality standard for

the consolidated release note. Agents use it as a benchmark, all content

is replaced with real Jira data at runtime. No variables or placeholders

appear in actual generated output. The detailed writing rules behind this

example live in `skills/release-note-writer-skill.md`; the abstract

title, narrative, and content-quality criteria previously kept in this

file now live there, this file exists to show what compliant output

actually looks like.



---



## WealthWise — Release 1.0 (July 2026)



Release 1.0 delivers one new AI-powered dashboard capability, one

enhancement to transaction visibility, resolves one bug fix in dashboard

metric accuracy, and documents no known issues.



---



## 🚀 What's New



### AI Insight banner with contextual spending alerts <span class="tag tag-ai">AI</span>



Previously, you had no proactive visibility into your spending trends

until you manually opened the Transactions or Budget screens, and by the

time you noticed an overspend, you had already gone past your budget.

Now, the Dashboard shows a persistent AI Insight banner that reads your

current month's spending in real time and surfaces a contextual alert

with a specific recommendation before you exceed your budget. You catch

overspending while there is still time to change course, instead of

finding out after the fact.



**Key benefits**



- See the exact category, percentage increase, and projected overrun

  amount driving a potential overspend, before it happens

- Get a specific behavioural suggestion, not a generic warning

- Jump straight from the banner to the AI Advisor for a deeper plan



[Learn more →](help-topic-ww-feat-301-ai-insight-banner.html)



---



## 🐛 Bug Fixes



| Bug ID | Description | Fix / Solution |

|--------|--------------|------------------|

| WW-DASH-101 | The Total Spent, Monthly Savings, and Goal Progress cards on the Dashboard showed values that did not match the Transactions and Budget screens, in some cases lagging by up to 24 hours. | All three Dashboard cards now read live data on every page load and update immediately after you add, edit, or delete a transaction. |



---

© 2026 WealthWise. All rights reserved.

Need help? Visit the WealthWise Help Centre or ask the AI Advisor.
