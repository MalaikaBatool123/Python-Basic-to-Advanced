import pickle
import os
from task import Task
from recurring_task import RecurringTask

class TaskPickleDAO:
    def __init__(self, storage_path: str) -> None:
         # Combine the current directory with the file name to get the full path
        self.storage_path = os.path.join(os.path.dirname(__file__), storage_path)


    def get_all_tasks(self) -> list[Task]:
        """Load all tasks from the pickle file."""
        # If the pickle file doesn't exist, show a message and return an empty list
        if not os.path.exists(self.storage_path):
            print("[i] No pickle file found. Returning empty task list.")
            return []
        # Open the pickle file in binary read mode
        with open(self.storage_path, "rb") as file:
            # Load the entire list of task objects from the file
            task_list = pickle.load(file)
        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """Save all tasks to the pickle file."""
        # Open the pickle file in binary write mode (this will overwrite existing data)
        with open(self.storage_path, "wb") as file:
             # serialize the entire list of tasks into the file
            pickle.dump(tasks, file)
        print(f"[✓] Tasks saved to {self.storage_path} successfully.")
