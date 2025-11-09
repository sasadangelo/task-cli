# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import argparse
from commands import AddTaskCommand, ListTaskCommand, DeleteTaskCommand, StatsCommand


class TaskCLI:
    def __init__(self):
        self.commands = {
            "add": AddTaskCommand(),
            "list": ListTaskCommand(),
            "delete": DeleteTaskCommand(),
            "stats": StatsCommand(),
        }

    def run(self):
        parser = argparse.ArgumentParser(description="Task Manager CLI")
        subparsers = parser.add_subparsers(dest="command", required=True)
        # add
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("--name", required=True, help="Task name")
        add_parser.set_defaults(func=self.commands["add"].execute)
        # list
        list_parser = subparsers.add_parser("list", help="List all tasks")
        list_parser.set_defaults(func=self.commands["list"].execute)
        # delete
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("--id", type=int, required=True, help="Task ID to delete")
        delete_parser.set_defaults(func=self.commands["delete"].execute)
        # stats command (with subcommands)
        stats_parser = subparsers.add_parser("stats", help="Show or export task statistics")
        stats_subparsers = stats_parser.add_subparsers(dest="subcommand", required=True)
        # stats summary
        summary_parser = stats_subparsers.add_parser("summary", help="Show a summary of tasks")
        summary_parser.set_defaults(subcommand="summary", func=self.commands["stats"].execute)
        # stats export
        export_parser = stats_subparsers.add_parser("export", help="Export tasks to CSV file")
        export_parser.add_argument("--output", default="tasks.csv", help="Output CSV file name")
        export_parser.set_defaults(subcommand="export", func=self.commands["stats"].execute)

        args = parser.parse_args()
        args.func(args)


if __name__ == "__main__":
    TaskCLI().run()
