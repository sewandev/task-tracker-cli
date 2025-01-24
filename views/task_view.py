from validators.validators import validate_alphanumeric

def get_user_input() -> str:
    while True:
        _input = input("\nInput a task (use 'help' for all command list):\n").strip()
        if not _input:
            print("Input cannot be empty. Please try again.")
        elif not validate_alphanumeric(_input):
            print("Invalid command. Special characters are not allowed.")
        else:
            return _input.lower()

def want_continue() -> bool:
    while True:
        _input = input("\nDo you want to continue? (y/n): ").strip().lower()
        if _input == 'y':
            return True
        elif _input == 'n':
            display_message("Exiting app ...")
            return False
        else:
            display_message("Invalid input. Please enter 'y' for yes or 'n' for no.")
                
def display_message(message: str) -> None:
    print(message)

def show_tasks(tasks: list) -> None:
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']} | Desc: {task['description']} | Status: {task['status']} | Created: {task['createdAt']} | Updated: {task['updatedAt']}")
    else:
        print("No tasks available.")

def show_command_help() -> None:
    commands = {
        "add <description>": "Create a new task.",
        "update <id> <description>": "Update an existing task.",
        "delete <id>": "Delete an existing task.",
        "list": "List all tasks.",
        "exit": "Leave the program."
    }

    print("\nYou can use the following commands:")
    for command, description in commands.items():
        print(f"- {command}: {description}")