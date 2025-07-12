import datetime
from task import Task
from recurring_task import RecurringTask
from task_list import TaskList
class TaskTestDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
    def get_all_tasks(self) -> list[Task]:
        task_list =[
        Task("Buy groceries",'description it is', datetime.datetime.now() - datetime.timedelta(days=4)),
        Task("Do laundry",'description it is', datetime.datetime.now() - datetime.timedelta(days=-2)),
        Task("Clean room",'description it is', datetime.datetime.now() + datetime.timedelta(days=-1)),
        Task("Do homework",'description it is', datetime.datetime.now() + datetime.timedelta(days=3)),
        Task("Walk dog",'description it is', datetime.datetime.now() + datetime.timedelta(days=5)),
        Task("Do dishes",'description it is', datetime.datetime.now() + datetime.timedelta(days=6))
        ]
        # sample recurring task
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(),datetime.timedelta(days=7), 8)
        # propagate the recurring task with some completed dates
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)
        task_list.append(r_task)
        return task_list    
    def save_all_tasks(self, tasks: list[Task]) -> None:
        pass