from task import Task
from recurring_task import RecurringTask
import datetime
from typing import Any
class TaskFactory:
    @staticmethod
    def create_task(title:str,description:str, date:datetime.datetime, **kwargs:Any) -> Task:
        if "interval" in kwargs:
            return RecurringTask(title,description, date, kwargs["interval"])   
        else:
            return Task(title,description, date)
    