import re

def validate_alphanumeric(input: str) -> bool:
    pattern = r'^[a-zA-Z0-9\s]+$'
    if re.match(pattern, input):
        return True
    return False