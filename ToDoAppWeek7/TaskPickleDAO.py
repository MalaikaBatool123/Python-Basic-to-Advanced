import pickle
import os
from task import Task
from recurring_task import RecurringTask

class TaskPickleDAO:
    def __init__(self, storage_path: str) -> None:
        # self.storage_path = storage_path
        self.storage_path = os.path.join(os.path.dirname(__file__), storage_path)


    def get_all_tasks(self) -> list[Task]:
        """Load all tasks from the pickle file."""
        print('tasks list', task_list)
        if not os.path.exists(self.storage_path):
            print("[i] No pickle file found. Returning empty task list.")
            return []

        with open(self.storage_path, "rb") as file:
            task_list = pickle.load(file)
        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """Save all tasks to the pickle file."""
        with open(self.storage_path, "wb") as file:
            pickle.dump(tasks, file)
        print(f"[✓] Tasks saved to {self.storage_path} successfully.")
