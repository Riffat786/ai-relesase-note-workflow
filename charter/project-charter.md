# Project Charter

## Project Name

AI-Powered Release Note Workflow Automation

## Project Owner

Riffat Wyne

## Project Duration

22 June 2026 – 05 July 2026

## Background

Creating release notes is often a manual and repetitive process that requires collecting information from multiple sources, drafting content, reviewing quality, and preparing final communications.

This project is part of the TWT AI Mastery certification workshop and will use release notes generation as a practical business use case to demonstrate AI capabilities including Commands, Skills, Agents, Marketplace integrations, Plugins, and MCP.

## Problem Statement

## Problem Statement

Creating release notes is a time-consuming and largely manual process for technical writers.

For every product release, developers or Subject Matter Experts (SMEs) provide the list of completed work items from the issue tracking system (Jira for this prototype). Depending on how the release data is exported, the information may be organized by release version, module, or as a single consolidated list containing new features, enhancements, bug fixes, and hotfixes.

Before documentation can begin, the technical writer must manually filter, categorize, and reorganize the release data into a consumable format. Depending on the release, this may involve grouping tickets by release version, module, or change type before the documentation process can even start. This preparation is repetitive, time-consuming, and varies for every release.

Once the data has been organized, the technical writer manually creates release-note entries using a predefined template that includes the headline, what changed, why the change was introduced, where the change applies, implementation or configuration details, and any known limitations. The completed release notes must then be reviewed for clarity, consistency, grammar, and compliance with the Microsoft Writing Style Guide before publication.

This project proposes an AI-assisted release note workflow that uses Atlassian MCP to retrieve release information from Jira, automatically structures the content into a standardized release-note template, validates the language against the Microsoft Writing Style Guide, and keeps the technical writer involved through mandatory human review and approval checkpoints before generating the final online-help output.


## Project Goal

To design and demonstrate an AI-assisted release note workflow that uses Atlassian MCP to retrieve release information from Jira, automatically structures the content into a standardized release-note template, validates the content against the Microsoft Writing Style Guide, and keeps the technical writer involved through mandatory human review and approval checkpoints before generating HTML/XML output.


## Target Users

- Technical Writers
- Product Managers
- Release Managers
- Documentation Teams
- Development Teams

## Scope

### In Scope

- Atlassian MCP integration
- Jira ticket retrieval
- Release note structuring
- Microsoft Writing Style Guide validation
- HTML/XML generation
- Human approval workflow
- Demo-ready proof of concept

### Out of Scope

- Production-ready solution
- Full system integrations
- Publishing automation
- Support for all documentation types
- Complete replacement of human review

## Sample Workflow

Change Information
→ Information Extraction
→ Release Note Draft
→ AI Review
→ Draft Improvement
→ Human Approval

## Success Criteria

The project will be considered successful if:

- Successfully retrieve sample Jira tickets using Atlassian MCP.
- Generate structured release notes from sample ticket data.
- Demonstrate Microsoft Writing Style Guide validation.
- Demonstrate human approval checkpoints.
- Generate HTML/XML output.
- Demonstrate an end-to-end workflow using realistic sample data.

## Deliverables

- Updated Project Charter
- Current (As-Is) Workflow
- Future (To-Be) Workflow
- Architecture Diagram
- Sample Jira Tickets
- Release Note Structuring Skill
- Microsoft Writing Style Guide Review Skill
- HTML/XML Generation Skill
- Release Note Generation Command
- Release Note Review Command
- Agent Workflow
- Working Prototype
- Demo Presentation

## Timeline


| Milestone                    | Target Date    |
| ---------------------------- | -------------- |
| Repository Setup             | 22 Jun 2026    |
| Team Formation               | 22-24 Jun 2026 |
| Discovery & Workflow Mapping | 24 Jun 2026    |
| Initial Prototype            | 27 Jun 2026    |
| Validation & Refinement      | 30 Jun 2026    |
| Demo Package Ready           | 02 Jul 2026    |
| Final Rehearsal              | 04 Jul 2026    |
| Poc Presentation             | 05 Jul 2026    |


## Risks

- Limited time available during the workshop
- Team members have varying levels of AI experience
- Scope expansion beyond workshop objectives
- Over-engineering the solution instead of demonstrating capabilities

## Guiding Principle

The objective is not to build the best release note generator. The objective is to demonstrate how AI capabilities can automate and improve a realistic documentation workflow.
