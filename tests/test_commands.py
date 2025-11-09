# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import os
import unittest
from commands.add_task_command import AddTaskCommand
from commands.list_task_command import ListTaskCommand
from commands.delete_task_command import DeleteTaskCommand


class TestTaskCommands(unittest.TestCase):
    TEST_FILE = "test_tasks.txt"

    def setUp(self):
        """Prepare a clean test environment before each test."""
        # Ensure we use a test-specific file
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)
        open(self.TEST_FILE, "w").close()

        # Patch the file used by commands
        self.add_command = AddTaskCommand()
        self.list_command = ListTaskCommand()
        self.delete_command = DeleteTaskCommand()

        # Monkey patch: redirect file operations to TEST_FILE
        self._patch_files()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def _patch_files(self):
        """Replace hardcoded 'tasks.txt' with 'test_tasks.txt'."""
        for cmd in [self.add_command, self.list_command, self.delete_command]:
            if hasattr(cmd, "FILE_PATH"):
                cmd.FILE_PATH = self.TEST_FILE
            else:
                cmd.FILE_PATH = self.TEST_FILE  # Add dynamic property

    def test_add_task(self):
        """Should append a task to the file."""
        args = type("Args", (), {"name": "Buy milk"})
        self.add_command.execute(args)

        with open(self.TEST_FILE) as f:
            tasks = [line.strip() for line in f.readlines()]

        self.assertIn("Buy milk", tasks)
        self.assertEqual(len(tasks), 1)

    def test_list_tasks(self):
        """Should list tasks without error."""
        # Add two tasks
        with open(self.TEST_FILE, "w") as f:
            f.write("Task 1\nTask 2\n")

        args = type("Args", (), {})()
        # We just verify that the command runs without exception
        try:
            self.list_command.execute(args)
        except Exception as e:
            self.fail(f"ListTaskCommand raised an exception: {e}")

    def test_delete_task(self):
        """Should delete the specified task."""
        with open(self.TEST_FILE, "w") as f:
            f.write("Task 1\nTask 2\nTask 3\n")

        args = type("Args", (), {"id": 2})
        self.delete_command.execute(args)

        with open(self.TEST_FILE) as f:
            tasks = [line.strip() for line in f.readlines()]

        self.assertEqual(len(tasks), 2)
        self.assertNotIn("Task 2", tasks)


if __name__ == "__main__":
    unittest.main()
