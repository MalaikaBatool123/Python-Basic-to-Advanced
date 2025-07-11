""" 
This file is for recurring tasks and its functionality, the tasks which should appear again after interval of time
"""
from task import Task
import datetime

class RecurringTask(Task):
    """
    This class is for recurring tasks  
    Args: inherits from parent class 'Task'
    """
    def __init__(self, title:str, description:str, due_date, interval:datetime.timedelta) -> None:
        # title, description, due_date are attributes inherited from parent class
        # interval is new attribute which is for repetition of tasks
        super().__init__(title, description, due_date)
        self.interval = interval
        # list of completed dates of recurring tasks for history
        self.completed_dates : list[datetime.datetime] = [] 
    def _compute_next_due_date(self) -> datetime.datetime:
        """Computes the next due date of the task.
        Returns:
        datetime.datetime: The next due date of the task.
        """
        return self.date_due + self.interval
    def __str__(self):
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"
