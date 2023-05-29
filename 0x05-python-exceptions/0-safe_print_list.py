#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0  # Variable to track the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end="")  # Print the element without a new line
            count += 1  # Increment the count of printed elements
    except IndexError:
        pass  # Ignore index errors when trying to access elements beyond the list length

    print()  # Print a new line after printing the elements
    return count  # Return the number of elements printed
