#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if ord(value) in range(48, 57):
            return True
    except (TypeError, ValueError):
        return False
