def get_user_input() -> str:
    return input("\nInput a task (add, update, delete, list):\n").strip().lower()

def display_message(message: str) -> None:
    print(message)

def show_tasks(tasks: list) -> None:
    if tasks:
        from json import dumps
        print(dumps(tasks, indent=4))
    else:
        print("No tasks available.")
