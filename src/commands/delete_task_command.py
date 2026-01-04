# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from .base import Command


class DeleteTaskCommand(Command):
    def execute(self, task_id: int):
        try:
            with open("tasks.txt") as f:
                tasks = [line.strip() for line in f]
        except FileNotFoundError:
            print("❌ No tasks found.")
            return

        if task_id < 1 or task_id > len(tasks):
            print(f"❌ Invalid task ID: {task_id}")
            return

        removed = tasks.pop(task_id - 1)

        with open("tasks.txt", "w") as f:
            f.write("\n".join(tasks))

        print(f"🗑️  Task deleted: {removed}")
