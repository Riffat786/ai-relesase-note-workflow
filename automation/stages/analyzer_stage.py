from automation.services.logger_service import (
    stage_header,
    section,
    bullet,
    success,
    blank,
)


def run():

    stage_header("Stage 2 - Analyzer")

    section("Input:")

    bullet("collected-release-data-2025.8.json")

    blank()

    section("Action:")

    bullet("Classifying release items")
    bullet("Identifying customer-facing changes")
    bullet("Filtering internal work items")
    bullet("Preparing structured release data")

    blank()

    section("Output:")

    bullet("analyzed-release.json")

    blank()

    success("Analyzer Stage Complete")

    blank()