import datetime
class Task:
    def __init__(self, title: str, description: str, due_date) -> None:
        # Initializes a Task object with a title, description, and due date.
        self.title = title  # Task title
        self.description = description  # Task description
        self.completed = False  # By default, task is not completed
        self.date_created = datetime.datetime.now()  # Set creation date to current timestamp
        self.due_date = due_date  # Set the due date as provided by the user

    def __str__(self) -> str:
        # This method controls how the Task object is displayed when printed
        status = "Completed" if self.completed else "Pending"  # Show readable completion status
        desc = self.description if self.description else "No description"  # Fallback if no description

        # Nicely formatted string that represents the full task info
        return f"Task: {self.title} | Status: {status} | Date Created: {self.date_created.strftime('%Y-%m-%d')} | Due Date: {self.due_date} | Description: {desc}"
    def mark_completed(self) -> None:
        # Mark the task as completed by setting the flag to True
        self.completed = True

    def change_title(self, new_title) -> None:
        # Allow changing the title of the task
        self.title = new_title

    def change_description(self, new_description) -> None:
        # Allow changing the task's description
        self.description = new_description

    def change_due_date(self, new_date) -> None:
        # Allow modifying the due date of the task
        self.due_date = new_date

    def __eq__(self, other):
        # This equality method helps compare two Task objects.
        # It returns True only if title, due_date, and description are all exactly the same.
        return (
            isinstance(other, Task)
            and self.title == other.title
            and self.due_date == other.due_date
            and self.description == other.description
        )
