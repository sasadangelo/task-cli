# 🧰 Task CLI

A simple Python command-line tool to manage personal tasks — built with modern tooling (`uv`) and a clean `src/` structure.
It demonstrates how to organize a CLI project, structure commands, and run tests using `unittest`. To setup the Python development environment this project uses the [Python Blueprint](https://github.com/sasadangelo/python-blueprint).

---

## ⚙️ Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-org/task-cli.git
cd task-cli
```

### 2️⃣ Install Python 3.14

Install Python 3.14 via uv:

```bash
uv python install 3.14
uv python pin 3.14
```

Check that it's active:

```bash
uv run python --version
```

### 3️⃣ Sync dependencies

```bash
uv sync
```

This command automatically:

* creates and activates a virtual environment (.venv/)
* installs dependencies from pyproject.toml
* uses the pinned Python 3.14 version

## 🚀 Usage

Run all CLI commands using uv run (no need to manually activate the virtualenv).

```bash
uv run python -m src.cli add --name "Buy milk"
```

Output:

✅ Task added: Buy milk

📋 List tasks

```bash
uv run python -m src.cli list
```

Output:

📋 Tasks:
1. Buy milk

🗑️ Delete a task

```bash
uv run python -m src.cli delete --id 1
```

Output:

🗑️  Task deleted: Buy milk

### 🧾 Where data is stored

Tasks are stored in a plain text file tasks.txt located at the project root:

```
task-cli/
├── src/
│   └── cli.py
└── tasks.txt   👈 list of all tasks
```

## 🧪 Running tests

All tests are under the tests/ folder and use Python’s built-in unittest framework.

Run them with:

```bash
uv run python -m unittest discover -s tests -v
```

or just:

```bash
uv run python -m unittest tests.test_commands -v
```

## 📁 Project structure

```
task-cli/
│
├── src/
│   ├── cli.py
│   └── commands/
│       ├── __init__.py
│       ├── base.py
│       ├── add_task_command.py
│       ├── list_task_command.py
│       └── delete_task_command.py
│
├── tests/
│   └── test_commands.py
│
├── pyproject.toml
└── tasks.txt
```

## 💡 Notes

The environment variable PYTHONPATH=src/ ensures that imports like
from src.commands import AddTaskCommand work correctly.

The CLI is structured to be easily extensible: just add new commands in src/commands/.

## 🏁 License

MIT © Salvatore D'Angelo

