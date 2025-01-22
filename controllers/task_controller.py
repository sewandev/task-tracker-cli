from models.task_model import load_tasks, add_task, update_task, delete_task
from views.task_view import get_user_input, display_message, show_tasks
import datetime

def handle_task_action():
    command = get_user_input()
    
    if not command.startswith(("add", "update", "delete", "list", "mark")):
        display_message("Invalid command. Use: add, update, delete, list.")

    if command.startswith("add"):
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

    elif command.startswith("update"):
        parts = command.split(" ", 2)
        task_id = int(parts[1])
        description = parts[2] # Bug: "IndexError: list index out of range". When i put "update 1" without a description, the program fails and close it.
        tasks = load_tasks()
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            update_task(task)
            display_message("Task updated.")
        else:
            display_message("Task ID not found.")

    elif command.startswith("delete"):
        task_id = int(command.split(" ")[1]) # Bug: "IndexError: list index out of range". When i put "delete" without a description, the program fails and close it.
        if delete_task(task_id):
            display_message("Task deleted.")
        else:
            display_message("Task ID not found.")

    elif command.startswith("list"):
        tasks = load_tasks()
        show_tasks(tasks)

    else:
        display_message("Invalid command.")

def run():
    while True:
        handle_task_action()
        option = input("Do you want to continue? (y/n): ").strip().lower()
        if option != "y":
            break
