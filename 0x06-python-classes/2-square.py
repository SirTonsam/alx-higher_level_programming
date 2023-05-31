#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        # Check if size argument is an integer
        if type(size) != int:
            raise TypeError("size must be an integer")
        # Check if size argument is greater than or equal to 0
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            # Assign the size argument to the private attribute __size
            self.__size = size
