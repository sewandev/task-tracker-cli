from models.task_model import load_tasks, add_task, update_task, delete_task
from views.task_view import get_user_input, display_message, show_tasks, show_command_help, want_continue
from validators.validators import validate_task_id
import datetime

def _add_task(description: str):
    description = description.split(" ", 1)[1]
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

def _update_task(arguments: list):
    if len(arguments) > 2 and validate_task_id(arguments[1]):
        arguments = arguments.split(" ", 2)
        task_id = int(arguments[1])
        description = arguments[2] 
        tasks = load_tasks()
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            update_task(task)
            display_message("Task updated.")
        else:
            display_message("Task ID not found.")

def _delete_task(argument: str):
    task_id = validate_task_id(argument.split(" ")[1])
    task_id = int(task_id)
    if delete_task(task_id):
        display_message("Task deleted.")
    else:
        display_message("Task ID not found.")

def handle_task_action():
    try:
        command = get_user_input()

        if not command.startswith(("add", "update", "delete", "list", "exit", "help")):
            pass # Se dirigirá directamente al else con un mensaje de error. No se hace aqui para evitar imprimir dos mensajes iguales

        arguments = True if len(command.split()) > 1 else False

        if command.startswith("add") and arguments:
            _add_task(command)

        elif command.startswith("update") and arguments:
            _update_task(command) 

        elif command.startswith("delete") and arguments:
            _delete_task(command)

        elif command.startswith("list") and not arguments:
            tasks = load_tasks()
            show_tasks(tasks)

        elif command.startswith("help") and not arguments:
            show_command_help()

        elif command.startswith("exit") and not arguments:
            exit()
        
        else:
            display_message("Invalid command. Use: help for the list of commands")
    except KeyboardInterrupt:
        display_message("Exiting app...")
        exit()
    except Exception as e:
        display_message(f"Unexpected error: {e}")

def run():
    while True:
        handle_task_action()
        exit() if not want_continue() else True
