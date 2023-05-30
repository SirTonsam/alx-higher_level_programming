#!/usr/bin/python3

class Square:
    def __init__(self, size):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): Private instance attribute to store the size of the square.
        """
        self.__size = size


    def print_size(self):
        """
        Prints the size of the square.
        """
        print(self.__size)
