import datetime
class Task:
    def __init__(self, title:str, description:str, due_date) -> None:
        self.title = title
        self.description = description
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.due_date = due_date
    def __str__(self) -> str:
        # this is method to show the task object output in string
        status = "Completed" if self.completed else "Pending"
        desc = self.description if self.description else "No description"
        
        return f"Task: {self.title} | Status: {status} | Date Created: {self.date_created.strftime('%Y-%m-%d')} | Due Date: {self.due_date} | Description: {desc}"
    def mark_completed(self) -> None:
        self.completed = True
    def change_title(self, new_title) -> None:
        self.title = new_title
    def change_description(self, new_description) -> None:
        self.description = new_description
    def change_due_date(self, new_date)-> None:
        self.due_date = new_date

