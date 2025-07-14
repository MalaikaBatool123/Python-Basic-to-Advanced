# controllers/task_manager_controller.py
from task_list import TaskList

from task_factory import TaskFactory
from TaskCsvDAO import TaskCsvDAO
from TaskPickleDAO import TaskPickleDAO
from owner import Owner
# from ui.command_line_ui import file_path, file_path_pkl
import config
class TaskManagerController:
    def __init__(self, owner):
        self.task_list = TaskList(owner)

    def add_task(self, title, desc, due_date, interval=None, priority=None):
        if interval:
            task = TaskFactory.create_task(title, desc, due_date, interval=interval)
        elif priority:
            task = TaskFactory.create_task(title, desc, due_date, priority=priority)
        else:
            task = TaskFactory.create_task(title, desc, due_date)
        
        self.task_list.add_task(task)

    def has_tasks(self) -> bool:
        return bool(self.task_list.tasks)

    def remove_task(self, index: int) -> None:
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("That task number doesn't exist.")
        task = self.task_list.get_task(index)
        if not task:
            raise IndexError("That task number doesn't exist.")

        removed_title = task.title
        # removed_title = self.task_list.tasks[index - 1].title
        
        self.task_list.remove_task(index)

        # Remove from CSV
        dao = TaskCsvDAO(config.file_path)
        dao.remove_task_by_title(removed_title)
        

    def get_all_tasks(self):
        return self.task_list.tasks

    def mark_task_completed(self, index: int):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")
        # getting task object by using get_task() method
        task = self.task_list.get_task(index)
        if not task:
            raise IndexError("That task number doesn't exist.")
        
        old_title = task.title
        task.mark_completed()
        dao = TaskCsvDAO(config.file_path)
        dao.update_task(task, old_title)

    def change_task_title(self, index: int, new_title: str):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")
        # getting task object by using get_task() method
        task = self.task_list.get_task(index)
        if not task:
            raise IndexError("That task number doesn't exist.")
        
        old_title = task.title
        task.change_title(new_title)
        dao = TaskCsvDAO(config.file_path)
        dao.update_task(task, old_title)

    def change_task_description(self, index: int, new_desc: str):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")
        # getting task object by using get_task() method
        task = self.task_list.get_task(index)
        if not task:
            raise IndexError("That task number doesn't exist.")
        

        old_title = task.title
        task.change_description(new_desc)        
        dao = TaskCsvDAO(config.file_path)
        dao.update_task(task, old_title)
        
    def change_due_date(self, index, new_date):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")
        # getting task object by using get_task() method
        task = self.task_list.get_task(index)
        if not task:
            raise IndexError("That task number doesn't exist.")
        
        old_title = task.title
        task.change_due_date(new_date)
        dao = TaskCsvDAO(config.file_path)
        dao.update_task(task, old_title)

    def view_over_due_tasks(self):
        self.task_list.view_over_due_tasks()

    def view_tasks(self):
        self.task_list.view_tasks()

    def load_tasks(self, tasks):
        for task in tasks:
            self.task_list.add_task(task)
    def load_tasks_from_csv(self, path: str):
        dao = TaskCsvDAO(path)
        tasks = dao.get_all_tasks()
        self.load_tasks(tasks)  # loads them into task_list
    def save_tasks_to_csv(self, path: str):  
        dao = TaskCsvDAO(path)
        
        dao.save_all_tasks(self.task_list.tasks)
    def get_task(self, index):
        task = self.task_list.get_task(index)
        return task
    def load_tasks_from_pickle(self, path: str):
        dao = TaskPickleDAO(path)
        tasks = dao.get_all_tasks()
        self.load_tasks(tasks)

    def save_tasks_to_pickle(self, path: str):
        dao = TaskPickleDAO(path)
        dao.save_all_tasks(self.task_list.tasks)

    def get_owner(self) -> Owner:
        return self.task_list.owner
