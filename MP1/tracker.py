from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data

    for task in tasks:
        if task['due'] is not None:
            task['due'] = str_to_datetime(task['due'])
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    """Name: Bhavya Shah; UCID: bs635; Date: 1 October, 2023"""
    task = TASK_TEMPLATE.copy()
    try: 
        #assigning the user input value to the attributes of task
        task['name'] = name
        task['due'] = str_to_datetime(due)
        task['description'] = description
        task['lastActivity'] = datetime.now()
        tasks.append(task)   #adding the new task to the list
        print("Task added successfully!")    #success message
    except ValueError as e:
        print(f"Task addition failed: {e}")  #failure message
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    try:
        if 0 <= index < len(tasks):
            task = tasks[index]
            print(f"Current Task Details for Task {index + 1}:") #Displaying the existing attributes of the task
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due']}")
            
            #Asking the user for the information for updation
            name = input("Enter the updated name of the task (Press Enter to keep current): ").strip()
            desc = input("Enter the updated description of the task (Press Enter to keep current): ").strip()
            due = input("Enter the updated due date (format: m/d/y H:M:S, Press Enter to keep current): ").strip()
            
            if not name and not desc and not due:
                print("No changes provided -> Task not updated!")  # no updates provided
            else:
                update_task(index, name=name, description=desc, due=due)
        else:
            print("Invalid task number.")  #failure message
    except Exception as e:
        print(f"An error occurred: {e} \nTask not updated")  #failure message with the error


def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    if 0 <= index < len(tasks):
        task = tasks[index].copy()   # finding task by 
        if name or description or due:
            task['name'] = name if name else task['name']  # Updating the attributes
            task['description'] = description if description else task['description']
            task['due'] = str_to_datetime(due) if due else task['due']
            task['lastActivity'] = datetime.now()
            tasks.pop(index)
            tasks.insert(index, task)
            print("Task updated successfully!")  # success message
        else:
            print("No changes provided -> Task not updated!")  # no updates provided
    else:
        print("Invalid task number -> Update unsuccesful")  # failure message
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    if 0 <= index < len(tasks):
        task = tasks[index].copy()   #finding task by index
        if task['done'] == False:
            task['done'] = datetime.now()
            tasks.pop(index)
            tasks.insert(index, task)
            print("Task marked as completed")  # success message
        else:
            print("Task is already completed") #if task is already marked done
    else:
        print("Invalid task number -> Task incomplete")  #failure message
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    if 0 <= index < len(tasks):
        task = tasks[index].copy() #finding task by index
        print(f"""
            [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
            Description: {task['description']} \n 
            Last Activity: {task['lastActivity']} \n
            Due: {task['due']}\n
            Completed: {task['done'] if task['done'] else '-'} \n
            """.replace('  ', ' '))
    else:
        print("Task not found! -> Enter valid task number") #failure message


def delete_task(index):
    """ deletes a task from the tasks list by index """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)   #deleting the task from list using index
        print(f"Task '{deleted_task['name']}' deleted succesfully.")  # Indicate which task was deleted
    else:
        print("Task not deleted! -> Enter valid task number") #failure message
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    _tasks = [task for task in tasks if not task['done']] # Select tasks that are not marked as done
    list_tasks(_tasks)  #passing it to list_tasks

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    time = datetime.now()   #current time
    
    #condition for finding overdue tasks
    _tasks = [task for task in tasks if not task['done'] and task['due'] is not None and task['due'] < time]
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    """Name: Bhavya Shah; ucid: bs635; Date: 1 October, 2023"""
    if 0 <= index < len(tasks):
        task = tasks[index].copy()        #finding task by index
        due_date = task['due']     #checking due_date
        
        if due_date is not None:
            current_time = datetime.now()
            time_difference = due_date - current_time   #difference

            if time_difference.total_seconds() > 0:
                days = time_difference.days   
                hours, remainder = divmod(time_difference.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"REMAINING: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
            else:
                overdue_time = abs(time_difference) #overdue task
                days = overdue_time.days
                hours, remainder = divmod(overdue_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"OVERDUE : {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")  
        else:
            print("Task does not have a due date.") #if there is no due date
    else:
        print("Invalid task number") #failure message

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()
