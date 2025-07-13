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
        # If task has been completed before, calculate next due from last completion
        if self.completed_dates:
            return self.completed_dates[-1] + self.interval
        # Otherwise calculate from existing due date
        return self.due_date + self.interval
    def mark_completed(self) -> None:
        # Add today's date to completed history
        today = datetime.date.today()
        self.completed_dates.append(today)

        # Update due date to next scheduled one
        self.due_date = self._compute_next_due_date()

        # Mark as completed (from parent)
        self.completed = True
    def __str__(self):
        # this will use the string method of parent class and then concatenate the new attribute
        return super().__str__() + f" | interval: {self.interval.days} days" 

    def __eq__(self, other):
        return (
            isinstance(other, Task)
            and self.title == other.title
            and self.due_date == other.due_date
            and self.description == other.description
            and self.interval == other.interval
        )
