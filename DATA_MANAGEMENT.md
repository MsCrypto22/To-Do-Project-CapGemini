# Data Management Guide

This document explains the data management system for the To-Do project, including sample data, test data, and how to use them for demonstrations.

## 📁 Data Files Structure

```
data/
├── tasks_seed.json      # Seed data for initial state
├── test_data.json       # Test data with edge cases
└── sample_demo.json     # Demo data for presentations
```

## 🎯 Types of Data

### 1. Seed Data (`data/tasks_seed.json`)
- **Purpose**: Initial state for the application
- **Content**: 15 realistic tasks across various categories
- **Categories**: Personal, Work, Home, Exercise, Chores, Wellbeing, Health, Hobby, Finance
- **Use Case**: Starting fresh, resetting to known state

### 2. Test Data (`data/test_data.json`)
- **Purpose**: Comprehensive testing scenarios
- **Content**: 15 tasks with edge cases and special characters
- **Features**: 
  - Special characters (@#$%)
  - Long descriptions
  - Unicode characters (café, résumé)
  - Emojis (🎯)
  - Empty categories
  - Mixed case categories
- **Use Case**: Testing application robustness

### 3. Demo Data (`data/sample_demo.json`)
- **Purpose**: Presentation and demonstration
- **Content**: 15 tasks with status indicators
- **Features**: Shows completed vs pending tasks
- **Use Case**: Demonstrating workflow and progress tracking

## 🛠️ Data Management Commands

### Using the Data Management Script

```bash
# Reset to different data states
python data_management.py seed    # Reset to seed data
python data_management.py test    # Reset to test data
python data_management.py demo    # Reset to demo data

# View data information
python data_management.py info    # Show file statistics
python data_management.py sample  # Preview sample data

# Backup and restore
python data_management.py backup  # Create backup
python data_management.py backups # List available backups
python data_management.py restore <backup_file>  # Restore from backup
```

### Manual Data Operations

```bash
# Copy seed data to current tasks
cp data/tasks_seed.json tasks.json

# Copy test data to current tasks
cp data/test_data.json tasks.json

# Copy demo data to current tasks
cp data/sample_demo.json tasks.json
```

## 🧪 Testing with Sample Data

### Running Tests
```bash
# Run comprehensive test suite
python tests/test_todo.py

# Run individual test scenarios
python -c "
import tests.test_todo as test
test.reset_to_test_data()
test.test_add_with_special_characters()
"
```

### Test Scenarios Covered
- ✅ Basic CRUD operations (Create, Read, Update, Delete)
- ✅ Special character handling
- ✅ Long text input
- ✅ Case-insensitive category filtering
- ✅ Unicode support
- ✅ Error handling (non-existent tasks)
- ✅ ID auto-increment
- ✅ Multiple operations

## 📊 Sample Data Preview

### Seed Data Examples
```json
[
  {"id": 1, "description": "Buy groceries", "category": "Personal"},
  {"id": 2, "description": "Finish project report", "category": "Work"},
  {"id": 5, "description": "Go for a 3 mile run", "category": "Exercise"},
  {"id": 7, "description": "Eat fruit and veggies today", "category": "Wellbeing"}
]
```

### Test Data Examples
```json
[
  {"id": 1, "description": "Test task with special chars: @#$%", "category": "Test"},
  {"id": 9, "description": "Task with unicode: café résumé", "category": "Unicode"},
  {"id": 10, "description": "Task with emoji 🎯", "category": "Emoji"}
]
```

### Demo Data Examples
```json
[
  {"id": 1, "description": "Complete project presentation", "category": "Work", "status": "completed"},
  {"id": 2, "description": "Buy birthday gift for mom", "category": "Personal", "status": "pending"}
]
```

## 🎤 Presentation Tips

### For Demonstrations
1. **Start with seed data**: `python data_management.py seed`
2. **Show basic operations**: Add, list, remove tasks
3. **Demonstrate filtering**: `python app/todo.py list --category Work`
4. **Show test scenarios**: Switch to test data for edge cases
5. **Run tests**: Show comprehensive test coverage

### Key Points to Highlight
- **Data persistence**: Changes are saved to `tasks.json`
- **Category filtering**: Case-insensitive search
- **Error handling**: Graceful handling of invalid inputs
- **Data integrity**: Auto-incrementing IDs
- **Unicode support**: International character handling

### Sample Presentation Flow
```bash
# 1. Start fresh
python data_management.py seed

# 2. Show current state
python app/todo.py list

# 3. Add a new task
python app/todo.py add "Prepare presentation" "Work"

# 4. Show filtering
python app/todo.py list --category Work

# 5. Remove a task
python app/todo.py remove 1

# 6. Show test data capabilities
python data_management.py test
python app/todo.py list --category Unicode

# 7. Run tests
python tests/test_todo.py
```

## 🔧 Customization

### Adding New Sample Data
1. Create a new JSON file in the `data/` directory
2. Follow the format: `[{"id": 1, "description": "...", "category": "..."}]`
3. Add the file path to `data_management.py` if needed

### Modifying Existing Data
- Edit the JSON files directly
- Use the data management script to reset states
- Create backups before making changes

### Extending Test Coverage
- Add new test functions to `tests/test_todo.py`
- Include edge cases and error scenarios
- Test with different data sets

## 📈 Data Statistics

| Data Type | Tasks | Categories | Special Features |
|-----------|-------|------------|------------------|
| Seed Data | 15 | 9 | Realistic scenarios |
| Test Data | 15 | 10 | Edge cases, Unicode |
| Demo Data | 15 | 8 | Status indicators |

This comprehensive data management system ensures you have all the sample data and test scenarios needed for effective demonstrations and thorough testing of your To-Do application. 