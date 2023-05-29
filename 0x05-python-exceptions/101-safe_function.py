#!/usr/bin/python3

import sys


def safe_print_list_integers(lst=[], num=0):
    count = 0
    for i in range(0, num):
        try:
            print("{:d}".format(lst[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
