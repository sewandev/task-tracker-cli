from models.task_model import load_tasks, add_task, update_task, delete_task_by_id
from views.task_view import get_user_input, display_message, display_tasks, display_command_help, confirm_continue
from validators.validators import validate_command_arguments, validate_and_convert_task_id, validate_task_status, validate_task_id
import datetime

# Diccionario de comandos y sus funciones correspondientes
COMMAND_HANDLERS = {
    "add": "_process_add_task",
    "update": "_process_update_task",
    "delete": "_process_delete_task",
    "mark-in-progress": "_process_update_task_status",
    "mark-done": "_process_update_task_status",
    "list": "_process_list_tasks",
    "help": "_process_help_command",
    "exit": "_process_exit_command"
}

def _process_add_task(user_input: str):
    """Handles the 'add' command to create a new task."""
    if not validate_command_arguments(user_input.split(), 2):
        display_message("Invalid argument. Usage: add <description>")
        return

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

def _process_update_task(command_parts: list):
    """Handles the 'update' command to modify a task's description."""
    if not validate_command_arguments(command_parts, 3) or not validate_task_id(command_parts[1]):
        display_message("Invalid argument. Usage: update <id> <description>")
        return

    task_id = int(command_parts[1])
    tasks_list = load_tasks()
    task = next((t for t in tasks_list if t["id"] == task_id), None)

    if not task:
        display_message("Task ID not found.")
        return

    new_description = command_parts[2]
    task["description"] = new_description
    task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    update_task(task)
    display_message(f"Task {task_id} was updated with a new description: {new_description}.")

def _process_update_task_status(command_parts: list):
    """Handles the 'mark-in-progress' and 'mark-done' commands to update a task's status."""
    if not validate_command_arguments(command_parts, 2) or not validate_task_id(command_parts[1]):
        display_message("Invalid argument. Usage: mark-in-progress <id> or mark-done <id>")
        return

    task_id = int(command_parts[1])
    tasks_list = load_tasks()
    task = next((t for t in tasks_list if t["id"] == task_id), None)

    if not task:
        display_message("Task ID not found.")
        return

    new_status = "in-progress" if command_parts[0] == "mark-in-progress" else "done"
    task["status"] = new_status
    task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    update_task(task)
    display_message(f"Task {task_id} was updated with a new status: {new_status}.")

def _process_delete_task(command_input: str):
    """Handles the 'delete' command to remove a task."""
    try:
        task_id = validate_and_convert_task_id(command_input.split(" ")[1])
        if delete_task_by_id(task_id):
            display_message(f"Task with ID {task_id} deleted.")
        else:
            display_message("Task ID not found.")
    except ValueError as error:
        display_message(str(error))

def _process_list_tasks(user_command: str = ""):
    """Handles the 'list' command to display tasks."""
    tasks_list = load_tasks()
    if user_command and " " in user_command:
        _, status_filter = user_command.split(" ", 1)
        status_filter = status_filter.strip().lower()
        if validate_task_status(status_filter):
            filtered_tasks = [task for task in tasks_list if task["status"] == status_filter]
            if not filtered_tasks:
                display_message(f"No tasks found with status '{status_filter}'.")
            display_tasks(filtered_tasks)
        else:
            display_message(f"Invalid status filter: '{status_filter}'. Use: done, in-progress, or todo.")
    else:
        display_tasks(tasks_list)

def _process_help_command():
    """Handles the 'help' command to display available commands."""
    display_command_help()

def _process_exit_command():
    """Handles the 'exit' command to terminate the program."""
    display_message("Exiting app...")
    exit()

def process_command():
    """Processes the user command by delegating to the appropriate handler."""
    try:
        user_command = get_user_input()
        command_parts = user_command.split()
        if not command_parts:
            display_message("Invalid command. Use 'help' for the list of commands.")
            return

        command = command_parts[0]
        if command in COMMAND_HANDLERS:
            handler = globals()[COMMAND_HANDLERS[command]]
            if command in ("add", "delete", "list"):
                handler(user_command)
            elif command in ("update", "mark-in-progress", "mark-done"):
                handler(command_parts)
            else:
                handler()
        else:
            display_message("Invalid command. Use 'help' for the list of commands.")
    except KeyboardInterrupt:
        display_message("Exiting app...")
        exit()
    except Exception as error:
        display_message(f"Unexpected error: {error}")

def run():
    """Main loop to run the task manager application."""
    while True:
        process_command()
        if not confirm_continue():
            break