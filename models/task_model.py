from views.task_view import display_message
import json
import os
from typing import Dict, Any, List

DATA_FOLDER = "data"
TASKS_FILE_PATH = os.path.join(DATA_FOLDER, "tasks.json")

def load_tasks() -> List[Dict[str, Any]]:
    try:
        if os.path.exists(TASKS_FILE_PATH):
            with open(TASKS_FILE_PATH, "r") as file:
                return json.load(file)
    except json.JSONDecodeError:
        display_message(f"Error: The file {TASKS_FILE_PATH} is corrupted. Starting with an empty task list.")
        return []
    except PermissionError:
        display_message(f"Error: You do not have permission to read the file {TASKS_FILE_PATH}.")
        return []
    except IOError as error:
        display_message(f"I/O error while trying to read {TASKS_FILE_PATH}: {error}")
        return []
    return []

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    try:
        os.makedirs(DATA_FOLDER, exist_ok=True)
        with open(TASKS_FILE_PATH, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as error:
        print(f"Error saving tasks: {error}")

def add_task(task: Dict[str, Any]) -> None:
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def update_task(updated_task: Dict[str, Any]) -> bool:
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == updated_task["id"]:
            tasks[i] = updated_task
            save_tasks(tasks)
            return True
    return False

def delete_task_by_id(task_id: int) -> bool:
    tasks_list = load_tasks()
    task_exists = any(task["id"] == task_id for task in tasks_list)
    if not task_exists:
        return False
    filtered_tasks = [task for task in tasks_list if task["id"] != task_id]
    save_tasks(filtered_tasks)
    return True
