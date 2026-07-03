# Expected Output — Sample 2 (Help Topic Structure Benchmark)



## CONTENT BENCHMARK — Help Topic



**Source:** `sample-data/sample-1-input.md` — WW-FEAT-301, What's New issue



This file shows the required output structure and quality standard for a

help topic generated per What's New feature. Agents use it as a

benchmark, all content is replaced with real Jira data at runtime. The

bug-fix table formatting rules previously kept in this file now live in

`skills/release-note-writer-skill.md` and `skills/release-note-reviewer-skill.md`;

this file exists to show what a compliant help topic actually looks like.



---



## AI Insight banner with contextual spending alerts <span class="tag tag-ai">AI</span>



*Release 1.0 · July 2026*



---



### Overview



**What it does:** Analyses your current month's spending in real time and

shows a banner on the Dashboard when a category is trending toward a

budget overrun, with a specific behavioural recommendation.



**Why it matters:** Previously, you only found out you had overspent

after opening the Budget or Transactions screen, often after the fact.

This banner surfaces the warning while you can still act on it.



**Key benefits:** Shows the exact category, percentage increase versus

last month, and projected overrun amount in rupees. Gives a specific

recommendation rather than a generic warning. Links directly to the AI

Advisor for a deeper plan. Is dismissible per session so it never feels

intrusive.



---



### Workflow



1. Open the Dashboard. WealthWise checks your spending across all

   categories against the same period last month.

2. If any category is more than 15% above last month's spending for the

   same period, the AI Insight banner appears at the top of the

   Dashboard.

3. Review the banner: it names the category, the percentage increase,

   the projected overrun in rupees, and a specific recommendation, for

   example cooking at home a few more days this week.

4. Select **Ask advisor** on the banner to open the AI Advisor for a more

   detailed plan, or dismiss the banner to continue to your Dashboard for

   this session.



---



*Back to [Release Notes](release-note-1-0-whats-new.html) | [Help Centre Home](#)*



---



## Notes for Agents Producing This Section



This example intentionally omits an **API Details** section. WW-FEAT-301

is a consumer-facing dashboard capability with no documented public API

endpoint in its Jira description, so the help-topic-writer-agent should

omit the section entirely and record:



```

[INSERT: API endpoint — not specified in Jira issue WW-FEAT-301, feature has no public API surface]

```



Do not invent an endpoint, method, or parameter table to fill this

section. An omitted API Details section is the expected, correct output

for most WealthWise consumer features, it is not a quality failure.
