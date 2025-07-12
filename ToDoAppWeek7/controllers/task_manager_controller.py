# controllers/task_manager_controller.py
from task_list import TaskList
from task import Task
from task_factory import TaskFactory
from TaskCsvDAO import TaskCsvDAO
from TaskPickleDAO import TaskPickleDAO
class TaskManagerController:
    def __init__(self, user_name):
        self.task_list = TaskList(user_name)

    def add_task(self, title, desc, due_date, interval=None):
        if interval:
            task = TaskFactory.create_task(title, desc, due_date, interval=interval)
        else:
            task = TaskFactory.create_task(title, desc, due_date)
        
        self.task_list.add_task(task)

    def has_tasks(self) -> bool:
        return bool(self.task_list.tasks)

    def remove_task(self, index: int) -> None:
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("That task number doesn't exist.")

        removed_title = self.task_list.tasks[index - 1].title
        self.task_list.remove_task(index)

        # Remove from CSV
        dao = TaskCsvDAO("tasks.csv")
        dao.remove_task_by_title(removed_title)
        

    def get_all_tasks(self):
        return self.task_list.tasks

    def mark_task_completed(self, index: int):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")

        old_title = self.task_list.tasks[index - 1].title
        self.task_list.tasks[index - 1].mark_completed()
        dao = TaskCsvDAO("tasks.csv")
        dao.update_task(self
                        .task_list.tasks[index - 1], old_title)

    def change_task_title(self, index: int, new_title: str):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")

        old_title = self.task_list.tasks[index - 1].title
        self.task_list.tasks[index - 1].change_title(new_title)
        dao = TaskCsvDAO("tasks.csv")
        dao.update_task(self.task_list.tasks[index - 1], old_title)

    def change_task_description(self, index: int, new_desc: str):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")

        old_title = self.task_list.tasks[index - 1].title
        self.task_list.tasks[index - 1].change_description(new_desc)        
        dao = TaskCsvDAO("tasks.csv")
        dao.update_task(self.task_list.tasks[index - 1], old_title)
        
    def change_due_date(self, index, new_date):
        if index < 1 or index > len(self.task_list.tasks):
            raise IndexError("Invalid index")
        old_title = self.task_list.tasks[index - 1].title
        self.task_list.tasks[index - 1].change_due_date(new_date)
        dao = TaskCsvDAO("tasks.csv")
        dao.update_task(self.task_list.tasks[index - 1], old_title)

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
        return self.task_list.tasks[index - 1]
    def load_tasks_from_pickle(self, path: str):
        dao = TaskPickleDAO(path)
        tasks = dao.get_all_tasks()
        self.load_tasks(tasks)

    def save_tasks_to_pickle(self, path: str):
        dao = TaskPickleDAO(path)
        dao.save_all_tasks(self.task_list.tasks)

