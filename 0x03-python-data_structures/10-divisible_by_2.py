#!/usr/bin/python3
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

for i in range(len(list_result)):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
