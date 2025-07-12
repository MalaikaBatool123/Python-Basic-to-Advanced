""" 
this is main file for To do List Manager application using OOP concepts
this file will use codes of task and tasklist classes"""
from task_list import TaskList
from task import Task
import datetime
from recurring_task import RecurringTask
from TaskTestDAO import TaskTestDAO
from TaskCsvDAO import TaskCsvDAO
from TaskPickleDAO import TaskPickleDAO

# function to add spacing
def spacing():
    print("\n")
    print("-"*40)
    print("\n")

def get_task_details(task_list):
    task_title = input("Enter title of task: ")
    # task_list.add_task(task)
    task_description = input("Enter the description: ")
    
    while True :
        input_date = input("Enter a due date (YYYY-MM-DD): ")
        due_date = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
        # task = Task(task_title, task_description, due_date)
        # task_list.add_task(task)
        # print(f"'{task_title}' has been added to your to-do list.\n")
        break
    return task_title, task_description, due_date
def main() -> None:
    print("="*40)   
    print("----Welcome to the To-Do List Manager----\n")
    
    name = input("Enter your name: ")
    
    task_list = TaskList(name)
    # task1 = Task("Buy groceries", "Milk, Eggs, Bread", datetime.date.today())
    # task2 = Task("Submit assignment", "OOP Week 4", datetime.date.today() + datetime.timedelta(days=2))
    # task_list.add_task(task1)
    # task_list.add_task(task2)
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
        print("8. Change Due date of task")
        print("9. Load Tasks from CSV")
        print("10. Save Tasks to CSV")
        print("11. Load Data from Pickle File")
        print("12. Save Data to Pickle File")
        print("13. Quit") 
            
        choice = input("Enter your choice: ") 
        print("\n")
            
        if choice == "1":
            while True:
                print("1. One Time Task")
                print("2. Recurring Task")
                print("3. Back")
                
                sub_choice = input("Enter your choice: ")
                if sub_choice == "1":
                    task_title, task_description, due_date = get_task_details(task_list)
                    task = Task(task_title, task_description, due_date)
                    task_list.add_task(task)
                    print(f"'{task_title}' has been added to your to-do list.\n")
                    break
                elif sub_choice == "2":
                    task_title, task_description, due_date = get_task_details(task_list)
                    interval = input("Enter the interval in days: ")
                    interval = datetime.timedelta(days=int(interval))
                    task = RecurringTask(task_title, task_description, due_date, interval)
                    task_list.add_task(task)
                    print(f"'{task_title}' has been added to your to-do list.\n")
                    break
                elif sub_choice == "3":
                    break
            # get_task_details(task_list)
            # adding tasks
            # task_title = input("Enter title of task: ")
            # # task_list.add_task(task)
            # task_description = input("Enter the description: ")
            
            # while True :
            #     input_date = input("Enter a due date (YYYY-MM-DD): ")
            #     due_date = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
            #     task = Task(task_title, task_description, due_date)
            #     task_list.add_task(task)
            #     print(f"'{task_title}' has been added to your to-do list.\n")
            #     break
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
                        old_title = task_list.tasks[index-1].title
                        task_list.tasks[index-1].mark_completed()
                        dao = TaskCsvDAO("tasks.csv")
                        dao.update_task(task_list.tasks[index-1], old_title)
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
                        old_title = task_list.tasks[index-1].title
                        task_list.tasks[index-1].change_title(new_title)
                        print('tasking: ', task_list.tasks[index-1])
                        print('old task: ', old_title)
                        dao = TaskCsvDAO("tasks.csv")
                        dao.update_task(task_list.tasks[index-1], old_title)
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
                        old_title = task_list.tasks[index-1].title
                        task_list.tasks[index-1].change_description(new_desc)
                        dao = TaskCsvDAO("tasks.csv")
                        dao.update_task(task_list.tasks[index-1], old_title)
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
            # change due date oof task
            task_list.view_tasks()
            print("\n")
            while True:
                index = input("Enter the number of the task to change due date: ")

                if index.isdigit():
                    # Convert to actual integer
                    index = int(index)  
                    if index > 0 and index <= len(task_list.tasks) :
                        # get new due date
                        old_title = task_list.tasks[index-1].title
                        new_date = input("Enter the new due date (YYYY-MM-DD): ")
                        due_date = datetime.datetime.strptime(new_date, "%Y-%m-%d").date()
                        task_list.tasks[index-1].change_due_date(due_date)
                        dao = TaskCsvDAO("tasks.csv")
                        dao.update_task(task_list.tasks[index-1], old_title)
                        break  # Exit the loop since input is valid
                    else:
                        print("Invalid task number. Please try again.\n")
                        continue
                else:
                    print("Invalid input. Please enter a number like 1, 2, 3...")
        
        elif choice == "9":
            # load data from file
            
            # get path of file - input fro user
            path = input("Enter file path to load tasks e.g. tasks.txt: ")
            dao = TaskCsvDAO(path)
            # dao = TaskTestDAO(path)
            
            # Load tasks from DAO and add to task list
            loaded_tasks = dao.get_all_tasks()
            for task in loaded_tasks:
                task_list.add_task(task)
            print('loading data from file...')
            
        elif choice == "10":
            path = input("Enter file path to save tasks (e.g. tasks.txt): ")
    
            # Create DAO and pass current tasks to save (it won’t really save as method is empty)
            
            dao = TaskCsvDAO(path)
            # dao = TaskTestDAO(path)
            dao.save_all_tasks(task_list.tasks)
            print('saving data to file...')
        
        elif choice == "11":
            path = input("Enter pickle file path to load from (e.g. tasks.pkl): ")
           
            dao = TaskPickleDAO(path)
            tasks = dao.get_all_tasks()
            for task in tasks:
                task_list.add_task(task)
            print("[✓] Tasks loaded from pickle.")

        elif choice == "12":
            path = input("Enter pickle file path to save to (e.g. tasks.pkl): ")
            dao = TaskPickleDAO(path)
            dao.save_all_tasks(task_list.tasks)
        elif choice == "13":
            # quit
            print("Goodbye! Your to-do list has been closed.")
            spacing()
            # exit the loop and program
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
# due date and completed dates is remaining from week 5 and the tasks after it are also remaining