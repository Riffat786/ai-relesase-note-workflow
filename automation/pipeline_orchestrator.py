#!/usr/bin/env python3

from automation.stages.collector_stage import run as collector
from automation.stages.analyzer_stage import run as analyzer
from automation.stages.writer_stage import run as writer
from automation.stages.reviewer_stage import run as reviewer
from automation.stages.draft_generator_stage import run as draft

print("=" * 60)
print("AI Release Note Pipeline")
print("Master Orchestrator")
print("=" * 60)
print()

collector()
analyzer()
writer()
reviewer()
draft()

print("=" * 60)
print("Pipeline Complete")
print("=" * 60)