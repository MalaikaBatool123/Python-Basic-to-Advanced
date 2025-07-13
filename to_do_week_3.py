
""" 
This file container code for 
To do List Manager application from the Week 3 Lab
"""

print("="*40)

# Step 1: Initialize an empty list to store tasks
tasks = []

# Step 2: Function to add a task
def add_task():
    task = input("Enter the task you want to add: ")
    # add the task to the list
    tasks.append(task)  
    print(f"'{task}' has been added to your to-do list.\n")

# Step 3: Function to view current tasks
def view_tasks():
    if not tasks:
        print("Your to-do list is empty.\n")
    else:
        print("\nHere are your current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()  # just a blank line for spacing

# Step 4: Function to remove a task
def remove_task():
    if not tasks:
        print("There are no tasks to remove.\n")
        return

    # Show current tasks so user knows the numbers
    view_tasks()  

    try:
        task_number = int(input("Enter the number of the task you want to remove: "))
        if 1 <= task_number <= len(tasks):
            # remove the selected task
            removed = tasks.pop(task_number - 1)  
            print(f"'{removed}' has been removed from your to-do list.\n")
        else:
            print("Invalid task number. Please try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Step 5: Main program loop
while True:
    print("📋 To-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit\n")

    choice = input("Enter your choice (1-4): ")

    # Handle each menu option
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Your to-do list has been closed.")
        # exit the loop and program
        break  
    else:
        print("Invalid choice. Please enter a number between 1 and 4.\n")

print("="*40)