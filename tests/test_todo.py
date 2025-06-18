import subprocess
import json
import os
import shutil

TASKS_FILE = 'tasks.json'
SEED_FILE = 'tasks_seed.json'

def reset_tasks():
    shutil.copy(SEED_FILE, TASKS_FILE)

def run_cmd(args):
    return subprocess.run(['python', 'todo.py'] + args, capture_output=True, text=True)

def test_add():
    reset_tasks()
    result = run_cmd(['add', 'Test task', 'TestCat'])
    assert 'Added task' in result.stdout
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    assert any(t['description'] == 'Test task' and t['category'] == 'TestCat' for t in tasks)
    print('test_add passed')

def test_remove():
    reset_tasks()
    result = run_cmd(['remove', '1'])
    assert 'Removed task' in result.stdout
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    assert not any(t['id'] == 1 for t in tasks)
    print('test_remove passed')

def test_list():
    reset_tasks()
    result = run_cmd(['list'])
    assert 'Buy groceries' in result.stdout
    print('test_list passed')

def test_list_category():
    reset_tasks()
    result = run_cmd(['list', '--category', 'Work'])
    assert 'Finish project report' in result.stdout
    assert 'Buy groceries' not in result.stdout
    print('test_list_category passed')

if __name__ == '__main__':
    # Save a copy of the seed data for test resets
    if not os.path.exists(SEED_FILE):
        shutil.copy(TASKS_FILE, SEED_FILE)
    test_add()
    test_remove()
    test_list()
    test_list_category()
    print('All tests passed!') 