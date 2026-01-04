# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from .base import Command


class ListTaskCommand(Command):
    def execute(self):
        try:
            with open("tasks.txt") as f:
                tasks = [line.strip() for line in f]
        except FileNotFoundError:
            tasks = []

        if not tasks:
            print("🗒️  No tasks found.")
            return

        print("📋 Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
