# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
# python3 -m pytest -v test/test_suite.py
# -----------------------------------------------------------------------------

import csv
import os
import unittest

from commands import AddTaskCommand, DeleteTaskCommand, ListTaskCommand, StatsCommand


class TestTaskCommands(unittest.TestCase):
    TASKS_FILE = "tasks.txt"
    CSV_FILE = "tasks.csv"

    def setUp(self):
        """Prepare a clean test environment before each test."""
        for f in [self.TASKS_FILE, self.CSV_FILE]:
            if os.path.exists(f):
                os.remove(f)
        open(self.TASKS_FILE, "w").close()

        # Initialize commands
        self.add_command = AddTaskCommand()
        self.list_command = ListTaskCommand()
        self.delete_command = DeleteTaskCommand()
        self.stats_command = StatsCommand()

    def tearDown(self):
        """Clean up after tests."""
        for f in [self.TASKS_FILE, self.CSV_FILE]:
            if os.path.exists(f):
                os.remove(f)

    def test_add_task(self):
        """Should append a task to the file."""
        self.add_command.execute(name="Buy milk")

        with open(self.TASKS_FILE) as f:
            tasks = [line.strip() for line in f.readlines()]

        self.assertIn("Buy milk", tasks)
        self.assertEqual(len(tasks), 1)

    def test_list_tasks(self):
        """Should list tasks without error."""
        with open(self.TASKS_FILE, "w") as f:
            f.write("Task 1\nTask 2\n")

        try:
            self.list_command.execute()
        except Exception as e:
            self.fail(f"ListTaskCommand raised an exception: {e}")

    def test_delete_task(self):
        """Should delete the specified task."""
        with open(self.TASKS_FILE, "w") as f:
            f.write("Task 1\nTask 2\nTask 3\n")

        self.delete_command.execute(task_id=2)

        with open(self.TASKS_FILE) as f:
            tasks = [line.strip() for line in f.readlines()]

        self.assertEqual(len(tasks), 2)
        self.assertNotIn("Task 2", tasks)

    def test_stats_summary(self):
        """Should display a summary of tasks."""
        with open(self.TASKS_FILE, "w") as f:
            f.write("Task 1\nTask 2\n")

        try:
            self.stats_command.summary()
        except Exception as e:
            self.fail(f"StatsCommand.summary() raised an exception: {e}")

    def test_stats_export(self):
        """Should export tasks to a CSV file."""
        with open(self.TASKS_FILE, "w") as f:
            f.write("Task 1\nTask 2\n")

        self.stats_command.export(self.CSV_FILE)

        self.assertTrue(os.path.exists(self.CSV_FILE))

        with open(self.CSV_FILE, newline="") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        # Validate CSV structure and content
        self.assertEqual(rows[0], ["ID", "Task"])
        self.assertEqual(rows[1][1], "Task 1")
        self.assertEqual(rows[2][1], "Task 2")
        self.assertEqual(len(rows), 3)
