from controllers.task_manager_controller import TaskManagerController   
import datetime
from owner import Owner
import config
class CommandLineUI:
    def __init__(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        owner = Owner(name, email)
        self.controller = TaskManagerController(owner)
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
                owner = self.controller.get_owner()
                print(f"Owner Name: {owner.name}")
                print(f"Owner Email: {owner.email}")
            elif choice == "14":
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
        print("13. Get Owner Details")
        print("14. Quit")
        
    def _get_task_details(self):
        """This method is used to get the title, description and due date of the task from the user."""
        title = input("Enter task title: ")
        desc = input("Enter task description: ")
        # input date in string
        date_str = input("Enter due date (YYYY-MM-DD): ")
        # converting string date into date object
        due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return title, desc, due_date

    def _add_task(self):
        """This method is used to add a task to the to-do list.
        It will ask the user whether the task is one time or recurring.
        """
        while True:
            print("1. One Time Task")
            print("2. Recurring Task")
            print("3. Back")

            sub_choice = input("Enter your choice: ")

            # one time task
            if sub_choice == "1":
                title, desc, due_date = self._get_task_details()
                # calling the controller method, as all the logic is in the controller
                self.controller.add_task(title, desc, due_date)
                print(f"'{title}' has been added to your to-do list.\n")
                break

            # recurring task
            elif sub_choice == "2":
                title, desc, due_date = self._get_task_details()
                # input interval days
                days = int(input("Enter the interval in days: "))
                # converting days into timedelta object to work on it later
                interval = datetime.timedelta(days=days)
                # calling the controller method, as all the logic is in the controller
                self.controller.add_task(title, desc, due_date, interval=interval)
                print(f"'{title}' has been added to your to-do list.\n")
                break

            elif sub_choice == "3":
                break

    def _remove_task(self):
        # Show current tasks before asking for deletion input
        self.controller.view_tasks()

        if not self.controller.has_tasks():
            print("[!] No tasks to remove.\n")
            return

        # Keep asking user until a valid task number is entered
        while True:
            try:
                user_input = input("Enter the number of the task to remove: ")

                # If task list is empty, notify the user and exit
                # Ensure input is a digit, not letters or symbols
                if not user_input.isdigit():
                    raise ValueError("Please enter a number (e.g. 1, 2, 3...)")

                index = int(user_input)
                # Ask controller to remove the task at this index
                self.controller.remove_task(index)  # let controller do all logic
                print("Task removed successfully.\n")
                # show the updated list of tasks
                self.controller.view_tasks()
                break

            except ValueError as ve:
                 # Catch non-numeric input and inform the user
                print(f"[!] {ve}\n")
            except IndexError as ie:
                # Catch invalid index (e.g., number too high or low)
                print(f"[!] {ie}\n")

    def _mark_task_completed(self):
        # Display current task list so user knows the numbers
        self.controller.view_tasks()

        # Check if there are any tasks at all
        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        # Repeat input prompt until valid task is selected
        while True:
            index = input("Enter the number of the task to mark as completed: ")

            if index.isdigit():
                index = int(index)
                try:
                    # Mark the selected task as completed
                    self.controller.mark_task_completed(index)
                    print("[✓] Task marked as completed.\n")
                    break
                except IndexError:
                    # If entered number is not a valid task index
                    print("Invalid task number. Please try again.\n")
            else:
                # Handle non-numeric input gracefully
                print("Invalid input. Please enter a number like 1, 2, 3...\n")


    def _change_task_title(self):
        # Show all tasks so the user can pick the one to edit
        self.controller.view_tasks()

        # Check if task list is empty and return early
        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        # Keep prompting user for valid input
        while True:
            index = input("Enter the number of the task to change title: ")

            if index.isdigit():
                index = int(index)
                try:
                    # Ask for new title
                    new_title = input("Enter the new title: ")

                    # Pass both index and new title to controller
                    self.controller.change_task_title(index, new_title)
                    print("[✓] Title updated.\n")
                    break
                except IndexError:
                    # Catch if index is out of range
                    print("Invalid task number. Please try again.\n")
            else:
                # Warn the user if they enter a non-numeric value
                print("Invalid input. Please enter a number like 1, 2, 3...\n")


    def _change_task_description(self):
        # Display the current list of tasks so the user can see which task they want to update
        self.controller.view_tasks()

        # If there are no tasks available, inform the user and exit this function early
        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        # Enter a loop to get valid input from the user
        while True:
            # Ask the user to input the number of the task they want to change
            index = input("Enter the number of the task to change description: ")

            # Check if the input is a digit (i.e., a number like "1", "2", etc.)
            if index.isdigit():
                index = int(index)  # Convert the valid numeric string input to an actual integer
                try:
                    # Prompt user to input the new description for the selected task
                    new_description = input("Enter the new description: ")
                    
                    # Call the controller's method to update the task description
                    self.controller.change_task_description(index, new_description)
                    
                    # Let the user know the update was successful
                    print("[✓] Description updated.\n")
                    
                    # Exit the loop since the operation was successful
                    break

                except IndexError:
                    # This will happen if the task number entered does not exist
                    print("Invalid task number. Please try again.\n")
            else:
                # If the input is not a valid number, show an error message and repeat
                print("Invalid input. Please enter a number like 1, 2, 3...\n")
                    
    def _change_task_due_date(self):
        # Show all current tasks so the user knows which task they might want to update
        self.controller.view_tasks()  

        # If there are no tasks, notify the user and stop the operation early
        if not self.controller.has_tasks():
            print("[!] No tasks available.\n")
            return

        # Continue prompting the user until a valid task number and date are provided
        while True:
            # Ask the user to select the task by number
            index = input("Enter the number of the task to change due date: ")

            # Check if the input is a valid number
            if index.isdigit():
                index = int(index)  # Convert the input string to an integer
                try:
                    # Ask the user for the new due date in the correct format
                    new_date = input("Enter the new due date (YYYY-MM-DD): ")

                    # Use the controller to update the due date of the selected task
                    self.controller.change_due_date(index, new_date)
                    # Confirm that the update was successful
                    print("[✓] Due date updated.\n")
                    # Exit the loop after successful update
                    break
                except IndexError:
                    # If the user entered a task number that doesn't exist, show an error message
                    print("Invalid task number. Please try again.\n")
            else:
                # If the user input is not a number, show an error message and loop again
                print("Invalid input. Please enter a number like 1, 2, 3...\n")     

    def _load_tasks_from_csv(self):
        # Check if a file path has already been set in the config module
        if (not config.file_path):
            # If not, ask the user to enter the path of the CSV file to load tasks from
            config.file_path = input("Enter file path to load tasks (e.g. tasks.csv): ")
        
        try:
            # Call the controller to load tasks from the given file path
            self.controller.load_tasks_from_csv(config.file_path)

            # If loading is successful, let the user know
            print("[✓] Tasks loaded from file.\n")
        except Exception as e:
            # If anything goes wrong (e.g., file not found or corrupt), catch and show the error
            print(f"[!] Failed to load tasks: {e}\n")

    def _save_tasks_to_csv(self):
        # Check if the CSV file path is not already set
        if (not config.file_path):
            # Prompt the user to enter the file path where tasks should be saved
            config.file_path = input("Enter file path to load tasks (e.g. tasks.csv): ")
        
        try:
            # Ask the controller to save all tasks to the given CSV file
            self.controller.save_tasks_to_csv(config.file_path)

            # Notify the user that the saving was successful
            print("[✓] Tasks saved to file.\n")
        except Exception as e:
            # If any unexpected error occurs during the saving process, show an error message
            print(f"[!] Failed to save tasks: {e}\n")


    def _load_tasks_from_pickle(self):
        # Check if the Pickle file path is not already set
        if (not config.file_path_pkl):
            # Ask the user to input the path to the Pickle file from which to load tasks
            config.file_path_pkl = input("Enter file path to load tasks (e.g. tasks.pkl): ")
        
        try:
            # Ask the controller to load tasks from the specified Pickle file
            self.controller.load_tasks_from_pickle(config.file_path_pkl)

            # Notify the user of successful loading
            print("[✓] Tasks loaded from pickle.\n")
        except Exception as e:
            # Catch and print any errors that occur during loading (e.g., file not found or unpickling issues)
            print(f"[!] Failed to load tasks: {e}\n")


    def _save_tasks_to_pickle(self):
        # Check if the Pickle file path has not already been defined
        if (not config.file_path_pkl):
            # Prompt the user for the Pickle file path to save the tasks
            config.file_path_pkl = input("Enter file path to load tasks (e.g. tasks.pkl): ")
        
        try:
            # ❗ BUG ALERT: This line mistakenly **loads** tasks instead of saving them.
            # The function name suggests saving, but it’s calling `load_tasks_from_pickle`.
            # It should likely be:
            # self.controller.save_tasks_to_pickle(config.file_path_pkl)

            self.controller.save_tasks_to_pickle(config.file_path_pkl)  # <-- should be save
            print("[✓] Tasks saved to pickle.\n")
        except Exception as e:
            # Handle and display any exceptions during the save process
            print(f"[!] Failed to save tasks: {e}\n")
