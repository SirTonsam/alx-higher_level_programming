#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        # Attempt to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle the case when the divisor is zero
        result = None
    finally:
        # Print the result using the specified format
        print("Inside result: {}".format(result))
    
    # Return the value of the result
    return result
