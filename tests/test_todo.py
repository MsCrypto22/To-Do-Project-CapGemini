import subprocess
import json
import os
import shutil

TASKS_FILE = 'tasks.json'
SEED_FILE = 'data/tasks_seed.json'
TEST_DATA_FILE = 'data/test_data.json'

def reset_tasks():
    shutil.copy(SEED_FILE, TASKS_FILE)

def reset_to_test_data():
    shutil.copy(TEST_DATA_FILE, TASKS_FILE)

def run_cmd(args):
    return subprocess.run(['python', 'app/todo.py'] + args, capture_output=True, text=True)

def test_add():
    reset_tasks()
    result = run_cmd(['add', 'Test task', 'TestCat'])
    assert 'Added task' in result.stdout
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    assert any(t['description'] == 'Test task' and t['category'] == 'TestCat' for t in tasks)
    print('✓ test_add passed')

def test_remove():
    reset_tasks()
    result = run_cmd(['remove', '1'])
    assert 'Removed task' in result.stdout
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    assert not any(t['id'] == 1 for t in tasks)
    print('✓ test_remove passed')

def test_list():
    reset_tasks()
    result = run_cmd(['list'])
    assert 'Buy groceries' in result.stdout
    print('✓ test_list passed')

def test_list_category():
    reset_tasks()
    result = run_cmd(['list', '--category', 'Work'])
    assert 'Finish project report' in result.stdout
    assert 'Buy groceries' not in result.stdout
    print('✓ test_list_category passed')

def test_add_with_special_characters():
    reset_tasks()
    result = run_cmd(['add', 'Task with @#$% symbols', 'Special'])
    assert 'Added task' in result.stdout
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    assert any('@#$%' in t['description'] for t in tasks)
    print('✓ test_add_with_special_characters passed')

def test_add_with_long_description():
    reset_tasks()
    long_desc = "This is a very long task description that contains many words and should test how the application handles lengthy input text"
    result = run_cmd(['add', long_desc, 'LongText'])
    assert 'Added task' in result.stdout
    print('✓ test_add_with_long_description passed')

def test_remove_nonexistent_task():
    reset_tasks()
    result = run_cmd(['remove', '999'])
    assert 'not found' in result.stdout
    print('✓ test_remove_nonexistent_task passed')

def test_list_empty_category():
    reset_tasks()
    result = run_cmd(['list', '--category', 'NonexistentCategory'])
    assert 'No tasks found' in result.stdout
    print('✓ test_list_empty_category passed')

def test_case_insensitive_category_filter():
    reset_tasks()
    result = run_cmd(['list', '--category', 'work'])
    assert 'Finish project report' in result.stdout
    print('✓ test_case_insensitive_category_filter passed')

def test_multiple_adds():
    reset_tasks()
    run_cmd(['add', 'First task', 'Test'])
    run_cmd(['add', 'Second task', 'Test'])
    run_cmd(['add', 'Third task', 'Test'])
    
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    test_tasks = [t for t in tasks if t['category'] == 'Test']
    assert len(test_tasks) >= 3
    print('✓ test_multiple_adds passed')

def test_id_auto_increment():
    reset_tasks()
    with open(TASKS_FILE) as f:
        initial_tasks = json.load(f)
    max_id = max(t['id'] for t in initial_tasks)
    
    run_cmd(['add', 'New task', 'Test'])
    
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    new_task = next(t for t in tasks if t['description'] == 'New task')
    assert new_task['id'] == max_id + 1
    print('✓ test_id_auto_increment passed')

def test_with_test_data():
    reset_to_test_data()
    result = run_cmd(['list'])
    assert 'Test task with special chars' in result.stdout
    print('✓ test_with_test_data passed')

def test_unicode_support():
    reset_to_test_data()
    result = run_cmd(['list', '--category', 'Unicode'])
    assert 'café' in result.stdout
    print('✓ test_unicode_support passed')

if __name__ == '__main__':
    # Save a copy of the seed data for test resets
    if not os.path.exists(SEED_FILE):
        shutil.copy(TASKS_FILE, SEED_FILE)
    
    print("🧪 Running comprehensive test suite...")
    print("=" * 50)
    
    test_add()
    test_remove()
    test_list()
    test_list_category()
    test_add_with_special_characters()
    test_add_with_long_description()
    test_remove_nonexistent_task()
    test_list_empty_category()
    test_case_insensitive_category_filter()
    test_multiple_adds()
    test_id_auto_increment()
    test_with_test_data()
    test_unicode_support()
    
    print("=" * 50)
    print("🎉 All tests passed!") 