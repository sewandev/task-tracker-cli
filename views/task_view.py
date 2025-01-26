from validators.validators import is_valid_alphanumeric

def get_user_input() -> str:
    try:
        while True:
            user_input = input("\nEnter a task (use 'help' for the command list):\n").strip()
            if not user_input:
                display_message("Input cannot be empty. Please try again.")
            elif not is_valid_alphanumeric(user_input):
                display_message("Invalid input. Only alphanumeric characters, spaces, and hyphens are allowed.")
            else:
                return user_input.lower()
    except KeyboardInterrupt:
        display_message("Input interrupted. Exiting...")
        exit()

def confirm_continue() -> bool:
    try:
        while True:
            user_input = input("\nDo you want to continue? (y/n): ").strip().lower()
            if user_input == 'y':
                return True
            elif user_input == 'n':
                display_message("Exiting app ...")
                return False
            else:
                display_message("Invalid input. Please enter 'y' for yes or 'n' for no.")
    except KeyboardInterrupt:
        display_message("Exiting app...")
        exit()
                
def display_message(message: str) -> None:
    print(message)

def display_tasks(tasks_list: list) -> None:
    if tasks_list:
        for task in tasks_list:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created: {task['createdAt']} | Updated: {task['updatedAt']}")
    else:
        print("No tasks available.")

def display_command_help() -> None:
    command_descriptions = {
        "add <description>": "Create a new task.",
        "update <id> <description>": "Update an existing task.",
        "delete <id>": "Delete an existing task.",
        "mark-in-progress <id>": "Update an existing task with status in-progress.",
        "mark-done <id>": "Update an existing task with status done.",
        "list": "List all tasks.",
        "exit": "Leave the program."
    }

    print("\nYou can use the following commands:")
    for command, description in command_descriptions.items():
        print(f"- {command}: {description}")