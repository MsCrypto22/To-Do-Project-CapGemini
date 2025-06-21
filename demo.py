#!/usr/bin/env python3
"""
Demonstration Script for To-Do Project
Shows all sample data and features for presentation purposes
"""

import subprocess
import time
import os

def run_cmd(args, show_output=True):
    """Run a command and optionally show output"""
    result = subprocess.run(['python', 'app/todo.py'] + args, capture_output=True, text=True)
    if show_output:
        print(result.stdout)
    return result

def run_data_cmd(args, show_output=True):
    """Run a data management command"""
    result = subprocess.run(['python', 'data_management.py'] + args, capture_output=True, text=True)
    if show_output:
        print(result.stdout)
    return result

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🎯 {title}")
    print("=" * 60)

def print_step(step_num, description):
    """Print a formatted step"""
    print(f"\n📋 Step {step_num}: {description}")
    print("-" * 40)

def demo_basic_operations():
    """Demonstrate basic CRUD operations"""
    print_header("Basic Operations Demo")
    
    print_step(1, "Show current tasks")
    run_cmd(['list'])
    
    print_step(2, "Add a new task")
    run_cmd(['add', 'Prepare presentation slides', 'Work'])
    
    print_step(3, "Show updated task list")
    run_cmd(['list'])
    
    print_step(4, "Filter tasks by category")
    run_cmd(['list', '--category', 'Work'])
    
    print_step(5, "Remove a task")
    run_cmd(['remove', '1'])
    
    print_step(6, "Show final task list")
    run_cmd(['list'])

def demo_data_management():
    """Demonstrate data management features"""
    print_header("Data Management Demo")
    
    print_step(1, "Show data files information")
    run_data_cmd(['info'])
    
    print_step(2, "Preview sample data")
    run_data_cmd(['sample'])
    
    print_step(3, "Switch to test data")
    run_data_cmd(['test'])
    
    print_step(4, "Show test data tasks")
    run_cmd(['list'])
    
    print_step(5, "Show special characters in test data")
    run_cmd(['list', '--category', 'Test'])
    
    print_step(6, "Show unicode support")
    run_cmd(['list', '--category', 'Unicode'])
    
    print_step(7, "Switch to demo data")
    run_data_cmd(['demo'])
    
    print_step(8, "Show demo data")
    run_cmd(['list'])

def demo_testing():
    """Demonstrate testing capabilities"""
    print_header("Testing Demo")
    
    print_step(1, "Reset to seed data for testing")
    run_data_cmd(['seed'])
    
    print_step(2, "Run comprehensive test suite")
    result = subprocess.run(['python', 'tests/test_todo.py'], capture_output=True, text=True)
    print(result.stdout)

def demo_edge_cases():
    """Demonstrate edge case handling"""
    print_header("Edge Cases Demo")
    
    print_step(1, "Add task with special characters")
    run_cmd(['add', 'Task with @#$% symbols!', 'Special'])
    
    print_step(2, "Add task with very long description")
    long_desc = "This is a very long task description that contains many words and should test how the application handles lengthy input text without breaking"
    run_cmd(['add', long_desc, 'LongText'])
    
    print_step(3, "Add task with unicode characters")
    run_cmd(['add', 'Task with café and résumé', 'Unicode'])
    
    print_step(4, "Try to remove non-existent task")
    run_cmd(['remove', '999'])
    
    print_step(5, "Filter by non-existent category")
    run_cmd(['list', '--category', 'NonExistentCategory'])
    
    print_step(6, "Show all tasks including edge cases")
    run_cmd(['list'])

def demo_presentation_flow():
    """Demonstrate a complete presentation flow"""
    print_header("Complete Presentation Flow")
    
    print_step(1, "Start fresh with seed data")
    run_data_cmd(['seed'])
    
    print_step(2, "Show initial state")
    run_cmd(['list'])
    
    print_step(3, "Add multiple tasks")
    run_cmd(['add', 'Complete project documentation', 'Work'])
    run_cmd(['add', 'Go to the gym', 'Exercise'])
    run_cmd(['add', 'Buy groceries', 'Personal'])
    
    print_step(4, "Show all tasks")
    run_cmd(['list'])
    
    print_step(5, "Filter by different categories")
    print("Work tasks:")
    run_cmd(['list', '--category', 'Work'])
    print("\nExercise tasks:")
    run_cmd(['list', '--category', 'Exercise'])
    print("\nPersonal tasks:")
    run_cmd(['list', '--category', 'Personal'])
    
    print_step(6, "Remove a task")
    run_cmd(['remove', '1'])
    
    print_step(7, "Show final state")
    run_cmd(['list'])
    
    print_step(8, "Run tests to show reliability")
    result = subprocess.run(['python', 'tests/test_todo.py'], capture_output=True, text=True)
    print("✅ All tests passed!")

def main():
    """Main demonstration function"""
    print("🚀 To-Do Project Demonstration")
    print("This script showcases all features and sample data")
    
    while True:
        print("\n" + "=" * 60)
        print("Choose a demonstration:")
        print("1. Basic Operations (CRUD)")
        print("2. Data Management")
        print("3. Testing Capabilities")
        print("4. Edge Cases")
        print("5. Complete Presentation Flow")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            demo_basic_operations()
        elif choice == '2':
            demo_data_management()
        elif choice == '3':
            demo_testing()
        elif choice == '4':
            demo_edge_cases()
        elif choice == '5':
            demo_presentation_flow()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-6.")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main() 