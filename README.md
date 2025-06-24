# Simple To-Do List App

## Approach & Design
- Command-line Python app for managing tasks.
- Tasks are stored in a local JSON file (`tasks.json`).
- Each task has an ID, description, and category.
- Supports adding, removing, and listing tasks, with optional category filtering.

## Project Structure
```
To-Do-Project-CapGemini/
│
├── app/                  # Application source code
│   └── todo.py
│
├── data/                 # Data and sample files
│   ├── tasks_seed.json   # Seed data for initial state
│   ├── test_data.json    # Test data with edge cases
│   └── sample_demo.json  # Demo data for presentations
│
├── tests/                # Test scripts
│   └── test_todo.py
│
├── data_management.py    # Data management utilities
├── demo.py              # Interactive demonstration script
├── DATA_MANAGEMENT.md   # Comprehensive data guide
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

## Sample Data & Testing

### Quick Start with Sample Data
```bash
# Reset to seed data (15 realistic tasks)
python data_management.py seed

# View current tasks
python app/todo.py list

# Run comprehensive tests
python tests/test_todo.py
```

### Available Sample Data
- **Seed Data**: 15 realistic tasks across 9 categories (Personal, Work, Home, Exercise, etc.)
- **Test Data**: 15 tasks with edge cases (special characters, unicode, long text, etc.)
- **Demo Data**: 15 tasks with status indicators for presentations

### Data Management Commands
```bash
# Reset to different data states
python data_management.py seed    # Reset to seed data
python data_management.py test    # Reset to test data  
python data_management.py demo    # Reset to demo data

# View data information
python data_management.py info    # Show file statistics
python data_management.py sample  # Preview sample data
```

### Interactive Demonstration
```bash
# Run interactive demo script
python demo.py
```
This provides guided demonstrations of all features including:
- Basic CRUD operations
- Data management
- Testing capabilities
- Edge case handling
- Complete presentation flow

## How to Test
- Run comprehensive tests: `python tests/test_todo.py`
- Tests cover:
  - ✅ Basic CRUD operations (Create, Read, Update, Delete)
  - ✅ Special character handling
  - ✅ Long text input
  - ✅ Case-insensitive category filtering
  - ✅ Unicode support
  - ✅ Error handling (non-existent tasks)
  - ✅ ID auto-increment
  - ✅ Multiple operations

## How to Verify
- Check the output of the commands above.
- Inspect `tasks.json` to see the current tasks.
- Use `python data_management.py info` to see data statistics.

## Sample Data Examples

### Seed Data
```json
[
  {"id": 1, "description": "Buy groceries", "category": "Personal"},
  {"id": 2, "description": "Finish project report", "category": "Work"},
  {"id": 5, "description": "Go for a 3 mile run", "category": "Exercise"}
]
```

### Test Data
```json
[
  {"id": 1, "description": "Test task with special chars: @#$%", "category": "Test"},
  {"id": 9, "description": "Task with unicode: café résumé", "category": "Unicode"},
  {"id": 10, "description": "Task with emoji 🎯", "category": "Emoji"}
]
```

## Presentation Tips
1. **Start with seed data**: `python data_management.py seed`
2. **Show basic operations**: Add, list, remove tasks
3. **Demonstrate filtering**: `python app/todo.py list --category Work`
4. **Show test scenarios**: Switch to test data for edge cases
5. **Run tests**: Show comprehensive test coverage
6. PowerPoint Presentation has been made as well

For detailed information about data management, see [DATA_MANAGEMENT.md](DATA_MANAGEMENT.md). 
