# Simple To-Do List App

## Approach & Design
- Command-line Python app for managing tasks.
- Tasks are stored in a local JSON file (`tasks.json`).
- Each task has an ID, description, and category.
- Supports adding, removing, and listing tasks, with optional category filtering.

## Key Files & Folders
- `todo.py`: Main application logic and CLI.
- `tasks.json`: Data file for tasks (with seed data).
- `test_todo.py`: Simple tests for core functions.

## How to Run
1. Make sure you have Python 3 installed.
2. Install requirements (none needed for standard Python 3).
3. Run the app:
   - Add a task: `python todo.py add "Task description" "Category"`
   - Remove a task: `python todo.py remove <task_id>`
   - List all tasks: `python todo.py list`
   - List tasks by category: `python todo.py list --category "Category"`

## How to Test
- Run: `python test_todo.py`
- This will check add, remove, and list functionality.

## How to Verify
- Check the output of the commands above.
- Inspect `tasks.json` to see the current tasks.

## Seed Data
- `tasks.json` includes a few example tasks in different categories. 