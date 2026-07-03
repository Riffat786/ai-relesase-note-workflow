from automation.services.logger_service import (
    stage_header,
    section,
    bullet,
    success,
    blank,
)


def run():

    stage_header("Stage 3 - Writer")

    section("Input:")

    bullet("analyzed-release.json")

    blank()

    section("Action:")

    bullet("Applying release note template")
    bullet("Generating customer-friendly language")
    bullet("Preserving work item traceability")
    bullet("Formatting Markdown output")

    blank()

    section("Output:")

    bullet("release-notes.md")

    blank()

    success("Writer Stage Complete")

    blank()