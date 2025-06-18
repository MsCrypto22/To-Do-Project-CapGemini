import argparse
import json
import os
import sys

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
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

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description, args.category)
    elif args.command == 'remove':
        remove_task(args.id)
    elif args.command == 'list':
        list_tasks(args.category)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 