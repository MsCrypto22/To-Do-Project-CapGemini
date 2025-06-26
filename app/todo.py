import argparse
import json
import os
import sys

TASKS_FILE = 'tasks.json'
CONFIG_FILE = 'config.json'

def load_config():
    """Load configuration from config.json"""
    if not os.path.exists(CONFIG_FILE):
        return {
            'tasks_file': 'tasks.json',
            'default_categories': ['Personal', 'Work', 'Home', 'Exercise'],
            'auto_backup': True,
            'backup_count': 5
        }
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    """Save configuration to config.json"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def get_tasks_file():
    """Get the tasks file path from configuration"""
    config = load_config()
    return config.get('tasks_file', TASKS_FILE)

def load_tasks():
    tasks_file = get_tasks_file()
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    tasks_file = get_tasks_file()
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description, category):
    tasks = load_tasks()
    task_id = max([t['id'] for t in tasks], default=0) + 1
    task = {'id': task_id, 'description': description, 'category': category}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task {task_id}: {description} [{category}]")

def remove_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(new_tasks)
        print(f"Removed task {task_id}.")

def list_tasks(category=None):
    tasks = load_tasks()
    if category:
        tasks = [t for t in tasks if t['category'].lower() == category.lower()]
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"{t['id']}: {t['description']} [{t['category']}]" )

def configure_app(setting=None, value=None):
    """Configure application settings"""
    config = load_config()
    
    if setting is None:
        # Show current configuration
        print("Current Configuration:")
        print(f"  Tasks file: {config.get('tasks_file', 'tasks.json')}")
        print(f"  Default categories: {', '.join(config.get('default_categories', []))}")
        print(f"  Auto backup: {config.get('auto_backup', True)}")
        print(f"  Backup count: {config.get('backup_count', 5)}")
        return
    
    if value is None:
        print(f"Error: Value required for setting '{setting}'")
        return
    
    # Update configuration based on setting
    if setting == 'tasks_file':
        config['tasks_file'] = value
        print(f"Tasks file set to: {value}")
    elif setting == 'default_categories':
        categories = [cat.strip() for cat in value.split(',')]
        config['default_categories'] = categories
        print(f"Default categories set to: {categories}")
    elif setting == 'auto_backup':
        if value.lower() in ['true', 'yes', '1']:
            config['auto_backup'] = True
            print("Auto backup enabled")
        elif value.lower() in ['false', 'no', '0']:
            config['auto_backup'] = False
            print("Auto backup disabled")
        else:
            print("Error: auto_backup must be true/false, yes/no, or 1/0")
            return
    elif setting == 'backup_count':
        try:
            count = int(value)
            if count < 0:
                print("Error: backup_count must be a positive number")
                return
            config['backup_count'] = count
            print(f"Backup count set to: {count}")
        except ValueError:
            print("Error: backup_count must be a number")
            return
    else:
        print(f"Error: Unknown setting '{setting}'")
        print("Available settings: tasks_file, default_categories, auto_backup, backup_count")
        return
    
    save_config(config)
    print("Configuration saved successfully!")

def renumber_tasks():
    """Renumber all tasks to have sequential IDs starting from 1"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to renumber.")
        return
    
    # Sort tasks by current ID to maintain order
    tasks.sort(key=lambda x: x['id'])
    
    # Renumber tasks sequentially
    for i, task in enumerate(tasks, 1):
        task['id'] = i
    
    save_tasks(tasks)
    print(f"Renumbered {len(tasks)} tasks with sequential IDs (1-{len(tasks)})")

def main():
    parser = argparse.ArgumentParser(description='Simple To-Do List App')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Task description')
    add_parser.add_argument('category', type=str, help='Task category')

    remove_parser = subparsers.add_parser('remove', help='Remove a task by ID')
    remove_parser.add_argument('id', type=int, help='Task ID to remove')

    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.add_argument('--category', type=str, help='Filter by category', default=None)

    renumber_parser = subparsers.add_parser('renumber', help='Renumber all tasks sequentially')

    configure_parser = subparsers.add_parser('configure', help='Configure application settings')
    configure_parser.add_argument('--setting', type=str, help='Configuration setting to modify')
    configure_parser.add_argument('--value', type=str, help='Value for the setting')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description, args.category)
    elif args.command == 'remove':
        remove_task(args.id)
    elif args.command == 'list':
        list_tasks(args.category)
    elif args.command == 'renumber':
        renumber_tasks()
    elif args.command == 'configure':
        configure_app(args.setting, args.value)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 