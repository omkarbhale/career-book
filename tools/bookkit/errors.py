"""Error collection for the build.

A build reports every problem it can find in one run, then fails if there were
any errors. ``BuildError`` is raised for problems that stop a single file from
being read at all.
"""

from __future__ import annotations

import sys


class BuildError(Exception):
    """A problem that makes one source file unusable."""


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def print(self, stream=sys.stderr) -> None:
        for w in self.warnings:
            print(f"warning: {w}", file=stream)
        for e in self.errors:
            print(f"error: {e}", file=stream)

    @property
    def ok(self) -> bool:
        return not self.errors
