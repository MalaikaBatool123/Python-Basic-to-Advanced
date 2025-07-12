from controllers.task_manager_controller import TaskManagerController   
from task_factory import TaskFactory
# from datetime import datetime
import datetime
from TaskCsvDAO import TaskCsvDAO
from TaskPickleDAO import TaskPickleDAO

class CommandLineUI:
    def __init__(self):
        name = input("Enter your name: ")
        self.controller = TaskManagerController(name)
    def run(self):
        while True:
            self._print_menu()
            print("\n")
            choice = input("Enter your choice: ") 
            print("\n")
            if choice == "1":
                self._add_task()
            elif choice == "2":
                self.controller.view_tasks()
            elif choice == "3":
                self._remove_task()
            elif choice == "4":
                self._mark_task_completed()
            elif choice == "5":
                self._change_task_title()
            elif choice == "6":
                self._change_task_description()
            elif choice == "7":
                self.controller.view_over_due_tasks()
            elif choice == "8":
                self._change_task_due_date
            elif choice == "9":
                self._load_tasks_from_csv()
            elif choice == "10":
                self._save_tasks_to_csv()
            elif choice == "11":
                self._load_tasks_from_pickle()
            elif choice == "12":
                self._save_tasks_to_pickle()
            elif choice == "13":
                print("Quit")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 13.\n")
        
    def _print_menu(self):
        print("To-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Remove a task") 
        print("4. Mark as completed")
        print("5. Change title of task")
        print("6. Change description of task")
        print("7. Show over due tasks")
        print("8. Change Due date of task")
        print("9. Load Tasks from CSV")
        print("10. Save Tasks to CSV")
        print("11. Load Data from Pickle File")
        print("12. Save Data to Pickle File")
        print("13. Quit")
    def _get_task_details(self):
        title = input("Enter task title: ")
        desc = input("Enter task description: ")
        date_str = input("Enter due date (YYYY-MM-DD): ")
        due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return title, desc, due_date

    def _add_task(self):
        while True:
            print("1. One Time Task")
            print("2. Recurring Task")
            print("3. Back")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                title, desc, due_date = self._get_task_details()
                self.controller.add_task(title, desc, due_date)
                print(f"'{title}' has been added to your to-do list.\n")
                break

            elif sub_choice == "2":
                title, desc, due_date = self._get_task_details()
                days = int(input("Enter the interval in days: "))
                interval = datetime.timedelta(days=days)
                self.controller.add_task(title, desc, due_date, interval=interval)
                print(f"'{title}' has been added to your to-do list.\n")
                break

            elif sub_choice == "3":
                break

    def _remove_task(self):
        self.controller.view_tasks()

        if not self.controller.has_tasks():
            print("[!] No tasks to remove.\n")
            return

        while True:
            try:
                user_input = input("Enter the number of the task to remove: ")

                if not user_input.isdigit():
                    raise ValueError("Please enter a number (e.g. 1, 2, 3...)")

                index = int(user_input)

                self.controller.remove_task(index)  # let controller do all logic
                print("Task removed successfully.\n")
                self.controller.view_tasks()
                break

            except ValueError as ve:
                print(f"[!] {ve}\n")
            except IndexError as ie:
                print(f"[!] {ie}\n")


    def _mark_task_completed(self):
        self.controller.view_tasks()

        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        while True:
            index = input("Enter the number of the task to mark as completed: ")

            if index.isdigit():
                index = int(index)
                try:
                    self.controller.mark_task_completed(index)
                    print("[✓] Task marked as completed.\n")
                    break
                except IndexError:
                    print("Invalid task number. Please try again.\n")
            else:
                print("Invalid input. Please enter a number like 1, 2, 3...\n")
    def _change_task_title(self):
        self.controller.view_tasks()

        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        while True:
            index = input("Enter the number of the task to change title: ")

            if index.isdigit():
                index = int(index)
                try:
                    new_title = input("Enter the new title: ")
                    self.controller.change_task_title(index, new_title)
                    print("[✓] Title updated.\n")
                    break
                except IndexError:
                    print("Invalid task number. Please try again.\n")
            else:
                print("Invalid input. Please enter a number like 1, 2, 3...\n")

    def _change_task_description(self):
        self.controller.view_tasks()

        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        while True:
            index = input("Enter the number of the task to change description: ")

            if index.isdigit():
                index = int(index)
                try:
                    new_description = input("Enter the new description: ")
                    self.controller.change_task_description(index, new_description)
                    print("[✓] Description updated.\n")
                    break
                except IndexError:
                    print("Invalid task number. Please try again.\n")
            else:
                print("Invalid input. Please enter a number like 1, 2, 3...\n")
                
                
    def _change_task_due_date(self):
        self.controller.view_tasks()  

        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        while True:
            index = input("Enter the number of the task to change due date: ")

            if index.isdigit():
                index = int(index)
                try:
                    new_date = input("Enter the new due date (YYYY-MM-DD): ")
                    self.controller.change_due_date(index, new_date)
                    print("[✓] Due date updated.\n")
                    break
                except IndexError:
                    print("Invalid task number. Please try again.\n")
            else:
                print("Invalid input. Please enter a number like 1, 2, 3...\n")     
    
    def _load_tasks_from_csv(self):
        path = input("Enter file path to load tasks (e.g. tasks.csv): ")
        try:
            self.controller.load_tasks_from_csv(path)
            print("[✓] Tasks loaded from file.\n")
        except Exception as e:
            print(f"[!] Failed to load tasks: {e}\n")

    def _save_tasks_to_csv(self):
        path = input("Enter file path to save tasks (e.g. tasks.csv): ")
        try:
            self.controller.save_tasks_to_csv(path)
            print("[✓] Tasks saved to file.\n")
        except Exception as e:
            print(f"[!] Failed to save tasks: {e}\n")
            
    def _load_tasks_from_pickle(self):
        path = input("Enter pickle file path to load from (e.g. tasks.pkl): ")
        try:
            self.controller.load_tasks_from_pickle(path)
            print("[✓] Tasks loaded from pickle.\n")
        except Exception as e:
            print(f"[!] Failed to load tasks: {e}\n")

    def _save_tasks_to_pickle(self):
        path = input("Enter pickle file path to save to (e.g. tasks.pkl): ")
        try:
            self.controller.save_tasks_to_pickle(path)
            print("[✓] Tasks saved to pickle.\n")
        except Exception as e:
            print(f"[!] Failed to save tasks: {e}\n")
