#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
    my_list (list): A list of integers.

    Returns:
    int: The sum of all unique integers in the list.
    """

    unique_integers = set(my_list)
    sum_of_unique_integers = sum(unique_integers)


return sum_of_unique_integers
