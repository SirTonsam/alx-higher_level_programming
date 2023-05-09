#!/usr/bin/python3
def uppercase(s):
    """Prints a string in uppercase"""
    new_s = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            new_s += chr(ord(c) - 32)
        else:
            new_s += c
    print("{:s}".format(new_s))
