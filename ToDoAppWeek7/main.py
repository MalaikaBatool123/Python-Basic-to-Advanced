""" 
this is main file for To do List Manager application using OOP concepts
this file will use codes of task and tasklist classes
This is the entry point of the program
"""
from ui.command_line_ui import CommandLineUI

# function to add spacing
def spacing():
    print("\n")
    print("-"*40)
    print("\n")


def main() -> None:
    print("="*40)   
    print("----Welcome to the To-Do List Manager----\n")
    ui = CommandLineUI()
    ui.run()
    print("\n")
if __name__ == "__main__":
    main()
    
# due date and completed dates is remaining from week 5 and the tasks after it are also remaining