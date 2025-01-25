import re

def is_valid_alphanumeric(input_text: str) -> bool:
    try:
        alphanumeric_pattern  = r'^[a-zA-Z0-9\s\-]+$'
        if re.match(alphanumeric_pattern , input_text):
            return True
        return False
    except TypeError as error:
        print(f"Error validating input: {error}")
        return False

def validate_task_id(task_id: str) -> bool:
    try:
        return task_id.isdigit()
    except TypeError as e:
        print(f"Error validating task id: {e}")
        return False