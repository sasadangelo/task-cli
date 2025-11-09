# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from abc import ABC, abstractmethod


class Command(ABC):
    """Base class for all CLI commands."""

    @abstractmethod
    def execute(self, args):
        pass
