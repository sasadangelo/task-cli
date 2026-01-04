# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import csv
import os

from .base import Command


class StatsCommand(Command):
    TASKS_FILE = "tasks.txt"

    def execute(self, subcommand: str, output: str):
        if subcommand == "summary":
            self._show_summary()
        elif subcommand == "export":
            self._export_to_csv(output)
        else:
            raise ValueError(f"Unknown subcommand: {subcommand}")

    def _load_tasks(self):
        if not os.path.exists(self.TASKS_FILE):
            return []
        with open(self.TASKS_FILE) as f:
            return [line.strip() for line in f if line.strip()]

    def _show_summary(self):
        tasks = self._load_tasks()
        print(f"📊 You have {len(tasks)} task(s).")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    def _export_to_csv(self, output_file: str):
        tasks = self._load_tasks()
        if not tasks:
            print("No tasks to export.")
            return

        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID", "Task"])
            for i, task in enumerate(tasks, 1):
                writer.writerow([i, task])

        print(f"✅ Tasks exported to {output_file}")
