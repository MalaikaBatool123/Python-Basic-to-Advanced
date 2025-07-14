import datetime
from task import Task
from owner import Owner

class TaskList:
    def __init__(self, owner:Owner) -> None:
        # Constructor that initializes the task list with the given owner
        self.owner = owner
        self.tasks = []  # Empty list to hold tasks

    def add_task(self, task:Task) -> None:
        # Adds a new task to the task list
        self.tasks.append(task)

    def remove_task(self,index) -> None:
        # Removes a task by its 1-based index (as seen by the user)
        
        if index >= 1 and index <= len(self.tasks):
            # Get the task object using get_task method
            task = self.get_task(index)
            
            print(f"Removed: {task.title}")  # Display task title that is being removed
            
            # Delete the task — NOTE: this only deletes the reference to the task, not from the list
            del task
        else:
            # If index is invalid, notify user
            print("Invalid index. Please try again.")

    """Property attribute is used to use the method as attribute
    In this case this method of getting in completed tasks will be used as attribute and not method"""
    @property
    def uncompleted_tasks(self) -> list[Task]:
        # Returns a list of tasks that are not marked as completed
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self) -> None:
        # Displays the tasks that are still pending (i.e., not completed)
        if not self.uncompleted_tasks:
            print("No tasks to show.")  # No uncompleted tasks
        else:
            print("The following tasks are still to be done:")
            for task in self.uncompleted_tasks:
                # Find original index of the task in the full list for proper numbering
                ix = self.tasks.index(task)
                print(f"{ix+1}: {task}")  # Show task number and string representation of task

    def view_over_due_tasks(self)->None:
        # Displays tasks that have passed their due date
        if not self.tasks:
            print("No tasks in the list.")
            return
        
        over_due_tasks = []
        today = datetime.date.today()

        # Check each task to see if it's overdue
        for index, task in enumerate(self.tasks, start=1):
            if task.due_date < today:
                over_due_tasks.append((index, task))  # Add index and task to the overdue list

        if over_due_tasks:
            print("Over Due Tasks:")
            for i, task in over_due_tasks:
                # If description exists, show it; otherwise say "No description"
                desc = task.description if task.description else "No description"
                print(f"{i}. {task.title} | Due Date: {task.due_date} | Description: {desc}")
        else:
            print("No over due tasks available")

        # Add visual spacing to the output
        print("\n")
        print("-"*40)
        print("\n")

    def get_task_by_title(self, title: str) -> Task:
        # Returns a task by matching the given title
        for task in self.tasks:
            if task.title == title:
                return task

    def get_task(self, index) -> Task:
        """Returns the task at the given index (1-based index for user-friendliness)."""
        if 1 <= index <= len(self.tasks):
            return self.tasks[index - 1]  # Convert 1-based to 0-based index
        else:
            return None  # Return None if index is invalid
