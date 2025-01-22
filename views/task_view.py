def get_user_input() -> str:
    return input("\nInput a task (add, update, delete, list):\n").strip().lower()

def display_message(message: str) -> None:
    print(message)

def show_tasks(tasks: list) -> None:
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']} | Desc: {task['description']} | Status: {task['status']} | Created: {task['createdAt']} | Updated: {task['updatedAt']}")
    else:
        print("No tasks available.")
