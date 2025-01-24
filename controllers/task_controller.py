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
    arguments = arguments.split(" ", 2)
    if len(arguments) < 2 or not validate_task_id(arguments[1]):
        display_message("Invalid argument.")
        return

    task_id = int(arguments[1])
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        display_message("Task ID not found.")
        return

    if len(arguments) > 2:  # Update description
        new_description = arguments[2]
        task["description"] = new_description
        task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        update_task(task)
        display_message(f"Task {task_id} was updated with a new description: {new_description}.")
    elif arguments[0] in ("mark-in-progress", "mark-done"):  # Update status
        new_status = "in-progress" if arguments[0] == "mark-in-progress" else "done"
        task["status"] = new_status
        task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        update_task(task)
        display_message(f"Task {task_id} was updated with a new status: {new_status}.")
    else:
        display_message("Invalid argument.")


def _delete_task(argument: str):
    task_id = validate_task_id(argument.split(" ")[1])
    task_id = int(task_id)
    if delete_task(task_id):
        display_message("Task deleted.")
    else:
        display_message("Task ID not found.")

def _list_tasks(command: str):
    tasks = load_tasks()
     # Determine if exist a filter in the command
    if " " in command:
        _, status_filter = command.split(" ", 1)
        status_filter = status_filter.strip().lower()
        valid_statuses = {"done", "in-progress", "todo"}
        
        if status_filter in valid_statuses:
            # Filter by status
            tasks = [task for task in tasks if task["status"] == status_filter]
        else:
            display_message(f"Invalid status filter: '{status_filter}'. Use: done, in-progress, or todo.")
            return
    show_tasks(tasks)

def handle_task_action():
    try:
        command = get_user_input()

        if not command.startswith(("add", "update", "delete", "list", "exit", "help")):
            pass

        arguments = True if len(command.split()) > 1 else False

        if command.startswith("add") and arguments:
            _add_task(command)

        elif command.startswith("update") and arguments:
            _update_task(command) 

        elif command.startswith("delete") and arguments:
            _delete_task(command)

        elif command.startswith("list"):
            _list_tasks(command)

        elif command.startswith(("mark-in-progress", "mark-done")) and arguments:
            _update_task(command)

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
