#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x = (0 - number) % 10
    x = 0 - x
else:
    x = number % 10
if number > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {x} and is 0")
else:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
