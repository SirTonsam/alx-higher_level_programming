#!/usr/bin/python3
import sys

argv = sys.argv[1:]
num_args = len(argv)

print(f"{num_args} argument{'s' if num_args != 1 else ''}:")
if num_args > 0:
    for i, arg in enumerate(argv):
        print(f"{i+1}: {arg}")
