#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print(f"{} is negative", number)
elif number == 0:
    print(f"{} is zero", number)
else:
    print(f"{} is positive", number)
