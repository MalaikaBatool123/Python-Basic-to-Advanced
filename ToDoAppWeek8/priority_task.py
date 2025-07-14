from task import Task
import datetime
class PriorityTask(Task):
    """
    Represents a task with a priority level.
    Inherits from Task and adds a 'priority' attribute with validation.
    """
    
    # This dictionary maps integer values to readable priority labels
    PRIORITY_MAP = {
        1: "Low",
        2: "Medium",
        3: "High"
    }
    def __init__(self, title: str, description: str, due_date: datetime.date, priority: int) -> None:
        super().__init__(title, description, due_date)

        # Ensure priority is within the accepted range (1, 2, 3)
        if priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1 (Low), 2 (Medium), or 3 (High).")
        
        self.priority = priority
    def __str__(self) -> str:
        # Add priority to the display string using its human-readable label
        priority_label = self.PRIORITY_MAP.get(self.priority, "Unknown")
        return super().__str__() + f" | Priority: {priority_label}"

    def change_priority(self, new_priority: int) -> None:
        # Allow changing the priority after creation with validation
        if new_priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1 (Low), 2 (Medium), or 3 (High).")
        self.priority = new_priority
