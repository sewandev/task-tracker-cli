import re

def validate_alphanumeric(input: str) -> bool:
    try:
        pattern = r'^[a-zA-Z0-9\s\-]+$'
        if re.match(pattern, input):
            return True
        return False
    except TypeError as e:
        print(f"Error validating input: {e}")
        return False

def validate_task_id(task_id: str) -> bool:
    try:
        return task_id.isdigit()
    except TypeError as e:
        print(f"Error validating task id: {e}")
        return False