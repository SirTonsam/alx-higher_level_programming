#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a variable to keep track of the number of integers printed
    try:
        for i in range(x):  # Iterate over the first x elements of the list
            if isinstance(my_list[i], int):  # Check if the element is an instance of int
                print("{:d}".format(my_list[i]), end="")  # Print the integer without a new line
                count += 1  # Increment the count of integers printed
    except IndexError:
        pass  # Catch the IndexError if x is greater than the length of the list
    finally:
        print()  # Print a new line
        return count  # Return the count of integers printed
