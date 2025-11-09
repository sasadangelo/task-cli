# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from .base import Command


class DeleteTaskCommand(Command):
    def execute(self, args):
        try:
            with open("tasks.txt") as f:
                tasks = [line.strip() for line in f]
        except FileNotFoundError:
            print("❌ No tasks found.")
            return
        if args.id < 1 or args.id > len(tasks):
            print(f"❌ Invalid task ID: {args.id}")
            return
        removed = tasks.pop(args.id - 1)
        with open("tasks.txt", "w") as f:
            f.write("\n".join(tasks) + "\n")
        print(f"🗑️  Task deleted: {removed}")
