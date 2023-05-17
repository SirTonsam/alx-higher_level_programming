#!/usr/bin/python3
"""
Module containing the function delete_at
"""


def delete_at(my_list=[], idx=0):
    """ Deletes an item at a specific position in a list.

    Args:
        my_list (list): The list from which to delete the item.
        idx (int): The index of the item to delete.

    Returns:
        list: The updated list after deleting the
        item at the specified index."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
