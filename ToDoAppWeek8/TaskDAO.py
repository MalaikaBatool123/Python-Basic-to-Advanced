"""Abstract class for DAO classes"""
from abc import ABC, abstractmethod
from task import Task


class TaskDAO(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[Task]:
        pass

    @abstractmethod
    def save_all_tasks(self, tasks: list[Task]) -> None:
        pass
    
    
    
    