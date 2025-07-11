import datetime
from task import Task


class TaskList:
    # tasks = list[Task]
    def __init__(self, owner) -> None:
        self.owner = owner
        # self.owner = ""
        self.tasks = []
    def add_task(self, task:Task) -> None:
         # Add a task to the list
        self.tasks.append(task)
    def remove_task(self,index) -> None:
        # not done yet
        # Remove a task by its index (user sees 1-based index)
        
        if index >= 1 and index <= len(self.tasks):
            
            print(f"Removed: {self.tasks[index-1].title}")
            
            # delete the task
            del self.tasks[index-1]
            
        else:
            print("Invalid index. Please try again.")
        
        # print("remove task")
    def view_tasks(self) -> None:
        # Show all tasks in the list
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your Current Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
                # print(f"{index + 1}. {task.title} | {task.description}")
    def view_over_due_tasks(self)->None:
        print("Over Due Tasks:")