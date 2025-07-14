from task import Task
from recurring_task import RecurringTask
import datetime
from typing import Any
from priority_task import PriorityTask
class TaskFactory:
    @staticmethod
    def create_task(title: str, description: str, date: datetime.datetime, **kwargs: Any) -> Task:
        # Factory method that creates either a Task or RecurringTask object depending on the presence of "interval"
        # It checks if an "interval" is passed in the keyword arguments (**kwargs).
        # it checks if a "priority" is passed in the keyword arguments (**kwargs).
        # If yes, it creates a RecurringTask object, otherwise just a normal Task.
        if "interval" in kwargs:
            return RecurringTask(title, description, date, kwargs["interval"])   
        elif "priority" in kwargs:
            return PriorityTask(title, description, date, kwargs["priority"])  # ✅ New
        else:
            return Task(title, description, date)
        
        
        
        