#!/usr/bin/env python3
"""
Data Management Script for To-Do Project
Provides utilities for seeding data, resetting states, and managing data files
"""

import json
import shutil
import os
import argparse

# Data file paths
TASKS_FILE = 'tasks.json'
SEED_FILE = 'data/tasks_seed.json'
TEST_DATA_FILE = 'data/test_data.json'
DEMO_FILE = 'data/sample_demo.json'

def load_json_file(filepath):
    """Load JSON data from file"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in file: {filepath}")
        return None

def save_json_file(filepath, data):
    """Save JSON data to file"""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Data saved to: {filepath}")
    except Exception as e:
        print(f"❌ Error saving to {filepath}: {e}")

def reset_to_seed():
    """Reset tasks.json to seed data"""
    if os.path.exists(SEED_FILE):
        shutil.copy(SEED_FILE, TASKS_FILE)
        print("✅ Reset to seed data")
    else:
        print(f"❌ Seed file not found: {SEED_FILE}")

def reset_to_test_data():
    """Reset tasks.json to test data"""
    if os.path.exists(TEST_DATA_FILE):
        shutil.copy(TEST_DATA_FILE, TASKS_FILE)
        print("✅ Reset to test data")
    else:
        print(f"❌ Test data file not found: {TEST_DATA_FILE}")

def reset_to_demo_data():
    """Reset tasks.json to demo data"""
    if os.path.exists(DEMO_FILE):
        shutil.copy(DEMO_FILE, TASKS_FILE)
        print("✅ Reset to demo data")
    else:
        print(f"❌ Demo file not found: {DEMO_FILE}")

def show_data_info():
    """Show information about all data files"""
    print("📊 Data Files Information")
    print("=" * 50)
    
    files = [
        ("Current Tasks", TASKS_FILE),
        ("Seed Data", SEED_FILE),
        ("Test Data", TEST_DATA_FILE),
        ("Demo Data", DEMO_FILE)
    ]
    
    for name, filepath in files:
        if os.path.exists(filepath):
            data = load_json_file(filepath)
            if data:
                print(f"{name}: {len(data)} tasks")
                if len(data) > 0:
                    categories = set(task.get('category', 'Unknown') for task in data)
                    print(f"  Categories: {', '.join(sorted(categories))}")
        else:
            print(f"{name}: File not found")

def create_backup():
    """Create a backup of current tasks.json"""
    if os.path.exists(TASKS_FILE):
        backup_file = f"tasks_backup_{int(os.path.getmtime(TASKS_FILE))}.json"
        shutil.copy(TASKS_FILE, backup_file)
        print(f"✅ Backup created: {backup_file}")
    else:
        print("❌ No tasks.json file to backup")

def restore_backup(backup_file):
    """Restore from backup file"""
    if os.path.exists(backup_file):
        shutil.copy(backup_file, TASKS_FILE)
        print(f"✅ Restored from: {backup_file}")
    else:
        print(f"❌ Backup file not found: {backup_file}")

def list_backups():
    """List available backup files"""
    backups = [f for f in os.listdir('.') if f.startswith('tasks_backup_') and f.endswith('.json')]
    if backups:
        print("📁 Available backups:")
        for backup in sorted(backups):
            print(f"  {backup}")
    else:
        print("📁 No backup files found")

def show_sample_data():
    """Show sample data from each file"""
    print("📋 Sample Data Preview")
    print("=" * 50)
    
    files = [
        ("Seed Data", SEED_FILE),
        ("Test Data", TEST_DATA_FILE),
        ("Demo Data", DEMO_FILE)
    ]
    
    for name, filepath in files:
        print(f"\n{name}:")
        data = load_json_file(filepath)
        if data:
            for i, task in enumerate(data[:3]):  # Show first 3 tasks
                print(f"  {task['id']}: {task['description']} [{task['category']}]")
            if len(data) > 3:
                print(f"  ... and {len(data) - 3} more tasks")

def main():
    parser = argparse.ArgumentParser(description='Data Management for To-Do Project')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Reset commands
    subparsers.add_parser('seed', help='Reset to seed data')
    subparsers.add_parser('test', help='Reset to test data')
    subparsers.add_parser('demo', help='Reset to demo data')
    
    # Info commands
    subparsers.add_parser('info', help='Show data files information')
    subparsers.add_parser('sample', help='Show sample data from all files')
    
    # Backup commands
    subparsers.add_parser('backup', help='Create backup of current tasks')
    subparsers.add_parser('backups', help='List available backups')
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore from backup')
    restore_parser.add_argument('backup_file', help='Backup file to restore from')

    args = parser.parse_args()

    if args.command == 'seed':
        reset_to_seed()
    elif args.command == 'test':
        reset_to_test_data()
    elif args.command == 'demo':
        reset_to_demo_data()
    elif args.command == 'info':
        show_data_info()
    elif args.command == 'sample':
        show_sample_data()
    elif args.command == 'backup':
        create_backup()
    elif args.command == 'backups':
        list_backups()
    elif args.command == 'restore':
        restore_backup(args.backup_file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 