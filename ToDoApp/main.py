""" 
this is main file for To do List Manager application using OOP concepts
this file will use codes of task and tasklist classes"""

from task_list import TaskList
from task import Task
import datetime

# function to add spacing
def spacing():
    print("\n")
    print("-"*40)
    print("\n")

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Adds some sample tasks to the task list for testing."""
    task_list.add_task(Task("Buy groceries", "Milk, eggs, and bread", datetime.datetime.now().date() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", "Wash and fold clothes", datetime.datetime.now().date() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", "Organize desk and vacuum floor", datetime.datetime.now().date() - datetime.timedelta(days=1)))
    task_list.add_task(Task("Do homework", "Finish math and science assignments", datetime.datetime.now().date() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", "Evening walk around the park", datetime.datetime.now().date() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", "Clean all utensils after dinner", datetime.datetime.now().date() + datetime.timedelta(days=6)))
    return task_list

def main() -> None:
    print("="*40)   
    print("----Welcome to the To-Do List Manager----\n")
    
    name = input("Enter your name: ")
    task_list = TaskList(name)
    
    # test tasks
    task1 = Task("Buy groceries", "Milk, Eggs, Bread", datetime.date.today())
    task2 = Task("Submit assignment", "OOP Week 4", datetime.date.today() + datetime.timedelta(days=2))
    # adding test Task Objects to list
    task_list.add_task(task1)
    task_list.add_task(task2)
    
    # for more test tasks
    task_list = propagate_task_list(task_list)

    
    print("\n")
    while True: 
        
        # menu
        print("To-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Remove a task") 
        print("4. Mark as completed")
        print("5. Change title of task")
        print("6. Change description of task")
        print("7. Show over due tasks")
        print("8. Quit") 
            
        choice = input("Enter your choice: ") 
        print("\n")
            
        if choice == "1":
            task_title = input("Enter title of task: ")
            task_description = input("Enter the description: ")
            
            # this loop is to ask the user to enter date until it is valid
            while True :
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                due_date = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
                task = Task(task_title, task_description, due_date)
                task_list.add_task(task)
                print(f"'{task_title}' has been added to your to-do list.\n")
                break
            print("-"*40)

        elif choice == "2":
            # view all tasks
            task_list.view_tasks()
            spacing()

        elif choice == "3":
            # removing tasks
            task_list.view_tasks()
            if not task_list.tasks:
                # print("There are no tasks to remove.\n")
                spacing()
                continue
            index = int(input("Enter the number of the task to remove: "))
            print("\n")
            task_list.remove_task(index)
            print("Your Remaining Tasks:\n")
            task_list.view_tasks()
            spacing()
        elif choice == "4":
            # mark as completed
            task_list.view_tasks()
            print("\n")
            if not task_list.tasks:
                # print("There are no tasks available\n")
                print("-"*40)
                print("\n")
                continue
            # check if index is valid
            while True:
                index = input("Enter the number of the task to mark as completed: ")

                if index.isdigit():
                    # Convert to actual integer
                    index = int(index)  
                    if index > 0 and index <= len(task_list.tasks) :
                        task_list.tasks[index-1].mark_completed()
                        break  # Exit the loop since input is valid
                    else:
                        print("Invalid task number. Please try again.\n")
                        continue
                        
                else:
                    print("Invalid input. Please enter a number like 1, 2, 3...")
            
            spacing()
        elif choice == "5":
            # change title
            task_list.view_tasks()
            print("\n")
            if not task_list.tasks:
                # print("There are no tasks available\n")
                spacing()
                continue
            while True:
                # user sees 1 based indexing
                index = input("Enter the number of the task to change title: ")

                if index.isdigit():
                    # Convert to actual integer
                    index = int(index)  
                    if index > 0 and index <= len(task_list.tasks) :
                        new_title = input("Enter the new title: ")
                        task_list.tasks[index-1].change_title(new_title)
                        break  # Exit the loop since input is valid
                    else:
                        print("Invalid task number. Please try again.\n")
                        continue
                        
                else:
                    print("Invalid input. Please enter a number like 1, 2, 3...")
            
            spacing()
        elif choice == "6":
            # change description
            task_list.view_tasks()
            print("\n")
            if not task_list.tasks:
                # print("There are no tasks available\n")
                spacing()
                continue
            while True:
                index = input("Enter the number of the task to change description: ")

                if index.isdigit():
                    # Convert to actual integer
                    index = int(index)  
                    if index > 0 and index <= len(task_list.tasks) :
                        new_desc = input("Enter the new description: ")
                        task_list.tasks[index-1].change_description(new_desc)
                        break  # Exit the loop since input is valid
                    else:
                        print("Invalid task number. Please try again.\n")
                        continue
                        
                else:
                    print("Invalid input. Please enter a number like 1, 2, 3...")
            spacing()
        elif choice == "7":
            # show over due tasks
            task_list.view_over_due_tasks()
        elif choice == "8":
            # quit
            print("Goodbye! Your to-do list has been closed.")
            spacing()
            # exit the loop and program
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

    
    
if __name__ == "__main__":
    main()