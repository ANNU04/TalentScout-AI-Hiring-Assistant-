import re

def validate_email(email):
    return re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email)

def validate_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone)

def is_exit_command(text):
    return text.strip().lower() in ["exit", "quit", "bye"]
    