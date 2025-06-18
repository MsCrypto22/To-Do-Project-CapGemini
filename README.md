# Simple To-Do List App

## Approach & Design
- Command-line Python app for managing tasks.
- Tasks are stored in a local JSON file (`data/tasks.json`).
- Each task has an ID, description, and category.
- Supports adding, removing, and listing tasks, with optional category filtering.

## Project Structure
```
To-Do-Project-CapGemini/
│
├── app/                  # Application source code
│   └── todo.py
│
├── data/                 # Data and seed files
│   ├── tasks.json
│   └── tasks_seed.json
│
├── tests/                # Test scripts
│   └── test_todo.py
│
├── README.md
└── LICENSE
```

## How to Run
1. Make sure you have Python 3 installed.
2. Install requirements (none needed for standard Python 3).
3. Run the app:
   - Add a task: `python app/todo.py add "Task description" "Category"`
   - Remove a task: `python app/todo.py remove <task_id>`
   - List all tasks: `python app/todo.py list`
   - List tasks by category: `python app/todo.py list --category "Category"`

## How to Test
- Run: `python tests/test_todo.py`
- This will check add, remove, and list functionality.

## How to Verify
- Check the output of the commands above.
- Inspect `data/tasks.json` to see the current tasks.

## Seed Data
- `data/tasks.json` includes a few example tasks in different categories. 