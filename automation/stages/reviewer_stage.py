from automation.services.logger_service import (
    stage_header,
    section,
    bullet,
    success,
    blank,
)


def run():

    stage_header("Stage 4 - Reviewer")

    section("Input:")

    bullet("release-notes.md")

    blank()

    section("Action:")

    bullet("Performing AI quality review")
    bullet("Checking customer-friendly language")
    bullet("Checking grammar and spelling")
    bullet("Validating Markdown formatting")
    bullet("Assessing consistency")
    bullet("Calculating quality score")

    blank()

    section("Output:")

    bullet("review-report.md")

    blank()

    success("Reviewer Stage Complete")

    blank()