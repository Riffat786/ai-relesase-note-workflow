#!/usr/bin/env python3

"""
Logger Service

Provides consistent console output across all
pipeline stages.
"""

def line():
    print("=" * 60)


def stage_header(stage_name):
    line()
    print(f" {stage_name}")
    line()
    print()


def section(title):
    print(title)


def bullet(text):
    print(f"  • {text}")


def success(message):
    print(f"✓ {message}")


def error(message):
    print(f"✗ {message}")


def blank():
    print()