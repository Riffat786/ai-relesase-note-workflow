# Quick Start — WealthWise Release Notes from Jira

Generate branded release notes and help topics automatically from your Jira KAN project.

---

## 1. Prerequisites (First Time Only)

### Connect Atlassian MCP

```bash
claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse
```

**When prompted:** Sign in with your Atlassian account that has access to https://twtaishubh.atlassian.net

**Do not:** Store API tokens, passwords, or credentials in any files. OAuth is managed by Claude Code.

### Verify Access

Check that you can access the KAN project:
- Go to https://twtaishubh.atlassian.net
- Verify you can see the KAN project
- Verify the project has at least one issue

---

## 2. Run the Pipeline

### Option A — Quick Command (Recommended)

In Claude Code, run:

```
/project:generate-release-notes
```

The pipeline runs to completion automatically without prompting for input.

### Option B — Manual Trigger

Copy the full prompt from `commands/release-note-generation-command.md` and paste it into Claude Code.

---

## 3. What Happens (3-5 minutes)

The orchestrator automatically:

1. ✅ Fetches all issues from KAN project (sorted by custom field cf[10019])
2. ✅ Classifies issues:
   - **What's New** — Story, Feature, New Feature
   - **Enhancements** — Task, Enhancement, Improvement, Sub-task
   - **Bug Fixes** — Bug
   - **Known Issues** — Any issue with label "known-issue"
3. ✅ Generates branded release notes (HTML + Markdown)
4. ✅ Generates help topics per What's New feature (HTML + Markdown)
5. ✅ Runs quality review:
   - Writing standards (second person, active voice, no internal IDs)
   - Structure compliance (matches benchmarks)
   - Branding rules (WealthWise colours, typography, tags)
   - Hyperlink integrity
6. ✅ Auto-fixes all High and Medium severity findings
7. ✅ Writes output files to `output/` directory

---

## 4. Review Output

```bash
# Output files are created here:
output/
├── release-note-[version]-whats-new.html      # Main release note (branded)
├── release-note-[version]-whats-new.md        # Markdown version
├── help-topic-[slug].html                     # Help topics (one per feature)
├── help-topic-[slug].md                       # Markdown help topics
└── release-note-review-report.md              # QA findings + auto-fix log
```

### Check Quality Report

```
output/release-note-review-report.md
```

Review any remaining Low severity findings. These are not auto-fixed (human judgment needed).

---

## 5. Approve and Publish

After reviewing:

1. ✅ Approve content in the HTML and Markdown files
2. ✅ Fix any remaining Low severity issues (edit directly or re-run pipeline)
3. ✅ Commit output files to git: `git add output/` and `git commit`
4. ✅ Publish to your documentation site

---

## Troubleshooting

### "Atlassian MCP not connected"

```bash
# Re-run the connection command
claude mcp add atlassian --transport sse https://mcp.atlassian.com/sse

# Then authenticate in the browser window that opens
```

### No issues fetched / Empty output

Check:
1. KAN project exists at https://twtaishubh.atlassian.net
2. KAN project has at least one issue
3. Your Atlassian OAuth token is valid (may have expired)
4. Your account has read access to the KAN project

### Help topic links broken

Re-run the pipeline. Links are auto-corrected after review.

### Output files not created

```bash
# Create the output directory
mkdir -p output

# Then re-run the pipeline
```

---

## Learn More

- **Architecture & MCP Integration:** `mcp-plugin-concept/integration-concept.md`
- **Orchestrator Details:** `agents/release-note-orchestrator.md`
- **WealthWise Branding Rules:** `skills/wealthwise-branding.md`
- **Writing Standards:** `skills/release-note-writer-skill.md`
- **Review Checklist:** `skills/release-note-reviewer-skill.md`

---

## Configuration

**Current Settings:**
- Jira Instance: https://twtaishubh.atlassian.net
- Project Key: KAN
- JQL: `project = KAN ORDER BY cf[10019] ASC`

To change these:
1. Edit `agents/release-note-orchestrator.md` — update `jira_board_url` and `jql` at the top
2. Edit `commands/release-note-generation-command.md` — update the data_source comment
3. Re-run the pipeline

---

## Questions?

See `CLAUDE.md` for full documentation and troubleshooting guide.
