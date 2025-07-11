""" 
This file container code for To do List Manager application using OOP concepts
"""
def spacing():
    print("\n")
    print("-"*40)
    print("\n")
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title} | Status: {status} | Description: {self.description}"
    def mark_completed(self):
        self.completed = True
    def change_title(self, new_title):
        self.title = new_title

class TaskList:
    # tasks = list[Task]
    def __init__(self, owner):
        self.owner = owner
        # self.owner = ""
        self.tasks = []
    def add_task(self, task:Task):
         # Add a task to the list
        self.tasks.append(task)
    def remove_task(self,index):
        # Remove a task by its index (user sees 1-based index)
        # 
        if index >= 1 and index <= len(self.tasks):
            # removed = self.tasks.delete(index)
            # print(f"Removed: {removed.title}")
            print("index: ", index)
            print("len: ", len(self.tasks))
            print("self.tasks[index-1]: ", self.tasks[index-1])
            
            print(f"Removed: {self.tasks[index-1].title}")
            
            # delete the task
            # del self.tasks[index]
        else:
            print("Invalid index. Please try again.")
        
        # print("remove task")
    def view_tasks(self):
        # Show all tasks in the list
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your Current Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
                # print(f"{index + 1}. {task.title} | {task.description}")
        
    def list_options(self):
        while True: 
            print("To-Do List Manager") 
            print("1. Add a task") 
            print("2. View tasks") 
            print("3. Remove a task") 
            print("4. Mark as completed")
            print("5. Change title of task")
            print("6. Quit") 
             
            choice = input("Enter your choice: ") 
            print("\n")
             
            if choice == "1":
                task_title = input("Enter title of task: ")
                # self.add_task(task)
                task_description = input("Enter the description: ")
                task = Task(task_title, task_description)
                self.add_task(task)
                print(f"'{task_title}' has been added to your to-do list.\n")
                print("-"*40)

            elif choice == "2":
                self.view_tasks()
                spacing()

            elif choice == "3":
                self.view_tasks()
                if not self.tasks:
                    # print("There are no tasks to remove.\n")
                    spacing()
                    continue
                index = int(input("Enter the number of the task to remove: "))
                print("\n")
                
                print(f"'{task_title}' has been added to your to-do list.\n")
                
                self.remove_task(index)
                spacing()
            elif choice == "4":
                self.view_tasks()
                print("\n")
                if not self.tasks:
                    # print("There are no tasks available\n")
                    print("-"*40)
                    print("\n")
                    continue
                index = int(input("Enter the number of the task to mark as completed: "))
                self.tasks[index-1].mark_completed()
                spacing()
            elif choice == "5":
                self.view_tasks()
                print("\n")
                if not self.tasks:
                    # print("There are no tasks available\n")
                    spacing()
                    continue
                index = int(input("Enter the number of the task to change title: "))
                new_title = input("Enter the new title: ")
                self.tasks[index-1].change_title(new_title)
                spacing()
            elif choice == "6":
                print("Goodbye! Your to-do list has been closed.")
                spacing()
                # exit the loop and program
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.\n")

def main():
    print("="*40)   
    print("----Welcome to the To-Do List Manager----\n")
    
    name = input("Enter your name: ")
    
    task_list = TaskList(name)
    print("\n")
    task_list.list_options()
    
    
if __name__ == "__main__":
    main()