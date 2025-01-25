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
        print(f"Error: {TASKS_FILE_PATH} contains corrupted data. Initializing empty array.")
        return []
    except IOError as e:
        print(f"Error I/O to try read {TASKS_FILE_PATH}: {e}")
        return []
    return []

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    try:
        os.makedirs(DATA_FOLDER, exist_ok=True)
        with open(TASKS_FILE_PATH, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error al guardar las tareas: {e}")

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
    filtered_tasks = [task for task in tasks_list if task["id"] != task_id]
    save_tasks(filtered_tasks)
    return True
