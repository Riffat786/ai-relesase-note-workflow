from automation.services.logger_service import (
    stage_header,
    section,
    bullet,
    success,
    blank,
)


def run():

    stage_header("Stage 5 - Draft Generator")

    section("Input:")

    bullet("release-notes.md")
    bullet("review-report.md")

    blank()

    section("Action:")

    bullet("Applying Document360 template")
    bullet("Populating release metadata")
    bullet("Setting article status to Draft")
    bullet("Preparing Technical Writer review package")

    blank()

    section("Output:")

    bullet("document360-draft.md")
    bullet("publication-checklist.md")

    blank()

    success("Draft Generator Stage Complete")

    blank()