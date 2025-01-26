import re

def is_valid_alphanumeric(input_text: str) -> bool:
    """Validates if the input text contains only alphanumeric characters, spaces, or hyphens."""

    if input_text is None:
        return False
    
    try:
        alphanumeric_pattern = r'^[a-zA-Z0-9\s\-]+$'
        return bool(re.match(alphanumeric_pattern, input_text))
    except TypeError as error:
        print(f"Error validating input: {error}")
        return False

def validate_task_id(task_id: str) -> bool:
    """Validates if the task ID is a positive integer."""

    try:
        return task_id.isdigit() and int(task_id) > 0
    except (TypeError, ValueError):
        return False

def validate_and_convert_task_id(task_id: str) -> int:
    """Validates and converts the task ID to an integer if it is a positive number."""

    if task_id.isdigit() and int(task_id) > 0:
        return int(task_id)
    raise ValueError("Task ID must be a positive integer.")

def validate_command_arguments(arguments: list, required_length: int) -> bool:
    """Validates if the command has the required number of arguments."""

    return len(arguments) >= required_length

def validate_task_status(status: str) -> bool:
    """Validates if the given status is one of the valid statuses."""
    
    valid_statuses = {"todo", "in-progress", "done"}
    return status.lower() in valid_statuses
