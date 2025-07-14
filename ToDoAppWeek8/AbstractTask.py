"""Abstract class for Task classes."""
from abc import ABC, abstractmethod
import datetime

class AbstractTask(ABC):
    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title = title
        self.description = description
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.due_date = due_date

    @abstractmethod
    def mark_completed(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass