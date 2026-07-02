from automation.services.logger_service import (
    stage_header,
    section,
    bullet,
    success,
    blank,
)


def run():

    stage_header("Stage 1 - Collector")

    section("Input:")

    bullet("release-2025.8.json")
    bullet("service-now-2025.8.json")

    blank()

    section("Action:")

    bullet("Collecting release data")
    bullet("Merging Azure DevOps and ServiceNow information")
    bullet("Validating release structure")

    blank()

    section("Output:")

    bullet("collected-release-data-2025.8.json")

    blank()

    success("Collector Stage Complete")

    blank()