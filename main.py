from os import path
from taskhandler import create_list, new_task, show_list, delete_entry, edit_entry
import sys

# variables
version = "aplha 0.1"

# pre-startup checks
# check if tasks.txt exists, if not --> create
if not path.exists("tasks.txt"):
    f = open("tasks.txt", "w+")
else:
    pass

# check for commandline arguments
if len(sys.argv) == 1:
    pass
# print current version
elif sys.argv[1] == '--version':
    print(version)
    quit()

print("Good Morning!")
todo_selection = '0'

# open a list and write all tasks to it
create_list()

# main loop
while todo_selection != '5':
    print("What do you want to do? \n")
    print("[1] Create a new task")
    print("[2] View current task list")
    print("[3] Delete a task")
    print("[4] Edit a task")
    print("[5] Exit Program")
    todo_selection = input("\nSelection: ")

# if statement, running different modules from taskhandler.py
# depending on user input
    if todo_selection == '1':
        new_task()

# 2 - View current task list
    elif todo_selection == '2':
        show_list()

# 3 - Show Tasklist and Delete an entry
    elif todo_selection == '3':
        delete_entry()

# 4 - Edit a tasks
    elif todo_selection == '4':
        edit_entry()

# 5 - Exit Program
    elif todo_selection == '5':
        print("Good Bye!")
        exit()

    else:
        print("\nThis is not a valid option! Please try again!\n")
