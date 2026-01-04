# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import click

from commands import (
    AddTaskCommand,
    DeleteTaskCommand,
    ListTaskCommand,
    StatsCommand,
)


@click.group(help="Task Manager CLI")
def cli():
    pass


@cli.command(help="Add a new task")
@click.option("--name", "-n", required=True, help="Task name")
def add(name):
    AddTaskCommand().execute(name=name)


@cli.command(help="List all tasks")
def list():
    ListTaskCommand().execute()


@cli.command(help="Delete a task")
@click.option("--id", "-i", "task_id", required=True, type=int, help="Task ID to delete")
def delete(task_id):
    DeleteTaskCommand().execute(task_id=task_id)


@cli.group(help="Show or export task statistics")
def stats():
    pass


@stats.command(help="Show a summary of tasks")
def summary():
    StatsCommand().summary()


@stats.command(help="Export tasks to CSV file")
@click.option("--output", "-o", default="tasks.csv", help="Output CSV file name")
def export(output):
    StatsCommand().export(output=output)


if __name__ == "__main__":
    cli()
