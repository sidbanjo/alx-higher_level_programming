#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print(f"Last digit of {} is {} and is greater than 5", number, number[-1])
elif number == 0:
    print(f"Last digit of {} is {} and is 0", number, number[-1])
else:
    print(f"Last digit of {} is {} and is less than 6 and not 0", number, number[-1])
