#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to print the value as an integer using "{:d}".format()
        print("{:d}".format(value))
        return True  # Return True if printing is successful
    except (ValueError, TypeError):
        # Catch ValueError or TypeError exceptions if value is not an integer
        return False  # Return False if printing fails
