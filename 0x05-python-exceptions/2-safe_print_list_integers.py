#!/usr/bin/python3

def safe_print_list_integers(lst=[], num=0):
    """Print the first num elements of a list that are integers.

    Args:
        lst (list): The list to print elements from.
        num (int): The number of elements of lst to print.

    Returns:
        The number of elements printed.
    """
    count = 0
    for i in range(0, num):
        try:
            print("{:d}".format(lst[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
