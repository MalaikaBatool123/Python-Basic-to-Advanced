import csv
import datetime
import os
from task import Task
from recurring_task import RecurringTask
class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        # gets the file path and joins it
        self.storage_path = os.path.join(os.path.dirname(__file__), storage_path)

        # initialize fieldnames
        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]
      
    def get_all_tasks(self) -> list[Task]:
        task_list = []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # getting each value from record one by one
                # Get the type of task (either Task or RecurringTask)
                task_type = row["type"]
                
                 # Get title and due date as string
                title = row["title"]
                date_due_str = row["date_due"]
                date_due = None
                
                # Convert the due date string into a datetime object (handling different formats)
                if date_due_str != "":
                    if "-" in date_due_str:
                        # Format is likely YYYY-MM-DD
                        date_due = datetime.datetime.strptime(date_due_str, "%Y-%m-%d").date()
                    elif "/" in date_due_str:
                        # Format is likely DD/MM/YYYY
                        date_due = datetime.datetime.strptime(date_due_str, "%d/%m/%Y").date()
                    else:
                        print(f"Unknown date format: {date_due_str}")
                        date_due = None  # or set a default/fallback
                
                # Check if the task was marked as completed
                completed = row["completed"] == "True"  # convert string to boolean
                
                # Handle the created date in a similar way
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
                        print(f"Unknown date format: {date_created_str}")
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

                else:  # Handle regular Task object
                    task = Task(title,'', date_due)
                    task.completed = completed
                    task.date_created = date_created

                task_list.append(task)

        return task_list
    
    def save_all_tasks(self, tasks: list[Task]) -> None:
        # create a set of existing task titles to check for duplicates
        existing_titles = set()

        # If file exists, load existing tasks to check for duplicates
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Add the title of each existing task to the set
                    # This helps us avoid saving duplicate tasks later
                    existing_titles.add(row["title"])  # Assuming title is unique

        # Open the file in append mode so we can add new tasks without deleting old ones
        with open(self.storage_path, "a", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)

             # If the file is empty, we add a header row to it first
            if os.stat(self.storage_path).st_size == 0:
                writer.writeheader()

            # Go through each task in the list
            for task in tasks:
                 # If this task is already in the file (based on title), skip it
                if task.title in existing_titles:
                    continue  # Skip duplicate tasks
                
                
                # This row dictionary will hold all the task details to be written
                row = {}
                
                # Add basic task information to the row
                row["title"] = task.title
                row["completed"] = str(task.completed)
                # changing the format fo date to YYYY-MM-DD or DD/MM/YYYY
                row["date_due"] = task.due_date.strftime("%Y-%m-%d")
                row["date_created"] = task.date_created.strftime("%d/%m/%Y")

                # Check if the task is a recurring task and handle accordingly
                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                     # If the interval has a 'days' attribute (like timedelta), extract it
                    interval = task.interval.days if hasattr(task.interval, "days") else task.interval
                    row["interval"] = f"{interval} days"
                    
                    # Convert the list of completed dates into a single comma-separated string
                    row["completed_dates"] = ",".join(
                        [d.strftime("%Y-%m-%d") for d in task.completed_dates]
                    )
                else:
                    # If it's just a normal one-time Task, keep these fields empty
                    row["type"] = "Task"
                    row["interval"] = ""
                    row["completed_dates"] = ""

                # Finally, write the task details to the CSV file
                writer.writerow(row)
    
    def update_task(self, updated_task: Task, old_title) -> None:
        
        """Updates a task in the CSV by replacing the one with the same title."""

        updated_rows = []
        found = False

        # Load all existing tasks
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    
                    if row["title"] == old_title:
                        # Replace with updated task
                        new_row = {}

                        new_row["title"] = updated_task.title
                        new_row["completed"] = str(updated_task.completed)
                        new_row["date_due"] = updated_task.due_date.strftime("%Y-%m-%d")
                        new_row["date_created"] = updated_task.date_created.strftime("%d/%m/%Y")

                        if isinstance(updated_task, RecurringTask):
                            new_row["type"] = "RecurringTask"
                            interval = updated_task.interval.days if hasattr(updated_task.interval, "days") else updated_task.interval
                            new_row["interval"] = f"{interval} days"
                            # new_row["interval"] = f"{updated_task.interval.days} days"
                            new_row["completed_dates"] = ",".join(
                                [d.strftime("%Y-%m-%d") for d in updated_task.completed_dates]
                            )
                        else:
                            new_row["type"] = "Task"
                            new_row["interval"] = ""
                            new_row["completed_dates"] = ""

                        updated_rows.append(new_row)
                        found = True
                    else:
                        # Keep other tasks as is
                        updated_rows.append(row)

        # If task wasn't found, don't update anything
        if not found:
            print(f"[!] Task with title '{updated_task.title}' not found.")
            return

        # Overwrite the CSV file with updated rows
        with open(self.storage_path, "w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        print(f"[✓] Task '{updated_task.title}' updated successfully.")
