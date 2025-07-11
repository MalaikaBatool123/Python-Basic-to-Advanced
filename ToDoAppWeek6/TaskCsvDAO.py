import csv
import datetime
import os
from task import Task
from recurring_task import RecurringTask
class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        # self.storage_path = storage_path
        
        self.storage_path = os.path.join(os.path.dirname(__file__), storage_path)

        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]
    def get_all_tasks(self) -> list[Task]:
        task_list = []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_type = row["type"]
                title = row["title"]
                date_due_str = row["date_due"]
                date_due = None
                if date_due_str != "":
                    if "-" in date_due_str:
                        # Format is likely YYYY-MM-DD
                        date_due = datetime.datetime.strptime(date_due_str, "%Y-%m-%d").date()
                    elif "/" in date_due_str:
                        # Format is likely DD/MM/YYYY
                        date_due = datetime.datetime.strptime(date_due_str, "%d/%m/%Y").date()
                    else:
                        print(f"⚠️ Unknown date format: {date_due_str}")
                        date_due = None  # or set a default/fallback
                completed = row["completed"] == "True"  # convert string to boolean
                # date_created = datetime.datetime.strptime(row["date_created"], "%Y-%m-%d")
                date_created = None
                date_created_str = row["date_created"]
                if date_created_str != "":
                    if "-" in date_created_str:
                        # Format is likely YYYY-MM-DD
                        date_created = datetime.datetime.strptime(date_created_str, "%Y-%m-%d").date()
                    elif "/" in date_created_str:
                        # Format is likely DD/MM/YYYY
                        date_created = datetime.datetime.strptime(date_created_str, "%d/%m/%Y").date()
                    else:
                        print(f"⚠️ Unknown date format: {date_created_str}")
                        date_created = None  # or set a default/fallback
                # If task is RecurringTask, create it accordingly
                if task_type == "RecurringTask":
                    interval_days = int(row["interval"].split()[0])  # get number from "7 days"
                    interval = datetime.timedelta(days=interval_days)
                    
                    # parse completed_dates from comma-separated string
                    completed_dates = []
                    if row["completed_dates"]:
                        date_strs = row["completed_dates"].split(",")
                        completed_dates = [datetime.datetime.strptime(d.strip(), "%Y-%m-%d") for d in date_strs]

                    task = RecurringTask(title,'', date_due, interval)
                    task.completed = completed
                    task.date_created = date_created
                    task.completed_dates = completed_dates

                else:  # Handle regular Task
                    task = Task(title,'', date_due)
                    task.completed = completed
                    task.date_created = date_created

                task_list.append(task)

        return task_list
    def save_all_tasks(self, tasks: list[Task]) -> None:
        existing_titles = set()

        # If file exists, load existing tasks to check for duplicates
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    existing_titles.add(row["title"])  # Assuming title is unique

        # Now open file in append mode
        with open(self.storage_path, "a", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)

            # If file was just created (empty), write header
            if os.stat(self.storage_path).st_size == 0:
                writer.writeheader()

            for task in tasks:
                if task.title in existing_titles:
                    continue  # Skip duplicate tasks

                row = {}
                print(task.date_created)
                # Common fields
                row["title"] = task.title
                row["completed"] = str(task.completed)
                row["date_due"] = task.due_date.strftime("%Y-%m-%d")
                row["date_created"] = task.date_created.strftime("%d/%m/%Y")

                # Recurring task
                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                    interval = task.interval.days if hasattr(task.interval, "days") else task.interval
                    row["interval"] = f"{interval} days"
                    row["completed_dates"] = ",".join(
                        [d.strftime("%Y-%m-%d") for d in task.completed_dates]
                    )
                else:
                    row["type"] = "Task"
                    row["interval"] = ""
                    row["completed_dates"] = ""

                writer.writerow(row)