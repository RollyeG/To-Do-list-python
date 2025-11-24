from task import Task
from task_manager import TaskManager

TaskApp = TaskManager()
option = 0
TaskApp.import_json()

print("Welcome to your task manager!")
while option != -1:
    option = int(input("1 to add task, 2 to remove task, 3 to see list, 4 to complete tasks -1 to exit: "))
    if option == 1:
        name = str(input("Name your task: "))
        prior = int(input("Set the task priority (1 to 3): "))
        new_task = Task(name, prior)
        added = TaskApp.add(new_task)
        if added:
            print("Task added succesfully!")
        else:
            print("Unable to add task")

    elif option == 2:
        name = str(input("Name the task to remove: "))
        removed = TaskApp.remove(name)
        if removed:
            print('Task removed succesfully!')
        else:
            print('Task not found')

    elif option == 3:
        print(TaskApp)
    
    elif option == 4:
        name = str(input("Name the task to complete: "))
        completed = TaskApp.complete(name)
        if completed:
            print('Task marked as completed succesfully!')
        else:
            print('Task not found')




TaskApp.save_json()

print("Thank you for using this service!")