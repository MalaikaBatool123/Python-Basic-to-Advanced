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
        # if any of tasks are present in list
        if not self.tasks:
            print("No tasks in the list.")
            return
                    
        over_due_tasks = []
        today = datetime.date.today()
        # if date of any task is passed already
        for index, task in enumerate(self.tasks, start=1):
            if task.due_date < today:
                over_due_tasks.append((index, task))
        #  Display overdue tasks if found
        if over_due_tasks:
            print("Over Due Tasks:")
            for i, task in over_due_tasks:
                desc = task.description if task.description else "No description"
                print(f"{i}. {task.title} | Due Date: {task.due_date} | Description: {desc}")
        else:
            print("No over due tasks available")
        # spacing
        print("\n")
        print("-"*40)
        print("\n")