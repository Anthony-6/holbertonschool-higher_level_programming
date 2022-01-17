#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_int = isinstance(value, int)
        if value_int is True:
            print(value)
        return value_int
    except (TypeError, ValueError):
        return False
