#!/usr/bin/python3
#import the add function from module add-0
from add_0 import add

#avoid exercution of code when imported
if __name__ == "__main__":
    a=1
    b=2
    #print the result 
    print("{} + {} = {}".format(a,b,add(a,b)))
