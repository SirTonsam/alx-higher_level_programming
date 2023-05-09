#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of", number, "is", end=" ")

if number < 0:
    last_digit = (abs(number) % 10) * -1
else:
    last_digit = number % 10

if last_digit == 0:
    print("0 and is 0")
elif last_digit > 5:
    print(last_digit, "and is greater than 5")
else:
    print(last_digit, "and is less than 6 and not 0")
