# Collaboration Instructions for Team Members

## Purpose

This repository is the official source of truth for the project.

All project-related work, decisions, documentation, prompts, skills, workflows, validation notes, and demo materials should be stored here and not only in chats, emails, or personal files.

---

# How We Will Collaborate

## GitHub Issues

Work should be tracked through GitHub Issues whenever possible.

Examples:

- Workflow Mapping
- Sample Data Collection
- Command Design
- Skills Design
- Agent Workflow Design
- MCP Research
- Validation
- Demo Preparation

Each issue should have:

- A clear objective
- Assigned owner
- Expected deliverable
- Status updates

---

## Branches

A branch is your personal workspace for a specific task.

Example:

```text
feature/release-note-command
```

When working on a major task, create a dedicated branch instead of editing the main branch directly.

Examples:

```text
feature/release-note-command
feature/release-note-review-skill
feature/agent-workflow-design
feature/demo-storyline
```

Benefits:

- Avoids overwriting other people's work
- Allows multiple team members to work simultaneously
- Makes review easier
- Keeps the main branch stable

---

## Pull Requests (PR)

When your work is ready:

1. Push your changes to your branch.
2. Create a Pull Request.
3. Request review if needed.
4. After approval, the changes will be merged into the main branch.

A Pull Request simply means:

"I have completed my work and would like it reviewed before it becomes part of the project."

---

## Example Workflow

```text
main
│
├── README.md
├── charter/
├── skills/
├── prompts-and-commands/
```

Create a branch:

```text
feature/release-note-command
```

Add your changes.

Submit a Pull Request:

```text
feature/release-note-command
↓
main
```

After approval:

```text
Changes become part of the official project.
```

---

## Simplified Approach for Workshop Participants

If you are new to GitHub:

You may contribute through:

- Issues
- Comments
- Documentation updates
- Meeting notes
- Research findings
- Sample data

>**NOTE** 
A technical team member can assist with branches and pull requests if needed.

---

## Recommended Contribution Model

### Use Branches For

- Commands
- Skills
- Agent workflows
- README updates
- Major project changes

### Direct Commits Are Acceptable For

- Meeting notes
- Sample data
- Research documents
- Validation notes
- Demo content

---

## Repository Rules

### Always Store Work in the Repository

Do:

- Commit prompts
- Commit skills
- Commit workflows
- Commit meeting notes
- Commit validation results

Do Not:

- Keep important work only in WhatsApp
- Keep important work only on your laptop
- Keep important work only in emails

---

## Owner Review

The Project Owner will periodically review:

- Repository structure
- Assigned work
- Documentation quality
- Open issues
- Progress toward milestones

---

## Guiding Principle

The goal is not simply to create files.

The goal is to make sure that any team member can understand the project, continue the work, and reproduce the proof-of-concept by using the repository alone.

The repository is our single source of truth.
