from models.task_model import load_tasks, add_task, update_task, delete_task
from views.task_view import get_user_input, display_message, show_tasks, show_command_help, want_continue
import datetime

def valid_id(id: str) -> bool:
    try:
        float(id)
        return True
    except:
        return False

def handle_task_action():
    command = get_user_input()

    if not command.startswith(("add", "update", "delete", "list", "exit", "help")):
        pass # Se dirigirá directamente al else con un mensaje de error. No se hace aqui para evitar imprimir dos mensajes iguales

    arguments = True if len(command.split()) > 1 else False

    if command.startswith("add") and arguments:
        description = command.split(" ", 1)[1]
        tasks = load_tasks()
        new_id = max((task["id"] for task in tasks), default=0) + 1
        new_task = {
            "id": new_id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "updatedAt": "Not updated yet"
        }
        add_task(new_task)
        display_message(f"Task '{description}' added.")

    elif command.startswith("update") and arguments:
        command_args = command.split(" ", 2)  
        if valid_id(command_args[1]) and bool(command_args[2]): # Bug: "IndexError: list index out of range". When i put "update 1" without a description, the program fails and close it.
            task_id = int(command_args[1])
            description = command_args[2] 
            tasks = load_tasks()
            task = next((t for t in tasks if t["id"] == task_id), None)
            if task:
                task["description"] = description
                task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                update_task(task)
                display_message("Task updated.")
            else:
                display_message("Task ID not found.")

    elif command.startswith("delete") and arguments:
        task_id = int(command.split(" ")[1]) # Bug: "IndexError: list index out of range". When i put "delete" without a description, the program fails and close it.
        if delete_task(task_id):
            display_message("Task deleted.")
        else:
            display_message("Task ID not found.")

    elif command.startswith("list") and not arguments:
        tasks = load_tasks()
        show_tasks(tasks)

    elif command.startswith("help") and not arguments:
        show_command_help()

    elif command.startswith("exit") and not arguments:
        exit()
    
    else:
        display_message("Invalid command. Use: help for the list of commands")

def run():
    while True:
        handle_task_action()
        exit() if not want_continue() else True
