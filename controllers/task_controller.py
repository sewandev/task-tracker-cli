from models.task_model import load_tasks, add_task, update_task, delete_task_by_id
from views.task_view import get_user_input, display_message, display_tasks, display_command_help, confirm_continue
from validators.validators import validate_task_id
import datetime

def _process_add_task(user_input: str):
    task_description = user_input.split(" ", 1)[1]
    tasks_list = load_tasks()
    new_task_id = max((task["id"] for task in tasks_list), default=0) + 1
    new_task = {
        "id": new_task_id,
        "description": task_description,
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "updatedAt": "Not updated yet"
    }
    add_task(new_task)
    display_message(f"Task ID: {new_task_id} '{task_description}' added.")

def _process_update_task(arguments: list):
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

def _process_delete_task(argument: str):
    task_id = validate_task_id(argument.split(" ")[1])
    task_id = int(task_id)
    if delete_task_by_id(task_id):
        display_message("Task deleted.")
    else:
        display_message("Task ID not found.")

def _process_list_tasks(user_command: str):
    tasks_list = load_tasks()
    # Determine if a filter exists in the command
    if " " in user_command:
        _, status_filter = user_command.split(" ", 1)
        status_filter = status_filter.strip().lower()
        valid_statuses = {"done", "in-progress", "todo"}
        
        if status_filter in valid_statuses:
            # Filter tasks by status
            filtered_tasks = [task for task in tasks_list if task["status"] == status_filter]
            display_tasks(filtered_tasks)
        else:
            display_message(f"Invalid status filter: '{status_filter}'. Use: done, in-progress, or todo.")
    else:
        display_tasks(tasks_list)


def process_command():
    try:
        user_command = get_user_input()

        if not user_command.startswith(("add", "update", "delete", "list", "exit", "help")):
            pass

        has_arguments = True if len(user_command.split()) > 1 else False

        if user_command.startswith("add") and has_arguments:
            _process_add_task(user_command)

        elif user_command.startswith("update") and has_arguments:
            _process_update_task(user_command) 

        elif user_command.startswith("delete") and has_arguments:
            _process_delete_task(user_command)

        elif user_command.startswith("list"):
            _process_list_tasks(user_command)

        elif user_command.startswith(("mark-in-progress", "mark-done")) and has_arguments:
            _process_update_task(user_command)

        elif user_command.startswith("help") and not has_arguments:
            display_command_help()

        elif user_command.startswith("exit") and not has_arguments:
            exit()
        
        else:
            display_message("Invalid command. Use: help for the list of commands")
    except KeyboardInterrupt:
        display_message("Exiting app...")
        exit()
    except Exception as error:
        display_message(f"Unexpected error: {error}")

def run():
    while True:
        process_command()
        exit() if not confirm_continue() else True
