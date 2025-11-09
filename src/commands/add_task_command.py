# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from .base import Command


class AddTaskCommand(Command):
    def execute(self, args):
        with open("tasks.txt", "a") as f:
            f.write(args.name + "\n")
        print(f"✅ Task added: {args.name}")
