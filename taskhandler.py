
# open a list (array)
todo_list = []

# CREATES AN INITIAL LIST OF TASKS
def create_list():
    f = open("tasks.txt", "r+")
    for x in f:
        todo_list.append(x)
    f.close()

#CREATE A NEW TASK
def new_task():
    # 1 - Create a new task
    new_task = input("Please name your task: ")
    todo_list.append(new_task + "\n")
    # write to file -----
    f = open("tasks.txt", "w")
    for x in todo_list:
        f.write(x)
    f.close()
    # end of write to file ------------
    print("Task saved! \n")

# SHOW THE CURRENT TASK LIST
def show_list():
    i = int(0)
    print("This is your current task list: \n")
    print("##########\n")
    for x in todo_list:
        print("[" + str(i) + "] " + x)
        i += 1
    print("##########\n")

# DELETE AN ENTRY FROM THE TASK LIST
def delete_entry():
    # Show current task list
    i = int(0)
    print("\nThis is your current task list: \n")
    print("##########\n")
    for x in todo_list:
        print("[" + str(i) + "] " + x)
        i += 1
    print("##########\n")
    # Select entry and delete
    select_del = input("Please select the task you want to remove: ")
    try:
        select_del = int(select_del)
        todo_list.pop(select_del)
        # write to file -----
        f = open("tasks.txt", "w")
        for x in todo_list:
            f.write(x)
        f.close()
        # end of write to file ------------
        print("The task has been deleted!")
    except:
        print("\nThis is not a valid entry! Please try again!\n")
        pass

def edit_entry():
    # Show current task list
    i = int(0)
    print("\nThis is your current task list: \n")
    print("##########\n")
    for x in todo_list:
        print("[" + str(i) + "] " + x)
        i += 1
    print("##########\n")
    # select entry to edit
    select_edit = input("Please select the task you want to edit: ")
    try:
        select_edit = int(select_edit)
        edit_txt = input("Please enter the updated task: ")
        todo_list[select_edit] = edit_txt
        print("The task has been updated!")
        # write to file -----
        f = open("tasks.txt", "w")
        for x in todo_list:
            f.write(x)
        f.close()
        # end of write to file ------------
    except:
        print("\nThis is not a valid entry! Please try again!\n")
        pass
